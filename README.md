# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：66
- 分类分布：
  - Embodied / Robotics / AR Applications: 26
  - Neural Scene Representations & Rendering: 17
  - 3D Reconstruction & Multi-view Geometry: 12
  - Dynamic / 4D Reconstruction: 7
  - Geometry Foundation Models: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1.  **从全局优化到诊断与可控编辑：3D场景表示正从“黑盒”走向“可解释”与“可控”。** 过去，工作重心是提升NeRF/3DGS的重建精度和渲染速度。今天，我们看到一个明确的转向：研究者不再满足于获得一个“好”的场景，而是开始关注场景的内部机理和编辑能力。例如，**Vis4GS** 直接为3DGS重建过程提供基元级可视化诊断工具，链接伪影与高斯属性。而 **Sculpting NeRF Geometry** 和 **Capacity-Controlled Multi-View Stylization** 分别通过人类偏好和最优运输理论，对场景的几何形状和风格进行精细调控。这表明社区开始将“可解释性”和“可控性”视为与“保真度”同等重要的指标。

2.  **物理先验与感知反馈深度融合：机器人/AR系统从“感知-建图”的线性流程，转向“建图-感知-控制”的闭环主动系统。** 传统的SLAM和建图往往是“一次性”的，缺乏任务导向和主动适应能力。今日的多篇论文展示了深刻的范式转变。**KRVF** 通过引入“来源感知”的体素和建图-感知反馈回路，让地图能主动修复深度失效区域。**RoboAtlas** 通过上下文多臂赌博机，让机器人能动态平衡几何探索与语义推理，实现主动SLAM。**UAV-MapFusion** 利用不确定性感知因子图，在合并多会话地图时，既抑制长程漂移又保持局部精度。这些工作共同描绘了下一代机器人世界模型的雏形：它利用先验知识（物理、地理）来指导感知，并基于感知结果主动调整建图和规划策略。

3.  **实用主义导向的鲁棒性突破：解决极端或退化场景下的“最后一公里”问题。** 许多经典问题（如单目重建、相对位姿估计、多会话地图合并）在理想条件下已取得不错效果，但今天的论文致力于攻克这些任务的“阿喀琉斯之踵”。**PanoImager** 专注于无SfM的场景，解决极稀疏全景图下的旋转主导和弱视差问题。**Rolling Shutter Relative Pose Estimation Made Practical** 通过仿射对应将所需匹配点数从20降至7，使RS相机的位姿估计在RANSAC框架中变得可行。**MIL-LC** 另辟蹊径，利用环境磁场作为互补模态，解决LiDAR在几何重复或纹理缺失场景中的退化问题。这反映出研究前沿正从“如何做得更好”转向“如何在最坏条件下也能工作”。

4.  **跨模态对齐与表示学习：生成式3D模型的瓶颈从“生成式模型能力”转向“表示学习与跨模态对齐”。** 以 FLUX3D 为代表的工作强调，单图生成3D场景的核心障碍不仅仅是扩散模型的强大与否，更是如何构建一个能保留2D高频细节、且与扩散潜空间良好对齐的3D表示。同样，**FLAT** 直接证明，可以从视频扩散潜码解码出几何更精确的三角形基元，这需要对3D表示进行精巧的参数化（如射线居中的旋转参数化）和训练技巧（如乘积窗函数）。这表明，3D生成任务的未来突破点在于设计更智能的3D表示和学习目标，使其能“理解”并“利用”预训练2D模型中蕴含的丰富先验。

#### 技术路线观察

| 技术路线 | 主要论文 | 侧重点对比 |
| :--- | :--- | :--- |
| **几何基础模型** | **Rolling Shutter Pose Estimation, DSP-SLAM++, Invariant Kalman Filter** | 侧重于经典几何问题的鲁棒求解。前者通过巧妙的数学推导增加信息量（仿射对应），后两者通过优雅的状态估计框架（不变卡尔曼滤波、异步建图流水线）解决多IMU或物体级SLAM的精度和实时性问题。 |
| **3D/4D 重建** | **PanoImager, PRISM, FLAT, FLUX3D** | 全力冲刺“单图/极稀疏图”到3D的快速重建。它们都采用“先验+可学习模块”的解耦策略。**PanoImager** 依赖前馈深度/姿态先验；**PRISM** 显式分解为几何扭曲先验和残差校正；**FLAT/FLUX3D**则依靠预训练的视频扩散模型。关键差异在于：PRISM追求无扩散采样的速度，而FLUX3D和FLAT追求更高的几何/外观精度。 |
| **神经场景表示** | **Vis4GS, Sculpting NeRF Geometry, Capacity-Controlled Stylization, GastroNVS** | 从“构建”转向“诊断、编辑与应用”。**Vis4GS** 是分析工具，**Sculpting NeRF**和**Stylization**是编辑方法，而**GastroNVS**则是特定应用（胃镜）的基准测试。它们不再是追求极致的渲染质量，而是赋予场景表示“可理解”和“可操作”的属性。 |
| **机器人/AR应用** | **RoboAtlas, UAV-MapFusion, KRVF, MIL-LC, fARfetch, OSC2Runner** | 核心驱动力是“鲁棒性”和“实用性”。研究方向扩散，但都瞄准真实世界的痛点：**RoboAtlas** 处理语义探索与几何探索的平衡；**UAV-MapFusion** 解决大规模、多会话地图的漂移问题；**MIL-LC** 应对传感器退化；**fARfetch** 克服户外AR的视距限制。共同特点是融合多源信息（VLM、RTK、磁力计）来增强单一传感器的不足。 |

#### 值得优先阅读的论文

1.  **PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling**
    - **优先级最高**。它代表了一种极有前途的单图3D重建范式：通过巧妙的物理洞察（几何扭曲可以覆盖大部分内容），实现了无需迭代采样的前馈式重建，在质量和速度之间取得了新的平衡，是图到3D领域的一个潜在里程碑。

2.  **FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation**
    - **优先级高**。它清晰指出了当前稀疏体素生成派方法的双瓶颈（表示瓶颈和跨模态对齐瓶颈），并提供了系统性的解决方案（DA-SLAT和SMDiT）。对于所有从事图像到3D资产生成的研究者来说，这篇论文的分析和解决方案具有很高的参考价值。

3.  **Rolling Shutter Relative Pose Estimation Made Practical**
    - **优先级高**。这篇论文解决了一个长期悬而未决的工程痛点。理论推导（RS校正的仿射约束）扎实，配套的高速求解器（1.2毫秒）极具实用价值。对于SLAM、SfM和多视图几何领域的研究者，这是理解滚动快门相机几何的必读材料。

4.  **RoboAtlas: Contextual Active SLAM**
    - **优先级中到高**。这篇论文代表了机器人主动SLAM的最高水平，它巧妙地将底层几何探索、中层语义地图和高层VLM推理整合在一个统一的概率框架（上下文多臂赌博机）下，并在1800平方米的真实场景中取得了接近完美的成功率。对于机器人领域的学者，这是一个值得深入学习的集成系统。

5.  **Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction**
    - **优先级中**。虽然它不是一个算法突破，但对3DGS社区非常有价值。它为开发者提供了调试和优化3DGS模型的强大工具，揭示了伪影与内部参数的关联，有助于推动3DGS的工程落地和学术研究。

#### 可能的研究机会

1.  **“诊断-编辑”一体化框架**：如果结合 **Vis4GS** 的诊断能力和 **Sculpting NeRF Geometry / Capacity-Controlled Stylization** 的编辑能力，可以构建一个闭环系统：先自动分析场景的几何或风格问题，然后据此自动生成编辑策略（如局部细化、风格迁移），实现3D资产的智能优化。

2.  **面向退化SL

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-06-26T10:46:20-04:00
**Total number of papers:** 58
**Number of papers added in the latest update:** 10
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

#### 2026-06-23 - GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction

