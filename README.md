# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：117
- 分类分布：
  - Neural Scene Representations & Rendering: 34
  - Embodied / Robotics / AR Applications: 32
  - 3D Reconstruction & Multi-view Geometry: 26
  - Dynamic / 4D Reconstruction: 15
  - Geometry Foundation Models: 10
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **动态/4D 重建从“外观建模”走向“可导出几何与运动分解”**  
   多篇论文不再满足于动态高斯泼溅的外观渲染，而是强调几何可导出性与运动结构约束。MEMO（2611.34939）让每个高斯保持为有效表面元素，从高斯场逐帧导出网格；DynMF2（2611.34931）把运动分解为若干刚性 SE(3) 轨迹，用 EM 直接作用于 3D 点轨迹，背景视为相机运动，无需掩码；AnyCam4D（2611.34223）解决非针孔相机下原生 4D 高斯的朝向/尺寸恢复问题。共同指向：动态重建的表示正在被要求“既能渲染，又能解释运动、又能输出几何”。

2. **前馈几何基础模型与重建管线加速/压缩成为独立问题**  
   TACC（2611.34476）针对前馈潜在 NVS 的全局 token 上下文开销，提出目标感知压缩；FoundSurface（2611.34128）将 pointmap 与射线表示结合，从无位姿图像直接恢复连续表面；Where to Approximate（2611.33948）专门研究循环多视图重建中“在哪里做近似”以加速；Embodied-VGGT（2611.33964）在长序列重建中利用具身采集的重复几何线索保持可靠局部几何。趋势是：前馈/循环重建的瓶颈正从“能不能建”转向“算得起、跑得长、保得住局部精度”。

3. **机器人/具身应用对场景表示提出“功能性”需求，而非仅视觉保真**  
   MERLoc（2611.34932）把 3DGS 扫描转为稠密功能性参考记忆，用位姿邻近检索替代外观检索以应对动态环境；CADENCE（2611.34549）在协同高斯 SLAM 中分离“匹配发现”与“匹配如何更新地图”，用传感器锚定区域记忆和物理检查控制污染；Loop4D（2611.34199）面向机器人操作结果预测联合建模 RGB 与几何演化；CoWM（2611.34302）用共享潜在动态对齐人类视频与机器人动作。场景表示正被嵌入定位、SLAM、操作预测等闭环，评价标准从渲染指标扩展到定位鲁棒性、地图抗污染、动作可执行性。

4. **“理解/验证”类工作增多：从提出方法转向检验失败解释与定量运动学能力**  
   Plausible Is Not Proven（2611.34393）对单目深度失败原因标签做四类审计，发现多数“合理”解释经不起检验；QK-Bench（2611.33991）评测 MLLM 的定量运动学理解，指出语义正确可能掩盖定量错误；Where to Approximate（2611.33948）用配对干预分离近似误差的注入、传播与输出影响。趋势是：社区开始系统性质疑此前被默认接受的失败归因和表示假设，强调可验证性。

5. **跨视角/跨具身一致性成为表示设计的一等约束**  
   Who Is Ego?（2611.34489）利用 ego 相机在 exo 图像中的对极点几何关系做佩戴者识别与分割，并把任务扩展到机器人、动物、无人机；CoWM 用共享物体关系状态与具身特定上下文解耦跨具身动态；CADENCE 用重力、气压高度、观测质量等跨设备线索约束匹配。跨视角、跨设备的几何一致性正在从后处理问题前移为表示与检索的核心设计。

#### 技术路线观察

- **几何基础模型**：FoundSurface 与 Embodied-VGGT 代表两条不同路线。前者走“pointmap 先验 + 射线回归”的前馈通用表面重建，强调零样本泛化与连续表面；后者走“长序列全局优化 + 具身重复线索选择性保留”，强调漂移纠正与局部几何不被破坏。Who Is Ego? 则把冻结前馈 3D 重建模型（VGGT-Ω）转成无需训练的几何读出工具，说明基础模型正在被当作可组合的几何先验而非端到端替代品。

- **3D/4D 重建**：DynMF2 与 MEMO 都在用更强的结构先验约束欠定动态重建——前者用刚性运动分解与 EM，后者用逐高斯时间高斯核运动模型并保持表面有效性。AnyCam4D 从相机模型端突破，避免去畸变损失视场。OceanFix（2611.34155）则针对水下稀疏视角，用扩散修复 + 介质感知蒸馏补足欠约束区域。整体上，4D 重建的技术分叉在于：是强化运动/几何参数化（MEMO、DynMF2），还是强化成像模型与修复先验（AnyCam4D、OceanFix）。

- **神经场景表示与渲染**：WorldExpand（2611.34810）把单全景扩展重构为稀疏互补高分辨率全景观测的联合生成，用覆盖引导选视角 + 联合全景扩散减少冗余和长轨迹误差；Surf-Style（2611.34062）转向基于表面的外观模型以获得跨视角一致风格化；TACC 则承认前馈 NVS 的 token 预算问题并做目标感知压缩。渲染侧的关键词从“更高保真”扩展到“观测预算如何花”“token 如何按目标分配”“风格如何绑定表面”。

- **机器人/AR 应用**：MERLoc 与 CADENCE 都把 3DGS 当作可查询、可更新的记忆结构，而非仅渲染产物；Loop4D 把 4D VAE 与循环扩散 Transformer 用于操作结果预测，强调运动细节不被压缩模糊；OneOcean（2611.34925）提供数据驱动的海洋仿真基准，补齐海洋机器人评测；机器人触诊（2611.34670）用 Laplace–Beltrami 算子把估计与探索统一在曲面内蕴几何上。应用侧共同点是：场景表示必须对接传感器不确定性、任务闭环和真实扰动。

#### 值得优先阅读的论文

1. **MEMO（2611.34939）**：动态场景逐帧网格导出是 4D 重建中较少被直接解决的输出形态问题；其“每个高斯始终是有效表面元素”的约束若成立，会影响后续动态高斯几何化的设计思路。优先读以确认其网格质量、拓扑变化处理和大幅快速运动的定量表现。

2. **DynMF2（2611.34931）**：用 EM 直接从 3D 点轨迹做刚性运动分解、无需渲染与掩码，方法简洁且与主流可微渲染路线不同。优先读以判断其运动数量自适应机制（requery/merge/split）的鲁棒性和对跟踪器误差的敏感度。

3. **CADENCE（2611.34549）**：把“跨设备匹配发现”与“匹配如何更新地图”分离，并用多传感器线索和独立置信度控制贡献，是协同 SLAM 中较少见的系统性防污染设计。优先读以了解其几何验证、物理检查与置信度分配的具体耦合方式。

4. **Where to Approximate（2611.33948）**：不只提加速方法，而是用配对干预分析近似误差的注入与传播，并给出“早期空间近似 + key/value 池化 + 交错复用”的具体结论。优先读以获取可复用的循环重建加速分析框架。

5. **Plausible Is Not Proven（2611.34393）**：对失败原因标签做四类审计（标注一致性、盲评人类、定向编辑响应、训练信号价值），方法学价值高于单一模型改进。优先读以评估自身工作中失败归因的可信度，并借鉴其审计协议。

#### 可能的研究机会

- **动态高斯的“表面有效性”与“运动分解”结合**：MEMO 保持高斯为表面元素，DynMF2 用刚性运动分解约束点轨迹。可探索将刚性/分段刚性运动先验注入逐高斯运动模型，减少 MEMO 类方法在快速大幅运动下的轨迹拟合负担，同时用运动分割结果指导网格拓扑一致性。

- **前馈重建的“目标感知压缩”扩展到 4D/视频上下文**：TACC 按目标视角几何相关性

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-26T17:20:20-05:00
**Total number of papers:** 117
**Number of papers added in the latest update:** 38
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

#### 2026-11-25 - Who Is Ego? Scaling Cross-View Camera Wearer Identification and Segmentation beyond Humans

**Authors:** Yifan Jin, Zheng Zhang, Tianwen Qian, Dong Wang, Bo Zhao, Yanwei Fu, Yuqian Fu
**Links:** [abs](https://arxiv.org/abs/2611.34489) - [pdf](https://arxiv.org/pdf/2611.34489)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, feed-forward 3D reconstruction, 3D reconstruction, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Who Is Ego? Scaling Cross-View Camera Wearer Identification and Segmentation beyond Humans
- 作者：Yifan Jin, Zheng Zhang, Tianwen Qian, Dong Wang, Bo Zhao, Yanwei Fu, Yuqian Fu
- 出版日期：2026-11-25T14:48:48Z
- 分类：Geometry Foundation Models
- 链接：摘要页 https://arxiv.org/abs/2611.34489 ；PDF https://arxiv.org/pdf/2611.34489

### 一句话总结
论文将“谁是自我（ego）相机佩戴者”的跨视角识别与分割任务从人类扩展到机器人、车辆、动物和无人机，并构建 FindEgo-1M 数据集，提出基于几何关系（对极点）的 EgoRay-ZS 与 EgoRay 方法。

### 研究问题
给定同步的第三人称（exo）图像，第一人称（ego）图像只显示相机所见，却不说明相机由谁或何物携带。论文要回答“谁是 ego”：在候选对象中识别 ego 相机的佩戴者；并把空间范围从“选择给定候选掩码”扩展到“佩戴者分割”，同时包含缺失预测与 ego-exo 视角间的相互相机定位。研究对象也从人类扩展到机器人、车辆、动物和无人机。

### 核心思路/方法
- 利用几何关系：ego 相机投影到 exo 图像中的对极点（epipole）位于其佩戴者上或附近。
- EgoRay-ZS：首个把冻结的前馈 3D 重建模型 VGGT-$Ω$ 转为无需训练的佩戴者识别与分割方案；其几何读出按候选掩码或分割提议相对 ego 相机的角偏移与距离排序，并由相对位姿提供相互相机方向。
- EgoRay：在 FindEgo-1M 上通过位姿监督训练，并结合由候选掩码约束的无标签测试时自适应，形成完整模型。
- 数据集 FindEgo-1M：包含 116 万真实与模拟 ego-exo 图像对，覆盖 12 种佩戴者类型、17 个领域和 111 个测试设置。

### 主要贡献
- 将相机佩戴者识别扩展到非人类佩戴者，并扩展任务空间范围至佩戴者分割、缺失预测和跨 ego-exo 视角的相互相机定位。
- 构建 FindEgo-1M 大规模 ego-exo 数据集。
- 提出 EgoRay-ZS，无需任务特定训练即可进行佩戴者识别与分割；摘要称其在 TF2023 原始标签上达到 78.0% 识别准确率，而数据集训练的 PEN 报告为 52.9%。
- 提出 EgoRay，在 FindEgo-1M 的已见与未见设置上分别达到 87.1 和 77.7 的机会校正准确率；在匹配查询上，摘要称其分别比 GPT-6 Astra 高 31.6 和 21.3 个百分点，且运行速度快 18 倍。
- 摘要称将发布数据、代码和模型。

### 局限性
- 摘要未提供足够信息说明 FindEgo-1M 的构建细节、标注质量、真实与模拟数据比例及潜在偏差。
- 摘要未提供足够信息说明 EgoRay 的失败情形、对候选掩码质量的敏感性、计算资源需求与泛化边界。
- 摘要未提供足够信息说明与 GPT-6 Astra 对比的具体协议、匹配查询定义及统计显著性。
- 摘要未提供足够信息说明“机会校正准确率”的计算方式与不同测试设置下的细分结果。

### 阅读优先级
中。理由：论文涉及跨视角几何、3D 基础模型复用、佩戴者识别与分割，并声称构建百万级数据集和无需训练方案，主题具有明确研究价值；但当前仅有摘要与元数据，缺少实验细节、数据构建与局限说明，是否投入深入阅读需结合对 ego-exo 跨视角任务或几何基础模型应用的兴趣再判断。

</details>

<details>
<summary>Abstract</summary>

A first-person (ego) image reveals what a camera sees, but not who or what carries it. Given a synchronized third-person (exo) image, camera wearer identification asks who is ego: which candidate carries the ego camera? We extend this task beyond humans to robots, vehicles, animals, and drones, and broaden its spatial scope (where is ego) from selecting a provided candidate mask to wearer segmentation with absence prediction and mutual camera localization across ego-exo views. We introduce FindEgo-1M, comprising 1.16M real and simulated ego-exo pairs across 12 wearer types, 17 domains, and 111 test settings. Our approach exploits a geometric relation: the ego camera's projection into the exo image, i.e., the epipole, lies on or near its wearer. We introduce EgoRay-ZS, the first method to turn a frozen feed-forward 3D reconstruction model, VGGT-$Ω$, into a training-free solution for wearer identification and segmentation. Its geometric readout ranks candidate masks or segmentation proposals by angular offset and distance to the ego camera, while the relative pose provides mutual camera directions. We then develop the full EgoRay model through pose-supervised training on FindEgo-1M and label-free test-time adaptation constrained by candidate masks. Without task-specific training, EgoRay-ZS achieves 78.0% identification accuracy on TF2023's original labels, versus 52.9% reported for the dataset-trained PEN. On FindEgo-1M, EgoRay achieves state-of-the-art chance-corrected accuracy of 87.1 and 77.7 on seen and unseen settings. On matched queries, EgoRay also outperforms GPT-6 Astra by 31.6 and 21.3 points on seen and unseen settings, respectively, while running $18\times$ faster. Data, code, and models will be released.

</details>

#### 2026-11-25 - Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction

**Authors:** Yiheng Han, Ziang Chen, Zhuyong Fu, Yiqing Yin, Nan Ma
**Links:** [abs](https://arxiv.org/abs/2611.33964) - [pdf](https://arxiv.org/pdf/2611.33964)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** VGGT, robotics, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction
- 作者：Yiheng Han, Ziang Chen, Zhuyong Fu, Yiqing Yin, Nan Ma
- 出版日期：2026-11-25T08:28:45Z
- 分类：主分类 Geometry Foundation Models；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.33964 ；PDF https://arxiv.org/pdf/2611.33964 ；代码 https://github.com/Ang-Sheep/Embodied-VGGT

### 一句话总结
Embodied-VGGT 针对长序列重建中“纠正累积漂移”与“保持局部几何一致性”的矛盾，利用具身采集中的平台—环境几何与重复观测线索，在全局优化中选择性保留可靠的局部几何关系。

### 研究问题
长序列重建需要同时完成两件事：纠正累积漂移，并保持局部一致的几何。摘要指出，在机器人与自动驾驶场景中，具身采集会提供反复出现的平台—环境几何，以及场景结构与平台运动的重复观测；论文关注如何利用这些线索建立可靠的局部关系，并在全局精化过程中有选择地保留这些关系。摘要未提供足够信息说明现有方法在该问题上的具体失效模式分类或完整问题定义。

### 核心思路/方法
论文提出 Embodied-VGGT，核心是“建立可靠局部关系并在全局精化中选择性保留”。摘要给出的方法组成包括：
- Memory-Augmented Grounded Chunks（MAGC）：建立在 Scal3R 的全局上下文记忆之上，使用由预测地面几何导出的相对尺度参考来正则化测试时记忆更新，以促进跨 chunk 一致性，同时限制对可靠局部几何的改动。
- Superpoint Alignment（SA）：在空间区域之间平衡地面与非地面证据，用于估计 chunk 间平移。
- Cross-Loop Optimization（CL）：利用交错窗口间的几何与运动一致性选择连贯的 chunk 组；每组获得共享的 Sim(3) 校正，从而在全局优化中保留其内部相对变换。

### 主要贡献
- 提出 Embodied-VGGT，利用具身采集中的重复平台—环境几何线索，在全局精化中建立并选择性保留可靠局部关系。
- 设计 MAGC，将 Scal3R 的全局上下文记忆与预测地面几何导出的相对尺度参考结合，用于正则化测试时记忆更新。
- 设计 SA 与 CL 分别处理几何关系的稳健建立与保留；CL 通过交错窗口的几何和运动一致性选择 chunk 组，并以共享 Sim(3) 校正保留组内相对变换。
- 在五个公开驾驶基准上进行实验；在 KITTI Odometry 上报告平均绝对轨迹误差 7.30 m、Chamfer distance 2.67 m，并称在相同评估协议下相较最先进基线分别降低 46.8% 和 23.3%。
- 发布代码以促进可复现性。

### 局限性
摘要未提供足够信息说明方法局限性、失败场景、计算开销、对具身线索缺失时的鲁棒性，以及五个公开驾驶基准的具体名称与完整实验设置。摘要仅报告了 KITTI Odometry 上的两项指标，未提供其他基准的详细结果或消融实验信息。

### 阅读优先级
中。理由：论文主题聚焦长序列重建中的漂移纠正与局部几何保持，属于 Geometry Foundation Models 与具身/机器人应用的交叉方向；摘要给出了明确的方法组件和 KITTI Odometry 上的定量改进，并公开代码，对相关方向读者有参考价值。但摘要未提供足够信息判断其在非驾驶场景、具身线索不足场景中的泛化性，也未给出完整实验细节，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry. In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion. We present Embodied-VGGT, which exploits these cues to establish reliable local relationships and selectively preserve them during global refinement. Memory-Augmented Grounded Chunks (MAGC) builds on Scal3R's global context memory and uses relative scale references derived from predicted ground geometry to regularize test-time memory updates, encouraging cross-chunk consistency while limiting changes to reliable local geometry. Superpoint Alignment (SA) and Cross-Loop Optimization (CL) jointly address the robust establishment and preservation of geometric relationships. SA balances ground and non-ground evidence across spatial regions to estimate inter-chunk translation. CL uses geometric and motion consistency across interleaved windows to select coherent chunk groups, each receiving a shared Sim(3) correction that preserves its internal relative transformations during global optimization. Experiments on five public driving benchmarks demonstrate consistent and substantial improvements in long sequence reconstruction. On KITTI Odometry, Embodied-VGGT achieves a mean absolute trajectory error of 7.30 m and a Chamfer distance of 2.67 m, reducing these errors by 46.8% and 23.3% compared with the state-of-the-art baseline under same evaluation protocol. To facilitate reproducibility, we released our code: https://github.com/Ang-Sheep/Embodied-VGGT.

</details>

#### 2026-11-25 - Linear-Time Online Visual Geometry Transformer with Hybrid Architecture

**Authors:** Haoyu Kang, Pingzhi Li, Ruichen Zhang, Tianlong Chen
**Links:** [abs](https://arxiv.org/abs/2611.33650) - [pdf](https://arxiv.org/pdf/2611.33650)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Linear-Time Online Visual Geometry Transformer with Hybrid Architecture
- 作者：Haoyu Kang, Pingzhi Li, Ruichen Zhang, Tianlong Chen
- 出版日期：2026-11-25T02:17:32Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2611.33650) / [PDF](https://arxiv.org/pdf/2611.33650)

### 一句话总结
LinearVGGT 通过由 StreamVGGT 蒸馏得到的“Mamba2 + 稀疏注意力”混合架构，在保持在线多视图 3D 重建能力的同时，将长视频流推理的计算与延迟增长大幅压低。

### 研究问题
现有基于 Transformer 的 3D 重建模型（如 VGGT、π³）可直接从多输入视图预测相机、深度与点图；StreamVGGT 等因果注意力模型虽支持在线视频，但缓存全部历史 token，总计算随流长度呈二次增长。CUT3R、TTT3R 等循环模型以固定大小状态实现常数代价，却会逐步遗忘早期几何。论文要解决的是：在线长视频流场景下，如何兼顾长程几何记忆与线性时间/近常数延迟。

### 核心思路/方法
- 提出 LinearVGGT，一个从 StreamVGGT 蒸馏而来的混合架构模型。
- 在每四个全局层中，三层使用 Mamba2 层进行高效序列建模。
- 剩余层使用 register-guided sparse attention，检索少量相关历史帧，以补偿 Mamba2 在精确长程召回上的不足。
- 蒸馏训练仅需 StreamVGGT 从 VGGT 学习时所用 GPU 小时的 9% 和训练帧数的 31%。

### 主要贡献
- 架构上融合 Mamba2 与 register-guided sparse attention，形成线性时间在线视觉几何 Transformer。
- 蒸馏效率显著：仅用 9% GPU 小时、31% 训练帧数。
- 在 1,024 帧上保持约 27 ms/帧的近常数延迟，平均比 StreamVGGT 快 12 倍。
- 性能超过其教师模型 StreamVGGT；与当时最优流式模型 LingBot-Map 相比有竞争力，同时快 2.5 倍、内存少 2.7 倍。

### 局限性
摘要仅给出总体延迟、加速比与内存对比，未提供具体数据集、评价指标数值、失败场景或消融细节；相关实验设置与误差分析“摘要未提供足够信息”。此外，稀疏注意力仅检索“少量”历史帧，是否在极端长程或复杂几何场景下受限，摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接针对在线长视频 3D 重建中“二次计算增长 vs. 早期几何遗忘”的核心矛盾，给出线性时间混合架构，并在摘要中报告了明确的效率与性能对比；对关注流式 3D 重建、几何基础模型和高效序列建模的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Transformer-based 3D reconstruction models such as VGGT and $π^3$ predict cameras, depth and point maps directly from many input views. Causal attention models such as StreamVGGT extend them to online video but cache all past tokens, so their total compute grows quadratically with the stream length. Recurrent models such as CUT3R and TTT3R keep a fixed-size state at constant cost, but they progressively forget early geometry. We present LinearVGGT, a hybrid model distilled from StreamVGGT, which uses Mamba2 layers for efficient sequence modeling in three of every four global layers. The remaining layers use register-guided sparse attention to retrieve a few relevant past frames, compensating for the limited exact long-range recall of Mamba2. Our distillation needs only 9\% of the GPU hours and 31\% of the training frames that StreamVGGT uses to learn from VGGT. LinearVGGT keeps an almost constant latency of 27 ms per frame over 1,024 frames and is on average $12 \times$ faster than StreamVGGT. It outperforms its teacher and is competitive with the state-of-the-art streaming model LingBot-Map, while running $2.5\times$ faster and using $2.7\times$ less memory.

</details>

#### 2026-11-24 - FocusAnchor: Zero-Shot Metric Depth by Anchoring a Depth Foundation Prior to Focus Cues

**Authors:** Ashkan Ganj, Hang Su, Tian Guo
**Links:** [abs](https://arxiv.org/abs/2611.32970) - [pdf](https://arxiv.org/pdf/2611.32970)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FocusAnchor: Zero-Shot Metric Depth by Anchoring a Depth Foundation Prior to Focus Cues
- 作者：Ashkan Ganj, Hang Su, Tian Guo
- 出版日期：2026-11-24T17:07:24Z
- 分类：Geometry Foundation Models
- 链接：摘要页面 https://arxiv.org/abs/2611.32970 ；PDF https://arxiv.org/pdf/2611.32970

### 一句话总结
FocusAnchor 是一个循环模型：它通过查询聚焦体积（focus volume）来细化度量深度，并反复把冻结基础模型给出的相对深度先验与当前深度估计对齐，再把对齐后的先验作为反馈来引导后续细化。

### 研究问题
现有 depth-from-focus 方法在聚焦线索较弱、新相机或焦切片较少时可能表现不佳。论文希望在这些条件下仍能获得可靠的零样本度量深度，并支持跨相机迁移和更实用的移动端采集。

### 核心思路/方法
- 采用循环模型，利用 focus-volume lookups 来细化度量深度。
- 将冻结的基础模型产生的相对深度先验反复对齐到当前深度估计；对齐后的先验进入反馈回路，用于引导后续细化。
- 该反馈机制把从纹理区域恢复出的度量尺度带入聚焦线索较弱的区域，同时保留场景结构。
- 为支持跨相机迁移，合成训练堆栈时随机化相机参数和焦距。
- 针对堆栈合成在不同切片间对图像噪声产生不同模糊、从而在无纹理表面制造人工深度线索的问题，加入逐切片独立噪声来抑制这些线索。
- 引入 variable-stack 训练以提升焦切片较少时的鲁棒性；对应变体为 FocusAnchor-flex。

### 主要贡献
- 提出 FocusAnchor，通过将冻结深度基础先验锚定到聚焦线索上，进行零样本度量深度估计。
- 设计反馈式对齐与细化循环，将纹理区域恢复的度量尺度传播到弱聚焦线索区域并保持场景结构。
- 通过随机化相机参数与焦距的堆栈合成支持跨相机迁移，并用逐切片独立噪声抑制合成产生的人工深度线索。
- 提出 variable-stack 训练及 FocusAnchor-flex，以改善少焦切片场景下的鲁棒性并支持更实用的移动采集。
- 摘要报告的对比结果：相比 FOSSA ViT-B，微调后 NYU Depth V2 上 AbsRel 降低 36%，DDFF-12 上降低 9%；零样本评估中 FocusAnchor 与 FocusAnchor-flex 在全部五个基准上取得最低的两个 AbsRel；ZEDD 测试上 FocusAnchor 比最佳竞争方法 FOSSA ViT-B 的 AbsRel 低 9%，FocusAnchor-flex 在 ZEDD 验证上用少 40% 的焦切片取得更低 AbsRel。

### 局限性
- 摘要未提供足够信息说明方法在极端无纹理场景、真实移动端噪声条件或更多相机类型上的具体表现。
- 摘要未提供足够信息说明计算开销、实时性、内存占用和模型规模。
- 摘要未提供足够信息说明五个零样本基准的具体构成、评测协议细节及失败案例分析。
- 摘要未提供足够信息说明对基础模型选择的依赖程度及更换基础模型后的影响。
- 摘要未提供足够信息说明逐切片独立噪声与 variable-stack 训练各自的消融贡献。

### 阅读优先级
中。理由：论文聚焦零样本度量深度、聚焦线索弱时的鲁棒性、跨相机迁移和少焦切片采集，问题定位清晰且摘要给出了多基准定量结果；但摘要未展开实验细节、计算成本和失败条件，是否高优先级取决于读者对 depth-from-focus、深度基础模型先验融合及移动端深度采集的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：X-3DComposer: Feed-Forward 3D Scene Composition with Any Assets from Any Views
- 作者：Zidian Qiu, Ancong Wu
- 出版日期：2026-11-24T12:16:40Z
- 分类：Geometry Foundation Models
- 链接：[摘要](https://arxiv.org/abs/2611.32491) / [PDF](https://arxiv.org/pdf/2611.32491)

### 一句话总结
X-3DComposer 将布局预测与资产生成分离，利用多视角几何模型把每个待摆放资产视为额外视角，从场景图像、对象掩码和任意来源资产出发，单次前向约一秒联合预测所有对象的旋转、平移与逐轴缩放。

### 研究问题
从图像组合可编辑 3D 场景需要两类要素：每个对象的资产，以及放置这些资产的布局。论文指出，3D 生成与 CAD 检索已能提供资产，但布局仍缺乏通用方案：场景生成方法将布局与生成耦合；姿态估计器一次只处理一个对象，且依赖真实尺寸 CAD 模型、深度或迭代优化。因此核心问题是：能否在不依赖上述限制的情况下，单独、通用地预测多对象场景布局。

### 核心思路/方法
方法将对象视为“视角”：对每个对象的资产进行渲染，把渲染图与场景图像一起输入一个由 VGGT-$\Omega$ 适配而来的多视角几何模型；随后根据该模型为各对象渲染预测出的相机，以闭式方式解出每个对象的姿态。输入包括场景的一幅或多幅图像、对象掩码，以及来自任意来源的每个对象资产；相机内参、相机位姿和深度为可选输入。模型为前馈式，单次前向约一秒，联合预测所有对象的旋转、平移和逐轴缩放。

### 主要贡献
- 提出 X-3DComposer，将布局预测与资产生成分离的前馈场景组合模型。
- 将对象资产渲染视为多视角输入，借助多视角几何模型预测渲染相机，并以闭式方式得到对象姿态。
- 支持任意来源资产与任意视角输入，相机内参、位姿和深度为可选，不要求真实尺寸 CAD 模型或迭代优化。
- 在固定五种场景生成方法所产生网格、仅替换布局的条件下，其布局比这些方法的原生布局更准确。
- 与独立布局模型 SceneMaker 相比，在 IndoorMix（来自六个室内数据集的测试集）上将场景级 Chamfer 距离降低 52%，在 3D-FUTURE 上降低 28%。

### 局限性
摘要未提供足够信息说明方法对掩码质量、资产渲染质量或极端遮挡的敏感性；摘要未提供足够信息说明失败案例、计算资源需求、泛化到室外或非室内场景的表现；摘要未提供足够信息给出五种场景生成方法的逐项结果、消融实验细节及可选输入缺失时的性能变化。

### 阅读优先级
中。理由：论文聚焦 3D 场景布局这一明确且具通用性的子问题，提出前馈、约一秒、支持任意资产与任意视角的方案，并在摘要中给出相对 SceneMaker 的量化改进；但摘要未提供实验细节、失败模式与更广泛场景的验证信息，适合作为 3D 场景组合与多视角几何应用方向的跟踪阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MaskedVGGT: Masked Multi-View Transformers Are Scalable 3D Learners
- 作者：Zichen Zou, Xiaosong Jia, Wen-Ming Chen, Zuxuan Wu, Yu-Gang Jiang
- 出版日期：2026-11-24T09:55:49Z
- 分类：主分类 Geometry Foundation Models；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.32297 ；PDF https://arxiv.org/pdf/2611.32297

### 一句话总结
MaskedVGGT 冻结强预训练 2D 编码器，仅以掩码自蒸馏方式预训练新增的多视图 Transformer，从而在不依赖几何标注的情况下学习跨视图交互，并在实验中优于同数据、同架构、同优化更新总量的单阶段监督 VGGT-$Ω$ 训练以及 E-RayZer、CroCo、MuM、Muskie。

### 研究问题
多视图前馈模型扩展性强，但依赖昂贵的几何标注，限制了数据规模扩展。现有 3D 自监督方法（如 CroCo、MuM、Muskie 的跨视图补全，或 RayZer、E-RayZer 的新视图合成）通常联合学习图像表示与跨视图交互。论文质疑：3D 预训练是否有必要从零学习单图像表示；这样做无法利用 2D 基础模型（如 DINO、CLIP、前沿 VLM）的持续进展。

### 核心思路/方法
- 冻结一个强预训练 2D 编码器，只预训练一个新增的、随机初始化的多视图 Transformer，专注学习跨视图交互。
- 通过掩码自蒸馏进行无标注预训练：学生模型基于完整锚视图与重度掩码的其余视图，预测被掩码位置的目标；指数滑动平均（EMA）教师模型基于未掩码输入提供预测目标。
- 强调一种“学习分工”：复用 2D 预训练获得的强图像表示，同时从无标注多视图数据中学习跨视图交互，不依赖几何标注。

### 主要贡献
- 提出 MaskedVGGT，将 3D 预训练的重点从单图像表示学习转向跨视图交互学习，并复用冻结的 2D 基础模型编码器。
- 设计无标注的掩码自蒸馏预训练框架，学生预测掩码位置目标、EMA 教师基于未掩码输入提供目标。
- 实验覆盖至 1B 参数规模：MaskedVGGT 预训练后微调，在相同训练数据、模型架构和总优化更新次数下，优于单阶段监督 VGGT-$Ω$ 训练；也优于 E-RayZer、CroCo、MuM、Muskie。
- 摘要称，用额外无标注视频扩展预训练可进一步提升泛化，且所学表示可迁移到多样下游任务。

### 局限性
- 摘要未提供足够信息说明具体下游任务清单、评价指标与量化迁移结果。
- 摘要未提供足够信息说明“额外无标注视频”的规模、来源、筛选方式及数据泄漏控制。
- 摘要未提供足够信息说明冻结 2D 编码器的具体模型、参数量配置与消融实验细节。
- 摘要未提供足够信息说明计算成本、训练时长、显存需求及与基线在算力上的对齐情况。
- 摘要未提供足够信息说明失败案例、适用场景边界及对 2D 编码器质量的敏感程度。

### 阅读优先级
高。理由：该工作直接回应 3D 预训练是否应从零学习图像表示这一关键问题，提出“冻结 2D 编码器 + 仅训练多视图 Transformer”的清晰分工，并在摘要中给出至 1B 参数规模、与监督 VGGT-$Ω$ 及多种 3D 自监督基线在同等训练条件比较的结论；若关注无几何标注的可扩展 3D 预训练与 2D 基础模型复用，该论文具有较高参考价值。

</details>

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

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-25 - DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation

**Authors:** Agelos Kratimenos, Yile Hua, Kostas Daniilidis
**Links:** [abs](https://arxiv.org/abs/2611.34931) - [pdf](https://arxiv.org/pdf/2611.34931)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, view synthesis, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynMF2: Rigid Motion Factorization by Expectation-Maximization for Monocular 4D Reconstruction and Motion Segmentation
- 作者：Agelos Kratimenos, Yile Hua, Kostas Daniilidis
- 出版日期：2026-11-25T18:59:14Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.34931) / [PDF](https://arxiv.org/pdf/2611.34931)

### 一句话总结
DynMF2 将单目视频中的场景运动分解为若干条刚性的 SE(3) 轨迹，并令每个点只跟随其中一条，通过 Expectation-Maximization（EM）直接从 3D 点轨迹中完成分解，无需渲染与掩码。

### 研究问题
单目随意拍摄的视频对运动场景的重建是欠定的：一个点从每个位置只被看到一次时，它沿相机方向滑动仍可能匹配每一帧。论文试图用运动本身的结构来约束重建，并解决如何在没有掩码的情况下把场景运动分解为刚性运动、同时支持视图合成与运动分割的问题。

### 核心思路/方法
- 以 DynMF 为基础，将场景运动建模为少量刚性 SE(3) 轨迹，每个点单独跟随其中一条，不做混合。
- 直接从 3D 点轨迹出发，用 EM 计算分解，不依赖渲染：M 步以闭式解为分配给某运动的点拟合该刚性运动；E 步将每个点重新分配给解释误差最小的运动。
- 背景被视为“相机自身的运动”，因此不需要掩码。
- 用三种工具修正分解：requery 在渲染显示跟踪器遗漏部分时补充轨迹；merge 合并一起运动的运动；split 分离不一起运动的运动。运动数量因此随场景自适应。

### 主要贡献
- 提出基于 EM、直接从 3D 点轨迹进行刚性运动分解的方法，无需渲染与掩码。
- 将背景统一为相机运动，避免依赖掩码。
- 引入 requery、merge、split 三种工具修正分解，使运动数量由场景决定。
- 摘要报告：在 iPhone 与 NVIDIA 数据集上，无掩码的 DynMF2 在视图合成上明显优于基于掩码的基线；在 iPhone 的 3D 跟踪上同样优于基线；能恢复掩码遗漏的细薄部件、细节和背景远处的小运动物体。
- 在 MOVi-F 与 iTACO 场景上取得有竞争力的运动分割结果，尽管模型从未被训练用于分割。

### 局限性
- 摘要未提供足够信息说明计算成本、实时性、对跟踪器质量的依赖程度及失败场景。
- 摘要未提供足够信息说明 merge/split/requery 的具体触发阈值与超参数敏感性。
- 摘要未提供足够信息说明在非刚性形变显著场景中的表现。
- 摘要未提供足够信息给出各数据集上的具体量化指标与消融实验细节。

### 阅读优先级
高。理由：该工作直接针对单目 4D 重建中的欠定性与运动分解问题，提出无需掩码、无需渲染的 EM 分解框架，并同时覆盖视图合成、3D 跟踪与运动分割三类任务；摘要声称在多个数据集上优于基于掩码的基线，且运动数量自适应，具有较强的方法论意义与后续对比价值。

</details>

<details>
<summary>Abstract</summary>

A single casual video leaves a moving scene under-determined: a point seen once from each place can slide toward or away from the camera and still match every frame. We constrain the reconstruction with the structure of the motion itself. Building on DynMF, we model a scene's motion as a handful of SE(3) trajectories, each rigid, and let every point follow one of them alone, never a blend. DynMF2 computes this factorization directly from 3D point trajectories, with no rendering, by Expectation-Maximization (EM). Its M-step fits, in closed form, every rigid motion to the points assigned to it, and its E-step reassigns every point to the motion that explains it with the least error. The background is simply one more motion, the camera's, so no masks are needed. Three tools then revise the factorization: requery adds trajectories where the rendering shows parts the tracker missed, merge joins motions that move together, and split separates those that do not. Thus the number of motions follows the scene. Without masks, DynMF2 clearly outperforms the mask-based baselines in view synthesis on iPhone and NVIDIA and in 3D tracking on iPhone. It recovers what masks leave out, from thin parts and details to small movers far in the background. Its motions segment the moving parts of MOVi-F and iTACO scenes competitively, although DynMF2 is never trained to segment. What moves in a scene is not decided in advance: it emerges from the rigid motions themselves.

</details>

#### 2026-11-25 - AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models

**Authors:** Sascha Kirch, Rafael Pagés, Jan Ondřej, Clara Pérez-Molina, Sergio Martin
**Links:** [abs](https://arxiv.org/abs/2611.34223) - [pdf](https://arxiv.org/pdf/2611.34223)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models
- 作者：Sascha Kirch, Rafael Pagés, Jan Ondřej, Clara Pérez-Molina, Sergio Martin
- 出版日期：2026-11-25T11:47:58Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.34223) / [PDF](https://arxiv.org/pdf/2611.34223)

### 一句话总结
AnyCam4D 提出一种基于光线光栅化的原生 4D 高斯训练与渲染方法，使动态高斯泼溅可直接使用原始非针孔相机影像，避免先去畸变造成的视场或细节损失。

### 研究问题
论文指出现有动态高斯泼溅大多假设相机为针孔模型，因此通常需要先对广角或鱼眼等真实相机 footage 去畸变，这会损失视场或细节。静态高斯泼溅已通过光线渲染适配任意相机，但原生 4D 高斯在时空建模中难以直接从协方差可靠恢复每个高斯的朝向和尺寸，因此不能直接沿用该方案。

### 核心思路/方法
AnyCam4D 在原始影像上训练原生 4D 高斯，并通过基于光线的光栅化进行渲染，以保留视场和分辨率，且每步开销约与标准投影相当。关键贡献是提出一种数值稳定的方式获取高斯朝向和尺寸：对 4D 协方差的一个平方根进行条件化处理。训练后的模型可通过其他相机渲染，包括滚动快门、景深或色差等效果。

### 主要贡献
- 提出 AnyCam4D，使原生 4D 高斯可直接在原始非针孔相机影像上训练与渲染，避免先去畸变。
- 提出数值稳定的方法，通过对 4D 协方差平方根进行条件化，获得高斯的朝向和尺寸。
- 采用基于光线的光栅化，保留视场与分辨率，且每步成本约与标准投影相当。
- 摘要报告：在合成的 170 度鱼眼相机上，用原始图像训练使 PSNR 提升 3.0–8.1 dB；在真实影像上，相比适配各相机的标准投影，AnyCam4D 在可比 PSNR 下具有更低感知误差，且无需相机特定推导；当合成相机相对采集 rig 视角旋转 60–80 度时，相对真值领先 6.2 dB。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算资源需求、对极端相机模型的适用范围、真实数据规模或与其他动态高斯方法的完整定量对比。

### 阅读优先级
高。理由：该论文直接针对动态 4D 高斯与任意相机模型之间的关键不兼容问题，提出原生 4D 高斯的光线渲染与数值稳定朝向/尺寸恢复方案，并给出鱼眼、真实影像及大视角旋转下的定量结果；对动态重建、非针孔相机渲染和 4D 高斯表示相关研究具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Real cameras are not pinholes, yet most dynamic Gaussian splatting assumes they are. Footage is therefore undistorted first, losing field of view or detail, especially with wide-angle and fisheye cameras. Static Gaussian splatting has largely solved this with ray-based rendering, which suits any camera. Native 4D Gaussians, which model motion in space-time, cannot use it directly: each Gaussian's orientation and size cannot be recovered reliably from its covariance. We present AnyCam4D, which trains native 4D Gaussians on original footage by ray-based rasterization, preserving field of view and resolution at about the per-step cost of standard projection. Our key contribution is a numerically stable way to obtain orientation and size: we condition a square root of the 4D covariance. Trained models render through other cameras, with rolling shutter, depth of field or chromatic aberration. With a synthetic 170-degree fisheye camera, training on original images improves peak signal-to-noise ratio (PSNR) by 3.0-8.1 dB. On real footage, AnyCam4D has lower perceptual error than the standard projection adapted to each camera, at comparable PSNR and without camera-specific derivations. With the synthetic camera rotated 60-80 degrees away from the capture rig's view, it leads by 6.2 dB against ground truth.

</details>

#### 2026-11-25 - Recall4D: Forgetting, Not Misalignment, Limits Long-Horizon Feed-Forward 4D Reconstruction

**Authors:** Tianle Lyu
**Links:** [abs](https://arxiv.org/abs/2611.33655) - [pdf](https://arxiv.org/pdf/2611.33655)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Recall4D: Forgetting, Not Misalignment, Limits Long-Horizon Feed-Forward 4D Reconstruction
- 作者：Tianle Lyu
- 出版日期：2026-11-25T02:22:11Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.33655) / [PDF](https://arxiv.org/pdf/2611.33655)

### 一句话总结
论文指出长视频中前馈 4D 跟踪器性能退化的主因是“遗忘”，而非窗口间对齐错误，并提出无需训练的 Recall4D 框架以持久世界状态和稀疏运动锚点缓解该问题。

### 研究问题
前馈 4D 跟踪器可从短片段恢复相机运动、深度和点轨迹，但在长视频上逐个窗口串联时精度会下降。论文检验的关键问题是：这种退化究竟源于窗口间对齐，还是其他机制。

### 核心思路/方法
- 诊断发现：用真实变换替换窗口间对齐后，跟踪误差基本不变；静态点误差随时间距上次观测的增长而增大，反复从已不再观测该点的窗口预测静态点会破坏已恢复几何，作者称之为“遗忘”。
- 简单验证：仅保留未见点的最后观测位置，即可在 PointOdyssey 上将误差降低 26%，且不修改跟踪器。
- Recall4D：训练无关框架，为冻结跟踪器增加持久世界状态与稀疏运动锚点。
  - 静态点：在相机视野外保留其世界空间位置；在视野内时，通过稀疏关键帧解码的观测平均进行细化。
  - 动态物体：跟踪器解码稀疏代表性锚点，再用几何蒙皮将其位移传播到稠密查询。

### 主要贡献
- 识别并命名长时程 4D 重建中的“遗忘”失效模式，并给出与窗口间错位不同的归因证据。
- 提出训练无关的 Recall4D，在不修改冻结跟踪器的前提下提升精度，并在两个长时程基准上运行速度提升 7.6–9.0 倍。
- 报告其精度增益可迁移到另外五个骨干和三个其他长序列任务，体现通用性。

### 局限性
摘要未提供足够信息。未说明具体基准名称、误差指标定义、失败场景、计算与存储开销细节，也未给出不同骨干或任务上的定量结果。

### 阅读优先级
中。理由：论文对长时程 4D 重建的失效原因给出了清晰且可操作的诊断，方法训练无关、具速度优势并声称跨骨干泛化，对相关方向有参考价值；但仅凭摘要无法核实实验细节与适用边界，需阅读全文后再判断其影响强度。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 4D trackers recover camera motion, depth, and point trajectories from short video clips, but chaining windows over long videos degrades their accuracy. We find that replacing inter-window alignment with ground-truth transforms leaves tracking error essentially unchanged. Static-point error instead grows with time since last observation: repeatedly predicting a static point from windows that no longer observe it corrupts previously recovered geometry. We call this failure forgetting. Merely retaining the last observed positions of unseen points reduces error by 26% on PointOdyssey without modifying the tracker. We introduce Recall4D, a training-free framework that augments a frozen tracker with a persistent world state and sparse motion anchors. Static points retain their world-space positions outside the camera view and are refined by averaging observations decoded at sparse keyframes while in view. For dynamic objects, the tracker decodes sparse representative anchors, while geometric skinning propagates their displacements to dense queries. Across two long-horizon benchmarks, Recall4D improves the accuracy of its backbone while running 7.6-9.0$\times$ faster, and its accuracy gains carry over to five further backbones and three other long-sequence tasks, demonstrating its generality.

</details>

#### 2026-11-24 - VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians

**Authors:** Shihang Wei, Yichi Zhang, Fengqing Zhu
**Links:** [abs](https://arxiv.org/abs/2611.33374) - [pdf](https://arxiv.org/pdf/2611.33374)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VersionGS: Compact and Motion-Robust Dynamic Gaussian Splatting via Versioned Gaussians
- 作者：Shihang Wei, Yichi Zhang, Fengqing Zhu
- 出版日期：2026-11-24T20:03:06Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33374)｜[PDF](https://arxiv.org/pdf/2611.33374)

### 一句话总结
VersionGS 用“版本化高斯”直接编码每帧高斯状态，仅以运动估计指导重建，从而在快速运动场景下提升重建质量并显著降低存储。

### 研究问题
现有动态高斯泼溅方法要么把时间变化编码为时间的平滑函数，要么编码为帧间约束更新；摘要指出，这类方法在快速运动下重建质量显著下降。在具有挑战性的舞蹈序列中，其高运动帧的 PSNR 相比低运动帧下降 1.1–4.0 dB。论文要解决的核心问题是：如何在快速运动下保持动态重建质量，同时控制存储开销与播放效率。

### 核心思路/方法
- 直接编码逐帧高斯状态，而不是依赖时间函数或帧间约束更新；运动估计仅用于指导重建。
- 在每组帧内维护共享字典：未变化的高斯保留当前版本，被修改的高斯作为新版本追加。
- 引入选择性顺序构建：根据光流、图像差异或渲染误差选择需要细化的高斯，其余保持不变，以提高版本复用。
- 对字典进行剪枝，并用模拟量化进行微调，最后编码为图像。
- 通过调整剪枝比例，可在不重建字典的情况下权衡存储与质量。
- 播放仅需 3DGS 光栅化器，不需要运动模型或神经网络。

### 主要贡献
- 提出 VersionGS，以版本化高斯直接编码逐帧状态，缓解快速运动下的质量退化。
- 通过共享字典、选择性顺序构建与版本复用，提升动态高斯的存储效率。
- 在 DanceNet3D 快速舞蹈序列上，相比最佳基线前景 PSNR 提升 2.7 dB；最高运动帧的 PSNR 下降小于 0.3 dB。
- 在 N3DV 和 Technicolor 上，相比整体最强基线 TAD-GS，存储分别减少 6.0 倍和 5.7 倍，同时取得更高 PSNR。
- 播放快速，且无需运动模型或神经网络，仅依赖 3DGS 光栅化器。

### 局限性
摘要未提供足够信息说明方法在不同运动模式、极端遮挡、长序列一致性、剪枝比例具体取值、量化误差影响、训练时间与计算成本等方面的表现；也未提供失败案例或与其他方法在非舞蹈类快速运动场景上的系统比较。

### 阅读优先级
高。理由：该论文直接针对动态高斯泼溅在快速运动下的质量退化问题，提出明确的版本化编码机制，并在摘要中给出可量化的质量与存储改进；同时播放不依赖运动模型或神经网络，若关注动态/4D 重建的紧凑表示与运动鲁棒性，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent dynamic Gaussian splatting methods encode temporal change, either as smooth functions of time or as constrained updates between frames. We observe that their reconstruction quality degrades significantly under fast motion. In challenging dance sequences, their PSNR drops by 1.1-4.0 dB on high-motion frames compared to low-motion frames. To overcome this limitation, we propose VersionGS, a method that directly encodes per-frame Gaussian states and uses motion estimation only to guide reconstruction. Within each group of frames, unchanged Gaussians keep their current versions in a shared dictionary, while modified Gaussians are appended as new versions. To maximize version reuse, we introduce selective sequential construction, which refines the Gaussians selected by optical flow, photograph differences or rendering errors and leaves the others unchanged. The dictionary is then pruned, fine-tuned with simulated quantization and encoded as images. Adjusting the pruning ratio trades off storage and quality without rebuilding the dictionary. On the fast dance sequences of DanceNet3D, VersionGS improves foreground PSNR by 2.7 dB over the best baseline, and its PSNR decreases by less than 0.3 dB on the highest-motion frames. On N3DV and Technicolor, it requires 6.0x and 5.7x less storage than TAD-GS, the strongest baseline overall, while achieving even higher PSNR. Finally, playback is fast and requires no motion model or neural network, only a 3DGS rasterizer.

</details>

#### 2026-11-24 - HARI4D: Hand-Articulation Aware 4D Reconstruction of Human-Object Interaction

**Authors:** Semin Kim, Xianghui Xie, Chuqiao Li, Jongyoo Kim, Gerard Pons-Moll
**Links:** [abs](https://arxiv.org/abs/2611.32932) - [pdf](https://arxiv.org/pdf/2611.32932)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, manipulation, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HARI4D: Hand-Articulation Aware 4D Reconstruction of Human-Object Interaction
- 作者：Semin Kim, Xianghui Xie, Chuqiao Li, Jongyoo Kim, Gerard Pons-Moll
- 出版日期：2026-11-24T16:39:09Z
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2611.32932

### 一句话总结
HARI4D 提出了一种手部关节感知的方法，可从单目 RGB 视频重建时空一致的人-物交互 4D 场景，并显式改善手部与物体的接触和关节姿态。

### 研究问题
从单目 RGB 相机进行 4D 人-物交互重建具有挑战性，尤其是涉及关节化手部时。已有全身重建工作忽略手部，导致手部穿入物体或与物体悬浮脱离。论文关注如何从单目 RGB 视频重建空间和时间一致、且手部关节准确的人-物交互 4D 结果。

### 核心思路/方法
论文提出 HARI4D，一种手部关节感知方法。方法包含：
- 一个历史感知的物体跟踪器，用于提供稳健、稳定的跟踪；
- 基于这些跟踪结果，通过由粗到细的推理改进交互配置，并遵循物体操作顺序：ReachNet 首先在接触阶段将全身和手臂带到物体处，TouchNet 再根据时间上下文和局部物体几何最终确定手部关节。

### 主要贡献
- 提出手部关节感知的 4D 人-物交互重建方法 HARI4D。
- 引入历史感知物体跟踪器以提供稳健稳定的跟踪。
- 设计由粗到细的交互配置改进流程，包括 ReachNet 和 TouchNet。
- 在训练中未见的 ARCTIC 上，相比先前方法将物体误差降低 56%，并将手部接触 F1 从 0.866 提升至 0.921。
- 方法可恢复准确的全身体-物体交互与连贯手部关节，并适用于在线视频。

### 局限性
摘要未提供足够信息。摘要未说明方法在更广泛场景、严重遮挡、快速运动或不同物体类别下的失败情况，也未提供计算效率、实时性开销或泛化边界的详细分析。

### 阅读优先级
中。理由：论文聚焦单目 RGB 下的 4D 人-物交互重建，且明确针对手部关节与接触一致性这一关键问题；摘要给出了在 ARCTIC 上的定量改进，并声称适用于在线视频，具有较高相关性。但摘要未提供方法细节、失败案例和效率信息，是否优先精读取决于读者对 4D 重建、手部建模或人-物交互的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MemHand: Memory-Enhanced World-Space Hand Motion Reconstruction from Egocentric Videos
- 作者：Junyi Ma, Zhangshuo Qi, Erhang Zhang, Mingjie Li, Hesheng Wang
- 出版日期：2026-11-24T16:12:13Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.32876 ；PDF https://arxiv.org/pdf/2611.32876

### 一句话总结
MemHand 是一个记忆增强框架，用短期事件记忆和长期尺度记忆解决第一人称视频中双手世界空间连续运动重建在遮挡、出视野等情形下上下文不足的问题，并在摘要报告的基准上取得优于 StableHand 的精度。

### 研究问题
从第一人称视频恢复双手在世界空间中的连续运动，对人到机器人的策略迁移和增强现实等应用很重要。该任务不能只逐帧重建手部，因为重建一帧所需的上下文往往分散在时间轴上，尤其是在遮挡或手移出视野时。已有工作利用时间上下文，但多来自固定长度窗口，无法保证每一帧都获得准确位姿和度量尺度所需上下文。

### 核心思路/方法
论文提出 MemHand 记忆增强框架，维护两种互补记忆：
- 短期事件记忆：在每次遮挡或出视野事件周围保留观测良好的手部上下文，并供给视觉证据弱或缺失的帧。
- 长期尺度记忆：由于度量尺度在整段录制中保持一致，它在有界状态内保留视频中最可靠的观测作为尺度锚点。

摘要称，两种记忆协同使 MemHand 在遮挡严重、频繁出视野的基准上达到最先进精度，并泛化到未见域；相对 StableHand，W-MPJPE 在 ARCTIC 上降低 57%，在 HOT3D 上降低 70%，输出连续且度量准确的世界空间手部位姿与轨迹。代码和模型将在项目页发布。

### 主要贡献
- 指出固定长度窗口无法保证每一帧都具备重建世界空间手部所需上下文的问题。
- 提出 MemHand，引入短期事件记忆与长期尺度记忆两种互补机制。
- 摘要报告其在严重遮挡和频繁出视野基准上取得最先进精度，并具有跨未见域泛化表现。
- 摘要给出相对 StableHand 的 W-MPJPE 降低幅度：ARCTIC 57%，HOT3D 70%。
- 承诺公开代码和模型，项目页为 https://irmvlab.github.io/memhand.github.io。

### 局限性
摘要未提供足够信息说明方法的具体失败情形、计算与存储开销、记忆容量或更新策略细节、对特定传感器或数据域的依赖，以及除 ARCTIC 和 HOT3D 外的定量结果。摘要也未提供足够信息说明消融实验、训练数据规模和实时性。

### 阅读优先级
高。理由：该论文直接针对第一人称视频中双手世界空间连续重建的遮挡与出视野上下文问题，提出明确的双记忆机制，并在摘要中报告了相对强基线的大幅 W-MPJPE 下降和跨域泛化结果；若关注第一人称手部运动重建、4D 重建或人到机器人策略迁移，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：PRC4D: Physical Relation-Constrained Persistent 4D Reconstruction
- 作者：Junho Kim, Hyunyoung Choi, Jiseok Kim, Seongwon Lee
- 出版日期：2026-11-24T11:02:02Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类：摘要未提供。
- 链接：摘要页 https://arxiv.org/abs/2611.32396 ；PDF https://arxiv.org/pdf/2611.32396

### 一句话总结
PRC4D 通过识别可靠的刚性物理关系，并利用序列级验证区分持续耦合与短暂交互，从而在遮挡期间保持 4D 重建的空间一致性并传播运动。

### 研究问题
现有 4D 重建方法在物体从视野中消失时，依赖局部空间与运动关联来保留已观测几何并扩展运动。但若把短期接触或共享运动误判为持续刚性，就会引入错误的运动约束，导致整体重建失真。论文要解决的问题是：如何识别真正可靠的刚性关系，避免短暂交互造成错误约束，并在遮挡期间维持重建一致性。

### 核心思路/方法
PRC4D 是一个物理关系约束框架。它结合 3D 接触与相对运动一致性，并加入序列级验证，用来区分持续耦合与短暂交互。由此得到的关系图用于指导已观测位姿的 refinement，并把运动从可见部件传播到被遮挡部件；摘要特别指出，这一过程不改变已重建的几何。

### 主要贡献
- 提出物理关系约束框架 PRC4D，用于识别可靠刚性关系并据此维持遮挡期间的空间一致性。
- 将 3D 接触、相对运动一致性与序列级验证结合，以区分持续耦合和短暂交互。
- 构建关系图来指导已观测位姿 refinement 与可见到遮挡部件的运动传播，同时不改变已重建几何。
- 在多样真实世界多物体序列和受控遮挡模拟上报告了重建精度提升、相对位姿误差降低以及可见性变化下更一致的物体配置。

### 局限性
摘要未提供足够信息。摘要未给出具体实验数据集规模、评价指标数值、计算开销、失败案例或方法假设的详细限制。

### 阅读优先级
中。理由：该论文针对 4D 重建中遮挡与错误刚性约束这一明确问题，方法思路清晰，且摘要报告了真实序列与受控模拟上的改进；但是否与具体研究方向相关，因未提供额外兴趣方向而无法判断，且摘要未给出定量结果与实现细节，建议在需要了解动态/4D 重建中关系约束与遮挡运动传播时阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：ST-SfM: Spatio-Temporal Structure-from-Motion for Initialising 4D Gaussian Splatting
- 作者：Harshit, Sami Brandt
- 出版日期：2026-11-24T09:13:06Z
- 分类：主分类：Dynamic / 4D Reconstruction；次分类：3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.32231) / [PDF](https://arxiv.org/pdf/2611.32231)

### 一句话总结
论文提出 ST-SfM，一种面向同步且已标定多相机视频的稀疏时空 SfM 方法，用于生成静态 3D 点与动态 4D 点，并以此初始化 4D Gaussian splatting。

### 研究问题
动态 Gaussian splatting 的初始化通常采用随机点，或仅使用首帧的 SfM 点云；摘要指出这两种方式都没有说明“什么在移动、在哪里移动、何时移动”。因此，问题在于如何从多相机视频中获得同时包含静态结构与动态时空信息的稀疏初始化。

### 核心思路/方法
ST-SfM 将场景分为静态与动态两个分支处理：
- 静态结构：在每个相机的时间中值图像上检测一次，经时间稳定性门控后，沿极线进行匹配。
- 动态运动：在视频体中检测时空兴趣点（STIPs），用 HOG3D 描述，并且仅在同时满足极线一致与时间一致的候选之间匹配。
- 跟踪与三角化：使用拒绝不一致合并的 union-find 进行跟踪，并对所有视图对用 RANSAC 三角化，得到静态 3D 点与带亚帧时间的动态 4D 点（x, y, z, t）。
- 应用：用 ST-SfM 得到的稀疏 4D 点云初始化 4D Gaussian splatting。

### 主要贡献
- 提出 ST-SfM：面向同步、已标定多相机视频的稀疏时空 SfM，同时输出静态 3D 点与动态 4D 点。
- 设计静态与动态分离的处理流程，并引入时间稳定性门控、极线与时间一致性匹配、拒绝不一致合并的 union-find 跟踪等机制。
- 将 ST-SfM 稀疏 4D 点云用于初始化 4D Gaussian splatting；摘要称在 N3DV 场景上相较随机初始化，PSNR、SSIM 与 LPIPS 均有改善。

### 局限性
- 摘要未提供足够信息说明方法对相机同步误差、标定误差或复杂非刚性运动的鲁棒性。
- 摘要未提供足够信息说明计算开销、运行时间与可扩展性。
- 摘要未提供足够信息说明除 N3DV 外其他数据集上的表现。
- 摘要未提供足够信息说明与首帧 SfM 初始化等其他初始化方式的完整对比细节。
- 摘要未提供足够信息说明失败案例或对静态/动态分离错误的敏感程度。

### 阅读优先级
中。理由：该论文关注 4D Gaussian splatting 的初始化问题，思路明确且与动态/4D 重建及多视图几何相关；但摘要仅给出 N3DV 上相对随机初始化的指标改善，未提供更全面的实验细节与局限性信息，适合作为相关方向的重点候选阅读，而非仅凭摘要即可判定为高优先级必读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MoGe-4D: Efficient, Flexible, and Unified Dense 4D Reconstruction and Tracking
- 作者：Ruicheng Wang, Linlin Xin, Sicheng Xu, Jianfeng Xiang, Zelong Lv, Yu Deng, Yue Dong, Guangzhong Sun, Tong Zhang, Jiaolong Yang
- 出版日期：2026-11-24T08:45:41Z
- 分类：Dynamic / 4D Reconstruction
- 链接：[摘要](https://arxiv.org/abs/2611.32198) / [PDF](https://arxiv.org/pdf/2611.32198)

### 一句话总结
MoGe-4D 提出一种前馈式统一框架，通过有序查询成对的非自我中心与自我中心动态点图，将稠密 4D 重建与跟踪中的几何和运动预测整合起来，并借助解耦查询解码与合成数据管线提升效率。

### 研究问题
论文针对从 RGB 视频重建动态场景的问题：该任务需要同时推理 3D 几何与跨视角运动。摘要指出，现有方法要么将重建和跟踪拆分为碎片化流水线，要么面临高昂的稠密时空解码成本。因此，核心问题是：如何在统一框架中高效完成稠密 4D 重建与跟踪，同时避免昂贵的稠密时空解码。

### 核心思路/方法
- 提出前馈框架 MoGe-4D，通过有序查询成对的非自我中心（allocentric）与自我中心（egocentric）动态点图来统一几何与运动预测。
- 每个查询将源像素在相机坐标系中映射到目标时间，并可闭式求解相对相机位姿，同时灵活支持深度、动态配准和稠密 3D 跟踪。
- 为高效进行稠密查询，将场景建模与查询解码解耦：高容量上下文编码器一次性缓存粗略全局时空特征，轻量查询编码器以灵活分辨率快速解码稠密点图。
- 针对稠密 4D 查询监督需要连续 3D 对应关系、而原始轨迹存储开销过大的问题，引入 RigIDTrack 合成数据管线与数据集，将表面动态压缩为刚性正则化的仿射体，从而以相对 RGB-D 视频约 15% 的存储开销恢复任意帧的精确 3D 轨迹。

### 主要贡献
- 提出统一的稠密 4D 重建与跟踪前馈框架 MoGe-4D，整合几何与运动预测。
- 设计了解耦的场景建模与查询解码机制，以支持高效、灵活分辨率的稠密点图查询。
- 引入 RigIDTrack 合成数据管线与数据集，以较低存储开销提供连续 3D 对应监督。
- 摘要声称：在多种基准上实现 state-of-the-art 的稠密 3D 跟踪，重建性能匹配专用 3D 基础模型，并且运行速度显著快于先前的 4D 基线。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基准名称、评价指标和定量结果。
- 摘要未提供足够信息说明方法在不同动态场景、遮挡、快速运动或复杂光照条件下的失败情况。
- 摘要未提供足够信息说明 RigIDTrack 的适用范围及其对真实数据的泛化影响。
- 摘要未提供足够信息说明计算资源需求、模型规模或实际部署限制。

### 阅读优先级
高。理由：该论文同时涉及动态 4D 重建与稠密 3D 跟踪的统一建模、高效查询解码和合成数据监督，摘要中明确声称在跟踪、重建和速度上具有优势；若关注动态场景重建、4D 跟踪或高效视觉基础模型，值得优先阅读。但需注意，当前仅基于摘要，具体实验证据需查阅全文。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Tornado4D: Physics-Guided 4D Gaussian Reconstruction of a Laboratory Tornado from Sparse One-Sided Videos
- 作者：Yucheng Zhu, Maria J. Molina, Christopher Metzler
- 出版日期：2026-11-23T19:16:36Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2611.31435 ；PDF https://arxiv.org/pdf/2611.31435

### 一句话总结
Tornado4D 利用 enclosure（封闭空间）几何知识引入旋转气流场先验，从稀疏单侧视频重建实验室烟雾龙卷风的时间分辨 4D 高斯表示，并在留出视角的新视角合成上优于逐帧 3DGS 和基于视频的 4DGS。

### 研究问题
论文关注如何从稀疏、单侧视频中对实验室烟雾龙卷风进行时间分辨的 3D 重建，以刻画龙卷风在空间和时间上的演化。摘要指出，即使是在受控环境中，该重建问题也严重欠约束：外观依赖视角、运动非刚性、未观测体积存在多种可能几何。

### 核心思路/方法
论文提出 Tornado4D，一个物理引导的 4D 高斯框架，用于从稀疏单侧视频重建实验室龙卷风。方法利用 enclosure（封闭空间）几何知识引入旋转气流场先验，以约束 3D 结构随时间的变化；这些旋转先验使其能够重建原本未观测到的结构。摘要提到通过留出相机视角上的新视角合成准确率评估重建精度，但未提供具体网络结构、损失函数、训练细节或数据集规模。

### 主要贡献
- 提出 Tornado4D，一个物理引导的 4D 高斯框架，用于从稀疏单侧视频重建实验室龙卷风。
- 引入基于 enclosure 几何知识的旋转气流场先验，约束 3D 结构的时间演化，并用于重建未观测结构。
- 在留出相机视角的新视角合成评估中，Tornado4D 相比逐帧 3DGS 和基于视频的 4DGS 有显著提升；具体数值指标摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法对 enclosure 几何先验的依赖程度及先验不准确时的鲁棒性。
- 摘要未提供足够信息说明方法在真实野外龙卷风或更复杂非实验室场景中的泛化能力。
- 摘要未提供足够信息说明定量评估的完整指标、对比实验设置、运行效率与重建分辨率等细节。
- 摘要未提供足够信息说明对稀疏单侧视频的视角数量、视频长度或烟雾特性变化的敏感度。

### 阅读优先级
中。理由：该工作面向欠约束动态 4D 重建，结合物理先验与 4D 高斯表示，问题设定和应用背景较有特色；但摘要仅给出留出视角新视角合成的相对比较结论，未提供具体定量结果、实现细节和泛化验证信息，适合作为相关方向的方法参考进一步阅读全文确认。

</details>

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

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-25 - CADENCE: Sensor-GroundedWorld-Consistent Gaussian SLAM for Collaborative Mobile Reconstruction

**Authors:** Reshad Ul Karim, Abrar Samin, Md Rashad Al Hasan Rony
**Links:** [abs](https://arxiv.org/abs/2611.34549) - [pdf](https://arxiv.org/pdf/2611.34549)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, rendering, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CADENCE: Sensor-GroundedWorld-Consistent Gaussian SLAM for Collaborative Mobile Reconstruction
- 作者：Reshad Ul Karim, Abrar Samin, Md Rashad Al Hasan Rony
- 出版日期：2026-11-25T15:26:02Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.34549 ；PDF https://arxiv.org/pdf/2611.34549

### 一句话总结
CADENCE 是一个面向消费级手机协同室内重建的高斯 SLAM 系统，将“寻找跨设备匹配”与“决定匹配观测如何更新地图”分离，以降低异构设备退化观测和错误关联对共享高斯地图的破坏。

### 研究问题
摘要指出，使用消费级手机进行协同重建有望更快、更完整地构建室内地图，但异构设备会带来退化观测和不可靠的跨设备关联；单个表现差的贡献者或一次错误匹配都可能污染共享高斯地图。因此，论文关注如何在协同高斯 SLAM 中稳健地建立跨设备匹配，并控制不同质量观测对地图更新的影响。

### 核心思路/方法
CADENCE 将跨设备匹配发现与匹配接受、地图更新决策分开处理。在匹配发现阶段，使用“传感器锚定的区域记忆”汇总已提交观测，并依据外观、相对位姿、重力、气压高度和观测质量对候选对端区域排序；随后通过确定性几何验证和可选物理检查决定接受哪些候选匹配。匹配被接受后，系统使用基于不同线索的独立置信度，分别控制该观测对位姿约束、几何、外观和记忆的贡献，从而使颜色不可靠时仍可利用有效深度。整个过程里，本地跟踪与建图、验证和网络通信保持隔离。

### 主要贡献
- 提出 CADENCE 协同高斯 SLAM 系统，将跨设备匹配发现与“是否及如何用对端观测更新地图”的决策分离。
- 设计传感器锚定的区域记忆，融合外观、相对位姿、重力、气压高度和观测质量进行候选区域排序。
- 引入确定性几何验证与可选物理检查来控制错误关联，并采用分线索置信度分别调节位姿、几何、外观和记忆的贡献。
- 摘要报告在八个未用于训练记忆的 Matterport3D 房屋上，区域记忆 AUROC 为 0.95 至 0.97，优于外观检索；验证将错误链接率保持在 0.5% 以下。
- 摘要报告软置信度加权将八种退化下的平均 PSNR 损失从 2.66 dB 降至 1.05 dB，并保留有用的对端深度；在十二个留出 iPhone 扫描上实现 6.98 cm 的平均绝对轨迹误差，精化地图的平均渲染质量优于基线。

### 局限性
摘要未提供足够信息说明计算开销、实时性、通信带宽需求、不同手机型号的泛化范围、失败案例、消融实验完整设置，以及“可选物理检查”的具体触发条件与成本。摘要也未提供足够信息说明基线细节和统计显著性。

### 阅读优先级
中。理由：论文主题集中在协同高斯 SLAM、异构设备鲁棒性和跨设备地图一致性，摘要给出了较明确的性能指标；但若关注具体实验协议、系统开销或实际部署可行性，需进一步阅读全文，摘要本身信息有限。

</details>

<details>
<summary>Abstract</summary>

Collaborative reconstruction with consumer phones promises faster and more complete indoor maps. However, heterogeneous devices introduce degraded observations and unreliable cross-device associations, so a single poor contributor or incorrect match can corrupt the shared Gaussian map. To address this, we propose \textbf{CADENCE}, a collaborative Gaussian simultaneous localization and mapping (SLAM) system that separates finding cross-device matches from deciding whether and how peer observations update the map. To find matches, a sensor-grounded regional memory summarizes committed observations and ranks candidate peer regions using appearance, relative pose, gravity, barometric altitude, and observation quality. Deterministic geometric verification and optional physical checks then decide which of the proposed matches are accepted. Once a match is accepted, separate cue-based confidences control how its observations contribute to pose constraints, geometry, appearance, and memory. As a result, useful depth can still contribute even when color is unreliable. Throughout this process, local tracking remains isolated from mapping, verification, and networking. We evaluate CADENCE on eight Matterport3D houses that were not used to train the memory. On these houses, regional memory achieves an area under the receiver operating characteristic curve (AUROC) of $0.95$ to $0.97$ and thus outperforms appearance retrieval, while verification keeps false-link rates below $0.5\,\%$. Furthermore, soft confidence weighting reduces the mean receiver peak signal-to-noise ratio (PSNR) loss from $2.66$ to $1.05$\,dB across eight degradations while retaining useful peer depth. Finally, using inertial and platform motion, CADENCE tracks all twelve held-out iPhone scans with a mean absolute trajectory error of $6.98$\,cm, and its refined maps achieve better average rendering quality than the baselines.

</details>

#### 2026-11-25 - Plausible Is Not Proven: Testing Failure Explanations in Monocular Depth Estimation

**Authors:** Zeeshan Ali, Md Rayyan, Anshuman Chakravorty, Omer Faraz, Anshi Bajaj, Amit Saini
**Links:** [abs](https://arxiv.org/abs/2611.34393) - [pdf](https://arxiv.org/pdf/2611.34393)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Plausible Is Not Proven: Testing Failure Explanations in Monocular Depth Estimation
- 作者：Zeeshan Ali, Md Rayyan, Anshuman Chakravorty, Omer Faraz, Anshi Bajaj, Amit Saini
- 出版日期：2026-11-25T13:54:08Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2611.34393)｜[PDF](https://arxiv.org/pdf/2611.34393)

### 一句话总结
论文提出 Vision Error Observatory（VEO）审计框架，用来检验单目深度估计模型失败原因标签是否可信；结果显示许多看似合理的失败解释经不起测试。

### 研究问题
单目深度模型的失败分析常为每个错误区域标注一个原因，例如遮挡边界、薄物体或反射表面，但摘要指出这些标签很少被验证。论文要回答的核心问题是：这些“看似合理”的失败解释是否真的成立，能否与标注、人类判断、图像编辑响应和训练信号价值相一致。

### 核心思路/方法
论文提出 VEO 审计流程：在传感器测量像素上找出不满足 \(δ_1\) 准则的区域，为每个区域标注一个可能原因或选择弃权，然后用四类测试检验这些标签：
1. 在标注模型未见过的数据上，检查标签与物体标注是否一致；
2. 检查标签与盲评人类评分者是否一致；
3. 检查标签对针对性图像编辑的响应；
4. 检查标签作为训练信号的价值。
论文在 NYU Depth V2、DIODE 和 iBims-1 上对八个模型应用该流程，并在 Hypersim 上额外检查标签，且多数决策规则在结果产生前固定。

### 主要贡献
- 提出并发布 VEO 审计协议，用于系统检验单目深度估计失败原因标签，而不仅提出解释。
- 对八类模型和多个数据集进行审计，并用四类测试评估失败标签。
- 报告多项负面或有限证据：遮挡边界标签虽与标注有一定一致性（AUROC 0.85 on NYU、0.81 on Hypersim、0.69 on iBims-1），但单一深度边缘线索表现相当，且最强模型多数边界失败在 2 像素容忍下消失；反射标签不能迁移到合成数据；无纹理标签相对标注接近随机；四项编辑测试中仅一项探索性测试支持其标签。
- 与五名盲评者比较时，VEO 标签仅在随机水平上与人类共识一致（Cohen's \(κ\) = 0.05）。
- 微调时提高被诊断区域权重，在所有测试权重下都导致目标像素误差增加；早先版本声称的架构特定失败指纹也未能跨数据集复现。
- 论文声明发布协议、代码、评分和所有结果文件。

### 局限性
摘要未提供足够信息说明数据集规模、模型细节、人类评分者招募方式、编辑测试的具体设计、统计显著性细节以及发布资源的具体范围。论文主要报告负面或有限验证结果；摘要未提供足够信息判断这些结论在其他任务、数据集或失败类型上的泛化程度。

### 阅读优先级
高。理由：该论文直接挑战单目深度估计失败分析中常见但少被验证的因果标签，并提供可审计协议和多类检验结果；对关注模型可靠性、误差分析和评测方法的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Failure analyses of monocular depth models often name a cause for each error, such as an occluding boundary, a thin object or a reflective surface, but such labels are rarely tested. We present the Vision Error Observatory (VEO), an audit that finds regions failing the $δ_1$ criterion on sensor-measured pixels, labels each with a likely cause or abstains, and then subjects the labels to four tests: agreement with object annotations on data the label model never saw, agreement with blinded human raters, response to targeted image edits, and value as a training signal. We apply it to eight models on NYU Depth V2, DIODE and iBims-1, with labels also checked on Hypersim, and fix most decision rules before their results. The occluding-boundary label agrees with annotations (AUROC 0.85 on NYU, 0.81 on Hypersim, 0.69 on iBims-1), but a single depth-edge cue does as well, and most boundary failures of the strongest model vanish under a 2-pixel tolerance. The reflection label does not transfer to synthetic data, the textureless label is near chance against annotations, and only one of four edit tests, an exploratory one, supports its label. Evaluated against five blinded raters, VEO's labels matched the human consensus only at chance level (Cohen's $κ$ = 0.05). In addition, an increase in the weight on the diagnosed regions during fine-tuning led to an increase in the error on targeted pixels at every weight tested. The architecture-specific failure fingerprint claimed by an earlier version of this project also failed to replicate across the datasets. Plausible failure explanations, in short, need to be tested before they are trusted; we release the protocol, code, ratings and every result file.

</details>

#### 2026-11-25 - OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction

**Authors:** Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan
**Links:** [abs](https://arxiv.org/abs/2611.34155) - [pdf](https://arxiv.org/pdf/2611.34155)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OceanFix: Reference-Guided Diffusion for Sparse-View Underwater 3D Reconstruction
- 作者：Gen Li, Maoxin Chen, Yao Xiao, Xinyang Li, Yu Pan
- 出版日期：2026-11-25T10:49:40Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.34155)｜[PDF](https://arxiv.org/pdf/2611.34155)

### 一句话总结
OceanFix 是一个参考引导的稀疏视角水下三维重建框架，将基于扩散的视角修复与高斯场景细化结合，用于缓解稀疏观测、光衰减和后向散射造成的欠约束区域与新颖视角伪影。

### 研究问题
论文关注稀疏视角水下三维重建中的以下问题：稀疏观测、光衰减和后向散射导致场景区域约束不足，并产生新颖视角渲染伪影。作者指出，近期高斯泼溅虽已支持高效的水下重建，但上述问题仍然存在。

### 核心思路/方法
OceanFix 采用“参考引导”的框架，将基于扩散的视角修复与高斯场景细化相结合。其修复模型采用两阶段训练策略，将水下外观适配与几何细化分离：
- 第一阶段：从参考观测和估计的介质特征中学习水下外观。
- 第二阶段：使用相机位姿和参考深度对齐参考特征，并以相对深度监督引导结构修复；推理时不需要目标视角深度。
此外，论文提出介质感知蒸馏，根据几何修复需求和通道特定的光学可观测性，将修复后的视角迁移到三维场景中。通过迭代的渲染、修复和蒸馏，OceanFix 细化欠约束区域，同时保留来自观测视角的监督。

### 主要贡献
- 提出 OceanFix，一个面向稀疏视角水下三维重建的参考引导框架，结合扩散视角修复与高斯场景细化。
- 设计两阶段训练策略，分离水下外观适配与几何细化；第二阶段利用相机位姿、参考深度和相对深度监督进行结构修复，且推理时无需目标视角深度。
- 提出介质感知蒸馏，依据几何修复需求和通道特定的光学可观测性，将修复视角迁移到三维场景。
- 通过迭代渲染、修复和蒸馏细化欠约束区域，并保留观测视角监督。
- 摘要称在水下数据集上的实验表明，该方法提升了稀疏视角三维重建的渲染质量，减少了可见伪影，并恢复了更精细的场景细节；具体数据集、指标和对比结果摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏视角、不同水体条件或大尺度场景下的适用边界。
- 摘要未提供足够信息说明两阶段训练与迭代修复-蒸馏的计算开销、收敛性或实时性。
- 摘要未提供足够信息说明对参考观测、参考深度或相机位姿估计误差的敏感性。
- 摘要未提供足够信息说明定量实验结果、对比基线、数据集规模及消融实验细节。
- 摘要未提供足够信息说明失败案例或方法在特定水下退化条件下的表现。

### 阅读优先级
中。理由：该论文面向稀疏视角水下三维重建这一明确且具有挑战性的问题，方法上结合扩散修复与高斯场景细化，并引入两阶段训练和介质感知蒸馏，具有一定的新颖性与方向参考价值；但当前仅依据摘要，缺少定量结果、数据集细节和消融信息，尚不足以判断其相对优势与泛化能力。若读者关注水下重建、稀疏视角补全或扩散模型与三维场景表示结合，可优先阅读全文；否则可保持中等优先级。

</details>

<details>
<summary>Abstract</summary>

Recent advances in Gaussian splatting have enabled efficient underwater reconstruction, but sparse observations, light attenuation, and backscatter still leave scene regions underconstrained and cause novel-view artifacts. We present OceanFix, a reference-guided framework for sparse-view underwater 3D reconstruction that combines diffusion-based view repair with Gaussian scene refinement. Our repair model follows a two-stage training strategy that separates underwater appearance adaptation from geometric refinement. The first stage learns underwater appearance from reference observations and estimated medium features. The second uses camera poses and reference depth to align reference features, with relative-depth supervision guiding structural repair without requiring target-view depth at inference. We further propose medium-aware distillation that transfers repaired views into the 3D scene according to geometric repair demand and channel-specific optical observability. Through iterative rendering, repair, and distillation, OceanFix refines underconstrained regions while retaining supervision from the observed views. Experiments on underwater datasets demonstrate that OceanFix improves rendering quality in sparse-view 3D reconstruction, reducing visible artifacts and recovering finer scene details.

</details>

#### 2026-11-25 - FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images

**Authors:** Shenxing Wei, Jinxi Li, Zihui Zhang, Ajay Kumar, Wei Wang, Bo Yang
**Links:** [abs](https://arxiv.org/abs/2611.34128) - [pdf](https://arxiv.org/pdf/2611.34128)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pointmap, surface reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FoundSurface: Feedforward Ray-Based 3D Scene Surface Reconstruction from Unposed Images
- 作者：Shenxing Wei, Jinxi Li, Zihui Zhang, Ajay Kumar, Wei Wang, Bo Yang
- 出版日期：2026-11-25T10:30:24Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.34128) / [PDF](https://arxiv.org/pdf/2611.34128)

### 一句话总结
该论文提出 FoundSurface，将 pointmap 表示与基于射线的表示相结合，从无位姿图像中直接恢复连续、高保真的三维表面。

### 研究问题
从无相机位姿的图像中进行准确的三维表面重建是计算机视觉中的基础挑战。现有前馈 pointmap 方法虽然免去相机位姿需求，但会产生离散、稀疏的表示，难以直接获得连续高精度表面。

### 核心思路/方法
- 利用预训练 pointmap 模型提取显式几何先验。
- 设计以查询视角为中心的选择模块，通过稳健的 surfel 投票机制挑选几何相关的参考视角。
- 使用跨注意力回归器，将目标查询射线与参考特征关联，估计连续粗表面。
- 通过基于 rayolet 的模块聚合局部三维特征，刻画高频细节并输出解析法线。
- 将方法作为单一基础模型在 9 个多样化数据集上训练。

### 主要贡献
- 提出融合 pointmap 与射线表示的通用前馈流程，从无位姿图像直接恢复连续三维表面。
- 引入基于 surfel 投票的参考视角选择机制，以及跨注意力粗表面估计与 rayolet 细节精化模块。
- 摘要声称在 6 个未见数据集上展现出优异的零样本泛化能力，并在几何精度与细节保持方面明显超越现有最优基线。

### 局限性
摘要未提供足够信息说明计算开销、推理速度、对稀疏视角或大尺度场景的鲁棒性、失败案例及定量实验细节；也未给出具体数据集名称、评价指标和消融结果。

### 阅读优先级
中。理由：该工作针对无位姿图像三维表面重建这一重要问题，提出 pointmap 与射线表示融合的明确技术路线，并声称具有较强零样本泛化能力；但摘要未提供定量结果与实现细节，需进一步阅读全文以验证其实际性能与适用边界。

</details>

<details>
<summary>Abstract</summary>

Accurate 3D surface reconstruction from unposed images remains a fundamental challenge in computer vision. Recent feed-forward pointmap methods eliminate the need for camera poses but inherently produce discrete, sparse representations. In this paper, we present a generalizable pipeline that directly recovers continuous, high-fidelity 3D surfaces from unposed images by seamlessly integrating pointmap- and ray-based representations. Our approach first extracts explicit geometric priors using a pre-trained pointmap model. A query-view-centric selection module then identifies geometrically relevant reference views via a robust surfel voting mechanism. Next, a cross-attention regressor bridges target query rays with reference features to estimate a continuous coarse surface. Lastly, a raylet-based module aggregates local 3D features to carve out high-frequency details and analytical normals. Trained as a single foundation model on 9 diverse datasets, our method demonstrates exceptional zero-shot generalization on 6 unseen datasets, clearly surpassing state-of-the-art baselines in geometric accuracy and detail preservation.

</details>

#### 2026-11-25 - Where to Approximate: Understanding and Accelerating Looped Multi-View Reconstruction

**Authors:** Siyuan Zhang, Yuhan Chen, Yangyang Ning, Nan Wang, Jun Yan
**Links:** [abs](https://arxiv.org/abs/2611.33948) - [pdf](https://arxiv.org/pdf/2611.33948)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Where to Approximate: Understanding and Accelerating Looped Multi-View Reconstruction
- 作者：Siyuan Zhang, Yuhan Chen, Yangyang Ning, Nan Wang, Jun Yan
- 出版日期：2026-11-25T08:09:12Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.33948 ；PDF https://arxiv.org/pdf/2611.33948

### 一句话总结
论文通过配对干预分析循环多视图重建中近似误差的注入、传播及对输出的影响，并据此设计了一种加速方案：早期对空间分辨率以及 key/value 做近似，再交错使用注意力输出复用与完整注意力，并以轻量自蒸馏适配。

### 研究问题
循环多视图重建通过重复应用共享 transformer 块来细化场景特征。若要让这些更新更廉价，需要理解某一步的近似会如何影响后续细化过程。论文关注的核心问题是：近似误差在循环细化中如何被注入、如何传播，以及如何影响最终输出，从而指导“在哪里近似”以加速模型。

### 核心思路/方法
- 使用 Déjà View 和 stacked reconstruction transformers 中的配对干预实验，将近似注入的误差、误差传播以及其对输出的影响分开分析。
- 在尺度调整后的状态误差度量下，发现 Déjà View 中近似误差比匹配的随机扰动被更强地衰减；并用局部 Jacobian 分解区分通道门控的贡献与对空间误差结构的响应。
- 发现早期进行空间近似可从后续细化中受益；跨步复用效果取决于缓存哪个量以及复用步的间隔。在最终范数相等时，近似误差对预测旋转的改变量是随机误差的 1.55 倍。
- 基于这些发现提出方法：在细化早期降低空间分辨率并池化 keys 和 values，然后将注意力输出复用与完整注意力交错进行，并通过轻量自蒸馏进行适配。

### 主要贡献
- 对循环多视图重建中的近似误差进行分离式分析，区分误差注入、传播和输出影响。
- 给出关于空间近似时机、跨步复用对象与间隔、以及近似误差相对随机误差影响的经验性发现。
- 提出一种由上述发现指导的加速方法，结合早期空间近似、key/value 池化、注意力输出复用与完整注意力交错、以及轻量自蒸馏。
- 在五个重建基准上报告：平衡配置比官方 16 步 Déjà View 模型快 1.63 倍，平均 pose AUC@3° 降低 1.86 点；在匹配延迟下，相较使用完整细化块的训练基线插值曲线，AUC@3° 高 4.73 点，并改善相应几何指标。

### 局限性
- 摘要未提供足够信息说明五个重建基准的具体名称、数据集规模与评价协议细节。
- 摘要未提供足够信息说明自蒸馏的具体损失设计、训练成本与超参数敏感性。
- 摘要未提供足够信息说明方法在更大模型、其他循环结构或不同视图数量下的泛化性。
- 摘要未提供足够信息说明 1.86 点 AUC 下降在不同应用场景中的可接受程度及误差分布。

### 阅读优先级
高。理由：论文不仅提出加速方法，还围绕“近似误差如何传播”给出分析框架和可操作的設計依据；摘要中包含明确的加速比与多个基准上的定量结果，对循环多视图重建的效率优化具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Looped multi-view reconstruction refines scene features by repeatedly applying a shared transformer block. Making these updates cheaper requires knowing how an approximation at one step affects the rest of the refinement. We study this with paired interventions in Déjà View and stacked reconstruction transformers, separating the error an approximation injects, how that error propagates, and how it affects the output. In Déjà View, approximation errors are attenuated more strongly than matched random perturbations under a scale-adjusted state-error measure, and a local Jacobian decomposition separates the contribution of channel gating from the response to spatial error structure. Spatial approximations made early benefit from subsequent refinement, whereas cross-step reuse depends on which quantity is cached and how reuse steps are spaced. At equal final norm, approximation errors change the predicted rotations 1.55 times as much as random errors. These findings guide our proposed method, which reduces spatial resolution and pools keys and values early in refinement, then interleaves attention-output reuse with full attention, and is adapted through lightweight self-distillation. Across five reconstruction benchmarks, the balanced configuration runs $1.63\times$ faster than the official 16-step Déjà View model with a 1.86-point reduction in average pose AUC@$3^\circ$. At matched latency, it exceeds the interpolated curve of a trained baseline using full refinement blocks by 4.73 points in AUC@$3^\circ$ and improves the corresponding geometry metrics.

</details>

#### 2026-11-25 - Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction

**Authors:** Di Wu, Jeeeun Kim, Shu Kong
**Links:** [abs](https://arxiv.org/abs/2611.33824) - [pdf](https://arxiv.org/pdf/2611.33824)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation, surface reconstruction, Gaussian Splatting, rendering, splatting, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction
- 作者：Di Wu, Jeeeun Kim, Shu Kong
- 出版日期：2026-11-25T05:54:14Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33824) / [PDF](https://arxiv.org/pdf/2611.33824)

### 一句话总结
论文针对普通智能手机拍摄的单目视频做手持物体扫描（IHOS），提出新数据集 ToysRUs，并针对相机位姿估计和遮挡条件下的表面重建提出改进方法。

### 研究问题
论文关注从普通智能手机拍摄的单目视频中进行手持物体扫描（IHOS），目标是推动非专家用户进行 3D 数字化。摘要指出该方向因缺乏真实数据集和系统基准而研究不足。在方法层面，论文重点分析相机位姿估计这一关键环节，并指出两个挑战：连续帧之间基线较小，以及大视角、长距离帧之间特征匹配稀疏；动态手部遮挡会进一步加剧这些问题。

### 核心思路/方法
- 数据集：构建 ToysRUs，包含用 4K 超高清单目视频采集的多样小雕像（figurines）。
- 位姿估计：从第一性原理研究用于相机位姿估计的 structure-from-motion（SfM）。根据上述挑战，提出在按足够角度间隔采样的视频子序列上执行 SfM，并迭代地将对应子轨迹拼接为统一的全局轨迹。
- 表面重建：为高保真表面重建引入遮挡感知的 2D Gaussian Splatting，包含不透明度渲染（opacity rendering），并省略手部区域上的不透明度损失（opacity loss）。

### 主要贡献
- 引入 ToysRUs 数据集，用于单目手持物体扫描研究。该数据集包含 4K 超高清单目视频采集的多样小雕像。
- 分析 IHOS 中基于 SfM 的相机位姿估计所面临的关键挑战，并提出基于角度间隔采样子序列并迭代拼接子轨迹的全局轨迹构建思路。
- 提出遮挡感知的 2D Gaussian Splatting，用于高保真表面重建，其中包含不透明度渲染，并省略手部区域上的不透明度损失。
- 摘要称定量和定性评估表明，该框架在几何精度和光度保真度上显著优于现有方法，包括神经隐式表示和 3D 基础模型。

### 局限性
- 摘要未提供足够信息说明数据集规模、采集设备细节、物体类别覆盖范围和标注方式。
- 摘要未提供足够信息说明定量实验的具体指标、对比方法配置、消融实验和误差分析。
- 摘要未提供足够信息说明方法在失败案例、计算成本、实时性、泛化到其他物体或场景方面的表现。
- 摘要未提供足够信息说明手部遮挡以外其他动态干扰或复杂背景对方法的影响。

### 阅读优先级
高。理由：论文同时覆盖数据集、位姿估计和表面重建三个 IHOS 关键环节，并声称在几何精度与光度保真度上优于神经隐式表示和 3D 基础模型；对 3D 重建、多视图几何和神经场景表示方向具有直接相关性。但具体实验细节需查阅原文确认。

</details>

<details>
<summary>Abstract</summary>

In-Hand Object Scanning (IHOS) from monocular video captured by a commodity smartphone holds immense potential to democratize 3D digitization for non-expert users, facilitating applications in digital archiving, augmented reality, and custom fabrication. Yet, IHOS remains largely understudied due to a lack of realistic datasets and systematic benchmarks. To bridge this gap, we introduce ToysRUs, a high-quality dataset featuring diverse figurines captured by 4K Ultra High-Definition (UHD) monocular videos. Studying IHOS from first principles, we examine structure-from-motion (SfM) for camera pose estimation, which is key to IHOS. We identify two key challenges: small baselines between consecutive frames, and sparse feature matches across large-view, long-range frames, further exacerbated by dynamic hand occlusions. Guided by these insights, we propose performing SfM on video sub-sequences sampled at sufficient angular intervals, and iteratively stitches the corresponding sub-trajectories into a unified global trajectory. Furthermore, for high-fidelity surface reconstruction, we introduce occlusion-aware 2D Gaussian Splatting, which incorporates opacity rendering and omits the opacity loss on hand regions. Quantitative and qualitative evaluations demonstrate that our framework significantly outperforms existing approaches, including neural implicit representations and 3D foundation models, in both geometric accuracy and photometric fidelity.

</details>

#### 2026-11-25 - DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation

**Authors:** Lifan Jiang, Yifan Huang, Jixuan Zhang, Peifeng Wang, Yuying Ma, Dehai Zhao, Deng Cai, Boxi Wu
**Links:** [abs](https://arxiv.org/abs/2611.33734) - [pdf](https://arxiv.org/pdf/2611.33734)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation
- 作者：Lifan Jiang, Yifan Huang, Jixuan Zhang, Peifeng Wang, Yuying Ma, Dehai Zhao, Deng Cai, Boxi Wu
- 出版日期：2026-11-25T03:54:18Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.33734)｜[PDF](https://arxiv.org/pdf/2611.33734)

### 一句话总结
论文标题指向“双图像条件扩散 Transformer 的数字人电商视频生成”，但所给摘要实际描述的是名为 GameWeaver 的视频—相机轨迹联合生成框架，两者明显不一致，摘要未提供与标题所述任务直接对应的信息。

### 研究问题
按标题，问题应是数字人电商视频生成中的双图像条件建模；但摘要讨论的是大规模 gameplay 视频与相机轨迹配对数据的稀缺与采集瓶颈，以及如何用统一扩散框架自动生成视频—相机配对数据。摘要未提供足够信息说明该问题与“数字人电商视频”之间的关系。

### 核心思路/方法
摘要给出的是 GameWeaver 的方法：用 tipxel 表示像素射线端点在参考坐标系下的归一化三维坐标，使其三通道场与 RGB 帧共享预训练视频模型的 VAE；采用全可训练双流 Transformer，通过双向门控注意力交换外观与几何特征，并以共享文本特征作为两流条件；最后由确定性拟合从生成的 tipxel 场中恢复相机内参与归一化轨迹。该描述与标题中的“DualCast / 双图像条件 / 数字人电商视频”不对应。

### 主要贡献
摘要声称的贡献包括：提出统一的扩散框架 GameWeaver，覆盖视频相机位姿估计、沿指定轨迹的视频生成、以及由参考图像和文本联合生成视频—相机三类任务；在评测中相机控制的归一化平移 MSE 为 0.0029，联合生成指令遵循得分为 85.48/100，对比最佳级联方法的 64.71。关于 DualCast 标题所述工作的贡献，摘要未提供足够信息。

### 局限性
- 标题与摘要存在明显不一致：标题为 DualCast 与数字人电商视频生成，摘要却全部围绕 GameWeaver 与 gameplay 视频—相机数据，无法据此确认论文真实主题。
- 摘要未提供 DualCast 的双图像条件机制、数字人建模方式、电商场景数据与评测指标等信息。
- 摘要未提供 GameWeaver 的训练数据规模、基线设置、消融实验、推理效率与失败案例等细节。
- 摘要未说明 tipxel 表示在复杂动态场景或真实电商数字人视频中的适用性。
- 以上缺失信息均属于“摘要未提供足够信息”。

### 阅读优先级
低。标题与摘要主题严重不匹配，仅凭所给元数据无法判断论文真实内容与贡献；若需引用或复现，应先核对 arXiv 页面与 PDF 是否元数据错配，再决定是否深入阅读。

</details>

<details>
<summary>Abstract</summary>

Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories. However, capturing synchronized camera trajectories often requires game-specific pipelines, limiting scalability. We therefore propose GameWeaver, a unified diffusion framework that automatically produces paired video--camera data through three complementary tasks: camera pose estimation from observed video, video generation along a prescribed camera trajectory, and joint video--camera generation from a reference image and text. First, each tipxel stores the normalized 3D coordinates of a pixel ray's endpoint in a reference coordinate frame. The resulting three-channel tipxel fields and RGB frames share the pretrained video model's VAE. Next, a fully trainable dual-stream Transformer exchanges appearance and geometry features through bidirectional gated attention and conditions both streams on shared text features. Finally, deterministic fitting recovers camera intrinsics and normalized trajectories from generated tipxel fields. In our evaluation tasks, GameWeaver achieves a normalized translation MSE of 0.0029 for camera control; for joint generation, it scores 85.48 out of 100 on instruction adherence versus 64.71 for the best cascade on that metric, validating the feasibility of the proposed approach.

</details>

#### 2026-11-24 - First-Hit Photoconsistency for Neural Surface Reconstruction

**Authors:** Gabriel Lenain, Edmond Boyer, Jean Ponce
**Links:** [abs](https://arxiv.org/abs/2611.32998) - [pdf](https://arxiv.org/pdf/2611.32998)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：First-Hit Photoconsistency for Neural Surface Reconstruction
- 作者：Gabriel Lenain, Edmond Boyer, Jean Ponce
- 出版日期：2026-11-24T17:25:53Z
- 分类：主分类 3D Reconstruction & Multi-view Geometry；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.32998) / [PDF](https://arxiv.org/pdf/2611.32998)

### 一句话总结
该论文提出仅利用基于几何可见性的多视角 patch 光度一致性，以及首次命中球面追踪，进行神经隐式表面重建，从而避免体渲染和参数化外观模型。

### 研究问题
多视角表面重建中，几何与外观联合优化会引入歧义：参数化外观模型可能补偿几何误差，使模型在表面不准确时仍能精确重现输入图像。论文希望在不依赖体渲染或参数化外观模型的条件下，实现准确的神经隐式表面重建。

### 核心思路/方法
对每条参考射线，使用球面追踪计算首次表面交点；由交点的位置与法向定义局部 patch，并利用从输入图像直接采样的颜色，在可见的邻近视角上评估该 patch 的光度一致性。为提升球面追踪效率，采用 1-Lipschitz 多层感知机。方法仅使用单一光度一致性损失，不使用前景掩码或辅助几何正则化。

### 主要贡献
- 提出仅依赖多视角 patch 光度一致性与几何可见性的神经隐式表面重建方法，不使用体渲染或参数化外观模型。
- 通过球面追踪得到首次表面交点，并以该点的位置和法向定义用于光度一致性评估的局部 patch。
- 使用 1-Lipschitz MLP 支持高效球面追踪，并采用单一光度一致性损失，无需前景掩码或辅助几何正则化。
- 摘要报告：在 BlendedMVS（BMVS）上，相较对比方法取得最低平均 Chamfer 距离；在 DTU 上达到与领先重建方法相当的几何精度。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败情形、计算成本、对视角覆盖或可见性的敏感性，以及在不同数据集上的完整定量结果与消融细节。

### 阅读优先级
中。理由：该工作针对几何与外观联合优化的歧义问题，提出无需体渲染和参数化外观模型的简洁监督思路，并报告了 BMVS 与 DTU 上的几何精度结果；但摘要未提供充分实验细节与局限性信息，是否优先精读取决于读者对神经隐式表面重建及光度一致性监督方向的关注程度。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：CityRecast: Suppressing Persistent Artifacts in Generative Satellite 3D Reconstruction
- 作者：Shuo Cui, Yingyan Hou, Wanxuan Lu, Hongfeng Yu, Daobing Zhang, Xian Sun
- 出版日期：2026-11-24T16:01:55Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.32863 ；PDF https://arxiv.org/pdf/2611.32863

### 一句话总结
CityRecast 通过高斯场景修复与监督校准，抑制卫星三维重建生成式高斯场景中持续存在的重影、拖影与模糊，尤其改善低仰角渲染伪影。

### 研究问题
卫星三维重建受稀疏观测与不同采集日期变化限制；现有方法虽用生成先验恢复缺失视觉细节，但其高斯场景中仍持续存在重影、拖影和模糊，且这些伪影在低仰角渲染中尤为明显。论文关注如何抑制这些持续伪影，并同时保持卫星视角的保真度。

### 核心思路/方法
论文提出 CityRecast，核心由“高斯场景修复”和“监督校准”两部分构成：
- 针对产生伪影的高斯分布进行修正，首先采用多角度 warm-up 约束其空间范围，以减少带入渐进式细化过程中的初始重影；
- 随后使用表面引导替换（surface-guided replacement）继续修复高斯分布，同时保留已有外观；
- 为给该修复过程提供更可靠监督，采用观测校准（observation calibration）缓解多时相观测的干扰；
- 进一步通过联合细化（joint refinement）减少生成视图之间的冲突。

### 主要贡献
- 提出 CityRecast，用于抑制生成式卫星三维重建中持续存在的伪影，明确针对低仰角渲染中的重影、拖影与模糊问题。
- 设计高斯场景修复流程，包括多角度 warm-up 约束空间范围与表面引导替换修复高斯分布。
- 引入观测校准以减轻多时相观测干扰，并通过联合细化减少生成视图之间的冲突。
- 在 DFC2019 与 IARPA 数据集上报告：低仰角渲染伪影减少，同时保持卫星视角保真度；相较 Skyfall-GS，FID-CLIP 在 DFC2019 上降低 25.3%，在 IARPA 上降低 51.8%；MUSIQ 分别提升 14.54 与 24.95 点。

### 局限性
摘要未提供足够信息说明方法的计算开销、对观测数量或质量的敏感性、失败案例、消融实验细节，以及在其他数据集或场景类型上的泛化表现。

### 阅读优先级
高。理由：该论文直接针对卫星三维重建中持续伪影这一明确问题，方法描述围绕伪影成因与监督可靠性展开，并给出两个数据上的定量指标；若关注生成式卫星三维重建、低仰角渲染质量与高斯场景修复，具有较高相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DOPER: Deep Object Pose Estimation Revisited
- 作者：Hugo Hadfield, Alperen Degirmenci, Jonathan Tremblay
- 出版日期：2026-11-24T15:54:17Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.32846) / [PDF](https://arxiv.org/pdf/2611.32846)

### 一句话总结
DOPER 是一个仅使用 RGB 输入的 6D 物体位姿估计框架。它在物体检测、分割与关键点预测之间共享视觉主干网络，并通过 PnP 恢复已知物体的位姿。其特点是：先利用合成数据训练，再通过部分监督与多视图几何约束适配真实观测。

### 研究问题
论文关注已知物体的 6D 位姿估计：如何在不使用深度输入、也不依赖学习式位姿精化器的情况下，从 RGB 观测中恢复位姿；同时，如何在合成训练到真实观测的迁移过程中，处理关键点监督不足和对应关系存在歧义的问题。摘要还提到，从欠明确的 CAD 模型出发，如何逐步细化物体表示与位姿估计器。

### 核心思路/方法
- 采用共享视觉主干的多任务框架，联合进行物体检测、分割和关键点预测，并通过 Perspective-n-Point 求解 6D 位姿。
- 从合成训练出发，在保留合成关键点标签的同时，利用部分监督适配真实观测。
- 使用经过校准的多视图观测，为关键点监督提供几何约束。
- 推理阶段可选热图精化，将刚性位姿直接拟合到预测的关键点分布上，从而缓解对应关系歧义；该过程不依赖深度输入或学习式位姿精化器。
- 从欠明确的 CAD 模型开始，渐进细化物体表示和位姿估计器。

### 主要贡献
- 提出 DOPER，一个 RGB 6D 位姿估计框架；其核心设计是让检测与位姿关键点联合学习。
- 提出从合成到真实的适配策略：结合部分监督、合成关键点标签和多视图几何约束。
- 提出推理阶段的可选热图精化，直接拟合刚性位姿，以解决对应关系歧义，且无需深度或学习式位姿精化器。
- 摘要报告：在 SPEED+ 与 SHIRT 上展示了对光照变化的有效适配和准确的时间位姿估计；在 HANDAL、HOPEv2、HOT3D、T-LESS 的评估配置中取得 state-of-the-art 检测 AP，且仅使用 RGB、实时运行（单 GB300 上每个物体模型 35 Hz）。

### 局限性
摘要未提供足够信息。摘要未给出失败案例、计算资源总体开销、对特定物体或场景类型的适用边界，也未说明多视图约束在实际部署中的依赖条件与限制。

### 阅读优先级
中。理由：该工作聚焦 RGB 6D 位姿估计中的合成到真实适配、多视图几何监督和无需学习式精化器的推理拟合，并报告了多个基准上的检测 AP 与实时性；但摘要未展开关键实验细节与局限。若关注物体位姿估计、RGB-only 实时感知或多视图几何约束在训练中的应用，值得进一步阅读全文验证。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Diving Deeper into Dense Keypoint Localization in Object Pose Estimation
- 作者：Jiahong Chen, Jinghao Wang, Yueneng Yang, Banglei Guan, Zi Wang, Dewen Hu, Qifeng Yu
- 出版日期：2026-11-24T14:46:04Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.32728 ；PDF https://arxiv.org/pdf/2611.32728

### 一句话总结
论文提出 GHLAPose，将混合格雷-二进制（HGB）编码与局部感知细化（LAR）结合的全局到局部框架，用于缓解二值编码在稠密关键点定位中的不连续性和量化误差，从而提升刚体目标 6D 位姿估计精度。

### 研究问题
论文关注刚体目标 6D 位姿估计中的稠密语义关键点定位问题。摘要指出，近期基于稠密语义关键点的方法采用二值编码进行高效全局关键点定位，但在高分辨率训练时受二值编码不连续性的阻碍，同时二值编码固有的离散与量化误差会带来显著的定位不确定性。论文旨在解决这些编码层面的问题，以提升关键点定位和最终位姿估计的精度。

### 核心思路/方法
论文提出 GHLAPose，一个“全局到局部”的框架，核心由两部分组成：

1. **混合格雷-二进制（HGB）编码**：用于首先缓解二值编码的不连续性，从而实现准确的初始全局关键点定位。
2. **局部感知细化（LAR）模块**：在 HGB 初始定位之后，进一步估计不确定性并细化关键点定位，以处理编码内在误差。

论文强调，该协同设计通过聚合全局特征和局部特征，形成精确的全局到局部策略。摘要未提供网络结构、损失函数、训练策略或实现细节的更多信息。

### 主要贡献
- 提出 GHLAPose，将 HGB 编码与 LAR 模块结合，形成全局到局部的稠密关键点定位框架。
- 使用 HGB 编码缓解二值编码的不连续性，以改善高分辨率下的训练和初始全局关键点定位。
- 通过 LAR 模块估计不确定性并细化关键点定位，以应对编码固有的离散与量化误差。
- 在 LM、LM-O、YCB-V 和 TUD-L 数据集上进行实验，摘要称其优于当前最优方法，尤其在细粒度指标上表现突出。具体而言：在 LM-O 上，ADD(-S) 0.02d 和 0.05d 指标分别比第二名方法高 1.4% 和 1.9%；在 YCB-V 上，ADD(-S) 0.1d 指标高 1%。摘要提到代码将在 GHLAPose 提供。

### 局限性
摘要未提供足够信息，无法判断方法的计算开销、实时性、对对称物体或严重遮挡的鲁棒性、消融实验的完整细节，以及 HGB 与 LAR 各自贡献的定量分解。摘要也未说明失败案例或适用边界。

### 阅读优先级
**中**。理由：论文主题属于 6D 位姿估计中的关键点定位，问题定义清晰，方法针对二值编码的已知缺陷提出明确改进，并在多个常用数据集上报告了相对当前最优方法的提升；但摘要仅给出有限指标提升和框架级描述，未提供实现细节、消融结果和效率信息。若读者关注物体位姿估计、机器人/AR 应用或稠密关键点定位，可优先阅读；若需要评估工程可用性或实时性能，则需进一步查看全文。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：RestPose: Canonicalization for Open Object Pose Estimation
- 作者：Sandeep Inuganti, Weihang Li, Benjamin Busam, Didier Stricker, Jason Rambach
- 出版日期：2026-11-24T14:28:29Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.32696) / [PDF](https://arxiv.org/pdf/2611.32696)

### 一句话总结
RestPose 提出在训练阶段不依赖参考模型或规范帧约定的开放物体位姿估计方法：从单张输入图像生成物体网格，经几何与物理分析完成规范化，再借助基础模型的稠密匹配估计位姿。

### 研究问题
现有基于学习的物体位姿估计方法依赖一个由任意建模约定定义的规范帧，并用该约定生成训练所需真值位姿标注，导致方法被绑定在任意约定上、限制泛化能力。论文希望避免在训练中依赖参考模型与规范帧约定。

### 核心思路/方法
- 主张规范帧可以对任意物体推导得到，而不是必须由人为选定的建模约定预先定义。
- 从单张输入图像生成物体网格。
- 对该网格进行几何与物理分析，从而实现物体的规范化（canonicalization）。
- 使用基于基础模型的稠密匹配来估计位姿。
- 在训练阶段不要求参考模型或规范帧约定，也不要求任务特定训练。

### 主要贡献
- 提出 RestPose，一种面向开放物体位姿估计的方法，训练时无需参考模型或规范帧约定。
- 给出从单图生成网格、再经几何与物理分析导出规范帧的流程。
- 在 HouseCat6D、NOCS、Omni6DPose 类别级基准上评估规范化效果，并报告相对监督式最先进方法在绝对指标上提升 18.3 点、在尺度无关指标上提升 13.8 点，且无需任务特定训练。
- 摘要说明代码将发布。

### 局限性
- 摘要未提供足够信息说明方法在不同物体类别、遮挡、对称物体或生成网格质量不佳时的具体失败情形。
- 摘要未提供足够信息说明计算开销、推理时延与对基础模型稠密匹配的依赖程度。
- 摘要未提供足够信息说明 18.3 点与 13.8 点提升对应的具体指标定义、评测协议细节及各数据集上的分项结果。
- 摘要未提供足够信息说明“几何与物理分析”的具体判据与鲁棒性边界。

### 阅读优先级
高。理由：该工作直接挑战位姿估计中规范帧约定这一基础设定，提出免参考模型、免任务特定训练的开放物体位姿估计路线，并在三个类别级基准上报告显著提升；若关注位姿估计泛化与规范化问题，值得优先阅读。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System
- 作者：Kuan Xu, Tianxin Hu, Ruofei Bai, Ruimeng Liu, Yuefan Hao, Zeyu Jiang, Zitong Zhan, Shenghai Yuan, Chen Wang, Lihua Xie
- 出版日期：2026-11-24T12:50:38Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.32523 ；PDF https://arxiv.org/pdf/2611.32523

### 一句话总结
AirLeg 提出一种自监督视觉-惯性-腿部 SLAM 系统，通过让视觉与腿部本体感知在训练到部署过程中相互促进，提升足式机器人定位的鲁棒性与精度。

### 研究问题
论文关注足式机器人视觉-惯性-腿部（VIL）状态估计中的腿部里程计监督问题：基于学习的腿部里程计受监督信号限制，仿真训练存在 sim-to-real 差距，真实世界标签则需要昂贵传感器或继承视觉估计误差。系统还希望在低成本四足平台上实现实时、低漂移定位。

### 核心思路/方法
- 在仿真中预训练腿部里程计网络，并通过 imperative learning 在无真值情况下适配到机器人。
- 采用多传感器 bundle adjustment：用腿部里程计细化视觉地图，再由视觉地图反过来监督网络。
- 部署阶段，融合估计在线适配网络。
- 设计双窗口估计器融合视觉、IMU 与腿部里程计。
- 通过 deformation-aware constraint 将受载足与视觉重建地形关联，并用方差分量估计对约束加权。

### 主要贡献
- 提出自监督 VIL SLAM 系统 AirLeg，使视觉与腿部本体感知从训练到部署相互改进。
- 引入无真值的 imperative learning 适配流程，以及多传感器 bundle adjustment 的互相监督机制。
- 设计双窗口估计器，并结合 deformation-aware 约束与方差分量估计提升定位与监督质量。
- 摘要报告：在 19 种方法中，AirLeg 以最低平均误差（0.19 m）完成全部 17 个 GrandTour 序列；在低成本四足平台上，仅用 0.5 小时无标签数据即达到最低漂移（0.6%），并在嵌入式计算机上实时运行。

### 局限性
- 摘要未提供足够信息说明方法在不同地形、光照、动态场景或极端运动条件下的具体表现。
- 摘要未提供足够信息说明 imperative learning 的收敛性、训练成本与超参数敏感性。
- 摘要未提供足够信息说明方差分量估计与 deformation-aware 约束在失败情况下的退化行为。
- 摘要未提供足够信息说明与更多基线方法在同等硬件与数据条件下的公平对比细节。
- 摘要未提供足够信息说明长期部署中的在线适配稳定性与漂移累积特性。

### 阅读优先级
高。理由：该论文聚焦足式机器人低成本 VIL SLAM 的关键监督瓶颈，提出自监督与多传感器互相监督的系统方案，并在摘要中给出覆盖 17 个序列、对比 19 种方法以及低成本四足实时部署的量化结果，对视觉-惯性-腿部融合、SLAM 与机器人定位方向具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：DiffAnchor: Anchor-Space Diffusion for Monocular 3D Hand Pose Estimation
- 作者：Changlong Jiang, Youci Tang, Haohong Kuang, Hang Xu, Jinghong Zheng, Ran Wang, Zhenghong Yu, Chen Feng, Xiaofeng Yue, Yang Xiao
- 出版日期：2026-11-24T12:42:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.32513) / [PDF](https://arxiv.org/pdf/2611.32513)

### 一句话总结
DiffAnchor 提出在“锚点空间”而非最终关节坐标上做少步扩散，以降低单目 3D 手部姿态估计中扩散生成的精度负担与推理成本。

### 研究问题
论文关注单目 3D 手部姿态估计的准确性与效率。摘要指出，现有基于扩散的方法直接对 3D 关节坐标去噪，需要生成过程同时探索合理姿态并恢复精确坐标，往往依赖更多去噪步数或多假设，从而增加推理成本。如何减少扩散过程的精度负担、在少步与单假设下实现精确预测，是本文要解决的问题。

### 核心思路/方法
论文提出少步的锚点空间扩散框架 DiffAnchor，核心是扩散“锚点”而不是“关节”。其思路是让随机探索不直接作用于最终输出，而是搜索有信息量的中间锚点，使锚点充当局部 3D 回归器；随后通过锚点到关节的偏移预测与加权聚合完成精确关节定位。方法中，固定上下文锚点提供稳定的全局参考，带噪动态锚点则被迭代细化到有信息量的关节区域。此外，重要性引导的锚点选择与补充机制用于保留有效锚点、移除无效锚点，并探索覆盖不足的区域。该设计旨在降低扩散过程的精度负担，并支持仅用少量去噪步和单一假设进行准确预测。

### 主要贡献
- 提出 DiffAnchor，将扩散过程从最终关节坐标转移到锚点空间，使扩散负责搜索有信息量的中间锚点，而精确关节定位由锚点到关节偏移预测与加权聚合完成。
- 设计固定上下文锚点与带噪动态锚点的协同机制：前者提供稳定全局参考，后者迭代细化到有信息量的关节区域。
- 引入重要性引导的锚点选择与补充机制，用于保留有用锚点、去除无效锚点并探索覆盖不足区域。
- 摘要称在 HO-3D V2、NYU、ICVL 和 InterHand2.6M 上进行大量实验，前三个基准达到 state-of-the-art，在具有挑战性的交互手部估计上具有竞争力，同时推理效率与确定性回归基线相当。

### 局限性
- 摘要未提供足够信息说明方法在遮挡、极端姿态、低质量输入或跨数据集泛化方面的具体失败情形。
- 摘要未提供足够信息说明锚点数量、去噪步数、重要性选择机制的超参数敏感性及消融细节。
- 摘要未提供足够信息给出具体推理时延、参数量、显存占用或与各基线效率对比的数值。
- 摘要未提供足够信息说明在 InterHand2.6M 上“competitive performance”的具体差距与原因。
- 摘要未提供足够信息说明训练数据规模、训练策略、输入模态细节及是否存在数据集特定假设。

### 阅读优先级
中。理由：该论文针对扩散式 3D 手部姿态估计的推理效率与精度负担提出明确的锚点空间建模思路，且摘要声称在多个常用基准上达到 state-of-the-art 并保持与确定性回归基线相当的推理效率；对关注单目 3D 手部姿态估计、扩散模型在视觉回归中应用的研究者有直接相关性。但摘要未给出实验细节、效率数值与局限性分析，是否值得优先精读需结合全文实验与消融部分进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：COHERE4D: Training-Free Dense Surface Alignment for Coherent Metric 4D Human-Scene Reconstruction
- 作者：Zhumei Wang, Shaofei Wang, Xiang An, Mingtao Pei, Siyuan Huang
- 出版日期：2026-11-24T12:09:36Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[abstract_url](https://arxiv.org/abs/2611.32482) / [pdf_url](https://arxiv.org/pdf/2611.32482)

### 一句话总结
COHERE4D 是一个无需训练的框架，通过将独立预训练的人体基础模型与场景基础模型所预测的人体表面进行稠密配准，重建具有一致度量尺度的 4D 人体-场景世界。

### 研究问题
单目 4D 重建中，人体基础模型能恢复度量尺度的身体网格，但缺乏场景 grounding；场景基础模型能估计全局一致的 3D 几何与相机运动，但缺乏可靠的度量尺度。二者实际上重建的是同一前景人体表面，但现有方法没有直接利用这一共享表面：由于场景重建中缺乏可靠的前景人体几何，已有方法要么采用稀疏接触约束，要么学习数据驱动的对齐模块，而后者对分布外场景泛化较差。论文旨在解决如何直接利用两个模型共享的人体表面，实现一致的人体-场景对齐与度量 4D 重建。

### 核心思路/方法
COHERE4D 直接配准由独立预训练的人体与场景基础模型预测的人体表面，以重建连贯的度量 4D 世界。具体而言：
- 在可见人体表面上建立稠密的、像素对齐的 3D 对应关系；
- 使用 RANSAC 结合跨帧共识，抑制来自遮挡、背景污染和深度噪声的离群点；
- 求解两个互补的几何量：一个序列级共享尺度，用于将场景几何与相机运动校准到人体度量尺寸；以及逐帧人体平移，用于将相机空间的人体网格与缩放后的场景几何对齐，从而保证空间与时间一致性。

### 主要贡献
- 提出 COHERE4D，一个无需训练的框架，直接配准独立预训练人体模型与场景模型预测的人体表面，重建连贯的度量 4D 世界。
- 建立稠密像素对齐的 3D 人体表面对应，并结合 RANSAC 与跨帧共识抑制遮挡、背景污染和深度噪声带来的离群点。
- 通过求解序列级共享尺度与逐帧人体平移，同时校准场景几何/相机运动到度量尺度并强制时空一致性。
- 摘要称在多种骨干网络与基准上，COHERE4D 在人体-场景对齐、度量场景与相机位姿重建、全局人体运动估计方面显著优于先前方法，仅增加 4 ms/帧，整体推理可达 14 FPS。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集规模、失败案例、对特定骨干网络的依赖程度、极端遮挡或快速运动场景下的表现等细节，因此无法基于摘要评估其局限。

### 阅读优先级
中。理由：该论文针对单目 4D 人体-场景重建中度量尺度与人体-场景对齐的关键问题，提出无需训练、仅增加 4 ms/帧的轻量对齐方案，问题定义清晰且方法具有一定通用性；但摘要未提供充分的实验细节与局限性说明，是否值得优先精读需结合全文的实验验证与适用场景进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GOLD-SLAM: Gaussian-splatting Omnidirectional LiDAR-Depth SLAM
- 作者：Weicong Zhang, Yuan Huang, Yu Zheng, Lin Chenxiao, Yingying Li, Lilong Fan, Liangdong Zhuang, Yufan Chen, Ruiping Liu, Junwei Zheng, Jiaming Zhang
- 出版日期：2026-11-24T10:20:41Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.32335 ；PDF https://arxiv.org/pdf/2611.32335

### 一句话总结
GOLD-SLAM 是一个在全景（球面）域内进行跟踪与建图的全向 LiDAR-深度高斯泼溅 SLAM 系统，通过利用 LiDAR 覆盖区域之外的视觉特征辅助位姿估计，并用深度感知的地图扩展与剪枝（DAEP）缓解增量建图中的覆盖不足与漂浮伪影。

### 研究问题
全景相机单帧可覆盖近整个球面视场，但其视场与 LiDAR 视场不匹配，这给依赖 LiDAR 深度先验的全景高斯泼溅 SLAM 带来显著挑战。论文即针对这一不匹配下的高质量渲染与精确几何重建问题展开。

### 核心思路/方法
- 在全景/球面域中执行跟踪与建图。
- 在缺乏 LiDAR 覆盖的区域使用已跟踪的视觉特征来改进位姿估计。
- 针对增量建图中新观测表面覆盖不足与漂浮伪影问题，提出 Depth-Aware Map Extension and Pruning（DAEP）。
- 收集新数据集 WHOLE，使用 UAV 平台覆盖 Weak-geometry、High-dynamic、Omnidirectional、Low-light、Easy 场景，以支持更广泛评估。
- 在资源受限平台（Jetson Orin NX，16 GB）上评估嵌入式配置，实现在线运行但以重建质量为代价。

### 主要贡献
- 提出 GOLD-SLAM 全向 LiDAR-深度高斯泼溅 SLAM 系统，结合高质量渲染与准确几何重建。
- 通过球面域跟踪建图与 LiDAR 未覆盖区域的视觉特征利用，缓解全景覆盖与 LiDAR 视场不匹配问题。
- 提出 DAEP 以处理增量建图中新观测表面覆盖不足和漂浮伪影。
- 构建 WHOLE 数据集，覆盖多类挑战场景，用于更广泛评估。
- 在公开基准与 WHOLE 上报告：相对透视系统具有竞争力渲染质量与更好几何精度；相对现有全景基线，平均 PSNR 提升 5.56–9.10 dB，平均 Depth-L1 降低 71.9–83.9%。
- 给出 Jetson Orin NX（16 GB）嵌入式配置的在线运行可行性评估。

### 局限性
- 嵌入式配置虽可在线运行，但摘要明确说明以重建质量为代价；具体质量下降幅度与量化细节摘要未提供足够信息。
- 摘要未提供方法在极端场景下的失败模式、计算开销细节、实时性指标（除嵌入式在线运行这一表述外）等信息，摘要未提供足够信息。
- 摘要未提供与更多类别基线（除全景基线与透视系统外）的系统性对比细节，摘要未提供足够信息。

### 阅读优先级
中。理由：论文聚焦全景高斯泼溅 SLAM 中 LiDAR 视场不匹配这一具体问题，提出球面域跟踪建图与 DAEP，并给出较明显的全景基线定量提升及嵌入式部署评估，对 3D 重建、神经渲染与 SLAM 交叉方向有参考价值；但摘要未展开关键实现细节与失败模式，是否高优先阅读取决于读者对全向/全景 SLAM 与 UAV 部署的具体兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：EventSSM: Causal Spatial-State Modelling for Asynchronous Events Event-Depth Estimation
- 作者：Sadiq O. Macaulay, Dipon Ghosh, Hadfield Simon
- 出版日期：2026-11-24T00:23:47Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.31720) | [PDF](https://arxiv.org/pdf/2611.31720)

### 一句话总结
提出 EventSSM，一个以事件包为时序输入、通过循环记忆进行因果空间状态建模的事件相机度量深度估计框架，并利用相机位姿几何变换与可微渲染把异步深度预测对齐到参考时间戳监督。

### 研究问题
事件相机输出异步亮度变化，而度量深度监督通常只在稀疏采样的参考时间戳上可用。将事件聚合成类帧表示虽简化学习，却可能掩盖原始事件流的细粒度时间结构。论文关注：如何在保留事件异步时序结构的前提下，进行与事件关联的度量深度估计，并桥接异步预测与帧时间监督之间的不匹配。

### 核心思路/方法
- 构建因果空间状态框架，用按时间顺序到达的事件包更新循环记忆，进行与事件关联的度量深度估计。
- 使用循环记忆保留持续的空间上下文与按物理时间对齐的状态。
- 为桥接异步预测与帧时间监督，利用标定相机位姿对预测的事件深度做几何变换，并在参考时间戳上可微渲染。
- 通过基准评测与受控消融考察跨模态初始化、时间循环、个体状态、读出与监督组件以及事件包细分等设计。

### 主要贡献
- 提出 EventSSM，面向异步事件的因果空间状态建模与度量深度估计框架。
- 设计基于事件包时序更新的循环记忆机制，避免将事件简单聚合为类帧表示。
- 提出利用标定位姿几何变换与可微渲染，将异步事件深度预测对齐到参考时间戳监督。
- 基准评测显示在多项深度误差指标上优于已有事件深度方法。
- 通过受控消融分析跨模态初始化、时间循环、状态、读出、监督组件及事件包细分的作用。

### 局限性
- 摘要未提供足够信息说明具体数据集、基线方法、误差指标数值及计算开销。
- 摘要未提供足够信息说明几何变换与可微渲染对位姿标定误差的敏感程度。
- 摘要未提供足够信息说明方法在稀疏或噪声事件条件下的鲁棒性。
- 摘要未提供足够信息说明消融实验的完整设置与定量结果。

### 阅读优先级
中。理由：论文聚焦事件相机异步时序建模与度量深度估计，方法思路（循环记忆 + 几何变换 + 可微渲染监督）对事件视觉与 3D 重建方向有参考价值；但摘要未给出具体实验规模与数值细节，是否精读需结合全文实验部分再判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Anchoring VAE Fine-Tuning to Its Latent Diffusion Prior
- 作者：Rafael Bischof, Dominik Narnhofer, Julius Erbach, Michael Kraus, Konrad Schindler, Bernd Bickel
- 出版日期：2026-11-23T22:38:59Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；未提供二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.31651 ；PDF https://arxiv.org/pdf/2611.31651

### 一句话总结
论文提出 Diffusion Prior Anchoring（DPA），在 VAE 微调阶段用分数蒸馏更新约束潜变量靠近预训练扩散模型能够准确去噪的高密度流形，从而在冻结扩散主干时改善非 RGB、非三通道任务上的迁移学习效果。

### 研究问题
现有做法在迁移学习中微调扩散主干但冻结 VAE 编码器，以保持潜变量分布；然而冻结编码器可能遗漏非 RGB 输入中的显著细节，并且受限于三通道输入。论文要解决的问题是：在允许 VAE 微调的同时，如何避免潜变量偏离预训练扩散模型所适配的分布，从而保持扩散先验的有效性。

### 核心思路/方法
论文引入 DPA 作为 VAE 微调期间的正则化器：它使用分数蒸馏更新，将潜变量引导至预训练扩散模型能够准确去噪的高密度流形。论文在三种图像与视频模型（FLUX 3、LTX-Video、Wan2.2）和四项任务（单目深度估计、MRI 重建、风场模拟、表面法向估计）上验证 DPA；并说明 DPA 也适用于修改过的 VAE，包括剪枝与多通道变体，例如使用同时编码深度与表面法向的四通道 VAE。

### 主要贡献
- 提出 DPA：一种在 VAE 微调期间应用的分数蒸馏式正则化方法，用于将潜变量锚定到预训练扩散模型的高密度流形。
- 相对冻结 VAE 降低预测误差 7.5%，相对仅解码器微调降低 4.9%，相对未锚定的 VAE 微调降低 4.0%（基于摘要给出的总体结果）。
- 指出收益随目标数据远离 RGB 训练分布而增大：从单目深度估计的 3.3% 到复值 MRI 的 7.2%。
- 证明 DPA 可应用于修改过的 VAE，包括剪枝和多通道变体；在编码深度与表面法向的四通道 VAE 上，深度估计误差降低 9.3%。

### 局限性
摘要未提供足够信息说明计算开销、训练稳定性、对分数蒸馏超参数的敏感性、各任务与各模型的完整消融，以及失败情形或适用范围边界。

### 阅读优先级
高。理由：该论文直接针对“冻结 VAE 编码器限制非 RGB 与多通道迁移”的关键瓶颈，给出可跨多种图像/视频模型与多任务验证的正则化方案，并报告相对多种基线的误差下降；对涉及扩散先验迁移、VAE 微调和多通道输入的研究方向具有较高相关性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：InitFree-SfM: When Initialization-Free Bundle Adjustment meets Learned Structure-from-Motion
- 作者：Simon Weber, Mateo de Mayo, Je Hyeong Hong, Carl Olsson, Daniel Cremers, Ronald Clark
- 出版日期：2026-11-23T20:22:10Z
- 分类：3D Reconstruction & Multi-view Geometry（主要分类）；次要分类：摘要未提供
- 链接：[摘要](https://arxiv.org/abs/2611.31516) / [PDF](https://arxiv.org/pdf/2611.31516)

### 一句话总结
论文指出现有无初始化光束法平差（InitFree BA）在重建精度上存在“优化目标值与实际重建质量不匹配”的问题，并提出结合学习对应关系、度量深度、深度一致轨迹构建与联合度量优化的完整无初始化 SfM 流程 InitFree-SfM，以及深度增强的 OSE（dOSE）目标。

### 研究问题
- 无初始化光束法平差（InitFree BA）需要在不依赖初始全局估计的情况下，联合恢复相机位姿与场景结构，相比传统 BA 更具挑战性。
- 近期方法从随机初始化出发优化替代的 Object Space Error（OSE）目标，但摘要指出：低目标值不一定带来准确重建，暴露出优化与重建之间的差距。
- 现有 InitFree BA 流程在现代 SfM 基准上难以产生准确的三维重建。

### 核心思路/方法
- 将学习到的度量深度引入 InitFree BA 流程，以提升其实际可行性。
- 提出完整的无初始化 SfM 流程 InitFree-SfM，组合以下要素：
  - 学习到的对应关系（learned correspondences）；
  - 度量深度（metric depth）；
  - 深度一致的轨迹构建（depth-consistent track construction）；
  - 联合度量优化（joint metric refinement）。
- 在该框架内提出简单的深度增强 OSE（dOSE）：在 OSE 的方向性约束之外，沿观测射线约束地标位置。
- 分析上挑战此前 InitFree BA 研究对替代目标的强调，指出几何约束在准确重建中起核心作用，而基于 OSE 的优化提供进一步提升。

### 主要贡献
- 揭示现有 InitFree BA 流程在现代 SfM 基准上重建精度不足，并指出优化目标与重建质量之间的差距。
- 证明引入学习到的度量深度可显著提升 InitFree BA 的实际可行性。
- 提出完整的无初始化 SfM 流程 InitFree-SfM，整合学习对应关系、度量深度、深度一致轨迹构建与联合度量优化。
- 提出深度增强 OSE（dOSE），在方向约束之外增加沿射线的位置约束。
- 摘要称该方法大幅优于现有 InitFree BA 方法，并在包括低重叠图像集合的挑战场景下，与成熟 SfM 流程达到有竞争力的精度。
- 分析结论强调几何约束在准确重建中的核心作用，重新审视此前对替代目标的侧重。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性或在更大规模数据集上的表现。
- 摘要未提供足够信息说明对学习度量深度质量的依赖程度及失败情形。
- 摘要未提供足够信息给出具体实验数据集、指标数值与消融细节。
- 摘要未提供足够信息说明低重叠场景之外的其他极端条件（如强动态、严重光照变化）下的鲁棒性。

### 阅读优先级
高。理由：该论文直接针对无初始化 SfM/BA 这一 challenging 问题，提出完整流程与新目标函数，并对“替代目标与重建质量不匹配”给出分析性结论；摘要声称在低重叠等挑战场景下与成熟流程有竞争力，对 3D 重建与多视图几何方向具有较高参考价值。但具体实验细节需查阅全文，摘要未提供足够信息。

</details>

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

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-25 - A Mesh for Every Moment

**Authors:** Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman
**Links:** [abs](https://arxiv.org/abs/2611.34939) - [pdf](https://arxiv.org/pdf/2611.34939)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Mesh for Every Moment
- 作者：Roy Or-El, Jeong Joon Park, Ira Kemelmacher-Shlizerman
- 出版日期：2026-11-25T18:59:45Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.34939 ；PDF https://arxiv.org/pdf/2611.34939

### 一句话总结
MEMO 面向多台同步相机拍摄的完整动态场景，重建其几何并在每一帧导出网格，核心是让每个高斯在时间序列中始终是有效的表面元素，从而可由高斯定义的场在任意时刻导出网格。

### 研究问题
现有动态高斯泼溅方法要么只建模外观，要么只处理由前景掩码分割出的孤立物体；它们都依赖 TSDF 融合或泊松重建来恢复网格，而固定网格限制了可捕捉的细节。此外，真实拍摄中常见的大幅快速运动是动态高斯泼溅方法通常忽视的挑战。摘要未提供足够信息说明其具体失败表现或量化影响。

### 核心思路/方法
- 提出 MEMO，从多台同步相机捕获的完整动态场景重建几何，并逐帧提取网格。
- 核心是受高斯过程启发的“逐高斯运动模型”：把每个高斯的位置和旋转随时间的变化表示为时间高斯核的组合。
- 该模型使每个高斯在整个序列中保持为有效表面元素，并携带动态几何的隐式表示，因此可在任意时刻从高斯定义的场中导出网格。
- 针对大幅快速运动，设计基于轨迹的初始化方案：以闭式解将每个高斯的初始轨迹拟合到点轨迹。
- 评估使用新基准 Blender-Moments（九个动画场景，且每帧有真值网格）以及两个真实世界数据集。

### 主要贡献
- 提出 MEMO 方法，用于完整动态场景的几何重建与逐帧网格提取。
- 提出受高斯过程启发的逐高斯运动模型，将位置与旋转表示为时间高斯核组合，并保持高斯作为有效表面元素，支持任意时刻导出网格。
- 设计基于轨迹的闭式初始化方案，以应对大幅快速运动。
- 提出 Blender-Moments 基准：九个动画场景，每帧提供真值网格。
- 摘要称：在对比的先进方法中几何重建最准确，并在新视角合成与训练时间上保持竞争力。具体数值与对比细节摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法在何种场景、运动幅度、相机配置或遮挡条件下会失效。
- 摘要未提供足够信息说明对多台同步相机的数量、同步精度或标定质量的依赖程度。
- 摘要未提供足够信息说明训练时间、内存占用或逐帧网格提取开销的具体量级。
- 摘要未提供足够信息说明 Blender-Moments 与真实数据集的规模、场景类型与评价指标细节。
- 摘要未提供足够信息说明与 TSDF 融合或泊松重建相比，在细节提升上的定量证据。

### 阅读优先级
中。理由：论文针对动态高斯泼溅中“完整动态场景逐帧网格化”与“大幅快速运动”两个明确问题，提出可解释的运动建模与初始化方案，并配套带逐帧真值网格的新基准；若关注动态场景几何重建、逐帧网格提取或动态高斯表示，具有较高相关性。但摘要未给出定量结果、失败案例与计算开销细节，是否值得优先精读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

We present MEMO (a Mesh for Every MOment), a method that reconstructs the geometry of complete dynamic scenes, captured by multiple synchronized cameras, and extracts a mesh at every frame. Existing dynamic Gaussian splatting methods either model appearance alone or target isolated objects segmented by foreground masks, and all of them recover meshes by TSDF fusion or Poisson reconstruction, whose fixed grids limit the detail they can capture. At the core of MEMO is a per-Gaussian motion model inspired by Gaussian processes, which represents each Gaussian's position and rotation over time as a combination of temporal Gaussian kernels. The model keeps every Gaussian a valid surface element throughout the sequence and carries an implicit representation of the dynamic geometry, so a mesh can be derived at any time from a field defined by the Gaussians. Although common in real captures, large and fast motion poses a challenge that dynamic Gaussian splatting methods usually overlook. To account for it, we design a track-based initialization scheme that fits each Gaussian's initial trajectory to point tracks in closed form. We evaluate MEMO on Blender-Moments, a new benchmark of nine animated scenes with ground-truth meshes at every frame, and on two real-world datasets. MEMO reconstructs the most accurate geometry among state-of-the-art methods, and remains competitive in novel-view synthesis and training time. Project page: https://memo-4d.github.io

</details>

#### 2026-11-25 - MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References

**Authors:** Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher
**Links:** [abs](https://arxiv.org/abs/2611.34932) - [pdf](https://arxiv.org/pdf/2611.34932)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** structure from motion, Gaussian Splatting, 3D Gaussian Splatting, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MERLoc: Robust Robot Localization in Dynamic Environments with Pose-Based Retrieval over 3D Gaussian Splatting References
- 作者：Michael Baumgartner, Dario Mylonopoulos, Sammy Christen, Markus Gross, Moritz Bacher
- 出版日期：2026-11-25T18:59:23Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2611.34932；PDF https://arxiv.org/pdf/2611.34932

### 一句话总结
MERLoc 将单次度量的 3D Gaussian Splatting 扫描构建为稠密的“功能性参考记忆”，并用基于位姿的空间邻近与视角方向检索参考视图，以提升动态环境中机器人定位对场景变化和重复结构的鲁棒性。

### 研究问题
机器人在已建图空间中运行时，需要在有人走动、物体被重新摆放的情况下仍能准确定位。摘要指出，现有大多数定位流程依赖外观检索得到的稀疏参考图像集合，在场景变化和重复结构下较为脆弱。论文要解决的是：如何减少对外观检索的依赖，并在动态场景中获得更稳健的参考视图选择与定位表现。

### 核心思路/方法
- 将一次度量 3D Gaussian Splatting 扫描转化为稠密的 Functional Reference Memory。
- 根据机器人形态与传感器，在可导航空间内以目标密度采样参考视图，并离线渲染。
- 对所选现成定位器预先编码参考视图，从而在推理阶段移除参考编码器。
- 采用基于位姿的检索策略：存在先验时，按空间邻近和观察方向选择参考，而非按外观选择，以规避视觉歧义。
- 在仿真与真实动态场景中，与一种经典定位器和四种学习型定位器结合评估。

### 主要贡献
- 提出 MERLoc，将 3D Gaussian Splatting 扫描用于构建稠密参考记忆，并支持按机器人形态和传感器进行参考视图采样与离线渲染。
- 提出基于位姿的参考检索策略，在存在先验时替代外观检索，降低场景变化与重复结构带来的视觉歧义影响。
- 摘要报告：在多数情况下，基于位姿的检索匹配或优于外观检索，即使外观检索也受同一先验门控；在真实数据上，十个后端/划分组合中有九个将位置 RMSE 降低 15–60%。
- 摘要报告：渲染记忆优于由 Structure-from-Motion 位姿化的真实图像缓存；系统在 Jetson Orin NX 上以 5 Hz 板载运行，并使导航策略成功穿越有人走动和物体被重新摆放的走廊。

### 局限性
- 摘要未提供足够信息说明方法对先验质量的依赖程度、先验缺失或退化时的表现。
- 摘要未提供足够信息说明 3D Gaussian Splatting 扫描的建图成本、存储开销及大规模场景扩展性。
- 摘要未提供足够信息给出各定位器、各场景下的完整失败案例与误差分布。
- 摘要未提供足够信息说明真实实验的规模、场景数量、传感器配置细节及基线公平性设置。
- 摘要未提供足够信息讨论 5 Hz 运行时的计算资源占用与实时性边界。

### 阅读优先级
中。理由：论文聚焦动态环境下机器人定位这一实际问题，且摘要给出了跨多种定位器、仿真与真实场景以及板载运行的定量结果，具有一定参考价值；但摘要未展开方法细节、失败模式和实验设置，是否值得深入阅读取决于读者对 3D Gaussian Splatting 参考表示、位姿检索和机器人定位鲁棒性的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Robots operating in previously mapped spaces must localize accurately despite moving people and rearranged objects. Most localization pipelines match the query against a sparse set of captured reference images retrieved by appearance, which is brittle under scene change and repeating structures. We present MERLoc, which turns a single metric 3D Gaussian Splatting scan into a dense Functional Reference Memory. Reference views are sampled over the navigable space for the robot's morphology and sensors at a target density and rendered offline. Pre-encoding them for the chosen off-the-shelf localizer removes the reference encoder from inference. A pose-based retrieval strategy then selects references by spatial proximity and viewing direction rather than appearance, sidestepping visual ambiguities whenever a prior exists. Across one classical and four learned localizers in simulated and real dynamic scenes, pose-based retrieval matches or outperforms appearance retrieval in most cases, even when the latter is gated by the same prior. On real data, it lowers position RMSE by 15-60 % in nine of ten backend/split combinations, and the rendered memory outperforms real-image caches posed by Structure-from-Motion. The system runs onboard a Jetson Orin NX at 5 Hz, enabling a navigation policy to successfully traverse a hallway with people roaming and rearranging objects.

</details>

#### 2026-11-25 - WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion

**Authors:** Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo
**Links:** [abs](https://arxiv.org/abs/2611.34810) - [pdf](https://arxiv.org/pdf/2611.34810)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion
- 作者：Yuyang Yin, Chenjie Cao, Xuhui Zuo, Yuning Gong, Pengfei Wang, Junta Wu, Zhenwei Wang, Yao Zhao, Tengfei Wang, Yunchao Wei, Chunchao Guo
- 出版日期：2026-11-25T17:58:06Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.34810 ；PDF https://arxiv.org/pdf/2611.34810

### 一句话总结
WorldExpand 将单张全景图的三维世界扩展表述为稀疏、互补且高分辨率全景观测的联合生成，以更少冗余的观测覆盖未观测区域，并输出可直接用于重建的带位姿全景图。

### 研究问题
从单张全景图构建完整三维世界时，大量场景区域未被观测。现有的全景视频式方法依赖密集序列生成来扩展空间覆盖，但存在相邻帧冗余大、长轨迹误差累积、独立生成的不同方向可能不一致等问题。论文要解决的核心问题是：在单全景世界扩展中“在哪里观测”以及“如何合成”稀疏但互补的高分辨率全景观测。

### 核心思路/方法
论文将单全景世界扩展重新表述为生成稀疏、互补、高分辨率全景观测，而不是密集序列。方法包含三个关键部分：
1. **Coverage-Guided View Selection**：使用场景自适应象限和基于 warp 的覆盖分数，确定信息量高的目标观测位置，即回答“在哪里观测”。
2. **Joint Panoramic Diffusion**：利用基于高斯泼溅的几何 warp，联合合成四张具有位姿约束且跨视角一致的全景图，即回答“如何合成”。
3. 诊断引导的全局—局部注意力调度：仅在敏感层保留全局注意力，以降低高分辨率联合生成的训练与推理成本。
生成得到的带位姿全景图可直接输入现有重建流程，构建显式三维表示。

### 主要贡献
- 提出将单全景世界扩展建模为稀疏、互补、高分辨率全景观测的生成，而非密集序列生成。
- 设计 Coverage-Guided View Selection，用场景自适应象限与 warp 覆盖分数选择信息量高的目标位置。
- 设计 Joint Panoramic Diffusion，借助高斯泼溅几何 warp 联合生成四张位姿约束、跨视角一致的全景图。
- 提出诊断引导的全局—局部注意力调度，降低高分辨率联合生成的训练和推理成本。
- 摘要称实验表明方法能恢复遮挡物后方和远处转角周围的内容，在新视角合成与下游三维重建指标上改善，并对多样真实场景具有稳健泛化能力；同时比最先进的全景视频方法运行显著更快，并产生更高分辨率、跨视角一致性更强的观测。

### 局限性
- 摘要未提供足够信息说明方法在极端稀疏视角或大范围完全未观测区域下的失败模式。
- 摘要未提供足够信息说明对重建流程的具体依赖程度及误差传播情况。
- 摘要未提供足够信息给出定量实验细节、数据集规模、计算资源与推理时延数值。
- 摘要未提供足够信息讨论生成全景的几何精度上限及跨视角一致性的定量衡量方式。

### 阅读优先级
高。理由：该论文针对单全景三维世界构建中的覆盖扩展与跨视角一致性问题提出明确的新表述与联合生成框架，且摘要声称在重建指标、分辨率、一致性和速度上均有改进；对神经场景表示、全景生成与三维重建交叉方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Constructing complete 3D worlds from a single panorama is challenging because large portions of the scene remain unobserved. Existing panoramic-video methods expand spatial coverage through dense sequential generation, but neighboring frames contain substantial redundancy, long trajectories accumulate errors, and independently generated directions may be inconsistent. We present WorldExpand, which formulates single-panorama world expansion as the generation of sparse, complementary, and high-resolution panoramic observations. This representation concentrates the generation budget on informative scene regions and preserves the fine-grained details required for 3D construction. WorldExpand addresses two key challenges: where to observe and how to synthesize. Our Coverage-Guided View Selection identifies informative target locations using scene-adaptive quadrants and warp-based coverage scores, while our Joint Panoramic Diffusion uses Gaussian-splatting-based geometric warps to jointly synthesize four pose-grounded and cross-view-consistent panoramas. A diagnostic-guided global--local attention schedule retains global attention only in sensitive layers, reducing the training and inference costs of high-resolution joint generation. The resulting posed panoramas can be directly fed into an existing reconstruction pipeline to build an explicit 3D representation. Experiments show that WorldExpand recovers content behind occluders and around distant corners, improves both novel-view synthesis and downstream 3D reconstruction metrics across various datasets, and generalizes robustly to diverse in-the-wild scenes. WorldExpand runs significantly faster than the state-of-the-art panoramic-video method while producing higher-resolution observations with stronger cross-view consistency.

</details>

#### 2026-11-25 - TACC: Target-Aware Carrier Compression for Dense-Context Novel View Synthesis

**Authors:** Yiming Fan, Yijia Guo, Zewen Guo, Liwen Hu, Yuheng Yuan, Yang Li, Zhiwei Li, Xitong Ling, Caihong Yuan, Shengbo Chen, Tiejun Huang, Lei Ma
**Links:** [abs](https://arxiv.org/abs/2611.34476) - [pdf](https://arxiv.org/pdf/2611.34476)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TACC: Target-Aware Carrier Compression for Dense-Context Novel View Synthesis
- 作者：Yiming Fan, Yijia Guo, Zewen Guo, Liwen Hu, Yuheng Yuan, Yang Li, Zhiwei Li, Xitong Ling, Caihong Yuan, Shengbo Chen, Tiejun Huang, Lei Ma
- 出版日期：2026-11-25T14:41:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.34476) | [PDF](https://arxiv.org/pdf/2611.34476)

### 一句话总结
论文提出面向前馈式潜在新视角合成的目标感知压缩模块 TACC，通过按源视图与目标视图的几何相关性动态选取 token，缓解密集输入下的全局场景 token 上下文带来的内存与延迟开销。

### 研究问题
前馈式新视角合成方法摆脱了逐场景优化，直接从输入视图推断 3D 表示，但其依赖全局场景 token 上下文，导致显著的内存和延迟开销，限制了处理日益密集的源视图上下文的能力。已有通用压缩方法固定且与目标无关，无法针对单个目标视图调整证据分配，因此不适合新视角合成任务。

### 核心思路/方法
TACC 是一个面向前馈潜在新视角合成的目标感知压缩模块。它将每个源视图组织为渐进式载体层次结构（progressive carrier hierarchy），并基于源视图与目标视图之间的几何相关性自适应检索 token，以动态分配精确的计算配额。这种选择性检索直接产生紧凑的、以目标视图为条件的表示。

### 主要贡献
- 指出现有通用压缩方法因固定、目标无关的特性而不适用于新视角合成，并提出目标感知压缩思路。
- 设计 TACC 模块：以渐进式载体层次组织源视图，依据源-目标几何相关性自适应检索 token，动态分配计算配额，形成紧凑的目标条件表示。
- 在 RE10K 上的实验表明，在密集输入设置下，TACC 在 LagerNVS 和 LVSM 上分别达到 Full Context 的 9.23 倍和 64 倍有效 FPS；有效 FPS 不包含一次性源编码与载体构建开销。

### 局限性
摘要未提供足够信息说明 TACC 的具体失败场景、对非密集输入的影响、载体构建开销的实际占比、与其他压缩方法的定量对比细节，以及除 RE10K 外的泛化表现。

### 阅读优先级
中。理由：该工作针对前馈式新视角合成中密集上下文带来的内存与延迟瓶颈，提出目标感知压缩思路，并在 RE10K 上报告了显著的有效 FPS 提升，与神经场景表示与渲染方向直接相关；但摘要未提供更广泛的实验细节与局限性分析，适合作为该方向效率优化问题的参考阅读。

</details>

<details>
<summary>Abstract</summary>

Recent feed-forward approaches mark a paradigm shift in novel view synthesis by eliminating the reliance on per-scene optimization, directly inferring 3D representations from input views. However, their reliance on global scene-token context incurs substantial memory and latency overhead, constraining their ability to handle increasingly dense source-view contexts. Compressing source representations offers an intuitive way to limit this token budget. Prior general-purpose compression methods are not tailored for novel view synthesis, as their fixed, target-agnostic nature fails to adapt evidence allocation to individual target views. To overcome this, we introduce TACC, a target-aware compression module tailored for feed-forward latent NVS. Specifically, TACC organizes each source view into a progressive carrier hierarchy. Driven by source-target geometric relevance, it adaptively retrieves tokens to dynamically allocate exact computational quotas. This selective retrieval directly yields a compact, target-conditioned representation. Extensive experiments on the RE10K demonstrate that under dense input settings, TACC achieves $9.23\times$ and $64\times$ higher Effective FPS than Full Context on LagerNVS and LVSM, respectively. Effective FPS excludes one-time source encoding and Carrier construction.

</details>

#### 2026-11-25 - Surf-Style: Surface-Based Scene Stylization

**Authors:** Wanrong Hong, Ancheng Lin, Mukesh Prasad, Jun Li
**Links:** [abs](https://arxiv.org/abs/2611.34062) - [pdf](https://arxiv.org/pdf/2611.34062)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, rendering, radiance, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Surf-Style: Surface-Based Scene Stylization
- 作者：Wanrong Hong, Ancheng Lin, Mukesh Prasad, Jun Li
- 出版日期：2026-11-25T09:36:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.34062) / [PDF](https://arxiv.org/pdf/2611.34062)

### 一句话总结
Surf-Style 通过在 3D 场景中重建物体表面，并基于表面定义可学习的外观模型，来实现跨视角一致且可局部控制的 3D 场景风格化。

### 研究问题
论文关注 3D 场景风格化中的跨视角一致性问题：将 2D 风格化方法独立应用于每个渲染视角，往往会导致不同视角之间的风格化结果不一致。现有基于隐式辐射场表示的方法虽然试图提升一致性，但由于像素外观与可学习场景参数之间是间接依赖关系，在优化过程中更新颜色存在歧义，难以强制实现一致的风格化。

### 核心思路/方法
论文提出 Surf-Style，其核心是在 3D 场景中重建物体表面，并利用这些表面实现几何一致性和局部化风格化。具体而言，Surf-Style 在 3D 空间上定义可学习的外观模型，并对该模型进行修改，以复现参考图像的视觉风格。摘要强调该方法相较现有先进方法具有更好的一致性，并在可控风格化方面提供更高灵活性，包括针对特定表面区域进行风格化以及组合不同风格。

### 主要贡献
- 提出 Surf-Style，一种基于表面的 3D 场景风格化方法，通过重建物体表面来获得几何一致性并支持局部化风格化。
- 在 3D 空间上定义可学习外观模型，并通过修改该模型复现参考图像的视觉风格。
- 摘要声称相较现有先进方法具有更优的一致性，并提供更灵活的可控风格化能力，包括面向特定表面区域和组合不同风格。
- 摘要未提供足够信息说明具体实验设置、定量指标、对比基线细节及用户研究结果。

### 局限性
- 摘要未提供足够信息说明方法对表面重建质量或几何误差的敏感程度。
- 摘要未提供足够信息说明其在大规模复杂场景、透明/反光材质或动态场景中的适用性。
- 摘要未提供足够信息说明计算开销、训练/优化时间及内存需求。
- 摘要未提供足够信息说明“组合不同风格”的具体实现方式与可能的风格冲突处理机制。
- 摘要未提供足够信息说明定量和定性实验的完整结果、失败案例及与基线方法的详细比较。

### 阅读优先级
中。理由：该论文主题属于神经场景表示与渲染中的 3D 风格化与跨视角一致性问题，问题定义清晰，方法思路基于表面重建与可学习外观模型，具有一定针对性；但当前仅提供摘要，缺少实验细节、定量结果和实现信息，是否值得深入阅读需结合全文中的实验充分性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Consistent and controllable 3D stylization is critical for visual computing applications such as immersive visualization, augmented and virtual reality content creation, and artistic scene rendering. While 2D image stylization has advanced significantly, extending these methods to 3D remains challenging due to the need for cross-view consistency, where stylized renderings must align across all viewpoints. Applying 2D stylization independently to each rendered view often results in inconsistencies across perspectives. Existing methods attempt to improve consistency by leveraging implicit radiance field representations, which model scene appearance as a function of spatial locations. However, these methods struggle with ambiguity in updating colors, as the indirect dependence between pixel appearance and learnable scene parameters makes it difficult to enforce consistent stylization during optimization. This work presents Surface-based Scene Stylization (Surf-Style), which reconstructs object surfaces in a 3D scene and uses these surfaces to achieve geometric consistency and localized stylization. Surf-Style defines a learnable appearance model over 3D space, which is modified to replicate the visual style of a reference image. Compared to state-of-the-art methods, our method achieves superior consistency and offers greater flexibility in controllable stylization, including the ability to target specific surface regions and combine different styles.

</details>

#### 2026-11-25 - UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis

**Authors:** Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim, Young-Min Kim, Hyeon-Jik Lee, Sang-Yun Kim, Hyeok-Jun Kwon, Hyuk-Sool Kwon, Hyeon-Min Bae
**Links:** [abs](https://arxiv.org/abs/2611.33920) - [pdf](https://arxiv.org/pdf/2611.33920)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis
- 作者：Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim, Young-Min Kim, Hyeon-Jik Lee, Sang-Yun Kim, Hyeok-Jun Kwon, Hyuk-Sool Kwon, Hyeon-Min Bae
- 出版日期：2026-11-25T07:39:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33920) / [PDF](https://arxiv.org/pdf/2611.33920)

### 一句话总结
论文提出 UPP-Gauss，将超声在组织中的传播物理先验引入显式高斯表示，用于合成 B-mode 超声图像的新视角，并在三个数据集上取得优于基线的重建质量。

### 研究问题
B-mode 超声图像的新视角合成需要同时建模声波在组织中的传播，以及探头位姿变化导致的成像外观变化。论文关注的问题是：如何把这类声学交互与传播规律有效整合到新视角合成模型中，以提高 B-mode 图像的重建质量。

### 核心思路/方法
UPP-Gauss 将超声传播相关的声学交互整合到显式高斯表示中。方法首先根据探头位姿和声束传播方向，对三个 3D 高斯场进行采样，构建声学图（acoustic maps）；随后按照超声传播规律组合这些声学图，以合成 B-mode 图像。

### 主要贡献
- 提出 UPP-Gauss，将超声传播物理信息融入显式高斯表示，用于 B-mode 新视角合成。
- 设计基于探头位姿与声束方向的三个 3D 高斯场采样流程，并将采样得到的声学图按超声传播规律组合以合成图像。
- 在三个声学特性不同的数据集上取得最佳重建质量，并保持高效渲染；相较每个数据集上的最佳基线，PSNR 平均提升 1.43 dB。

### 局限性
摘要未提供足够信息。论文未在摘要中说明方法的具体计算开销、对探头位姿或声学参数准确性的依赖程度、跨设备或跨组织泛化能力，以及失败情形等局限。

### 阅读优先级
中。理由：该工作面向 B-mode 超声新视角合成，将传播物理先验与显式高斯表示结合，主题明确且报告了平均 1.43 dB 的 PSNR 提升；但摘要未提供更详细的实验设置、对比方法、效率指标和局限性信息。是否优先精读，取决于读者对超声成像物理建模与高斯表示交叉方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Accurate novel-view synthesis of B-mode ultrasound images requires modeling acoustic propagation through tissue and the resulting appearance variations across probe poses. We propose Ultrasound Propagation Physics-informed Gaussian Splatting (UPP-Gauss), which integrates these acoustic interactions into an explicit Gaussian representation. UPP-Gauss constructs acoustic maps by sampling three 3D Gaussian fields using the probe pose and acoustic beam propagation direction, then combines these maps according to ultrasound propagation to synthesize B-mode images. Across three acoustically diverse datasets, UPP-Gauss achieves the best reconstruction quality with efficient rendering, improving PSNR over the best baseline on each dataset by 1.43 dB on average. These results demonstrate accurate and efficient B-mode novel-view synthesis through explicit Gaussian modeling of ultrasound propagation.

</details>

#### 2026-11-25 - Tortho-Gaussian++: Suppressing Geometric Drift and Floaters for Robust Gravity-Aligned TDOM Generation in Large-Scale Aerial Scenes

**Authors:** Xiang Wang, Xin Wang, Zongqian Zhan
**Links:** [abs](https://arxiv.org/abs/2611.33905) - [pdf](https://arxiv.org/pdf/2611.33905)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tortho-Gaussian++: Suppressing Geometric Drift and Floaters for Robust Gravity-Aligned TDOM Generation in Large-Scale Aerial Scenes
- 作者：Xiang Wang, Xin Wang, Zongqian Zhan
- 出版日期：2026-11-25T07:27:09Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.33905 ；PDF https://arxiv.org/pdf/2611.33905

### 一句话总结
提出 Tortho-Gaussian++ 这一 3DGS 训练框架，通过几何可观测性分析、优化器状态初始化改进与稳健重力方向估计，抑制几何漂移与浮尘伪影并自动裁剪外围不可靠区域，用于大规模航空场景的重力对齐 TDOM 生成。

### 研究问题
3D Gaussian Splatting 已用于航空场景重建并扩展到真数字正射影像图（TDOM）生成，但存在几何漂移、浮尘伪影以及重力对齐稳健性不足等问题；摘要指出这些问题会影响大规模航空场景下 TDOM 生成的稳健性。

### 核心思路/方法
摘要给出三部分方法：
1. 基于视线的几何可观测性分析，定量刻画每个高斯（Gaussian）的几何可靠性，并据此裁剪几何支撑特别弱的外围区域；
2. 在致密化过程中改进新建高斯（Gaussian）的优化器状态初始化，在不依赖外部先验的情况下从内在抑制漂移与浮尘；
3. 设计稳健的重力方向估计方案，结合图像导出的重力线索、相机分布先验与天底视角，获得用于 TDOM 渲染的重力对齐正交投影参考。

### 主要贡献
- 提出 Tortho-Gaussian++ 训练框架，用于抑制几何漂移与浮尘，并自动裁剪不可靠外围区域。
- 提出基于视线的几何可观测性分析，对高斯（Gaussian）的几何可靠性进行定量刻画并裁剪弱支撑外围区域。
- 改进致密化时新建高斯（Gaussian）的优化器状态初始化，内在抑制漂移与浮尘，无需外部先验。
- 设计结合图像重力线索、相机分布先验与天底视角的稳健重力方向估计方案，用于重力对齐 TDOM 渲染。
- 摘要称在多个大规模无人机数据集上，平均 PSNR 较原始 3DGS 提升 0.5–3.5 dB，与先验引导的 3DGS 方法性能相当或更优；训练时间、显存（VRAM）与高斯数量分别降低 45.5%、47.2%、58.6%。

### 局限性
摘要未提供足够信息说明方法的具体适用边界、失败情形或定量评估之外的局限。摘要提到的实验仅覆盖摘要所述的大规模无人机数据集；更广泛场景的泛化性、对不同数据条件的敏感性等，摘要未提供足够信息。

### 阅读优先级
中。理由：该工作面向 3DGS 航空重建与 TDOM 生成，问题明确且摘要给出了量化性能与资源开销收益；但摘要未展开方法细节与实验设置，是否与具体研究兴趣高度契合需进一步阅读全文判断。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has demonstrated remarkable performance in aerial scene reconstruction, motivating its recent extension to true digital orthophoto maps (TDOMs) generation. We propose Tortho-Gaussian++, a novel 3DGS training framework that suppresses geometric drift and floaters and automatically prunes unreliable peripheral regions, coupled with a robust gravity-aligned TDOM rendering solution. First, we explore geometric support via viewing-ray-based geometric observability analysis, quantitatively characterizing the reliability for each Gaussian and subsequently pruning peripheral regions with particularly weak geometric support. Second, the optimizer state initialization is refined for newly created Gaussians during densification, intrinsically suppressing drift and floaters without external priors. Lastly, a robust gravity direction estimation solution is designed, combining image-derived gravity cues, camera-distribution priors and nadir views, to achieve a gravity-aligned orthogonal projection reference for TDOM rendering. Extensive experiments on multiple large-scale UAV (Unmanned Aerial Vehicle) datasets demonstrate that our Tortho-Gaussian++ outperforms vanilla 3DGS by 0.5-3.5 dB in average PSNR and yields comparable or superior performance to prior-guided 3DGS methods. Notably, it reduces the training time, VRAM and Gaussian number by 45.5%, 47.2%, and 58.6%, respectively. Qualitative evaluations confirm that our method effectively suppresses drift and floaters, while robust gravity direction estimation reduces tilt-induced facade artifacts in TDOMs.

</details>

#### 2026-11-25 - SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training

**Authors:** Ryosuke Watanabe, Tomoaki Konno
**Links:** [abs](https://arxiv.org/abs/2611.33796) - [pdf](https://arxiv.org/pdf/2611.33796)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** surface reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training
- 作者：Ryosuke Watanabe, Tomoaki Konno
- 出版日期：2026-11-25T05:21:54Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33796) / [PDF](https://arxiv.org/pdf/2611.33796)

### 一句话总结
SprintGS 在 FastGS 基础上针对紧凑 3DGS 模型训练中仍存在的冗余光栅化与不随高斯数量收缩的损失计算开销进行优化，实现比 FastGS 更快且质量可比的训练。

### 研究问题
3D Gaussian Splatting（3DGS）虽能实时渲染逼真新视角，但其逐场景训练（优化）仍然较慢。近期如 FastGS 的快速训练方法通过减少高斯数量将训练缩短到数分钟，但作者对 FastGS 进行性能剖析后发现两类即使模型已紧凑仍存在的成本：一是光栅化仍是最大开销且其中仍有冗余工作；二是损失计算不随高斯数量减少而收缩，导致其在训练时间中的占比随模型紧凑化而上升。

### 核心思路/方法
SprintGS 是构建在 FastGS 之上的训练框架，目标是保持模型紧凑的同时降低上述两类成本：
- 针对光栅化：
  - 计划式瓦片剔除（scheduled tile culling）：使用粗略覆盖范围将每个高斯限制在其真正重要的瓦片上，并在训练结束前将该粗略范围退火至精确范围；
  - 收敛感知剪枝（convergence-aware pruning）：移除已收敛且近乎透明的高斯；
  - 洗牌高效反向传播（shuffle-efficient backward pass）：减少 GPU 线程间交换的数据。
- 针对损失：
  - 融合损失（fused loss）：在前向传播中直接计算损失及其图像梯度，无需损失图（loss map），从而移除其大部分成本。

### 主要贡献
- 识别并剖析了 FastGS 紧凑模型下仍存在的两类训练开销：光栅化冗余与不随高斯数量收缩的损失计算。
- 提出 SprintGS 训练框架，通过计划式瓦片剔除、收敛感知剪枝、洗牌高效反向传播与融合损失降低上述成本。
- 摘要报告：在质量可比情况下，SprintGS 训练速度比 FastGS 快 2.15 倍；在其高质量设置下快 1.81 倍。
- 摘要还称其可加速其他快速训练方法，以及动态、稀疏视角和表面重建场景。

### 局限性
- 摘要未提供足够信息说明计划式瓦片剔除中粗略覆盖范围的具体构造方式与退火调度细节。
- 摘要未提供足够信息说明收敛感知剪枝的收敛判据与剪枝阈值设定。
- 摘要未提供足够信息说明融合损失的具体数学形式及与标准损失的一致性保证。
- 摘要未提供足够信息说明实验数据集、评价指标、基线配置及“质量可比”的具体量化依据。
- 摘要未提供足够信息说明方法在更大规模场景、不同 GPU 架构或极端稀疏视角下的表现与失败情形。
- 摘要未提供足够信息说明“加速其他快速训练方法”的具体方法与范围。

### 阅读优先级
中。理由：该论文聚焦 3DGS 训练加速中的具体系统级冗余消除，问题定位清晰且报告了明确的加速比，对关注 3DGS 训练效率的读者有参考价值；但摘要未给出实验细节与质量量化结果，且方法建立在 FastGS 之上，若读者不熟悉 FastGS 或更关注渲染质量与泛化性，需进一步阅读全文验证。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) renders photorealistic novel views in real time, but its per-scene training (optimization) remains slow. Recent fast training methods such as FastGS shorten training to a few minutes by reducing the number of Gaussians. Profiling FastGS, we find two costs that remain even in its compact model. First, rasterization is still the largest cost, and redundant work remains in it. Second, the loss computation does not shrink with the number of Gaussians, so its share of the training time grows as the model becomes compact. We present SprintGS, a training framework built on FastGS that keeps the model compact and reduces both costs. For rasterization, scheduled tile culling limits each Gaussian to the tiles where it matters, using a coarse footprint that is annealed to the exact one before training ends; convergence-aware pruning removes converged, nearly transparent Gaussians; and a shuffle-efficient backward pass reduces the data exchanged between GPU threads. For the loss, a fused loss computes the loss and its image gradient in the forward pass without a loss map, removing most of its cost. SprintGS trains 2.15x faster than FastGS at comparable quality, and 1.81x faster in its high-quality setting. It also accelerates other fast training methods and dynamic, sparse-view, and surface reconstruction.

</details>

#### 2026-11-25 - Efficient Scene-Distribution-Aware Second-Order Optimization for 3D Gaussian Splatting

**Authors:** Hyunseung Son, Young Sun Choi, Youngsik Yun, Kibeom Hong, Youngjung Uh
**Links:** [abs](https://arxiv.org/abs/2611.33698) - [pdf](https://arxiv.org/pdf/2611.33698)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient Scene-Distribution-Aware Second-Order Optimization for 3D Gaussian Splatting
- 作者：Hyunseung Son, Young Sun Choi, Youngsik Yun, Kibeom Hong, Youngjung Uh
- 出版日期：2026-11-25T03:07:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33698) / [PDF](https://arxiv.org/pdf/2611.33698)

### 一句话总结
该论文针对 3D Gaussian Splatting 的多视角二阶优化成本高、视角选择存在冗余、像素处理有额外开销等问题，提出考虑场景覆盖的视角选择策略与两种联合处理/缓存复用实现策略，以更少优化时间取得更高 PSNR。

### 研究问题
3DGS 优化按单个训练视角更新高斯参数，更新次数达数万次。多视角批处理可降低对单个训练视角的依赖，二阶优化能以更大、结构化的参数变化减少更新次数；但更新次数减少后，每次二阶更新更正“只拟合当前更新所用视角”的机会更少，因此场景覆盖更重要。多视角二阶更新本身昂贵，像素采样可降成本，但仍存在两个问题：一是选择视角时未考虑重叠，导致部分视角冗余；二是已有工作对每个视角的采样像素分别处理，并从头重新计算 alpha compositing，带来额外开销。

### 核心思路/方法
- 提出一种视角选择策略，以减少不考虑重叠时造成的视角冗余，使每次二阶更新更关注场景覆盖。
- 引入两种实现策略：对多个视角的采样像素进行联合 pass 处理；复用渲染过程中缓存的 transmittance 与 accumulated color，以减少上述两类开销。

### 主要贡献
- 针对多视角二阶 3DGS 优化中的视角冗余问题，提出减少冗余的视角选择策略。
- 针对逐视角分别处理采样像素与重算 alpha compositing 的开销，提出联合 pass 处理与缓存复用两种实现策略。
- 摘要称在三个数据集上，该方法以不到采样二阶基线一半的优化时间达到更高 PSNR，SSIM 与 LPIPS 具有竞争力。

### 局限性
摘要未提供足够信息。例如具体数据集名称、基线配置、消融实验、内存开销、视角选择策略的细节与适用范围等，均无法仅据摘要判断。

### 阅读优先级
中。理由：该工作聚焦 3DGS 二阶优化的效率与场景覆盖问题，问题定位明确，并有速度与 PSNR 的摘要级结果；但摘要未给出数据集、实现细节和完整实验配置，是否值得深入阅读取决于读者对 3DGS 优化加速与二阶方法的关注程度。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) optimization updates the Gaussian parameters one training view at a time, tens of thousands of times. Unlike such single-view updates, multi-view batches reduce dependence on individual training views, and second-order optimization reduces the number of updates with larger, structured parameter changes. Because fewer updates leave fewer chances to correct a change that fits only the views used in one update, scene coverage becomes more important for each second-order update. Multi-view second-order updates, however, are expensive. Pixel sampling reduces this cost, but two issues remain. First, selecting views without considering overlap leaves some views redundant. To address this, we propose a view selection strategy that reduces this redundancy. Second, existing work processes the sampled pixels of each view in a separate pass and recomputes alpha compositing for these pixels from scratch. We introduce two implementation strategies that reduce both overheads by processing the sampled pixels of multiple views in joint passes and reusing the transmittance and accumulated color cached during rendering. On three datasets, our method reaches higher PSNR than the sampled second-order baseline in less than half its optimization time, with competitive SSIM and LPIPS.

</details>

#### 2026-11-25 - VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors

**Authors:** Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina
**Links:** [abs](https://arxiv.org/abs/2611.33591) - [pdf](https://arxiv.org/pdf/2611.33591)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors
- 作者：Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina
- 出版日期：2026-11-25T01:00:43Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.33591) / [PDF](https://arxiv.org/pdf/2611.33591)

### 一句话总结
VivaWorld 提出一种结合组合式混合 3D 表示与混合相机嵌入的框架，用于从单张图像生成几何与视角一致的长时程视频。

### 研究问题
长时程视频生成对交互式世界建模、物理智能与空间推理很重要，但在缺乏 3D 基础时，保持几何一致性和准确相机控制仍然困难。论文关注如何从图像出发生成几何与视角一致的长视频。

### 核心思路/方法
- 构建组合式混合 3D 表示：将保留观测场景几何与外观的重建点云，与提供完整物体几何（覆盖 360° 新视角）的生成纹理网格相结合。
- 引入连通区域过滤，去除不一致的漂浮组件，以支持稳健的跨视角重建。
- 提出混合相机嵌入，结合全局 Plücker 射线与物体锚定 Plücker 射线，以同时捕捉场景级相机运动和相机—物体关系。
- 通过控制适配器，将上述嵌入与视觉引导一起注入视频生成模型。

### 主要贡献
- 提出 VivaWorld 框架，用于从图像生成几何与视角一致的长视频。
- 设计结合重建点云与生成纹理网格的组合式混合 3D 表示。
- 引入连通区域过滤以提升跨视角重建稳健性。
- 提出融合全局与物体锚定 Plücker 射线的混合相机嵌入，并通过控制适配器注入视频生成模型。
- 摘要称实验显示其在视觉质量与相机控制方面达到 state-of-the-art，并支持可控新视角合成、长时程场景探索与物理 AI。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、计算开销、对输入图像的依赖条件或定量实验细节；相关局限性无法仅凭摘要判断。

### 阅读优先级
高。理由：该工作面向长时程视频世界模型中的几何一致性与相机控制难题，提出组合式 3D 先验与混合相机嵌入，且涉及新视角合成、长时程场景探索与物理 AI 等方向，与主分类 Neural Scene Representations & Rendering 及机器人/AR 应用分类均相关；但优先级判断仅基于摘要信息。

</details>

<details>
<summary>Abstract</summary>

Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D grounding. We introduce \textbf{VivaWorld}, a framework for generating geometry- and view-consistent long videos from an image. We first construct a compositional hybrid 3D representation that combines reconstructed point clouds, which preserve observed scene geometry and appearance, with generated textured meshes, which provide complete object geometry across $360^\circ$ novel views. We also introduce a connected-region filter removing inconsistent floating components for robust cross-view reconstruction and propose a hybrid camera embedding that combines global and object-anchored Plücker rays to capture both scene-level camera motion and camera-object relationships, and inject it together with the visual guidance into a video generation model via a control adapter. Extensive experiments show VivaWorld achieves state-of-the-art visual quality and camera control, while supporting controllable novel-view synthesis, long-horizon scene exploration, and physical AI. Project page is available at: https://research.nvidia.com/labs/sil/projects/vivaworld/

</details>

#### 2026-11-25 - ProPolar: Progressive Polar Decomposition for Implicit Neural Representations

**Authors:** Pureum Kim, Younggeon Ryu, Dongyoon Lee, Hae Beom Lee, Kyong Hwan Jin
**Links:** [abs](https://arxiv.org/abs/2611.33567) - [pdf](https://arxiv.org/pdf/2611.33567)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ProPolar: Progressive Polar Decomposition for Implicit Neural Representations
- 作者：Pureum Kim, Younggeon Ryu, Dongyoon Lee, Hae Beom Lee, Kyong Hwan Jin
- 出版日期：2026-11-25T00:30:14Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33567)｜[PDF](https://arxiv.org/pdf/2611.33567)

### 一句话总结
针对隐式神经表示（INR）训练中“先低频、后高频”的由粗到细特性，论文提出渐进式秩调度与秩感知学习率调度，以增强基于低秩子空间的动量优化方法。

### 研究问题
INR 在训练早期主要捕捉全局低频结构，随后再细化局部高频细节；但标准优化器并不感知这种由粗到细的学习行为。摘要指出，这类优化器会在动量缓冲中累积梯度矩阵，并在早期保留与主导低频方向不一致的分量，从而可能不利于后续高频细节的恢复。

### 核心思路/方法
论文面向“基于子空间的动量优化”进行改进，其中动量矩阵在低秩子空间内更新。具体提出两个组件：
1. **渐进增长的秩调度器（progressively growing rank scheduler）**：在训练过程中逐步扩展低秩子空间；
2. **秩感知学习率调度器（rank-aware learning-rate scheduler）**：在秩增长期间保持峰值学习率，使新增子空间能够贡献于细节恢复。

### 主要贡献
- 指出标准优化器对 INR 的由粗到细学习行为不敏感，并分析了动量缓冲中低频方向与不一致分量的问题。
- 提出渐进秩调度与秩感知学习率调度，用于增强低秩子空间动量优化。
- 在图像拟合、单图像超分辨率（SISR）和神经辐射场优化上进行实验；摘要称该方法相较竞争优化器改善了收敛与峰值重建质量，且最大收益出现在高频细化阶段。
- 摘要还提到针对 NeRF 的超参数优化（HPO）研究，确认在匹配搜索预算下收益仍然存在。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、内存占用或实现复杂度。
- 摘要未提供足够信息说明各任务上的完整实验设置、数据集规模、对比基线细节与消融实验范围。
- 摘要未提供足够信息说明秩调度的具体增长策略、超参数敏感性及失败情形。
- 摘要未提供足够信息说明该方法在 INR 之外或其他表示学习任务中的适用性。

### 阅读优先级
**中**。理由：该论文聚焦 INR 优化器与训练动力学，问题定位清晰，且涉及图像拟合、SISR 与 NeRF 多类任务；但摘要未给出足够实验细节与实现信息，是否值得优先精读取决于读者对 INR 优化策略或由粗到细训练机制的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Implicit neural representations (INRs) capture global low-frequency structure during the early stage of training and then refine localized high-frequency details, afterwards. However, standard optimizers are agnostic to the coarse-to-fine learning behavior of INRs. Such optimizers accumulate a gradient matrix in momentum buffer and retain components misaligned with the dominant low-frequency directions in the early stage. We propose a progressively growing rank scheduler and a rank-aware learning-rate scheduler for enhancing a subspace-based momentum optimization, where a momentum matrix is updated within a low-rank subspace. The rank schedule expands the subspace during training, and the scheduler holds the peak learning rate through rank growth so that the added subspace contributes to fine-detail recovery. Experiments on image fitting, single-image super-resolution (SISR), and neural radiance field optimization show that the proposed method improves convergence and peak reconstruction quality over competitive optimizers. The largest gains appear in the high-frequency refinement stage, mirroring the coarse-to-fine progression that the rank schedule targets. A significant study on hyperparameter optimization (HPO) on NeRF further confirms that these gains persist under matched search budgets.

</details>

#### 2026-11-24 - SplatWAM: Splatting World Action Models for Real-Time 3D Imagination

**Authors:** Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield
**Links:** [abs](https://arxiv.org/abs/2611.33467) - [pdf](https://arxiv.org/pdf/2611.33467)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering, splatting, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SplatWAM: Splatting World Action Models for Real-Time 3D Imagination
- 作者：Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield
- 出版日期：2026-11-24T21:43:32Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.33467 ；PDF https://arxiv.org/pdf/2611.33467

### 一句话总结
SplatWAM 是一种生成式世界模型，它直接在紧凑的三维高斯基元上学习动作条件动态，并支持从任意视角光栅化预测状态，从而在显式三维空间中实现实时新视角渲染与策略学习。

### 研究问题
摘要指出，典型世界模型在像素空间或潜空间中预测未来观测，这限制了它们直接表示真实三维场景演化的能力。论文试图解决的核心问题是：如何让世界模型直接在显式三维表示上建模动作条件动态，而不是依赖像素或潜空间预测，从而支持任意视角渲染和基于三维表示的下游策略学习。

### 核心思路/方法
论文提出 SplatWAM，其核心是在紧凑的三维高斯基元上学习动作条件动态，包含以下组件：
1. **SplatWAM-T**：一个 tokenizer，将数量可变的无位姿视角编码为固定预算的高斯 token。
2. **SplatWAM-D**：一个动态模型，针对每个动作在单次前向传播中预测未来高斯状态；使用对数欧几里得协方差坐标和可微渲染监督，以便在显式三维空间中学习。每个预测状态可从任意视角光栅化，从而在构造上强制跨视角共享同一三维表示。
3. **SplatWAM-P**：一个轻量级 flow-matching 策略头，与动态模型联合训练。

### 主要贡献
1. 提出直接在紧凑三维高斯基元上学习动作条件动态的生成式世界模型 SplatWAM，而非在像素或潜空间预测未来观测。
2. 设计 SplatWAM-T 将可变数量无位姿视角编码为固定预算高斯 token，并用 SplatWAM-D 在单次前向中预测未来高斯状态，结合对数欧几里得协方差坐标和可微渲染监督。
3. 在 OGBench Scene 上，SplatWAM 渲染新视角比视频世界模型快 12 倍（RTX 5090 上约 80 FPS），PSNR 最高高 2.0 dB。
4. 在 8 个任务套件上，无模型的高斯 token 策略相比像素基策略最高提升 24.8 个百分点；SplatWAM-P 相比 LPWM 提升 12 个百分点，并在无学习价值函数的情况下匹配 HIQL。
5. 在 LIBERO 上，约 1B 参数的模型优于 WorldVLA（约 7B）和机器人预训练的 OpenVLA（约 7B），在两者均不使用大规模机器人预训练时匹配 OpenVLA-OFT。
6. 摘要称将发布代码和检查点。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、计算资源需求细节、方法对特定场景或数据分布的依赖、高斯 token 固定预算带来的信息损失、训练稳定性或泛化边界等局限。

### 阅读优先级
**高**。理由：该论文直接针对世界模型中显式三维表示与动作条件动态结合的关键问题，提出完整的方法组件（tokenizer、动态模型、策略头），并在多个基准上报告了渲染速度、PSNR 和策略性能的定量提升；同时涉及实时三维想象与策略学习，主题与神经场景表示和渲染方向高度相关。但需注意，以上判断仅基于摘要信息，具体实验细节和可复现性需查阅全文。

</details>

<details>
<summary>Abstract</summary>

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We present SplatWAM (Splatting World Action Model), a generative world model that learns action-conditioned dynamics directly over compact 3D Gaussian primitives. A tokenizer SplatWAM-T first encodes a variable number of unposed views into a fixed budget of Gaussian tokens. A dynamics model SplatWAM-D then predicts future Gaussian states in a single forward pass per action, using log-Euclidean covariance coordinates and differentiable rendering supervision to facilitate learning in an explicit 3D space. Each predicted state can be rasterized from arbitrary viewpoints, enforcing a shared 3D representation across views by construction. On OGBench Scene, SplatWAM renders novel views 12x faster than video world models (~80 FPS on an RTX 5090) with up to 2.0 dB higher PSNR. We further introduce SplatWAM-P, a lightweight flow-matching policy head jointly trained with the dynamics model. Across 8 task suites, model-free Gaussian-token policies outperform pixel-based counterparts by up to 24.8 percentage points. SplatWAM-P improves over Latent Particle World Model (LPWM) by 12 percentage points and matches HIQL without a learned value function. On LIBERO, our ~1B model outperforms WorldVLA (~7B) and the robot-pretrained OpenVLA (~7B), while matching OpenVLA-OFT when both are trained without large-scale robot pretraining. Code and checkpoints will be released.

</details>

#### 2026-11-24 - FoamSurf: A Voronoi-Surfel Representation for Differentiable Rendering

**Authors:** Grzegorz Wilczyński, Julia Farganus, Krzysztof Byrski, Rafał Tobiasz, Mikołaj Zieliński, Dominik Belter, Przemysław Spurek
**Links:** [abs](https://arxiv.org/abs/2611.33462) - [pdf](https://arxiv.org/pdf/2611.33462)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** differentiable rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FoamSurf: A Voronoi-Surfel Representation for Differentiable Rendering
- 作者：Grzegorz Wilczyński, Julia Farganus, Krzysztof Byrski, Rafał Tobiasz, Mikołaj Zieliński, Dominik Belter, Przemysław Spurek
- 出版日期：2026-11-24T21:37:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33462) | [PDF](https://arxiv.org/pdf/2611.33462) | [项目页](https://grzegorzwilczynski.com/foamsurf/)

### 一句话总结
FoamSurf 提出一种混合表示：用平面高斯 surfel 建模固体表面、用空间填充 Voronoi 单元建模散射介质，并通过单一可微光线追踪器在任意光线上合成二者，从而在无分割掩码的情况下实现表面与介质的分离、独立编辑以及沿反射/折射光线的介质效果建模。

### 研究问题
论文针对散射介质场景（如水下、雾、烟）中的表面—介质联合建模问题，指出已有方法存在以下不足：
- 近期基于高斯的方法虽能生成散射介质场景的逼真图像，但仅表面渲染中仍可能残留介质痕迹；
- 神经场方法能更准确分离表面与介质，但训练慢且难以编辑；
- 上述两类方法都只沿相机光线评估介质，未建模介质在反射和折射光线上的效果。

这些限制导致难以可靠恢复表面、独立编辑表面与介质，以及一致地渲染插入物体。

### 核心思路/方法
- **混合表示**：表面采用平面高斯 surfel（planar Gaussian surfels）表示，介质采用空间填充 Voronoi 单元（space-filling Voronoi cells）表示。
- **统一可微光线追踪**：使用单一可微光线追踪器沿任意光线对表面与介质进行合成，从而覆盖反射与折射光线上的介质效应。
- **训练先验**：通过训练先验在无分割掩码的条件下保持表面与介质的分离。
- **下游能力**：恢复出的表面与介质组件可分别移除、编辑或风格化；同一重建支持插入网格物体，并在直接、反射与折射光线上计算衰减与散射。

### 主要贡献
- 提出 FoamSurf 这一表面—介质混合表示，结合平面高斯 surfel 与 Voronoi 介质单元。
- 用单一可微光线追踪器在任意光线上合成表面与介质，弥补已有方法仅沿相机光线评估介质的不足。
- 在无分割掩码条件下，借助训练先验实现表面与介质的分离。
- 摘要称在真实水下场景、合成场景和浓雾场景中，图像质量与当前最优方法相当，并在所比较方法中取得最准确的表面—介质分离。
- 支持组件级独立编辑与插入网格物体的一致渲染，指向场景恢复、编辑与合成的一体化能力。

### 局限性
摘要未提供足够信息。摘要未给出训练时间、计算开销、参数量、失败案例或对特定场景类型的适用范围限制等具体信息。

### 阅读优先级
**中**。理由：该论文关注散射介质中的表面—介质联合表示与可微渲染，问题定义清晰，且强调无掩码分离、任意光线介质建模与组件级编辑，对神经渲染与场景编辑方向具有潜在参考价值；但摘要未提供定量指标、实现细节与局限性信息，是否值得深入研读需结合全文实验与对比结果判断。

</details>

<details>
<summary>Abstract</summary>

Scenes inside a scattering medium contain solid surfaces, such as the seabed or rocks, and a semi-transparent medium, such as water, fog, or smoke. Recent Gaussian-based methods produce realistic images of scenes in scattering media, but traces of the medium can remain visible in surface-only renders. Neural fields separate surfaces and medium more accurately, but they are slow to train and difficult to edit. Both approaches evaluate the medium only along camera rays, so its effects along reflected and refracted rays are not modeled. These limitations prevent reliable surface recovery, independent editing of surfaces and the medium, and consistent rendering of inserted objects. We present FoamSurf, a hybrid representation that models surfaces with planar Gaussian surfels and the medium with space-filling Voronoi cells. A single differentiable ray tracer composites both along arbitrary rays, while training priors keep them separate without segmentation masks. Across real underwater scenes, synthetic scenes, and dense fog, FoamSurf achieves image quality on par with the state of the art and the most accurate surface-medium separation among the compared methods. The recovered components can be removed, edited, or stylized independently, and the same reconstruction supports inserted mesh objects with attenuation and scattering along both direct and reflected or refracted rays. Together, these capabilities enable scene restoration, editing, and composition within a single reconstructed model. Project page: https://grzegorzwilczynski.com/foamsurf/

</details>

#### 2026-11-24 - Synchronizing Cameras via 3D Object Relationships

**Authors:** Sujong Shin, Sang-Il Choi, Kwang Moo Yi
**Links:** [abs](https://arxiv.org/abs/2611.33387) - [pdf](https://arxiv.org/pdf/2611.33387)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Synchronizing Cameras via 3D Object Relationships
- 作者：Sujong Shin, Sang-Il Choi, Kwang Moo Yi
- 出版日期：2026-11-24T20:10:55Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33387) / [PDF](https://arxiv.org/pdf/2611.33387)

### 一句话总结
论文提出利用 3D 空间中物体之间的关系（如两人之间的距离）作为跨视角稳定的对齐线索，对同一动态事件的多个视频进行时间同步。

### 研究问题
多相机拍摄同一动态事件时，如何实现视频间的时间同步。摘要指出，近期受动态重建和新视角合成驱动的同步方法多依赖像素级证据，如跨视角点对应或重建场景的光度损失；但在动态场景中，快速运动和遮挡使承载大量时间信息的运动区域难以跨视角匹配。论文因此关注：能否不依赖难以匹配的像素级运动区域，而用更稳定的全局线索完成同步。

### 核心思路/方法
- 核心思想：回归“物体是相机全局推理可靠线索”的传统思路，用物体间关系进行对齐。
- 关系线索：以 3D 度量物体间关系（例如两个人之间的距离）；这类关系在所有视角下仅相差尺度而保持稳定，可作为对齐线索。
- 获取物体身份：将每个相机的少量帧输入视觉语言模型，提示其识别场景中的物体；由于线索是关系性的，跨相机比较时只需每个视角中每个物体的身份。
- 分割与跟踪：使用开放词汇分割器在每个视频中分割并跟踪每个已识别物体。
- 获取 3D 位置：使用预训练深度估计器获得物体的 3D 位置。
- 补充线索：在深度或分割失败处，用点轨迹提供的 2D 运动补充 3D 线索。
- 同步求解：寻找使不同相机线索最一致的时间偏移；先对每个相机对求解，再通过鲁棒优化对所有相机联合求解。

### 主要贡献
- 提出以 3D 物体关系作为跨视角稳定的同步线索，而非依赖动态场景中易受快速运动和遮挡影响的像素级证据。
- 构建了一套结合视觉语言模型物体识别、开放词汇分割与跟踪、预训练深度估计以及点轨迹 2D 运动补充的流程，用于提取和比较跨相机的物体关系线索。
- 采用先相机对、后全体相机联合的鲁棒优化策略求解时间偏移。
- 摘要称在四个标准基准上评估并优于当前最优方法。

### 局限性
- 摘要未提供足够信息说明方法在物体识别失败、开放词汇分割跟踪失败或深度估计严重错误时的整体鲁棒性边界。
- 摘要未提供足够信息说明“仅相差尺度”的假设在实际场景中的适用条件与失效情形。
- 摘要未提供足够信息说明四个标准基准的具体构成、评价指标、定量结果和消融实验细节。
- 摘要未提供足够信息说明视觉语言模型识别物体身份的准确率及其对最终同步性能的影响。
- 摘要未提供足够信息说明计算开销、运行时间或对相机数量与视频长度的扩展性。

### 阅读优先级
中。理由：论文针对多视频时间同步中动态区域难以匹配的问题，提出较清晰的替代思路，即用 3D 物体关系作为稳定线索，并给出从物体识别、分割跟踪、深度估计到鲁棒同步优化的完整流程；摘要声称在四个标准基准上优于当前最优方法。但摘要未给出定量结果、失败案例和计算成本等关键细节，是否值得优先精读取决于读者对动态多视角同步或神经场景表示与渲染方向的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

In this paper, we synchronize multiple videos of the same dynamic event through object relationships. Driven by dynamic reconstruction and novel view synthesis, many recent synchronization methods rely on pixel-level evidence, such as point correspondences across views or the photometric losses of a reconstructed scene. In dynamic scenes, however, fast motion and occlusions make the moving regions that carry much of the timing information hard to match across views. We thus propose to bring back the traditional wisdom that objects are reliable cues for global reasoning about cameras. Measured in 3D, the relationships between objects, such as the distance between two people, are stable across all views up to scale; they can serve as cues for alignment. To compare these relationships across cameras, we only need the identity of each object in every view, as the cues are relational. We obtain these identities by giving a vision-language model a few frames of every camera and prompting it to identify the objects in the scene. We then segment and track each identified object through every video with an open-vocabulary segmentor. To obtain the 3D locations of objects, we use a pretrained depth estimator. Where depth or segmentation fails, we complement these 3D cues with 2D motion from point tracks. Finally, we synchronize the cameras by finding the temporal offsets at which the cues of different cameras agree best, first for each camera pair and then for all cameras jointly with robust optimization. We evaluate our method on four standard benchmarks, outperforming the state of the art.

</details>

#### 2026-11-24 - FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots

**Authors:** Mario Gomez Andreu, Carlos Martinez Cuenca, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Marco Hutter, Jesus Tordesillas
**Links:** [abs](https://arxiv.org/abs/2611.33380) - [pdf](https://arxiv.org/pdf/2611.33380)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, view synthesis, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FOCI: Trajectory Optimization on Gaussian Splats for Gaussian Robots
- 作者：Mario Gomez Andreu, Carlos Martinez Cuenca, Maximum Wilder-Smith, Victor Klemm, Vaishakh Patil, Marco Hutter, Jesus Tordesillas
- 出版日期：2026-11-24T20:05:59Z
- 分类：Neural Scene Representations & Rendering（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2611.33380)｜[PDF](https://arxiv.org/pdf/2611.33380)

### 一句话总结
论文提出 FOCI，一种直接在 3D Gaussian Splatting（3DGS）上优化机器人轨迹的算法，用高斯间重叠积分构建可解释的碰撞表示，并让环境与机器人均以 Gaussian Splats 表达，从而实现方向感知的狭窄空间规划。

### 研究问题
3DGS 已作为 NeRF 的快速替代方案用于三维重建与视图合成，本文希望利用 3DGS 编码的空间信息，解决机器人轨迹优化中的碰撞建模问题。摘要指出，已有方法常用保守包围盒表示机器人，会低估环境的可通行性；本文关注的是如何避免这种保守性，并支持多种机器人形态与静态、动态高斯场景下的轨迹优化。

### 核心思路/方法
FOCI（Field Overlap Collision Integral）直接在 Gaussians 上优化轨迹，其核心是一种基于高斯间“重叠积分”概念的碰撞公式，作者强调该公式新颖且可解释。方法适用于不同机器人形态（固定基座与移动基座机械臂、腿足机器人、UAV），并能处理静态与动态 Gaussian-Splat 环境。与环境表示相对应，机器人也表示为 Gaussian Splats，而非保守包围盒；摘要称这种表示具有有利的计算性质，并支持方向感知规划，使机器人能够通过非常紧窄的空间。

### 主要贡献
- 提出 FOCI 算法，可直接在 3DGS 高斯上进行轨迹优化。
- 提出基于高斯间重叠积分的碰撞表示，具有可解释性。
- 将环境与机器人都表示为 Gaussian Splats，避免保守包围盒对可通行性的低估，并支持方向感知规划。
- 方法覆盖固定/移动基座机械臂、腿足机器人与 UAV，且支持静态与动态高斯环境。
- 摘要称在合成与真实 Gaussian Splats 上进行了广泛测试，即使环境包含数十万高斯，也能在数秒内为腿足、空中与机械臂机器人计算出无碰撞轨迹；代码已公开。

### 局限性
摘要未提供足够信息来系统说明局限性。可确认的边界是：方法聚焦于基于 3DGS 的轨迹优化与碰撞表示，摘要未给出失败案例、定量成功率、实时性在更大规模或更复杂动态场景下的表现，也未说明对高斯重建质量或参数设置的敏感性。上述方面均“摘要未提供足够信息”。

### 阅读优先级
高。理由：该论文直接面向 3DGS 与机器人轨迹优化的交叉问题，提出可解释的碰撞公式和“机器人也用 Gaussian Splats 表示”的非保守建模范式，摘要声称覆盖多种机器人形态、静态/动态环境并在数十万高斯规模下数秒求解，且代码开源；对关注神经场景表示用于机器人规划与控制的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods. Leveraging the spatial information encoded in 3DGS, this work proposes FOCI (Field Overlap Collision Integral), an algorithm that is able to optimize trajectories directly on the Gaussians themselves. FOCI leverages a novel and interpretable collision formulation for 3DGS using the notion of the overlap integral between Gaussians. The formulation presented applies to different robot morphologies (e.g., fixed and mobile base manipulators, legged robots, UAVs) and handles both static and dynamic Gaussian-Splat environments. Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot as Gaussian Splats. This not only has desirable computational properties, but also allows for orientation-aware planning, allowing the robot to pass through very tight and narrow spaces. We extensively test our algorithm in both synthetic and real Gaussian Splats, showcasing that collision-free trajectories for legged, aerial and manipulator robots can be computed in seconds, even with hundreds of thousands of Gaussians making up the environment. The code is available at https://github.com/leggedrobotics/foci

</details>

#### 2026-11-24 - Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild

**Authors:** Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng
**Links:** [abs](https://arxiv.org/abs/2611.33145) - [pdf](https://arxiv.org/pdf/2611.33145)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lost on Campus: Evaluating Embodied Spatial Reasoning of Vision-Language Models in the Wild
- 作者：Zehan Zheng, Yanyuan Chen, Deming Li, Yutao Tang, Jianwen Xie, Alan Yuille, Jieneng Chen, Cheng Peng
- 出版日期：2026-11-24T18:57:48Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33145) | [PDF](https://arxiv.org/pdf/2611.33145)

### 一句话总结
论文提出“Lost on Campus”基准，用于在大规模真实户外3D环境中评估视觉语言模型的具身空间推理能力，并揭示现有模型在户外场景中的显著不足。

### 研究问题
现有具身空间推理评测多基于静态图像或合成室内环境，语义捷径可能足以应对，难以真实反映模型在开放世界中的空间推理能力。论文关注：如何在大规模真实户外3D环境中，对视觉语言模型的具身空间推理进行更忠实的评估。

### 核心思路/方法
论文构建了名为“Lost on Campus”的基准，基于3D Gaussian Splatting重建的大规模真实户外3D环境。该基准引入统一的“推理—行动”评估框架，将用于孤立推理的诊断式问答与多模态指令下的闭环交互导航相结合。为进行细粒度诊断，评估涵盖六个能力方面：动作 grounding、空间前瞻、度量感知、目标导向规划、自我中心—异中心定位、时空一致性。

### 主要贡献
- 提出面向真实户外3D环境的具身空间推理基准“Lost on Campus”，基于3D Gaussian Splatting重建场景。
- 设计统一的推理—行动评估框架，兼顾诊断式问答与闭环交互导航。
- 从六个能力维度对具身空间推理进行细粒度评估。
- 实验发现包括：真实户外环境比室内环境对空间推理要求更高，现有模型表现较差；视觉语言模型在细粒度视觉对齐上仍有困难，空间前瞻与自我中心—异中心定位是主要瓶颈；提升多模态交互能力与长期空间推理对推进具身智能至关重要。

### 局限性
摘要未提供足够信息。论文摘要未说明基准规模、模型数量、具体实验设置、评价指标细节及方法本身的适用范围限制。

### 阅读优先级
高。理由：该论文直接针对具身空间推理评测中“静态图像或合成室内环境”与真实开放世界之间的差距，提出真实户外3D环境基准与推理—行动统一评估框架，并给出明确的能力瓶颈发现，对视觉语言模型具身评估方向具有较强参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：AnyPrune: Optimization-Free Pruning for Any Feedforward 3D Gaussian Splatting Pipeline
- 作者：Nicola Leonetti, Federico Stella, Aoxiang Fan, Saqib Javed, Pascal Fua, Luigi Di Stefano
- 出版日期：2026-11-24T14:50:30Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.32735) / [PDF](https://arxiv.org/pdf/2611.32735)

### 一句话总结
AnyPrune 是一个基于 Transformer、无需重新优化的剪枝模块，可叠加在任意前馈 3DGS 流水线上，通过短时单 GPU 训练学习目标流水线特有的冗余模式，从而在保持或改善渲染质量的同时大幅减少高斯数量与内存存储开销。

### 研究问题
前馈 3DGS 流水线通过单次前向传播从图像重建可实时渲染的 3D 高斯，但所得表示包含远超忠实渲染所需的高斯数量，尤其当输入视图较多时，内存与存储需求急剧增加。现有剪枝方法要么需要昂贵的重新优化，违背单次前向传播的初衷；要么依赖简单策略，未充分利用可用信息。因此需要一种无需优化、可通用适配任意前馈 3DGS 流水线的剪枝方案。

### 核心思路/方法
AnyPrune 被设计为一个基于 Transformer 的、无优化剪枝模块，位于任意前馈 3DGS 流水线之上。它在冻结的目标前馈流水线上进行短时单 GPU 训练，学习并利用该流水线特有的冗余模式来移除不必要的高斯。摘要未提供足够信息说明其具体网络结构、训练损失或剪枝决策机制。

### 主要贡献
- 提出 AnyPrune，一个无需优化、基于 Transformer 的剪枝模块，可工作于任意前馈 3DGS 流水线之上。
- 通过在冻结目标流水线上的短时单 GPU 训练，学习流水线特定的冗余模式以移除不必要高斯。
- 在多数设置下，渲染质量优于现有无优化剪枝方法，并能泛化到未见数据集；摘要称通过跨多个前馈流水线、数据集和输入视图数量的广泛实验验证。
- 在消费级 GPU 上约 5 秒剪枝 1.6M 高斯场，快于所有合并高斯或重新优化场的方法。
- 可与前馈流水线内置剪枝结合，在中等剪枝比例下进一步剪枝，同时保持或改善渲染质量。
- 可建议场景特定的剪枝比例，以保留大部分质量。

### 局限性
摘要未提供足够信息说明方法在极端剪枝比例、训练数据分布偏移或不同硬件条件下的具体表现；也未提供失败案例、计算开销的详细分解或与所有基线方法的完整定量对比。摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对前馈 3DGS 的存储与内存瓶颈提出通用、无需优化的剪枝模块，问题定义清晰且实用性强，摘要报告了速度与质量上的优势；但摘要未给出具体定量结果、方法细节与充分局限性分析，需阅读全文才能判断其通用性与实际收益。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Completion-Aware Compression for Progressive 3D Gaussian Splatting
- 作者：Reagan Koo, Yeong-Gyu Kim, Eun-Seok Ryu
- 出版日期：2026-11-24T13:51:18Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.32628) / [PDF](https://arxiv.org/pdf/2611.32628)

### 一句话总结
本文提出一种面向渐进式 3D Gaussian Splatting 的编解码器，在单一紧凑码流中按任意已接收字节预算进行细粒度更新，并在属性保真度与高斯“提前可用”带来的图像收益之间做完成度感知的分配。

### 研究问题
3DGS 场景表示体积大、传输成本高；剪枝与压缩虽能减小文件，但渐进传输还要求在完整场景到达前就能获得可用重建。现有渐进表示虽能提供部分场景，但其基于层级的更新受预定义编码边界限制，灵活性不足。

### 核心思路/方法
论文提出一种渐进式 3DGS 编解码器，核心是在分配编码资源时同时考虑属性保真度与“让高斯更早可用”的图像收益，即完成度感知分配（completion-aware allocation）。其单一紧凑码流支持部分 3D 重建，随着字节到达逐步加入新解码的高斯；并支持在任意已接收字节预算下进行细粒度更新，无需单独编码，也无需后续属性细化。

### 主要贡献
- 提出支持任意接收字节预算下细粒度更新的渐进式 3DGS 单码流编解码方案。
- 引入完成度感知分配，在属性保真度与高斯提前可用所带来的图像收益之间取得平衡。
- 摘要报告：在匹配完整文件大小与接收字节数时，完成度感知分配相比仅属性分配在 1/8 PSNR 上提升 0.48–1.43 dB。
- 摘要报告：所提编解码器将原始 3DGS 表示压缩 62–88 倍，同时保持接近参考的 Full PSNR；在评估的 50-Mbps 传输模型下，约 0.2 秒即可获得部分重建。

### 局限性
摘要未提供足够信息说明以下方面：具体数据集与场景类型、基线方法的完整设置、编码复杂度与解码端计算开销、不同网络条件下的鲁棒性、主观视觉质量评估，以及“近参考 Full PSNR”的具体数值定义与误差范围。

### 阅读优先级
中。理由：该工作聚焦 3DGS 渐进传输与压缩这一明确且实用的问题，摘要给出了压缩比、PSNR 增益和部分重建时延等量化结果；但摘要未展开方法细节、实验覆盖与复杂度分析，是否值得深入阅读需结合全文中的实验设置与对比完整性进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Mind the Band: The Hidden Frequency Variable in Geometric RoPE
- 作者：Seonghyun Jin, Youngmin Kim, Jong Chul Ye
- 出版日期：2026-11-24T08:21:24Z
- 分类：Neural Scene Representations & Rendering（未提供二级分类）
- 链接：[摘要](https://arxiv.org/abs/2611.32171)｜[PDF](https://arxiv.org/pdf/2611.32171)

### 一句话总结
论文指出几何 RoPE 中的“频带”是被忽视却会改变基准排序的隐藏变量，并给出频带设置与梯度稳定性的分析及实用准则。

### 研究问题
几何旋转位置编码（RoPE）通过按视射线、深度和重投影图像坐标旋转 token 特征，将 3D 相机几何引入多视图注意力。每个坐标是在一系列频率上旋转的，这构成其“频带”。但现有实现把频带留给继承默认值：要么沿用标准 2D RoPE 的最高频率，要么让频率跨度随注意力头维度指数增长。论文要回答的是：这种未标准化的频带设置会带来什么影响，以及应如何设置频带。

### 核心思路/方法
- 将频带视为几何 RoPE 中的关键变量，系统考察其对多视图任务的影响。
- 在 RealEstate10K 新视图合成中比较不同模型规模与头尺寸下的表现，并单独改变头尺寸以验证排序反转现象。
- 在固定模型宽度、48 通道头的情况下，用四个频率填充 243 倍范围（对比默认 3 倍范围），观察性能恢复情况。
- 跨越视图合成与双视图深度估计，分析频带过窄与过宽的影响。
- 针对过宽频带的退化，论文从“前向—反向不对称”角度解释：对预测深度区间上的旋转取平均会在前向中压制高频，但关于预测深度的对应梯度未被同等压制；并通过仅阻断这些高频深度梯度来检验该解释。

### 主要贡献
- 揭示几何 RoPE 中频带设置未标准化，且该设置可能逆转基准排名：RayRoPE 在 47M 模型（144 通道头）中与最强基线持平，但在 25M 模型（48 通道头）中落后 1.2 dB；在固定模型宽度、仅改变头尺寸时也出现相同反转。
- 给出频带过窄的恢复证据：在 48 通道下用四个频率填充 243 倍范围，可挽回该差距中的 0.9 dB。
- 指出过窄频带会一致地模糊对应关系；当最高频率位于每 8 像素块 0.3–3 次旋转（在 256×256 RealEstate10K 上为 10–90 次旋转）时，三种基于投影的编码均表现可靠。
- 解释过宽频带导致 RayRoPE 退化的前向—反向不对称机制；仅阻断高频深度梯度可恢复 90–93% 的损失 PSNR，说明前向平滑不保证反向稳定。
- 提炼实用准则：在图像坐标中设置频带、在小头中填充跨度、避免无条件的同视图阻尼；并倡导未来多视图基准报告并匹配频带。

### 局限性
摘要未提供足够信息说明计算开销、跨数据集的泛化边界、其他几何编码的适用性，以及所提准则的完整消融范围。论文的结论主要基于摘要所述的新视图合成与双视图深度估计设置，其他任务与模型配置下的表现摘要未提供足够信息。

### 阅读优先级
高。理由：该文直指几何 RoPE 中容易被忽略但可能改变基准结论的频带变量，并同时给出排序反转证据、机理解释与可操作准则，对多视图注意力与位置编码相关研究及基准比较具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：View Management with Gaussian Placement and Opacity Regularization for Online 3DGS
- 作者：Dong Hwi Kim, Park Sangwon, Chaehyeon Song, Ayoung Kim
- 出版日期：2026-11-24T06:08:33Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.32025)｜[PDF](https://arxiv.org/pdf/2611.32025)

### 一句话总结

针对在线 3DGS 建图中地图因稀疏视角而过拟合的问题，论文从视角管理和高斯模型复杂度控制两方面提出改进：渐进引入非关键帧并分配更新预算，以及边缘引导初始化和自参考不透明度正则化。

### 研究问题

在线 3DGS 建图与 SLAM 结合后，地图仍沿用传统 SLAM 设计：只在为定位选出的关键帧上训练，并用不确定的前端深度正则化几何。这些设计忽视了 3DGS 地图的模型复杂度问题——参数达数百万，而每个区域可见视角很少，导致地图对稀疏输入过拟合。同时，每增加一个视角或高斯都需竞争同一实时预算，使问题更难解决。

### 核心思路/方法

论文从“视角”和“高斯”两侧同时入手：

1. **视角管理**：为在保留关键帧所维持的地图结构的同时增加视角，随着建图更新完成，渐进接纳非关键帧图像；并将有限更新按各组帧提供的监督量分配。
2. **边缘引导初始化**：在图像细节需要的位置放置新高斯，以控制地图模型复杂度。
3. **自参考不透明度正则化（SOR）**：利用累积的渲染证据（不增加额外渲染开销），抑制那些持续出现在“由地图导出的表面参考”前方的、具有不透明度的高斯，以弥补前端深度的不确定性。

### 主要贡献

- 提出渐进接纳非关键帧并跨帧组分配更新预算的视角管理策略，在不破坏关键帧结构的前提下增加建图视角。
- 提出边缘引导的高斯初始化，将新高斯放置于图像细节所需处，以控制地图复杂度。
- 提出 Self-Referenced Opacity Regularization（SOR），以无额外渲染成本的累积渲染证据抑制不合理的前景高斯不透明度，补充不确定的前端深度。
- 摘要称上述设计在实时预算内同时改善在线地图的外观与几何。

### 局限性

- 摘要未提供足够信息说明方法的定量实验结果、对比基线及评测数据集。
- 摘要未提供足够信息说明实时预算的具体数值、系统运行平台与帧率表现。
- 摘要未提供足够信息说明 SOR 中“地图导出的表面参考”的具体构建方式及其失效条件。
- 摘要未提供足够信息说明方法对前端深度质量、关键帧选择策略的敏感性与适用范围。

### 阅读优先级

**中**。理由：该论文直接针对在线 3DGS-SLAM 中稀疏视角过拟合与实时预算竞争这一实际问题，视角管理与不透明度正则化的思路对相关方向有参考价值；但摘要未给出任何定量结果与实验设置，无法据此判断改进幅度，建议在需要了解在线 3DGS 建图优化策略时阅读全文验证。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：HiGS: A Hierarchical Architecture for Fast Differentiable 3D Gaussian Splatting
- 作者：Dawid Pająk, Martin Bisson, Rodolfo Lima, François Trudel
- 出版日期：2026-11-24T04:23:36Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.31918) / [PDF](https://arxiv.org/pdf/2611.31918)

### 一句话总结
HiGS 提出一种层次化分块的高斯泼溅统一架构，为分区、光栅化与并行处理采用不同粒度，并用有界深度排序批次同时支撑渲染与重建，以降低稠密区域对帧时间的支配并加速训练。

### 研究问题
摘要指出，3D Gaussian Splatting 将同一屏幕 tile 同时作为分区单元、光栅化单元和并行工作单元。分区偏好较大的 tile，而光栅化偏好较小的 tile；每个 tile 只有一个工作单元时，最稠密的 tile 会决定帧时间。论文关注这种粒度冲突以及稠密区域导致的负载不均问题，同时关注重建训练中的优化器内存开销。

### 核心思路/方法
HiGS 将各角色的粒度分开：高斯在粗粒度 macro-tile 上分区，在其内部的细粒度 render tile 上光栅化，并以有界、深度排序的批次处理。稠密区域会发出更多批次，而不是形成一个更长的工作单元，从而使帧时间跟随着视图中的实际工作量，而不是由最稠密的 tile 决定。相同的批次也承载重建：合成过程提供区分每个批次所需的透射率和颜色，使各批次可独立求导，优化器内存流量成为主要训练成本。方法将优化器融合进反向传播，直接存储和更新的参数与动量减半，并把外观更新推迟到视图之外。

### 主要贡献
- 提出 HiGS 层次化分块架构，为分区、光栅化和并行处理分别采用粗 macro-tile、细 render tile 与有界深度排序批次。
- 使帧时间随视图工作量变化，而不是由最稠密 tile 决定，并报告在负载不均视图上优势最大。
- 将同一批次机制用于重建，利用合成提供透射率和颜色以支持批次独立求导。
- 将优化器融合进反向传播，减少直接存储和更新的参数与动量，并推迟视图外的外观更新。
- 摘要声称在评估的已发表方法中渲染更快，重建更快且内存更少，同时保持相同图像质量和精确的前后向 alpha 合成。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集、基线列表、定量指标、内存与速度的具体数值、不同场景规模下的表现，以及方法的失败情形或适用边界。摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对 3DGS 中 tile 粒度冲突和训练优化器开销提出较明确的架构与系统级改进，并声称在渲染速度、重建速度和内存上均有收益；但摘要未给出定量结果、实验范围和对比细节，需阅读全文后才能判断其实际效果与适用性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Collision Rendering: GPU-Accelerated Trajectory Planning on Sparse Voxel Radiance Fields with Risk-Bounded Collision Checking
- 作者：Byoungkwon Yoon, Han Gyeom Lee, Hojun Lee, Yuseop Sim, Daniel Sungwoo Bae, Martin Byung-Guk Jun
- 出版日期：2026-11-23T22:44:37Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.31658) / [PDF](https://arxiv.org/pdf/2611.31658)

### 一句话总结
该论文提出 Collision Rendering，这是面向稀疏体素辐射场（SVR）的轨迹规划框架；它把 SVR 的渲染流程用作碰撞概率的快速数值近似器，并支持 GPU 加速、带风险上界的碰撞检查，以及基于渲染不透明度的可微碰撞代价。

### 研究问题
辐射场虽能为机器人提供细致的场景表示，但在轨迹规划中仍未得到充分探索；目前也缺少一种被广泛认可的方法，把学习到的空间基元转化为可靠的碰撞判定标准。论文希望解决在辐射场表示上如何实现可靠、快速且可用于规划的碰撞检查这一问题。

### 核心思路/方法
- 利用 SVR 结构化的体积密度，将其渲染流程作为碰撞概率的快速数值近似器。
- 用碰撞球近似机器人，并在每个球的位置放置一个重合的球形相机。
- 在概率碰撞模型下，从相机的渲染流程推导每个球在最大方向上的碰撞概率上界。
- 在 GPU 上评估该上界，得到模块化碰撞检查器；它可集成到现有基于采样的规划器中，并且不需要辅助几何地图，也不改变已学习的表示。
- 通过同一渲染流程，从渲染的不透明度计算碰撞代价及其梯度，从而把框架扩展到轨迹优化。

### 主要贡献
- 提出首个面向稀疏体素辐射场（SVR）的轨迹规划框架，支持 GPU 加速、带风险上界的碰撞检查和可微碰撞代价。
- 给出基于渲染流程的碰撞概率上界推导，并把碰撞检查器设计为模块化组件，从而兼容现有采样规划器。
- 将同一渲染流程扩展用于轨迹优化，通过渲染不透明度获得碰撞代价及其梯度。
- 摘要称实验在消费级 GPU 上实现毫秒级碰撞检查时间，所有查询均得到无碰撞轨迹，并优于其他基于辐射场的规划器。

### 局限性
- 摘要未提供足够信息说明碰撞概率上界的理论紧致程度及近似误差范围。
- 摘要未提供足够信息说明实验规模、机器人类型、场景数量与基线设置细节。
- 摘要未提供足够信息说明方法在非 SVR 辐射场表示上的适用性。
- 摘要未提供足够信息说明轨迹优化的收敛性与计算开销细节。
- 摘要未提供足够信息说明真实机器人部署或安全认证相关验证。

### 阅读优先级
中。理由：该工作把辐射场渲染与轨迹规划中的碰撞检查直接结合，问题定位清晰，且声称具备毫秒级检查与无碰撞轨迹结果；但当前仅有摘要与元数据，实验细节和理论紧致性信息不足。若关注辐射场在机器人规划中的应用，值得进一步阅读全文核实。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：InterGS+: Inter-Frame Gaussian Splatting Compression with Geometry-Aware Transformer Prediction and Adaptive Residual Coding
- 作者：Muhammad Talha, Zhu Li, Joel Jung
- 出版日期：2026-11-23T19:55:31Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.31482) / [PDF](https://arxiv.org/pdf/2611.31482)

### 一句话总结
该论文提出一种轻量级的帧间后处理编解码器 InterGS+，通过几何感知的 Transformer 预测和按属性自适应的残差编码，降低动态 3D Gaussian Splatting 的存储与传输成本。

### 研究问题
动态 3DGS 能实现实时逼真的渲染，但每一帧都用大量不规则高斯基元表示，且这些基元带高维属性，导致显著的存储和传输开销。跨帧利用时间冗余比较困难：高斯基元在不同帧之间并不保持固定的身份对应关系。论文关注的问题是如何在这种身份不稳定的条件下，有效进行帧间时间预测与残差表示。

### 核心思路/方法
- 采用轻量级后处理（post-hoc）帧间编解码框架，同时改进时间预测和残差表示。
- 当前帧几何用 G-PCC 编码，并在预测前先重建，使编码端与解码端具有一致的时间邻域。
- 属性预测结合轻量 KNN 与双边预测器，并引入几何感知 Transformer 用于球谐（SH）外观预测，且进行逐高斯的模式选择。
- 残差编码按属性分别适配：
  - SH 新息（innovation）在共享 PCA 域中用矢量量化加精化进行编码；
  - 不透明度与尺度在激活后的 gamma-companded 域中编码；
  - 旋转以规范化四元数新息形式，采用矢量量化加精化编码。
- 在 MPEG 动态序列上的结果：相比 G-PCC Amd. 1 平均 BD-rate 降低 45.48%，相比 InterGS-Lite 降低 7.78%；对应 BD-PSNR 增益分别为 9.98 dB 和 1.10 dB；平均解码复杂度为 0.049 ms/Gaussian，体现其可流式动态 3DGS 压缩的高效性。

### 主要贡献
- 提出 InterGS+ 轻量级帧间后处理编解码器，联合提升时间预测与残差表示。
- 针对高斯基元跨帧身份不固定的问题，通过先编码并重建当前帧几何，使编解码两端获得一致的时间邻域。
- 在属性预测中引入几何感知 Transformer（用于 SH 外观）并结合 KNN/双边预测器与逐高斯模式选择。
- 设计按属性类型分化的残差编码策略（SH 的 PCA 域矢量量化、不透明度/尺度的 gamma-companded 域、旋转的规范化四元数新息）。
- 摘要报告了相对 G-PCC Amd. 1 与 InterGS-Lite 的 BD-rate 和 BD-PSNR 改进，以及较低的平均解码复杂度。

### 局限性
- 摘要未提供足够信息说明方法在非 MPEG 动态序列或更广泛数据集上的泛化表现。
- 摘要未提供足够信息说明不同属性预测器/模式选择的具体计算开销分解，仅给出平均解码复杂度。
- 摘要未提供足够信息说明与更多动态 3DGS 压缩方法的完整对比范围。
- 摘要未提供足够信息说明高斯基元身份不匹配严重或遮挡/拓扑变化剧烈场景下的失效情况。
- 摘要未提供足够信息说明训练或后处理阶段的时间成本与端到端部署要求。

### 阅读优先级
高。理由：该论文直接针对动态 3DGS 的存储与传输瓶颈，提出帧间预测与自适应残差编码的组合方案，并在摘要中给出明确的 BD-rate、BD-PSNR 与解码复杂度指标；对关注动态 3DGS 压缩、流式传输和神经场景表示效率的研究者具有较高参考价值。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Enhancing Sparse-View Gaussian Splatting with Feed-Forward Priors via Spectral Fusion and Distillation
- 作者：Weikai Lin, Jun Dai, Sheng Zhao, Junjie Zhao, Yuhao Zhu
- 出版日期：2026-11-23T19:14:07Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.31428) / [PDF](https://arxiv.org/pdf/2611.31428) / [项目页](https://linwk20.github.io/spectral-fusion-gs/)

### 一句话总结
该论文提出一种即插即用方法，利用预训练前馈新视角合成模型作为先验，通过频域融合与蒸馏增强稀疏视角高斯泼溅，在不牺牲渲染速度的前提下提升质量。

### 研究问题
稀疏训练视角下的高斯泼溅在训练视角附近能渲染高质量图像，但在训练集欠采样的较远区域重建质量下降。前馈新视角合成模型借助强学习先验可从差异较大的视角重采样场景，但渲染耗时超过十倍，且域外场景会产生高频伪影。论文关注如何结合两者优势，同时避免前馈模型带来的慢速渲染与高频伪影问题。

### 核心思路/方法
论文观察到两种方法在频域上互补：先验在低频更准确，高斯在高频更准确；先验相对于高斯的可靠性随图像频率升高而反比下降，因此最优融合权重是一个仅含一个可拟合参数的一阶低通滤波器。基于此，方法智能融合两种方法各自可靠的部分。为在渲染时移除较慢的前馈模型，论文将融合图像作为教师信号，蒸馏回高斯，并与来自输入视角的监督保持平衡。

### 主要贡献
- 提出一种即插即用方法，用预训练前馈 NVS 模型增强已有的稀疏视角高斯模型。
- 指出两者在频域上的互补性，并提出以单参数一阶低通滤波器刻画最优融合权重。
- 通过频域融合与蒸馏，在渲染时不需要前馈模型，从而不牺牲渲染速度。
- 摘要称该方法能提升多种稀疏视角高斯方法的质量，且分析适用于不同先验模型。

### 局限性
- 摘要未提供足够信息说明方法在何种稀疏视角程度、场景类型或数据集上的具体表现与失效条件。
- 摘要未提供足够信息说明蒸馏训练成本、融合参数拟合方式及对不同前馈先验模型的定量泛化结果。
- 摘要未提供足够信息说明与现有方法相比的完整定量指标和消融实验细节。

### 阅读优先级
高。理由：论文直接针对稀疏视角高斯泼溅在欠采样区域质量下降这一关键问题，提出频域互补融合与蒸馏的清晰思路，并强调不牺牲渲染速度的即插即用增强；对神经渲染与三维场景表示方向具有较强相关性。

</details>

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

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-25 - One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics

**Authors:** Shuaijun Liu, Qifu Wen, Xingwei Chen, Xinwen Hu, Feiyang You, Sijia Chen, Ningxin Su
**Links:** [abs](https://arxiv.org/abs/2611.34925) - [pdf](https://arxiv.org/pdf/2611.34925)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Ocean, Many Tasks: A Data-Grounded Simulation Suite and Benchmark for Marine Robotics
- 作者：Shuaijun Liu, Qifu Wen, Xingwei Chen, Xinwen Hu, Feiyang You, Sijia Chen, Ningxin Su
- 出版日期：2026-11-25T18:58:56Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.34925) | [PDF](https://arxiv.org/pdf/2611.34925)

### 一句话总结
论文提出面向海洋机器人仿真套件与基准 OneOcean，以统一时空海洋环境（地形、数据驱动洋流与潮汐、可选污染场）为基础，构建多任务阶梯（任务难度分级）与标准化评测，用于在贴合真实数据的扰动下检验规划与控制方法。

### 研究问题
现有海洋机器人仿真平台难以同时兼顾“视觉真实感”“高通量实验”“基于真实数据的海洋条件真实性”。论文针对这一权衡，试图提供一种可复现、可聚合、可系统压力测试规划与控制的仿真与基准环境。

### 核心思路/方法
- 构建统一的时空海洋环境产品：协调海底地形与数据驱动的洋流、潮汐，并可选择加入污染场，用于清理相关评估。
- 在该环境表示上定义任务阶梯（任务难度分级）：涵盖洋流下导航与定点保持（station-keeping）、航点与路线跟随、深度剖面跟踪、区域扫描、管道巡检，以及多智能体协同（编队通行、鱼群保护与巡逻/驱赶、水面污染定位、围控与清理）。
- 支持 2–10 个载具的多智能体设置；仿真器支持 3 至 6 自由度（DoF）。
- 产出标准化指标与可复现的运行清单（run manifests），支持跨任务、难度与规模设置的一致聚合。
- 实验在不同数据集变体与场景上系统施压基于真实数据的扰动，并比较启发式基线、行为克隆（BC）与基于大语言模型（LLM）的规划器之间的权衡。

### 主要贡献
- 提出 OneOcean 仿真套件与基准，强调基于真实数据的海洋环境真实性，而非仅依赖视觉真实感。
- 给出覆盖单智能体与多智能体、从导航到巡检与污染清理的任务阶梯，并统一多智能体规模与自由度支持。
- 提供标准化指标与可复现运行清单，便于跨任务、难度和规模进行一致性聚合评测。
- 在数据驱动扰动下系统评估启发式、BC 与 LLM 规划器，揭示方法间权衡。

### 局限性
- 摘要未提供足够信息说明仿真器与真实海洋环境之间的验证程度或 sim-to-real 差距。
- 摘要未提供足够信息说明各任务的具体场景数量、数据来源细节、指标定义与统计显著性。
- 摘要未提供足够信息说明 LLM 规划器的具体接口、计算开销与可扩展性边界。
- 摘要未提供足够信息说明污染场建模的物理真实性及其对清理任务评估的影响程度。
- 摘要未提供足够信息说明多智能体通信假设、失败模式与安全性约束。

### 阅读优先级
高。理由：该工作直接回应海洋机器人仿真中“真实海洋条件—高通量—可复现评测”的关键矛盾，并提供多任务、多智能体、标准化指标与运行清单的基准框架；对规划与控制方法的系统比较（启发式、BC、LLM）也具备较强的评测参考价值。是否适合精读取决于读者对海洋机器人基准、数据驱动扰动评测或多智能体任务阶梯的具体需求。

</details>

<details>
<summary>Abstract</summary>

Simulation is essential for marine robotics, yet existing platforms often trade off between visually realistic worlds, high-throughput experimentation, and ocean-condition realism grounded in real data. We present OneOcean, a data-grounded simulation suite and benchmark built around a unified spatiotemporal ocean-environment product that harmonizes bathymetry with data-driven currents and tides, with optional pollution fields for cleanup-related evaluation. On top of this environment representation, OneOcean defines a task ladder spanning navigation and station-keeping under currents, waypoint and route following, depth-profile tracking, area scanning, pipeline inspection, and multi-agent coordination, including formation transit, fish protection and patrol (herding), and surface pollution localization, containment, and cleanup. The suite supports multi-agent settings with 2-10 vehicles. Our simulator supports three to six Degrees of Freedom (DoF) and produces standardized metrics and reproducible run manifests, enabling consistent aggregation across tasks, difficulties, and scaling settings. Experiments across dataset variants and scenes systematically stress planning and control under data-grounded disturbances and reveal trade-offs among heuristic baselines, Behavior Cloning (BC), and a Large Language Model (LLM)-based planner.

</details>

#### 2026-11-25 - Anytime-Valid Sequential Verification for Sensing-Efficient Robot Navigation under Perception Uncertainty

**Authors:** Saad Korchi, Abderrahim Waga
**Links:** [abs](https://arxiv.org/abs/2611.34764) - [pdf](https://arxiv.org/pdf/2611.34764)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anytime-Valid Sequential Verification for Sensing-Efficient Robot Navigation under Perception Uncertainty
- 作者：Saad Korchi, Abderrahim Waga
- 出版日期：2026-11-25T17:32:43Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：[摘要](https://arxiv.org/abs/2611.34764)｜[PDF](https://arxiv.org/pdf/2611.34764)

### 一句话总结
论文提出一种基于高斯似然比的序贯验证规则，用于判断机器人下一步足迹新覆盖的格子是否有足够证据表明可通行，并在静态栅格仿真中减少所需的传感扫描次数。

### 研究问题
论文关注的问题是：机器人在陌生栅格导航时，传感器读数有噪声，因此很难判断下一步移动所涉及的格子是否空闲；增加扫描可以减少这种不确定性，但固定扫描次数会在每个位置都消耗相同的传感开销。论文希望在不发生观测碰撞的前提下，减少每段任务所需的传感扫描次数，并研究认证误差预算的空间分配和观测偏差对方法的影响。

### 核心思路/方法
论文在静态栅格仿真中采用序贯规则，用高斯似然比判断机器人足迹新覆盖的格子是否已有足够证据表明空闲。摘要将序贯验证门与“四扫描参考方案”对比；参考方案中的四扫描次数是在验证数据上选定的。两者分别使用各自在验证数据上选定的路由权重。随后，论文在同一批场景上做回顾性检查，将路由权重设为相等后再比较。空间变体则把相同的认证误差预算更多分配到初始起点—终点矩形附近。

### 主要贡献
- 提出并评估一种基于高斯似然比的序贯验证门，用于在感知不确定性下判断足迹新覆盖格子是否可通行。
- 在 324 个来自 18 张公开地图的留出场景上，序贯验证门与四扫描参考方案均完成全部任务，且未观察到碰撞；在各自验证选定路由权重下，序贯验证门平均每回合 123.15 次扫描，参考方案为 224.13 次，减少 45.05%，95% 地图分层 bootstrap 区间为 42.21%–48.95%。
- 在相同场景上用相等路由权重做回顾性检查时，在两个测试权重下分别减少 43.91% 和 43.37%，且所有任务均完成。
- 在 12 张此前未使用地图的 216 个场景上，将更多相同认证误差预算分配到初始起点—终点矩形附近，使序贯验证门的扫描次数进一步减少 11.58%；该空间变体完成 206 个任务，而原始验证门完成 208 个，并且计算时间增加。
- 摘要指出，碰撞界依赖所假设的观测模型和足迹几何；在持续逐格偏差的压力测试中，原始验证门完成 0/54 个任务。

### 局限性
- 摘要明确指出，碰撞界依赖所假设的观测模型和足迹几何。
- 在持续逐格偏差的压力测试中，原始验证门完成 0/54 个任务，说明该方法对这类偏差假设较敏感。
- 空间变体虽然进一步减少扫描次数，但完成任务数为 206，低于原始验证门的 208，且计算时间增加。
- 摘要未提供足够信息说明真实机器人实验、非静态环境表现、不同传感器类型的泛化性，以及压力测试中偏差的具体生成方式。
- 摘要未提供足够信息说明四扫描参考方案之外的其他基线、完整计算开销数值和理论证明细节。

### 阅读优先级
中。理由：论文给出了较明确的扫描次数减少幅度、留出场景验证和压力测试结果，对关注感知不确定性下机器人导航与序贯验证的读者有参考价值；但摘要显示研究主要基于静态栅格仿真，且持续偏差压力测试下原始方法失败，真实场景适用性等信息摘要未提供足够信息，因此优先级不宜定为高。

</details>

<details>
<summary>Abstract</summary>

When a robot navigates an unfamiliar grid, noisy sensor readings can make it hard to tell whether the cells along its next move are free. Additional scans can reduce that uncertainty, but a fixed scan count spends the same sensing effort at every position. In a static-grid simulation, a sequential rule uses a Gaussian likelihood ratio to determine when the cells newly covered by the robot's footprint have enough evidence of free space. On 324 held-out scenarios from 18 public maps, the sequential gate and a four-scan reference chosen on validation data both completed every mission without an observed collision. With their respective validation-selected routing weights, the gate averaged 123.15 scans per episode versus 224.13 for the reference, a reduction of 45.05% (95% map-stratified bootstrap interval: 42.21--48.95%). In a retrospective check on the same scenarios with routing weights held equal, the reductions were 43.91% and 43.37% at the two tested weights, with all missions completed. On 216 scenarios from 12 previously unused maps, allocating more of the same certification error budget near the initial start--goal rectangle cut the sequential gate's scan count by a further 11.58%. The spatial variant completed 206 missions versus 208 for the original gate and increased computation time. The collision bound depends on the assumed observation model and footprint geometry. In a stress test with persistent per-cell bias, the original gate completed 0 of 54 missions.

</details>

#### 2026-11-25 - Autonomous Ergodic Robotic Palpation for Elastic Mapping of Curved Soft Tissues

**Authors:** Luca Beber, Cem Bilaloglu, Edoardo Lamon, Matteo Saveriano, Daniele Fontanelli, Luigi Palopoli, Sylvain Calinon
**Links:** [abs](https://arxiv.org/abs/2611.34670) - [pdf](https://arxiv.org/pdf/2611.34670)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Autonomous Ergodic Robotic Palpation for Elastic Mapping of Curved Soft Tissues
- 作者：Luca Beber, Cem Bilaloglu, Edoardo Lamon, Matteo Saveriano, Daniele Fontanelli, Luigi Palopoli, Sylvain Calinon
- 出版日期：2026-11-25T16:36:46Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.34670 ；PDF https://arxiv.org/pdf/2611.34670

### 一句话总结
本文提出一种基于点云、直接作用于曲面软组织的遍历式自主机器人触诊框架，利用 Laplace–Beltrami 算子将在线黏弹性估计与探索规划统一在曲面内蕴几何上，以实现与几何一致的弹性建图及硬质包涵体定位。

### 研究问题
现有自主机器人触诊方法多依赖先验网格模型或平面表面假设，难以泛化到复杂人体解剖结构。论文旨在解决在曲面软组织上直接进行自主触诊与弹性属性建图的问题，并支持硬质包涵体定位。

### 核心思路/方法
- 直接使用点云数据在曲面软组织表面操作，不依赖先验网格模型或平面假设。
- 以 Laplace–Beltrami 算子为核心，将在线估计与探索同时建立在曲面内蕴几何之上。
- 使用无迹卡尔曼滤波（UKF）估计局部黏弹性参数，并融合到表面感知的高斯过程（GP）中。
- 由该概率模型驱动基于扩散的遍历运动规划器，生成连续探索轨迹，并将新采样信息以闭环方式反馈给 GP。
- 采用混合力-阻抗控制器调节交互力，以维持接触。
- 评估方式包括：在仿真中与现有方法比较；在具有不同几何与黏弹性属性的组织模拟硅胶体模上进行物理实验；摘要称其展示了几何一致建图与接触丰富条件下的硬质包涵体定位。

### 主要贡献
- 提出面向曲面软组织的遍历式触诊框架，直接在点云上运行。
- 引入 Laplace–Beltrami 算子，使在线估计与探索规划统一于曲面内蕴几何。
- 将 UKF 局部黏弹性估计、表面感知 GP 与扩散式遍历运动规划器结合为闭环流程。
- 通过混合力-阻抗控制维持接触，并在仿真与硅胶体模物理实验中验证了几何一致建图与硬质包涵体定位。

### 局限性
- 摘要未提供足够信息说明计算复杂度、实时性上限或大规模曲面的可扩展性。
- 摘要未提供足够信息说明在真实人体组织、体内环境或强噪声/大变形条件下的泛化能力。
- 摘要未提供足够信息给出定量性能指标、对比方法细节、失败案例或参数敏感性分析。
- 摘要提到在仿真和硅胶体模上验证，但是否覆盖广泛解剖几何与病理差异，摘要未提供足够信息。

### 阅读优先级
中。理由：论文主题集中在曲面软组织自主触诊、曲面内蕴几何建模与闭环遍历规划，方法组合具有明确的新意；摘要已给出仿真与体模实验验证，但未提供定量结果与真实组织验证细节。若关注机器人触诊、软体组织建图或曲面上的主动感知，可优先阅读；若需要直接评估临床可用性，则需进一步查看全文实验部分。

</details>

<details>
<summary>Abstract</summary>

Autonomous robotic palpation offers repeatable, quantitative estimates of tissue properties for stiff inclusion localization. However, existing methods often rely on prior mesh models or planar surface assumptions that do not generalize to complex human anatomy. We propose an ergodic palpation framework that operates directly on curved soft surfaces using point cloud data. Central to our approach is the Laplace--Beltrami operator, which grounds both online estimation and exploration in the surface intrinsic geometry. We estimate local viscoelastic parameters using an Unscented Kalman Filter (UKF) and fuse them into a surface-aware Gaussian Process (GP). This probabilistic model drives a diffusion-based ergodic motion planner, generating a continuous exploration trajectory that feeds the new informative samples back to the GP in a closed loop. Throughout this process, a hybrid force-impedance controller regulates interaction forces to maintain contact. We evaluate the approach against existing methods in simulation and validate it in physical experiments on tissue-mimicking silicone phantoms with varying geometries and viscoelastic properties, demonstrating geometry-consistent mapping and stiff inclusion localization under contact-rich conditions.

</details>

#### 2026-11-25 - Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics

**Authors:** Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling, Hui Wang, Sheng Liu, Miao Li
**Links:** [abs](https://arxiv.org/abs/2611.34302) - [pdf](https://arxiv.org/pdf/2611.34302)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Co-World Model for Human-Video-to-Robot Transfer via Co-Constructed Shared Latent Dynamics
- 作者：Xuetao Li, Xuan Jiang, Chen Liu, Zhongrui Rao, Yu Ling, Hui Wang, Sheng Liu, Miao Li
- 出版日期：2026-11-25T12:54:52Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.34302) / [PDF](https://arxiv.org/pdf/2611.34302)

### 一句话总结
论文提出 Co-World Model（CoWM），利用配对但不同步的人类视频流与机器人轨迹流联合优化共享潜在动态表示，以实现从单次人类演示到机器人的零样本技能迁移。

### 研究问题
论文关注从人类视频向机器人技能迁移时的两个核心问题：一是跨具身动态不匹配（cross-embodiment dynamics mismatch），现有方法或重定向人类特定几何，或仅匹配静态视觉目标，难以处理动态差异；二是动作执行缺乏落地依据（ungrounded action execution）。论文目标是在人类视频丰富廉价、机器人轨迹稀缺昂贵的背景下，实现从单次人类演示到机器人的零样本技能迁移。

### 核心思路/方法
CoWM 是一个预测框架，基于配对但不同步的人类与机器人流进行联合优化。为弥合跨具身动态差距，方法将每个观测解耦为共享的物体关系状态（shared object-relation state）和具身特定上下文（embodiment-specific context）。在潜在动作对齐方面，CoWM 使用 effect-swap 与 action-sensitivity 目标跨具身对齐潜在动作，使动作依据其对被操作物体的预测效果进行匹配，而不是依据具身相关的运动学。为支持落地执行，方法引入 phase-aware receding-horizon controller：估计演示进度，将推断出的人类动作先验投影到机器人动作支撑密度上，并将所得潜在动态转化为可执行的机器人命令。

### 主要贡献
- 提出 Co-World Model（CoWM），一个从配对但不同步的人类与机器人流联合优化的预测框架。
- 通过将观测解耦为共享物体关系状态与具身特定上下文，应对跨具身动态不匹配。
- 使用 effect-swap 和 action-sensitivity 目标，以预测效果而非具身相关运动学来对齐跨具身潜在动作。
- 设计 phase-aware receding-horizon controller，用于估计演示进度、将人类动作先验投影到机器人动作支撑密度并生成可执行机器人命令。
- 摘要称在仿真和两个物理机器人平台上进行了大量实验，展示了 CoWM 的有效性、跨平台泛化能力以及各组件贡献；具体实验细节摘要未提供足够信息。

### 局限性
- 摘要未提供足够信息说明方法对配对但不同步数据的具体依赖程度、数据规模及同步质量要求。
- 摘要未提供足够信息说明在仿真与两个物理机器人平台上的具体任务、评价指标、对比基线及定量结果。
- 摘要未提供足够信息说明失败案例、适用任务范围及计算成本。
- 摘要未提供足够信息说明各组件贡献的消融实验具体设置与结果。

### 阅读优先级
高。理由：该论文针对人类视频到机器人零样本迁移中的跨具身动态不匹配与动作落地问题提出较完整的框架，且摘要明确涉及仿真和两个物理平台验证；若关注机器人学习、跨具身迁移或从人类视频学习技能，具备较高阅读价值。但具体实验细节需查阅全文确认。

</details>

<details>
<summary>Abstract</summary>

Human videos are abundant and cheap to obtain, whereas robot trajectories remain scarce and costly, making zero-shot skill transfer from a single human demonstration an appealing route to scalable robot learning. Existing methods, however, either retarget human-specific geometry or match only static visual goals, and thus stumble over the cross-embodiment dynamics mismatch and the ungrounded action execution. We present the Co-World Model (CoWM), a predictive framework jointly optimized from paired yet unsynchronized human and robot streams. To bridge the cross-embodiment dynamics gap, CoWM disentangles each observation into a shared object-relation state and embodiment-specific context. It aligns latent actions across embodiments using effect-swap and action-sensitivity objectives,such that actions are matched by their predicted effects on the manipulated objects rather than by embodimentdependent kinematics. For grounded execution, a phase-aware receding-horizon controller estimates demonstration progress, projects the inferred human action prior onto the robot action-support density, and translates the resulting latent dynamics into executable robot commands. Extensive experiments in simulation and on two physical robot platforms demonstrate the effectiveness of CoWM, its cross-platform generalizability, and the contribution of each component. See the demo video in the supporting information for details.

</details>

#### 2026-11-25 - Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers

**Authors:** Gen Li, Fan Luo, Mengjun Lin, Shu Han, Bohan Li, Hao Zhao
**Links:** [abs](https://arxiv.org/abs/2611.34199) - [pdf](https://arxiv.org/pdf/2611.34199)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pointmap, manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers
- 作者：Gen Li, Fan Luo, Mengjun Lin, Shu Han, Bohan Li, Hao Zhao
- 出版日期：2026-11-25T11:27:05Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.34199 ；PDF https://arxiv.org/pdf/2611.34199

### 一句话总结
Loop4D 提出一种面向机器人操作结果预测的 4D 世界建模框架，通过保持运动的 4D VAE 表示与循环式扩散 Transformer，联合建模 RGB 外观与几何演化。

### 研究问题
论文关注机器人操作结果预测中需要同时建模视觉外观与演化中的 3D 几何这一核心问题。摘要指出两个挑战：一是视频压缩可能模糊细粒度机器人运动；二是联合预测 RGB 与几何需要足够的生成能力。

### 核心思路/方法
方法由表示学习与生成建模两部分构成。表示方面，4D VAE 将 RGB 与 pointmap 序列编码为紧凑的时空潜变量，并强调保留运动细节与几何结构；其中 RGB VAE 结合几何引导监督与预测式重建以减少压缩造成的运动伪影，几何 VAE 通过轻量适配器适配预训练 RGB 表示并保留其先验。生成方面，Dual-Stream Looped Diffusion Transformer 维护独立的外观流与几何流，共享 Transformer 权重并设置跨模态连接；通过在不同循环中复用 Transformer 块增加有效深度而不复制主干参数，使较少参数的模型通过额外计算改善 RGB 与几何的联合预测。

### 主要贡献
摘要明确提出的贡献包括：提出 Loop4D 框架，以保持运动的 4D 表示和循环式生成细化应对上述挑战；设计 4D VAE 编码 RGB 与 pointmap 序列；设计结合几何引导监督与预测式重建的 RGB VAE，以及使用轻量适配器的几何 VAE；提出共享权重、跨模态连接并循环复用 Transformer 块的双流循环扩散 Transformer。摘要称实验展示了高质量 4D 生成，并在模拟机器人操作任务中验证了 Loop4D。具体数据集、指标和对比结果摘要未提供足够信息。

### 局限性
摘要未提供足够信息说明方法在真实机器人任务、非模拟环境、极端运动、长时预测或计算开销方面的具体局限；也未提供定量实验结果、失败案例分析或与其他方法的完整比较，因此无法仅依据摘要判断其边界条件与适用范围。

### 阅读优先级
中。理由：该论文问题定位清晰，涉及具身世界建模、4D 表示与扩散 Transformer 的结合，对机器人操作预测与 4D 生成方向具有相关性；但摘要未给出具体实验设置、定量结果与真实场景验证信息，是否值得优先精读需结合全文实验部分再判断。

</details>

<details>
<summary>Abstract</summary>

Predicting the outcomes of robotic manipulation requires modeling both visual appearance and evolving 3D geometry. This poses two challenges: video compression can obscure fine-grained robot motion, while jointly predicting RGB and geometry demands sufficient generative capacity. We introduce Loop4D, a framework that addresses these challenges through motion-preserving 4D representations and recurrent generative refinement. Our 4D VAE encodes RGB and pointmap sequences into compact spatiotemporal latents while preserving motion details and geometric structure. Our RGB VAE combines geometry-guided supervision with predictive reconstruction to reduce compression-induced motion artifacts. Our geometry VAE uses lightweight adapters to adapt pretrained RGB representations while preserving their priors. Building on these representations, our Dual-Stream Looped Diffusion Transformer maintains separate appearance and geometry streams with shared Transformer weights and cross-modal connections. By reusing Transformer blocks across loops, we increase effective depth without replicating backbone parameters, enabling models with fewer parameters to improve joint RGB-geometry prediction through additional computation. Experiments demonstrate high-quality 4D generation and validate Loop4D in simulated robotic manipulation tasks.

</details>

#### 2026-11-25 - QK-Bench: Benchmarking Quantitative Kinematic Understanding for Dynamic Spatial Intelligence

**Authors:** Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang, Jianhua Han, Meng Tian, Shaohui Liu, Wangmeng Zuo
**Links:** [abs](https://arxiv.org/abs/2611.33991) - [pdf](https://arxiv.org/pdf/2611.33991)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：QK-Bench: Benchmarking Quantitative Kinematic Understanding for Dynamic Spatial Intelligence
- 作者：Lennox Wei, Jiaqi Yao, Shixin Sun, Yuanzheng Zhang, Jianhua Han, Meng Tian, Shaohui Liu, Wangmeng Zuo
- 出版日期：2026-11-25T08:45:45Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.33991 ；PDF https://arxiv.org/pdf/2611.33991

### 一句话总结
论文提出 QK-Bench，用于评测多模态大模型从单目 RGB 视频中进行定量运动学理解的能力，并发现当前模型在该基准上表现显著不足。

### 研究问题
论文关注空间智能中的“定量运动学理解”：模型不仅要语义上识别物体在接近，还要能从视觉证据中判断运动幅度、速率、参考系依赖关系以及未来空间演化。摘要指出，语义正确的描述可能掩盖定量错误，而这类错误在碰撞避免、轨迹跟踪和反应式抓取等任务中至关重要。研究问题是：多模态大语言模型（MLLMs）能否可靠完成这类定量运动学理解。

### 核心思路/方法
论文构建了 Quantitative Kinematics Benchmark（QK-Bench），包含来自 379 个视频的 2,341 个多项选择问答对，覆盖 17 个任务，分为 Object-Centric Kinematics、Camera Ego-Motion Kinematics 和 Multi-Object Kinematic Relations 三类。摘要说明，基准利用隐藏的几何与时间信号支持轨迹构建和筛选，并通过固定运动学规则将物理量映射为可验证答案，包括类别标签；同时进行轨迹和问题验证，以确保目标可靠性和采样帧中足够的视觉支持。所有模型均接收统一的单目 RGB 输入。

### 主要贡献
- 提出 QK-Bench，用于评测 MLLMs 的定量运动学理解，覆盖运动幅度、速率、参考系依赖和未来空间演化等维度。
- 构建了包含 379 个视频、2,341 个多项选择问答对、17 个任务和三大任务类别的基准。
- 采用隐藏几何与时间信号、固定运动学规则和轨迹/问题验证来提升答案可验证性与视觉支持充分性。
- 对专有、开源和空间 MLLMs 进行评估，发现最强模型总体准确率仅 41.2%，且空间 MLLMs 没有一致优势，表明当前空间智能进展未必能可靠迁移到定量运动学理解。

### 局限性
摘要未提供足够信息说明基准的样本多样性、标注成本、任务难度分布、模型评估的具体设置、误差来源分析以及方法本身的适用范围限制。摘要仅报告了最强模型总体准确率为 41.2% 以及空间 MLLMs 无一致优势，未提供更细粒度的实验细节。

### 阅读优先级
高。理由：该论文直接针对空间智能中“语义正确但定量错误”的关键缺口，提出可验证的定量运动学基准，并给出当前 MLLMs 显著不足的评估结果；对多模态大模型、具身智能、机器人感知与动态空间理解相关研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence concerns both scene structure and its temporal evolution. Yet a semantically correct description can conceal a quantitative error: recognizing that objects are approaching does not determine their closing speed or whether they will meet. Such errors are critical in collision avoidance, trajectory tracking, and reactive grasping, where actions depend on motion magnitude, timing, and relative geometry. We study quantitative kinematic understanding in multimodal large language models (MLLMs): resolving motion magnitude, rate, reference-frame dependence, and future spatial evolution from visual evidence. We introduce the Quantitative Kinematics Benchmark (QK-Bench), comprising 2,341 multiple-choice QA pairs from 379 videos and 17 tasks spanning Object-Centric Kinematics, Camera Ego-Motion Kinematics, and Multi-Object Kinematic Relations. Hidden geometric and temporal signals support trajectory construction and filtering, while fixed kinematic rules map physical quantities to verifiable answers, including categorical labels. Trajectory and question validation ensure target reliability and sufficient visual support in the sampled frames. All models receive a unified monocular RGB input. Evaluations of proprietary, open-source, and spatial MLLMs reveal substantial limitations: the strongest model achieves only 41.2\% overall accuracy, and spatial MLLMs show no consistent advantage. These findings indicate that current advances in spatial intelligence do not reliably transfer to quantitative kinematic understanding.

</details>

#### 2026-11-25 - 3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding

**Authors:** Nannan Zhang, Ting Huang, Zeyu Zhang, Haoyu Chen, Yanjie Zhu, Hao Tang
**Links:** [abs](https://arxiv.org/abs/2611.33835) - [pdf](https://arxiv.org/pdf/2611.33835)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3D CoCa v3: Contrastive Learners with Scene Graphs for Urban Scene Understanding
- 作者：Nannan Zhang, Ting Huang, Zeyu Zhang, Haoyu Chen, Yanjie Zhu, Hao Tang
- 出版日期：2026-11-25T06:03:25Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.33835 ；PDF https://arxiv.org/pdf/2611.33835 ；代码 https://github.com/AIGeeksGroup/3DCoCav3

### 一句话总结
3D CoCa v3 是一个面向城市 3D 场景理解的场景图增强对比与生成框架，通过金字塔视觉编码器、语言模型解码器以及基于 MSG 的关系描述，将结构化空间关系引入 3D-语言对齐，并在 City-3DQA 与 GeoEval3D 上报告了性能提升。

### 研究问题
论文关注大规模 3D 城市场景理解中的表示学习问题：现有 3D 视觉-语言方法主要强调全局语义对齐或对象级表示，而在统一的对比与生成框架中，结构化关系建模仍探索不足。论文试图在对比学习与生成框架中同时纳入多尺度几何结构与复杂空间关系。

### 核心思路/方法
论文提出 3D CoCa v3，一个场景图增强的对比与生成框架。方法层面包括：
- 使用 Pyramid Vision Encoder 进行多尺度几何表示学习；
- 采用基于语言模型的解码器，并引入问题引导的 caption 检索与视觉交叉注意力；
- 引入基于 MSG 的关系描述，以结构化空间关系丰富对比式 3D-语言对齐；
- 构建 City3D-9.6K 数据集，包含多视角城市视觉-语言数据、对齐的视觉-几何观测、场景描述和场景图，用于语义与关系监督。

### 主要贡献
- 提出 3D CoCa v3，将场景图增强的关系建模引入统一的对比与生成式 3D 视觉-语言框架。
- 设计 Pyramid Vision Encoder 与语言模型解码器结合的结构，并加入问题引导的 caption 检索和视觉交叉注意力。
- 引入基于 MSG 的关系描述，以结构化空间关系增强 3D-语言对比对齐。
- 构建 City3D-9.6K 多视角城市视觉-语言数据集，提供场景描述与场景图监督。
- 在 City-3DQA 上报告句级划分总体 top-1 准确率 88.35%、城市级划分 64.79%，分别超过 3D CoCa v2 20.88 和 3.57 个百分点；并在 GeoEval3D 上报告最佳性能。

### 局限性
摘要未提供足够信息说明方法局限、失败场景、计算成本、数据偏差或泛化边界。摘要仅报告了 City-3DQA 与 GeoEval3D 上的结果，未提供消融实验细节、训练配置、参数量或推理开销等信息，因此无法据此评估这些方面的局限。

### 阅读优先级
中。理由：论文主题集中在城市 3D 场景理解、3D 视觉-语言对比与生成、场景图关系建模，若读者关注该方向，其方法组合与新数据集具有直接相关性；但摘要未提供充分的实验细节与局限性信息，且兴趣方向未额外指定，因此不建议作为泛化阅读的高优先级文献。

</details>

<details>
<summary>Abstract</summary>

Understanding large-scale 3D urban scenes requires representations that capture both multi-scale geometric structures and complex spatial relationships. However, existing 3D vision-language methods primarily emphasize global semantic alignment or object-level representations, leaving structured relational modeling underexplored within unified contrastive and generative frameworks. In this paper, we present 3D CoCa v3, a scene-graph-enhanced contrastive and generative framework for urban 3D scene understanding. Our framework features a Pyramid Vision Encoder for multi-scale geometric representation learning and a language-model-based decoder with question-guided caption retrieval and visual cross-attention. We further introduce MSG-based relational descriptions to enrich contrastive 3D-language alignment with structured spatial relationships. To support semantic and relational supervision, we construct City3D-9.6K, a multi-view urban vision-language dataset with aligned visual-geometric observations, scene captions, and scene graphs. Extensive experiments on City-3DQA demonstrate that 3D CoCa v3 achieves 88.35% and 64.79% overall top-1 accuracy on the sentence-wise and city-wise splits, surpassing 3D CoCa v2 by 20.88 and 3.57 percentage points, respectively. Furthermore, 3D CoCa v3 achieves the best performance on GeoEval3D, demonstrating its effectiveness in urban spatial reasoning and geometric understanding. Code is available at https://github.com/AIGeeksGroup/3DCoCav3.

</details>

#### 2026-11-25 - GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting

**Authors:** Shijun Guo, Yaming Yang, Haoran Xu, Wei Zhao, Ziyu Guan, Cai Xu, Peixi Peng
**Links:** [abs](https://arxiv.org/abs/2611.33693) - [pdf](https://arxiv.org/pdf/2611.33693)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting
- 作者：Shijun Guo, Yaming Yang, Haoran Xu, Wei Zhao, Ziyu Guan, Cai Xu, Peixi Peng
- 出版日期：2026-11-25T02:58:48Z
- 分类：主分类为 Embodied / Robotics / AR Applications；次级分类：摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.33693 ；PDF https://arxiv.org/pdf/2611.33693

### 一句话总结
GeoTex 是一个面向自动驾驶世界模型的 4D 占用世界模型，通过“几何作为纹理”的编码方式联合建模列内高度模式与列间关系，并借助固定关系记忆与近期历史残差更新进行历史接地的预测，在摘要报告的对比中提升了预测 mIoU/IoU 并减少了参数量。

### 研究问题
论文针对 4D 占用预测中的两个问题：其一，语义占用将图像颜色与纹理抽象为离散标签后，类内局部形状主要依赖 3D 体素排布来区分，而现有方法借用图像编码框架，通过高度通道化或平面分解获得紧凑潜表示，在压缩前未充分联合建模“列内高度模式”和“列间关系”，削弱了几何线索；其二，预测阶段对互补的历史信息利用不足，且难以保留可靠的观测证据。

### 核心思路/方法
GeoTex 由表示与预测两部分构成，并在预测训练后进行解码适配：
- GeoTex Representation：将列内高度模式与列间关系联合编码为紧凑连续潜表示，并通过内容相关的高度展开与几何交互恢复 3D 结构。
- GeoTex Prediction：在固定跨观测关系记忆中保留初始证据贯穿整个 rollout，并通过目标参照的残差更新引入互补的近期历史。
- 预测训练完成后，采用 decoder-only 适配改善对预测状态的语义解码。

### 主要贡献
- 提出 GeoTex 占用世界模型，结合 geometry-as-texture 编码与历史接地预测。
- 在表示层面联合建模列内高度模式与列间关系，并以内容相关高度展开和几何交互恢复 3D 结构。
- 在预测层面以固定跨观测关系记忆保留初始证据，并以目标参照残差更新利用近期历史。
- 摘要报告：相对 GenieDrive，平均预测 mIoU 与 IoU 分别提升 9.79% 与 11.91%，参数量从 3.47M 降至 2.33M，且增益在更长预测时域上增大；代码见补充材料。

### 局限性
摘要未提供足够信息说明局限性；例如失败场景、对特定数据集或传感器配置的依赖、计算开销与实时性、长时域误差累积等均未在摘要中给出。摘要亦未提供足够信息说明具体实验设置、数据集、基线细节与消融结果。

### 阅读优先级
中。理由：该工作聚焦 4D 占用预测中的几何编码与历史利用，摘要给出了明确的动机、方法组成和相对基线的量化收益，并对自动驾驶世界模型与占用预测研究方向具有相关性；但摘要未提供实验设置、数据集与消融等细节，是否值得优先精读需结合全文实验严谨性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models. Semantic occupancy abstracts image color and texture into discrete labels, leaving 3D voxel arrangements as the primary cues for distinguishing local shapes within each class. Existing methods borrow image-encoding frameworks to obtain compact latent representations through height channelization or plane factorization, but do not sufficiently model within-column height patterns and cross-column relations jointly before compression, weakening these geometric cues. Forecasting also underutilizes complementary history and struggles to retain reliable observation evidence. We therefore propose GeoTex, an occupancy world model combining geometry-as-texture encoding with history-grounded forecasting. GeoTex Representation jointly encodes within-column height patterns and cross-column relations into compact continuous latent representations and restores 3D structure through content-dependent height unfolding and geometric interaction. GeoTex Prediction retains initial evidence throughout rollout in fixed cross-observation relational memory and incorporates complementary recent history through target-referenced residual updates. After prediction training, decoder-only adaptation improves semantic decoding of predicted states. GeoTex improves average forecasting mIoU and IoU by 9.79% and 11.91% relative to GenieDrive while reducing parameters from 3.47M to 2.33M, with gains increasing at longer horizons. Code is included in the supplementary material.

</details>

#### 2026-11-24 - Fast Muscle-Driven Whole-Body Motion Tracking with a Differentiable World Model

**Authors:** Kaibo He, Maciej Bakowicz, Shihe Zhou, Yusen Feng, Yanan Sui, Dhanush Radhakrishnan
**Links:** [abs](https://arxiv.org/abs/2611.33460) - [pdf](https://arxiv.org/pdf/2611.33460)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Fast Muscle-Driven Whole-Body Motion Tracking with a Differentiable World Model
- 作者：Kaibo He, Maciej Bakowicz, Shihe Zhou, Yusen Feng, Yanan Sui, Dhanush Radhakrishnan
- 出版日期：2026-11-24T21:36:26Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.33460) / [PDF](https://arxiv.org/pdf/2611.33460)

### 一句话总结
该论文将 SuperMimic 的可微世界模型追踪方法扩展到 700 肌肉与 354 肌肉的全身肌骨模型，通过一套提速训练配方把 MS-Human-700 的训练时间从数小时缩短到数分钟，并在测试时利用世界模型进一步降低追踪误差。

### 研究问题
用全身肌骨模型做动作捕捉追踪，需要在上百块肌肉之间协调，同时还要处理接触问题；现有控制器训练往往要耗费数小时至数天的 GPU 时间，因此每次调参的代价都很高。

### 核心思路/方法
- 以 SuperMimic 为基础：通过在学习到的世界模型 rollout 上做反向传播来训练追踪策略。
- 将方法扩展到 MS-Human-700（700 块肌肉）和 MyoFullBody（354 块肌肉），并把 MuJoCo 的激活动力学放进世界模型内。
- 提速配方：沿用为 Unitree G1 开发的加速设置，替换其中三个在肌肉模型上失效的设置，并加入四项自有改动：
  1. 观测中不使用肌肉几何信息；
  2. 数据采集与更新并发进行；
  3. 使用 Beta 探索噪声，使每个激励保持在 $[0,1]$；
  4. 采用 50 Hz 控制。
- 测试时通过世界模型精炼策略动作。

### 主要贡献
- 在单张 RTX 5090 上，MS-Human-700 用 6.3 分钟达到 SuperMimic 已发表超参数 3.9 小时达到的 held-out return，快 37 倍；用 20 分钟达到比其 10 小时后更低的追踪误差。
- MyoFullBody 无需重新调参即快 34 倍。
- 消融显示肌肉模型的特异性：较高的策略学习率会使一半运行停滞；裁剪高斯噪声会引入 Beta 噪声所避免的 tonic co-contraction。
- 测试时经世界模型精炼动作，位置误差再降低 26%，且没有 held-out clip 失败；达到相同 return 的训练时间从 6.3 分钟降至 5.1 分钟。

### 局限性
- 摘要未提供足够信息说明方法在真实硬件、真实传感器噪声或跨受试者泛化上的表现。
- 摘要未提供足够信息说明与其它肌肉驱动追踪方法的系统性对比范围。
- 摘要未提供足够信息说明 Beta 噪声与 50 Hz 控制等设计在其他肌骨模型上的适用边界。
- 摘要未提供足够信息说明测试时世界模型精炼带来的额外计算开销。

### 阅读优先级
高。理由：该工作直接针对肌肉驱动全身动作追踪训练代价高的问题，给出数量级提速，并在两个大规模肌肉模型上验证，还包含消融与测试时精炼结果；对肌骨仿真、物理动画与机器人动作追踪方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Tracking motion capture with a whole-body musculoskeletal model means coordinating hundreds of muscles through contact, and current controllers take hours to days of GPU time to train, so every tuning decision is expensive. SuperMimic trains a tracking policy by backpropagating through the rollouts of a learned world model. We extend it to MS-Human-700 (700 muscles) and MyoFullBody (354 muscles), with MuJoCo's activation dynamics inside the world model. To make its training fast, our recipe takes the speedups developed for the Unitree G1, replaces three of their settings that fail on muscles, and adds four changes of our own: observations without muscle geometry, data collection concurrent with the updates, Beta exploration noise that keeps every excitation in $[0,1]$, and 50 Hz control. On one RTX 5090 it trains MS-Human-700 in 6.3 minutes to the held-out return that SuperMimic's published hyperparameters reach in 3.9 hours, 37$\times$ sooner, and in 20 minutes to lower tracking errors than theirs after 10 hours. It trains MyoFullBody 34$\times$ sooner without retuning. Ablations show what is specific to muscles: a higher policy learning rate stalls half of the runs, and clipped Gaussian noise adds a tonic co-contraction that Beta noise avoids. Finally, refining the policy's actions through the world model at test time lowers the position error by a further 26% with no held-out clip failing, and reaches the same return after 5.1 instead of 6.3 minutes of training. Code, the training recipe and videos are on the project page https://muscle-supermimic.beanpow.top.

</details>

#### 2026-11-24 - ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification

**Authors:** Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai
**Links:** [abs](https://arxiv.org/abs/2611.33143) - [pdf](https://arxiv.org/pdf/2611.33143)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ROAM-Bench: Evaluating Embodied Active Spatial Intelligence through Evidence Verification
- 作者：Xingjian Ran, Xiaoye Mo, Sihao Liu, Li Luo, Taiqiang Wu, Ji Zhao, Wenqi Shao, Hongyang Li, Jiaqi Wang, Bo Dai
- 出版日期：2026-11-24T18:56:22Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.33143) | [PDF](https://arxiv.org/pdf/2611.33143)

### 一句话总结
提出 ROAM-Bench，一个在机器人运动与碰撞约束下，通过独立检查结果和任务要求来评估具身主动空间智能的基准。

### 研究问题
现有基准不足以区分“结果正确”与“任务要求完成”之间的差异，难以准确评估具身智能体通过探索和交互收集信息、并据此推理和行动的能力。

### 核心思路/方法
构建 ROAM-Bench 基准：在机器人运动与碰撞约束下，使用仿真状态和回合记录进行独立检查，评估任务结果与任务要求的完成情况，并对几何、覆盖或放置进行更强检查。基准包含 5 组共 11 种任务类型、27 个室内环境，共 250 个经人工验证的任务，覆盖物体与房间搜索、计数、几何判断、方向推理和重定位。

### 主要贡献
- 提出 ROAM-Bench，强调区分结果正确性与任务要求完成度的评估方式。
- 构建 250 个经人工验证的任务，覆盖 11 种任务类型、5 个任务组和 27 个室内环境。
- 报告人类评估者在 100 个抽样任务上达到 84% 的严格任务成功率，且每个正确结果均满足所需检查。
- 在七个前沿视觉语言模型上识别出两种互补的失败模式：结果正确但任务要求未满足，以及结果错误却通过了更强检查。
- 通过 oracle 输入诊断表明，更完整的目标观测和校准反馈可改善最终空间判断。
- 摘要未提供足够信息说明具体的模型名称、实验规模及量化结果细节。

### 局限性
- 摘要未提供足够信息说明基准在真实机器人平台上的验证情况。
- 摘要未提供足够信息说明任务多样性之外的其他环境或场景覆盖范围。
- 摘要未提供足够信息说明人类评估者与模型评估之间的完整对比数据。
- 摘要未提供足够信息说明 oracle 输入诊断的具体设置与适用范围。

### 阅读优先级
中。该基准针对具身空间智能评估中“结果正确”与“任务要求完成”的区分问题，对具身智能与机器人评估方向有参考价值；但摘要未提供具体模型表现数据和实验细节，需阅读全文以判断其方法严谨性与适用性。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Physicl Scenes: An Artist-created 3D Dataset for Learning Perception and Action
- 作者：Yueh-Cheng Liu, Snehal Jauhri, Matthias Nießner, Angela Dai
- 出版日期：2026-11-24T18:55:07Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.33137) / [PDF](https://arxiv.org/pdf/2611.33137)

### 一句话总结
论文提出 Physicl Scenes，一个由艺术家创建并整理的 6,499 个高质量 3D 场景数据集，覆盖家庭房间、公共室内与户外空间，面向视觉与具身学习的联合监督，并附带移动操作基准。

### 研究问题
论文关注视觉与具身学习缺乏高质量、带丰富标注的 3D 场景训练数据的问题。摘要指出，现有替代方案是其他合成数据集，但未具体说明这些数据集存在哪些不足；摘要未提供足够信息说明对现有数据集缺陷的详细分析。

### 核心思路/方法
- 构建艺术家创建并整理的 3D 场景数据集，共 6,499 个场景，覆盖家庭房间、公共室内和户外空间。
- 场景包含详细几何、基于物理的材质（physically based materials）以及精心编排的环境。
- 提供物体级和部件级语义标注，为视觉学习和具身学习提供丰富的联合监督。
- 在逆渲染、3D 重建、场景理解和移动操作等任务上，用该数据集训练当前先进方法，并与其他合成数据集对比性能。
- 提出一个移动操作基准，评估视觉-语言-动作模型在多样化 3D 场景中执行物理抓取与放置，并利用部件标注评估抓取位置。

### 主要贡献
- 发布 Physicl Scenes 数据集：6,499 个艺术家创建与整理的 3D 场景，包含几何、物理材质、环境构图以及物体级和部件级语义标注。
- 展示该数据集作为训练数据在逆渲染、3D 重建、场景理解和移动操作任务上的价值；摘要称，在这些任务中，使用该场景训练当前先进方法相比其他合成数据集可提升性能。
- 提出移动操作基准，用于评估视觉-语言-动作模型在真实布局的多样 3D 场景中的物理抓取与放置，并利用部件标注对抓取位置进行评分。
- 数据集将公开释放，以促进视觉与具身 AI 研究。

### 局限性
- 摘要未提供足够信息说明数据集的具体规模分布，例如各类场景的数量比例、标注粒度细节或材质与几何的生成方式。
- 摘要未提供足够信息说明实验设置、基线方法细节、性能提升幅度或统计显著性。
- 摘要未提供足够信息说明移动操作基准的任务数量、评估指标细节、模型范围及失败案例分析。
- 摘要未提供足够信息说明数据集的许可协议、发布平台、维护计划或潜在偏差。
- 摘要未提供足够信息说明与其他合成数据集对比的具体数据集名称及比较维度。

### 阅读优先级
中。理由：该论文涉及具身 AI、3D 场景理解与移动操作，数据集和基准具有潜在实用价值；但摘要仅概述数据集构成与任务覆盖，未给出实验细节、性能数值或基准设计细节。若研究兴趣集中在 3D 场景数据集、逆渲染、3D 重建或视觉-语言-动作模型评测，可优先阅读全文；否则可先关注摘要与后续公开数据。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Motion Conditioned World Modeling for Embodied Visual Tracking
- 作者：Jiahao Zhang, Xuan Yao, Junyu Gao, Changsheng Xu
- 出版日期：2026-11-24T16:25:49Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32900) / [PDF](https://arxiv.org/pdf/2611.32900)

### 一句话总结
论文提出一种运动条件化的世界模型，将预测的目标运动分布与机器人自身运动引入潜在状态转移，用于提升具身视觉跟踪中的未来视觉状态预测与跟踪策略学习。

### 研究问题
具身视觉跟踪中，目标运动具有不确定性，机器人自身运动又会引起视角变化，二者共同影响视觉观测，使未来状态预测具有挑战性。论文关注如何在这种双重不确定性下建模未来视觉状态，并利用预测的运动线索辅助跟踪决策。

### 核心思路/方法
- 提出 Motion-Conditioned World Modeling，将预测的目标运动分布和机器人 ego-motion 融入潜在状态转移。
- 设计 Geometry–Progress 模块，通过共享运动模式与路径条件化的进度分布，联合建模几何路径和单步移动距离。
- 该建模方式旨在捕捉路线选择与运动进度中的不确定性，同时保留二者之间的依赖关系。
- 利用动作诱导的坐标变换，将预测路径表达在下一机器人坐标系中，为未来视觉状态预测提供几何条件。
- 通过条件化转移分支，以未来视觉特征重建监督运动预测器，将显式运动表示与后续观测关联。
- 模型联合优化运动似然、特征重建和专家动作监督，使跟踪策略结合视觉上下文与预测运动线索。

### 主要贡献
- 提出运动条件化的世界模型框架，将目标运动不确定性与机器人 ego-motion 纳入潜在状态转移。
- 提出 Geometry–Progress 模块，联合建模路径选择与运动进度的不确定性及其依赖关系。
- 通过动作诱导坐标变换为未来视觉状态预测提供几何 grounded 条件。
- 通过未来视觉特征重建监督运动预测器，将运动表示与后续观测连接。
- 摘要称在三个具身跟踪基准上使用轻量 0.5B 骨干取得更好的跟踪性能和跨环境泛化能力。

### 局限性
- 摘要未提供足够信息说明具体实验设置、基准名称、对比方法和消融实验细节。
- 摘要未提供足够信息说明模型失败场景、计算开销细节或对真实机器人部署的限制。
- 摘要未提供足够信息说明 0.5B 骨干的具体结构、训练数据规模及跨环境泛化的具体评估方式。

### 阅读优先级
中。理由：论文问题聚焦具身视觉跟踪中的运动不确定性与视角变化，方法将运动预测、世界模型和跟踪策略结合，具有一定相关性；但摘要未提供充分实验细节与失败案例分析，是否值得深入阅读需结合全文实验部分进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation
- 作者：Aly Magassouba
- 出版日期：2026-11-24T15:21:57Z
- 分类：主分类 Embodied / Robotics / AR Applications；无次要分类
- 链接：[摘要](https://arxiv.org/abs/2611.32797) / [PDF](https://arxiv.org/pdf/2611.32797)

### 一句话总结
提出 Screw Attention Policy，将任务几何（物体位姿、相对 SE(3) 变换、关节螺旋轴）显式提供，仅学习执行部分，用约 30K 参数实现仿真训练后的零样本跨机器人形态迁移与真机部署。

### 研究问题
机器人操作策略通常依赖大规模学习来获取几何结构。论文关注的问题是：能否将这些几何结构显式“供给”策略，从而只学习执行环节，并在小参数量、纯仿真训练条件下实现对新场景布局、新机器人形态的泛化与零样本迁移。

### 核心思路/方法
- 提出以几何为中心的操作框架 Screw Attention Policy。
- 策略输入为感知与机器人模型提供的物体位姿、相对 SE(3) 变换以及关节螺旋轴（joint screw axes）。
- 策略仅需 30K 可学习参数。
- 完全在仿真中、单一机械臂上训练。
- 论文报告其可泛化到新场景布局、跨机器人形态零样本迁移，并可直接部署到真实机器人，无需适应或微调。

### 主要贡献
- 提出“供给几何、学习执行”的策略设计思路，将几何结构显式输入而非完全依赖大规模学习获得。
- 以仅 30K 学习参数实现策略，并在摘要报告的指标中取得：LIBERO 96% 成功率、布局变化下 85.8%、五种未见机械臂上 80.2%、真机 24 次试验中成功 21 次。
- 展示仿真单臂训练后可零样本跨机器人形态迁移并直接真机部署，无需适应或微调。
- 摘要据此提出观点：大规模操作策略学到的很大一部分可能是几何结构，而这些结构可以被直接供给。

### 局限性
- 摘要未提供足够信息说明方法的具体网络结构、注意力机制细节及训练配置。
- 摘要未提供足够信息说明感知模块（物体位姿、SE(3) 变换、螺旋轴）的获取精度要求及其失效情形。
- 摘要未提供足够信息说明真机实验的任务类型、试验设置与统计口径。
- 摘要未提供足够信息说明跨形态迁移对机器人模型与关节螺旋轴先验的依赖程度。
- 摘要未提供足够信息说明与基线方法的系统性对比及消融结果。

### 阅读优先级
高。理由：论文给出明确且较强的量化结果（LIBERO 96%、跨五种未见机械臂 80.2%、真机 21/24），并提出“几何可供给而非学习”的可检验观点；若关注零样本策略迁移、跨形态机器人与小参数策略设计，该摘要值得优先阅读全文以核验方法与实验细节。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：MemAnchorWorld: A Sparse World Model with Horizon-Conditioned Memory Retrieval for Autonomous Driving
- 作者：Xinyang Jia, Yuqi Zhang, Jiakai Wang, Yahu Yang, Guandong Pan, Chao Tong, Xianglong Liu
- 出版日期：2026-11-24T14:56:56Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.32745 ；PDF https://arxiv.org/pdf/2611.32745 ；项目页 https://memanchorworld.github.io/

### 一句话总结
MemAnchorWorld 是一种稀疏占用世界模型，通过显式检索历史几何与语义证据，缓解稀疏世界模型在长时程 4D 语义占用预测中的误差累积问题。

### 研究问题
论文关注自动驾驶中的 4D 语义占用预测任务。现有稀疏世界模型使用少量演化查询表示场景，但在长时程预测中难以有效利用历史时序证据：它们依赖场景状态隐式携带历史信息，导致误差在连续预测步骤中传播和累积，进而产生几何与语义偏差。摘要未提供足够信息说明该问题在更广泛场景或数据集上的具体表现边界。

### 核心思路/方法
- 提出 MemAnchorWorld，一个显式检索相关历史几何与语义证据的稀疏占用世界模型，用于 4D 语义占用预测。
- 受 von Restorff 效应启发，设计“预测时间条件化的分层双路径记忆锚点检索机制”。
- 该机制以历史信息的有效年龄和语义兼容性为指导，结合查询级候选选择与点级记忆锚点检索，为不同预测时间下的稀疏点提供历史证据。
- 引入点级残差适配器，由任务和预测时间联合门控，分别控制对语义、占用置信度和空间位置的残差修正，以更好利用记忆锚点和现有特征。
- 摘要未提供足够信息说明各模块的网络结构细节、训练策略或消融实验设置。

### 主要贡献
- 针对稀疏世界模型长时程预测中历史时序证据利用不足、误差传播累积的问题，提出显式历史证据检索方案。
- 提出预测时间条件化的分层双路径记忆锚点检索机制，结合查询级与点级检索。
- 提出任务与预测时间联合门控的点级残差适配器，用于语义、占用置信度和空间位置的残差修正。
- 在 Occ3D-nuScenes 上，1–3 秒预测时程内取得平均 mIoU 13.55% 和平均 IoU 22.84%，摘要称两项指标均达到 state-of-the-art。
- 摘要未提供足够信息说明与其他方法的具体对比范围、统计显著性或多数据集验证情况。

### 局限性
- 摘要仅报告 Occ3D-nuScenes 上的结果，是否在其他数据集或驾驶场景中有效，摘要未提供足够信息。
- 摘要未提供足够信息说明模型参数量、推理时延、计算开销或实时性表现。
- 摘要未提供足够信息说明记忆机制在极长时程、遮挡或历史信息缺失情况下的鲁棒性。
- 摘要未提供足够信息说明各模块的消融实验、失败案例或误差分析。
- 摘要未提供足够信息说明“state-of-the-art”所比较的具体基线方法与评测协议细节。

### 阅读优先级
高。理由：该论文直接面向自动驾驶 4D 语义占用预测中的长时程稀疏世界模型问题，提出明确的历史记忆检索与残差修正机制，并在摘要中给出 Occ3D-nuScenes 上的定量结果和 SOTA 声明；若研究兴趣涉及稀疏世界模型、时序记忆检索或占用预测，值得优先阅读。但需注意摘要未提供实验细节与多数据集验证信息，深入结论应结合全文核实。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing to Drive on a Single Board: Attention-Free Depth for Onboard Robot Navigation
- 作者：Itai Mizlish, Boaz Ben-Moshe
- 出版日期：2026-11-24T14:39:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32718) / [PDF](https://arxiv.org/pdf/2611.32718)

### 一句话总结
论文面向单板机器人平台（Raspberry Pi 5 + Hailo-8L），指出将 Depth Anything V2 直接量化为 int8 会因注意力 softmax 权重过小造成显著精度损失，转而用无注意力机制的 ResNet-34 U-Net 学生模型蒸馏 Depth Anything V2-Large，并在该芯片上实现实时深度估计与导航栈。

### 研究问题
小型地面机器人仅能携带一个相机和少量算力，而可把相机变为距离传感器的深度基础模型通常是面向 GPU 的视觉 Transformer。论文关注：在整层整数运算（含注意力）的 Hailo-8L 加速器上部署此类模型时，量化会带来何种精度损失、原因是什么，以及如何在单板上实现可用的深度感知与导航。

### 核心思路/方法
- **量化问题诊断**：将 Depth Anything V2 量化到 Hailo-8L 后，模型丢失场景的大片区域；作者测量发现，在 449 个 token 时，91% 的 softmax 权重低于一个 int8 步长，但这些权重承载了 17–33% 的注意力质量。
- **蒸馏而非量化**：采用无注意力的 ResNet-34 U-Net 学生模型（24.5M 参数）蒸馏 Depth Anything V2-Large。
- **部署与验证**：学生模型在芯片上达到 27.1 FPS，其 int8 输出与浮点版本高度一致（Pearson 0.99993）；在仿真场地的留出场景中，它是该芯片上最准确的深度网络（AbsRel 0.269，对比 0.354–0.530）。
- **真实场景对比**：在真实户外驾驶的 1,000 个立体验证点上，与厂商的 Depth Anything V2-Small 构建相比无显著差异，但运行更快（27.1 vs 21.6 FPS）。
- **导航栈**：利用障碍物与地面相交位置进行测距，仅需相机高度；建图、混合 A* 规划与 SLAM 运行在 Pi 自身 CPU 上。

### 主要贡献
- 量化分析并解释了 Depth Anything V2 在整数注意力加速器上的精度退化原因（softmax 权重低于 int8 步长）。
- 提出以无注意力学生模型蒸馏替代直接量化，在 Hailo-8L 上实现实时、int8 一致的深度估计。
- 在仿真与真实户外场景中对比了学生模型与厂商 Depth Anything V2-Small 构建的精度与速度。
- 构建了完整的单板导航栈（深度测距、建图、混合 A* 规划、SLAM），并在高斯泼溅重建的真实场地中进行硬件在环测试：实时栈在 10 个场景中 7.9±1.1 次无接触到达目标，精确障碍物条件下为 9.2±0.4；使用自身位姿与模拟轮式里程计为 7.7±0.7；真实 Pi 与 Hailo-8L 在环时为 8.2±0.4（5 个种子）。
- 开源代码、预训练模型与数据（GitHub 链接见摘要）。

### 局限性
- 摘要未提供足够信息说明学生模型在更广泛真实场景（非特定仿真场地或单次户外驾驶）中的泛化能力。
- 摘要未提供足够信息说明导航栈在动态障碍、复杂地形或不同机器人平台上的表现。
- 摘要未提供足够信息说明蒸馏训练数据规模、训练成本及对教师模型版本的依赖程度。
- 摘要未提供足够信息说明与更多其他深度模型或量化方案的全面对比。

### 阅读优先级
**高**。理由：论文针对边缘设备上深度基础模型部署中的具体量化瓶颈给出了可解释的测量与替代方案，并提供了完整的单板导航栈及硬件在环实验结果，对机器人嵌入式感知与部署方向具有直接参考价值；同时开源代码与模型，便于复现与进一步评估。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving
- 作者：JiaHui Huang, Songyan Zhang, Hanbing Li, Hanchao Leng, Kuiyuan Yang, Guang Chen, Hangjun Ye, Chen Lv
- 出版日期：2026-11-24T12:41:13Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32510) / [PDF](https://arxiv.org/pdf/2611.32510)

### 一句话总结
GeoVLDrive 提出一种几何接地的视觉-语言-动作规划框架，通过引入 3D 基础模型特征与结构化隐式思维链，增强自动驾驶规划的三维时空推理能力。

### 研究问题
现有视觉-语言-动作（VLA）规划器虽继承预训练视觉-语言模型的语义知识，但其推理很少真正基于三维场景结构及其随时间演化的过程。论文旨在解决 VLA 规划中缺乏几何接地与时空推理的问题。

### 核心思路/方法
- 使用 3D 基础模型的多层特征，通过门控交叉注意力增强视觉-语言骨干网络。
- 设计结构化隐式思维链（CoT），将未来场景几何、关键智能体运动与元动作组织为有序、分别监督的隐式状态。
- 由动作专家基于这些状态与多层场景特征生成轨迹提案，并利用场景接地、相互作用的评分 token 对提案进行排序。
- 提出 NAVSIM 3DQA，用于训练与评估度量级三维空间与运动理解。

### 主要贡献
- 提出几何接地的 VLA 框架 GeoVLDrive，用于三维时空推理与规划。
- 引入结构化隐式 CoT，将未来几何、关键智能体运动与元动作纳入有序监督的隐式状态。
- 设计基于场景接地评分 token 的轨迹提案生成与排序机制。
- 提出 NAVSIM 3DQA 基准，用于度量三维空间与运动理解。
- 报告结果：NAVSIM v1 上 91.8 PDMS，NAVSIM v2 上 90.9 EPDMS；NAVSIM 3DQA 上几何接地骨干总体 89.2%，比微调的 Qwen3-VL-2B 基线高 4.6 个百分点；LingoQA 上 Lingo-Judge 准确率 68.6%。

### 局限性
摘要未提供足够信息。摘要未说明计算开销、推理延迟、模型规模、训练数据规模、失败案例、消融实验细节及 NAVSIM 3DQA 的具体构成与评测协议。

### 阅读优先级
中。理由：该工作针对 VLA 规划中几何接地不足的关键问题，提出较完整的方法与评测基准，并在多个指标上给出明确结果；但摘要未提供实验细节与局限性信息，是否值得深入阅读需结合全文的实验严谨性、可复现性与实际部署代价进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution
- 作者：Zhilu Zhang, Xiaoyu Liu, Wenxi Liu, Shengfeng He
- 出版日期：2026-11-24T12:03:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32473) / [PDF](https://arxiv.org/pdf/2611.32473)

### 一句话总结
OmniPersist 提出了一种在单阶段扩散模型中将透视视频生成与全景演化耦合起来的统一框架，旨在解决相机转离再转回时视野外动态对象无法合理演化、容易突变或消失的问题。

### 研究问题
论文关注动作条件世界模型中的动态对象持续性问题：现有视频扩散模型在相机转向别处再转回时，视野外的运动实体在潜空间中无法合理演化，常常发生突变或完全消失，作者将这一问题的根源归结为有界透视视角的限制。

### 核心思路/方法
- 提出 OmniPersist，一个统一框架，在单阶段扩散模型内耦合透视视频生成与全景演化，不依赖辅助模型，也不需要初始全景输入。
- 为保持效率，全景流以较低帧率建模。
- 通过 Geometric Anchoring (GeoAnch) 实现空间对应，通过 Temporal Compensation (TemComp) 实现时间聚合，从而在空间和时间两个维度上桥接两种视角。
- 该方法对相机控制架构不敏感，同时支持潜空间层级和注意力层级的条件注入。
- 在新构建的动态基准上，围绕图像到视频与视频延续两类任务开展了广泛实验。

### 主要贡献
- 针对有界透视视角导致的视野外动态实体演化不合理问题，提出单阶段耦合透视生成与全景演化的统一框架。
- 设计 GeoAnch 与 TemComp 两个组件，分别负责跨视角的空间对应和跨时间的信息聚合，并以低帧率全景流控制计算开销。
- 方法不依赖辅助模型或初始全景输入，且兼容潜空间级与注意力级的相机控制架构。
- 构建了新的动态基准，并在图像到视频和视频延续任务上报告了视觉质量、相机可控性、重访一致性和动态持续性方面的一致提升。

### 局限性
- 摘要未提供足够信息说明方法的具体计算开销、推理速度或显存占用。
- 摘要未提供足够信息说明新构建动态基准的规模、数据来源与评价指标细节。
- 摘要未提供足够信息说明失败案例、极端相机运动下的表现，以及与基线方法的定量对比数值。
- 摘要未提供足够信息说明低帧率全景流建模对快速运动对象的影响。

### 阅读优先级
中。理由：该工作面向动作条件世界模型中的动态对象持续性这一明确问题，方法思路（透视与全景耦合、几何锚定与时间补偿）具有针对性，且与具身智能、机器人、AR 应用方向相关；但摘要仅给出定性结论，未提供定量结果与实现细节，是否值得深入阅读需结合全文实验数据进一步判断。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Can You Find the Edit When Nothing Looks Wrong? A Paired Benchmark for Text-Driven Image Manipulation Localization Beyond Semantic Abnormality
- 作者：Peiyu Zhuang, Jianquan Yang, Zhuoying Cai, Yi Jiang, Yingquan Chen, Xinle Wang, Zeqin Yu, Dongdong Lin, Ruitao Xie, Kaige Li, Xiaochun Cao
- 出版日期：2026-11-24T09:19:33Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2611.32242 ；PDF：https://arxiv.org/pdf/2611.32242

### 一句话总结
论文构建了一个配对基准，对同一目标分别生成语义上合理与语义上异常的编辑，用于衡量文本驱动图像篡改定位在“语义合理性”变化下的性能差异。

### 研究问题
现有基准缺少针对同一目标的、匹配的“合理编辑”与“异常编辑”配对，因此难以衡量定位性能如何随语义合理性变化。论文关注的问题是：当编辑结果在语义上看起来正常、并不显眼时，篡改定位是否仍然有效。

### 核心思路/方法
论文为每张源照片中的同一目标生成语义合理与语义异常的替换版本；两种编辑使用相同的编辑器、语言和生成设置。随后为每个输出估计独立掩码，并保留掩码重叠足够的配对，从而在两种语义条件下直接比较定位性能。发布数据包含来自 6,500 张照片的 47,747 个双语三元组，覆盖四种编辑器、三个源域和六种预期违规类型。

### 主要贡献
1. 构建了配对基准，使同一目标的合理编辑与异常编辑可在受控条件下直接比较。
2. 数据集规模为 47,747 个双语三元组、6,500 张照片，覆盖四种编辑器、三个源域和六种预期违规类型。
3. 在九个公开定位器上进行评估，发现在 27 组“模型—数据集”比较中有 26 组的编辑器平均 IoU 在合理编辑上更低。
4. 该差距在像素变化控制和区域大小分析下仍然存在，作者将其归结为“语义合理性捷径”：当编辑结果看起来普通时，定位往往变弱。

### 局限性
摘要未提供足够信息说明基准在真实场景覆盖、编辑器类型外推、掩码估计误差影响等方面的具体局限；也未提供足够信息说明像素变化控制和区域大小分析的详细设置与边界条件。

### 阅读优先级
中。理由：该论文提出了一个与篡改定位评测直接相关的配对基准，并报告了跨多个定位器的一致现象，对关注图像编辑定位与基准评测的研究者有参考价值；但摘要未展开具体方法细节与实验设置，且分类标注为 Embodied / Robotics / AR Applications，与主题的匹配度需进一步查看全文确认。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：NativeDrive: Native Multimodal Foundations for Autonomous Driving
- 作者：Zehua Fan, Qi Jiang, Wei Li, Kai Tang, Yue Jiang, Yujian Li, Bailin Li, Feng Gao, Yan Wang, Kun Zhan
- 出版日期：2026-11-24T08:59:01Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32216) / [PDF](https://arxiv.org/pdf/2611.32216)

### 一句话总结
NativeDrive 是一个无编码器的原生多模态自动驾驶框架，它在统一的“理解—生成”主干网络上适配策略学习，并通过复用理解专家与生成专家的接口，实现离散与连续策略以及训练期的稠密场景结构监督。

### 研究问题
自动驾驶需要语义理解和细粒度场景感知，以便精确预测动作。视觉—语言—动作模型（VLA）继承了语义先验，但低维动作标签提供的结构监督有限；已有工作用视觉生成任务扩展 VLA，或采用基于视频的世界—动作模型（WAM），但这两类方法都会引入外观重建开销，而这种开销与规划的相关性较低。论文关注的是：如何在单一原生多模态主干内统一理解与生成，并为驾驶策略学习提供更充分的监督，同时避免上述外观重建开销。

### 核心思路/方法
- 提出 NativeDrive：一个无编码器的原生多模态驾驶框架，将统一主干适配于策略学习，并引入面向驾驶的稠密监督任务。
- Native Action Interface：复用理解专家的 token 预测接口来输出离散策略，并适配生成专家来输出连续策略。
- Driving Semantic Editing：训练时复用生成专家的编辑能力，提供稠密的场景结构监督；推理时只运行选定的规划策略。
- 摘要称该框架在 NAVSIM v1 和 v2 上，于统一理解—生成模型中取得有竞争力的规划表现，并通过消融实验验证了各组件的有效性。

### 主要贡献
- 提出无编码器的原生多模态自动驾驶框架 NativeDrive，在统一主干上同时利用理解与生成能力服务驾驶策略。
- 设计 Native Action Interface，分别复用理解专家与生成专家来支持离散策略和连续策略。
- 提出 Driving Semantic Editing，将生成专家的编辑能力用于训练期的稠密场景结构监督，且不增加推理阶段负担。
- 在 NAVSIM v1 和 v2 上报告了统一理解—生成模型中有竞争力的规划性能，并给出组件消融验证；摘要提到代码将发布。

### 局限性
- 摘要未提供足够信息说明具体实验设置、对比基线、评价指标细节、消融实验的具体数值，以及计算成本或推理效率。
- 摘要未提供足够信息说明 Driving Semantic Editing 的具体监督形式、数据需求与潜在失败场景。
- 摘要未提供足够信息说明该方法在 NAVSIM 之外数据集或真实场景中的泛化表现。
- 摘要未提供足够信息说明“无编码器”设计对输入分辨率、模态对齐和训练稳定性的具体影响。

### 阅读优先级
中。理由：该论文聚焦自动驾驶中统一多模态理解与生成、策略接口复用和训练期稠密监督，问题定位清晰，且声称在 NAVSIM v1/v2 上有竞争力的规划表现；但当前仅有摘要与元数据，缺少实验细节与定量结果，适合作为方向跟踪阅读，待全文或代码发布后再决定是否深入复现。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Instant LiDAR: Feed-Forward Gaussian Reconstruction for LiDAR Simulation
- 作者：Xin Kang, Jiahui Huang, Jiawei Ren, Sipeng Zhang, Yu Chen, Weihua Zhang, Junjie Lai
- 出版日期：2026-11-24T06:27:32Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.32042) / [PDF](https://arxiv.org/pdf/2611.32042)

### 一句话总结
提出一种前馈式 LiDAR 高斯重建流水线，无需逐场景优化，即可在数分钟内将多帧 LiDAR 扫描重建为可复用的高斯资产，用于自动驾驶仿真。

### 研究问题
LiDAR 重建可支撑闭环自动驾驶仿真，但逐场景优化需耗时数小时，导致大规模资产库的构建与维护成本高昂。直接以 LiDAR 测量初始化高斯会因非均匀采样与有限视场导致重建质量差：稀疏回波造成表面空洞，合并多帧虽扩大覆盖却引入冗余基元。

### 核心思路/方法
Instant LiDAR 采用前馈流水线，将多帧 LiDAR 扫描重建为可复用的高斯资产，无需逐场景优化。方法包含三个关键组件：
1. **测量锚定的高斯预测**：预测器对锚定于记录回波的属性进行细化；
2. **采样感知的高斯尺度**：使空间支撑适配 LiDAR 采样特性；
3. **多帧整合**：将重叠预测合并为覆盖整个驾驶日志的紧凑资产。

### 主要贡献
- 提出无需逐场景优化的前馈 LiDAR 高斯重建流水线，可在数分钟内重建多帧扫描为可复用资产。
- 针对 LiDAR 非均匀采样与有限视场问题，设计测量锚定预测、采样感知尺度与多帧整合三项机制。
- 摘要报告：在 Physical AI（PAI）上重建速度约为 NuRec 的 46 倍，在 Waymo 上约为 70 倍；在 Waymo 上达到可比的下游 3D 检测精度。

### 局限性
- 摘要未提供足够信息说明方法在不同 LiDAR 配置、稀疏程度或场景类型下的泛化表现。
- 摘要未提供足够信息说明多帧整合的具体误差累积或冗余控制效果。
- 摘要未提供足够信息说明除 3D 检测外的其他下游仿真指标。
- 摘要未提供足够信息说明与 NuRec 对比之外的基线或消融结果。

### 阅读优先级
**中**。理由：该工作针对自动驾驶仿真中 LiDAR 资产构建成本高的实际问题，提出前馈重建思路并报告显著加速与可比下游精度，具有一定工程与应用价值；但摘要未提供方法细节、泛化性与消融信息，是否深入阅读取决于对 LiDAR 仿真资产构建或前馈高斯重建方向的兴趣。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：VLG-Drive: Unifying Vision-Language and Geometric Priors for Autonomous Driving
- 作者：Junge Zhang, Jie Zhu, Yanqi Jia, Xiangyu Xu, Zixun Huang, Wenbin He, Xin Li, Jiachen Li, Liu Ren
- 出版日期：2026-11-24T04:57:54Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.31952 ；PDF https://arxiv.org/pdf/2611.31952

### 一句话总结
VLG-Drive 冻结视觉语言模型和几何基础模型，仅训练融合接口与规划器，将两类特征逐点融合为联合 token 后预测自车轨迹。

### 研究问题
驾驶规划器既需要视觉语言模型提供的场景语义，也需要几何基础模型从视觉历史中恢复的空间结构。论文关注如何在不微调这两类基础模型的前提下，有效结合语义与几何信息用于规划。

### 核心思路/方法
- 保持 VLM 与几何基础模型冻结，只从轨迹标签训练一个融合接口和一个规划器。
- 在每个相机网格单元上，通过“几何锚定的残差”将配对的 VLM 特征与几何特征融合为一个联合 token。
- 规划器以指令为条件，读取这些联合 token 并预测自车轨迹。

### 主要贡献
- 提出 VLG-Drive，将视觉语言先验与几何先验通过轻量融合接口统一到驾驶规划中，且不调整两个基础模型。
- 在 NavHard 扰动初始状态下取得 31.78 EPDMS，摘要称其为对比方法中最高；在 NavTest 仅用相机输入取得 88.27 PDMS。
- 两个基准上逐点融合均优于独立的 VLM 流和几何流。
- 在 420 个 HUGSIM 场景的闭环驾驶中，摘要称其优于所有对比规划器。
- 结论上，基于冻结视觉语言与几何基础模型融合特征训练轻量规划器，可作为适配任一模型用于规划的有效替代方案。

### 局限性
- 摘要未提供足够信息说明融合接口的具体结构、训练细节、参数量与计算开销。
- 摘要未提供足够信息说明各基准的完整对比方法列表、统计显著性与失败案例分析。
- 摘要未提供足够信息说明对 VLM 或几何模型输出质量、相机配置及扰动类型的敏感性。
- 摘要未提供足够信息说明真实道路部署验证情况；闭环结果仅提及 HUGSIM 场景。

### 阅读优先级
中。理由：问题定位清晰，冻结双基础模型加轻量融合的思路对自动驾驶规划有参考价值，且摘要给出多项基准与闭环结果；但当前仅有摘要，缺少方法细节、消融设置与局限性讨论，需阅读全文后再判断其可复现性与实际影响。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Gaze World Model
- 作者：Jiawen Zhang, Houze Yang, Xu Cao, Yifan Shen, Zhongyi Zhou, Steve Wong, Ismini Lourentzou, Inki Kim, James M. Rehg
- 出版日期：2026-11-24T02:32:30Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次级分类信息
- 链接：摘要页 https://arxiv.org/abs/2611.31836 ；PDF https://arxiv.org/pdf/2611.31836

### 一句话总结
论文提出 Gaze World Model（GWM），在冻结的 V-JEPA 2.1 编码器上联合训练潜在场景预测与以人物为条件的注视监督，用于估计注视位置、检测注视转移并预测未来注视与转移。

### 研究问题
摘要指出，既有的注视目标估计方法大多逐帧运行，不建模注视如何在目标之间转移；而注视转移常由场景的动态变化驱动，这种信息正是世界模型所擅长编码的。但场景变化与注视变化之间的关系并不显眼：画面远处发生的事件可能只引起人物头部或眼睛的轻微运动。因此，论文关注如何在视频中建模场景动态与人物注视转移之间的关系，并完成注视位置估计、注视转移检测以及未来注视与转移预测。

### 核心思路/方法
- 在冻结的 V-JEPA 2.1 编码器上，联合训练潜在场景预测目标与以人物为条件的注视监督。
- 输入视频片段与人物头部框，GWM 估计观察片段内的注视位置并检测注视转移。
- 基于预测的场景特征，进一步预测未来的注视与注视转移。
- 摘要提到消融显示潜在预测目标同时改善转移检测与注视定位。

### 主要贡献
- 提出 Gaze World Model（GWM），将潜在场景预测与人物条件注视监督协同训练于冻结 V-JEPA 2.1 编码器之上。
- 将注视转移检测与未来注视/转移预测纳入统一建模框架，而不仅做逐帧注视目标估计。
- 为 VideoAttentionTarget 与 ChildPlay 增加事件级注视转移标注，用于训练与评测上述任务。
- 据摘要，GWM 在两个基准上取得最先进的转移检测结果，四类 AP 比最强基线约高 10 个点；注视目标估计与最强图像模型相当；在未来注视定位与转移预测上优于所比较的基线。

### 局限性
- 摘要未提供足够信息说明模型计算开销、推理速度或实时性。
- 摘要未提供足够信息说明所增事件级标注的具体规模、标注一致性或数据偏差。
- 摘要未提供足够信息说明在更复杂场景、多人交互或跨数据集泛化方面的表现。
- 摘要未提供足够信息说明失败案例或对头部框质量的敏感程度。
- 摘要未提供足够信息说明与最强图像基线“相当”的具体数值差距。

### 阅读优先级
中。理由：论文主题聚焦视频中的注视转移建模与未来注视预测，并把世界模型式潜在预测引入注视分析；摘要给出了明确的基准结果与约 10 点四类 AP 提升，对该方向有参考价值。但摘要未提供方法细节、数据规模与泛化性信息，且分类偏具身/机器人/AR 应用，是否高优先级取决于读者对注视建模与世界模型交叉方向的兴趣；在仅基于摘要判断时定为中。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：Beyond the Benchmark: Localizing Released Autonomous Driving Models to Real Vehicles
- 作者：Morui Zhu, Deyuan Qu, Qi Chen, Qing Yang
- 出版日期：2026-11-24T02:06:37Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2611.31814 ；PDF https://arxiv.org/pdf/2611.31814 ；项目页 https://released-to-real.github.io

### 一句话总结
论文研究已发布自动驾驶模型迁移到新真实车辆上的部署差距，提出 Released-to-Real（R2R）部署定位方法，通过识别并只修正与源系统耦合的组件，在不替换已发布模型的前提下完成数据、行为与物理传感器的适配。

### 研究问题
已发布自动驾驶模型在基准测试上表现良好，但部署到新的真实车辆仍具挑战性。作者发现，即使经过常规适配，已发布模型仍可能与其源感知、数据和执行过程的假设相耦合。论文要解决的是：如何定位这些源系统耦合，并只修正受影响部分，同时保留已发布模型本身。

### 核心思路/方法
- 提出 R2R（Released-to-Real）部署定位方法：识别源系统耦合，只修正受影响组件，保留已发布模型。
- 在数据与行为适配方面，发现轨迹级优化与滚动时域执行之间的不匹配通过自车状态而非观测进入，提出 Human-Anchored Reinforcement Learning（HA-RL），在记录的目标驾驶数据上修正该问题，避免生成式闭环强化学习所需的高成本 rollout。
- 在物理传感器适配方面，R2R 在冻结感知权重的情况下定位并修正依赖源系统的空间与时间表示，不需要目标标注，也不需要重新训练。

### 主要贡献
- 揭示并形式化了已发布自动驾驶模型在真实车辆部署中的“源系统耦合”问题。
- 提出 R2R 部署定位方法论，强调只修正受影响组件并保留已发布模型。
- 提出 HA-RL，用于修正轨迹级优化与滚动时域执行之间经自车状态传导的不匹配。
- 给出去标注、免重训的物理传感器空间与时间表示修正方案。
- 摘要报告的结果：HA-RL 将已发布扩散规划器的闭环成功率从 82.2% 提升到 95.2%；跨多个已发布检测器和三个真实传感器装置进行传感器适配后，某已发布多相机检测器在五相机目标装置上的车辆 mAP 从 0.041 提升到 0.420。

### 局限性
摘要未提供足够信息说明方法在更多车型、更多传感器配置或更多已发布模型上的泛化能力；也未提供计算开销、失败案例、安全性验证、实验规模与统计显著性等细节。摘要未提供足够信息说明 HA-RL 与传感器适配的具体实现限制及对目标数据数量的依赖程度。

### 阅读优先级
中。理由：论文聚焦已发布自动驾驶模型向真实车辆部署的落地问题，提出“定位源系统耦合并只修正受影响组件”的思路，并给出闭环成功率与跨传感器装置的 mAP 提升结果，对具身/机器人及自动驾驶部署实践有参考价值；但摘要未展开实验规模、泛化性与安全性细节，需阅读全文后再判断其方法稳健性与适用范围。

</details>

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
<summary>AI 简析</summary>

### Metadata
- 标题：FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator
- 作者：Wenkang Hu, Haoran Wang, Liu Liu, Wenchao Huang, Yiji Chen, Mengao Zhao, Xincheng Tang, Zhengjie Shu, Lai Jiang, Wei Li, Zhendong Wang, Zhizhong Su, Huamin Wang, Ruigang Yang
- 出版日期：2026-11-23T21:19:02Z
- 分类：主分类 Embodied / Robotics / AR Applications；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.31577 ；PDF https://arxiv.org/pdf/2611.31577 ；项目网站 https://fabricbench.github.io/

### 一句话总结
FabricBench 是一个面向双臂布料操作的标准化策略基准，基于接触驱动的可变形仿真器，提供六类任务、一万个仿真就绪资产，并系统评测配置与外观泛化能力。

### 研究问题
摘要指出，布料操作因几何持续变化、自遮挡和接触交互而对机器人策略构成挑战，但标准化评测仍主要集中于刚性物体。论文旨在填补双臂布料操作缺乏可复现、标准化评测基准的空白，并检验现有代表性策略在配置泛化与外观泛化上的表现。

### 核心思路/方法
- 构建 FabricBench 基准：包含跨越服装、丝绸、包袋的六项双臂布料操作任务，提供 10,000 个仿真就绪资产，并设置对配置与外观泛化的受控测试。
- 仿真器基于 Newton 中的开源求解器，通过接触力实现稳定的双臂抓取、保持与释放，不采用人工附着。
- 重新设计布料—刚性体接触与双向力耦合，支持机械臂、布料与自由刚性物体之间的交互；摘要以包袋承载内容物并向夹爪传递重量为例说明该能力。
- 在受控的抓取—保持—释放评测中，该求解器在全部 45 次试验中成功，而所测试的基线配置全部失败。
- 评测六种代表性策略，包括视觉—语言—动作模型与世界动作模型；并将 π₀.₅ 零样本部署到真实机器人，在六项任务上检验难度排序一致性（Spearman ρ=0.94）。

### 主要贡献
- 提出面向双臂布料操作的标准化策略基准 FabricBench，覆盖多类布料对象与六项任务。
- 提供接触驱动的可变形仿真器设计，强调无需人工附着的抓取、保持与释放，以及布料—刚性体双向力耦合。
- 给出受控的抓取—保持—释放验证结果：所提求解器 45/45 成功，测试的基线配置为 0。
- 对六种代表性策略进行评测，揭示长时程折叠与强变形初始配置下的显著性能不足：最佳策略平均成功率 77%，但在长时程 T 恤折叠任务上无策略超过 36%；在最变形的初始 T 恤配置下，各策略成功率降至 6%–14%，且降幅大于所评估的外观变化。
- 通过真实机器人零样本部署初步检验仿真任务难度排序的可迁移性（Spearman ρ=0.94）。

### 局限性
- 摘要未提供足够信息说明仿真器与真实世界之间的物理保真度、仿真到现实的系统性差距及其定量评估细节。
- 摘要未提供足够信息说明六项任务的具体定义、成功判定标准、评测规模与统计显著性。
- 摘要未提供足够信息说明 10,000 个仿真就绪资产的来源、多样性构成与质量筛选流程。
- 摘要未提供足够信息说明所评测六种策略的具体名称、训练数据与算力配置（仅提及类别与 π₀.₅ 的零样本部署）。
- 摘要未提供足够信息说明基线配置的具体内容，以及 45 次试验之外更广泛求解器鲁棒性测试的结果。
- 摘要未提供足够信息说明真实机器人实验的平台、任务设置与样本量。

### 阅读优先级
高。理由：该工作直接针对双臂布料操作缺乏标准化评测的问题，提供任务、资产与仿真器设计，并给出多策略对比及仿真—真实难度排序一致性的初步证据；对关注可变形物体操作、策略泛化评测与仿真基准构建的研究者具有较高参考价值。

</details>

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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