**Authors:** Chenrui Fan, Paolo Favaro
**Links:** [abs](https://arxiv.org/abs/2606.24829) - [pdf](https://arxiv.org/pdf/2606.24829)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoT2V-Bench: Benchmarking 3D Consistency in Text-to-Video Models via 3D Reconstruction
- 作者：Chenrui Fan, Paolo Favaro
- 出版日期：2026-06-23
- 分类：Geometry Foundation Models（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要页 https://arxiv.org/abs/2606.24829 | PDF https://arxiv.org/pdf/2606.24829

### 一句话总结
本文提出一个基于3D重建的诊断基准GeoT2V-Bench，用于评估相机提示的文本生成视频模型所生成片段是否具备支持刚性3D重建的几何一致性。

### 研究问题
如何客观、细粒度地评估相机提示的文本生成视频模型输出的3D几何一致性，即生成的帧能否作为同一静态3D场景的多视角证据进行有效重建。

### 核心思路/方法
构建一个重建驱动的诊断管线：先使用VGGT风格几何估计法估算每帧相机内参和姿态，再通过DeformableGS拟合动态场景，并利用时序中值聚合获得静态MedianGS代理。最后沿估计相机路径重渲染该代理。基准不返回单一合格/不合格标签或分数，而是输出一个连续重建画像，涵盖表观图像运动、估计轨迹行为、MedianGS静态渲染误差、静态渲染流一致性以及灵活拟合与静态拟合之间的差距。实验基于12个开源模型配置、80个GeCo-Eval静态场景提示和4种种子，共完成3,840次重建。

### 主要贡献
1. 提出GeoT2V-Bench基准，专门用于诊断相机提示T2V模型在3D一致性方面的缺陷。
2. 提供多维度的连续重建画像指标，能捕获可见运动、静态渲染误差、流一致性和灵活vs静态行为之间可能存在的分歧。
3. 揭示生成视频在被测试为全局静态场景采集时涌现的互补失败模式。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：本文针对3D生成领域的关键评估问题提出系统性诊断方案，方法设计新颖且指标多元，对关注文本生成视频模型几何一致性的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Camera-prompted text-to-video (T2V) models are increasingly used to synthesize virtual camera captures, such as orbiting objects or moving through static scenes. For these outputs, visual plausibility is insufficient: the generated frames should also provide coherent multi-view evidence for a single static 3D scene. We introduce GeoT2V-Bench, a reconstruction-based diagnostic benchmark for evaluating whether camera-prompted T2V clips can support explicit rigid 3D reconstruction. Our pipeline estimates per-frame camera intrinsics and poses with VGGT-style geometry estimation, fits DeformableGS, derives a static MedianGS proxy by temporal-median aggregation, and renders this proxy along the estimated camera path. Instead of producing a pass/fail label or a single scalar score, GeoT2V-Bench reports a continuous reconstruction profile covering apparent image motion, estimated trajectory behavior, MedianGS static rendering error, static-render flow agreement, and the gap between flexible and static fits. On a fair-format four-seed evaluation with 3,840 completed reconstructions from 12 open-weight model configurations and 80 GeCo-Eval static-scene prompts, we find that visible motion, static rendering error, flow agreement, and flexible-vs-static behavior often disagree. GeoT2V-Bench therefore captures complementary failure modes that emerge when generated videos are tested as global static-scene acquisitions.

</details>

#### 2026-06-23 - PointVG-R: Internalizing Geometric Reasoning in MLLMs for Precise Pointing Localization via Visual Chain of Thought

**Authors:** Ling Li, Bowen Liu, Zinuo Zhan, Jianhui Zhong, Ziyu Zhu, Bingcai Wei, Kenglun Chang, Zhidong Deng
**Links:** [abs](https://arxiv.org/abs/2606.24539) - [pdf](https://arxiv.org/pdf/2606.24539)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** geometric reasoning, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointVG-R: Internalizing Geometric Reasoning in MLLMs for Precise Pointing Localization via Visual Chain of Thought
- 作者：Ling Li, Bowen Liu, Zinuo Zhan, Jianhui Zhong, Ziyu Zhu, Bingcai Wei, Kenglun Chang, Zhidong Deng
- 出版日期：2026-06-23
- 分类：Geometry Foundation Models
- 链接：https://arxiv.org/abs/2606.24539

### 一句话总结
该论文提出PointVG-R，一个通过强化学习与视觉思维链（Visual Chain of Thought）在多模态大语言模型（MLLM）中引入几何推理，从而提升指点点定位（pointing-based visual grounding）精度的方法。

### 研究问题
传统方法在点定位任务中，通常将输入图像编码为静态特征表示，主要依赖语言域进行推理，忽视了图像中存在的丰富感知线索和显式空间几何关系，导致模型在解读手势空间关系时存在认知脆弱性。本文旨在解决这一问题，增强MLLM对指向手势的几何推理能力。

### 核心思路/方法
1. **几何推理流程**：设计一个类似人类迭代认知过程的几何推理管道，使模型能够结合图像进行思考。
2. **EgoPoint-CoT数据集**：构建包含详细推理轨迹的高质量视觉思维链（CoT）数据集，用于监督微调（SFT）和强化学习（RL）。
3. **训练策略**：通过强化学习（RL）和冷启动数据集整合几何感知推理；提出基于组方差的自适应重要性加权策略，动态调整训练中的奖励信号，优化学习过程。

### 主要贡献
1. 提出PointVG-R，一种引入几何感知推理的MLLM，专门应对点指定位任务。
2. 构建EgoPoint-CoT数据集，提供带有详细推理轨迹的视觉思维链数据。
3. 提出基于组方差的自适应重要性加权策略，动态调整强化学习中的奖励信号。
4. 实验结果表明，PointVG-R在mIoU指标上超过基线15.86个点，达到当前最佳性能（SOTA）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文提出了一种结合几何推理与视觉思维链的新方法，在点指定位领域取得显著性能提升（mIoU提升15.86点），且涉及强化学习、多模态大模型等前沿技术，具有较强的方法创新性和应用价值。适合对视觉推理、多模态学习或目标定位感兴趣的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Pointing-based visual grounding requires models to precisely locate target objects by deciphering complex spatial relationships between the visual scene and pointing gestures. Traditional methods typically encode input images into static feature representations and perform reasoning primarily within the linguistic domain, often overlooking the rich perceptual cues and explicit spatial geometry inherent in images. In this study, we aim to mitigate the cognitive vulnerability of models in interpreting gestural spatial relations by proposing PointVG-R, a reasoning-guided Multi-modal Large Language Model (MLLM). PointVG-R introduces geometric-aware reasoning for pointing-based grounding, enabling the model to think with images through the strategic integration of Reinforcement Learning (RL) and cold-start data. Specifically, we design a novel geometric reasoning pipeline that simulates the iterative cognitive process humans employ when interpreting pointing gestures. Furthermore, we construct EgoPoint-CoT, a high-quality visual Chain-of-Thought (CoT) dataset featuring detailed reasoning trajectories to guide the model via Supervised Fine-Tuning (SFT) and RL. To address the varying quality of learning signals encountered during training, we further propose an Adaptive Importance Weighting strategy based on Group Variance, which dynamically adjusts reward signals to optimize the learning process. Experimental results demonstrate that PointVG-R achieves SOTA performance, outperforming the baseline by $\textbf{15.86}$ points in mIoU. Extensive ablation studies further validate the efficacy of our proposed modules. Code: https://github.com/lingli1724/PointVG-R.

</details>

#### 2026-06-22 - Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views

**Authors:** Jiho Choi, Seonho Lee, Seojeong Park, Hyunjung Shim
**Links:** [abs](https://arxiv.org/abs/2606.23557) - [pdf](https://arxiv.org/pdf/2606.23557)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views
- 作者：Jiho Choi, Seonho Lee, Seojeong Park, Hyunjung Shim
- 出版日期：2026-06-22
- 分类：Geometry Foundation Models
- 链接：摘要: https://arxiv.org/abs/2606.23557, PDF: https://arxiv.org/pdf/2606.23557

### 一句话总结
本文提出DR-MV3D框架，通过密集且可验证的奖励来监督多视图3D问答中的推理过程，从而改善多模态大模型在跨视图推理和视角选择上的不一致与脆弱性问题。

### 研究问题
多视图3D视觉问答（MV3D-VQA）任务中，当前多模态大模型通常只使用稀疏的、答案级别的监督信号进行训练，这导致了推理过程中跨视图推理不一致和视角选择不稳健。

### 核心思路/方法
- 将MV3D-VQA分解为三个可学习的中间步骤：异中心全局地图构建、基于问题的视图轨迹规划、以及用于答案预测的自中心定位。
- 引入两种密集奖励，使中间步骤无需人工标注即可学习：
  - **全局一致性奖励**：将预测的地图与来自冻结的3D视觉基础模型（如VGGT + SAM3）的几何一致性伪目标进行对齐。
  - **局部轨迹奖励**：监督有序的视角选择。
- 使用轨迹级别的策略优化方法（GRPO）对整个流程进行优化。

### 主要贡献
- 提出了DR-MV3D，一个基于地图的学习框架，利用密集、可验证的奖励来监督MV3D-VQA的推理过程。
- 通过分解任务并引入全局和局部两种密集奖励，使中间推理步骤变得可学习且无需人工标注。
- 在MindCube、VSI-Bench和BLINK (MV)三个基准上的实验表明，DR-MV3D相比强多图像基线方法有持续改进，验证了过程级密集监督对多视图3D推理的有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：本文针对多视图3D推理中的监督稀疏性问题提出了一个创新且可行性高的密集奖励框架，实验覆盖多个基准且有显著提升，对几何基础模型和多模态大模型的结合研究有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-view 3D Visual Question Answering (MV3D-VQA) requires integrating partial observations into a coherent 3D scene representation and selecting informative viewpoints for multi-step spatial reasoning. However, current multimodal LLMs are typically trained with sparse, answer-level supervision, which often yields inconsistent cross-view reasoning and brittle view selection. We present DR-MV3D (Dense Reward for MV3D-VQA), a map-grounded learning framework that provides dense, verifiable rewards to supervise the reasoning process. Our approach decomposes MV3D-VQA into (i) allocentric global map construction, (ii) question-conditioned view-trajectory planning, and (iii) egocentric grounding for answer prediction. To make intermediate steps learnable without manual annotations, we introduce two rewards: a global consistency reward that aligns the predicted map with geometry-consistent pseudo targets from frozen 3D vision foundation models (e.g., VGGT + SAM3), and a local trajectory reward that supervises ordered viewpoint selection. We optimize the full pipeline with trajectory-level policy optimization (GRPO). Experiments on MindCube, VSI-Bench, and BLINK (MV) show that DR-MV3D consistently improves over strong multi-image baselines, supporting the effectiveness of process-level dense supervision for multi-view 3D reasoning.

</details>

#### 2026-06-22 - G-MASt3R-SfM: Graph-based View Pruning and Multi-stage Optimization for Robust SfM

**Authors:** Toshiki Watanabe, Shintaro Ito, Natsuki Takama, Koichi Ito, Takafumi Aoki
**Links:** [abs](https://arxiv.org/abs/2606.22856) - [pdf](https://arxiv.org/pdf/2606.22856)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** MASt3R, image matching, 3D reconstruction, structure from motion, SfM, camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：G-MASt3R-SfM：基于图的视角剪枝与多阶段优化的鲁棒SfM
- 作者：Toshiki Watanabe, Shintaro Ito, Natsuki Takama, Koichi Ito, Takafumi Aoki
- 出版日期：2026-06-22
- 分类：Geometry Foundation Models（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要：https://arxiv.org/abs/2606.22856，PDF：https://arxiv.org/pdf/2606.22856

### 一句话总结
本文提出G-MASt3R-SfM，通过基于图的视角剪枝和多阶段优化两大模块，提升了基于MASt3R匹配的SfM管线在困难条件下的鲁棒性和精度。

### 研究问题
现有基于MASt3R的SfM方法（如MASt3R-SfM）存在一个关键缺陷：MASt3R在进行全景匹配时，会为无重叠的图像对生成错误对应关系，这些不可靠匹配被直接用于优化，导致姿态估计精度显著下降。因此，如何有效抑制非重叠图像对引入的噪声，提升SfM的鲁棒性成为核心问题。

### 核心思路/方法
该论文提出G-MASt3R-SfM管线，包含两个核心模块：
1. **基于图的视角剪枝（GVP）模块**：利用匹配置信度构建场景图，从几何一致性角度剪除离群视角（即产生大量错误匹配的视图）。
2. **多阶段优化（MSO）模块**：通过逐步扩展优化范围——从局部一致性优化到全局一致性优化——渐进式地精细化相机参数，避免早期就引入全局全局错误。

### 主要贡献
- 提出了一种新的SfM管线，能有效处理MASt3R在非重叠图像对上产生的误匹配问题。
- 设计了GVP模块，用图结构来识别和修剪离群视角，提升输入匹配的可靠性。
- 设计了MSO模块，通过局部到全局的渐进式优化策略，稳定地恢复相机参数。
- 在ETH3D数据集上的实验表明，该方法在相机姿态估计和3D重建精度上均达到了当前最优水平。

### 局限性
摘要未提供足够信息。例如未明确讨论在更大规模场景或不同数据集上的泛化能力，也未提及剪枝策略可能丢失有效视角的风险，以及多阶段优化带来的计算开销。

### 阅读优先级
**高**。理由：
1. 该工作直接针对当前基于学习匹配的SfM方法（如MASt3R-SfM）的核心缺陷——非重叠对误匹配——进行了系统性改进，具有明确的实用价值。
2. 提出的GVP和MSO模块思路清晰，实验验证在ETH3D上取得SOTA，适合对此方向感兴趣的研究者快速了解当前前沿进展。
3. 文章发表于2026年，且出自日本团队，属于较新成果，对从事三维重建、视觉定位的研究者有较强参考意义。

</details>

<details>
<summary>Abstract</summary>

Structure from Motion (SfM) is essential for multi-view 3D reconstruction, however, its accuracy heavily relies on the accuracy of image matching. While the recent correspondence matching method, MASt3R, enables robust matching even under challenging conditions, it tends to generate incorrect correspondences for non-overlapping image pairs. Consequently, existing SfM methods using MASt3R, such as MASt3R-SfM, suffer from significant degradation in pose estimation accuracy as they incorporate these unreliable matches directly into optimization. To address this issue, we propose G-MASt3R-SfM, a novel SfM pipeline that enhances robustness through two key modules. First, the Graph-based View Pruning (GVP) module constructs a scene graph from matching confidence and geometrically prunes outlier views. Second, the Multi-Stage Optimization (MSO) module progressively refines camera parameters by expanding the optimization scope from local consistency to the global consistency. Experiments on the ETH3D dataset demonstrate that our method achieves state-of-the-art accuracy in both camera pose estimation and 3D reconstruction, effectively suppressing noise caused by outliers.

</details>

## Dynamic / 4D Reconstruction

### 2026-06

#### 2026-06-25 - Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds

**Authors:** Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang, Hailan Ma, Huadong Mo, Zhenhong Sun
**Links:** [abs](https://arxiv.org/abs/2606.26964) - [pdf](https://arxiv.org/pdf/2606.26964)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 3D, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Look-Before-Move: Narrative-Grounded World Visual Attention in Dynamic 3D Story Worlds
- 作者：Jiaming Bian, Bingliang Li, Yuehao Wu, Pichao Wang, Zhi Wang, Hailan Ma, Huadong Mo, Zhenhong Sun
- 出版日期：2026-06-25
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.26964

### 一句话总结
本文提出一个名为 Look-Before-Move 的相机规划框架，该框架通过先构建语义观察契约、进行蒙特卡洛视点搜索，再执行语义轨迹接地，使动态3D故事世界中的智能体能够根据叙事意图主动决定观察内容，而非被动生成运动。

### 研究问题
在动态3D故事世界中，相机如何从被动生成平滑运动转向主动选择观察目标（即根据叙事意图和物理约束决定“看什么”、“如何构图”以及“如何转移注意力”）？

### 核心思路/方法
该方法将相机规划拆分为“观察指定”和“运动执行”两个阶段。具体包含三个步骤：
1. **语义观察契约**：将导演意图（叙事目标）转化为可执行的视觉约束条件。
2. **蒙特卡洛视点搜索**：在满足叙事要求和几何可行性的前提下，搜索符合约束的视点。
3. **语义轨迹接地**：将选定视点连接成连续、无碰撞且时间一致的相机运动轨迹。

### 主要贡献
1. 提出“叙事接地世界视觉注意力”概念，将相机视为在动态3D故事世界中根据叙事意图和物理约束决定观察的具身观察者。
2. 设计 Look-Before-Move 框架，创新性地分离观察指定与运动执行，生成叙事一致且几何可行的相机轨迹。
3. 基于 StoryBlender 构建动态3D故事世界基准，包含50个故事、457个场景、1585个镜头，支持动画角色、语义配置和可执行3D环境。
4. 实验表明，该框架在主体感知、意图一致性和轨迹质量上优于代表性基线方法，验证了在生成相机运动前组织视觉注意力的重要性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中

理由：该工作专注于具身AI在动态3D环境中的视觉注意力与相机规划问题，属于较具体的交叉方向。若研究兴趣在于叙事驱动的智能体感知或动态场景中的运动规划，则本文有较高参考价值；若领域不涉及3D故事世界或具身视觉，则阅读优先级降低。

</details>

<details>
<summary>Abstract</summary>

As embodied AI and world models increasingly operate in dynamic 3D environments, visual perception must move beyond passively interpreting given observations toward actively deciding what to observe. We study this problem through camera planning in dynamic 3D story worlds, where the camera must not only generate smooth motion, but also decide what visual evidence should be acquired before it moves. We formulate this capability as Narrative-Grounded World Visual Attention, where the camera acts as an embodied observer that determines what to observe, how to compose the observation, and how to shift attention over time under narrative intent and physical 3D constraints. To realize this capability, we propose Look-Before-Move, a camera planning framework that separates observation specification from motion execution. It first builds a Semantic Observation Contract to convert directorial intent into executable visual constraints, then performs Monte Carlo Viewpoint Search to find narrative-compliant and geometrically feasible viewpoints, and finally applies Semantic Trajectory Grounding to connect selected viewpoints into continuous, collision-aware, and temporally coherent camera motion. We further construct a dynamic 3D Story World Benchmark based on StoryBlender, covering 50 stories, 457 scenes, and 1585 shots with animated characters, semantic scene configurations, and executable 3D environments. Experiments show that our framework improves subject perception, intent consistency, and trajectory quality over representative baselines, demonstrating the importance of organizing visual attention before generating camera motion.

</details>

#### 2026-06-22 - Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild

**Authors:** Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani
**Links:** [abs](https://arxiv.org/abs/2606.23688) - [pdf](https://arxiv.org/pdf/2606.23688)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lift4D: Harmonizing Single-View 3D Estimation for 4D Reconstruction In-the-Wild  
- 作者：Yehonathan Litman, Xiaoxuan Ma, Manan Shah, Nicolas Ugrinovic, Kris Kitani, Fernando De la Torre, Shubham Tulsiani  
- 出版日期：2026-06-22T17:59:54Z  
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering  
- 链接：摘要：https://arxiv.org/abs/2606.23688，PDF：https://arxiv.org/pdf/2606.23688  

### 一句话总结  
Lift4D 提出了一种测试时优化框架，通过因果潜在条件生成时间一致的单帧3D重建作为初始化，并结合遮挡感知优化和扩散先验，从单目视频中高质量重建动态非刚体4D场景，尤其适用于野外复杂场景。

### 研究问题  
如何从单目野外视频中重建动态非刚体对象的4D表示，克服现有方法在缺乏4D训练数据、依赖初始先验后仅靠视频监督、以及处理大形变和严重遮挡时的局限性。

### 核心思路/方法  
1. **时间一致的3D初始化**：采用现有单视图3D重建模型，通过因果潜在条件（causal latent conditioning）使其生成时间上连续的逐帧预测，为可变形3D高斯泼溅表示提供一致性初始化。  
2. **遮挡感知优化与雕塑**：通过遮挡感知优化，使该表示与输入视频对齐，忠实恢复可见表面细节；同时利用视图条件扩散先验补全未观察区域，完成对表示的精炼（“雕塑”）。  
3. **测试时优化**：整个框架在测试时自适应优化，无需额外的4D训练数据。

### 主要贡献  
- 提出一种结合单视图3D估计与测试时优化的框架，解决4D重建中数据稀缺和野外复杂场景的挑战。  
- 通过因果潜在条件实现时间一致的逐帧3D预测，初始化可变形表示。  
- 引入遮挡感知优化与扩散先验，在恢复可见细节的同时合理补全遮挡区域。  
- 在存在严重遮挡和非刚体运动的野外序列上，显著优于先前4D重建方法。

### 局限性  
摘要未提供足够信息，如对计算效率、具体失败案例、泛化到不同动态类型（如拓扑变化）或对输入视频质量的要求等未提及。

### 阅读优先级  
高。理由：该工作针对单目4D重建中的核心难点（大形变、严重遮挡、数据稀缺）提出了新的框架，并在野外场景上取得显著改进，对动态重建领域具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic non-rigid objects from monocular video requires integrating visual cues from direct observations with data-driven priors over geometry and appearance. Prior approaches either learn to directly predict 4D representations from visual input or initialize a 3D representation that is subsequently deformed and refined based on video evidence. However, the former are constrained by the scarcity of 4D training data, while the latter leverage priors only for the initial reconstruction and rely solely on video supervision thereafter; neither handles complex in-the-wild scenarios with large deformations and occlusions well. We present Lift4D, a test-time optimization framework that addresses both limitations. First, we adapt an existing single-view 3D reconstruction model to yield temporally consistent per-frame predictions via causal latent conditioning, providing a coherent initialization for a deformable 3D Gaussian Splatting representation. We then ``sculpt'' this representation to match the input video through an occlusion-aware optimization that faithfully recovers visible surface details while completing unobserved regions using a view-conditioned diffusion prior. We demonstrate that Lift4D clearly improves over prior 4D reconstruction methods, particularly on challenging in-the-wild sequences with severe occlusions and non-rigid motion.

</details>

#### 2026-06-22 - MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing

**Authors:** Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
**Links:** [abs](https://arxiv.org/abs/2606.23455) - [pdf](https://arxiv.org/pdf/2606.23455)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MeGAS: Thermomechanical Dynamic Gaussian Splatting for Thermophysical Scene Editing
- 作者：Zesong Yang, Yuanhang Lei, Liyuan Cui, Yihang Chen, Jiaer Huang, Boming Zhao, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- 出版日期：2026-06-22T15:05:59Z
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：摘要: https://arxiv.org/abs/2606.23455；PDF: https://arxiv.org/pdf/2606.23455

### 一句话总结
MeGAS是一个将热力学相变动力学融入3D高斯溅射的框架，实现了对热物理现象（如熔化、凝固）的物理一致且逼真的场景编辑与渲染。

### 研究问题
如何将温度这一隐形物理因素融入神经渲染框架，以合成和编辑涉及热力学相变的物理现象，弥合真实感场景重建与基于物理的动画之间的差距。

### 核心思路/方法
1. **热力学动态高斯表示**：在3D高斯溅射（3DGS）基础上增加温度属性，构建新的表示。
2. **物理求解器**：采用热对流-扩散求解器，并耦合物质点法（MPM）动力学与相变模型，驱动高斯的演化。
3. **拓扑自适应渲染策略**：针对极端变形导致的裂缝和漂浮物问题，提出新的高斯渲染策略以保持拓扑一致性。

### 主要贡献
1. 首次将热力学相变动力学与3D高斯溅射结合，提出MeGAS框架。
2. 设计了带温度属性的热力学动态高斯表示及对应的物理求解器。
3. 提出拓扑自适应高斯渲染策略，提升极端变形下的渲染质量。
4. 实验证明MeGAS在保持物理一致性的同时，能生成高保真度真实感渲染。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作创新性地将温度这一关键物理因素引入3D高斯溅射，弥补了现有物理驱动神经渲染方法仅关注机械动力学的不足。对于从事动态场景重建、物理仿真与神经渲染交叉领域的研究人员具有较高参考价值，且应用场景（如热物理现象编辑）具有独特吸引力。

</details>

<details>
<summary>Abstract</summary>

Recent advances integrate physically grounded Newtonian dynamics with neural rendering frameworks, narrowing the gap between photorealistic scene reconstruction and physics-based animation. However, existing approaches focus on mechanically driven dynamics while neglecting temperature, a fundamental yet invisible physical factor underlying phenomena such as melting, solidification, and other thermomechanical processes. In this paper, we propose MeGAS, a novel framework that incorporates thermomechanical phase-change dynamics into 3D Gaussian Splatting (3DGS). Specifically, we propose a new thermomechanical dynamic Gaussian Splatting representation that augments 3DGS with temperature attributes and employs a heat advection-diffusion solver with MPM dynamics incorporating phase transitions, enabling physically plausible and visually realistic synthesis of thermophysical phenomena. Furthermore, a new topology-adaptive Gaussian rendering strategy is proposed to mitigate cracking and floaters under extreme deformation. Extensive experiments demonstrate that MeGAS produces physically consistent thermomechanical behavior while maintaining high-fidelity photorealistic rendering, advancing toward physics-integrated world models.

</details>

#### 2026-06-22 - Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion

**Authors:** Yuqiang Huang, Yuxi Wang, Junyu Dong, Zhaoxiang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.23298) - [pdf](https://arxiv.org/pdf/2606.23298)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Ocean4D: Generative Underwater 4D Reconstruction via Medium-Aware Video Diffusion
- 作者：Yuqiang Huang, Yuxi Wang, Junyu Dong, Zhaoxiang Zhang
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.23298

### 一句话总结
该论文提出名为Ocean4D的生成式框架，通过结合4D几何一致性条件生成与介质感知去噪扩散，实现从单目视频到水下动态场景的4D重建。

### 研究问题
现有水下4D重建方法多基于空气环境假设，未显式建模水下介质对光的吸收和散射，且近静态假设对动态干扰（如漂移粒子）敏感，导致几何不稳定和跨视角不一致。本研究旨在解决这些耦合挑战。

### 核心思路/方法
- **4D-GCC**：构建4D几何一致性的条件模块，改进跨帧覆盖范围，为目标轨迹生成提供全局结构约束。
- **Medium-Aware Block**：在潜在扩散过程中执行隐式介质感知去噪，专门稳定水下吸收和散射造成的外观退化。
- 输入单目视频和目标相机轨迹，生成沿目标路径的一致视频，同时保留全局结构和跨视角一致性。

### 主要贡献
1. 提出首个专门面向水下环境的生成式4D重建框架Ocean4D。
2. 设计4D几何一致性条件（4D-GCC）和介质感知去噪模块，解决水下光线退化与动态变化的耦合问题。
3. 在动态和静态水下基准上达到最先进性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文针对水下4D重建这一特殊且困难的任务，提出了完整的生成式框架，并在公开基准上取得领先结果，对相关领域（水下视觉、动态场景重建）有明确参考价值。

</details>

<details>
<summary>Abstract</summary>

Underwater 4D reconstruction remains challenging due to the coupling between degraded light transport in participating media and dynamic water variations. Most existing Methods are developed under in-air assumptions and do not explicitly account for underwater absorption and backscatter. Additionally, near-static assumptions make these approaches sensitive to drifting particles and dynamic distractors , leading to unstable geometry and inconsistent cross-view results. To address these issues, we propose a generative framework for underwater 4D reconstruction, named Ocean4D, which is built on two complementary components. Specifically, 4D-GCC constructs 4D geometrically consistent conditioning with improved cross-frame coverage, while the Medium-Aware Block performs implicit medium-aware denoising in the latent diffusion process to stabilize underwater appearance under absorption and scattering. Given a monocular video and target cameras, our method generates videos along the target trajectories while preserving global structure and cross-view consistency. Extensive experiments on both dynamic and static underwater benchmarks demonstrate state-of-the-art performance on underwater reconstruction.

</details>

#### 2026-06-22 - Temporally Aware Densification for Dynamic 3D Gaussian Splatting

**Authors:** Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan
**Links:** [abs](https://arxiv.org/abs/2606.23212) - [pdf](https://arxiv.org/pdf/2606.23212)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic 3D, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Temporally Aware Densification for Dynamic 3D Gaussian Splatting
- 作者：Vikram Sandu, Mayurdeep Pathak, Rajiv Soundararajan
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.23212

### 一句话总结
本文提出一个时间感知的密集化框架，通过结合时间可见性、自适应阈值和变形偏移策略，改善动态3D高斯泼溅中动态区域的重建质量。

### 研究问题
现有动态3D高斯泼溅方法沿用静态场景的密集化策略，忽视了时间连续性，导致动态区域因高斯短暂存在、监督稀疏而出现重建不充分和模糊问题。

### 核心思路/方法
1. **Visibility-Aware Densification (VAD)**：将时间可见性集成到密集化过程中，使高斯单元根据其实际时间存在情况被精细化。
2. **Temporally-Adaptive Thresholding (TAT)**：根据每个高斯单元的时间寿命动态调整密集化阈值，促进静态和动态区域的平衡优化。
3. **Temporal Offset Warping (TOW)**：围绕时间中心增强变形能力，延长高度动态高斯单元的寿命，促进更有效的密集化。

### 主要贡献
- 揭示了动态3D高斯泼溅中静态密集化策略的缺陷，并指出其对动态区域重建的负面影响。
- 提出VAD框架作为即插即用模块，可泛化应用于多种动态3D高斯泼溅方法。
- 在三个动态多视角基准数据集上，动态区域的视觉质量显著优于现有方法。

### 局限性
摘要未提供足够信息：未提及计算开销、训练/推理速度变化、对极端动态场景的鲁棒性，或现有基准数据集之外的泛化能力限制。

### 阅读优先级
**高**。理由：该工作直击动态场景重建中一个被忽视的关键问题（密集化策略与时间不兼容），提出的方法具有即插即用性，且实验在多个基准上取得显著改进，对从事动态/4D重建的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Despite modeling temporal motion, dynamic 3D Gaussian Splatting (3DGS) methods still inherit a static densification strategy that is ill-suited for dynamic scenes. This neglect of temporal behavior leads to under-reconstructed and blurry dynamic regions, as short-lived Gaussians receive sparse supervision and fail to densify effectively. We propose a Visibility-Aware Densification (VAD) framework that integrates temporal visibility into the densification process, ensuring that Gaussians are refined based on their actual temporal presence. A Temporally-Adaptive Thresholding (TAT) mechanism further adjusts each Gaussian's densification threshold according to its temporal lifespan, promoting balanced refinement of both static and dynamic regions. Finally, a Temporal Offset Warping (TOW) design enhances deformation capacity around temporal centers, extending the lifespan of highly dynamic Gaussians and facilitating more effective densification. Our approach achieves substantial improvements in the visual quality of dynamic regions, outperforming existing methods across three dynamic multi-view benchmark datasets. Moreover, the proposed VAD module generalizes across diverse dynamic 3DGS methods, consistently improving dynamic reconstruction as a plug-and-play component.

</details>

#### 2026-06-22 - MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations

**Authors:** Yuhua Luo, Junsheng Zhang, Mengyin Liu, Xincheng Lin, Ming Yan, Zhudi Chen, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang
**Links:** [abs](https://arxiv.org/abs/2606.23000) - [pdf](https://arxiv.org/pdf/2606.23000)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations
- 作者：Yuhua Luo, Junsheng Zhang, Mengyin Liu, Xincheng Lin, Ming Yan, Zhudi Chen, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang
- 出版日期：2026-06-22
- 分类：Dynamic / 4D Reconstruction
- 链接：https://arxiv.org/abs/2606.23000

### 一句话总结
本文提出MotionMAR，一种基于多尺度自回归的粗到细框架，从稀疏观测中重建人体运动，并通过在AMASS数据集上的实验取得了最先进精度。

### 研究问题
如何从稀疏观测（sparse observations）中准确、结构一致地重建完整的人体运动序列，特别是处理运动中的时间层次结构（从低频全局轨迹到高频细节）。

### 核心思路/方法
采用粗到细的渐进式重建框架，包含四个集成组件：
1. **Temporal Multi-scale Tokenization (TMT) VQ-VAE**：对运动数据进行多时间尺度编码，将语义运动与微小抖动分离。
2. **Motion Autoregressive Network (MAN)**：在潜在空间中跨尺度运行，先通过粗索引建立全局结构，再生成细索引恢复具体细节。
3. **Scale-Aware Control (SAC)**：集成稀疏跟踪数据，确保生成输出与实际观测对齐。
4. **Motion Refinement Network (MRN)**：对连续姿态进行平滑并消除量化伪影。

### 主要贡献
- 提出一种结构感知的、粗到细的多尺度自回归框架，用于从稀疏观测中重建人体运动。
- 设计了TMT VQ-VAE、MAN、SAC和MRN四个协同组件，分别处理多尺度编码、自回归预测、观测对齐和细节平滑。
- 在AMASS数据集上取得了当前最先进的运动重建精度。
- 开源了代码（http://www.lidarhumanmotion.net/motionmar/）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文提出了一种新颖的粗到细多尺度自回归框架，解决从稀疏观测重建人体运动的实际问题，并在标准数据集AMASS上实现了最先进结果。对于从事人体运动捕捉、4D重建或时间序列预测的研究者具有直接参考价值，且代码已开源，可复现性强。

</details>

<details>
<summary>Abstract</summary>

Human motion follows a temporal hierarchical structure, transitioning from low-frequency global trajectories to high-frequency details. Inspired by the success of multi-level autoregressive models in computer vision, we propose MotionMAR, a coarse-to-fine framework for motion reconstruction from sparse observations. It first estimates the global trajectory of human motion and then gradually refines the temporal details. This architecture consists of four integrated components. The Temporal Multi-scale Tokenization (TMT) VQ-VAE encodes the data at multiple temporal resolutions, separating semantic motion from minor jitters. The Motion Autoregressive Network (MAN) operates in this latent space, predicting motion across scales. It first establishes the global structure through coarse indices and then generates finer indices to recover specific details. Meanwhile, the Scale-Aware Control (SAC) module integrates sparse tracking data to ensure the generated output aligns with actual observations. The Motion Refinement Network (MRN) subsequently smooths consecutive poses and eliminates quantization artifacts. Experiments show that MotionMAR achieves state-of-the-art accuracy on the AMASS dataset, providing a reliable and structure-aware approach for motion reconstruction. The source code is publicly available at http://www.lidarhumanmotion.net/motionmar/.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-06

#### 2026-06-25 - PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views

**Authors:** Zhisong Xu, Takeshi Oishi
**Links:** [abs](https://arxiv.org/abs/2606.27071) - [pdf](https://arxiv.org/pdf/2606.27071)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, SfM, SLAM, 3DGS, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PanoImager: Geometry-Guided Novel View Synthesis and Reconstruction from Sparse Panoramic Views
- 作者：Zhisong Xu, Takeshi Oishi
- 出版日期：2026-06-25
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering（副分类）
- 链接：摘要页（https://arxiv.org/abs/2606.27071），PDF（https://arxiv.org/pdf/2606.27071）

### 一句话总结
PanoImager 是一个无需 SfM 的框架，结合前馈深度/姿态先验、几何条件扩散视图补全和深度引导的 3DGS 优化，从稀疏全景图像中实现稳定的新视图合成与三维重建。

### 研究问题
如何在旋转主导、弱视差运动的极端稀疏全景视图输入下，实现稳定可靠的三维重建和新视图合成，克服传统 SfM/SLAM 初始化不稳定的问题。

### 核心思路/方法
1. **SfM-free 设计**：摒弃 SfM 流程，直接利用前馈任务提供姿态和深度先验。
2. **视图分解与补全**：将稀疏全景图分解为局部透视视图，通过几何条件扩散模型合成辅助视图，以丰富稀疏证据。
3. **深度引导的 3DGS 优化**：利用深度信息稳定高斯渲染优化，提升跨视图一致性。

### 主要贡献
- 提出 PanoImager 框架，在极端稀疏全景视角下实现更优的重建和合成稳定性，可作为 SfM/SLAM 初始化失败时的离线/背景组件，用于地图优化。
- 在多个基准测试中，展现了在极稀疏输入下的鲁棒性提升。

### 局限性
摘要未提供足够信息，无法详细说明具体局限性。

### 阅读优先级
**高**。
理由：该工作针对传统 SfM/SLAM 在稀疏全景场景下的核心痛点（初始化和弱视差）提出了创新的无 SfM 解决方案，结合了深度先验、扩散模型和 3DGS 优化，对实时建图、自主导航和 VR/AR 等领域具有潜在应用价值。

</details>

<details>
<summary>Abstract</summary>

Panoramic sensing offers wide field-of-view coverage, yet 3D reconstruction from sparse panoramas remains challenging under rotation-dominant, weak-parallax motion. In such regimes, SfM/SLAM initialization is often ill-conditioned and unreliable. We present PanoImager, an SfM-free framework that combines feed-forward pose/depth priors, geometry-conditioned diffusion view completion, and depth-guided 3DGS optimization. Given only a few panoramic images, PanoImager decomposes them into local perspective views, synthesizes auxiliary observations to enrich sparse evidence, and stabilizes Gaussian optimization for improved cross-view consistency. Experiments on multiple benchmarks show improved stability under extreme sparsity, suggesting PanoImager as an offline/background component for map refinement when SfM/SLAM fails to initialize.

</details>

#### 2026-06-25 - Rolling Shutter Relative Pose Estimation Made Practical

**Authors:** Daniel Barath
**Links:** [abs](https://arxiv.org/abs/2606.26863) - [pdf](https://arxiv.org/pdf/2606.26863)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rolling Shutter Relative Pose Estimation Made Practical
- 作者：Daniel Barath
- 出版日期：2026-06-25T10:47:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.26863

### 一句话总结
本文通过引入仿射对应（ACs）并推导滚动快门校正的仿射约束，将滚动快门相对位姿估计所需匹配点数从20对降至7对，从而使其在RANSAC框架中变得实用。

### 研究问题
如何在不牺牲精度和效率的前提下，减少滚动快门相机相对位姿估计所需的最小匹配点数，从而使其在RANSAC等鲁棒估计中实际可用。

### 核心思路/方法
1. **引入仿射对应（ACs）**：将仿射对应融入滚动快门双视图几何，推导出“RS校正的仿射约束”，每个仿射对应在标准极线约束之外额外提供两个方程。
2. **线性化代数求解器**：利用RS参数物理上的小量，线性化约束；通过零空间投影消除12个RS未知数；使用作用矩阵求解剩余20阶系统，整个求解耗时1.2毫秒。
3. **仅需7个仿射对应**即可同时估计位姿和RS运动参数。

### 主要贡献
- 提出RS校正的仿射约束，将最小匹配点数从20降至7。
- 实现一个高速（1.2毫秒）的线性化代数求解器。
- 在TUM RS基准上，位姿和RS参数精度均优于所有测试方法，且能准确估计平移速度（该量从点对应中因v-t耦合而难以恢复）。
- 在全局快门数据集EuRoC MAV上，精度与标准5点算法相当，表明其泛化能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作解决了滚动快门相对位姿估计长期存在的实用性瓶颈（点数过多），提出了创新性的仿射约束和高效求解器，并在多个基准上验证了精度和泛化能力，对计算机视觉几何建图领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Rolling shutter (RS) cameras equip virtually all consumer devices, yet RS-aware relative pose estimation has remained impractical: the state-of-the-art solver requires a minimum of 20 point correspondences, making RANSAC-based robust estimation prohibitively expensive due to the exponential dependence of the iteration count on the sample size. We make RS relative pose estimation practical by introducing affine correspondences (ACs) into the RS two-view geometry. We derive novel \emph{RS-corrected affine constraints} that account for the coupling between point perturbations and the row-dependent essential matrix, providing two equations per correspondence beyond the standard epipolar constraint. Building on these constraints, we develop a linearized algebraic solver that estimates pose and RS motion from only 7 ACs. The solver exploits the physical smallness of RS parameters to linearize the constraints, eliminates the 12 RS unknowns via null-space projection, and solves the remaining degree-20 system via action matrices in 1.2\,ms. On the TUM RS benchmark, our method achieves the best pose and RS parameter accuracy among all tested methods and, uniquely among RS solvers, provides accurate translational velocity estimates -- which are poorly conditioned from point correspondences alone due to a $\vec{v}$-$\vec{t}$ coupling. On the global-shutter EuRoC MAV dataset, the solver achieves comparable accuracy to the standard 5-point algorithm, demonstrating that it generalizes well to the GS setting. Code is at https://github.com/danini/rolling_shutter_made_practical.

</details>

#### 2026-06-24 - PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling

**Authors:** Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
**Links:** [abs](https://arxiv.org/abs/2606.25430) - [pdf](https://arxiv.org/pdf/2606.25430)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRISM: Feed-Forward Single-Image 3D Reconstruction via Geometric Warp-Residual Modeling
- 作者：Zhijie Zheng, Xinhao Xiang, Jiawei Zhang
- 出版日期：2026-06-24
- 分类：主类别：3D Reconstruction & Multi-view Geometry；次类别：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25430

### 一句话总结
本文提出PRISM，一种无需扩散采样、仅通过前馈几何扭曲和残差校正的单图三维重建框架，在保持与扩散方法相当的重建质量的同时大幅降低推理时间。

### 研究问题
如何从单张图像高效且高质量地重建三维场景，克服现有基于扩散模型的方法因迭代采样而推理慢的部署难题。

### 核心思路/方法
1. 观察到几何前向扭曲（geometric forward warping）即可覆盖目标视图的大部分内容，仅留下少量残差需要校正。
2. 提出PRISM：将多视角潜在（latent）预测分解为**参数无关的几何先验**与**学习的残差校正**，推理时无需扩散采样。
3. 设计两阶段训练策略：先通过潜在监督蒸馏（latent supervised distillation）学习几何泛化，再通过感知微调（perceptual fine-tuning）优化外观质量。

### 主要贡献
1. 提出纯前馈框架PRISM，实现从单图到多视图的快速三维重建，无需迭代扩散采样。
2. 利用几何扭曲-残差建模分解任务，使大部分视图内容直接由几何变换完成，降低编码器负担。
3. 设计两阶段训练策略，使模型能够在纯合成数据上泛化，并兼顾几何准确度与外观保真度。
4. 在三个基准上达到与扩散方法可比的性能，同时将每个场景的推理时间大幅降至36秒。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对三维重建中扩散模型推理慢的显著痛点，提出了一种高效的纯前馈替代方案，并在多个基准上验证了速度-质量的权衡优势。秒级推理时间（36秒/场景）对机器人、VR等实时或近实时应用具有重要意义，且两阶段训练策略对合成数据泛化有启发价值。

</details>

<details>
<summary>Abstract</summary>

Reconstructing 3D scenes from a single image is a fundamental challenge in computer vision, with broad applications in virtual reality, robotics, and content creation. Recent methods achieve outstanding performance by leveraging camera-controlled video diffusion models, but rely on iterative diffusion sampling, which greatly limits their practical deployment. We observe that geometric forward warping alone can cover the majority of a target view directly from the input image, with only a compact residual left for the encoder to correct. Motivated by this observation, we propose PRISM, a feed-forward framework that decomposes multi-view latent prediction into a parameter-free geometric prior and a learned residual correction, with no diffusion sampling required at inference. To enable generalization from purely synthetic training data, we devise a two-stage training strategy combining latents supervised distillation for geometric generalization and perceptual fine-tuning for appearance quality optimization. Extensive experiments on three benchmarks demonstrate that PRISM achieves competitive reconstruction quality compared with diffusion-based methods, while reducing inference time dramatically to only 36 seconds per scene.

</details>

#### 2026-06-23 - Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems

**Authors:** Sven Goffin, Cédric Schwartz, Silvère Bonnabel, Olivier Brüls, Pierre Sacré
**Links:** [abs](https://arxiv.org/abs/2606.25083) - [pdf](https://arxiv.org/pdf/2606.25083)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems  
- 作者：Sven Goffin, Cédric Schwartz, Silvère Bonnabel, Olivier Brüls, Pierre Sacré  
- 出版日期：2026-06-23  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2606.25083  

### 一句话总结
本文提出一种基于不变卡尔曼滤波（IEKF）的迭代方法，用于多IMU铰接刚体系统的扩展位姿估计（方向、速度、位置），通过引入相对L-扩展位姿的Lie群表示，将关节运动学约束以不变形式融入滤波，显著提升估计精度与收敛性。

### 研究问题
如何为多IMU构成的铰接刚体系统（如机器人和人体）实现具有收敛保证和一致性的扩展位姿估计，同时处理跨刚体的位姿耦合与关节约束问题。

### 核心思路/方法
1. 定义**相对L-扩展位姿**（relative L-extended pose）作为运动链系统的Lie群表示，使系统动态具有群仿射性质。  
2. 将关节运动学约束建模为**无噪声伪测量**，并嵌入迭代不变扩展卡尔曼滤波（IterIEKF）框架中，从而保留不变滤波的收敛性和一致性保证。  
3. 在UR5e机器人和人体腿部数据集上验证，与标准EKF、迭代EKF及绝对位姿IterIEKF进行对比。

### 主要贡献
- 首次将不变卡尔曼滤波的收敛与一致性保证扩展至多IMU铰接系统；  
- 提出一种将关节约束以不变形式显式融入滤波的有效方案；  
- 实验显示，提出方法在所有场景中均取得最低RMSE，相比次优滤波器至少降低50%，且收敛更快、运行间变异性更低。

### 局限性
摘要未提供具体局限性信息（如传感器噪声假设、计算复杂度、对非线性约束的适应性等）。

### 阅读优先级
**高**  
理由：该方法针对机器人运动跟踪与人体动作分析中的核心问题，提出理论严谨且实验效果显著的创新方案（RMSE降低50%以上），对从事滤波、位姿估计与惯性导航的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Accurate extended pose estimation (orientation, velocity, and position) for IMU-instrumented articulated rigid-body systems is a key challenge in robotics and human motion analysis. The invariant extended Kalman filter (IEKF) addresses this problem for a single rigid body with convergence guarantees and consistency under unobservability, but extending these properties to articulated systems is nontrivial: inter-body pose coupling prevents a direct application, and incorporating joint kinematic constraints within the invariant framework remains an open problem. To address this gap, we introduce the relative L-extended pose, a Lie group representation for kinematic-tree systems. With one IMU per body, it yields group-affine dynamics and allows joint constraints to be expressed in invariant form. We incorporate these constraints as noise-free pseudo-measurements within an iterated IEKF (IterIEKF), thereby preserving the convergence and consistency guarantees of invariant filtering. Validated on both a UR5e robot and a human leg, the proposed IterIEKF outperforms all EKF, IterEKF, and absolute-pose IterIEKF baselines. It converges faster, exhibits lower run-to-run variability, and consistently achieves the lowest RMSE, with reductions of at least 50% compared to the second-best filter across all scenarios considered in this work.

</details>

#### 2026-06-23 - Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM

**Authors:** Leshu Li, Jie Peng, Yang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.24796) - [pdf](https://arxiv.org/pdf/2606.24796)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** simultaneous localization and mapping, SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, autonomous driving, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Pocket-SLAM: Rendering-Area-Aware Pruning for Memory-Efficient 3DGS-SLAM
- 作者：Leshu Li, Jie Peng, Yang Zhao
- 出版日期：2026-06-23T16:48:58Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24796

### 一句话总结
该论文提出了一种面向渲染区域的剪枝策略，在不牺牲定位与建图精度的前提下，显著降低3DGS-SLAM在自动驾驶等大规模场景中的内存消耗并提升帧率。

### 研究问题
3DGS-SLAM在大尺度场景（如自动驾驶）中运行时，高斯点随建图过程持续累积，导致内存消耗不断增长，从而限制了其在大规模场景下的应用。

### 核心思路/方法
提出一种“渲染区域感知剪枝”策略：根据高斯点对有效渲染区域的贡献程度（而非仅依赖不透明度或梯度幅值等单点启发式指标）来选择性移除冗余高斯点，从而直接针对内存冗余的来源进行剪枝。

### 主要贡献
- 提出了一种渲染区域感知的剪枝方法，从渲染区域贡献角度解决3DGS-SLAM的内存冗余问题。
- 在EuRoC和KITTI数据集上的实验证明，该方法在大型室外场景中一致优于现有剪枝方法。
- 实现了超过60%的内存降低和2倍以上的FPS提升，同时保持定位与建图精度。
- 项目代码已开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作针对3DGS-SLAM在大尺度场景中的内存瓶颈问题提出了有效解决方案，实验指标（60%+内存减少、2倍FPS提升）显著，且代码已公开，对自动驾驶等实时应用场景具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has garnered significant attention in Simultaneous Localization and Mapping (SLAM) due to its advances in capturing fine-grained geometry features and synthesizing novel views. For SLAM in large-scale scenes, such as autonomous driving, 3DGS-SLAM faces a critical limitation: memory consumption increases continuously over time as Gaussian points accumulate, leading to poor memory efficiency and limiting its applicability. In this work, we propose a rendering-area-aware pruning strategy that selectively removes Gaussians based on their contribution to the effective rendering area, rather than solely relying on Gaussian-level heuristics such as opacity or gradient magnitude. This perspective directly targets the sources of memory redundancy, effectively reducing the peak memory footprint of 3DGS-SLAM during runtime. Evaluations on the EuRoC and KITTI datasets demonstrate that our method consistently outperforms existing pruning approaches in large-scale outdoor scenes, achieving over 60% memory reduction and more than 2 times FPS improvement while preserving localization and mapping accuracy. These results highlight rendering-area-aware pruning as a promising direction for scaling 3DGS-SLAM to real-world autonomous driving scenarios. Our code is publicly available at https://github.com/UMN-ZhaoLab/Pocket-SLAM.git.

</details>

#### 2026-06-23 - Decentralized Pose Graph Riemannian Optimization for Object-based Multi-Robot SLAM

**Authors:** Yixian Zhao, Yan Huang, Yang Xu, Liang Li, Jinming Xu
**Links:** [abs](https://arxiv.org/abs/2606.24489) - [pdf](https://arxiv.org/pdf/2606.24489)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Decentralized Pose Graph Riemannian Optimization for Object-based Multi-Robot SLAM
- 作者：Yixian Zhao, Yan Huang, Yang Xu, Liang Li, Jinming Xu
- 出版日期：2026-06-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2606.24489 | 论文PDF https://arxiv.org/pdf/2606.24489

### 一句话总结
本文提出一种完全去中心化的黎曼优化框架，通过共识机制解耦位姿图优化问题，并在SE(d)流形上利用近似二阶信息提升收敛效率，适用于基于物体的多机器人SLAM。

### 研究问题
在基于物体的多机器人SLAM中，现有分散式位姿图优化方法通常假设通信拓扑与物理交互拓扑高度一致，这限制了其在稀疏、间歇或时变通信场景下的应用。因此，如何设计一种能够在灵活通信拓扑下高效收敛且保持几何一致性的去中心化优化方法。

### 核心思路/方法
1. 提出一个完全去中心化的黎曼优化框架，将耦合的位姿与物体联合估计问题通过共识机制解耦，从而支持灵活通信拓扑。
2. 开发一个分布式近似牛顿方法，在SE(d)流形上直接操作，利用局部二阶信息加速收敛，同时保持流形几何结构。
3. 证明方法收敛到黎曼一阶稳定点，并通过局部条件数分析说明二阶信息相比一阶黎曼下降的优势。

### 主要贡献
1. 首个支持灵活通信拓扑的去中心化物体级多机器人SLAM位姿图优化框架。
2. 在SE(d)流形上引入分布式近似牛顿方案，利用二阶信息降低迭代次数和通信开销，同时保持估计精度。
3. 从理论上证明收敛性并分析二阶信息的优势，在公共基准、大规模仿真和真实多机器人实验中验证了准确性、运行效率、跨拓扑可扩展性和通信故障鲁棒性。

### 局限性
摘要未提供足够信息。论文摘要未明确提及局限性内容。

### 阅读优先级
中  
理由：该工作面向多机器人SLAM后端优化，对关注去中心化SLAM、流形优化或通信受限场景的读者有明确参考价值；但摘要未提供实验性能数据对比或具体限定条件，且论文尚未正式出版（arXiv预印本），需结合原文进一步评估其实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Pose graph optimization (PGO) is a key back-end component for state estimation in networked multi-robot simultaneous localization and mapping (SLAM). In object-based multi-robot SLAM, the problem becomes more tightly coupled because robots must jointly estimate both their trajectories and the poses of persistent objects observed by multiple agents. Existing decentralized solutions often assume that the communication graph closely matches the physical interaction topology, which is restrictive in realistic deployments where communication is sparse, intermittent, or time-varying. This paper presents a fully decentralized Riemannian optimization framework for object-based multi-robot PGO that decouples the coupled estimation problem via a consensus mechanism, enabling flexible communication topologies. To improve convergence under limited communication budgets, we further develop a distributed approximate-Newton scheme that exploits local second-order information while operating directly on the SE(d) manifold to preserve geometric consistency, and we establish the convergence to Riemannian first-order stationary points and provide a local condition-number analysis explaining the benefit of approximate second-order information over first-order Riemannian descent. The resulting method reduces iteration count and communication overhead without sacrificing estimation accuracy. Extensive evaluations on public benchmarks, large-scale simulations, and real-world multi-robot experiments demonstrate improved accuracy, runtime efficiency, scalability across network topologies, and robustness to communication failures.

</details>

#### 2026-06-23 - Bengal-HP_RU: A Dataset of Bengal People For Head Pose Estimation

**Authors:** Md. Ahanaf Arif Khan, Md. Tawhidur Rahman, Sangeeta Biswas, Md. Iqbal Aziz Khan, Subrata Pramanik, Sanjoy Kumar Chakravarty, Bimal Kumar Pramanik
**Links:** [abs](https://arxiv.org/abs/2606.24122) - [pdf](https://arxiv.org/pdf/2606.24122)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Bengal-HP_RU: A Dataset of Bengal People For Head Pose Estimation
- 作者：Md. Ahanaf Arif Khan, Md. Tawhidur Rahman, Sangeeta Biswas, Md. Iqbal Aziz Khan, Subrata Pramanik, Sanjoy Kumar Chakravarty, Bimal Kumar Pramanik
- 出版日期：2026-06-23
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2606.24122

### 一句话总结
该论文发布了第一个以孟加拉人为中心的人头姿态估计数据集，包含12,894张带连续偏航、俯仰和滚转角标注的头像。

### 研究问题
现有的人头姿态数据集主要涵盖西方或东亚人群，南亚（特别是孟加拉）人群严重缺乏代表性。因此，该研究旨在填补这一空白，构建一个针对孟加拉对象的头部姿态估计数据集。

### 核心思路/方法
1. 数据来源：从Wikimedia Commons（基于自由许可）收集图片。
2. 数据标注：采用自动化处理流程后，再经过人工标签校正，为每张图像标注连续的偏航、俯仰和滚转角度。
3. 数据划分：根据Wikimedia上传者身份进行划分，防止数据污染，最终得到10,494张训练图像和2,400张测试图像，来自296位唯一上传者。
4. 数据特性：通过收集过程确保年龄、性别、遮挡、光照和背景的多样性，体现野外真实场景。

### 主要贡献
1. 发布了首个公开的、以孟加拉人为对象的头部姿态估计数据集（Bengal-HP_RU）。
2. 数据集包含12,894张标注图像，并提供了连续的姿态角度值。
3. 数据集划分策略避免了数据污染，且通过人工校正保证了标签质量。
4. 该数据集丰富了现有人头姿态数据集的种族和地域多样性。

### 局限性
摘要未提供关于模型性能、数据集与现有方法对比、标注精度具体数值、数据分布统计（如各角度范围的具体分布）以及潜在偏差分析等局限性信息。仅说明数据集在年龄、性别、遮挡、光照、背景方面具有多样性。

### 阅读优先级
中。理由：该论文主要贡献是提供一个特定的、针对南亚人群的数据集，对于从事人脸姿态估计或人脸分析研究的学者，尤其是关注数据多样性和公平性的团队，有较高参考价值。但摘要未展示在该数据集上的基准模型性能，也未提及方法创新，因此不属于方法学突破性论文，阅读优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Existing head pose datasets predominantly feature subjects of Western or East Asian origin, leaving South Asian populations, particularly Bengali individuals, largely underrepresented. We introduce Bengal-HP_RU, the first publicly available head pose dataset centred on Bengali subjects, comprising 12,894 labelled head images annotated with continuous yaw, pitch, and roll values. Images were collected from Wikimedia Commons under free licences and processed through an automated pipeline followed by manual label correction. The dataset is partitioned by Wikimedia uploader identity to prevent data contamination, yielding 10,494 training and 2,400 test images across 296 unique uploaders. Bengal-HP_RU exhibits substantial diversity in subject age, gender, occlusion, illumination, and background, reflecting realistic in-the-wild conditions. The dataset is publicly available at https://doi.org/10.17632/xbw9kr37jb.2.

</details>

#### 2026-06-22 - Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation

**Authors:** Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
**Links:** [abs](https://arxiv.org/abs/2606.23293) - [pdf](https://arxiv.org/pdf/2606.23293)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, embodied AI, manipulation, localization, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Flow6D: Discrete-to-Continuous Flow Matching for Efficient and Accurate Category-Level 6D Pose Estimation
- 作者：Mingyu Mei, Li Zhang, Zibo Dai, Han Sun, Xinyue Zhao, Huiliang Shen, Zaixing He
- 出版日期：2026-06-22
- 分类：3D Reconstruction & Multi-view Geometry (主分类), Embodied / Robotics / AR Applications (副分类)
- 链接：https://arxiv.org/abs/2606.23293

### 一句话总结
Flow6D提出一种两级分层流匹配框架，通过先离散后连续的策略，在保持实时推理速度（70 FPS）的同时，提升类别级6D姿态估计的精度，并自然扩展到铰接物体。

### 研究问题
如何解决类别级6D姿态估计中，高维连续空间直接回归带来的精度受限（噪声和局部最优）和搜索效率低（阻碍实时性）两个关键挑战。

### 核心思路/方法
提出一种两阶段分层流匹配框架：
1. **离散隐空间定位**：先将旋转和平移参数离散化为箱子，使用离散流匹配模型锁定真实姿态附近的隐空间，降低搜索复杂度。
2. **连续姿态回归**：在隐空间中采样后，使用连续流匹配模型预测局部姿态残差，优化估计并回归到精确姿态。

### 主要贡献
- 提出Flow6D框架，结合离散到连续的两阶段流匹配，同时提升效率和精度。
- 在合成和真实数据集上超越现有最优方法，并实现实时推理（70 FPS）。
- 框架自然扩展至铰接物体姿态估计，无需额外设计。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法为类别级6D姿态估计提供了新颖的分层流匹配思路，在精度和实时性（70 FPS）上均取得突破，且对铰接物体有扩展性，对计算机视觉和机器人操作领域具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

6D pose estimation is a key task in computer vision and embodied AI, widely used in robotic manipulation, augmented reality, etc. Existing methods directly regress in a high-dimensional continuous space, facing two key challenges in category-level pose estimation: limited accuracy due to noise and local optima, and inefficient search over an infinite space that hinders real-time performance. This paper proposes Flow6D, a hierarchical flow matching framework with a two-stage discrete latent space localization-continuous pose regression strategy. Rotation and translation parameters are first discretized into bins, with a discrete flow matching model locking the latent space around the true pose to reduce search complexity. Then, by sampling in the latent space, a continuous flow matching model predicts local pose residuals to optimize the estimate and regress to an accurate pose. The framework also naturally extends to articulated objects, outperforming state-of-the-art methods on synthetic and real datasets with real-time inference at 70 FPS. Project website: https://flow6d.github.io/.

</details>

#### 2026-06-22 - DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction

**Authors:** Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi
**Links:** [abs](https://arxiv.org/abs/2606.23031) - [pdf](https://arxiv.org/pdf/2606.23031)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DrivingVoxels: Compositional Sparse Voxel Rasterization for Dynamic Driving Scene Reconstruction
- 作者：Tania Aguirre, Luis Roldão, Moussab Bennehar, Nathan Piasco, Dzmitry Tsishkou, Simone Rossi, Pietro Michiardi
- 出版日期：2026-06-22T08:42:16Z
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications（次分类）
- 链接：[摘要](https://arxiv.org/abs/2606.23031) | [PDF](https://arxiv.org/pdf/2606.23031)

### 一句话总结
DrivingVoxels 提出一种基于组合式稀疏体素光栅化的动态驾驶场景重建框架，通过多独立八叉树联合光栅化实现高效几何表示与训练加速。

### 研究问题
如何高效地重建动态驾驶场景中的无界环境与多个动态物体，同时克服现有稀疏体素方法局限于静态场景、以及3D高斯泼溅方法训练耗时且内存不可控的不足。

### 核心思路/方法
- 采用组合式稀疏体素表示：为每个刚体动态物体定义局部八叉树，并独立建模；另用独立静态八叉树表示静止背景。
- 在单次渲染过程中联合光栅化多个八叉树中的稀疏体素，实现统一渲染。
- 采用完全显式、无神经网络的表示，结合LiDAR引导的结构初始化，高效捕捉场景几何结构。

### 主要贡献
- 提出DrivingVoxels框架，针对动态驾驶场景设计组合式稀疏体素渲染方法。
- 在PandaSet基准上，该方法在新视角合成（NVS）和重建的感知指标上与现有方法持平，在结构指标上更优。
- 因基于强LiDAR先验的高效优化流程，训练时间短于基于3D高斯泼溅的方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作针对动态驾驶场景重建中的效率与表示问题提出新颖的组合式显式体素方法，实验显示训练速度优势；但摘要未提供与其他动态方法（如4D重建或神经辐射场）的详细对比，且未讨论内存消耗具体数值，建议对时序重建或自动驾驶场景视觉感兴趣时阅读。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic urban scenes remains challenging due to the unbounded nature of driving environments and the presence of multiple dynamic objects. Currently, potentially faster sparse voxel methods are mainly designed for static scenarios. On the other hand, dynamic approaches based on 3D Gaussian Splatting, despite their high-fidelity, are often time-consuming for driving scenarios and exhibit uncontrollable memory growth in large scenes. To address these limitations, we present DrivingVoxels, a compositional sparse voxel rendering framework for dynamic driving scenes. Our method jointly rasterizes sparse voxels from multiple independent octrees within a single rendering pass. Each rigid dynamic object is represented by an octree defined in its local coordinate frame, while a separate static octree models the stationary background. DrivingVoxels adopts a fully explicit, neural-free representation together with a LiDAR-guided structural initialization that efficiently captures scene geometry. We evaluate our framework on the PandaSet benchmark, demonstrating that DrivingVoxels performs on par on perceptual metrics and better on structural metrics for NVS and reconstruction while requiring shorter training times than previous 3DGS-base methods to an efficient optimization workflow anchored by a strong LiDAR prior.

</details>

#### 2026-06-22 - Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?

**Authors:** Yu Zhan, Guangcheng Chen, Hanjing Ye, Zhiqin Cheng, Zanjia Tong, Wenjun Xu, Hong Zhang
**Links:** [abs](https://arxiv.org/abs/2606.22987) - [pdf](https://arxiv.org/pdf/2606.22987)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** depth estimation, monocular depth, mesh reconstruction, manipulation, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Can Single-View Mesh Reconstruction Generalize to Robot Camera Rotation?
- 作者：Yu Zhan, Guangcheng Chen, Hanjing Ye, Zhiqin Cheng, Zanjia Tong, Wenjun Xu, Hong Zhang
- 出版日期：2026-06-22
- 分类：3D Reconstruction & Multi-view Geometry (primary); Embodied / Robotics / AR Applications (secondary)
- 链接：arXiv: 2606.22987

### 一句话总结
本文系统评估了单视图网格重建方法在机器人相机旋转下的泛化能力，发现现有方法对相机转动鲁棒性差，并提出基于重力先验的优化方法可显著降低布局方向误差。

### 研究问题
当前单视图网格重建模型依赖于视角先验，当机器人相机在操作和导航过程中发生旋转（即分布外旋转）时，模型是否仍然能够输出一致的3D网格、空间布局和物理合理的结果？

### 核心思路/方法
1. 提出一种带有受控轴向滚转、俯仰和偏航扫描的评估协议，用于追踪单目深度估计、规范对象网格、相机空间布局和物理合理性中的误差链。
2. 在Aria Digital Twin数据集和真实Franka腕部相机序列上进行实验，分析旋转对MDE、布局漂移和碰撞穿透的影响。
3. 比较两阶段流水线（SAM3D+FoundationPose）与单阶段前馈布局预测的鲁棒性。
4. 提出“Gravity-Aware Refinement”方法，利用重力线索修正布局方向。

### 主要贡献
1. 首次系统评估单视图网格重建在机器人相机旋转下的泛化失败模式（3D不一致、错误布局、物理约束违反）。
2. 实验表明：相机旋转会导致MDE失真、布局漂移和碰撞穿透，而规范网格预测相对稳定。
3. 两阶段流水线（SAM3D+FoundationPose）比单阶段前馈预测更鲁棒。
4. 提出的重力感知细化将单阶段ICP布局方向误差降低47.1%。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作直接回应机器人视觉中相机旋转这一实际部署难题，揭示了现有方法在分布外旋转下的严重退化，并提供了量化改进（误差降低47.1%），对从事3D重建、机器人感知和数字孪生研究的人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Single-view mesh reconstruction predicts object meshes and spatial layouts from a single observation, making it attractive for fast robot spatial reasoning and real-to-sim digital twins. However, robot-mounted cameras naturally rotate during manipulation and navigation, while learned single-view reconstruction models often rely on view-dependent priors and may generalize poorly to out-of-distribution camera rotations. Such rotations can introduce 3D inconsistencies, incorrect layouts, and violations of physical constraints, but this failure mode remains under-evaluated. We introduce an evaluation protocol with controlled axis-wise roll, pitch, and yaw sweeps to trace errors in monocular depth estimation (MDE), canonical object meshes, camera-space layout, and physical plausibility within a representative SAM3D-style pipeline. On the Aria Digital Twin dataset and a real Franka wrist-camera sequence, camera rotations induce MDE distortion, layout drift, and collision penetration, while canonical mesh predictions remain relatively stable. A two-stage SAM3D+FoundationPose pipeline is more robust than one-stage feed-forward layout prediction, and our Gravity-Aware Refinement reduces one-stage pairwise ICP-based layout-orientation error by 47.1$\%$. Our evaluation reveals that current single-view mesh reconstruction methods generalize poorly to robot camera rotation, and suggests that explicit gravity cues are important for reliable robotic single-view mesh reconstruction.

</details>

#### 2026-06-22 - Visual Geometry Transformer in the Wild: Distractor-Free 3D Reconstruction

**Authors:** Tianbo Pan, Xingyi Yang, Shizun Wang, Xinchao Wang
**Links:** [abs](https://arxiv.org/abs/2606.22787) - [pdf](https://arxiv.org/pdf/2606.22787)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Visual Geometry Transformer in the Wild: Distractor-Free 3D Reconstruction  
- 作者：Tianbo Pan, Xingyi Yang, Shizun Wang, Xinchao Wang  
- 出版日期：2026-06-22  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2606.22787  

### 一句话总结
本文提出VGTW，一个端到端的多视图3D重建框架，通过抑制跨视图不一致的干扰物（如瞬时遮挡物），从存在干扰的真实场景中鲁棒地重建出干净点云。

### 研究问题
现有端到端多视图3D重建方法依赖“无干扰、完美几何一致性”的静态假设，无法处理真实场景中常见的瞬时遮挡、干扰物等不一致视图，导致重建失败。本文旨在解决在存在干扰物的情况下，如何从不一致的多视图图像中实现鲁棒的3D重建。

### 核心思路/方法
1. **Distractor-aware Training (DAT) 策略**：在注意力机制中，将每个视图的干净特征与受干扰物污染的特征分离，同时强制跨视图的特征一致性。  
2. **辅助掩码预测头**：使用新收集的、带有像素级干扰物掩码的数据集进行监督训练，使模型学会识别干扰物区域。  
3. **前馈架构**：训练后的VGTW可直接输出干净、无干扰的点云，无需额外的3D监督，且保持计算效率，兼容现有pipeline。

### 主要贡献
- 提出VGTW，首个能处理真实场景中干扰物和遮挡的端到端多视图3D重建框架。  
- 提出Distractor-aware Training策略，通过分离干扰特征与一致特征提升鲁棒性。  
- 收集并公开了带有像素级干扰物掩码的新数据集，用于辅助干扰感知训练。  
- 实验表明，VGTW在多样化真实场景中达到最先进性能，且具有良好的泛化能力。

### 局限性
摘要未提供足够信息。具体局限性（如对复杂干扰类型的鲁棒性边界、数据集规模约束、或对极端遮挡的处理能力）未在摘要中提及。

### 阅读优先级
**高**  
理由：该工作针对当前多视图3D重建方法在真实场景中的关键瓶颈（干扰物和遮挡），提出了实用的端到端解决方案，且无需额外3D监督，对推动该领域从理想环境走向实用化有重要意义。方法新颖、实验结果明确，值得精读。

</details>

<details>
<summary>Abstract</summary>

Current end-to-end multi-view 3D reconstruction methods achieve impressive results, but rely on a restrictive static assumption: the scenes is entire distractor-free with perfect cross-view geometry. This reliance on idealized inputs causes even the most advanced methods to fail in real-world settings, where transient distractors and occlusions present. To address this, we propose Visual Geometry Transformer in the Wild (VGTW), an end-to-end framework for robust reconstruction from inconsistent views. At its core, we isolate and suppress distractor-affected regions while preserving the consistent components across views. Specifically, we introduce a Distractor-aware Training (DAT) strategy that separates clean features from distractor-contaminated ones in the attention mechanism while enforcing feature consistency across images. To enable this, we train the model with an auxiliary mask prediction head, using supervision from a new dataset we collected with pixel-level distractor masks. The resulting VGTW model is a feed-forward network that directly outputs clean, distractor-free point clouds. Remarkably, it requires no additional 3D supervision, remains computationally efficient, and is compatible with existing pipelines. Extensive experiments validate our approach, demonstrating state-of-the-art performance and robust generalization in diverse, real-world scenarios.

</details>

## Neural Scene Representations & Rendering

### 2026-06

#### 2026-06-25 - Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN

**Authors:** Archer Moore, Mingming Gong, Liam Hodgkinson
**Links:** [abs](https://arxiv.org/abs/2606.27305) - [pdf](https://arxiv.org/pdf/2606.27305)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, rendering, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sculpting NeRF Geometry: Human-Preference Fine-Tuning of a 3D-Aware Face GAN
- 作者：Archer Moore, Mingming Gong, Liam Hodgkinson
- 出版日期：2026-06-25
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.27305

### 一句话总结
本文提出直接从人类偏好学习的奖励信号微调预训练3D感知生成对抗网络（EG3D）的NeRF密度场，无需网格或形状先验，即可改善人脸几何质量。

### 研究问题
如何在无外部网格、形状先验或文本条件的情况下，仅通过人类偏好反馈直接优化隐式3D表示（NeRF）的几何结构。

### 核心思路/方法
1. 基于预训练的3D感知人脸GAN（EG3D）进行微调。
2. 奖励模型直接从NeRF的连续密度场（σ值）学习，无需预训练，仅需少量偏好样本。
3. 使用密度一致性约束保持2D外观相似性，几何调整仅由密度场的奖励信号驱动。
4. 作为概念验证，仅使用单个标注者的偏好进行训练。

### 主要贡献
1. 首次直接对NeRF密度场进行人类偏好微调，避免转换为网格或其他显式表示。
2. 奖励模型简单易训练，无需预训练，在小样本偏好数据上有效。
3. 在无条件3D人脸GAN上验证方法，用户偏好比较中胜率74.4%，同时量化了分布代价（FID-50k从4.09升至6.66）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该方法提出了一种新颖的、无需网格/文本条件的3D几何优化框架，直接通过人类偏好调整NeRF密度场，具备实际应用潜力（如3D内容创作），且实验验证了用户偏好显著提升。尽管存在分布代价，但全文对NeRF社区和生成模型微调领域有参考价值。

</details>

<details>
<summary>Abstract</summary>

Reinforcement learning from human feedback (RLHF) for 3D generation is now established across a number of works, but most existing pipelines optimise explicit surface representations, often by converting radiance fields into meshes and training heavily on surface-supervised data. We instead fine-tune a pretrained 3D-aware generative model directly from a learned reward over radiance-field density ($σ$) values, with no externally supplied mesh or shape prior. The reward model requires no pretraining, trains easily on a small set of preference samples, and yields robust improvement in 3D geometry. Working on an unconditional 3D-aware face GAN (EG3D), our reward reads the continuous 3D density field of the neural radiance field (NeRF) directly and supplies a geometry-only learning signal, requiring neither text conditioning, mesh extraction, nor multi-view rendering. A density-consistency constraint keeps the 2D appearance qualitatively similar while the geometry is reshaped, at a measurable but bounded distributional cost (FID-50k rises from 4.09 to 6.66): the fine-tuned generator, trained from the preferences of a single annotator as a proof of concept, produces face geometries preferred by users in 74.4% of pairwise comparisons.

</details>

#### 2026-06-25 - Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction

**Authors:** Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung
**Links:** [abs](https://arxiv.org/abs/2606.26985) - [pdf](https://arxiv.org/pdf/2606.26985)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vis4GS: A Visual Analytic Tool for 3D Gaussian Splatting Reconstruction
- 作者：Kai-Yuan Lin, Aryabima Mandala Putra, Jui-Chi Lee, Shih-Hsuan Hung
- 出版日期：2026-06-25
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.26985；PDF：https://arxiv.org/pdf/2606.26985

### 一句话总结
Vis4GS是一个用于3D高斯溅射重建的多视图可视化分析工具，通过连接伪影、高斯属性、视角覆盖度与训练历程，支持基元级别的重建故障诊断，并经过用户研究验证其易用性与理解能力优于原始3DGS查看器。

### 研究问题
3D高斯溅射（3DGS）虽支持快速训练与实时渲染，但其优化过程难以解释。现有查看器主要展示最终重建场景，无法解释高斯属性如何导致可见伪影或如何在训练过程中演变。

### 核心思路/方法
基于原始3DGS查看器与训练框架，构建了四个相互关联的可视化视图：
1. 交互式高斯分析视图：支持高斯选择与伪影评分。
2. 属性时间线视图：展示高斯属性随时间变化。
3. 高斯稠密化树视图：可视化复制、分裂、剪枝等谱系事件。
4. 日志与控制面板。
系统还集成了视角覆盖度分析与多尺度谱系探索，通过将场景级伪影与基元级证据及优化历史相连，提供结构化诊断流程。

### 主要贡献
1. 提出Vis4GS工具，首次在基元级别对3DGS重建伪影进行可视化诊断。
2. 设计四个联动视图，覆盖伪影评分、属性演化、稠密化谱系与视角覆盖度。
3. 用户研究表明Vis4GS在可用性与伪影理解上优于原始3DGS查看器。
4. 提供超越最终图像检查与全局指标的故障诊断工作流。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中
理由：该工具主要服务于3DGS实践中的调试与诊断，对关注3DGS内部分析或可视化系统设计的读者有参考价值；但摘要未提供定量性能比较或技术实现细节，理论贡献有限，适合中等优先级阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) supports fast training and real-time rendering, but its optimization process remains difficult to interpret. Existing viewers mainly expose the final reconstructed scene and offer limited support for explaining how Gaussian properties contribute to visible artifacts or evolve during training. We present Vis4GS, a multi-view visual analytics tool for primitive-level diagnosis of 3DGS reconstruction artifacts. Built on the original 3DGS viewer and training framework, Vis4GS links rendered artifacts to Gaussian properties, View Coverage, training progress, and Gaussian genealogy through four linked views: an interactive Gaussian analysis view, a property timeline view, a Gaussian densification tree view, and a log and control panel. The system supports Gaussian selection, blur and needle-like artifact scoring, View Coverage analysis, and multiscale genealogy exploration of clone, split, prune, and clone-split events. By connecting scene-level artifacts with primitive-level evidence and optimization history, Vis4GS enables a structured workflow for diagnosing reconstruction failures beyond final-image inspection and global metrics. A user study also shows that Vis4GS provides stronger support for usability and artifact understanding than the original 3DGS viewer.

</details>

#### 2026-06-25 - Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting

**Authors:** Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang
**Links:** [abs](https://arxiv.org/abs/2606.26754) - [pdf](https://arxiv.org/pdf/2606.26754)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Capacity-Controlled Multi-View Stylization of 3D Gaussian Splatting
- 作者：Zhihao Wen, Yixin Yang, Bojian Wu, Yang Zhou, Dani Lischinski, Daniel Cohen-Or, Hui Huang
- 出版日期：2026-06-25T08:36:50Z（注：日期在论文输入中标记为2026年，可能为录入错误或未来日期，但按原信息输出）
- 分类：Neural Scene Representations & Rendering
- 链接：摘要URL: https://arxiv.org/abs/2606.26754；PDF: https://arxiv.org/pdf/2606.26754

### 一句话总结
本文提出一种基于最优运输的容量控制框架，通过半平衡最优运输问题约束风格特征的列容量，从而改善3D Gaussian Splatting的多视角风格化一致性与稳定性。

### 研究问题
如何在不牺牲场景语义结构的前提下，使3DGS在不同视角下稳定分配风格特征，避免多对一特征重用和跨视角不一致的问题。

### 核心思路/方法
1. 将局部风格匹配重新表述为半平衡最优运输问题，引入可调强度的显式列容量约束，以缓解多对一匹配并实现可控的风格特征分配。
2. 提出新颖的跨视角匹配引导机制，约束场景内容与风格模式之间的对应关系，增强跨视角连贯性。
3. 引入若干几何正则化方法改进基础3DGS，使其在风格化过程中能表示更精细的纹理。

### 主要贡献
1. 提出基于最优运输的容量控制框架，通过列容量约束实现多视角稳定的风格化。
2. 设计跨视角匹配引导机制，提升风格化在视图间的一致性。
3. 引入几何正则化增强3DGS，使其在风格化时保留细粒度纹理与语义结构。

### 局限性
摘要未提供足够信息，未讨论方法的计算开销、场景复杂度的适用边界，或可能的失败案例。

### 阅读优先级
中。理由：该方法针对3D风格化中多视角一致性的痛点提出了理论新颖的解决方案（最优运输+容量控制），但属于特定任务优化，对于不从事3D神经渲染或风格化的读者相关性较低；且摘要未提供定量比较或实验细节，需进一步阅读正文评估有效性。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) provides an efficient and explicit representation for novel view synthesis, enforcing stylistic coherence across viewpoints remains challenging. Existing 3D stylization methods typically apply 2D feature-matching losses independently per rendered view, which leads to unstable style allocation, many-to-one feature reuse, and limited cross-view consistency. We propose a capacity-controlled framework for multi-view stylization of 3DGS, grounded in optimal transport. Specifically, we reformulate local style matching as a semi-balanced optimal transport problem. By introducing explicit column-capacity constraints with tunable strength, our formulation mitigates many-to-one matching and enables controllable allocation of style features. This transport-based objective provides a principled mechanism for balancing feature coverage and stylistic diversity while maintaining stable correspondences across viewpoints. To further enhance cross-view coherence, we incorporate a novel cross-view matching guidance to constrain correspondences between scene content and style patterns. In addition, we introduce several geometric regularizations to enhance the vanilla 3DGS, thereby enabling optimized Gaussian primitives to represent finer-grained textures during stylization. Extensive experiments demonstrate that our approach significantly improves multi-view stylistic consistency and produces stable, expressive 3D stylizations while preserving the core semantic structure of the scene.

</details>

#### 2026-06-24 - Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation

**Authors:** Masaki Minai, Yusuke Monno, Masatoshi Okutomi, Sho Suzuki
**Links:** [abs](https://arxiv.org/abs/2606.25427) - [pdf](https://arxiv.org/pdf/2606.25427)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, radiance, splatting, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gastroendoscopy View Synthesis: A New Real Dataset and Evaluation
- 作者：Masaki Minai, Yusuke Monno, Masatoshi Okutomi, Sho Suzuki
- 出版日期：2026-06-24
- 分类：神经场景表示与渲染（Neural Scene Representations & Rendering）
- 链接：摘要链接 https://arxiv.org/abs/2606.25427 ; PDF链接 https://arxiv.org/pdf/2606.25427

### 一句话总结
本文发布了首个用于胃内窥镜新型视角合成（NVS）的真实数据集GastroNVS，并基于多种3D高斯泼溅（3DGS）方法进行了评估，指出了该应用场景下的挑战。

### 研究问题
现有胃内窥镜场景下的新型视角合成研究缺乏足够的真实数据集，无法有效评估和推动相关方法（如NeRF和3DGS）在该领域的应用。

### 核心思路/方法
1. 创建并发布首个真实胃内窥镜NVS数据集GastroNVS，包含胃镜图像、相机位姿和点云数据。
2. 利用该数据集，对多种3D高斯泼溅方法进行定量和定性评估，以验证数据集的适用性并分析当前方法的不足。

### 主要贡献
- 提出了首个用于胃内窥镜新型视角合成的真实数据集GastroNVS。
- 基于该数据集对现有3DGS方法进行了系统评估，揭示了胃内窥镜场景下NVS的具体挑战，为未来研究提供基准和方向。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：本文针对胃内窥镜这一特定医学应用，提供了首个真实NVS数据集，填补了现有数据资源的空白。对于从事医学影像分析、神经渲染或内窥镜图像处理的研究者具有直接参考价值，且数据集可申请获取，便于后续复现与拓展。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis (NVS) is an active research topic in computer vision, owing to the success of neural radiance field (NeRF) and 3D Gaussian splatting (3DGS) methods. While NVS opens the door to potential applications in gastroendoscopy, such as extending the field of view of endoscopic images and enabling digital twins for 3D archiving and endoscopist manipulation training, the dataset is insufficient to evaluate NVS for gastroendoscopy. In this paper, we present the first real gastroscopy dataset for NVS, namely the GastroNVS dataset, which contains a set of gastroscopic images, camera poses, and a point cloud for real gastroendoscopy inspection. To assess the suitability of the GastroNVS dataset, we evaluate several 3DGS methods and discuss the challenges for future development. The dataset is available on request from our project page.

</details>

#### 2026-06-23 - FLAT: Feedforward Latent Triangle Splatting for Geometrically Accurate Scene Generation

**Authors:** Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari
**Links:** [abs](https://arxiv.org/abs/2606.24876) - [pdf](https://arxiv.org/pdf/2606.24876)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, rendering, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FLAT: 前馈潜在三角形泼溅技术用于几何精确的场景生成
- 作者：Orest Kupyn, Goutam Bhat, Philipp Henzler, Fabian Manhardt, Christian Rupprecht, Federico Tombari
- 出版日期：2026-06-23T17:53:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.24876

### 一句话总结
本文首次证明可以从视频扩散潜在码中直接解码出三角形泼溅（triangle splats）作为显式表面基元，通过射线居中旋转参数化和乘积窗函数解决了梯度流问题，从而在保持视觉质量的同时显著提升了3D场景几何精度。

### 研究问题
如何从单张图像的压缩视频扩散潜在码中，直接在单个前馈过程中解码出表面对齐的显式几何基元（三角形泼溅），以替代现有的体素化3D高斯表示，从而获得具有良好定义表面的可渲染场景。

### 核心思路/方法
1.  提出FLAT方法，从视频扩散潜在码直接解码三角形泼溅。
2.  **射线居中的旋转参数化（ray-centered rotation parameterization）**：用于三角形回归，降低对基元朝向的敏感性。
3.  **乘积窗函数（product window function）**：一种新颖的可微分三角形渲染中的窗口函数，改善梯度流，使得训练时梯度能更有效地回传到三角形参数上。
4.  轻量级测试时精化步骤（test-time refinement step）：将预测的三角形“汤”转换成完全不透明、可用于游戏引擎的表示，支持实时渲染。
5.  在相同训练设定下系统比较了3D高斯泼溅、2D高斯泼溅和三角形泼溅的表示权衡。

### 主要贡献
- 首次证明可以从视频扩散潜在码中直接解码三角形泼溅作为显式表面基元。
- 提出了射线居中旋转参数化和乘积窗函数，有效解决了三角形泼溅训练中梯度流不畅的难题。
- 在标准基准测试上，相比最先进的前馈基线方法，FLAT在保持竞争性视觉质量的同时实现了显著更好的几何精度。
- 提供了首个关于前馈场景生成中不同基元表示（3DGS、2DGS、三角形泼溅）权衡的系统性分析。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该工作首次将显式三角形泼溅与前馈视频扩散潜在码解码相结合，解决了几何精度和表面定义的瓶颈，并提供了系统的基元表示对比分析。这对于3D场景生成、神经渲染和计算机图形学领域有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating explorable 3D scenes from a single image requires strong generative priors and accurate geometric representations suitable for downstream use. Current video diffusion models offer high-quality generation and implicitly encode multi-view geometric structure in latent space. However, existing feedforward latent scene decoders typically output volumetric 3D Gaussians that lack a well-defined surface, limiting their use in simulation or standard graphics pipelines. This motivates decoding surface-aligned primitives that are not only renderable but also closer to explicit geometric assets. We ask whether compressed video diffusion latents can be mapped directly to explicit surface primitives in a single pass. To this end, we introduce FLAT and, for the first time, show that triangle splats can be decoded directly from video diffusion latents. Compared with decoding 3D Gaussians, predicting flat primitives is notoriously more challenging due to high sensitivity to primitive orientations, oftentimes leading to poor gradient flow. FLAT solves with two key ingredients: a ray-centered rotation parameterization for triangle regression and a novel product window function that improves gradient flow during differentiable triangle rendering. On standard benchmarks, FLAT achieves significantly better geometric accuracy while maintaining competitive visual quality compared to state-of-the-art feedforward baselines. We further show that a lightweight test-time refinement step converts the predicted triangle soup into a fully opaque, game-engine-ready representation that supports real-time rendering. By evaluating 3DGS, 2DGS, and triangle splatting variants under an identical training setup, we provide the first systematic analysis of representation tradeoffs in feedforward scene generation. The project page is available at https://flat-splat.github.io

</details>

#### 2026-06-23 - FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation

**Authors:** Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo
**Links:** [abs](https://arxiv.org/abs/2606.24874) - [pdf](https://arxiv.org/pdf/2606.24874)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FLUX3D: High-Fidelity 3D Gaussian Generation with Diffusion-Aligned Sparse Representation  
- 作者：Haorui Ji, Weizhe Liu, Hongdong Li, Hengkai Guo  
- 出版日期：2026-06-23  
- 分类：Neural Scene Representations & Rendering  
- 链接：https://arxiv.org/abs/2606.24874  

### 一句话总结
FLUX3D 提出了一种基于扩散对齐稀疏表示的图像到3D高斯泼溅生成框架，通过改进特征表示和跨模态对齐，显著提升了生成3D资产的外观保真度。

### 研究问题
当前基于稀疏体素表示的图像到3DGS生成方法，在保持输入图像的高频视觉细节方面存在两个瓶颈：1）使用用于语义抽象的判别式2D特征构建稀疏体素潜伏表示，抑制了重建线索，导致表示瓶颈；2）在生成阶段，标准扩散变换器缺乏有效机制来对齐密集2D图像标记与稀疏3D体素潜伏表示，导致跨模态对应瓶颈。

### 核心思路/方法
1. **表示学习改进**：提出扩散对齐结构化潜伏表示（DA-SLAT），重新审视稀疏体素3D表示学习中的2D特征选择，并配合仅解码器架构，提升3DGS重建保真度。  
2. **跨模态对齐改进**：设计稀疏结构感知扩散框架，包括稀疏结构多模态扩散变换器（SMDiT）和模态感知旋转位置嵌入（MARoPE），实现与几何无关的2D-3D对齐。

### 主要贡献
1. 提出DA-SLAT方法，优化稀疏体素表示的2D特征选择，提高3DGS重建细节。  
2. 设计SMDiT和MARoPE机制，解决生成阶段稀疏与密集模态的对应问题。  
3. 实验表明FLUX3D在生成高质量3DGS资产的外观保真度上显著优于所有现有最先进方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文针对图像到3DGS生成领域的关键保真度瓶颈，提出了系统性的架构改进，且在基准测试中全面超越现有方法，对高精度3D内容生成方向有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Sparse voxel representation has emerged as a scalable foundation for image-to-3D Gaussian Splatting (3DGS) generation, yet current methods struggle to preserve high-frequency visual details of input images due to two structural bottlenecks. First, they adopt discriminative 2D features optimized for semantic abstraction to construct sparse voxel latents, which suppress reconstructive cues and induce a representation bottleneck. Second, in the generation stage, standard diffusion transformers lack effective mechanisms to align dense 2D image tokens with sparse 3D voxel latents, resulting in a cross-modal correspondence bottleneck. To address these issues, we propose FLUX3D, a scalable image-to-3DGS framework that boosts both representation learning and cross-modal alignment during generation. We first revisit 2D feature selection for sparse-voxel-based 3D representation learning, propose Diffusion-Aligned Structured Latents (DA-SLAT) and couple it with a decoder-only architecture to improve 3DGS reconstruction fidelity. We also design a sparse-structure-aware diffusion framework, which integrates the Sparse-structure Multimodal Diffusion Transformer (SMDiT) and Modal-Aware Rotary Positional Embedding (MARoPE) to achieve geometry-agnostic 2D-3D alignment. Extensive benchmark experiments demonstrate that FLUX3D yields substantial improvements in appearance fidelity and significantly outperforms all state-of-the-art (SOTA) methods in generating high-quality 3DGS assets.

</details>

#### 2026-06-23 - OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis

**Authors:** Chenrui Fan, Paolo Favaro
**Links:** [abs](https://arxiv.org/abs/2606.24799) - [pdf](https://arxiv.org/pdf/2606.24799)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OrbitForge: Text-to-3D Scene Generation via Reconstruction-Anchored Video Synthesis
- 作者：Chenrui Fan, Paolo Favaro
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering
- 链接：摘要链接 https://arxiv.org/abs/2606.24799；PDF链接 https://arxiv.org/pdf/2606.24799

### 一句话总结
OrbitForge 通过冻结的文本到视频模型与逐提示的3D高斯泼溅重建优化，将单次文本生成的视频转化为完整的闭环轨道3D场景，无需多视图微调或分数蒸馏优化。

### 研究问题
如何利用现有文本到视频模型生成高质量、覆盖完整的3D场景，同时克服视频中相机运动难控、视图覆盖不全及帧间不一致的问题。

### 核心思路/方法
1. **初始重建**：从首段生成的视频出发，通过可变形高斯泼溅（使用稳健的MedianGS代理）获得初步3D重建。
2. **缺失视图检测**：沿预设轨道渲染视图，识别未覆盖的视角区域。
3. **补全与重构**：仅使用文本到视频模型补全缺失视图，再将完整的轨道渲染结果重建为最终的高斯泼溅场景。整个流程无需任务特定视频或多视图微调、也无需逐提示的分数蒸馏或逐步生成视图。

### 主要贡献
- 提出一种无需多视图微调或分数蒸馏优化的文本到3D场景生成框架。
- 通过3D重建作为锚点，改善生成视频的3D一致性。
- 引入重建设计中考虑覆盖率评估的必要性：仅依赖局部平滑度会奖励那些从未尝试完整轨道的生成方法。
- 在T3Bench派生测试集（300个提示）上，OrbitForge重建的平均覆盖中位数为359.0度，将MedianGS单独重建的Q10 ImageReward值从8.07提升至16.36，并在覆盖率-质量上接近VideoMV。

### 局限性
摘要未提供关于运行时间、计算资源消耗、对复杂场景（如动态物体或细粒度纹理）的适用性、或与更强基线方法（如多视图扩散模型）的对比等具体局限性信息。

### 阅读优先级
高。理由：该工作提出了一种直接利用现有文本到视频模型生成高质量3D场景的实用方案，克服了视图覆盖不足和一致性问题，且无需特定微调；在覆盖率评估和性能提升上有明确、可量化的贡献（如359度轨道覆盖和ImageReward提升），对神经场景表示与渲染领域的从业者极具参考价值。

</details>

<details>
<summary>Abstract</summary>

Generic text-to-video models can be used as rich open-world scene priors. Despite the high quality of today's generated videos, they do not directly yield reliable 3D assets: camera motion is difficult to control, view coverage is partial, and frames often contain inconsistencies across time. We introduce OrbitForge, an adapter built from frozen video priors and per-prompt Gaussian Splatting reconstruction optimization that converts a single text-generated video into a canonical closed-orbit 3D Gaussian Splatting scene. We use 3D reconstruction as an anchor to improve the 3D consistency of the generated video. We obtain a preliminary 3D reconstruction from a first generated video via Deformable Gaussian Splatting with a robust MedianGS proxy. We render views from a prescribed orbit to detect missing viewpoints. OrbitForge uses the text-to-video model to complete only the missing views, and reconstructs the completed orbit into a final Gaussian Splatting scene. This design requires no task-specific video or multiview fine-tuning, avoids per-prompt score-distillation optimization, and does not progressively generate views one step at a time. We further argue that this setting demands coverage-aware evaluation: local smoothness alone rewards methods that never attempt a full orbit. On a frozen 300-prompt T3Bench-derived audit, OrbitForge reconstruction attains a 359.0-degree measured median span, raises originally unsupported-bin Q10 ImageReward from 8.07 to 16.36 relative to MedianGS-only reconstruction, while remaining competitive with VideoMV on the coverage-quality.

</details>

#### 2026-06-23 - ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos

**Authors:** Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum
**Links:** [abs](https://arxiv.org/abs/2606.24628) - [pdf](https://arxiv.org/pdf/2606.24628)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting, embodied AI, manipulation, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos
- 作者：Pranjal Mishra, René Zurbrügg, Max Wilder-Smith, Marco Hutter, Marc Pollefeys, Zuria Bauer, Hermann Blum
- 出版日期：2026-06-23
- 分类：神经场景表示与渲染（主分类）；具身/机器人/AR应用（副分类）
- 链接：摘要: https://arxiv.org/abs/2606.24628 | PDF: https://arxiv.org/pdf/2606.24628

### 一句话总结
提出ArtiTwinSplat框架，仅需RGB-D视频即可自动构建具有关节、照片级真实感的物体数字孪生，支持实时渲染、视角控制和交互操作，且无需CAD模型、仿真资产或人工标注。

### 研究问题
如何从现实世界的RGB-D视频中自动、规模化地重建具有**可交互关节**且**照片级逼真**的物体数字孪生，以降低机器人系统集成中动态对象建模的瓶颈。

### 核心思路/方法
1. **基于3D高斯溅射（3D Gaussian Splatting）**：保持几何保真度与光度真实感。
2. **无监督关节发现流水线**：仅从观测到的运动恢复物体部件结构和关节运动学，无需人工标注。
3. **追踪与优化阶段**：提供稳定、可查询的数字孪生，支持实时渲染、视角控制与交互操作。

### 主要贡献
- 提出首个能直接从RGB-D视频自动构建**可交互**、**关节式**数字孪生的框架。
- 无需CAD模型、仿真资产或人工标注，直接操作真实世界观测数据。
- 产物可直接用于下游机器人规划与学习系统，降低具身AI与人机协作中物体操纵的集成门槛。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
- 理由：该方法直接解决了机器人学与具身AI中从真实世界视频自动生成可交互数字孪生的实际瓶颈，方法创新性（无监督关节发现+3D高斯溅射）和实用性（无需仿真资产）突出，且发表时间较新（2026年），对相关领域研究者有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Deploying robots in unstructured real-world environments needs accurate, interactive models of the objects. Constructing these models at scale remains a critical bottleneck for robotic system integration. We present ArtiTwinSplat, a framework that automatically constructs articulated, photo-realistic digital twins of objects directly from RGB-D videos, requiring no CAD models, simulation assets, or manual annotations. Our method is built on 3D Gaussian Splatting that preserve geometric fidelity and photometric realism, coupled with an unsupervised articulation discovery pipeline that recovers part structure and joint kinematics from observed motion alone. With tracking and optimization stages our method provides stable, queryable digital twins that support real-time rendering, viewpoint control, and interactive manipulation. Unlike prior methods confined to simulation, ArtiTwinSplat operates directly on real-world observations and produces twins that are immediately usable by downstream robot planning and learning systems. This method offers a practical, scalable pathway toward digital twin construction, lowering the integration barrier for articulated object manipulation in embodied AI and human-robot collaboration contexts.

</details>

#### 2026-06-23 - Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation

**Authors:** Tianyu Zhu, Yingping Liang, Hesong Li, Ying Fu
**Links:** [abs](https://arxiv.org/abs/2606.24464) - [pdf](https://arxiv.org/pdf/2606.24464)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** monocular geometry, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Boosting Text-Driven Video Segmentation via Geometry-Aware Distillation
- 作者：Tianyu Zhu, Yingping Liang, Hesong Li, Ying Fu
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.24464

### 一句话总结
本文提出GeoLaV框架，通过两阶段方法蒸馏3D几何知识，增强文本驱动的视频目标分割中的时空一致性与语言定位能力。

### 研究问题
现有文本驱动视频目标分割（RVOS）模型通常在2D图像或视频数据集上训练，使用朴素的分割损失，忽略了帧间的几何一致性，导致空间理解薄弱。

### 核心思路/方法
1. **第一阶段**：单目几何预训练。利用单目新颖视角合成任务，在大型单图像数据集上进行空间对齐，使模型获得几何一致的视觉表征。
2. **第二阶段**：几何感知蒸馏与微调。从通用3D先验模型中蒸馏3D结构知识，并在视频分割数据集上微调模型，从而增强时空连贯性与语言接地能力。

### 主要贡献
1. 提出GeoLaV两阶段框架，将3D几何知识从图像蒸馏至文本驱动视频分割模型中。
2. 仅使用图像分割数据即可在RVOS任务中实现显著的零样本泛化能力。
3. 联合几何感知蒸馏与视频微调后，在多个RVOS基准上达到最先进性能。

### 局限性
摘要未提供具体局限性信息，例如方法对计算资源的需求、对特定数据集依赖程度或失败案例等。

### 阅读优先级
- **优先级：高**
- **理由**：该方法在文本驱动视频分割任务上通过引入几何感知蒸馏实现了性能提升，且仅用图像数据即可零样本泛化，具有实际应用潜力，但需注意该论文标注日期为2026年，可能为预印本，需进一步验证可信度。

</details>

<details>
<summary>Abstract</summary>

Text-driven Referring Video Object Segmentation (RVOS) aims to locate and segment target objects in videos given natural language. However, existing models are typically trained on 2D image or video datasets with naive segmentation losses, which overlooks the geometric consistency across frames and leads to weak spatial understanding. In this paper, we propose Geometry-enhanced Language-guided Video segmentation (GeoLaV), a two-stage framework that distills 3D geometric knowledge from images to enhance text-driven video segmentation. In the first stage, we perform monocular geometry pretraining with monocular novel-view synthesis, enabling the model to acquire geometry-consistent visual representations via spatial alignment on large-scale single-image datasets. In the second stage, we introduce geometry-aware distillation and fine-tune the model on video segmentation datasets, transferring 3D structural knowledge from a general 3D prior model. This process reinforces 3D awareness and improves both spatiotemporal coherence and language grounding in segmentation. Extensive experiments show that our method using only image segmentation data already provides notable zero-shot generalization in RVOS. When combined with geometry-aware distillation for fine-tuning on videos, our method achieves state-of-the-art performance across multiple RVOS benchmarks. The code is available at https://github.com/Tony1882880/GeoLaV.

</details>

#### 2026-06-23 - SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks

**Authors:** Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang
**Links:** [abs](https://arxiv.org/abs/2606.24361) - [pdf](https://arxiv.org/pdf/2606.24361)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks
- 作者：Zhewen He, Junyi Hu, Haomian Huang, Zhenhua Li, Yu-Shen Liu, Yi Fang
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.24361

### 一句话总结
论文发布了SignNet-1M，一个大规模多语言手语视频数据集，通过3D高斯泼溅和扩散模型合成真实场景变化，以提升手语模型在现实分布偏移下的鲁棒性。

### 研究问题
现有手语模型在受限条件下（如视角、背景、签名者身份多样性有限）训练，导致在真实世界分布偏移下泛化能力差。论文旨在通过构建大规模增强数据集来改善这一现状。

### 核心思路/方法
构建SignNet-1M数据集，涵盖美国手语（ASL）、中国手语（CSL）和德国手语（DGS）。数据增强沿三个轴进行：
1. 通过3D高斯泼溅合成新视角渲染（旋转和缩放）。
2. 利用扩散模型进行场景/身份编辑（背景替换和签名者替换），同时保留手语动作和语言内容。
3. 应用渲染后增强，模拟采集和压缩伪影（如姿态/时间扰动和视频级损坏），以匹配野外记录。

### 主要贡献
- 发布了大规模多语言手语视频数据集SignNet-1M，包含ASL、CSL和DGS。
- 提供了跨下游任务（如翻译和识别）的统一基准测试套件，以及隔离每种增强组件的消融实验。
- 实验表明，使用该数据集训练可提升跨视角、跨背景、跨身份及渲染后偏移下的泛化能力，同时保持强分布内性能。
- 公开了数据集、完整增强管线和基准测试。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该论文针对手语识别与翻译中的关键鲁棒性问题，提出了一个大规模、多语言、多方式增强的数据集，并提供了统一的基准测试。对于从事手语处理、多模态学习、以及数据增强（特别是3D渲染和扩散模型应用）的研究人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Sign language models are typically trained on datasets captured under constrained conditions, with limited viewpoint, background, and signer-identity diversity, leading to poor robustness under real-world distribution shifts. We introduce SignNet-1M, a large-scale augmented dataset spanning ASL, CSL, and German Sign Language (DGS). SignNet-1M synthesizes realistic variations along three axes: (i) novel-view rendering (rotation and zoom) via 3D Gaussian Splatting (3DGS), (ii) scene/identity editing via diffusion models for background replacement and signer substitution while preserving sign motion and linguistic content, and (iii) post-rendering augmentations that emulate capture and compression artifacts (e.g., pose/temporal perturbations and video-level corruptions) to better match in-the-wild recordings. Beyond data release, we provide a unified benchmark suite across downstream tasks (e.g., translation and recognition) and ablations that isolate each augmentation component. Experiments across backbones show that training with SignNet-1M consistently improves generalization under cross-view, cross-background, cross-identity, and post-rendering shifts, while maintaining strong in-distribution performance. The dataset, full augmentation pipeline, and benchmark are available at https://signnet.chatsign.ai/.

</details>

#### 2026-06-23 - MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving

**Authors:** Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan
**Links:** [abs](https://arxiv.org/abs/2606.24301) - [pdf](https://arxiv.org/pdf/2606.24301)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, neural rendering, rendering, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving
- 作者：Hongli Xiao, Youjian Zhang, Yucai Bai, Chaoyue Wang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering（主要），Embodied / Robotics / AR Applications（次要）
- 链接：https://arxiv.org/abs/2606.24301

### 一句话总结
本文提出MM-TRELLIS，一个基于TRELLIS的多模态3D车辆生成模型，通过融合多视图图像和LiDAR点云，从自动驾驶场景中生成高保真、几何准确的3D车辆网格。

### 研究问题
如何利用自动驾驶场景中的多模态传感器数据（多视图图像和LiDAR点云）生成高质量、几何一致的3D车辆模型，以克服现有方法依赖神经渲染导致网格质量低、且无法适应任意多视图输入和真实驾驶图像的问题。

### 核心思路/方法
1. **多模态输入融合**：将多视图图像作为条件输入，LiDAR点云作为测试时的几何指导，确保几何精度和跨视图一致性。
2. **去噪对齐策略**：在去噪过程中，先将指导点云与模型先验对齐，再强制生成几何与指导点云之间的一致性。
3. **体素过滤策略**：基于3D高斯泼溅的透明度进行体素过滤，抑制浮动伪影，生成干净网格。

### 主要贡献
- 提出MM-TRELLIS，将自动驾驶数据集中的多模态传感器集成到原生3D生成模型中。
- 利用LiDAR点云在测试阶段提供几何指导，提升生成车辆的几何准确性和跨视图一致性。
- 引入基于3D高斯泼溅透明度的体素过滤技术，有效清除浮动伪影，生成高质量网格。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。
理由：该工作直接针对自动驾驶场景中3D车辆生成的实际需求，提出利用多模态数据（图像+LiDAR）改进生成质量，方法创新点明确（点云指导、体素过滤），且在Waymo数据集上取得优于现有方法的结果。对于从事自动驾驶仿真、数据生成或3D生成研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment. However, most existing vehicle generation methods fail to fully exploit multimodal sensors i.e. multi-view images and LiDAR point clouds) and rely on neural rendering based reconstruction, leading to low-quality mesh. Recently, native 3D generative models have made significant progress, yet they are not built for arbitrary multi-view inputs and often struggle with in-the-wild driving images. In this work, we present MM-TRELLIS, a multi-modal version of TRELLIS for in-the-wild 3D vehicle generation that integrates LiDAR and image sensors from autonomous driving datasets into native 3D generative models. Specifically, multi-view images are cycled as conditioning inputs, while LiDAR point clouds provide test-time guidance to ensure geometric accuracy and cross-view consistency. During denoising, we first align the guidance point cloud with the model priors, then enforce consistency between the generated geometry and the guidance point cloud. Finally, we introduce a voxel filtering strategy based on the opacity of 3D Gaussian Splatting to suppress floaters and produce clean meshes. Comprehensive experiments on Waymo dataset demonstrate our method outperforms existing methods in high-fidelity 3D vehicle generation. Code is available at https://github.com/HongliXiao/MM-TRELLIS.

</details>

#### 2026-06-23 - 3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis

**Authors:** Hongli Xiao, Youjian Zhang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan
**Links:** [abs](https://arxiv.org/abs/2606.24257) - [pdf](https://arxiv.org/pdf/2606.24257)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward reconstruction, mesh reconstruction, Gaussian Splatting, 3D Gaussian Splatting, view synthesis, splatting, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis
- 作者：Hongli Xiao, Youjian Zhang, Yaohui Jin, Xiaoguang Ren, Wenjing Yang, Long Lan
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering（主）；Embodied / Robotics / AR Applications（副）
- 链接：https://arxiv.org/abs/2606.24257

### 一句话总结
提出3DCarGen框架，通过3D一致的多视图合成生成任意数量的视图，实现从单张真实图像到高质量3D车辆模型的重建。

### 研究问题
如何从单张真实世界图像生成具有几何一致性的可扩展3D车辆资产，以支持自动驾驶仿真。

### 核心思路/方法
1. 输入单张图像，首先生成一组固定视角的多视图图像。
2. 将这些图像输入前馈重建模型，基于3D高斯泼溅得到粗糙的3D表示。
3. 利用此显式3D先验，多视图扩散模型从任意相机视角生成3D一致的图像。
4. 扩展快速网格重建算法，引入颜色-法线联合优化，从合成密集视图中恢复细节且连贯的3D车辆模型。

### 主要贡献
- 提出3DCarGen框架，实现了从单张真实图像合成任意数量3D一致多视图图像的能力。
- 通过显式3D先验引导的多视图扩散模型，提升了跨视图几何一致性。
- 扩展快速网格重建算法，结合颜色-法线联合优化，生成细节丰富的3D车辆模型。
- 在合成和真实数据集上实验证明，该方法在几何一致性和重建保真度上优于现有方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作聚焦自动驾驶仿真中的核心需求——高质量3D车辆资产生成，方法新颖（结合多视图扩散与显式3D先验），且在合成与真实数据集上均验证了有效性，对从事神经渲染、自动驾驶仿真等领域的读者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

High-quality 3D vehicle assets are essential for autonomous driving simulation. Although multi-view diffusion-based paradigms enable controllable single-image reconstruction, they typically produce limited viewpoints and exhibit cross-view geometric inconsistencies, thereby reducing reconstruction fidelity in real-world scenarios. In this work, we introduce 3DCarGen, a scalable single-view 3D car generation framework designed for real-world images by synthesizing an arbitrary number of 3D-consistent multi-view images. Specifically, given a single image as input, we first synthesize a set of images from fixed viewpoints. These images are then fed into a feed-forward reconstruction model, resulting in a coarse 3D representation based on 3D Gaussian Splatting. Conditioned on this explicit 3D prior, our multi-view diffusion model generates 3D-consistent images from arbitrary camera viewpoints. We further extend a fast mesh reconstruction algorithm by incorporating color-normal joint optimization to recover detailed and coherent 3D vehicle models from the synthesized dense views. Extensive experiments on synthetic and real-world datasets demonstrate that our approach achieves robust geometric consistency and reconstruction fidelity compared to existing methods. Code and models will be released.

</details>

#### 2026-06-23 - Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms

**Authors:** Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir
**Links:** [abs](https://arxiv.org/abs/2606.24180) - [pdf](https://arxiv.org/pdf/2606.24180)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, rendering, splatting, robotics, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Deep Learning Approaches for 3D Medical Scene Completion: From Geometric Modeling to Generative Paradigms
- 作者：Afifa Khaled, Said Jadid Abdulkadir, Majdy Mohamed Eltayeb Eltahir
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（副分类）
- 链接：摘要页 https://arxiv.org/abs/2606.24180；PDF https://arxiv.org/pdf/2606.24180

### 一句话总结
本文是2016至2026年间三维场景补全领域的系统综述，梳理了从SSCNet的体素语义补全到基于扩散先验与高斯泼溅渲染的最新范式演变。

### 研究问题
三维场景补全作为计算机视觉和机器人领域中的一个重要问题，其应用涵盖自主导航、增强现实等。本研究旨在系统性地综述过去十年（2016–2026）该领域从几何建模到生成范式的代表性研究方法及其演进。

### 核心思路/方法
- 进行系统综述，收集并分析2016–2026年间的相关研究贡献。
- 讨论表征范式的演化：体素网格、点学习、隐式神经场、Transformer网络、扩散网络，以及基于渲染感知的3D高斯原语（Gaussian primitives）。
- 构建分类法（taxonomy）以清晰呈现十年间该领域的贡献结构。
- 列举尚未解决的挑战，并提出下一代系统发展的研究方向。

### 主要贡献
- 对过去十年三维场景补全研究进行系统梳理和综合分析。
- 提出一种分类法，帮助理解该领域内不同表征范式间的演进关系。
- 明确指出当前面临的关键挑战，并拟定未来研究议程。

### 局限性
- 摘要未提供足够信息，无法评价实验数据集、定量对比结果或具体性能指标。
- 未提及所综述论文的筛选标准、文献数量或代表性实验结果。

### 阅读优先级
**高**。理由：该综述覆盖了三维场景补全领域从几何建模到最新生成范式（扩散模型、高斯泼溅）的完整演进，且发表于2026年，能提供极新的技术全景和未来方向，适合希望快速了解领域脉络的研究者。

</details>

<details>
<summary>Abstract</summary>

Three-dimensional scene completion has evolved as a major problem in computer vision and robotics, and its applications are diverse, including autonomous navigation and augmented reality. In this study, a systematic review has been conducted to compile the research contributions made in the last ten years, i.e., 2016 to 2026, which has revolutionized the field from the voxel semantic completion paradigm represented by SSCNet to the latest paradigm that combines generative diffusion priors with real-time rendering using a Gaussian splatting technique. The evolution in representation paradigms, such as voxel grids, point learning, implicit neural fields, transformer networks, diffusion networks, and the latest paradigm based on rendering-aware 3D Gaussian primitives, has been discussed in this study. A comprehensive analysis has been carried out on the contributions made in the last ten years, and a taxonomy has been developed to provide a clear idea about the contributions made in the field. The study has also discussed the research contributions made in the field, along with the challenges that still need to be addressed. Finally, the study has presented a research agenda that will provide a clear idea about the directions that can be followed in the development of the next-generation system

</details>

#### 2026-06-23 - Geometry-Aware Style Transfer in 3D Gaussian Splatting

**Authors:** Min Hyeok Bang, Jun Hyeong Kim, Seung-Wook Kim, Se-Ho Lee
**Links:** [abs](https://arxiv.org/abs/2606.24144) - [pdf](https://arxiv.org/pdf/2606.24144)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Geometry-Aware Style Transfer in 3D Gaussian Splatting
- 作者：Min Hyeok Bang, Jun Hyeong Kim, Seung-Wook Kim, Se-Ho Lee
- 出版日期：2026-06-23
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页面：https://arxiv.org/abs/2606.24144；PDF：https://arxiv.org/pdf/2606.24144；代码：https://github.com/oweixx/gast

### 一句话总结
本文提出了一种几何感知的3D高斯泼溅风格迁移框架，通过解耦优化策略同时转移外观和几何结构，解决了现有方法忽视结构适应性的问题。

### 研究问题
如何在3D高斯泼溅风格迁移中同时实现外观属性（如颜色）和几何结构的有效转移，避免颜色与几何更新之间的相互干扰。

### 核心思路/方法
1. 采用解耦优化方案，交替更新颜色和几何参数以减少两者间的干扰。
2. 提出几何感知对比特征匹配（GCFM），整合RGB、深度和边缘线索到对比目标中，用于在优化阶段指导风格图像的结构特征向高斯图元传递。

### 主要贡献
- 首次提出几何感知的3DGS风格迁移框架，显式进行几何结构适应。
- 设计解耦优化策略，实现稳定且一致的场景级几何变换。
- 引入GCFM方法，有效转移风格图像的几何特征。
- 实验表明在定性保真度和定量指标上显著优于现有3DGS风格化方法。

### 局限性
摘要未提供足够信息：未讨论计算开销、对复杂场景的适应性、对风格图像几何特征的依赖程度或泛化边界条件。

### 阅读优先级
高  
理由：该工作直接回应了3DGS风格迁移领域的关键限制（缺乏几何适应），方法清晰（解耦优化+GCFM），且提供了理论与实验支撑（性能显著优于现有方法）。对于关注3D场景编辑、风格迁移或高斯泼溅优化的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

In this paper, we present a novel geometry-aware style transfer framework for 3D Gaussian splatting (3DGS) that simultaneously transfers appearance attributes and geometric structures. Unlike prior works that primarily focus on color-based stylization and often overlook structural adaptation, our method explicitly incorporates geometry adaptation through a decoupled optimization scheme that alternately updates color and geometry parameters. This strategy alleviates potential interference between color and geometry updates, leading to stable and consistent scene-level geometry transformation. The decoupled optimization is enabled by the proposed geometry-aware contrastive feature matching (GCFM). GCFM integrates RGB, depth, and edge cues into a contrastive objective and is employed in both optimization phases to effectively transfer structural characteristics from style images to Gaussian primitives. Extensive experiments show that our approach achieves superior performance in both qualitative fidelity and quantitative metrics, significantly outperforming existing 3DGS-based stylization methods. Our code is available at \href{https://github.com/oweixx/gast}{https://github.com/oweixx/gast}.

</details>

#### 2026-06-22 - Learning Stable Canonical Worlds for Novel View Synthesis and Beyond

**Authors:** Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma
**Links:** [abs](https://arxiv.org/abs/2606.23027) - [pdf](https://arxiv.org/pdf/2606.23027)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Stable Canonical Worlds for Novel View Synthesis and Beyond
- 作者：Xiaoyu Xu, Jian Zou, Sheyang Tang, Zhihua Wang, Jing Liao, Kede Ma
- 出版日期：2026-06-22
- 分类：Neural Scene Representations & Rendering
- 链接：摘要：https://arxiv.org/abs/2606.23027；PDF：https://arxiv.org/pdf/2606.23027

### 一句话总结
本文提出CanonicalGS，一种前馈式高斯泼溅管道，通过将杂乱的视图证据融合到稳定的规范潜在世界中，实现了更鲁棒的新视图合成，并能迁移到下游视觉感知任务。

### 研究问题
当前前馈式高斯泼溅（FFGS）方法依赖视图依赖预测，当输入视图增加时，会积累噪声或冗余证据，而无法收敛到稳定的场景表示。如何将多视图观测映射为稳定、以场景为中心的表示是主要研究问题。

### 核心思路/方法
- 首先从深度、语义特征和不确定性估计中提取每视图的证据。
- 然后利用不确定性感知融合，将这些证据在规范潜在世界中聚合。
- 通过强调可靠观测并抑制不确定或冗余证据，得到可扩展的场景表示。

### 主要贡献
- 提出CanonicalGS管道，将杂乱多视图观测转化为稳定的规范场景表示。
- 在新视图合成上，峰值信噪比提升最高达2.5 dB。
- 在语义分割等下游任务上，准确率提升11%。
- 表明该方法能更有效地随输入视图增加而扩展。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高。理由：该工作直接面向新视图合成这一核心问题，并显示了明确且可量化的性能提升（2.5 dB PSNR和11%语义分割准确率），同时具备跨任务迁移能力，对神经场景表示与渲染方向的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Feed-forward Gaussian splatting (FFGS) facilitates real-time novel view synthesis, yet current methods often remain tied to view-dependent predictions. As more input views are added, they may accumulate noisy or redundant evidence instead of converging to a stable scene representation. In this paper, we introduce CanonicalGS, a feed-forward pipeline that maps cluttered multi-view observations into a stable, scene-centric representation. CanonicalGS first extracts view-centric evidence from depth, semantic features, and uncertainty estimates, and then aggregates this evidence in a canonical latent world using uncertainty-aware fusion. By emphasizing reliable observations while suppressing uncertain or redundant ones, CanonicalGS produces representations that scale more effectively for novel view synthesis and transfer to downstream visual perception tasks. Experiments show up to a $2.5$ dB improvement in peak signal-to-noise ratio for synthesizing novel views and an $11\%$ gain in semantic segmentation accuracy.

</details>

#### 2026-06-21 - Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography

**Authors:** Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang
**Links:** [abs](https://arxiv.org/abs/2606.22525) - [pdf](https://arxiv.org/pdf/2606.22525)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography
- 作者：Yikuang Yuluo, Ao Wang, Shen Kuan, Yujie Liu, Wang Liao, Ying Chen, Shuangyang Zhong, Yixing Huang, Fuquan Wang
- 出版日期：2026-06-21
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2606.22525

### 一句话总结
本文发现稀疏视角三维高斯断层重建中存在投影质量提升但体积重建恶化的“投影-体积保真度发散”问题，并提出名为LADES的无真值优化控制器来解决该漂移。

### 研究问题
稀疏视角计算机断层扫描重建是一个严重病态逆问题，近期3D高斯喷射方法提供了高效显式表示。但研究发现，在投影域优化可能产生误导：渲染投影可能不断改善，而重建的体积却在退化。如何诊断和控制这种表示层面的优化漂移？

### 核心思路/方法
1. 识别故障模式：提出投影-体积保真度发散（PVFD），一种由各向异性高斯变形和稀疏Radon约束下视图特定基元共适应引起的优化漂移。
2. 诊断指标：引入几何和体积层级的诊断方法，测量针状高斯退化和体素化密度场的稳定性。
3. 控制器LADES：包含两个无真值组件——线性退火丢弃（在早期训练时施加强随机掩蔽，破坏过早的基元共适应，再逐步恢复全容量进行结构巩固）和结构感知早停（根据高斯种群增长饱和而非验证PSNR来终止稠密化）。

### 主要贡献
- 识别并形式化了稀疏视角高斯层析中的投影-体积保真度发散（PVFD）故障模式。
- 引入几何和体积层级的诊断工具，用于量化高斯退化与体密度场稳定性。
- 提出无真值优化控制器LADES，能够提高体积保真度、抑制结构退化、大幅减少训练时间，同时保持有竞争力的投影精度。

### 局限性
摘要未提供足够信息。

### 阅读优先级
高  
理由：该工作直接针对稀疏视角3D高斯重建中核心的优化漂移问题，提出新颖的诊断与无真值控制方案，实验显示在体积保真度、训练效率方面有显著改进。对于从事断层重建、神经场景表示或逆向渲染的研究者具有较重要的参考价值，且问题陈述清晰、方法简洁有力。

</details>

<details>
<summary>Abstract</summary>

Sparse-view computed tomography is a severely ill-posed inverse problem, where recent 3D Gaussian Splatting methods offer an efficient explicit representation for tomographic reconstruction. However, we find that projection-domain optimization can be misleading in this setting: the rendered projections may continue to improve while the reconstructed volume deteriorates. We identify this failure mode as Projection-Volume Fidelity Divergence (PVFD), a representation-level optimization drift caused by anisotropic Gaussian deformation and view-specific primitive co-adaptation under sparse Radon constraints. To characterize this behavior, we introduce geometry- and volume-level diagnostics that measure needle-like Gaussian degeneration and the stability of the voxelized density field. Based on these observations, we propose LADES, a ground-truth-free optimization controller for sparse-view Gaussian tomography. LADES combines Linearly Annealed Dropout, which applies strong stochastic masking in early training to disrupt premature primitive co-adaptation and gradually restores full capacity for structural consolidation, with Structure-Aware Early Stopping, which terminates densification according to the saturation of Gaussian population growth rather than validation PSNR. Experiments on sparse-view CT reconstruction show that LADES improves volumetric fidelity, suppresses structural degeneration, and substantially reduces training time while maintaining competitive projection accuracy. These results suggest that robust Gaussian-based tomography requires monitoring and controlling volumetric structure, rather than optimizing projection fit alone.

</details>

## Embodied / Robotics / AR Applications

### 2026-06

#### 2026-06-25 - EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting

**Authors:** Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao
**Links:** [abs](https://arxiv.org/abs/2606.27277) - [pdf](https://arxiv.org/pdf/2606.27277)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting
- 作者：Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hengshuang Zhao
- 出版日期：2026-06-25
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.27277

### 一句话总结
EO-WM 提出了一种物理信息引导的视频扩散Transformer模型，实现了在变化气象条件下对地球观测的多光谱概率预测，并通过两个诊断基准验证了其天气响应预测的准确性。

### 研究问题
如何在不完全观测、天气驱动的地球观测预测任务中，构建能捕捉预测不确定性并对气象强迫变化做出正确响应的世界模型。

### 核心思路/方法
1. **视角转换**：将EO预测视为部分观测、天气驱动的世界建模问题，气象信号作为条件，但由于观测稀疏和地表状态不可观测而存在不确定性。
2. **物理信息条件框架**：将气象强迫分解为气候基线、天气异常和累积物理应力（如持续热浪或干旱应力）信号，并通过不同的条件路径注入模型。
3. **模型架构**：采用视频扩散Transformer（Video Diffusion Transformer）作为基础，结合上述条件信号生成概率性多光谱预测。
4. **诊断基准**：设计了极端夏季基准（评估极端天气下植被退化预测的严重程度感知）和季节匹配对基准（测试不同天气强迫下的响应保真度）。

### 主要贡献
1. 提出了EO-WM模型，将物理信息条件框架引入视频扩散Transformer，实现概率性EO预测。
2. 引入两个新基准来评估模型对气象变化的正确响应行为，超越传统重建精度指标。
3. 实验显示，在预测NDVI下降幅度误差上相对降低5.63%，方向命中率相对提升7.80%，同时保持标准像素级指标的竞争力。

### 局限性
摘要未提供关于计算资源、数据依赖、模型泛化性、失败案例或潜在偏差等信息。未能基于摘要确定模型在无极端天气或低质量数据下的表现。

### 阅读优先级
**高**
理由：该论文针对地球观测预测中一个关键但未被充分建模的问题（天气驱动的不确定性响应），提出了有理论依据的方法和评估基准，并在核心指标上取得显著提升，对遥感与气候应用领域具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Earth Observation (EO) forecasting aims to predict future Earth surface dynamics from satellite observations under changing meteorological conditions. In this paper, we view this task as a partially observed, weather-driven world modeling problem, in which weather acts as a conditioning signal, while forecasting remains uncertain due to sparse observations and unobserved land-surface states. However, existing methods do not fully capture this setting: deterministic models collapse uncertainty into a single future prediction, while diffusion-based methods typically treat weather variables as undifferentiated conditioning signals, and existing benchmarks focus mainly on reconstruction accuracy rather than whether forecasts respond correctly to changed weather forcing.We introduce EO-WM, a video diffusion transformer for multispectral EO forecasting. EO-WM incorporates a physically informed conditioning framework that represents meteorological forcing through a climatological baseline, weather anomalies, and cumulative physical stress signals. Specifically, it separates baseline and anomaly through distinct conditioning pathways, and accumulates anomalous forcing over time to capture sustained heat and drought stress. To evaluate weather-response behavior beyond standard metrics, we introduce two diagnostic benchmarks: an Extreme Summer Benchmark for severity-aware prediction of vegetation degradation under extreme weather, and a Seasonal Matched-Pair Benchmark for testing response fidelity under changed weather forcing. Experiments show that EO-WM reduces the error in predicted Normalized Difference Vegetation Index (NDVI) decline amplitude by a relative 5.63% and improves directional hit rate by a relative 7.80%, while remaining competitive on standard pixel-level metrics. The benchmarks and model will be made open-source at https://github.com/Luo-Z13/EO-WM.

</details>

#### 2026-06-25 - UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping

**Authors:** Feng Pan, Chunran Zheng, Bing Xue, Yukang Cui, Jiayu Wen, Zhiyu Chen, Wei Wang
**Links:** [abs](https://arxiv.org/abs/2606.26928) - [pdf](https://arxiv.org/pdf/2606.26928)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UAV-MapFusion: RTK-Aligned Uncertainty-Aware Coarse-to-Fine Multi-Session UAV Mapping
- 作者：Feng Pan, Chunran Zheng, Bing Xue, Yukang Cui, Jiayu Wen, Zhiyu Chen, Wei Wang
- 出版日期：2026-06-25T12:03:29Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要: https://arxiv.org/abs/2606.26928, PDF: https://arxiv.org/pdf/2606.26928

### 一句话总结
本文提出一种利用RTK对准和不确定性感知因子图的多会话无人机点云地图粗到细优化系统，以解决大范围地图合并中长距离漂移与局部几何精度难以兼顾的问题。

### 研究问题
如何在大规模多会话无人机点云地图合并中，同时抑制长距离漂移并保持局部几何精度。

### 核心思路/方法
1. **初始合并**：基于场景图对多会话地图进行粗对齐。
2. **RTK时空对齐**：使用动态时间规整（DTW）估计时间偏移，并利用多输出高斯过程（MOGP）在不完整采样和帧丢失下恢复连续RTK约束。
3. **不确定性感知因子图**：将RTK约束与不确定性信息整合到统一的因子图中。
4. **局部优化**：通过迭代平面因子优化提升局部几何精度。

### 主要贡献
- 提出一种面向无人机场景的多会话点云地图合并系统，结合RTK对准与粗到细优化。
- 引入DTW和MOGP处理RTK数据的时空对齐问题，提升长距离稳定性。
- 利用不确定性感知因子图和平面因子细化同时提高全局一致性与局部精度。

### 局限性
- 摘要未提供具体的实验场景参数（如数据集大小、飞行时长、对比基线等），也未详细说明失败案例或假设条件，因此局限性信息不足。

### 阅读优先级
阅读优先级：中。  
理由：该方法针对无人机大范围地图合并的实用技术问题，思路明确且包含多种创新模块（如DTW、MOGP、不确定性因子图），适合对多传感器融合或地图建图感兴趣的读者；但摘要中未提供详细实验结果，若需深入评估效果需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Large-scale point cloud maps are essential for robotics and spatial intelligence tasks. UAVs provide an efficient means for large-scale map acquisition; however, due to limited flight endurance and onboard storage, mapping a large-scale scene within a single flight remains difficult. Existing multi-session map merging methods can extend the mapping range, yet in UAV scenarios they still struggle to simultaneously suppress long-range drift and preserve local geometric accuracy. To address this issue, an uncertainty-aware multi-session point cloud map merging and coarse-to-fine optimization system is proposed. The proposed method first performs initial multi-session map merging based on a scene graph, and then incorporates RTK observations through an RTK spatiotemporal alignment module, where temporal offsets are estimated using Dynamic Time Warping (DTW), and continuous RTK constraints are recovered using Multi-Output Gaussian Processes (MOGP) under incomplete sampling and frame dropouts. On this basis, a unified uncertainty-aware factor graph is constructed, and local geometric accuracy is further improved through iterative plane-factor refinement. Experiments on real-world datasets validate the effectiveness and robustness of the proposed method. To facilitate further research and development in the community, our code and dataset will be publicly released.

</details>

#### 2026-06-25 - OSC2Runner: OpenSCENARIO 2.x Compliant High-Fidelity AV Simulation in CARLA

**Authors:** Thoshitha Gamage, Lasanthi Gamage
**Links:** [abs](https://arxiv.org/abs/2606.26533) - [pdf](https://arxiv.org/pdf/2606.26533)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OSC2Runner: OpenSCENARIO 2.x Compliant High-Fidelity AV Simulation in CARLA
- 作者：Thoshitha Gamage, Lasanthi Gamage
- 出版日期：2026-06-25
- 分类：具身/机器人/AR应用
- 链接：arXiv abs: https://arxiv.org/abs/2606.26533

### 一句话总结
OSC2Runner是首个能在CARLA仿真器中原生执行OpenSCENARIO v2.x DSL的编排框架，通过多遍转译器将场景描述编译为行为树，实现了精确的确定性仿真。

### 研究问题
现有连续仿真框架缺乏对新兴ASAM OpenSCENARIO v2.x DSL的原生支持，导致基于场景的测试在运行v2.x逻辑时出现时空漂移、异步事件延迟及人工运动突变等问题，亟需一种能高保真执行v2.x场景的仿真方法。

### 核心思路/方法
该框架将场景翻译形式化为编译流水线，采用多遍转译器架构，将类型安全的抽象语法树直接合成为动态确定性行为树（基于py_trees），并将其原生映射到CARLA的原子API，从而绕过静态轨迹回放，实现实时交互式执行。

### 主要贡献
1. 提出首个原生映射OpenSCENARIO v2.x DSL到CARLA的编排框架，填补v2.x执行空白。
2. 设计多遍转译器架构，实现从DSL到行为树的确定性编译。
3. 在高并发对抗工况实验中验证了逐刻确定性、精确的空间触发评估及100.0毫秒级跨参与者黑板同步，且运动学分析证实严格遵循连续环境边界。

### 局限性
摘要未提供足够信息：未明确讨论框架的计算开销、对复杂场景的扩展性、与OpenSCENARIO其他版本或第三方仿真器的兼容性，以及未提供可复现性的详细实验配置。

### 阅读优先级
低。理由：论文聚焦于自动驾驶仿真工具链的特定执行一致性问题（OpenSCENARIO v2.x与CARLA集成），对于非该领域（如场景测试工具开发或高保真仿真技术）的读者，其技术贡献的泛化性有限；且摘要未提供充分的性能对比基准或开放实现细节，难以评估其实用价值。

</details>

<details>
<summary>Abstract</summary>

Scenario-Based Testing predominantly relies on the legacy ASAM OpenSCENARIO 1.x XML standard because existing continuous simulation frameworks lack native execution support for the recently matured v2.x Domain-Specific Language (DSL). Adapting legacy interpreters to evaluate v2.x logic introduces spatiotemporal drift, asynchronous event latencies, and artificial kinematic snapping. Addressing this execution gap, OSC2Runner introduces the first orchestration framework capable of natively mapping the OpenSCENARIO v2.x DSL to CARLA. The framework achieves this by formalizing scenario translation as a compilation pipeline through a multi-pass transpiler architecture. Bypassing static trajectory playback, the architecture synthesizes type-safe Abstract Syntax Trees directly into dynamic deterministic behavior trees (py_trees) natively mapped to CARLA's atomic APIs. Empirical validation in highly concurrent adversarial case studies demonstrates tick-by-tick determinism, exact spatial trigger evaluation, and 100.0 ms cross-actor blackboard synchronization. Kinematic analysis proves the strict adherence to continuous environmental boundaries. This architecture transitions Scenario-Based Testing from approximate behavioral interpretation to mathematically rigorous execution, establishing the deterministic backend required for co-simulation, hardware-in-the-loop testing, and automated LLM-driven generation pipelines.

</details>

#### 2026-06-24 - KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation

**Authors:** Runfeng Ling
**Links:** [abs](https://arxiv.org/abs/2606.26321) - [pdf](https://arxiv.org/pdf/2606.26321)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KRVF: A Source-Aware Semantic Voxel World Representation for Edge Mobile Manipulation
- 作者：Runfeng Ling
- 出版日期：2026-06-24T19:07:42Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2606.26321；PDF链接 https://arxiv.org/pdf/2606.26321

### 一句话总结
本文提出了KRVF，一种面向边缘端移动机械臂的、具有来源感知的语义体素世界表示方法，用于在线构建任务导向的机器人记忆。

### 研究问题
如何在边缘计算约束下，为移动机械臂构建一个当前、可查询、具有语义意义且可用于任务操作的世界模型，特别是解决传统重建导向方法在语义推理和传感器失效场景下的不足。

### 核心思路/方法
KRVF将局部世界状态表示为任务导向的体素，每个体素编码占用情况、颜色、语义证据、时间新鲜度和证据来源。该表示分离了测量占用与语义先验假设，实现了对深度失效敏感的物体推理，同时避免破坏持久几何。此外，KRVF通过渲染地图先验深度来修复缺失数据，形成建图与感知间的反馈回路，并暴露语义物体与抓取候选的任务级查询算子。

### 主要贡献
1. 提出了KRVF表示法，将体素明确记录证据来源（source-aware），区分了测量与语义先验，支持深度失效感知的物体推理。
2. 设计了建图-感知反馈回路，通过地图先验深度修复提升感知鲁棒性。
3. 提供了任务级查询接口，直接支持语义物体搜索与抓取候选生成。
4. 在ROS 2中实现了在线RGB-D观测到任务导向机器人记忆的转换系统。

### 局限性
摘要未提供足够信息，未讨论实验验证、数据集、性能指标或与现有方法的定量对比。

### 阅读优先级
低。理由：该技术报告仅形式化提出了KRVF表示与系统设计，但摘要中缺乏实验评估和基线对比，无法判断方法在实际任务中的有效性与效率。若对边缘端机器人语义建图感兴趣可作参考，但需等待后续验证。

</details>

<details>
<summary>Abstract</summary>

Mobile manipulators need world models that are current, queryable, semantically meaningful, and usable under edge-compute constraints. This technical report presents KRVF, a source-aware semantic voxel world representation for edge mobile manipulation. Unlike reconstruction-centric mapping pipelines that primarily optimize global geometric fidelity, KRVF represents local world state as task-oriented voxels that encode occupancy, color, semantic evidence, temporal freshness, and evidence source. The representation separates measured occupancy from semantic-prior hypotheses, enabling depth-failure-aware object reasoning without silently corrupting persistent geometry. KRVF also closes a feedback loop between mapping and sensing by rendering map-prior depth for repair, and exposes task-level query operators for semantic objects and grasp candidates. The report formalizes the KRVF representation and documents a ROS 2 implementation that turns online RGB-D observations into a task-facing robot memory.

</details>

#### 2026-06-24 - RoboAtlas: Contextual Active SLAM

**Authors:** Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
**Links:** [abs](https://arxiv.org/abs/2606.26046) - [pdf](https://arxiv.org/pdf/2606.26046)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, mapping, simulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoboAtlas: Contextual Active SLAM
- 作者：Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications（主要），3D Reconstruction & Multi-view Geometry（次要）
- 链接：摘要 [https://arxiv.org/abs/2606.26046](https://arxiv.org/abs/2606.26046) | PDF [https://arxiv.org/pdf/2606.26046](https://arxiv.org/pdf/2606.26046)

### 一句话总结
RoboAtlas是一个上下文感知的主动SLAM框架，通过结合几何探索、全局语义地图推理和基于VLM的自我中心推理，并利用上下文多臂赌博机在探索与语义导航之间动态切换，实现了大规模真实场景下高效、鲁棒的语义导航任务。

### 研究问题
如何在大规模、多语义实例的真实环境中，使机器人自适应地平衡几何探索与语义推理，以实现基于上下文感知的高效主动SLAM？

### 核心思路/方法
1. **系统框架**：RoboAtlas结合了前沿探索、全局语义地图推理（基于OpenRoboVox 3D语义映射系统）和基于VLM的自我中心推理。
2. **决策机制**：通过一个**上下文多臂赌博机**（contextual multi-armed bandit）来动态调整行为：当场景理解不足时偏向探索，随着语义理解提升，逐渐过渡到语义引导的导航。
3. **评估**：在仿真和真实Unitree Go2机器人上测试（环境超过1800 m²，约3万语义实例），并在GOAT-Bench“Val Unseen”基准上对比，验证了高性能。

### 主要贡献
1. 提出了RoboAtlas，一种上下文主动SLAM框架，能自适应平衡几何探索与语义推理。
2. 在GOAT-Bench“Val Unseen”基准上，使用GPT-4o时达到**90.6%的成功率（SR）**，比先前最强基线提升17.8个百分点；即使使用更小的Qwen2.5-VL-7B模型（88.8% SR），仍优于所有使用GPT-4o的基线，**揭示了3D语义映射框架带来的信息增益比单纯替换基础模型更为重要**。
3. 在真实大规模环境（1800 m²，约3万语义实例）中实现**100%任务成功率**，验证了系统在现实世界中的鲁棒性和效率。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作在主动SLAM领域提出了创新的上下文自适应框架，并在标准基准和大规模真实场景上取得了显著优于现有方法的性能（特别是揭示了语义地图框架对基础模型性能的关键提升作用），对机器人导航、语义推理领域的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.

</details>

#### 2026-06-24 - From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response

**Authors:** Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
**Links:** [abs](https://arxiv.org/abs/2606.25957) - [pdf](https://arxiv.org/pdf/2606.25957)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response
- 作者：Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25957

### 一句话总结
本文提出利用无人机搭载量子磁力计，通过仿真与主动采样重建坍塌建筑内部磁性结构，以辅助灾后搜救。

### 研究问题
如何在灾后72小时黄金救援期内，通过无人机搭载量子磁力计，有效感知坍塌建筑（钢混结构）内部的磁性结构，定位幸存者或空洞。

### 核心思路/方法
1. **仿真管道**：使用Unreal Engine生成钢混停车库坍塌场景，通过每个三角形的偶极子近似计算诱导磁场，验证在屋顶上方约1米处可恢复亚pT到亚nT量级的磁信号。
2. **传感器部署**：评估不同传感器阵列（重点为三传感器阵列）在梯度分辨率与无人机载荷约束间的权衡。
3. **主动重建**：采用高斯过程回归作为后端，结合贝叶斯主动采样策略，从稀疏多传感器样本中重建空间磁场结构，并用多个独立坍塌实例验证管道有效性。

### 主要贡献
1. 提出将量子级磁力计作为灾后搜救的补充传感模态，并构建完整的“坍塌仿真→传感器部署→主动重建”管道。
2. 通过仿真证明，在约1米距离外可检测到有意义的磁性结构（亚pT至亚nT范围）。
3. 三传感器阵列可在梯度分辨率与载荷约束间取得最优平衡，且主动采样在约100个样本点内达到峰值结构相关性。

### 局限性
摘要未提供足够信息。具体局限性包括但不限于：仿真环境与真实倒塌场景的差异、量子磁力计在户外实际部署的鲁棒性、对不同类型建筑废墟的适应性以及算法计算复杂度等均未在摘要中提及。

### 阅读优先级
**高**。理由：本文针对灾害救援这一紧迫应用场景，提出新颖的量子磁力计+主动采样方案，方法设计完整（仿真→部署→重建），且结果量化明确（三传感器最优、100样本收敛）。对于关注量子传感、搜救机器人或主动感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Locating survivors of building collapses within the first 72 hours is a critical challenge in disaster response, and existing sensing modalities provide only partial information about the structure beneath the rubble. This paper proposes drone-based quantum magnetometry as a complementary modality and develops a simulation pipeline spanning rubble physics, sensor-array deployment, and active spatial reconstruction. We use Unreal Engine to generate a steel-reinforced concrete parking-garage collapse and compute the induced magnetic field via a per-triangle dipole approximation, establishing that meaningful magnetic structure is recoverable in the sub-pT to sub-nT range from roughly 1 m above the roofline. Then, we feed sparse multi-sensor samples into a Gaussian Process Regression back-end driven by Bayesian active sampling and validate the pipeline across multiple independent collapse realizations; a three-sensor array optimizes the trade-off between gradient resolution and UAV payload constraints, and active sampling reaches peak structural correlation in roughly $100$ samples. Together, these results indicate that quantum-grade sensing could become a useful tool for drone-based structural analysis and potentially void detection in collapsed buildings.

</details>

#### 2026-06-24 - DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild

**Authors:** Ahmad Kourani, Ghina Daoud, Daniel Asmar, Imad Elhajj
**Links:** [abs](https://arxiv.org/abs/2606.25953) - [pdf](https://arxiv.org/pdf/2606.25953)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, manipulation, autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DSP-SLAM++: A Unified Framework for Multi-Class, High-Fidelity Object SLAM in the Wild
- 作者：Ahmad Kourani, Ghina Daoud, Daniel Asmar, Imad Elhajj
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications（主类），3D Reconstruction & Multi-view Geometry（次类）
- 链接：摘要网址：https://arxiv.org/abs/2606.25953；PDF网址：https://arxiv.org/pdf/2606.25953

### 一句话总结
DSP-SLAM++ 通过异步建图流水线和传感器融合适配，在保持实时性的同时支持多类物体高保真建模，将物体SLAM推向实际应用。

### 研究问题
现有面向物体的SLAM系统在实时性能、多类别支持和高保真语义连贯物体模型生成之间存在权衡，缺乏统一的解决方案。

### 核心思路/方法
- 扩展 DSP-SLAM 框架，引入异步建图流水线，实现实时性能。
- 针对单目鱼眼-激光雷达（monocular fisheye-LiDAR）组合进行专用传感器融合适配。
- 通过异步处理消除建图线程瓶颈，显著降低物体处理延迟。

### 主要贡献
1. 提出统一框架DSP-SLAM++，同时支持多类别物体高保真建模和实时运行。
2. 设计了异步建图流水线，将最大物体处理延迟相比现有最优基线降低70%，支持25Hz多类别数据集的鲁棒实时运行。
3. 针对单目鱼眼-激光雷达传感器套件进行适配，使高保真多类物体SLAM在自动驾驶等室外场景中更实用，并开源代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对物体SLAM领域的关键权衡问题（实时性、多类支持、高保真度）提出了改进方案，量化指标明确（延迟降低70%，支持25Hz数据集），且开源代码，对从事机器人、自动驾驶等实际应用的读者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing object-aware SLAM systems force a trade-off between real-time performance, multi-class support, and the generation of high-fidelity, semantically coherent object models. To address this trade-off, we present DSP-SLAM++, which extends the DSP-SLAM framework with an asynchronous mapping pipeline for real-time performance and dedicated sensor fusion adaptations for a monocular fisheye-LiDAR suite. Experiments demonstrate that our system generates fine-grained, geometrically-complete shapes for multiple object classes while eliminating severe mapping thread bottlenecks by reducing maximum object processing latency by up to 70\% compared to the state-of-the-art baseline, enabling robust, real-time performance on a challenging 25 Hz multi-class datasets. This work makes high-fidelity, multi-class object SLAM more practical for real-world applications like autonomous driving and robotic manipulation by enabling its use on platforms with common fisheye-LiDAR sensor setups. The open-source code is available at: [github.com/AUBVRL/DSP-SLAMpp].

</details>

#### 2026-06-24 - MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework

**Authors:** Qiyang Lyu, Zhenyu Wu, Wei Wang, Hongming Shen, Danwei Wang
**Links:** [abs](https://arxiv.org/abs/2606.25796) - [pdf](https://arxiv.org/pdf/2606.25796)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework
- 作者：Qiyang Lyu, Zhenyu Wu, Wei Wang, Hongming Shen, Danwei Wang
- 出版日期：2026-06-24
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25796

### 一句话总结
本文提出了一种磁力计-惯性-LiDAR融合的多模态定位框架MIL-LC，旨在解决GNSS拒止、几何重复或纹理缺失环境中自主移动机器人的鲁棒定位问题，通过引入环境磁场作为补充模态，在LiDAR退化或长期部署中磁场变化时仍能保持可靠定位。

### 研究问题
如何实现自主移动机器人在挑战性环境（如GNSS拒止、几何重复、纹理缺失的办公室、酒店、地下停车场）中的鲁棒定位，克服单模态传感器限制以及现有多模态融合框架对几何/纹理特征或基础设施信标的过度依赖。

### 核心思路/方法
提出MIL-LC框架，融合磁力计、惯性测量单元和LiDAR数据，并采用自定义传感器套件。利用环境磁场（AMF）作为不依赖几何/纹理特征、无需额外基础设施的互补模态，解决LiDAR几何退化或长期部署中磁图变化时的定位问题。通过仿真和真实环境实验验证框架的鲁棒性和准确性。

### 主要贡献
1. 提出首个面向自主移动机器人的磁力计-惯性-LiDAR融合定位框架MIL-LC，填补了该场景下AMF融合研究的空白。
2. 设计自定义传感器套件，使框架在LiDAR几何退化或长期部署中磁图变化时仍能提供可靠定位。
3. 通过仿真和真实环境实验证明MIL-LC框架的鲁棒且准确的定位性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作聚焦于机器人定位领域的实际工程难题（几何退化、磁图变化），方法新颖（AMF融合），但摘要中实验细节和性能量化数据不足，限于具体应用场景（AMR），对跨领域读者启发性有限。

</details>

<details>
<summary>Abstract</summary>

Localization in challenging environments, such as GNSS-denied, geometrically repetitive, or textureless scenes commonly found in offices, hotels, and underground parking facilities, remains an open problem for reliable autonomous mobile robot (AMR) deployment. Single-modality localization methods are inherently limited by the constraints of individual sensors. Although multimodal fusion frameworks have shown improved robustness, most existing approaches still rely heavily on geometric or texture features, or on infrastructure-based beacons, which increase installation and maintenance costs while reducing deployment flexibility. Recently, ambient magnetic field (AMF)-based localization has attracted growing attention because it does not depend on geometric or texture features, nor does it require additional infrastructure, making it a promising complementary modality for AMR localization. However, existing studies have only explored such fusion in pedestrian scenarios using smartphone-mounted sensor suites, and practical solutions for AMR systems remain largely unexplored. To address this gap, this article proposes a magnetometer-inertial-LiDAR fused multimodal localization framework with a custom-designed sensor suite, termed MIL-LC, which provides reliable localization even when LiDAR suffers from geometric degeneration or when the magnetic map changes during long-term deployment. Extensive experiments in both simulation and real-world environments demonstrate that the proposed MIL-LC framework achieves robust and accurate localization performance.

</details>

#### 2026-06-23 - fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation

**Authors:** Christian Fronk, Hanting Ye, David Hunt, Miroslav Pajic, Maria Gorlatova
**Links:** [abs](https://arxiv.org/abs/2606.25162) - [pdf](https://arxiv.org/pdf/2606.25162)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, AR, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：fARfetch: Enabling Collocated AR-HRC in Large Visually Diverse Environments with VLM-Driven AR Content Adaptation
- 作者：Christian Fronk, Hanting Ye, David Hunt, Miroslav Pajic, Maria Gorlatova
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.25162

### 一句话总结
fARfetch 是一个面向大型、视觉多样环境的增强现实-人机协作（AR-HRC）系统，通过语义地图、缩微世界表示和视觉语言模型（VLM）驱动的AR内容自适应，显著提升了户外大空间内协作任务的效率和内容可读性。

### 研究问题
如何在大型、视觉多样（如户外）环境中，解决增强现实人机协作（AR-HRC）中因长距离和视线受阻导致的交互困难与虚拟内容可读性下降问题。

### 核心思路/方法
系统集成了三个关键组件：
1. **共享语义环境地图**：AR头显与机器人共同构建并可视化检测到的地标，支持基于地标的“前往”指令。
2. **上下文感知的缩微世界表示**：为精细路径规划提供共环境的小型化、全景式抽象视图。
3. **VLM驱动的AR视图管理**：联合调整虚拟内容的颜色、大小和方向，以在大型视觉多样环境中保持内容可读性。

系统基于Meta Quest 3头显和Unitree Go2四足机器人实现，并在真实户外大尺度（30.5米）巡检任务中开展了12名用户的受试者内实验。

### 主要贡献
- 提出一套完整的AR-HRC系统，整合了语义地图、缩微世界和VLM内容自适应，适用于大型、视觉多样环境。
- 通过用户实验验证：相比无AR基线，fARfetch显著提升任务完成时间（快66%），并降低了脑力负荷（-43%）、时间需求（-34%）和挫败感（-66%）。
- 定制可读性调查表明，系统在大尺度户外环境中能有效保持虚拟内容的可读性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对实际户外大空间人机协作的明确痛点（内容可读性、交互效率），提出了新颖的VLM驱动自适应方法，并附有显著量化的用户实验证据，对AR-HRC领域的研究者和从业者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Augmented Reality (AR) can improve collocated human-robot collaboration by making robot state and intent visible and enabling intuitive control, yet large, visually diverse environments like the outdoors challenge both interaction and content legibility, especially at long distances and beyond visual line of sight. We present fARfetch, an AR-HRC system that integrates (i) shared semantic environment mapping across an AR headset and robot that visualizes detected landmarks in AR to support landmark-grounded go-to commands, (ii) a context-aware world-in-miniature representation of the shared environment for fine-grained path authoring, and (iii) vision-language-model driven AR view management that jointly adapts virtual content color, size, and orientation to maintain legibility in large visually diverse environments. We implement fARfetch with a Meta Quest 3 headset and Unitree Go2 quadruped robot, and conduct a within-subjects user study (N=13) on a real-world large-scale (30.5m) outdoor inspection task. fARfetch yielded significantly faster completion times than a non-AR baseline (66%) and significantly lower workload in mental demand (-43%), temporal demand (-34%), and frustration (-66%). A custom legibility survey indicated fARfetch effectively maintained virtual content legibility in the large outdoor environment.

</details>

#### 2026-06-23 - Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics

**Authors:** Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
**Links:** [abs](https://arxiv.org/abs/2606.24814) - [pdf](https://arxiv.org/pdf/2606.24814)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Vision-Language Model Reasoning for Contextual Semantic Mapping in Intralogistics
- 作者：Marvin Rüdt, Hao Pang, Constantin Enke, Zäzilia Seibold, Kai Furmans
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24814

### 一句话总结
本文提出了一种结合SLAM、SAM、实例聚类和VLM多视角推理的管道，用于在内部物流环境中生成包含几何结构、物体类别和可移动性信息的上下文语义地图，无需任务特定训练。

### 研究问题
如何使仅依赖几何地图的自主移动机器人获得对物体及其上下文属性（如可移动性）的语义理解，并构建支持上下文感知过滤的语义地图。

### 核心思路/方法
- 结合SLAM（同步定位与地图构建）进行几何建图，SAM（分割一切模型）进行实例分割，实例聚类对同一物体进行聚合，以及VLM（视觉-语言模型）多视角推理。
- 通过聚合多视角观测并在零样本、开放词汇设置下查询VLM，推断物体上下文属性（本文以可移动性为例）。
- 采用两种提示策略评估三种VLM，并进行组件级分析。

### 主要贡献
- 提出一种无需任务特定训练或预定义物体类别的上下文语义地图构建管道。
- 在语义分类上达到98.93%的mIoU，在物体可移动性估计上达到89.17%的mAcc。
- 通过组件分析揭示了VLM推理是上下文理解的主要瓶颈，实例聚类是全景性能的主要限制。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该研究针对内部物流中移动机器人的实际需求，提出了一种结合SLAM、SAM和VLM的创新管道，取得了非常高的语义分类性能（98.93% mIoU），并提供了详细的组件瓶颈分析，对机器人语义建图领域有直接参考价值。论文发表于2026年，技术方法新颖。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots operating in intralogistics environments rely on geometric maps for localization and navigation, but lack semantic understanding of objects and their contextual properties. We present a contextual semantic mapping pipeline that combines SLAM-based geometric mapping, SAM-based instance segmentation, instance clustering, and VLM multi-view reasoning to produce a contextual semantic map representation encoding geometric structure, object class, and object movability. By aggregating observations across multiple viewpoints and querying a VLM in a zero-shot, open-vocabulary setting, the pipeline infers contextual object properties--here demonstrated through movability--without requiring task-specific training or predefined object categories. We evaluate three VLMs under two prompting strategies and conduct a component-wise analysis of the pipeline. The proposed pipeline achieves 98.93 % mIoU for semantic classification and 89.17 % mAcc for object movability estimation. Component analysis identifies VLM reasoning as the primary bottleneck for contextual understanding and instance clustering as the main limitation for panoptic performance. The resulting semantic map supports context-aware filtering and robust navigation in dynamic intralogistics environments.

</details>

#### 2026-06-23 - Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization

**Authors:** Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
**Links:** [abs](https://arxiv.org/abs/2606.24767) - [pdf](https://arxiv.org/pdf/2606.24767)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, embodied AI, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Compact Object-Level Representations with Open-Vocabulary Understanding for Indoor Visual Relocalization
- 作者：Zhaopeng Cui, Jiarui Hu, Jingbo Liu, Boming Zhao, Xiyue Guo, Boyin Feng, Haocheng Peng, Yujun Shen, Hujun Bao, Guofeng Zhang
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24767

### 一句话总结
本文提出OpenReLoc，一种利用开放词汇语义理解的紧凑目标级表示进行室内视觉重定位的系统，通过结合多模态语义匹配、目标参考框架和形状引导的损失函数实现高精度相机定位。

### 研究问题
如何组织场景中的丰富的对象信息（包括语义、布局和几何），构建结构化地图表示，并仅使用对象单元驱动相机重定位任务，同时提升场景理解能力和定位精度。

### 核心思路/方法
1. 利用预训练基础模型，引入多模态机制融合开放词汇语义知识，实现有效的2D-3D对象匹配。
2. 设计面向对象的参考框架作为位置先验，并基于Distance-IoU（DIOU）提出参考框架选择策略，支持可扩展场景。
3. 提出双路径2D迭代最近像素损失（Iterative Closest Pixel loss），并利用对象形状指导，确保稳定准确的位姿优化。

### 主要贡献
1. 首次探索仅使用对象单元构建结构化地图表示并驱动相机重定位任务。
2. 提出OpenReLoc系统，结合开放词汇语义理解与目标级表示，增强可解释性和实用性。
3. 在多个数据集上验证了重定位召回率和精度的优越性能。

### 局限性
摘要未提供足够信息。

- 缺少关于计算效率、实时性、泛化能力或失败案例的具体分析。
- 未提及对复杂场景（如光照变化、动态目标）的鲁棒性评估。
- 未说明开放词汇模型的具体选择、训练细节或消融实验结果。

### 阅读优先级
中

理由：该工作聚焦室内视觉重定位任务，结合了开放词汇语义理解与目标级表示，思路新颖且实验结果优秀。但论文仍在预印本阶段（2026年6月发布），摘要简洁，未提供可复现的细节，需待公开代码和完整论文以评估其实用价值。对相关领域研究者而言具有参考意义，但非紧急必读。

</details>

<details>
<summary>Abstract</summary>

Indoor visual relocalization plays a critical role in emerging spatial and embodied AI applications. However, prior research was predominantly devoted to low-level vision schemes, struggling to perceive scene semantics and compositions, which limits both interpretability and applicability. In this paper, we explore the issue of how to organize rich object information in a scene, including semantics, layout, and geometry, into a structured map representation, thereby utilizing object units exclusively to drive the camera relocalization task. To this end, we propose OpenReLoc, a camera relocalization system designed to provide scene understanding and accurate pose estimation capabilities. Leveraging recent foundation models, we first introduce a multi-modal mechanism to integrate open-vocabulary semantic knowledge for effective 2D-3D object matching. Additionally, we design object-oriented reference frames as position priors, paired with a reference frame selection strategy based on the Distance-IoU (DIOU), enabling extension to scalable scenes. Moreover, to ensure stable and accurate pose optimization, we also propose a dual-path 2D Iterative Closest Pixel loss guided by object shape. Experimental results demonstrate that OpenReLoc achieves superior relocalization recall and accuracy across various datasets. Our source code will be released upon acceptance.

</details>

#### 2026-06-23 - UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving

**Authors:** Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, Yun Ye
**Links:** [abs](https://arxiv.org/abs/2606.24759) - [pdf](https://arxiv.org/pdf/2606.24759)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, driving scene, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：UniDrive: A Unified Vision-Language and Grounding Framework for Interpretable Risk Understanding in Autonomous Driving  
- 作者：Xiaowei Gao, Pengxiang Li, Yitai Cheng, Ruihan Xu, James Haworth, Stephen Law, Yun Ye  
- 出版日期：2026-06-23  
- 分类：Embodied / Robotics / AR Applications  
- 链接：https://arxiv.org/abs/2606.24759  

### 一句话总结  
UniDrive提出了一种融合时间推理与高分辨率感知的统一视觉-语言框架，用于自动驾驶中的可解释风险理解，在DRAMA-Reasoning基准上取得了最优性能，并展现了良好的小目标定位与零样本泛化能力。

### 研究问题  
现有自动驾驶场景理解方法在时间推理（处理多帧动态）与空间精度（定位细粒度风险目标）之间存在权衡，导致对小型、远处或部分遮挡的危害识别不足，且语言驱动的模型解释缺乏接地证据。

### 核心思路/方法  
- 设计双分支架构：**时间推理分支**从多帧输入建模场景动态；**高分辨率感知分支**从最新帧保留细粒度空间细节。  
- 通过**门控交叉注意力融合模块**整合两个分支，将动态上下文与精确空间证据对齐。  
- 基于融合表示，联合生成自然语言风险描述和风险对象的接地边界框输出。

### 主要贡献  
- 提出UniDrive统一框架，同时实现时间语义与高分辨率感知的显式结合。  
- 在DRAMA-Reasoning验证集上取得最优整体性能，在小目标定位中表现突出。  
- 零样本泛化到NuScenes和BDD100K数据集，且获得人类评级的可解释性与可信度提升。

### 局限性  
摘要未提供足够信息，未说明框架的计算开销、失败案例或性能边界（如极端天气、密集交通等场景下的表现）。

### 阅读优先级  
**高**  
理由：该工作直接针对自动驾驶中可解释风险理解的核心难点（时空权衡），提出明确的双分支融合方案，实验展示了多基准优势与零样本泛化能力，代码已开源，适合希望跟进统一视觉-语言 grounding 框架的研究者或工程实践者。

</details>

<details>
<summary>Abstract</summary>

Recent multimodal large language models (MLLMs) have shown strong potential for autonomous driving scene understanding, yet existing methods still face a fundamental trade-off between temporal reasoning and spatial precision. Models that rely on single-frame or low-resolution inputs often miss small, distant, or partially occluded hazards, while language-centric driving models frequently provide limited grounded evidence for their explanations. To address this gap, we propose UniDrive, a unified visual-language and grounding framework for interpretable risk understanding in autonomous driving. UniDrive combines a temporal reasoning branch that models scene dynamics from multi-frame visual input with a high-resolution perception branch that preserves fine-grained spatial details from the latest frame. The two branches are integrated through a gated cross-attention fusion module, enabling dynamic context to be aligned with precise spatial evidence. Based on the fused representation, UniDrive jointly generates natural-language risk descriptions and grounded bounding-box outputs for risk objects. Experiments on the DRAMA-Reasoning benchmark show that UniDrive outperforms representative image-based and video-based baselines in both captioning and risk-object grounding. In particular, UniDrive achieves the best overall performance on the validation split and demonstrates clear advantages in small-object localization, zero-shot generalization to NuScenes and BDD100K, and human-rated interpretability and trustworthiness. These results suggest that explicitly combining temporal semantics and high-resolution perception provides a stronger foundation for interpretable and safety-oriented autonomous driving systems. The code is available at https://github.com/pixeli99/unidrive-dev.

</details>

#### 2026-06-23 - ForensicsTok: Forensics-Guided Tokenized Modeling for Image Tampering Localization

**Authors:** Lei Xu, Haowei Wang, Shen Chen, Taiping Yao, Bin Li, Changsheng Chen
**Links:** [abs](https://arxiv.org/abs/2606.24538) - [pdf](https://arxiv.org/pdf/2606.24538)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** splatting, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForensicsTok: Forensics-Guided Tokenized Modeling for Image Tampering Localization
- 作者：Lei Xu, Haowei Wang, Shen Chen, Taiping Yao, Bin Li, Changsheng Chen
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.24538

### 一句话总结
本文提出ForensicsTok，将图像篡改定位重新表述为自回归序列生成任务，通过基于代码簿的令牌解码器和多尺度专家特征融合，提升多模态大模型在篡改定位上的性能与鲁棒性。

### 研究问题
现有基于多模态大模型（MLLM）的图像篡改定位方法，因依赖外部分割解码器形成拼接流水线，导致反向传播中空间信号被稀释、受分割器语义先验限制，定位效果欠佳。

### 核心思路/方法
1. 将篡改定位转化为自回归序列生成任务，直接生成空间对齐的令牌序列，摆脱中间监督。
2. 提出令牌溅射解码器（TSD）：通过基于代码簿的代码平滑技术，将令牌映射为二值掩码，缓解确定性解码器带来的梯度尖锐问题。
3. 提出层次化专家融合（HEF）模块：注入来自取证专家模型的多尺度特征，弥补标准MLLM中取证先验的缺失，构建统一架构。

### 主要贡献
- 为图像篡改定位提出一种新的自回归令牌化建模范式，替代了传统的分段流水线。
- 设计了令牌溅射解码器，实现令牌到掩码的平滑映射。
- 提出层次化专家融合模块，融合多尺度取证特征，增强对多样化篡改线索的捕捉能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中  
理由：该方法在六个基准上显著优于现有MLLM基线，且略优于强取证专家基线，并表现出较强的鲁棒性，对图像取证领域有实际价值。但分类为机器人/AR应用（可能为平台分类错误），且摘要未提供具体数据集及实验设置，需进一步阅读原文以确认核心创新点的通用性。

</details>

<details>
<summary>Abstract</summary>

Multi-modal Large Language Models (MLLMs) offer powerful reasoning for forensic tasks, yet existing approaches utilizing exogenous segmentation decoders often suffer from suboptimal localization. The reliance on stitched pipelines introduces information bottlenecks during backpropagation, which dilutes spatial signals and is limited by semantic priors of the segmentor. To address these limitations, we propose ForensicsTok, which reformulates image manipulation localization as an autoregressive sequence generation task. ForensicsTok directly generates spatially grounded token sequences, enabling precise mask prediction without intermediary supervision. Specifically, we introduce a Token Splatting Decoder (TSD) to map tokens to binary masks via codebook-aware code smoothing, which mitigates sharp gradients from deterministic detokenizers. Furthermore, to capture diverse tampering clues, we propose a Hierarchical Expert Fusion (HEF) module that injects multi-scale features from a forensic expert model. This unified architecture effectively compensates for the lack of forensic priors in standard MLLMs. Extensive experiments on six benchmarks show that ForensicsTok substantially improves over existing MLLM-based baselines and slightly improves over strong forensic expert baselines, while exhibiting stronger robustness to perturbations.

</details>

#### 2026-06-23 - NavWM: A Unified Navigation World Model for Foresight-Driven Planning

**Authors:** Yanghong Mei, Longteng Guo, Ming-Ming Yu, Guiyu Zhao, Xingjian He, Jing Liu
**Links:** [abs](https://arxiv.org/abs/2606.24101) - [pdf](https://arxiv.org/pdf/2606.24101)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：NavWM: A Unified Navigation World Model for Foresight-Driven Planning
- 作者：Yanghong Mei, Longteng Guo, Ming-Ming Yu, Guiyu Zhao, Xingjian He, Jing Liu
- 出版日期：2026-06-23
- 分类：Embodied / Robotics / AR Applications
- 链接：[Abstract](https://arxiv.org/abs/2606.24101) | [PDF](https://arxiv.org/pdf/2606.24101)

### 一句话总结
NavWM提出了一种统一的世界模型，通过潜在世界推理、多模态动作预测和可控视觉生成的集成，实现了前瞻性导航规划，在零样本导航和未来状态生成上显著超越现有方法。

### 研究问题
传统视觉导航策略在复杂环境中存在短视决策和模式崩溃问题；现有的世界模型范式将感知、生成和控制模块分离，无法捕捉三者共享的时空动态。

### 核心思路/方法
1. **统一架构**：将潜在世界推理、多模态动作预测和可控视觉生成无缝集成。
2. **潜在世界令牌**：用于提取几何和语义先验，赋予智能体鲁棒的结构理解。
3. **锚定多模态轨迹预测**：基于锚点生成多样化的动作空间，克服确定性策略的局限性。
4. **闭环规划**：利用视觉前瞻评估并选择最优路径，使生成世界模型可作为鲁棒的闭环规划器。

### 主要贡献
- 首次提出统一导航世界模型，融合推理、预测和生成三种能力。
- 引入锚定多模态轨迹预测框架，扩展动作多样性，提升规划的鲁棒性。
- 在多种机器人数据集上实现高保真未来状态生成与零样本导航的成功率显著提升，达到新最优水平。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该论文发表于2026年，提出了一种新颖的统一世界模型架构，解决了导航中关键的多模块协同与前瞻规划问题，实验在多个数据集上取得显著提升，对具身智能与机器人导航领域的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Conventional visual navigation policies often struggle with myopic decision-making and mode collapse in complex environments. While world models offer a promising alternative, existing paradigms typically isolate perception, generation, and control, failing to capture their shared spatio-temporal dynamics. In this paper, we propose NavWM, a unified navigation world model that seamlessly integrates latent world reasoning, multimodal action prediction, and controllable visual generation. At its core, NavWM leverages latent world tokens to distill geometric and semantic priors, endowing the agent with robust structural understanding. To overcome the limitations of deterministic policies, we introduce an anchor-based multimodal trajectory forecasting framework that generates a diverse action space. This inherent diversity explicitly empowers the generative world model to act as a robust closed-loop planner, utilizing visual foresight to evaluate and select the optimal path. Extensive experiments across diverse robotics datasets demonstrate that NavWM significantly advances the state-of-the-art, delivering remarkable improvements in both high-fidelity future state generation and zero-shot navigation success.

</details>

#### 2026-06-23 - DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs

**Authors:** Haidong Hou, Zhangguo Yu, Hengbo Qi, Jianlin Zhang
**Links:** [abs](https://arxiv.org/abs/2606.24089) - [pdf](https://arxiv.org/pdf/2606.24089)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynaWM: Dynamics-Aware Distillation with World Model and Momentum Targets for Smooth Locomotion over Continuous Stairs  
- 作者：Haidong Hou, Zhangguo Yu, Hengbo Qi, Jianlin Zhang  
- 出版日期：2026-06-23  
- 分类：具身/机器人/AR应用 (Embodied / Robotics / AR Applications)  
- 链接：摘要: https://arxiv.org/abs/2606.24089 | PDF: https://arxiv.org/pdf/2606.24089  

### 一句话总结  
本文提出DynaWM框架，通过引入世界模型正则化和动量目标编码器，提升双足轮式机器人在连续楼梯场景中的地形适应性与运动平滑性。

### 研究问题  
当前学生-教师（teacher-student）框架在双足轮式机器人长楼梯攀爬任务中，存在动力学感知表征弱化以及地形几何编码不完整的问题，导致机器人难以平滑遍历连续楼梯。

### 核心思路/方法  
1. 引入一个**世界模型**作为正则化器，强制编码器学习前向动力学感知，从而保留完整的地形几何信息，并支持分层编码可视化。  
2. 采用**动量目标编码器**（momentum target encoder）为学生网络提供一致的蒸馏目标，防止因教师网络非平稳更新导致维度坍塌（dimensional collapse），稳定知识迁移过程。

### 主要贡献  
- 提出动力学感知表征学习框架DynaWM，增强地形几何编码能力，并通过PCA可视化与定量指标验证编码器能分层捕捉地形几何。  
- 在仿真和真实硬件实验中，DynaWM使双足轮式机器人能够克服多种连续楼梯，实现了更高的地形适应性和运动平滑性。

### 局限性  
- 摘要未提供模型的泛化能力（例如是否适用于楼梯之外的其他复杂地形）的讨论。  
- 摘要未提及计算开销或实时性分析，也未详细说明教师网络的训练过程或框架对硬件要求的限制。  

### 阅读优先级  
**高**  
理由：该工作针对双足轮式机器人攀爬连续楼梯这一具体且具挑战性的实际问题，提出了明确的方法改进（世界模型正则化+动量目标蒸馏），并在仿真和实物上验证了效果。对于从事具身机器人学习、四足/双足运动控制的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent advances in control have enabled bipedal-wheeled robots to traverse slopes and single-step obstacles, yet long staircase traversal remains challenging as current teacher-student frameworks suffer from weakened dynamics-aware representations and incomplete terrain geometry encoding. To bridge this gap, we propose DynaWM, a dynamics-aware representation learning framework. To enhance terrain encoding capability and enable transparent assessment, we introduce a world model as a regularizer to enforce forward-dynamics awareness, preserving comprehensive terrain geometry while facilitating hierarchical encoding visualization. To stabilize knowledge transfer, we employ a momentum target encoder to provide consistent distillation targets, preventing dimensional collapse from non-stationary teacher updates. Evaluation of the learned representations through Principal Component Analysis (PCA) visualization and quantitative metrics reveals that our encoder hierarchically captures terrain geometry with higher terrain encoding capability, leading to enhanced terrain adaptability and motion smoothness. Experimental results in simulation and real hardware demonstrate that our method achieves superior terrain adaptability and motion smoothness, enabling bipedal-wheeled robots to overcome diverse continuous stairs, as shown in Fig. 1.

</details>

#### 2026-06-22 - LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation

**Authors:** Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
**Links:** [abs](https://arxiv.org/abs/2606.23685) - [pdf](https://arxiv.org/pdf/2606.23685)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation
- 作者：Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.23685

### 一句话总结
LaST-HD提出一种新的机器人学习范式，通过对齐人体手部与机器人演示在共享潜在推理空间中的物理动力学，使机器人能从可扩展的人类手部数据中学习高效的物理操作行为。

### 研究问题
如何使机器人从大规模、低成本采集的人类手部演示数据中，有效学习适用于不同机械结构的物理操作技能，并提升对新颖物体、场景和位置的泛化能力。

### 核心思路/方法
1. **对齐潜在推理空间**：在“先推理后动作”的VLA框架下，利用未配对的人手与机器人轨迹训练一个辅助的动作条件世界模型，生成统一的潜在目标，对齐不同形态的表示。
2. **低成本数据采集**：开发Out-of-Lab (OOL) Glove，一种专用于人手数据采集的低成本动作捕捉手套，提供精确关键点并可作为通用动作监督信号。
3. **渐进式混合训练**：采用混合人-机器人协同训练和人手在线矫正后训练两步法，先通过混合共训练提升泛化性，再利用在线矫正适应新环境。

### 主要贡献
1. 提出LaST-HD，一种通过对齐跨形态潜在动力学实现人类到机器人动作学习的新范式。
2. 开发OOL Glove低成本数据采集设备，并展示其采集的人手数据可作为不同机械手（夹爪、灵巧手）的通用监督。
3. 验证渐进式混合训练方法，仅用20分钟OOL手套数据即可在新环境中达到90%以上的准确率，并显著提升对新型物体、场景和位置的泛化能力。

### 局限性
摘要未提供足够信息。摘要未提及具体实验失败案例、对特殊工况（如极端光照、物体变形）的鲁棒性、或该方法在更复杂操作任务（如精密装配）上的表现。

### 阅读优先级
**高**  
理由：该工作提出了一种新颖的、基于潜在空间对齐的人-机器人动作学习范式，结合低成本数据采集设备，在仅需少量数据的情况下获得了高准确率和强泛化性。对于关注机器人模仿学习、人机交互、低成本数据采集和技能迁移的研究者具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space. Rather than mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model on unpaired human-hand and robot trajectories to synthesize unified latent targets. After aligning cross-embodiment representations in this shared forward-dynamics space, these targets supervise LaST-HD's latent reasoning process, enabling it to internalize shared physical dynamics and drive efficient human-hand action learning. Moreover, we develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for human-hand data collection. The captured human data provide precise keypoints and serve as universal action supervision across grippers and dexterous hands. Armed with the aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-to-human training recipe comprising mixed human-robot co-training and human-hand online correction post-training. Through mixed co-training, LaST-HD improves generalization to novel objects, scenes, and positions using only human-hand demonstrations. With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.

</details>

#### 2026-06-22 - IMAGIN-4D: Image-Guided Controllable Interaction Generation

**Authors:** Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, Michael J. Black, Dimitrios Tzionas, Shreyas Hampali
**Links:** [abs](https://arxiv.org/abs/2606.23675) - [pdf](https://arxiv.org/pdf/2606.23675)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, embodied AI, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IMAGIN-4D: Image-Guided Controllable Interaction Generation
- 作者：Sai Kumar Dwivedi, Federica Bogo, Buğra Tekin, Chenhongyi Yang, Nadine Bertsch, Tomas Hodan, Michael J. Black, Dimitrios Tzionas, Shreyas Hampali
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要：https://arxiv.org/abs/2606.23675；PDF：https://arxiv.org/pdf/2606.23675

### 一句话总结
提出一种基于扩散模型的人-物交互生成方法IMAGIN-4D，利用参考图像作为空间和时间条件，通过分解图像特征实现对交互姿态、轨迹和接触的精细控制。

### 研究问题
现有的人-物交互生成方法依赖文本、物体几何和稀疏路径点，但这些信号无法唯一指定交互细节（如抓取方式、接近方向、身体姿势等），导致生成结果存在歧义。本研究旨在利用参考图像提供更明确的交互视觉规范，并解决单一图像特征混淆不同时空条件的问题。

### 核心思路/方法
1. **空间解耦条件**：从参考图像中提取“交互状态令牌”（interaction-state tokens），分别编码身体姿态、物体姿态、身体-物体接触及空间关系。
2. **时间解耦条件**：对每个生成帧，从图像中查询与帧相关的“帧感知令牌”（frame-aware tokens），使不同帧段能关注同一图像中不同的视觉线索。
3. **角色感知条件融合**：文本、路径点和交互状态令牌使用独立的AdaLN（自适应层归一化）流，帧感知令牌则通过交叉注意力与运动令牌交互，以平衡图像、文本和路径点条件。
4. **数据与评估**：由于缺乏配对图像，构建了从运动到图像的合成渲染流程（基于FullBodyManipulation数据集），并引入图像-运动对齐度量，用于评估生成运动与参考快照是否匹配。

### 主要贡献
1. 提出IMAGIN-4D，首个通过参考图像实现精细交互控制的扩散模型。
2. 设计了时空解耦的图像条件方法，避免单一图像特征对交互细节的混淆。
3. 构建了合成运动到图像的渲染流程及图像-运动对齐度量，填补了缺少配对图像数据的空白。
4. 在FBM和BEHAVE数据集上，相比单令牌或均匀图像条件的基线方法，IMAGIN-4D在保持路径点跟踪和运动质量的同时，显著提升了交互控制的细粒度。

### 局限性
摘要未提供足够信息，例如模型对复杂遮挡、未见物体类型或长序列生成的鲁棒性未提及。

### 阅读优先级
**高**  
理由：该工作解决了人-物交互生成中歧义性的关键问题，提出了创新的时空解耦图像条件机制，且实验在多个数据集上验证了有效性。对从事角色动画、机器人交互、AR/VR及具身AI的研究者有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Generating human-object interactions (HOI) is central to character animation, robotics, AR/VR, and embodied AI. Recent HOI generation methods synthesize motion from text, object geometry, and sparse waypoints, controlling action semantics and object trajectories. However, these signals underspecify interaction: the same prompt and trajectory can produce different grasps, approach directions, body poses, object poses, contacts, and body-object layouts. We address this ambiguity with a reference image as a visual specification of the desired interaction snapshot. However, a single global image representation conflates distinct cues and conditions all frames on identical visual evidence. We therefore introduce IMAGIN-4D, a diffusion-based HOI generator that decomposes image conditioning spatio-temporally. For spatial conditioning, IMAGIN-4D extracts supervised interaction-state tokens for body pose, object pose, body-object contact, and spatial relationships at the depicted frame. For temporal conditioning, it computes frame-aware tokens by querying image patches per generated frame, allowing sequence segments to attend to different visual cues from the same image. To balance image, text, and waypoint cues, IMAGIN-4D uses role-aware conditioning: text, waypoints, and interaction-state tokens use separate AdaLN streams, while frame-aware visual tokens cross-attend with motion tokens. Since HOI motion datasets lack paired images, we build a synthetic motion-to-image rendering pipeline from FullBodyManipulation (FBM) and introduce an image-adherence metric to evaluate whether generated motions match the reference snapshot. Experiments on FBM and BEHAVE show that IMAGIN-4D improves fine-grained interaction control over single-token and uniformly image-conditioned baselines while preserving waypoint-following and motion quality. Code and models will be released at https://imagin4d.github.io.

</details>

#### 2026-06-22 - From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models

**Authors:** David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau
**Links:** [abs](https://arxiv.org/abs/2606.23312) - [pdf](https://arxiv.org/pdf/2606.23312)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, scene understanding, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Pixels to Concepts: Growing Rich 3D Semantic Scene Graph Forests utilizing Foundation Models
- 作者：David Oberacker, Meike Deitersen, Niklas Spielbauer, Tristan Schnell, Georg Heppner, Arne Roennau
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.23312

### 一句话总结
本文提出一种利用视觉语言模型（VLM）和大语言模型（LLM）构建包含开放语义关系的3D场景图森林的方法，以提升机器人的场景理解与任务执行能力。

### 研究问题
现有3D场景图方法通常局限于预定义的刚性关系类别，忽略了语义连接（如因果联系或环境上下文），导致无法支持复杂的真实世界环境理解需求。本文研究如何利用基础模型构建具有开放语义关系的3D场景图森林，以改善场景理解和机器人任务执行。

### 核心思路/方法
1. **节点与关系提取**：先用VLM识别实例特定的概念节点和关系，再用LLM通过推理扩展出更广泛、更抽象的概念节点和关系。
2. **图森林构建**：将物体节点、概念节点及关系组装成层次化的3D场景图森林，并引入概念节点表示抽象概念。
3. **评估**：在uHumans2和ScanNet室内数据集上验证生成关系的准确性和相关性；通过开放词汇物体检索任务（基于ScanNet数据及Boston Dynamics Spot实际室内部署）展示在机器人应用中的下游适用性。

### 主要贡献
- 利用基础模型构建更富表达力、语义更深的3D层次化场景图。
- 提出开放语义关系的场景图森林，突破预定义关系类别的限制。
- 在真实室内环境和公开数据集上验证了方法在机器人语义理解与环境感知中的潜力。

### 局限性
摘要未提供足够信息，无法推断具体的局限性（如计算开销、泛化能力边界等）。

### 阅读优先级
**高**  
理由：研究面向机器人场景理解核心难点，结合VLM和LLM构建层次化场景图的方法具有创新性，且在真实机器人平台（Boston Dynamics Spot）上进行了验证，对从事具身智能、3D感知及机器人操作的研究者具有参考价值。

</details>

<details>
<summary>Abstract</summary>

Operating in complex real-world environments requires robots to understand their surroundings on a functional semantic level. This demands a detailed multi-layer world model capturing the complex relations of its surroundings. Hierarchical 3D scene graphs address this challenge by integrating geometric, semantic, and relational data within a unified spatial framework. However, current 3D scene graph approaches often restrict themselves to rigid structures of pre-determined relationship classes, mostly neglecting important semantic connections, like causal connections or environmental contexts. This paper explores the potential of foundation models to build forests of 3D scene graphs with open semantic relationships to improve scene understanding and robotic task execution. We propose a method where instance-specific concept-nodes and relationships are first identified by a VLM and extended upon by a LLM, inferring broader, more abstract concept-nodes and relationships through reasoning. These object-nodes, concept-nodes, and relationships are then assembled into a forest of hierarchical 3D scene graphs, enhanced with concept-nodes to represent abstract concepts. Evaluations were conducted on the uHumans2 and ScanNet indoor dataset, validating the accuracy and relevance of the generated relationships. Downstream suitability of scene-graph forests for robotics applications is demonstrated in an open-vocabulary object-retrieval task utilizing both ScanNet data and a real-world indoor deployment using a Boston Dynamics Spot. This paper leverages foundation models to create more expressive, semantically deep 3D hierarchical scene graphs and demonstrates their potential to advance semantic and environmental understanding in robotics.

</details>

#### 2026-06-22 - Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI

**Authors:** Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
**Links:** [abs](https://arxiv.org/abs/2606.22971) - [pdf](https://arxiv.org/pdf/2606.22971)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, autonomous driving, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Humanoid-OmniOcc: Stereo-Based Full-View Occupancy Dataset for Embodied AI
- 作者：Xianda Guo, Bohao Zhang, Chenwei Huang, Shiyuan Chen, Ruilin Wang, Yiqun Duan, Cong Yang, Qin Zou, Wei Sui
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22971

### 一句话总结
本文提出了一个面向人形机器人的全景立体占据数据集Humanoid-OmniOcc，并基于Real2Sim2Real闭环范式设计了相应的占据预测模型。

### 研究问题
现有占据预测数据集主要面向自动驾驶场景（前向相机、远场几何、静态道路先验），不适用于人形机器人在复杂室内环境中的全身感知。

### 核心思路/方法
1. **数据集构建**：包含15个模拟室内场景和5个真实环境，采集超过155K样本，采用全景立体（panoramic stereo）相机配置。
2. **Real2Sim2Real闭环**：真实传感器参数驱动物理准确仿真，仿真生成大规模带标注训练数据，模型在仿真训练后直接在真实数据上评测，实现迭代优化。
3. **模型设计**：提出Humanoid-OmniOcc模型，利用鲁棒的深度先验进行精确的2D到3D提升（lifting）。

### 主要贡献
1. 发布了首个面向人形机器人的大规模全景立体占据数据集，覆盖多样场景和风格。
2. 提出了Real2Sim2Real闭环框架，弥合仿真到真实的鸿沟。
3. 设计了基于立体深度先验的占据预测模型，在仿真和真实场景中均优于单目基线方法。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**  
理由：该工作针对人形机器人感知这一前沿方向，提出了新颖的全景立体数据集和Real2Sim2Real闭环框架，实验验证了跨场景泛化能力，对具身AI和机器人研究具有重要参考价值。

</details>

<details>
<summary>Abstract</summary>

Occupancy prediction at voxel-level granularity is essential for safe robotic navigation and interaction in complex environments. Existing occupancy datasets, however, are predominantly designed for autonomous driving with vehicle-centric biases -- forward-facing cameras, far-field geometry, and static road priors -- limiting their applicability to embodied humanoid perception. We present Humanoid-OmniOcc, a large-scale panoramic stereo-based occupancy dataset tailored for humanoid robots. The dataset encompasses 15 diverse simulated indoor scenes and 5 real-world environments, yielding over 155K samples with broad scene and style diversity. Importantly, the dataset is designed around a Real2Sim2Real closed-loop paradigm: real sensor specifications drive physically accurate simulation, simulation produces large-scale annotated training data, and models trained in simulation are directly evaluated on real-world captures -- enabling iterative refinement of the sim-to-real pipeline. We further propose \textbf{H}umanoid \textbf{S}urround \textbf{S}tereo-guided \textbf{Occ}upancy model (Humanoid-OmniOcc) that exploits robust depth priors for accurate 2D-to-3D lifting. Extensive experiments show that Humanoid-OmniOcc consistently outperforms monocular baselines and generalizes well to both unseen simulated test scenes and real-world environments, validating the effectiveness of the Real2Sim2Real design. Code and data will be available upon acceptance at https://d-robotics-ai-lab.github.io/humanoid-omniocc.

</details>

#### 2026-06-22 - HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration

**Authors:** Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
**Links:** [abs](https://arxiv.org/abs/2606.22756) - [pdf](https://arxiv.org/pdf/2606.22756)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration
- 作者：Sandilya Sai Garimella, Daniel Chase Butterfield, Sean Wilson, Lu Gan
- 出版日期：2026-06-22
- 分类：Embodied / Robotics / AR Applications；3D Reconstruction & Multi-view Geometry
- 链接：[abstract](https://arxiv.org/abs/2606.22756) | [pdf](https://arxiv.org/pdf/2606.22756)

### 一句话总结
HERCULES是一个基于Unreal Engine 5的开源仿真框架，专为异构多机器人（UAV-UGV）SLAM、协同感知与探索设计，支持大规模动态环境下的被动数据采集与主动闭环规划。

### 研究问题
如何解决现有仿真工具在异构多机器人（UAV-UGV）协同操作中的架构限制，实现大规模、高保真、动态环境下的SLAM、协同感知与探索任务开发与评估。

### 核心思路/方法
1. 基于Unreal Engine 5的AirSim和Cosys-AirSim构建，修复了先前框架的架构缺陷。
2. 新增UGV控制器以匹配UAV控制接口，提供共享导航栈（地图、可通行性分析、规划、控制）。
3. 扩展传感器套件：物理长波红外相机、可配置夜视模式。
4. 集成智能体（行人、交通、野生动物）与高保真动态现象（火灾、洪水、作物病害传播）。
5. 提供轻量级API、ROS 2封装、硬件级时间同步。
6. 支持两种运行模式：离线被动回放轨迹生成多模态数据集，以及在线主动闭环规划。

### 主要贡献
- 开源了首个面向异构多机器人（UAV-UGV）的高保真仿真与数据采集框架。
- 解决了现有框架在并发操作、传感器同步和大规模动态环境中的架构限制。
- 提供了异构多机器人SLAM基准数据集（双UAV+双UGV，覆盖沙漠、森林、城市千米级场景），并公开源码、文档与实验代码。

### 局限性
摘要未提供局限性信息。

### 阅读优先级
中。理由：框架工具性较强，直接贡献在于开源仿真基准和数据集，但摘要未给出与传统方法的定量对比或性能突破，对关注异构多机器人SLAM与协同感知的读者有参考价值，但对追求方法论创新的读者帮助有限。

</details>

<details>
<summary>Abstract</summary>

We present HERCULES, an open-source simulator and data-collection pipeline for heterogeneous multi-robot autonomy. Built upon the Unreal Engine 5 (UE5)-based simulators AirSim and Cosys-AirSim, HERCULES resolves key architectural limitations of prior frameworks to enable concurrent unmanned aerial and ground vehicle (UAV-UGV) operation in large-scale, photorealistic, dynamic environments. It introduces a new waypoint-tracking UGV controller that mirrors existing UAV control interfaces, and provides a shared navigation stack for mapping, traversability analysis, planning, and control across heterogeneous platforms. Expanding inherited sensor suites, it adds physics-based long-wave infrared (LWIR) cameras and configurable night-vision modes for degraded visual environments. HERCULES provides lightweight APIs, ROS 2 wrappers, and rigorous time synchronization across sensors and platforms, and brings state-of-the-art game-engine capabilities into robotics simulation, integrating intelligent agents such as pedestrians, traffic, and wildlife with high-fidelity dynamic phenomena, including fire, flooding, and crop disease spread. HERCULES runs in two modes: passively, replaying offline-designed trajectories to generate reproducible multi-modal datasets, and actively, running an online planner in closed loop from live observations. Our experiments in heterogeneous multi-robot SLAM, collaborative perception, and exploration, using both HERCULES-generated data and active closed-loop execution, demonstrate its utility for advancing heterogeneous multi-robot autonomy. We publicly release our source code, experiment code, documentation, and datasets, including a heterogeneous multi-robot SLAM benchmark collected with two UAVs and two UGVs across kilometer-scale desert, forest, and city environments, at https://lunarlab-gatech.github.io/HERCULES-website.

</details>

#### 2026-06-21 - MAPS: Multi-Anchor Projection Similarity for Joint Vision-Language Geo-Localization

**Authors:** Yutong Hu, Siyuan Tan, Shaocheng Yan, Pengcheng Shi, Qingwu Hu, Jiayuan Li
**Links:** [abs](https://arxiv.org/abs/2606.22543) - [pdf](https://arxiv.org/pdf/2606.22543)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MAPS: Multi-Anchor Projection Similarity for Joint Vision-Language Geo-Localization
- 作者：Yutong Hu, Siyuan Tan, Shaocheng Yan, Pengcheng Shi, Qingwu Hu, Jiayuan Li
- 出版日期：2026-06-21
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2606.22543

### 一句话总结
本文提出一种名为 MAPS 的多锚点投影相似度方法，通过将视觉-语言联合地理定位问题建模为多锚点几何对齐，利用锚点平面上的投影长度作为新的相似度度量，实现了该任务上的领先性能。

### 研究问题
当前跨视图、跨模态地理定位模型主要基于点对点对齐，无法有效处理视觉与文本线索联合定义语义子空间的查询场景。因此，研究如何针对联合图像-文本查询（Vision-Language Geo-Localization, VLGL）设计更有效的对齐与相似度度量方法。

### 核心思路/方法
- 将 VLGL 视为多锚点几何对齐问题：利用视觉和文本查询特征在高维空间构建一个锚点平面（anchor plane）。
- 提出 MAPS 距离度量：通过目标特征在该锚点平面上的投影长度来衡量相似度，替代传统余弦相似度。
- 设计基于 MAPS 的对比损失：训练时驱使目标特征朝向对应的锚点平面，使学习到的表示与几何对齐一致。

### 主要贡献
- 首次将联合图像-文本查询的地理定位形式化为多锚点几何对齐问题。
- 提出 MAPS 相似度度量，能够捕获目标特征与联合查询子空间之间的几何一致性，比点对点余弦相似度更具判别力。
- 提出 MAPS 对比损失，使表示学习与检索几何对齐协同优化。
- 在 VLGL 任务上取得当时最优性能（状态达到最新技术水平）。

### 局限性
摘要未提供足够信息（例如实验设定、数据集、失败案例、计算开销、模型鲁棒性等）。

### 阅读优先级
中  
理由：该工作针对视觉-语言联合查询这一特定地理定位问题，提出了几何视角下的新度量与训练目标，方法创新性较强。但摘要未提供具体实验细节和结果数值，无法全面评估其实用性和复现难度，适合对该子方向感兴趣的读者关注。

</details>

<details>
<summary>Abstract</summary>

Humans localize places by integrating perceptual cues from vision with semantic reasoning from language, forming a scene understanding that is both intuitive and structured. Although existing geo-localization models have made substantial progress in cross-view and cross-modal settings, they are largely built upon point-to-point alignment, which is insufficient for joint vision-language queries. In such queries, visual and textual cues do not simply act as independent references, but jointly define a semantic subspace for locating the target. In this paper, we formulate vision-language geo-localization (VLGL) with joint image-text queries as a multi-anchor geometric alignment problem and propose a unified framework for this setting. To realize this formulation, we propose Multi-Anchor Projection Similarity (MAPS), a new metric which constructs an anchor plane from visual and textual query features in a high-dimensional space and measures similarity by the projection length of the target feature onto this plane. Unlike cosine similarity which evaluates isolated pairwise relations, MAPS captures the geometric consistency between the target feature and the joint query subspace, providing a more discriminative ranking criterion during retrieval. To make the learned representation consistent with this geometry, we further introduce a MAPS-based contrastive loss that drives target features toward the corresponding anchor plane. The proposed framework, similarity metric, and training objective jointly yield state-of-the-art performance in VLGL.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
