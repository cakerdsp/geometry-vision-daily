# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：36
- 分类分布：
  - Embodied / Robotics / AR Applications: 11
  - 3D Reconstruction & Multi-view Geometry: 11
  - Neural Scene Representations & Rendering: 7
  - Dynamic / 4D Reconstruction: 4
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **前馈/可泛化重建加速替代“逐场景优化”**  
   ThermalSplat（2611.15435）用前馈高斯泼溅直接从稀疏热红外图像重建，明确不依赖位姿、RGB 引导和逐场景训练；Kosmo-GFM（2611.16840）把几何基础模型、位姿优化引擎与重建派生监督整合为“生产可用”系统；TTB（2611.17331）则把测试时训练的计算前移到一次“烘焙”，换取解码期效率。三者共同指向：重建系统的价值重心正从“单场景拟合质量”转向“跨场景泛化 + 推理成本”。

2. **动态/4D 重建开始处理“拓扑变化”和“干扰物”，而非仅形变**  
   Topo-4DGS（2611.16012）指出固定表示形变无法处理切割、开合等分裂/合并/表面显露事件，提出部件级独立刚性变换与高斯动态激活；ReCan-GS（2611.16259）用形变场 Jacobian 敏感性分数分离 Core 与 Distractor 高斯，无需掩码或预训练分割器。二者都在挑战 4DGS 的“固定拓扑 + 全观测联合建模”假设，4D 重建的问题定义正在细化。

3. **世界模型/视频预训练特征向 3D 任务迁移，但“表示适配”成为瓶颈**  
   Track4D（2611.15287）系统比较 RTV 与 NCMV 两种视频化 3D 跟踪表示，指出表示偏离自然视频分布会直接影响 VDM 复用效果；Multi-View 3D Reconstruction Using V-JEPA Features（2611.15143）则报告空间相机回归轨迹误差比全局低 29.3%，但差于 identity poses，说明视频预训练特征并非“拿来即用”。ActWorld-JEPA（2611.16579）进一步指出潜空间预测一致性不等于规划质量，需要用 R³ 把预测表示与候选评分对齐。这一组论文共同反映：JEPA/VDM 类潜空间模型进入 3D/规划任务时，核心工程问题转为“如何定义可学习的中间表示”。

4. **机器人感知从“静态位姿/掩码”走向“运动学状态、力—变形、障碍几何”显式建模**  
   VOKE（2611.16423）在 6D 位姿之外补线/角速度与加速度；单视角 RGB-D 力—变形估计（2611.15650）直接建模弹塑性材料力—体积关系；MOSAIC（2611.15937）向 VLA 注入角色特定掩码、深度几何 token 与障碍物注意力监督；VINE（2611.16282）用外置相机估计视角不变障碍图再供 PPO/A* 使用。这些工作共同说明：下游控制不再满足于让策略从 2D 观测中隐式推断物理量，而是把几何、运动学、接触力作为显式中间表征接入。

5. **边缘/嵌入式部署与渲染底层优化成为独立议题**  
   EG360（2611.16793）以 6.593M 参数在 Jetson Orin NX 上达 35 FPS，同时强调零样本泛化；RGB-D SLAM on the Edge（2611.16472）在 Raspberry Pi 5 上对 RTAB-Map/ORB-SLAM3 做阶段级与函数级剖析；MatrixSplat（2611.15153）指出 3DGS 的深度排序 alpha 合成与 Tensor Cores 不匹配，改用顺序无关加权累加。效率问题正从“模型压缩”扩展到“渲染管线与硬件单元对齐”。


#### 技术路线观察

- **几何基础模型路线**：Kosmo-GFM 代表“GFM 预测 + 几何优化 + 重建监督闭环”的系统化路线，输出相机参数、深度、跨视图对应与动态 3D 点，直接服务 3D/4DGS 下游；ThermalSplat 则走“前馈泛化 + 无需位姿”的轻量路线，用 soft census loss 与边界结构 loss 应对热红外低纹理。两者一个偏系统集成、一个偏模态专用泛化，共同点是都在削弱传统 SfM/逐场景优化的前置依赖。

- **3D/4D 重建路线**：4DGS 方向出现明显分化——Topo-4DGS 从“表示结构”入手（部件级刚性变换 + 高斯激活/停用），ReCan-GS 从“优化准则”入手（Jacobian 敏感性分数做分离/剪枝）。Track4D 则代表另一条路：不直接重建，而是把 3D 跟踪表示为视频信号，借用视频扩散先验。Multi-View V-JEPA 工作更偏“组件隔离分析”，提醒视频预训练特征的收益需要与相机回归方式、细化步骤分开归因。

- **神经场景表示与渲染路线**：TTB 关注 decoder-only 视图合成模型的测试时效率，把跨视图注意力烘焙进轻量 MLP；MatrixSplat 关注 3DGS 渲染与 GPU 矩阵单元的匹配。前者是“模型级效率”，后者是“系统级效率”，但都指向同一判断：高质量新视图合成的瓶颈正从表达能力转向推理/渲染吞吐。

- **机器人/AR 应用路线**：VOKE、MOSAIC、VINE、RUMI（2611.15802）、力—变形估计（2611.15650）分别覆盖运动学感知、VLA 几何增强、外置相机导航、力感知数据采集接口、弹塑性材料建模。整体技术侧重点是把“显式物理/几何中间量”插入感知—控制链路：VOKE 输出速度/加速度，MOSAIC 输出角色特定几何 token，VINE 输出视角不变障碍图，RUMI 输出接触力。这与纯端到端 VLA 路线形成互补而非替代关系。

- **交叉观察**：Spatial Foundry（2611.17318）提供共享场景坐标、可编辑资产与多模态对齐数据，可能同时服务 4D 重建、具身导航与空间智能评测；但当前论文列表中尚未出现直接使用该数据集的工作，其影响需后续观察。


#### 值得优先阅读的论文

1. **Topology-Aware 4D Gaussian Splatting for Egocentric Videos（2611.16012）**  
   理由：它把 4DGS 的失效模式从“形变建模不足”推进到“拓扑变化”这一更本质的表示假设问题，并附带 TopoEgo 基准。若后续要做动态物体交互重建，这是问题定义层面的关键参考。

2. **Kosmo-GFM（2611.16840）**  
   理由：少见的“生产就绪”系统论文，把 GFM、位姿优化与重建监督串成闭环，并在 SpatialBench 上报告深度/位姿/动态点误差。适合判断几何基础模型当前工程成熟度与系统瓶颈。

3. **TTB（2611.17331）**  
   理由：直接处理 decoder-only 视图合成模型的效率—质量权衡，且“把注意力映射烘焙进 MLP”的思路可能迁移到其他 KV-cache 推理场景。对关注新视图合成部署成本的研究者优先级高。

4. **Track4D（2611.15287）**  
   理由：它没有停留在“用视频扩散模型做 3D 任务”的口号，而是系统比较两种表示并指出表示分布偏移问题。对想复用视频预训练先验做几何任务的人，这篇提供了可操作的表示设计参照。

5. **MOSAIC（2611.15937）或 VOKE（2611.16423）（二选一）**  
   理由：若关注 VLA 与杂乱场景操作，选 MOSAIC，它展示了不改变主干、以辅助监督注入几何/障碍信息的模块化路线；若关注灵巧手内操作与感知—控制链路，选 VOKE，它把运动学状态显式化并接入 RL。两篇都体现了“显式中间表征”这一趋势。


#### 可能的研究机会

- **拓扑感知 4

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-17T16:45:50-05:00
**Total number of papers:** 46
**Number of papers added in the latest update:** 24
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

#### 2026-11-16 - IGRecon4D: Dynamic-Object-Aware Feed-Forward Reconstruction of Driving Scenes

**Authors:** Yifei Tong, Ziyang Huang, Yizhao Han, Xiaoxiao Long, Hao Zhu
**Links:** [abs](https://arxiv.org/abs/2611.21126) - [pdf](https://arxiv.org/pdf/2611.21126)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Embodied / Robotics / AR Applications
**Matched keywords:** feed-forward reconstruction, dynamic scene reconstruction, scene reconstruction, depth estimation, autonomous driving, driving scene, localization

<details>
<summary>Abstract</summary>

Feed-forward 4D driving-scene reconstruction enables efficient modeling of dynamic autonomous-driving scenes, but current methods suffer from two complementary failure modes: semantic leakage of traffic participants into the static representation and geometric drift of Gaussian locations across viewpoints. We propose \textbf{IGRecon4D}, a feed-forward dynamic scene reconstruction framework that addresses these failures with training-time instance-prior distillation and LiDAR-anchored Gaussian positioning. Specifically, an instance-level semantic branch provides a potentially dynamic participant prior, which is distilled into dynamic-mask learning through the Instance-Dynamic Consistency Constraint to encourage high-recall localization of traffic-participant regions prone to dynamic-static leakage. In parallel, sparse LiDAR measurements guide dense depth estimation, and the resulting depths are back-projected to anchor Gaussian positions for improved multi-view geometric consistency. Experiments on the Waymo Open Dataset and zero-shot evaluation on nuScenes demonstrate improved full-image reconstruction on the main benchmark and stronger traffic-participant-region reconstruction under cross-dataset evaluation.

</details>

#### 2026-11-16 - What the Averages Hide: Monocular Metric Depth Models Still Fail in Everyday Scenes, Mostly on Scale

**Authors:** Hualie Jiang, Yujie Luo, Ziyang Song, Ximeng Li, Zhiqiang Lou, Rui Xu
**Links:** [abs](https://arxiv.org/abs/2611.20518) - [pdf](https://arxiv.org/pdf/2611.20518)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** metric depth, depth estimation

<details>
<summary>Abstract</summary>

Zero-shot monocular metric depth models are evaluated by averaging metric and scale-aligned scores across datasets. Averages cannot show how many images still have severely wrong metric depth, whether depth is under- or overestimated, or whether different models fail on the same images. We propose an evaluation built on per-image results: the failure rate (metric $δ_1$ < 0.5); scale-aligned metrics for structure, and the bias, dispersion and absolute error of the alignment scale for scale; and a cross-model comparison that separates shared from model-specific failures. We apply it to 11 recent architectures with and without ground-truth intrinsics (18 model evaluations) on the 7 everyday-scene benchmarks (4,406 images) used by MoGe-2. Metric depth estimation is not solved in everyday scenes, and the remaining difficulty is mainly scale: the best of the 18 evaluations still has a failure rate of 7.7% (datasets weighted equally); pooled over all failures, 78.8% have intact structure, and after scale correction 98.3% no longer fail. Images failed by at least 6 architectures make up 7.3% of the data, concentrated on HAMMER and DIODE; even when selected only by architectures of other families, they hold 34% to 40% of the error of the top 6 models, against 14% to 18% for as many random images from the same datasets. Adding objects reduces the scale error of most models; ground-truth intrinsics and, in most families, larger models reduce the failures but do not remove them. We recommend reporting failure rates, structure and scale separately, and results stratified by how many models fail. We will release the code, the per-image results with shared-failure labels, and two diagnostic sets built from TUM RGB-D.

</details>

#### 2026-11-12 - Kosmo-GFM: A Production-Ready Geometry Foundation Model

**Authors:** Sheng Tang, Shengzhe Wei, Tiancheng Chen, Wenhua Jin, Xinyang Lu, Tinghao Jiang, Shuoxuan Feng, Yupeng Liu, Yu Zhang, Xingshuo Chang, Keren Zhou, Yuhan Xiong, Jiahao Li, Haoming Liu, Jituo Tian, Hui Liang, Chaoqun Tang, Feng Tian, Wentao Ouyang, Kaojin Zhu, Xiaolin Chai, Peihuang Fu, Miao Zheng, Yunbo Hu, Feixue Cai, Zizhen Zou, Weigang Wang, Yexuan Yang, Haoyu Feng, Weiqi Zhang, Juntong Fang, Zesong Li
**Links:** [abs](https://arxiv.org/abs/2611.16840) - [pdf](https://arxiv.org/pdf/2611.16840)
**Primary category:** Geometry Foundation Models
**Secondary categories:** Dynamic / 4D Reconstruction, Neural Scene Representations & Rendering
**Matched keywords:** geometry foundation model, dynamic 3D, scene flow, 4D Gaussian, scene reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Kosmo-GFM: A Production-Ready Geometry Foundation Model
- 作者：Sheng Tang, Shengzhe Wei, Tiancheng Chen, Wenhua Jin, Xinyang Lu, Tinghao Jiang, Shuoxuan Feng, Yupeng Liu, Yu Zhang, Xingshuo Chang, Keren Zhou, Yuhan Xiong, Jiahao Li, Haoming Liu, Jituo Tian, Hui Liang, Chaoqun Tang, Feng Tian, Wentao Ouyang, Kaojin Zhu, Xiaolin Chai, Peihuang Fu, Miao Zheng, Yunbo Hu, Feixue Cai, Zizhen Zou, Weigang Wang, Yexuan Yang, Haoyu Feng, Weiqi Zhang, Juntong Fang, Zesong Li
- 出版日期：2026-11-12T14:17:22Z
- 分类：Geometry Foundation Models；Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.16840) / [PDF](https://arxiv.org/pdf/2611.16840)

### 一句话总结
Kosmo-GFM 是一个面向生产场景重建的系统，将几何基础模型（GFM）、位姿优化引擎（PoseEngine）和来自 KosmoWorld 的重建监督结合起来，以提升相机参数、深度、跨视图对应和动态 3D 点预测，并服务于下游 3D/4D Gaussian Splatting。

### 研究问题
论文关注的是场景级重建中如何利用学习到的几何先验：GFM 需要从图像和视频预测相机参数、深度、跨视图对应关系和动态 3D 点；PoseEngine 需要把这些预测与几何优化结合，恢复场景级相机位姿与几何；KosmoWorld 则要从重建的真实场景生成图像和几何监督，以改进 GFM 的几何预测。摘要未提供足够信息说明具体失败模式或问题定义细节。

### 核心思路/方法
系统由三部分组成。第一，GFM 从图像和视频中预测相机参数、深度、跨视图对应关系和动态 3D 点。第二，PoseEngine 将这些预测与几何优化相结合，恢复场景级相机位姿和几何，供下游 3D 与 4D Gaussian Splatting 使用。第三，KosmoWorld 从重建的真实世界场景生成图像与几何监督，用于提升 GFM 的几何预测。此外，PoseEngine Flash 提供了进一步的精度—效率权衡，并报告了混合精度运行时间。摘要还提到独立扩展实验显示，随着数据、模型计算和训练预算增加，总体趋势较为有利。

### 主要贡献
- 提出 Kosmo-GFM 场景重建系统，整合 GFM、PoseEngine 与 KosmoWorld 的重建派生监督。
- GFM 在 SpatialBench 的 Sparse 和 Medium 子集上，相比所比较方法取得最低绝对相对深度误差和最高 5 度相对位姿 AUC。
- 在五个评估数据集上，GFM 取得最低的动态点与场景流平均端点误差。
- 在全部比较重建系统均完成的 34 个场景上，PoseEngine 在 1、3、5 度阈值下取得最高场景平均位姿 AUC，累计运行时间 14.07 小时，约为 GLUEMAP 69.67 小时的 20%。
- PoseEngine Flash 测得混合精度运行时间 2.62 小时，约为 GLUEMAP 运行时间的 4%。
- 扩展实验显示，随着数据、模型计算和训练预算增加，总体趋势较为有利。

### 局限性
摘要未提供足够信息说明失败场景、精度上限、对特定数据分布的依赖、PoseEngine Flash 的精度代价细节，以及各数据集和场景规模的具体范围。摘要未提供足够信息说明系统在极端稀疏视图、强动态场景或生产部署条件下的限制。

### 阅读优先级
中。理由：论文涉及几何基础模型、场景级位姿优化和 3D/4D 重建的完整系统，并给出了与 GLUEMAP 的运行时间和位姿 AUC 对比，以及深度、位姿、动态点和场景流指标；对关注几何基础模型与生产级重建流水线的读者有参考价值。但摘要未展开方法细节、失败案例和完整实验设置，是否精读取决于对 PoseEngine、KosmoWorld 监督机制或 3D/4D Gaussian Splatting 下游流程的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

We present Kosmo-GFM, a scene reconstruction system that integrates a geometry foundation model (GFM), a pose optimization engine (PoseEngine), and reconstruction-derived supervision from KosmoWorld. GFM predicts camera parameters, depth, cross-view correspondences, and dynamic 3D points from images and videos. PoseEngine combines these predictions with geometric optimization to recover scene-level camera poses and geometry for downstream 3D and 4D Gaussian Splatting. KosmoWorld generates images and geometric supervision from reconstructed real-world scenes to improve GFM's geometric predictions. On the Sparse and Medium subsets of SpatialBench, GFM achieves the lowest absolute relative depth error and the highest relative-pose AUC at 5 degrees among the compared methods. It also achieves the lowest mean endpoint errors for dynamic points and scene flow across the five evaluated datasets. Across 34 scenes completed by all compared reconstruction systems, PoseEngine achieves the highest scene-averaged pose AUC at thresholds of 1, 3, and 5 degrees, with a cumulative runtime of 14.07 hours, approximately 20% of GLUEMAP's 69.67 hours. PoseEngine Flash provides a further accuracy-efficiency trade-off, with a measured mixed-precision runtime of 2.62 hours, approximately 4% of GLUEMAP's runtime. Separate scaling experiments show generally favorable trends with increased data, model computation, and training budgets. These results support the use of learned geometric priors within a scene-level reconstruction pipeline.

</details>

## Dynamic / 4D Reconstruction

### 2026-11

#### 2026-11-16 - WinDEX: Metric 3D Hand Motion Reconstruction in the Wild for Dexterous Teleoperation and Policy Learning

**Authors:** Hongyu Ma, Hairong Qu, Shiqi Zhao, Yongsong Yang, Kai Shi, Jiahao Ai, Xin You, Peng Yin
**Links:** [abs](https://arxiv.org/abs/2611.21143) - [pdf](https://arxiv.org/pdf/2611.21143)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** motion reconstruction, SLAM, manipulation

<details>
<summary>Abstract</summary>

Human manipulation data are widely used to train robots for human-like dexterity. However, low-cost, large-scale collection in the wild remains challenging. Existing methods remain limited in geometrically grounded metric-scale reconstruction, real-world generalization and inference speed. We present WinDEX, integrating (1) geometric-temporal optimization for metric 3D hand annotation from in-the-wild egocentric stereo videos, combined with visual-inertial SLAM for world-frame reconstruction; (2) WinDEX-Net, an end-to-end, fisheye-native network combining calibrated stereo, local detail and temporal context, with a data-model flywheel of model-assisted annotation and retraining; (3) distilled models for offline reconstruction and causal streaming, supporting reinforcement learning and teleoperation; and (4) low-cost CyberCap stereo-inertial capture, forming the WinDEX-Hand dataset with 1,000 hours of training annotations and held-out human-annotated in-the-wild 2D and independent optical motion-capture evaluation sets. Offline reconstruction runs at 43.61 FPS and causal streaming at 171 FPS. On held-out data, offline reconstruction achieves state-of-the-art accuracy: 14.5 pixels in-the-wild reprojection error and, with visual-inertial odometry, 37.29 mm world-frame joint error. We achieve 7.6 and 3.6 times the task success rates of reinforcement learning policies trained with WiLoR and HaWoR motion references, respectively, and demonstrate real-time arm-hand teleoperation. Project website: https://fruitrabbit.github.io/WinDEX/.

</details>

#### 2026-11-15 - See the Lives of Stars in a Handful of Light

**Authors:** Shuhong Liu, Gengjia Chang, Quanfeng Xu, Ziteng Cui, Qianyu Zhou, Xiaoyu Dong, Lin Gu, Tatsuya Harada
**Links:** [abs](https://arxiv.org/abs/2611.20089) - [pdf](https://arxiv.org/pdf/2611.20089)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Galaxies evolve over hundreds of millions of years, and no telescope has ever watched one move. Cosmological simulations make this evolution visible as a sequence of multi-view images, inviting the question of whether a galaxy can be recovered in four dimensions from its images. This setting defeats existing dynamic scene methods, since millions of stars span only a few pixels each, faint populations blend into diffuse light, and free deformations reproduce the images without obeying gravity. We present Cosmos4D, which rests on two components. Gravitational 4D Gaussian Splatting represents each star as a self-luminous Gaussian whose motion is integrated through a gravitational potential and a low-dimensional force field shared by all stars. Luminosity-stratified dynamics give bright stars individual orbits supervised across image scales and carry faint populations with a velocity field estimated from optical flow. We further build a 4D dataset of eight galaxies from four cosmological simulations, on which Cosmos4D outperforms dynamic Gaussian baselines in both photometric quality and physical accuracy. With these advancements, we glimpse eight hundred million years of a galaxy's life in ninety-six frames.

</details>

#### 2026-11-15 - Spatiotemporal Reconstruction of Auroral Precipitations with Neural Fields

**Authors:** Nazar Misyats, Mizuki Fukizawa, Yoshimasa Tanaka, Satoshi Ikehata
**Links:** [abs](https://arxiv.org/abs/2611.19757) - [pdf](https://arxiv.org/pdf/2611.19757)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** spatiotemporal reconstruction

<details>
<summary>Abstract</summary>

Auroras provide remote optical observations of energetic electrons precipitating into the upper atmosphere, and whose energy distribution encodes key information about large scale magnetospheric processes. Recovering the underlying electron precipitation field from ground-based camera images of auroras remains a challenging inverse problem. Existing auroral tomography techniques are often limited to simplified static settings, discrete spatial and energy grids, or strong assumptions on the electron energy spectrum. We propose to model the dynamic auroral electron precipitation field via a temporally conditioned neural network. The state of the precipitation field at each frame is represented by a per-frame latent code driven by learned discrete dynamics. A shared decoder maps horizontal positions and latent states to electron energy spectra. The predicted flux is converted to multi-wavelength volume emission rates and rendered into camera images accounting for delayed emissions. We evaluate the method on synthetic dynamic auroral sequences and real multi-view auroral videos, showing that the proposed representation produces temporally coherent precipitation reconstructions and image projections consistent with the observations.

</details>

#### 2026-11-12 - Reconstruct What You Can: Distractor-free 4D Gaussian Splatting

**Authors:** Joel Julin, Liuyue Xie, Ananya Bal, Mose Sakashita, Koichiro Niinuma, Laszlo A. Jeni
**Links:** [abs](https://arxiv.org/abs/2611.16259) - [pdf](https://arxiv.org/pdf/2611.16259)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, 4D Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reconstruct What You Can: Distractor-free 4D Gaussian Splatting
- 作者：Joel Julin, Liuyue Xie, Ananya Bal, Mose Sakashita, Koichiro Niinuma, Laszlo A. Jeni
- 出版日期：2026-11-12T03:59:45Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.16259 ；PDF https://arxiv.org/pdf/2611.16259

### 一句话总结
提出 ReCan-GS，一种 4D Gaussian Splatting 框架，利用从学习到的形变场导出的、基于 Jacobian 的形变敏感性分数区分一致场景内容与不一致观测，从而在无掩码、无预训练分割器、无介质专属监督的情况下抑制动态重建中的干扰物。

### 研究问题
从随意拍摄的视频进行动态重建时，需要在保留有效主体运动的同时抑制瞬态遮挡物、阴影和体积效应。现有方法要么通过静态场景假设抑制了有效运动，要么对所有观测联合建模，导致鬼影和不稳定几何。论文关注如何将一致的场景内容与不一致的观测分离开来。

### 核心思路/方法
ReCan-GS 从学习到的形变场中导出基于 Jacobian 的形变敏感性分数，并将其作为重建歧义的经验代理。该分数引导两种处理方式：一是将高斯分离为动态的 Core Gaussians 与逐视角的 Distractor Gaussians；二是对敏感的 Core Gaussians 进行事后剪枝。同一准则支持去除空间遮挡物、光度伪影以及演化中的烟雾或雾，且不需要掩码、预训练分割器或介质特定监督。

### 主要贡献
- 提出 ReCan-GS 4D Gaussian Splatting 框架，用于分离一致场景内容与不一致观测。
- 引入基于 Jacobian 的形变敏感性分数，作为重建歧义的经验代理，并用于 Core/Distractor 高斯分离或事后剪枝。
- 同一准则可处理空间遮挡物、光度伪影及演化烟雾/雾，无需掩码、预训练分割器或介质专属监督。
- 在合成与真实动态场景以及合成烟雾/雾场景上进行了实验，显示其在所评估的干扰物情形下具有效用。

### 局限性
摘要未提供足够信息。摘要未给出定量实验结果、具体失败情形、计算开销、对形变场质量的依赖程度，也未说明在何种干扰物类型或场景条件下可能失效。

### 阅读优先级
中。理由：该工作针对 casual video 动态重建中干扰物抑制这一明确问题，方法思路清晰且声称无需掩码或预训练分割器，具有一定通用性；但摘要仅提供方法概述与实验场景类型，未给出定量结果与失败分析，需阅读全文才能判断实际效果与适用边界。

</details>

<details>
<summary>Abstract</summary>

Dynamic reconstruction from casual video must preserve valid subject motion while suppressing transient occluders, shadows, and volumetric effects. Existing methods either suppress valid motion through static-scene assumptions or model all observations jointly, producing ghosting and unstable geometry. We introduce ReCan-GS, a 4D Gaussian Splatting framework that separates coherent scene content from inconsistent observations. It derives a Jacobian-based deformation-sensitivity score from the learned deformation field, using it as an empirical proxy for reconstruction ambiguity. The score guides separation into dynamic Core Gaussians and per-view Distractor Gaussians, or post-hoc pruning of sensitive Core Gaussians. The same criterion supports removal of spatial occluders, photometric artifacts, and evolving smoke or fog without masks, pretrained segmenters, or medium-specific supervision. Experiments on synthetic and real dynamic scenes and synthetic smoke/fog scenes demonstrate its usefulness across the evaluated distractor regimes.

</details>

#### 2026-11-11 - Topology-Aware 4D Gaussian Splatting for Egocentric Videos

**Authors:** Leonardo Vanni, Stefano Gasperini, Federico Tombari, Chiara Plizzari
**Links:** [abs](https://arxiv.org/abs/2611.16012) - [pdf](https://arxiv.org/pdf/2611.16012)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D Gaussian, Gaussian Splatting, splatting, embodied AI

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Topology-Aware 4D Gaussian Splatting for Egocentric Videos
- 作者：Leonardo Vanni, Stefano Gasperini, Federico Tombari, Chiara Plizzari
- 出版日期：2026-11-11T21:13:08Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2611.16012 ；PDF https://arxiv.org/pdf/2611.16012

### 一句话总结
论文针对第一人称单目视频中涉及拓扑变化（分裂、合并、打开、关闭）的动态场景重建，提出拓扑感知的 Topo-4DGS 方法，并构建 TopoEgo 基准，以缓解传统 4DGS 因依赖固定表示形变而产生的视觉伪影。

### 研究问题
从单目第一人称视频中重建动态场景与物体对具身智能很重要，但现有 4D Gaussian Splatting（4DGS）方法在处理切割、组装、打开或关闭等涉及拓扑变化的日常交互时表现不佳。其原因在于 4DGS 依赖对固定表示进行形变，当事件导致表面分裂、合并或显露时，会产生严重视觉伪影。论文要解决的是这一类拓扑变化下的动态重建问题。

### 核心思路/方法
论文提出 Topo-4DGS，一种拓扑感知的重建方法。其核心是联合建模部件级运动与时变表面支撑：为相互作用的部件分配独立的刚性变换，并随着表面出现、消失或分离而动态激活或停用高斯。论文还提出 TopoEgo，作为首个针对第一人称视频中拓扑变化的基准，覆盖 fission、fusion、open、close 四类事件。

### 主要贡献
- 指出并形式化第一人称视频中拓扑变化对 4DGS 的挑战：固定表示形变会导致分裂、合并或表面显露时出现严重伪影。
- 提出 TopoEgo 基准，专门覆盖第一人称视频中的拓扑变化，包括分裂、合并、打开、关闭。
- 提出 Topo-4DGS，通过部件级独立刚性变换与高斯动态激活/停用来处理拓扑变化。
- 摘要称大量实验表明 Topo-4DGS 在拓扑变化场景下显著优于当前最先进的 4DGS 方法，尤其是在事件发生后的帧上。

### 局限性
摘要未提供足够信息说明具体实验设置、数据集规模、评价指标、计算开销、失败案例或方法在不同场景条件下的泛化能力。摘要仅提到代码和数据将公开，未给出定量结果细节。

### 阅读优先级
高。理由：该论文直接针对 4DGS 在拓扑变化下的关键失效模式，问题定义清晰，且同时提出新基准与新方法；对动态/4D 重建、神经场景表示与第一人称视频理解方向具有较强相关性。但具体效果与可复现性需待全文和公开代码数据进一步确认。

</details>

<details>
<summary>Abstract</summary>

Reconstructing dynamic scenes and objects from monocular egocentric video is crucial for embodied AI, yet existing 4D Gaussian Splatting (4DGS) approaches struggle with everyday interactions involving topological changes, such as cutting, assembly, opening, or closing. Since 4DGS methods rely on deforming a fixed representation, events that split, merge, or reveal surfaces cause severe visual artifacts. To address this challenge, we introduce TopoEgo, the first benchmark dedicated to topological changes in egocentric video (covering fission, fusion, open, and close), alongside Topo-4DGS, a topology-aware reconstruction method. Topo4DGS jointly models part-level motion and time-varying surface support by assigning independent rigid transformations to interacting parts and dynamically activating or deactivating Gaussians as surfaces appear, disappear, or separate. Extensive experiments demonstrate that Topo-4DGS significantly outperforms state-of-the-art 4DGS approaches across topological changes, especially on post-event frames. Code and data will be made publicly available.

</details>

#### 2026-11-11 - Track4D: Representing Dense 3D Tracking for Video Diffusion Models

**Authors:** Yushi Lan, Zeren Jiang, Kelvin Li, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
**Links:** [abs](https://arxiv.org/abs/2611.15287) - [pdf](https://arxiv.org/pdf/2611.15287)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dense correspondence, 4D reconstruction, dynamic 3D

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Track4D: Representing Dense 3D Tracking for Video Diffusion Models
- 作者：Yushi Lan, Zeren Jiang, Kelvin Li, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
- 出版日期：2026-11-11T10:24:21Z
- 分类：Dynamic / 4D Reconstruction
- 链接：摘要页 https://arxiv.org/abs/2611.15287 ；PDF https://arxiv.org/pdf/2611.15287 ；项目页 https://nirvanalan.github.io/projects/track4d

### 一句话总结
论文研究如何复用预训练视频扩散模型（VDM）做稠密 3D 点跟踪，并系统比较两种把 3D 跟踪表示为“类视频信号”的方案。

### 研究问题
在训练数据稀缺的条件下，如何将基于海量视频预训练的 VDM 改用于稠密 3D 点跟踪。关键难点在于：3D 跟踪信号需要被表示为视频形式，而这种表示可能偏离 VDM 训练时所依赖的自然视频分布。

### 核心思路/方法
- 系统评估两种视频化表示：
  - **Residual 3D Tracking Video (RTV)**：编码每个像素相对于查询帧的 3D 偏移，可直接从生成的视频中恢复 3D 轨迹。
  - **Normalized Coordinate Map Video (NCMV)**：为每个像素标注随时间不变的规范坐标，更接近自然视频、更易被 VDM 学习，但需要借助现成 2D 跟踪器做后处理才能恢复 3D 轨迹。
- 以冻结的 Wan 骨干为基础，采用 LoRA 适配。
- 以现成 3D 重建器输出的 point maps 作为几何 scaffold 进行条件化。
- 仅使用一个动态 3D 跟踪数据集训练。
- 另有一个回归读出（regression readout），绕过视频 VAE 并使用额外训练数据，以进一步提升效果。

### 主要贡献
- 提出并比较 RTV 与 NCMV 两种用于 VDM 的稠密 3D 跟踪视频表示；摘要指出 RTV 跟踪更准确，而 NCMV 表明 VDM 能够以视频形式生成稠密对应关系。
- 在冻结 Wan 骨干上以 LoRA 适配、point maps 几何条件化和单一动态 3D 跟踪数据集训练，构建 Track4D。
- 在四个真实与合成基准上取得有竞争力的零样本跟踪表现。
- 通过绕过视频 VAE 的回归读出与额外训练数据获得进一步提升，展示该方向的潜力。

### 局限性
- 摘要未提供足够信息说明具体失败情形或定量局限。
- 摘要未提供足够信息说明 RTV 与 NCMV 的详细误差来源与计算开销对比。
- 摘要未提供足够信息说明对现成 3D 重建器和 2D 跟踪器的依赖程度及其误差传播影响。
- 摘要未提供足够信息说明单一训练数据集的覆盖范围与泛化边界。
- 摘要未提供足够信息说明回归读出所需额外训练数据的规模与可得性。

### 阅读优先级
中。理由：论文聚焦“复用视频扩散模型先验做稠密 3D 跟踪”这一明确问题，并给出两种表示的系统比较与零样本基准结果，对动态/4D 重建方向有参考价值；但摘要未展开实验细节、失败案例与计算成本，是否需要精读取决于读者对 VDM 先验迁移或稠密 3D 跟踪表示设计的直接兴趣。

</details>

<details>
<summary>Abstract</summary>

We study how to repurpose video diffusion models (VDMs), pretrained on millions of videos, for dense 3D point tracking, where training data is scarce. Doing so is non-trivial, as it requires representing 3D tracks as video-like signals that may lie outside the natural-video distribution on which the VDM was trained. We thus systematically assess the effectiveness of two such video representations. The first, Residual 3D Tracking Video (RTV), encodes per-pixel 3D offsets relative to a query frame and allows recovery of 3D trajectories directly from the generated video. The second, Normalized Coordinate Map Video (NCMV), labels each pixel with a canonical coordinate invariant through time. This is closer to a natural video and easier for the VDM to learn, but requires additional post-processing with an off-the-shelf 2D tracker to recover 3D tracks. RTV tracks more accurately, while NCMV shows that a VDM can generate dense correspondence as a video. We instantiate both representations with LoRA adaptation of a frozen Wan backbone, conditioned on point maps from an off-the-shelf 3D reconstructor as a geometric scaffold. Trained with a single dynamic 3D tracking dataset, Track4D achieves competitive zero-shot tracking on four real and synthetic benchmarks. A regression readout that bypasses the video VAE and uses additional training data brings further improvement, demonstrating the potential of this direction for dense 3D tracking. We hope our analysis will inspire future work that leverages VDM priors for dense 3D tracking and 4D reconstruction. Project page: https://nirvanalan.github.io/projects/track4d

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-11

#### 2026-11-16 - Polygraph: Large-Scale Multi-Session Trajectory Optimization using Pose Graphs

**Authors:** Petar Lukovic, Tian Yi Lim, Marc Pollefeys, Pablo Speciale, Hermann Blum, Zuria Bauer
**Links:** [abs](https://arxiv.org/abs/2611.21163) - [pdf](https://arxiv.org/pdf/2611.21163)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** metric depth, pose estimation, feature matching

<details>
<summary>Abstract</summary>

Robots, vehicles, and wearable devices often traverse the same environment many times. Each pass produces its own trajectory from onboard visual or visual-inertial odometry. These trajectories are locally accurate but drift over time and live in unrelated coordinate frames. Turning many such independent trajectories into one globally consistent set is the large-scale multi-session trajectory optimization problem. Existing solutions largely work offline. All sessions must be available up front, one session is fixed as the reference frame, and a single fused map is then optimized. This paper presents Polygraph, a multi-session trajectory optimization pipeline that processes sessions online, one keyframe and one spatial cluster at a time, and never builds a 3D map. Keyframes are grouped into local clusters. When a cluster closes, it is matched against every other session through learned image retrieval. Candidate pairs are verified with sparse feature matching, monocular metric depth, and robust pose estimation. A two-tier consensus gate admits a cross-session edge into the shared pose graph only once independent evidence corroborates it. A cheap incremental solve keeps the graph current, and a periodic robust batch solve prunes outliers. We evaluate Polygraph on stereo outdoor driving, HoloLens and iPad indoor traversals, legged indoor locomotion with a Boston Dynamics Spot, and large-scale outdoor vehicle and handheld routes. Against the closest prior work on the same GPU model, using its reported timings, Polygraph runs faster, commits fewer loop-closure edges, and matches or improves on accuracy.

</details>

#### 2026-11-16 - Correspondence-Free Camera Pose Estimation by Matching Moments

**Authors:** Subhransu S. Bhattacharjee, Dylan Campbell, Rahul Shome
**Links:** [abs](https://arxiv.org/abs/2611.20797) - [pdf](https://arxiv.org/pdf/2611.20797)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>Abstract</summary>

The blind perspective-$n$-point (PnP) problem is to estimate the pose of a calibrated camera from 2D and 3D point sets with unknown correspondences. We show that, for complete, noiseless observations, fourteen permutation-invariant image moments up to order four identify a fixed camera pose for almost every 3D point set containing at least twenty points. Our learning-free method, MomentPnP, matches these moments between the observed 2D points and the projected 3D points to initialize a camera pose without correspondences and refines the pose and correspondence weights using expectation--maximization. Across the test sets of three benchmarks, our method reduces median rotation error by $5$--$170\times$ relative to the best learned baseline, both with and without outliers. We recover accurate poses even with as many outliers as inliers. On dense ETH3D scans, pose accuracy improves as the point sets grow, even as individual correspondences become harder to resolve.

</details>

#### 2026-11-16 - sqrtVINS-Based 360 Visual-Inertial SLAM Systems: Hilti-Trimble SLAM Challenge 2026 Entry

**Authors:** Jungwoo Lee, Hogyun Kim, Jiwon Choi, Jinyong Jeong, Younggun Cho
**Links:** [abs](https://arxiv.org/abs/2611.20568) - [pdf](https://arxiv.org/pdf/2611.20568)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>Abstract</summary>

This report describes our submission to the 2026 Hilti-Trimble SLAM Challenge. The system is a 360-camera visual-inertial pipeline that uses only the provided dual-fisheye image streams and IMU measurements. First, raw images are preprocessed with low-light enhancement and static/dynamic masking, and then fed into a $\sqrt{\text{VINS}}$ frontend as the local odometry, with deep learning-based SuperPoint features, ELSED line segments, and LightGlue matching. The resulting trajectory is refined using a GTSAM-based backend that performs tightly-coupled factor graph optimization with SALAD global descriptor and visual bundle adjustment (BA). The backend performs local-to-global structureless BA, tightly regularized intrinsic and extrinsic refinement, and global scale adjustment supported by the known inter-camera baseline and cross-view constraints. The design targets long indoor sequences with dark regions, repetitive corridors, dynamic objects, and limited geometric parallax, while keeping the pipeline reproducible in the provided ROS2 workspace. Fig. 1 demonstrates that our proposed method aligns well with the floorplan across several indoor sequences.

</details>

#### 2026-11-16 - Pointillist Maize: 3D Reconstruction of Field-Grown Maize Using RGB UAV Imagery

**Authors:** Dewi Endah Kharismawati, Toni Kazic
**Links:** [abs](https://arxiv.org/abs/2611.20502) - [pdf](https://arxiv.org/pdf/2611.20502)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view stereo, structure from motion

<details>
<summary>Abstract</summary>

Three-dimensional reconstruction can extend field phenotyping to individual maize organs, but thin, flexible, occluding structures and plant movement complicate reconstruction. We evaluated whether consumer-grade UAV RGB video processed with Structure from Motion and multi-view stereo could recover recognizable field-grown maize structures, and examined the effects of acquisition trajectories and frame sampling. COLMAP reconstructions preserved recognizable leaves, stems, tassel branches, ears, silks, and brace roots. For an equal-frame comparison, we reconstructed one plant from two sets of 295 frames from the same video: a single orbit sampled at 5 frames/second and three orbits at different altitudes (ribbon skirt) sampled at 2 frames/second. After ground removal, the reconstructions contained 520,601 and 375,318 points, respectively. The single orbit yielded greater point concentration within plant structures and fewer visible gaps, while the ribbon skirt yielded fewer scattered points and slightly lower proportions of isolated points. In densely planted nursery rows, visible voids occupied 17.57% of the rendered scene with one orbit at 1 frame/second, decreasing to 5.07% with additional serpentine passes and 2.68% when the original orbit was sampled at 3 frames/second. Additional observations also increased point dispersion associated with plant movement. A curlicue trajectory tested in a different field in 2024 produced distinguishable individual plants without visible duplicated structures, although substantial voids remained, mainly on the soil surface. These results demonstrate the feasibility of recovering recognizable maize organs from consumer UAV imagery and reveal trade-offs between acquisition strategies, reconstruction completeness, and point dispersion. Independent geometric validation is still needed before quantitative phenotyping.

</details>

#### 2026-11-16 - Structure-Guided Multi-Granularity Spatiotemporal Transformer for Efficient Monocular 3D Human Pose Estimation

**Authors:** Sheng Xu, Aoduo Li, Rongli He
**Links:** [abs](https://arxiv.org/abs/2611.20361) - [pdf](https://arxiv.org/pdf/2611.20361)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Existing multi-granularity methods for monocular 3D human pose estimation emphasize spatial joint features while underusing skeletal structure, including global connectivity and temporal continuity. Moreover, modeling entire frame sequences incurs high computational costs. We propose a Structure-Aware Multi-Granularity Spatiotemporal Transformer that integrates structural priors across spatial and temporal representations for accurate and efficient pose estimation. A three-level feature extractor captures human topology at the joint, bone, and limb levels. Gated Adaptive Spatial Attention (GASA) embeds structural constraints into spatial attention, while Multi-Granularity Feature Enhancement (MGFE) uses hierarchical pooling and fusion to strengthen local details and global semantics. Temporal Segment Fusion (TSF) aligns temporal contexts across granularities to capture both short- and long-range motion patterns. Hierarchical Cross-Attention (HCA) promotes spatiotemporal interaction between granularities, and Keyframe Attention (KFA) selects informative motion segments to reduce redundancy and computational cost. Experiments demonstrate improved accuracy and efficiency over conventional Transformer-based approaches, highlighting the effectiveness of structure-aware multi-granularity modeling for monocular 3D human pose estimation.

</details>

#### 2026-11-15 - AstroPIE-53: Towards Understanding Failure Modes of Human Pose Estimation in Space

**Authors:** Stephanie Käs, Marten Flaig, Lukas Woyke, Osmanalp Ömeroğlu, Felix Krueckel, Onur Alp Çulha, Bastian Leibe
**Links:** [abs](https://arxiv.org/abs/2611.20207) - [pdf](https://arxiv.org/pdf/2611.20207)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>Abstract</summary>

Reliable monitoring of astronauts is essential for safety, situational awareness, and autonomous assistance in space missions. While modern computer vision enables accurate human detection and pose estimation on Earth, its robustness in space environments remains largely unquantified due to limited data availability. We present AstroPIE-53, a pilot dataset of 53 annotated astronaut videos collected from publicly available mission footage. To respect copyright restrictions, we release video identifiers, reconstruction scripts, and dense annotations rather than raw videos. The dataset includes bounding boxes, challenge classes, and human-annotated pose failure tags. We benchmark state-of-the-art person detection and pose estimation models under realistic zero-shot deployment conditions and perform the first systematic failure analysis for astronaut monitoring. Our results reveal substantial performance degradation caused by occlusions, unusual body orientations, low contrast, and microgravity motion patterns.

</details>

#### 2026-11-15 - SemLite-GS: Semantic-Selective Parallel Gaussian Splatting for Lightweight Building Reconstruction from UAV Oblique Imagery

**Authors:** Tengfei Wang, Xin Wang, Zihan Li, Quanjian Ji, Yifei Yu, Dong Lin, Zongqian Zhan
**Links:** [abs](https://arxiv.org/abs/2611.19773) - [pdf](https://arxiv.org/pdf/2611.19773)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** scene reconstruction, multi-view stereo, dense reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Lightweight 3D building models support urban spatial analysis, but their production often requires dense scene reconstruction, building extraction, and mesh simplification. Although 3D Gaussian Splatting (3DGS) is more efficient than conventional multi-view stereo, existing large-scale methods lack semantic selection and parallel instance-level training. We present SemLite-GS, a building-centric framework that reconstructs lightweight building meshes from large-scale UAV oblique imagery. First, an orthographic reference map establishes globally consistent building identities, which are propagated to oblique views to form camera-instance pairs and regions of interest. Second, semantic-selective parallel PGSR training jointly processes multiple pairs within relevant image regions while updating only target Gaussians; contextual Gaussians remain fixed to preserve visibility. Third, architectural planes extracted from rendered depth, opacity, and normal maps guide signed distance field optimization, producing meshes with adaptive polygon allocation and well-defined structural boundaries. Experiments on multiple large-scale UAV datasets demonstrate that our SemLite-GS substantially reduces building reconstruction time compared with representative full-scene 3DGS methods. With comparable polygon budgets, SemLite-GS achieves superior preservation of dominant planar structures and sharp architectural transitions compared with conventional dense reconstruction followed by mesh decimation. The source code is available at https://github.com/IRIS-LAB-whu/SemLite-GS.

</details>

#### 2026-11-12 - EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion

**Authors:** Laiyan Ding, Chongxi Meng, Rui Huang
**Links:** [abs](https://arxiv.org/abs/2611.16793) - [pdf](https://arxiv.org/pdf/2611.16793)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EG360: Efficient and Generalizable $360^\circ$ Depth Estimation via Adaptive Panorama-Perspective Distillation and Spherical Cross-Level Feature Fusion
- 作者：Laiyan Ding, Chongxi Meng, Rui Huang
- 出版日期：2026-11-12T13:38:57Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2611.16793) / [PDF](https://arxiv.org/pdf/2611.16793)

### 一句话总结
EG360 是一个以轻量深度模型为基础的全景深度估计模型，通过自适应全景-透视蒸馏（APPD）和球面跨层特征融合（SCFF），在仅 6.593M 参数（重参数化后）下实现较强零样本泛化，并在 Jetson Orin NX 16GB（MAXN 模式）上达到 35 FPS。

### 研究问题
论文关注全景深度估计中“强泛化但计算昂贵”与“轻量但泛化差”两类模型之间的差距：使用大型预训练模型的方法零样本泛化较好，但高计算成本使嵌入式平台实时推理困难；此前的轻量全景模型多面向单域评估，因域偏移而泛化不佳。作者希望构建同时兼顾高效与可泛化的全景深度估计模型。

### 核心思路/方法
- 以轻量深度模型为基础构建 EG360。
- 设计自适应全景-透视蒸馏策略（Adaptive Panorama-Perspective Distillation, APPD），并由场景几何引导。
- 引入球面跨层特征融合模块（Spherical Cross-Level Feature Fusion, SCFF），用于全局语义感知。
- 通过重参数化后仅 6.593M 参数，在真实世界基准上取得较强零样本性能，并在 Jetson Orin NX 16GB（MAXN 模式）上以 35 FPS 运行；摘要称此前 ViT-small 模型在该设备上低于 2 FPS。

### 主要贡献
- 提出 EG360，一个高效且可泛化的全景深度估计模型，旨在缩小强泛化大模型与轻量单域模型之间的差距。
- 提出由场景几何引导的自适应全景-透视蒸馏策略 APPD。
- 提出用于全局语义感知的球面跨层特征融合模块 SCFF。
- 在仅 6.593M 参数（重参数化后）条件下，于真实世界基准取得较强零样本性能，并在指定嵌入式平台上实现 35 FPS；摘要提及代码将公开。

### 局限性
- 摘要未提供足够信息说明 APPD 中场景几何引导的具体形式、蒸馏损失设计及训练数据构成。
- 摘要未提供足够信息说明所采用的真实世界基准名称、零样本评估指标数值及与具体对比方法的完整结果。
- 摘要未提供足够信息说明 SCFF 的具体网络结构、融合层级与计算开销分析。
- 摘要未提供足够信息说明 35 FPS 对应的输入分辨率、精度设置及端到端流水线范围。
- 摘要未提供足够信息说明方法在不同域偏移类型或极端场景下的失败模式与局限性讨论。

### 阅读优先级
中。理由：该论文聚焦全景深度估计的轻量化与零样本泛化，并给出嵌入式平台实时性结果，对关注高效 3D 感知与全景深度估计的研究者有参考价值；但摘要未提供具体基准、指标数值和消融细节，需阅读全文才能判断方法有效性与可复现性。

</details>

<details>
<summary>Abstract</summary>

Generalized panorama depth estimation has witnessed great advances in recent years. These methods typically achieve robust zero-shot generalization performance using large pretrained models, but their high computational cost makes real-time inference on embedded platforms challenging. In contrast, previous lightweight panorama models have mostly been developed for single-domain evaluations and cannot generalize well due to domain shifts. To reduce the gap between these two types of models, we introduce EG360, an efficient and generalizable panorama depth estimation model. Specifically, building on a lightweight depth model, we design an Adaptive Panorama-Perspective Distillation (APPD) strategy guided by scene geometry, along with a Spherical Cross-Level Feature Fusion (SCFF) module for global semantic perception. As a result, with only 6.593M parameters after reparameterization, EG360 achieves strong zero-shot performance on real-world benchmarks and runs at 35 FPS on a Jetson Orin NX 16GB in MAXN mode, whereas a previous ViT-small model runs at less than 2 FPS. Our code will also be made public for future research.

</details>

#### 2026-11-12 - RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5

**Authors:** Himanshu Patil, Jaideep Joshi, Rohit Saluja, Ganesh Ramakrishnan
**Links:** [abs](https://arxiv.org/abs/2611.16472) - [pdf](https://arxiv.org/pdf/2611.16472)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5
- 作者：Himanshu Patil, Jaideep Joshi, Rohit Saluja, Ganesh Ramakrishnan
- 出版日期：2026-11-12T08:29:56Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类摘要未提供
- 链接：摘要页 https://arxiv.org/abs/2611.16472 ；PDF https://arxiv.org/pdf/2611.16472

### 一句话总结
该论文在 Raspberry Pi 5 上对 RTAB-Map 与 ORB-SLAM3 两套 RGB-D SLAM 系统进行基准测试与分阶段、函数级性能剖析，重点报告跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度，并指出精度比较因运行间轨迹误差波动而无法定论。

### 研究问题
论文关注的问题是：在 ARM 边缘板（Raspberry Pi 5）上，标准 RGB-D SLAM 系统的实际运行表现如何。摘要指出，无 GPS 的微型飞行器常在 ARM 边缘板上运行 SLAM，但关于标准 RGB-D SLAM 系统在此类硬件上行为表现的公开数据很少。因此，论文以 RTAB-Map 和 ORB-SLAM3 为对象，考察其在边缘硬件上的跟踪覆盖、精度、耗时、资源占用与热行为。

### 核心思路/方法
- 在 Raspberry Pi 5 上使用 6 个 TUM RGB-D 序列、3 种图像分辨率对 RTAB-Map 和 ORB-SLAM3 进行基准测试。
- 每次运行记录跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度。
- 对两套系统进行阶段级和函数级剖析。
- RTAB-Map 被配置为处理并保留每一帧，因此其后端每帧运行，而不是按其默认 1 Hz 频率运行。
- 汇报结果时强调时间与精度必须结合覆盖率解读：在四分之一分辨率下，两套系统在多数序列上丢失跟踪，而丢失跟踪的运行更早结束，并且在其保留的位姿上报告更低误差。

### 主要贡献
- 提供了 RTAB-Map 与 ORB-SLAM3 在 Raspberry Pi 5 上使用 TUM RGB-D 序列的基准测试数据，覆盖 3 种分辨率，并记录跟踪覆盖率、轨迹误差、每帧时间、内存、CPU 负载和温度。
- 给出了两套系统的阶段级与函数级剖析结果。
- 报告了具体耗时特征：在所有配置均能跟踪的序列上，RTAB-Map 前端每帧 38–74 ms、完整流水线 150–462 ms；ORB-SLAM3 分别为 13–45 ms 和 26–62 ms。
- 指出 RTAB-Map 的主要开销来自优化不断增长的位姿图，原因是其默认工作内存无界；ORB-SLAM3 的局部 bundle adjustment 开销约与跟踪相当，但运行在并行线程中。
- 指出计时可重复性在 1–5% 以内，但相同运行之间的轨迹误差波动可达 27%，因此两系统之间的精度差异无法定论。
- 报告未发生热降频。

### 局限性
- 摘要未提供足够信息说明除 Raspberry Pi 5 之外的硬件平台、其他边缘设备的对比结果。
- 摘要未提供足够信息说明 6 个 TUM RGB-D 序列的具体名称与场景构成。
- 摘要未提供足够信息说明内存、CPU 负载和温度的具体数值或统计方式。
- 摘要未提供足够信息说明函数级剖析的具体工具与热点函数清单。
- 摘要未提供足够信息说明 RTAB-Map 非默认配置对结论外推的影响范围。
- 摘要未提供足够信息说明精度比较的统计检验方法；仅指出轨迹误差波动可达 27%，精度差异无法定论。
- 摘要未提供足够信息说明四分之一分辨率下丢失跟踪的具体序列数量与原因分析。

### 阅读优先级
中。理由：该论文针对 ARM 边缘板上的 RGB-D SLAM 基准测试与性能剖析，提供了 RTAB-Map 与 ORB-SLAM3 在 Raspberry Pi 5 上的耗时、覆盖率与资源数据，并对精度比较给出谨慎结论；对关注边缘部署、系统选型与性能瓶颈的读者有直接参考价值。但摘要显示精度差异无法定论，且实验范围限于摘要所述平台、序列与配置，若读者更关注算法精度创新或更广泛硬件对比，则需要进一步查看全文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Micro aerial vehicles that operate without GPS often run SLAM on ARM-based edge boards, yet there is little published data on how standard RGB-D SLAM systems behave on such hardware. We benchmark RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5 using six TUM RGB-D sequences at three image resolutions, recording tracking coverage, trajectory error, time per frame, memory, CPU load and temperature for every run, and we profile both systems at the stage and function level. RTAB-Map was configured to process and keep every frame, so its back end runs on every frame rather than at its default rate of 1 Hz. On the sequences that every configuration tracked, its front end takes 38-74 ms per frame and its full pipeline 150-462 ms, compared with 13-45 ms and 26-62 ms for ORB-SLAM3. RTAB-Map's main cost is optimizing a pose graph that keeps growing, because its working memory is unbounded by default; ORB-SLAM3's local bundle adjustment costs about as much as its tracking but runs in a parallel thread. At quarter resolution, both systems lose tracking on most sequences, and runs that lose tracking finish sooner and report lower error on the poses they keep, so time and accuracy must be read alongside coverage. Timing is repeatable to within 1-5%, but trajectory error varies by up to 27% between identical runs, so the accuracy differences between the two systems are inconclusive. No thermal throttling occurred.

</details>

#### 2026-11-11 - SCR-Mamba: Skeleton-conditioned Mamba with cross-scale incremental refinement for efficient 3D human pose estimation

**Authors:** Jie Wang, Xuejing Gu, Congzhe Zhang, Zibo Zhao
**Links:** [abs](https://arxiv.org/abs/2611.15526) - [pdf](https://arxiv.org/pdf/2611.15526)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SCR-Mamba: Skeleton-conditioned Mamba with cross-scale incremental refinement for efficient 3D human pose estimation
- 作者：Jie Wang, Xuejing Gu, Congzhe Zhang, Zibo Zhao
- 出版日期：2026-11-11T14:14:27Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.15526) / [PDF](https://arxiv.org/pdf/2611.15526)

### 一句话总结
论文提出 SCR-Mamba，通过将骨骼结构关系条件化注入 Mamba 的状态建模过程，并以跨尺度增量细化减少全分辨率时序计算，从而在视频 3D 人体姿态估计中兼顾精度与效率。

### 研究问题
摘要指出，基于 Mamba 的视频 3D 人体姿态估计方法虽能以线性复杂度建模长序列，但存在两点不足：
1. 选择性状态更新通常未直接利用骨骼关系；
2. 在全时序分辨率上堆叠建模模块会带来较高计算开销，而压缩时序序列又难以保留逐帧细节。

### 核心思路/方法
论文的核心由两个模块构成：
- **Skeleton-Conditioned State Modeling, SCSM**：从骨骼连接和左右对称关系中生成骨骼上下文，并以该上下文为条件生成空间分支与时间分支的选择性参数，使结构关系参与状态信息的写入、传播和读取。
- **Cross-Scale Incremental Refinement, CSIR**：通过内容自适应聚合构建多尺度运动表示，并用粗尺度建模产生的增量逐步细化保留的逐帧特征，在整合长程运动上下文的同时减少全分辨率计算。

### 主要贡献
基于摘要可归纳为：
1. 提出 SCR-Mamba，将骨骼结构条件引入 Mamba 的选择性状态建模，使骨骼关系直接参与状态更新相关过程。
2. 提出 CSIR，以跨尺度增量细化方式整合长程运动上下文并降低全分辨率计算开销。
3. 在 Human3.6M 上，SCR-Mamba-L 在使用 Stacked Hourglass 2D 检测和 243 帧输入时达到 36.8 mm MPJPE（P1），参数量 7.72 M、MACs 15.10 G，计算成本低于 StructMamPose-L 的 1/7 且精度相近；SCR-Mamba-X 达到 36.6 mm P1 和 30.9 mm P-MPJPE（P2），摘要称其取得 state-of-the-art 性能。
4. 在 MPI-INF-3DHP 上，SCR-Mamba-X 取得 PCK 99.3%、AUC 88.1%、MPJPE 14.2 mm。

### 局限性
- 摘要未提供足够信息说明方法在更广泛数据集、跨数据集泛化或真实场景遮挡条件下的表现。
- 摘要未提供足够信息说明 SCSM 与 CSIR 各模块的消融实验细节及各自贡献比例。
- 摘要未提供足够信息说明失败案例、误差分布或对 2D 检测质量的敏感性分析。
- 摘要未提供足够信息说明训练成本、推理延迟以外的实际部署开销。

### 阅读优先级
**高**。理由：论文聚焦视频 3D 人体姿态估计中 Mamba 方法的结构关系利用与计算效率问题，摘要给出了明确的模块设计、Human3.6M 与 MPI-INF-3DHP 上的量化结果，并声称在相近精度下显著降低计算成本，同时达到 state-of-the-art 性能；对关注高效时序建模与骨架结构先验的研究方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Mamba-based methods for video-based 3D human pose estimation can model long sequences with linear complexity, but their selective state updates usually lack direct exploitation of skeletal relations. Meanwhile, stacking modeling blocks at the full temporal resolution leads to high computational overhead, while compressing the temporal sequence makes it difficult to retain per-frame details. To address these issues, we propose SCR-Mamba, whose core consists of Skeleton-Conditioned State Modeling (SCSM) and Cross-Scale Incremental Refinement (CSIR). SCSM generates a skeleton context from bone connections and left-right symmetry relations and generates the selective parameters of the spatial and temporal branches conditioned on it, so that structural relations are involved in the writing, propagation, and reading of state information. CSIR constructs multi-scale motion representations through content-adaptive aggregation and progressively refines the retained per-frame features with the increments produced by coarse-scale modeling, integrating long-range motion context while reducing full-resolution computation. On Human3.6M with Stacked Hourglass (SH) 2D detections and 243-frame inputs, SCR-Mamba-L achieves 36.8 mm MPJPE (P1) with 7.72 M parameters and 15.10 G MACs, less than 1/7 of the computational cost of StructMamPose-L with similar accuracy; SCR-Mamba-X further reaches 36.6 mm P1 and 30.9 mm P-MPJPE (P2), achieving state-of-the-art performance. On MPI-INF-3DHP, SCR-Mamba-X achieves a percentage of correct keypoints (PCK) of 99.3%, an area under the curve (AUC) of 88.1%, and an MPJPE of 14.2 mm.

</details>

#### 2026-11-11 - ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction

**Authors:** Prasanna S, Gopi Raju Matta, Divya Madhuri Vemunuri, Kaushik Mitra
**Links:** [abs](https://arxiv.org/abs/2611.15435) - [pdf](https://arxiv.org/pdf/2611.15435)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 3D reconstruction, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ThermalSplat: Generalizable Pose-Free Gaussian Splatting for Sparse-View Thermal 3D Reconstruction
- 作者：Prasanna S, Gopi Raju Matta, Divya Madhuri Vemunuri, Kaushik Mitra
- 出版日期：2026-11-11T13:09:30Z
- 分类：3D Reconstruction & Multi-view Geometry；Neural Scene Representations & Rendering
- 链接：摘要 https://arxiv.org/abs/2611.15435 ；PDF https://arxiv.org/pdf/2611.15435

### 一句话总结
ThermalSplat 提出一种可泛化、无位姿依赖、无需 RGB 引导和逐场景训练的前馈式高斯泼溅框架，旨在直接从稀疏热红外图像重建三维场景。

### 研究问题
论文关注热红外图像在三维场景表示中的瓶颈：热图像纹理弱、发射率具有视角依赖性，导致标准位姿估计器容易失败，并使标准 3D Gaussian Splatting 在稀疏视角约束下失效。现有热重建方法通常依赖密集采集和昂贵的逐场景优化，且许多方法需要对齐的 RGB-热红外数据集来获得可靠相机位姿与初始点云，因而无法用于纯热红外、无位姿环境。论文要解决的问题是：如何在仅有稀疏热红外图像、没有已知相机位姿、没有 RGB 引导且不进行逐场景训练的条件下，实现可泛化的热三维重建。

### 核心思路/方法
论文提出 ThermalSplat，声称是首个可泛化、前馈式高斯泼溅框架，可直接从稀疏热图像重建三维场景，不依赖已知相机位姿、RGB 引导或逐场景训练。针对热红外特有问题，方法采用 soft census loss 进行亮度不变的结构匹配，并采用 boundary structure loss 显式监督温度不连续边界。模型在聚合的多源数据集上训练，并在单次前馈过程中合成未见场景的重建结果。

### 主要贡献
- 提出 ThermalSplat，一个可泛化、前馈式的高斯泼溅框架，用于稀疏热图像的三维重建，且不要求已知相机位姿、RGB 引导或逐场景训练。
- 针对热图像低纹理与视角依赖发射率问题，引入 soft census loss 以实现亮度不变的结构匹配。
- 引入 boundary structure loss，显式监督温度不连续区域。
- 在聚合多源数据集上训练后，模型可在单次前馈中重建未见场景。
- 摘要称实验表明，在稀疏条件下 ThermalSplat 相对场景特定热泼溅方法具有严格优势；即使与这些基线在其理想密集采集设置下相比，ThermalSplat 也取得更优的感知保真度。

### 局限性
摘要未提供足够信息说明方法的具体失败场景、计算资源需求、训练数据规模与组成细节、对不同热传感器或场景类型的泛化边界，以及定量实验指标和消融结果。摘要也未提供足够信息说明无位姿条件下的绝对尺度、位姿估计精度或实时性能。

### 阅读优先级
高。理由：该论文针对稀疏、无位姿、纯热红外条件下的三维重建这一明确瓶颈，提出前馈式可泛化框架，并声称在稀疏条件下优于场景特定方法、在感知保真度上优于密集设置基线；若这些声明在论文中得到充分验证，对热三维重建、无位姿高斯泼溅和稀疏视角重建方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Thermal infrared imaging is vital for applications like search-and-rescue and autonomous navigation, yet trans- lating it into 3D scene representations remains a critical bottleneck. The low-texture nature and view-dependent emissivity of thermal images cause standard pose estima- tors to fail catastrophically, collapsing standard 3D Gaus- sian Splatting pipelines under sparse-view constraints. Fur- thermore, existing thermal reconstruction methods rely heavily on dense capture and computationally expensive per-scene optimization. Critically, many of these ap- proaches depend on aligned RGB-thermal datasets to ob- tain reliable camera poses and initial point clouds, ren- dering them unusable in purely thermal, unposed envi- ronments. To break this bottleneck, we present Thermal- Splat, the first generalizable, feed-forward Gaussian splat- ting framework that reconstructs 3D scenes directly from sparse thermal images without requiring known camera poses, RGB guidance, or per-scene training. We over- come thermal-specific challenges using a soft census loss for brightness-invariant structural matching and a bound- ary structure loss to explicitly supervise temperature discon- tinuities. Trained on an aggregated multi-source dataset, ThermalSplat synthesizes sharp reconstructions of unseen scenes in a single feed-forward pass. Extensive experi- ments demonstrate that ThermalSplat holds a strict advan- tage over scene-specific thermal splatting methods in the sparse regime. Furthermore, even compared against these baselines operating under their ideal dense capture set- tings, ThermalSplat achieves superior perceptual fidelity. By eliminating the need for computationally expensive per scene optimization, ThermalSplat offers an efficient and generalizable approach to thermal 3D reconstruction.

</details>

#### 2026-11-11 - Multi-View 3D Reconstruction Using V-JEPA Features

**Authors:** Anwar Shamim, Jeffrin Sam
**Links:** [abs](https://arxiv.org/abs/2611.15143) - [pdf](https://arxiv.org/pdf/2611.15143)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Multi-View 3D Reconstruction Using V-JEPA Features
- 作者：Anwar Shamim, Jeffrin Sam
- 出版日期：2026-11-11T07:33:05Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.15143) / [PDF](https://arxiv.org/pdf/2611.15143)

### 一句话总结
论文研究仅使用 RGB 图像的多视角三维重建，将视频预训练特征与相机估计、场景聚合、极线传输和残差点图结合，并在 CO3D 和 TUM RGB-D 上比较不同相机回归与联合相对目标配置的效果。

### 研究问题
如何将预测式视频编码器提供的稠密视觉表示用于多视角三维重建，并考察相机估计方式、联合相对目标以及细化步骤对深度、相机位姿和重建几何的影响。摘要强调，在将重建增益归因于预测式视频预训练之前，需要先对组件和编码器进行隔离比较。

### 核心思路/方法
摘要给出的方法框架包括：视频预训练特征、相机估计、场景聚合、极线传输和残差点图，用于监督式、仅 RGB 的多视角重建。实验比较了全局相机回归与空间相机回归，并比较了带联合相对目标的配置；在 CO3D 上使用五视图窗口进行评估，同时使用一个独立训练的 TUM RGB-D 模型进行室内窗口实验。摘要还提到对结果进行了 refinement，并报告了深度与位姿之间的竞争性影响。

### 主要贡献
- 提出并研究一种结合视频预训练特征、相机估计、场景聚合、极线传输和残差点图的 RGB-only 多视角重建架构。
- 在 CO3D 的 168 个五视图窗口上比较全局与空间相机回归：空间相机配置的绝对轨迹误差比全局相机配置低 29.3%，但其轨迹误差差于 identity poses，深度误差差于全局配置。
- 报告联合相对目标配置的效果：归一化内参误差和相似度对齐 Chamfer 距离从 0.6447 改善到 0.5573，但原始 Chamfer 距离从 3.5535 增加到 4.4374。
- 在 163 个室内窗口上报告：相机误差为 0.3063 m，identity poses 为 0.3694 m；深度误差为 0.4279，constant median depth 为 0.2516；refinement 使室内相机误差变差。
- 结果区分了表示适配、对齐后的形状和原始重建，并指出在将重建增益归因于预测式视频预训练前，需要进行隔离的组件与编码器比较。

### 局限性
- 摘要仅给出有限数据集与窗口数量上的结果，未提供完整实验设置、训练细节、基线细节或统计显著性信息。
- 摘要显示方法在多项指标上并未全面优于简单基线，例如空间相机配置的轨迹误差差于 identity poses、深度误差差于全局配置；联合相对目标在原始 Chamfer 距离上变差；室内深度误差差于 constant median depth；refinement 使室内相机误差变差。
- 摘要未提供关于 V-JEPA 特征本身与其他编码器的隔离比较结果，也未提供组件消融的完整信息。
- 摘要未提供足够信息说明模型在更多数据集、更多视角数量或真实复杂场景中的泛化能力。
- 摘要未提供足够信息说明计算成本、推理速度、内存需求或实现细节。

### 阅读优先级
中。理由：论文主题属于多视角三维重建与视频预训练特征结合的方向，且摘要明确报告了相机回归、联合目标和 refinement 的正负结果，对评估“视频预训练特征是否真正带来重建增益”有参考价值；但摘要也显示结果存在明显竞争与不一致，且缺少完整实验细节，适合作为需要进一步核对全文方法与实验设计的阅读材料。

</details>

<details>
<summary>Abstract</summary>

Predictive video encoders provide dense visual representations, but adapting them to 3D reconstruction requires accurate depth, camera poses, and cross-view geometry. We study supervised RGB-only multi-view reconstruction using an architecture that combines video-pretrained features, camera estimation, scene aggregation, epipolar transport, and residual pointmaps. Experiments compare global and spatial camera regression with joint relative objectives on CO3D, alongside an independently trained TUM RGB-D model. On 168 CO3D five-view windows, the spatial-camera configuration achieves 29.3% lower absolute trajectory error than the global-camera configuration, but performs worse than identity poses in trajectory error and worse than the global configuration in depth error. The joint relative-objective configuration improves normalized intrinsics error and similarity-aligned Chamfer distance from 0.6447 to 0.5573, but increases raw Chamfer distance from 3.5535 to 4.4374. On 163 indoor windows, camera error is 0.3063 m versus 0.3694 m for identity poses, while depth error is 0.4279 versus 0.2516 for constant median depth. Refinement worsens indoor camera error, and additional experiments show competing depth and pose effects. Overall, the results distinguish representation adaptation, aligned shape, and raw reconstruction, highlighting the need for isolated component and encoder comparisons before attributing reconstruction gains to predictive video pretraining.

</details>

#### 2026-11-11 - MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments

**Authors:** Hyunjun Kim, Youngjin Seo, Sungwon Seo, Jiyou Shin, Kunwoo Kim, Chanyong Park, Hyungpil Moon
**Links:** [abs](https://arxiv.org/abs/2611.15066) - [pdf](https://arxiv.org/pdf/2611.15066)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments
- 作者：Hyunjun Kim, Youngjin Seo, Sungwon Seo, Jiyou Shin, Kunwoo Kim, Chanyong Park, Hyungpil Moon
- 出版日期：2026-11-11T05:34:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.15066) / [PDF](https://arxiv.org/pdf/2611.15066)

### 一句话总结
提出 MiniPose：先制作大型工业管段的缩小实体复制品，用真实 RGB-D 相机采集多姿态数据，再把深度图按逆缩放变换对应到全尺寸物体的几何表示，从而以较低采集负担引入真实外观与真实深度传感器测量特性。

### 研究问题
大型重型工业物体（如船厂大型管道系统、石化装置结构件）的 6-DOF 位姿估计在机器人感知中研究相对不足。反复搬动这类大物体在物理和空间上都很困难，因此难以获得姿态多样性足够的真实训练数据；合成数据虽可扩展，但难以忠实复现真实 RGB-D 观测，尤其是真实深度传感器的结构化测量误差。论文关注如何同时缓解真实数据采集负担与 sim-to-real 差距。

### 核心思路/方法
- 制作目标物体的缩小版复制品，用真实 RGB-D 相机采集其多种姿态下的 RGB-D 数据。
- RGB 图像直接使用；深度图通过简单的逆缩放变换，转换为与全尺寸物体几何一致的表示。
- 将少量缩微模型真实图像与大量合成图像混合训练，使训练过程能纳入仅靠合成数据难以复现的真实外观和传感器测量特性。
- 为检验收益是否依赖特定网络，选择两种不同形式的 RGB-D 位姿估计器 PVN3D 与 RDPN6D 进行评估。
- 摘要报告：每种管型最多混入 1,000 张缩微图像（不足训练数据的 10%）与 10,000 张合成图像，两种估计器在多种管型上的平均 ADD-S AUC 均优于仅用合成数据训练；与全尺寸真实数据训练的比较进一步表明，在难以进行全尺寸采集时缩微数据可作为替代。

### 主要贡献
- 提出基于缩微模型的真实 RGB-D 数据采集流程 MiniPose，针对大型工业管段的 6-DOF 位姿估计。
- 通过逆缩放把缩微深度图映射为全尺寸物体的几何一致表示，使真实采集数据可与合成数据混合用于训练。
- 在两种不同形式的 RGB-D 位姿估计器上验证混合缩微真实数据相对纯合成训练的 mean ADD-S AUC 提升，说明收益不限于单一网络。
- 与全尺寸真实数据训练比较，提示缩微数据可在全尺寸采集困难时作为代理，降低大型工业物体的数据采集负担。

### 局限性
- 摘要未提供足够信息说明逆缩放变换对真实深度传感器结构化误差的保持程度与适用范围。
- 摘要未提供足够信息说明缩微复制品与全尺寸物体在材质、表面特性、光照条件等方面的差异及其影响。
- 摘要未提供足够信息说明实验涉及的管段类型数量、具体姿态分布、相机型号与采集环境。
- 摘要未提供足够信息说明与全尺寸真实数据训练比较时的具体数据量、性能差距及统计细节。
- 摘要未提供足够信息说明方法对其他大型工业物体或非管段类目标的泛化能力。

### 阅读优先级
中。理由：论文针对大型工业物体 6-DOF 位姿估计中真实数据采集困难这一实际问题，提出可操作的缩微实物采集与深度逆缩放方案，并在两种位姿估计器上报告一致增益，对工业机器人感知与 sim-to-real 数据构建有参考价值；但摘要未给出更细的实验设置、误差保持机制与跨物体泛化证据，需阅读全文后才能判断其适用边界。

</details>

<details>
<summary>Abstract</summary>

6-DOF pose estimation of large and heavy industrial objects, such as large piping systems in shipyards and structural components in petrochemical plants, remains relatively underexplored in robotic perception. Repeatedly repositioning large objects is physically and spatially demanding, making it difficult to acquire real training data with sufficient pose diversity. Synthetic data offer a scalable alternative, but faithfully reproducing real RGB-D observations, particularly the structured measurement errors of real depth sensors, remains difficult. We propose MiniPose, a practical pipeline for miniature-based real RGB-D data collection that addresses both the data-acquisition burden and the sim-to-real gap. We fabricate a scaled-down replica and capture RGB-D data of it in diverse poses using a real RGB-D camera. RGB images are used directly, while depth maps are converted to a geometrically consistent representation of the full-scale object via a simple inverse scaling transformation. This allows training to incorporate real appearance and sensor measurement characteristics that are difficult to reproduce using synthetic data alone. To examine whether the benefit depends on a particular network, we evaluate two RGB-D pose estimators with different formulations, PVN3D and RDPN6D. Mixing at most 1,000 miniature images per pipe type, less than 10\% of the training data, with 10,000 synthetic images improves the mean ADD-S AUC across pipe types over synthetic-only training for both estimators. A comparison with training on full-scale real data further suggests that miniature data can serve as a proxy where full-scale collection is difficult, reducing the data-collection burden for large industrial objects.

</details>

#### 2026-11-11 - Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion

**Authors:** Dimitrios Chatziparaschis, Georgios Georgakis, Adnan I. Ansar, Shehryar Khattak, Konstantinos Karydis
**Links:** [abs](https://arxiv.org/abs/2611.14958) - [pdf](https://arxiv.org/pdf/2611.14958)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth prediction, depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion
- 作者：Dimitrios Chatziparaschis, Georgios Georgakis, Adnan I. Ansar, Shehryar Khattak, Konstantinos Karydis
- 出版日期：2026-11-11T03:09:13Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2611.14958) / [PDF](https://arxiv.org/pdf/2611.14958)

### 一句话总结
论文提出 EM-ViT，一个在机器人运行过程中在线适配单目深度基础模型相对深度输出的轻量级 Vision Transformer 模型，通过稠密视差细化与有效基线标量预测恢复度量尺度，并可选用机器人自运动信息进行快速训练。

### 研究问题
在未知和非结构化环境中，机器人需要几何理解能力以保障安全高效运行。单目深度估计基础模型可提供稠密长距离深度预测，替代昂贵的 LiDAR 和立体相机等机载硬件。但这类离线模型主要在仿射不变深度表示上训练，其在新颖场景中的泛化能力仍不明确。论文关注的核心问题是：如何利用机器人运行中采集的观测，在线适配基础模型给出的相对深度输入，使其适用于新场景。

### 核心思路/方法
论文提出 EM-ViT 模型。方法受立体相机参数化启发，将深度预测分解为两部分：一是通过稠密视差细化恢复场景的相对结构，二是通过有效基线标量预测确定缺失的度量尺度。学习过程利用稀疏 LiDAR 点和可选的机器人自运动（Ego-Motion）信息，快速训练一个轻量级 Vision Transformer。同时，内部引入梯度匹配损失，以在实时条件下保留输入视差的细粒度语义结构。

### 主要贡献
- 提出 EM-ViT，一种能够在线适配基础模型相对深度输入的单目深度估计模型，用于新场景下的机器人操作。
- 借鉴立体相机参数化，将深度预测分解为稠密视差细化与有效基线标量预测，以分别恢复相对结构和度量尺度。
- 利用稀疏 LiDAR 点及可选的机器人自运动信息快速训练轻量级 ViT，并通过梯度匹配损失实时保持输入视差的细粒度语义结构。
- 在 KITTI 等公开序列上进行验证，摘要称其在线学习流程相比现有 MDE 基础模型能够更快、更高精度地适配新场景。

### 局限性
- 摘要未提供足够信息说明方法在无 LiDAR 或自运动信息不可用时的具体性能。
- 摘要未提供足够信息说明计算开销、实时性量化指标及不同硬件平台上的表现。
- 摘要未提供足够信息说明除 KITTI 外其他数据集或真实机器人场景的系统性评估结果。
- 摘要未提供足够信息说明与基线方法对比的完整实验设置与消融细节。
- 代码与补充材料标注为“将公开”，摘要未提供足够信息说明当前可获取状态。

### 阅读优先级
中。理由：该论文聚焦单目深度基础模型在新场景中的在线适配问题，结合视差细化、度量尺度恢复与机器人自运动，问题定位清晰且对机器人感知有潜在价值；但摘要仅给出有限实验信息（主要提及 KITTI），且发表于未来日期，实际实验细节、泛化性与实时性证据需进一步阅读全文确认。

</details>

<details>
<summary>Abstract</summary>

The geometric understanding of a scene is a crucial component for safe and efficient robotic operations in novel and unstructured environments. The recent emergence of foundation models for Monocular Depth Estimation (MDE) has provided an opportunity to enrich robotic perception capabilities with dense long-range depth predictions, replacing expensive onboard hardware (e.g., LiDARs and stereo cameras). However, these offline models are primarily trained on affine-invariant depth representations, and their generalization to novel scenes remains unclear. In this work we present EM-ViT, a monocular depth estimation model that learns to adapt online relative depth inputs from a foundation model prior to the metric scale with observations collected during robotic operations. Motivated by the stereo camera parameterization, our method decomposes depth prediction via dense disparity refinement to recover the scene's relative structure and an effective baseline scalar prediction to determine the missing metric scale. The learning process leverages sparse LiDAR points and, optionally, the robot's Ego-Motion (EM) to rapidly train a lightweight Vision Transformer (ViT), while an internal gradient matching loss preserves the fine-grained semantic structure of the input disparity in real-time. We demonstrate the efficacy of our method on publicly available sequences, such as KITTI, and show that our online learning pipeline can adapt to novel scenes faster and with higher accuracy than existing MDE foundation models. The code and supplementary materials will be publicly available at https://emvit-mde.github.io.

</details>

## Neural Scene Representations & Rendering

### 2026-11

#### 2026-11-16 - The Mask Is Not the Object: Volumetric Supervision for 3D Gaussian Segmentation

**Authors:** Jeonghwan Cho, Minsu Kim, Junyoung Hong, Seon Joo Kim
**Links:** [abs](https://arxiv.org/abs/2611.21383) - [pdf](https://arxiv.org/pdf/2611.21383)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting enables object-level operations on Gaussian primitives, yet existing segmentation methods are largely trained and evaluated through rendered views. This mismatch can produce accurate rendered masks from incomplete 3D selections since alpha-blended feature supervision concentrates learning on dominant contributors while leaving occluded or low-contribution Gaussians weakly supervised. We propose VODA, a plug-and-play supervision objective that exploits local depth structure to group per-pixel contributors and directly supervises all Gaussians in selected depth clusters, bypassing contribution-weighted gradient delivery. To evaluate volumetric completeness, we introduce Removal-3D, a synthetic object-removal benchmark, and the Removal Depth Error (RDE), a metric comparing predicted and ground-truth depth changes. Across four rendering-based baselines, VODA consistently improves volumetric segmentation on Removal-3D while maintaining or improving performance on LERF and ScanNet. Further analysis shows that VODA recovers lower-contribution Gaussians, while simple gradient reweighting and spatial propagation fail to reproduce comparable gains.

</details>

#### 2026-11-16 - QuantileGS: Quantile-Based Conformal Bounds on RGB Rendering Errors for Novel View Synthesis with 3D Gaussian Splatting

**Authors:** Haiyang Xu, Ziye Zhang, Bin Pan, Xia Xu, Zhenwei Shi
**Links:** [abs](https://arxiv.org/abs/2611.21253) - [pdf](https://arxiv.org/pdf/2611.21253)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, mapping, localization

<details>
<summary>Abstract</summary>

Uncertainty quantification for novel view synthesis with 3D Gaussian Splatting (3DGS) assesses rendering reliability at unseen viewpoints. This reliability depends on the discrepancy between rendered and true colors, which cannot be measured without ground-truth images. We therefore quantify uncertainty in this unknown discrepancy through upper bounds on per-pixel RGB mean absolute error. However, learned bounds may underestimate these errors and overstate rendering reliability, motivating calibration to a prescribed coverage level. In this paper, we propose QuantileGS, a post-hoc framework that combines learned rendering-error quantiles with scale-normalized conformal calibration to produce spatially adaptive error bounds. The framework comprises three phases. Phase 1, Rendering-Error Computation, measures RGB mean absolute error between observed images and predictions from a frozen 3DGS model. Phase 2, Ordered Gaussian Quantile Fields, learns two scalar attributes per Gaussian to predict lower and upper rendering-error quantiles. Phase 3, Scale-Normalized Conformal Calibration, calibrates the upper prediction on held-out images, using the quantile gap to scale the correction. Under the stated assumptions, the resulting bounds provide finite-sample marginal coverage. At a nominal coverage level of 90%, calibration raises mean empirical test coverage from 69.6% to 89.6% on LLFF and from 80.1% to 92.1% on Mip-NeRF 360. On LF, coverage remains conservative at 96.3% before and 96.4% after calibration. Applications to active view selection, Gaussian pruning, and RGB-D simultaneous localization and mapping illustrate how these bounds inform downstream decisions.

</details>

#### 2026-11-16 - A Gaussian Primitive Data Management Framework for Efficient 3DGS Trajectory Rendering

**Authors:** Haolun Ma, Ziyi Liu, Zizhuo Xu, Chuhan Hu, Lei Li
**Links:** [abs](https://arxiv.org/abs/2611.20546) - [pdf](https://arxiv.org/pdf/2611.20546)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, rendering, splatting

<details>
<summary>Abstract</summary>

Trajectory rendering, which renders novel views of a reconstructed 3D scene along a camera path, is a core operation in digital twins and autonomous inspection. Structured 3D Gaussian Splatting (3DGS) renders a single view in real time by decoding sparse anchors into Gaussians on demand, but it renders a trajectory view by view: every view projects all anchors to select them, re-decodes anchors already requested by neighboring views, and runs all steps on the GPU while the CPU idles. We treat this as a spatial data management problem, where anchors are spatial objects, views are range queries, and decoded Gaussians are shared derived data, and propose GDM-GS, which removes redundancy at three levels. Within a view, an anchor index and an occluder index answer each view as a holed-frustum range query, so out-of-view and provably hidden anchors are never decoded. Across views, shared materialization decodes each requested anchor once per group of consecutive views while preserving each view's selection. Across processors, a hybrid pipeline balances selections between the CPU and the GPU before grouped decoding under bounded memory. Experiments on large-scale public scenes show that GDM-GS substantially reduces trajectory rendering latency while preserving image quality.

</details>

#### 2026-11-12 - TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models

**Authors:** Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
**Links:** [abs](https://arxiv.org/abs/2611.17331) - [pdf](https://arxiv.org/pdf/2611.17331)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** view synthesis, rendering, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models
- 作者：Chin-Yang Lin, Ryo Hachiuma, Jaesung Choe, Min-Hung Chen, Yu-Chiang Frank Wang, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu, Cheng Sun
- 出版日期：2026-11-12T18:59:52Z
- 分类：Neural Scene Representations & Rendering（次要分类：摘要未提供）
- 链接：摘要页 https://arxiv.org/abs/2611.17331 ；PDF https://arxiv.org/pdf/2611.17331 ；项目页 https://test-time-baking.github.io

### 一句话总结
论文提出 Test-Time Baking（TTB），把仅解码器视图合成模型中的跨视图注意力映射“烘焙”进轻量 MLP，从而在保持高保真渲染质量的同时显著提升渲染效率。

### 研究问题
论文关注仅解码器的大规模视图合成模型（LVSMs）的效率问题：这类模型借助 KV-cache，在不重建三维几何的情况下从神经网络回归新视图，并达到先进质量；而 Test-Time Training（TTT）层虽然节省计算，却牺牲质量。因此，核心问题是：能否在不牺牲渲染质量的前提下，获得接近 TTT 的渲染效率。

### 核心思路/方法
TTB 的基本做法是学习把跨视图注意力中的全局场景信息烘焙进一个轻量 MLP，以支持快速、高保真的新视图解码。其两个关键设计如下：

1. **重新利用 TTT 的 fast-weight MLP**：不是用其完全替代注意力，而是让其从输入—输出对中显式学习跨视图注意力映射。这样可达到与 TTT 相同的渲染效率，同时显著提高质量。
2. **处理模态错位问题**：针对 context prefilling 与新视图渲染之间的模态错位，将 context tokens 解耦为两类——仅含相机信息的 context rendering tokens 作为 TTB 输入；含图像内容的 context ground-truth tokens 作为 TTB 映射目标。由此使被烘焙的 MLP 不必承担 context 与新视图处理之间的模态泛化挑战。

### 主要贡献
- 提出 Test-Time Baking（TTB）策略，将跨视图注意力中的全局场景信息烘焙进轻量 MLP，实现快速且高保真的新视图解码。
- 通过重新利用 TTT 的 fast-weight MLP 显式学习跨视图注意力映射，在保持 TTT 级渲染效率的同时显著提升质量。
- 通过解耦 context tokens（相机-only 渲染 tokens 作为输入、含图像内容的目标 tokens 作为映射目标），缓解 context prefilling 与新视图渲染之间的模态错位。
- 摘要称方法在多个基准上实现最高 **23x** 渲染加速，质量与当前最先进方法相当。

### 局限性
摘要未提供足够信息。摘要未说明失败案例、适用场景边界、额外训练开销、对特定模型架构的依赖程度，也未给出各基准的详细定量结果与消融实验。

### 阅读优先级
**高**。理由：论文直接针对仅解码器视图合成模型的渲染效率与质量权衡，提出明确的“烘焙”思路与两项关键技术设计，并报告最高 23x 加速且质量与 SOTA 相当；对关注高效神经渲染、视图合成加速及 TTT 替代方案的研究者有较强相关性。但具体实验细节与泛化性需查阅原文确认。

</details>

<details>
<summary>Abstract</summary>

Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking (TTB), a strategy that learns to bake global scene information from cross-view attention into a lightweight MLP, enabling fast and high-fidelity novel-view decoding. The first key is to repurpose the fast-weight MLP of TTT to learn the cross-view attention mapping explicitly from its input-output pairs, rather than replacing attention entirely, achieving the same rendering efficiency as TTT while delivering substantially higher quality. The second key addresses a modality misalignment between context prefilling and novel-view rendering: we disentangle context tokens into camera-only context rendering tokens to serve as TTB input, and context ground-truth tokens with image content to serve as the TTB mapping target, ensuring the baked MLPs are relieved of the modality generalization challenge between context and novel-view processing. Our method achieves up to **23x** rendering speedup with quality on par with the state-of-the-art across several benchmarks. Project page: https://test-time-baking.github.io

</details>

#### 2026-11-12 - Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering

**Authors:** Sipeng Chen, Shibo Li
**Links:** [abs](https://arxiv.org/abs/2611.16650) - [pdf](https://arxiv.org/pdf/2611.16650)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning the Missing Derivative: Neural Multiple-Scattering Operators for Inverse Volume Rendering
- 作者：Sipeng Chen, Shibo Li
- 出版日期：2026-11-12T11:27:20Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.16650) ｜ [PDF](https://arxiv.org/pdf/2611.16650)

### 一句话总结
论文用神经算子预测多重散射场，并在逆渲染中对它求导，以替代冻结源断层成像中被丢弃的导数项和可微路径追踪中昂贵且噪声较大的采样估计。

### 研究问题
从照片重建光学厚介质时，需要建模多重散射及其对消光变化的响应。冻结源断层成像忽略了这一导数；可微路径追踪虽能估计该导数，但依赖昂贵、带噪的采样。因此，问题在于：如何在逆渲染中高效获得多重散射对消光变化的导数。

### 核心思路/方法
- 用神经算子预测多重散射场，并在逆渲染过程中通过该算子进行微分；透射率和单次散射则直接计算。
- 针对优化过程中的关键问题：一个在留出介质上能准确预测散射场的算子，在优化器实际访问的密度状态下仍可能给出较差的导数。
- 解决方式：在由该算子驱动的逆过程所产生的状态上做微调，并使用蒙特卡洛散射场监督。
- 在留出的光学厚云数据上评估重光照效果；与冻结源断层成像在相同时间下比较，与可微路径追踪在给予后者显著更多时间时比较。

### 主要贡献
- 提出以神经算子预测多重散射场并对该算子求导的逆体渲染方法，避免冻结源近似丢弃导数，也避免依赖可微路径追踪的高成本噪声采样。
- 识别并处理“预测场准确但优化访问状态处导数不佳”的问题，通过在逆过程生成状态上微调并使用蒙特卡洛散射场监督。
- 摘要报告：在留出的光学厚云上，同等时间下重光照优于冻结源断层成像；在可微路径追踪获得显著更多时间时优于后者；在逆轨迹上训练还改善了访问状态处的导数对齐并减少优化漂移。

### 局限性
- 摘要未提供足够信息说明方法在大规模场景、复杂材质或非云介质上的泛化能力。
- 摘要未提供足够信息说明微调阶段所需的蒙特卡洛监督成本、训练数据规模及对优化器设置的敏感性。
- 摘要未提供足够信息给出定量指标、误差分析或失败案例。

### 阅读优先级
中。理由：该工作聚焦逆体渲染中多重散射导数建模这一明确问题，方法思路与评估对比在摘要中较清晰；但摘要未给出定量结果和细节，是否值得深入阅读取决于对神经算子、逆体渲染及光学厚介质重光照的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reconstructing optically thick media from photographs requires modeling multiple scattering and its response to changes in extinction. Frozen-source tomography discards this derivative; differentiable path tracing estimates it through expensive, noisy sampling. We instead predict the multiple-scattering field with a neural operator and differentiate through it during inverse rendering, while computing transmittance and single scattering directly. A further challenge arises during optimization: an operator that predicts the field accurately on held-out media can still produce poor derivatives at the density states visited by the optimizer. We address this by fine-tuning on states generated during inversions driven by the operator, using Monte Carlo scattering-field supervision. On held-out optically thick clouds, our method improves relighting over frozen-source tomography at equal time and outperforms differentiable path tracing given substantially more time. Training on inversion trajectories also improves derivative alignment at visited states and reduces optimization drift.

</details>

#### 2026-11-11 - MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs

**Authors:** Yangming Zhang, Siyi Wu, Jian Wang, Bingzhe Li, Wei Niu, Sheng Di, Ming Li, Miao Yin
**Links:** [abs](https://arxiv.org/abs/2611.15153) - [pdf](https://arxiv.org/pdf/2611.15153)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MatrixSplat: Matrix-Parallel and Feature-Scalable 3D Gaussian Splatting Rendering on GPUs
- 作者：Yangming Zhang, Siyi Wu, Jian Wang, Bingzhe Li, Wei Niu, Sheng Di, Ming Li, Miao Yin
- 出版日期：2026-11-11T07:49:26Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2611.15153) | [PDF](https://arxiv.org/pdf/2611.15153)

### 一句话总结
MatrixSplat 将 3DGS 中受顺序依赖限制的 alpha 合成改写为与顺序无关的加权累加，从而把高维特征渲染映射为 GPU Tensor Cores 上的矩阵并行计算，以提升特征可扩展性与渲染效率。

### 研究问题
现有 3DGS 渲染流程与现代 GPU 架构匹配不佳：按深度排序的 alpha 合成带来强烈的逐像素顺序依赖，限制了并行性，并导致以标量 FMA 为主的执行方式，未能充分利用 Tensor Cores 等高吞吐矩阵单元。该问题在多模态、语义增强的 3DGS 中更严重，因为需要从数百万个高斯中累加高维特征，计算与内存开销快速上升。

### 核心思路/方法
论文首先指出 alpha 合成的顺序依赖是高维特征高效渲染的关键障碍，并采用与顺序无关的加权累加形式，将特征渲染转化为面向矩阵的计算。框架包含三项关键设计：
1. 基于 tile 的 splatting 流水线，将特征累加映射为 Tensor Cores 上的 warp 级矩阵乘累加执行；
2. warp 粒度的高斯打包策略，以缓解可见性不规则并提高特征复用；
3. 惰性通道分批特征获取流水线，以降低共享内存压力、维持高 warp 占用率，并将高维特征的内存访问与矩阵执行重叠。

### 主要贡献
- 识别并形式化 alpha 合成顺序依赖对高维特征 3DGS 渲染并行性的阻碍，并采用顺序无关的加权累加实现矩阵化特征渲染。
- 提出 MatrixSplat 框架，包含 tile 级 splatting、warp 粒度高斯打包与惰性通道分批特征获取三项设计。
- 摘要报告在 Mip-NeRF 360、LERF 和 3D-OVS 上，相较 3DGS 最高 3.8 倍加速、相较 TC-GS 最高 2 倍加速，同时保持渲染质量与语义准确率；高维特征下渲染内核时间最高降低 36.7 倍；集成到现有快速渲染器可额外获得 1.69–2.84 倍加速。

### 局限性
摘要未提供足够信息说明局限性。例如未给出硬件平台细节、不同特征维度下的完整扩展性曲线、与更多基线方法的全面比较、数值精度影响、内存占用变化及失败场景等。

### 阅读优先级
高。理由：该工作直接针对 3DGS 渲染与 GPU 矩阵单元利用不匹配这一系统性问题，涉及实时新视角合成与语义/多模态 3DGS 的共同瓶颈；摘要给出了明确的加速结果与可集成的框架设计，对关注 3DGS 渲染效率、GPU 加速和高维特征渲染的研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) has emerged as a mainstream representation for real-time novel view synthesis and 3D reconstruction. However, existing 3DGS rendering pipelines are poorly aligned with modern GPU architectures: depth-sorted alpha compositing introduces strong per-pixel sequential dependencies, limiting parallelism and resulting in scalar FMA-dominated execution that underutilizes high-throughput matrix units such as Tensor Cores. This mismatch becomes more severe for multimodal and semantically enriched 3DGS, where high-dimensional features must be accumulated from millions of Gaussians, leading to rapidly increasing computation and memory costs. We propose MatrixSplat, a matrix-parallel rendering framework for feature-scalable 3DGS on modern GPUs. We first identify the sequential dependency of alpha compositing as a key obstacle to efficient high-dimensional feature rendering, and adopt an order-independent weighted accumulation formulation that transforms feature rendering into matrix-oriented computation. Our framework features three key designs: (i) a tile-based splatting pipeline that maps feature accumulation to warp-level matrix-multiply-accumulate execution on Tensor Cores; (ii) a warp-granularity Gaussian packing strategy that mitigates visibility irregularity and improves feature reuse; and (iii) a lazy channel-batched feature-fetching pipeline that reduces shared-memory pressure, maintains high warp occupancy, and overlaps memory access with matrix execution for high-dimensional features. On Mip-NeRF 360, LERF, and 3D-OVS, MatrixSplat achieves up to 3.8$\times$ speedup over 3DGS and 2$\times$ over TC-GS while maintaining rendering quality and semantic accuracy, and further reduces render-kernel time by up to 36.7$\times$ for high-dimensional features. Integrated into existing fast renderers, it provides an additional 1.69-2.84$\times$ speedup.

</details>

## Embodied / Robotics / AR Applications

### 2026-11

#### 2026-11-16 - Non-Imaging Optical Tactile Sensors for Robotics: Transduction Principles, System Integration, and Robotic Applications

**Authors:** Hao Wu, Yu Feng, Haotian Guo, Huichan Zhao, Changsheng Wu, Jianshu Zhou
**Links:** [abs](https://arxiv.org/abs/2611.20770) - [pdf](https://arxiv.org/pdf/2611.20770)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, localization

<details>
<summary>Abstract</summary>

Non-imaging optical tactile sensors encode contact through changes in optical intensity, wavelength, spectra, or photon counts, offering diverse architectures for robotic touch. Their usefulness depends on whether contact variables can be reliably distinguished from coupled mechanical and environmental effects, and whether the resulting information can be delivered in time to guide action. This review develops a unified framework linking mechanical load transmission, optical encoding, readout, and tactile inference to robotic task requirements. It examines reflective and waveguide-based devices, micro/nanofibers, fiber gratings, interferometric and resonant structures, and mechanoluminescent composites. Three considerations emerge across these approaches. First, high optical sensitivity supports accurate tactile estimation only when target variables remain identifiable under the relevant contact and calibration conditions. Second, spatial coverage and feedback timing must be assessed at the system level, accounting for multiplexing, acquisition, demodulation, and inference. Third, device characterization, offline recognition, and closed-loop robotic performance provide distinct levels of evidence and require different evaluation criteria. Representative studies illustrate how these considerations shape force estimation, contact localization, slip correction and distributed interaction. This review concludes with priorities for calibration transfer, reliable interfaces, scalable readout, and task-based validation, providing a basis for selecting and developing non-imaging optical tactile architectures for robotics.

</details>

#### 2026-11-16 - Vision-Language Grounded Semantic Navigation for Autonomous Mobile Robots

**Authors:** Ravindran Vasoor Saravanan, Chittin Varunav Ravi, Madhumita Singh, Thirulok Sundar Mohan Rasu
**Links:** [abs](https://arxiv.org/abs/2611.20558) - [pdf](https://arxiv.org/pdf/2611.20558)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, mapping, localization, simulation

<details>
<summary>Abstract</summary>

Language-guided navigation enables mobile robots to interpret natural language commands and navigate toward user-specified targets in unstructured environments. However, integrating open-vocabulary visual perception with classical robotics pipelines for mapping and navigation remains a challenging problem. In this work, we present a complete ROS2-based system that combines frontier-based exploration, open-vocabulary object detection using Grounding DINO, depth-based 3D localization, and semantic mapping to enable end-to-end vision-language grounded navigation in simulation. The system accepts natural language commands such as ``go to the yellow box,'' detects candidate objects from RGB images using text prompts, estimates their positions in the world frame, and generates navigation goals executed by the Nav2 stack. In a Gazebo-based indoor environment with a TurtleBot3 robot, the system autonomously explored the room, detected three of the five target objects, and successfully executed both natural language navigation commands tested, without task-specific training. The results indicate that open-vocabulary grounding models can be integrated into classical navigation pipelines, though performance is limited by detection uncertainty, depth-based localization error, and incomplete exploration coverage. These findings highlight both the feasibility and current limitations of deploying vision-language grounded navigation systems using lightweight, CPU-only architectures.

</details>

#### 2026-11-16 - AsymEEF: Bimanual Manipulation with Asymmetric End Effectors

**Authors:** Xiaokang Sun, Ningyue Wang, Kunqi Xu, Guangqi Jiang, Jianglong Ye, Yong Wu, Xueyan Zou
**Links:** [abs](https://arxiv.org/abs/2611.20557) - [pdf](https://arxiv.org/pdf/2611.20557)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Teleoperated demonstrations are costly to collect and rarely reusable across end-effectors with different kinematics and action spaces. This burden grows in bimanual manipulation, where each end-effector pair may require new data. We present AsymEEF, a framework for executable cross-end-effector demonstration generation and unified bimanual policy learning. Given a small source dataset, AsymEEF transfers demonstrations to heterogeneous combinations of two-, three-, and five-fingered end-effectors without additional teleoperation. Kinematic teacher anchors provide geometric supervision, while sparse real-world X-Calib anchors correct discrepancies in grasp execution. A shared encoder maps wrist poses and actuator states to a morphology-agnostic latent space, and a morphology-conditioned decoder reconstructs target commands. Generated trajectories undergo replay filtering for task-level executability. The representation also supports a unified bimanual visuomotor policy trained across multiple pairs. Across four simulated and six real-world tasks, AsymEEF improves replay success over adapted transfer baselines, achieves a mean replay-valid expansion gain of 16.6 times in simulation, and is evaluated through downstream policy training on real robots. Project website: https://asymeef.vercel.app/.

</details>

#### 2026-11-15 - Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding

**Authors:** Mayank Mayank, Bharanidhar Duraisamy, Rohit Mohan, Abhinav Valada
**Links:** [abs](https://arxiv.org/abs/2611.20203) - [pdf](https://arxiv.org/pdf/2611.20203)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>Abstract</summary>

Automotive radar provides long-range sensing and direct Doppler velocity measurements, but its sparse and non-uniformly sampled point clouds pose significant challenges for panoptic segmentation. Dynamic objects often yield only a few detections amid a dominant static background, providing limiting the geometric cues for separating object instances. We propose \emph{Radar Panoptic Transformer (RPT)}, an end-to-end point-based network that incorporates radar-adaptive feature extraction with semantic-guided mask prediction. Its backbone aggregates pose-aligned temporal context through grouped vector attention and learns per-point neighborhood radii conditioned on range, azimuth, and radar cross section (RCS). Point-wise semantic predictions initialize queries at likely foreground detections and guide masked cross-attention through query-point class agreement, producing instance masks without geometric clustering. An auxiliary RCS-consistency loss matches instance-level statistics between predicted and annotated instances. RPT achieves state-of-the-art performance on RadarScenes with $71.6\%$ mIoU and $82.2\%$ PQ. We further evaluate RPT on MAN TruckScenes, where it outperforms the evaluated baselines in a long-range, full-surround radar setting with sensing ranges up to $230\,\mathrm{m}$. RPT achieves real-time end-to-end inference at $31$\,Hz on RadarScenes, exceeding the sensor frame rate.

</details>

#### 2026-11-15 - Latent World Modeling for Point-Cloud Video Pretraining

**Authors:** Zhuoyue Zhang, Jian Liu, Jihua Zhu, Ajmal Saeed Mian
**Links:** [abs](https://arxiv.org/abs/2611.20090) - [pdf](https://arxiv.org/pdf/2611.20090)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>Abstract</summary>

Masked modeling is the dominant self-supervised paradigm for point-cloud videos. However, it leaks the information it is meant to predict, whether it reconstructs masked points as in MAE-style methods or predicts their latent features. Because point-cloud tokens are anchored at points sampled from each frame, querying a target at its own position reveals where its geometry has moved, in reconstruction and latent prediction alike. For latent predictors, random spatio-temporal masks introduce a further shortcut, as visible frames on both sides of each target allow interpolation rather than forecasting. The pretext task thus reduces to completion. Once the target positions are withheld, a masked latent predictor performs only slightly better than copying the last frame. To remove this leakage, we propose PointWM, a latent world model that turns completion into forecasting by predicting the features and geometry of future frames from strictly earlier context. Each target is queried only with its last-seen position and timestamp, while a latent action learned without annotations is meant to capture the part of the future that the past leaves undetermined. On HOI4D action segmentation with a P4Transformer backbone, PointWM improves F1@50 over training from scratch by 24.9 offline and 29.1 under strictly causal inference. These results show the promise of latent world models as a leakage-free pretraining paradigm for point-cloud videos.Our code is publicly available at https://github.com/InitalZ/PointWM.

</details>

#### 2026-11-15 - EasyNav: A Modular Architecture for Real-Time Navigation Across Heterogeneous Robot Environments

**Authors:** Francisco Martín Rico, Francisco Miguel Moreno, Juan Sebastián Cely Gutiérrez, Esther Aguado, Miguel Ángel De Miguel Paraíso, José Miguel Guerrero
**Links:** [abs](https://arxiv.org/abs/2611.19894) - [pdf](https://arxiv.org/pdf/2611.19894)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping, localization

<details>
<summary>Abstract</summary>

Most robot navigation stacks implicitly bind mapping, localization, planning, and control to specific representations and data flows, yielding architectures hard to extend, compare experimentally, or reason about end-to-end timing. This is critical in heterogeneous scenarios, where multiple spatial representations, sensing modalities, and coordinate frames coexist and evolve at different rates. This paper presents a navigation architecture centered on an explicit, shared navigation state that serves as the sole interaction interface between modular components. Constraining mapping, localization, planning, and control to operate over this shared state enables interchangeable, representation-agnostic pipelines under explicit compatibility and timing contracts. We realize this architecture as EasyNav, an open source ROS 2 framework, and validate it through real-robot experiments, including indoor navigation with laser sensing and large-scale indoor-outdoor navigation with GPS and 3D LiDAR across multi-level routes. Compared with Nav2 under matched conditions, EasyNav reduces reaction latency from 377 to 33 ms indoors and from 71 to 8 ms outdoors, while also using less CPU and memory.

</details>

#### 2026-11-15 - Beyond Vehicle-Centric Data: Scaling Autonomous Driving through Roadside-to-Vehicle Generation

**Authors:** Yichen Zhang, Zihan Wang, Hao Chen, Runyi Huang, Ruixue Zong, Jing Wang, Yunong Mao, Lei He, Keqiang Li
**Links:** [abs](https://arxiv.org/abs/2611.19830) - [pdf](https://arxiv.org/pdf/2611.19830)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, autonomous driving

<details>
<summary>Abstract</summary>

Training autonomous driving models requires large and diverse datasets, collected primarily by vehicles. Scaling them entails investment in fleet operation, data processing and annotation. Road infrastructure records traffic and multi-vehicle interactions, yet the viewpoint gap between roadside and onboard sensors limits its direct use for training. Here we introduce AnyR2V, a framework that transforms multimodal roadside observations into seven-camera surround-view videos for different vehicle perspectives. It aggregates sequential observations into a shared scene representation of geometry and road-user motion, then renders appearance, depth and layout conditions along target-vehicle trajectories. Supervised by spatiotemporally aligned roadside-vehicle pairs, AnyR2V generates surround-view videos guided by scene structure and road-user motion. Existing roadside 3D bounding boxes are transformed into target-vehicle coordinates and paired with generated images, allowing one traffic recording and its annotations to yield training data from multiple vehicle perspectives. We construct R2V360, a dataset of 89 real traffic sequences at an urban intersection, with aligned multimodal roadside data and onboard surround-view videos. AnyR2V outperforms six scene reconstruction methods in image fidelity and in depth and semantic agreement between generated and real onboard images. We further evaluate generated videos along other vehicles' trajectories by adding them to real training data. Adding generated frames equal to 50% of the original real training frame count improves mean average precision (mAP) by 3.3-3.4 AP-points across three 3D object detectors on the real onboard test set, relative to real-data-only baselines. These results demonstrate that roadside traffic records can provide training data from multiple vehicle perspectives, offering a new data source for autonomous driving.

</details>

#### 2026-11-15 - JEPA4R: Embodied JEPA World Models with 4D Point Planning

**Authors:** Jiarui Dong, Zhiheng Liang, Yanjun Li, Zeyu Zhang, Heejeong Nam, Haoyu Chen, Hao Tang
**Links:** [abs](https://arxiv.org/abs/2611.19771) - [pdf](https://arxiv.org/pdf/2611.19771)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, digital twin, simulation, world model

<details>
<summary>Abstract</summary>

Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space. Two challenges remain: 2D images leave the metric geometry that manipulation acts on implicit and entangled with appearance, and what these models imagine stays hidden, as they are mostly judged in simulation by short-horizon latent planning. We present JEPA4R, a JEPA world model that observes single-depth-camera point clouds, predicts and plans in their latent space, and acts through a policy head on its frozen latents; we call this 4D point planning. A decoder on the frozen world model shows what it imagines as 4D point clouds, with a mean point error within 1.1 cm over 200 steps. Under the policy-learning protocols of OGBench and CortexBench, JEPA4R leads pixel JEPA models on OGBench Cube-Single, Cube-Double, Cube-Triple and Scene, and ranks first on MetaWorld and Adroit Relocate with 98.4% and 88.0%, above the runner-up, R3M, at 96.0% and 65.3%. Trained only in a digital twin, JEPA4R and its policy heads run zero-shot on the real arm with both a gripper and a dexterous hand.

</details>

#### 2026-11-15 - M-CROSS: A Multisensor Simulation Dataset for SLAM across Water--Land Transitions

**Authors:** Yan Dong, Tianyi Wu, Junyu Yang, Shaoqiang Qiu, Zefeng Yan, Tao Zhang, Bin Han
**Links:** [abs](https://arxiv.org/abs/2611.19765) - [pdf](https://arxiv.org/pdf/2611.19765)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, localization, simulation

<details>
<summary>Abstract</summary>

Water--land cross-domain robots require continuous localization across land, transition and underwater phases, where sensor characteristics and availability change abruptly. Existing datasets and conventional metrics are not designed to capture transition-induced degradation and failures. We present \textbf{M-CROSS}, to the best of our knowledge, the first multisensor simulation dataset and benchmark for SLAM across continuous water--land transitions. It provides synchronized LiDAR, sonar, stereo camera, IMU, DVL, and depth measurements; 6DoF pose ground truth; sensor-wise medium-state annotations; and medium-dependent sensor degradation models. We establish a transition-aware protocol comprising the Trajectory Completion Rate (TCR), Piecewise Absolute Pose Error (PW-APE), Transition End Error (TEE), and Transition Survival Period (TSP), which measure trajectory completion, single-domain accuracy, transition-induced error, and localization survival under prolonged partial immersion, respectively. Experiments with 6 representative SLAM systems show that existing methods fail to maintain both localization accuracy and trajectory continuity across the full set of water--land transitions, exhibiting transition-induced drift, trajectory discontinuities, and tracking failures. M-CROSS is publicly available https://anonymous.4open.science/r/MCross-Dataset

</details>

#### 2026-11-12 - Spatial Foundry: A Multimodal Dataset for Spatial Intelligence

**Authors:** Ethan Lin, Yang Song
**Links:** [abs](https://arxiv.org/abs/2611.17318) - [pdf](https://arxiv.org/pdf/2611.17318)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** metric depth, geometric reconstruction, spatial intelligence, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatial Foundry: A Multimodal Dataset for Spatial Intelligence
- 作者：Ethan Lin, Yang Song
- 出版日期：2026-11-12T18:58:36Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页面 https://arxiv.org/abs/2611.17318 ；PDF https://arxiv.org/pdf/2611.17318

### 一句话总结
该论文提出了 Spatial Foundry，一个包含 5,280 个带家具住宅 3D 场景配置、具备可编辑资产并对齐视觉、几何与时间信息的多模态数据集，旨在为空间智能和世界模型研究提供统一参考系下的数据基础。

### 研究问题
摘要指出，空间智能需要把视觉观察与环境几何、物体及持久状态联系起来；但仅靠图像会隐含这些关系，而彼此割裂的标注又难以在统一参考下研究外观、相机运动与场景变化。论文因此关注如何构建一个多模态、共享坐标且支持受控变化的数据集，以支撑空间感知与世界模型相关研究。

### 核心思路/方法
论文构建了 Spatial Foundry 数据集，包含 5,280 个带家具住宅 3D 场景配置，并提供可编辑资产以及对齐的视觉、几何和时间数据。其模态包括平面图、透视与全景 RGB、度量深度、点云、网格、实例级 3D 边界框，以及与视频配对的相机轨迹。共享场景坐标将跨视角、跨时间的观察联系起来；可编辑源场景支持生成额外相机路径和受控物体变化。摘要还描述了数据表示与构建流程。

### 主要贡献
- 提出 Spatial Foundry 多模态数据集：5,280 个带家具住宅 3D 场景配置，包含可编辑资产和对齐的视觉、几何、时间数据。
- 提供多种模态：平面图、透视/全景 RGB、度量深度、点云、网格、实例级 3D 边界框、相机轨迹与视频配对。
- 通过共享场景坐标连接跨视角和跨时间观察，并利用可编辑源场景支持额外相机路径与受控物体变化。
- 摘要列出潜在应用方向：平面图条件 3D 生成、几何重建、实例级感知、相机条件视频生成、共享世界建模和场景编辑。
- 摘要提到公开项目页面提供视频和交互式彩色点云预览。

### 局限性
- 摘要未提供足够信息说明数据集规模之外的多样性、真实感与仿真差距。
- 摘要未提供足够信息说明标注精度、质量控制或人工校验流程。
- 摘要未提供足够信息说明基线实验、评价指标或与其他数据集的定量比较。
- 摘要未提供足够信息说明数据许可、使用限制或伦理与隐私相关考虑。
- 摘要未提供足够信息说明可编辑场景变化的具体类型、范围与可控程度。

### 阅读优先级
中。理由：该工作与空间智能、具身/机器人/AR 应用中的多模态数据构建和世界模型研究相关，数据集模态较丰富且强调共享坐标与受控变化；但摘要未给出实验验证、定量结果或数据质量细节，是否值得深入阅读取决于读者对数据集构建、3D 场景理解或相机条件生成等方向的具体需求。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bounding boxes, and camera trajectories paired with video. Shared scene coordinates link observations across views and time; editable source scenes enable additional camera paths and controlled object changes. We describe the data representation and construction workflow, and discuss applications in floor-plan-conditioned 3D generation, geometric reconstruction, instance-level perception, camera-conditioned video generation, shared world modeling, and scene editing. Controlled camera and scene variations support spatial perception and world-model research. The public project page provides videos and an interactive colored point-cloud preview.

</details>

#### 2026-11-12 - ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving

**Authors:** Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2611.16579) - [pdf](https://arxiv.org/pdf/2611.16579)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving
- 作者：Ziying Song, Shengkai Zhang, Caiyan Jia, Lei Yang, Lin Liu, Yuchen Liu, Ziyang Liu, Zirui Li, Gang Wang, Peiliang Wu, Li Wang, Yadan Luo, Chen Lv
- 出版日期：2026-11-12T10:10:39Z
- 分类：主分类 Embodied / Robotics / AR Applications；无二级分类
- 链接：摘要页 https://arxiv.org/abs/2611.16579 ；PDF https://arxiv.org/pdf/2611.16579

### 一句话总结
论文提出 ActWorld-JEPA，将动作条件化的联合嵌入预测架构（JEPA）用于候选轨迹规划，并通过关系残差重排序（R³）把潜空间未来预测与候选规划评分连接起来，实现端到端自动驾驶的候选选择。

### 研究问题
摘要指出，JEPA 能在潜空间中进行未来预测而无需像素重建，但“潜预测一致性”本身并不能确立候选规划之间的相对驾驶质量。因此，核心问题是：如何利用 JEPA 的潜空间预测表示来评估和选择候选驾驶规划，使预测结果真正服务于驾驶决策。

### 核心思路/方法
论文给出一个面向候选规划的联合嵌入公式，包含两个主要部分：

1. **Plan-Conditioned JEPA（PC-JEPA）**：使用全局与逐步的轨迹意图引导循环潜预测，再通过门控交叉注意力（gated cross-attention）将预测未来与当前场景结合。
2. **Relational Residual Reranking（R³）**：在规划监督下建模“规划表示”与“未来表示”之间的一致性和差异，对基础规划分数产生有界、门控的残差修正。

该公式在推理时仅使用已观测上下文和候选轨迹，将潜预测与候选选择相连接。

### 主要贡献
- 提出 ActWorld-JEPA，将动作条件化的 JEPA 世界模型与潜空间规划结合，用于基于候选的端到端自动驾驶。
- 提出 PC-JEPA，以全局和逐步轨迹意图引导循环潜预测，并用门控交叉注意力融合预测未来与当前场景。
- 提出 R³，在规划监督下利用规划与未来表示的一致/差异信息，对基础规划分数进行有界门控残差修正。
- 报告了基准结果：NAVSIM v1 navtest 上 94.1 PDMS；NAVSIM v2 navtest 与 navhard 上分别为 91.6 和 42.7 EPDMS；nuScenes 上 1–6 秒平均 L2 误差 1.20 m、预测碰撞率 0.76%。
- 摘要称该工作为从 JEPA 预测表示走向“由预期后果指导驾驶决策”提供了有效路径。

### 局限性
- 摘要未提供足够信息说明计算开销、实时性、模型规模或训练成本。
- 摘要未提供足够信息说明各模块的消融实验细节与各自增益。
- 摘要未提供足够信息说明失败案例、安全边界或分布外场景表现。
- 摘要提到“benchmark-specific implementations”以及最终选择器使用聚合 NAVTEST 反馈进行校准，但未提供足够信息说明其泛化性与公平性影响。
- 摘要未提供足够信息说明 nuScenes 评估的具体设置与对比基线细节。

### 阅读优先级
**中**。理由：论文主题处于 JEPA 世界模型与端到端自动驾驶规划的交叉点，方法结构（PC-JEPA + R³）和报告的基准指标具有明确参考价值；但摘要未展开实验细节、消融与局限性，需阅读全文后才能判断其方法增益与泛化性。若关注潜空间预测用于规划候选重排序，优先级可视为偏高；若仅需广泛了解自动驾驶规划进展，则为中等。

</details>

<details>
<summary>Abstract</summary>

Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction. However, latent predictive consistency alone does not establish the relative driving quality of candidate plans. We present ActWorld-JEPA, a joint-embedding formulation for candidate-based driving. Where Plan-Conditioned JEPA (PC-JEPA) uses global and step-wise trajectory intentions to guide recurrent latent prediction, then combines the predicted future with the current scene through gated cross-attention; Relational Residual Reranking ($R^3$) models agreement and discrepancy between plan and future representations under planning supervision, yielding bounded, gated residual corrections to the base planning scores. This formulation connects latent prediction to candidate selection using only observed context and proposed trajectories at inference. Benchmark-specific implementations report 94.1 PDMS on NAVSIM v1 navtest, with the final selector calibrated using aggregate NAVTEST feedback, and 91.6 and 42.7 EPDMS on NAVSIM v2 navtest and navhard, respectively. The nuScenes evaluation reports a mean $L_2$ error of 1.20 m and a predicted collision rate of 0.76% over 1--6 s. This work provides an effective path from JEPA's predictive representations to driving decisions informed by anticipated consequences.

</details>

#### 2026-11-12 - VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation

**Authors:** Shengjia Zhu, Wenqiang Xu, Lin Shao
**Links:** [abs](https://arxiv.org/abs/2611.16423) - [pdf](https://arxiv.org/pdf/2611.16423)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** pose estimation, manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation
- 作者：Shengjia Zhu, Wenqiang Xu, Lin Shao
- 出版日期：2026-11-12T07:33:05Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要 https://arxiv.org/abs/2611.16423 ；PDF https://arxiv.org/pdf/2611.16423

### 一句话总结
VOKE 是一个运动学感知框架，在现有物体位姿估计器输出基础上，补充估计物体的线速度、角速度、线加速度和角加速度，并将该运动状态用于位姿精化与下游强化学习控制。

### 研究问题
摘要指出，基于视觉的灵巧手内操作不仅需要知道物体“在哪里”，还需要知道物体“如何运动”；但多数机器人操作系统依赖的现成视觉感知模型只输出静态物体掩码、几何或 6D 位姿，导致下游控制器需要从带噪声的视觉观测中隐式推断物体动力学。VOKE 要解决的问题是：如何从视觉中显式恢复较完整的物体运动学状态，并让其可用于感知到控制的链路。

### 核心思路/方法
摘要给出的方法由两个核心感知模块和一个下游应用研究组成：

1. **Pluggable Kinematics Module（PKM，可插拔运动学模块）**：接在标准位姿估计器的输出之后，从时序视觉特征中预测物体的线速度、角速度、线加速度和角加速度。
2. **Kinematics-guided Pose Refinement Module（KPRM，运动学引导的位姿精化模块）**：将上述运动向量转换为二阶、运动先验的参考位姿，并据此精化逐帧位姿估计。
3. **下游应用 Kinematics-Augmented Reinforcement Learning（KARL，运动学增强强化学习）**：将运动学增强的策略与使用位姿历史的基线策略进行比较；策略先在仿真中训练，随后将运动学增强策略不做策略微调地迁移到实体机器人。

整体上，VOKE 将“位姿估计”扩展为包含位姿、线/角速度、线/角加速度的完整物体运动学状态估计。

### 主要贡献
基于摘要可归纳的贡献包括：

- 提出 VOKE 运动学感知感知框架，用于增强现有物体及手-物位姿估计器，输出更完整的物体运动学状态。
- 设计 PKM，可从时序视觉特征预测线/角速度与线/角加速度。
- 设计 KPRM，利用运动向量构造二阶运动先验参考位姿并精化逐帧位姿。
- 在 DexYCB 和 OakInk 上评估：摘要称其在三种不同 backbone 上一致改善物体位姿估计，并且相较“位姿差分”显著降低速度与加速度估计误差。
- 通过 KARL 展示下游应用：运动学增强策略在仿真训练后可零策略微调迁移至实体机器人，形成从感知到控制的完整通路。

### 局限性
- 摘要未提供足够信息说明 VOKE 在真实机器人上的感知鲁棒性、泛化范围或失败情形。
- 摘要未提供足够信息说明实验的定量指标细节、数据集划分、训练数据规模与计算开销。
- 摘要未提供足够信息说明 PKM 对位姿估计器误差的敏感程度，以及 KPRM 在快速运动或遮挡条件下的表现。
- 摘要未提供足够信息说明 KARL 相比位姿历史基线的具体性能差距与统计显著性。
- 摘要未提供足够信息说明方法对不同物体类别、手型或传感器配置的适用边界。

### 阅读优先级
**中**。理由：该论文聚焦灵巧手内操作中“显式运动学感知”这一感知到控制的关键缺口，方法模块清晰，且有跨数据集评估与实体机器人迁移的下游验证；但仅凭摘要无法判断定量提升幅度、真实场景鲁棒性和与现有方法的完整对比，适合在需要了解手内操作感知-控制链路时进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Vision-based dexterous in-hand manipulation requires knowing not only where an object is, but also how it moves. However, most robotic manipulation systems rely on off-the-shelf visual perception models whose outputs are limited to static object masks, geometry, or 6D poses, leaving downstream controllers to infer object dynamics implicitly from noisy visual observations. We present VOKE, a kinematics-aware perception framework that augments existing object and hand-object pose estimators to recover a complete object kinematic state comprising pose, linear and angular velocity, and linear and angular acceleration. VOKE contains two core perception modules and a downstream application study. First, a Pluggable Kinematics Module (PKM) attaches to the output of a standard pose estimator and predicts the object's linear and angular velocity and acceleration from temporal visual features. Second, a Kinematics-guided Pose Refinement Module (KPRM) converts this motion vector into a second-order, motion-prior reference pose and refines the per-frame pose estimates. We evaluate VOKE on DexYCB and OakInk, where it consistently improves object pose estimation across three different backbones and substantially reduces velocity and acceleration estimation error compared with pose differencing. As a downstream application, we use Kinematics-Augmented Reinforcement Learning (KARL) to compare a kinematics-augmented policy with a pose-history baseline. After training the policies in simulation, we transfer the kinematics-augmented policy to the physical robot without policy fine-tuning, demonstrating the complete perception-to-control pathway in the target domain.

</details>

#### 2026-11-12 - Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras

**Authors:** Raul Steinmetz, Jair Augusto Bottega, Ayanori Yorozu, Akihisa Ohya
**Links:** [abs](https://arxiv.org/abs/2611.16282) - [pdf](https://arxiv.org/pdf/2611.16282)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras
- 作者：Raul Steinmetz, Jair Augusto Bottega, Ayanori Yorozu, Akihisa Ohya
- 出版日期：2026-11-12T04:32:37Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2611.16282) / [PDF](https://arxiv.org/pdf/2611.16282)

### 一句话总结
论文研究利用固定外置相机进行室内机器人导航，指出 PPO 端到端学习在该设置下失败，并提出 VINE：先通过监督学习估计视角不变障碍图，再供 PPO 策略或 A* 规划器使用。

### 研究问题
论文关注室内环境下、基于固定外置相机（exocentric cameras，即基础设施安装、位于机器人外部的相机）的机器人导航与避障问题。作者指出，标准 PPO 在机载相机场景中可行，但在该外置相机设置下无法端到端学习导航；其归因是外置观测与以机器人为中心的动作和目标表述之间存在视角不匹配，仅靠奖励信号难以解决。

### 核心思路/方法
论文提出 VINE（Viewpoint-Invariant Navigation from Exocentric Cameras）。VINE 使用一个通过监督学习训练的障碍图估计网络，输入包括外置图像、相机位姿、机器人位姿和房间尺寸，输出视角不变的障碍图。该障碍图既可供 PPO 策略使用，也可供 A* 等规划器使用。摘要还称，该方法无需针对特定视角调参，仅需近似相机位姿估计，并对相机内参变化具有鲁棒性，且可扩展到部分覆盖的双相机设置。

### 主要贡献
- 明确指出标准 PPO 在外置固定相机端到端导航设置中失败，并将其归因于外置观测与以机器人为中心的动作和目标表述之间的视角不匹配。
- 提出 VINE，通过监督学习估计视角不变障碍图，并将该图接入 PPO 策略或 A* 规划器。
- 摘要声称其地图估计优于透视映射方法，可处理大范围位置和朝向的相机而无需视角特定调参。
- 摘要声称仅需近似相机位姿：x、y、z 各轴噪声标准差 30cm，平均旋转误差约 20°。
- 摘要声称对相机内参变化具有鲁棒性，并可扩展到部分覆盖的双相机设置。
- 摘要声称在评估时相机位置随机化的仿真环境中，VINE 的导航成功率超过使用机载相机的 PPO。

### 局限性
摘要未提供足够信息说明实验规模、仿真环境细节、真实机器人实验、失败案例、计算开销、与更多基线方法的系统比较，以及“优于透视映射方法”和“超过机载相机 PPO”的具体量化结果。摘要未提供足够信息说明方法在真实室内环境中的泛化能力与安全性边界。

### 阅读优先级
中。理由：该论文针对外置相机机器人导航中的视角不匹配问题提出明确的中间表征方案，并给出监督学习障碍图与 PPO/A* 的结合路径；若关注基础设施相机辅助机器人导航、视角不变表征或端到端策略失败分析，具有参考价值。但当前仅有摘要与元数据，缺少实验细节与量化结果，需阅读全文后再判断其证据强度。

</details>

<details>
<summary>Abstract</summary>

We study robot navigation in indoor environments from fixed exocentric cameras (infrastructure-mounted, external to the robot). We show that standard Proximal Policy Optimization (PPO), which succeeds with onboard cameras, fails to learn this navigation end-to-end in our setup. This failure results from the perspective mismatch between exocentric observations and egocentric action and goal formulations, which is too complex to resolve from the reward signal alone. To address this, we propose Viewpoint-Invariant Navigation from Exocentric Cameras (VINE). VINE uses an obstacle map estimation network, trained with supervised learning, that takes exocentric images, camera pose, robot pose, and room dimensions as input and produces a viewpoint-invariant obstacle map. This map can be used either by a PPO policy or by a planner such as A*. VINE's map estimation performs better than perspective mapping approaches, handles cameras placed across a wide range of positions and orientations without view-specific tuning, requires only approximate camera pose estimates (noise with a standard deviation of 30cm per axis in x, y, and z and about 20° of rotation error on average), is robust to intrinsic variation, and extends to two-camera setups with partial coverage. Despite operating from cameras randomized in position during evaluation, VINE surpasses the navigation success rate of PPO with an onboard camera in simulated environments.

</details>

#### 2026-11-11 - MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes

**Authors:** Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli
**Links:** [abs](https://arxiv.org/abs/2611.15937) - [pdf](https://arxiv.org/pdf/2611.15937)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene reconstruction, manipulation, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes
- 作者：Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli
- 出版日期：2026-11-11T19:32:35Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.15937) / [PDF](https://arxiv.org/pdf/2611.15937)

### 一句话总结
MOSAIC 提出一种模块化、空间与障碍物感知的框架，可接入预训练 VLA 策略，通过角色特定语义掩码、几何 token 和障碍物感知注意力监督增强杂乱场景下的操作性能。

### 研究问题
现有 Vision-Language-Action（VLA）模型主要依赖 2D 视觉观察和语言指令，场景几何与障碍物关系需要隐式推断。在杂乱环境中，小空间误差可能导致意外接触或碰撞。论文关注如何在不改变预训练 VLA 主干架构的前提下，显式引入语义、几何和障碍物感知线索以改善动作生成。

### 核心思路/方法
- 在 VLA 主干上增加辅助语义 grounding 任务，预测目标物体、目标区域和周围障碍物的角色特定掩码。
- 将目标与目标区域掩码结合由 3D 场景重建估计的深度，构造角色特定几何 token，并直接注入 action expert。
- 提出障碍物感知注意力监督，在任务执行中强调机器人本体附近的障碍物，并将得到的注意力特征注入后续 action-expert 层以进一步引导动作生成。
- 上述组件共同提供显式语义、几何和障碍物感知线索，同时保留底层预训练 VLA 架构。

### 主要贡献
- 提出可集成到预训练 VLA 策略的模块化空间与障碍物感知框架 MOSAIC。
- 引入角色特定语义掩码预测，并结合深度构造几何 token 注入 action expert。
- 提出障碍物感知注意力监督，将相关注意力特征注入后续 action-expert 层。
- 在 RoboPRO 基准上评估，包括视觉扰动测试，并在真实世界操作任务上验证；摘要报告杂乱场景成功率提升 5.1%，视觉扰动下提升 9.7%，最具挑战环境提升最高达 25.0%。

### 局限性
- 摘要未提供足够信息说明方法在不同 VLA 主干、不同机器人平台上的泛化能力。
- 摘要未提供足够信息说明 3D 场景重建与深度估计失败时的鲁棒性。
- 摘要未提供足够信息说明真实世界实验的任务数量、评价协议与统计显著性。
- 摘要未提供足够信息说明计算开销、推理延迟和模块化组件的消融细节。
- 摘要未提供足够信息说明代码与数据集的实际可用状态（仅说明接收后发布）。

### 阅读优先级
高。理由：该论文直接针对 VLA 在杂乱场景中缺乏显式几何与障碍物感知的问题，提出可插拔框架，并在摘要中给出明确的成功率提升数据，包括视觉扰动和最具挑战环境下的增益；对具身智能与机器人操作方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relationships to be inferred implicitly. This limitation is particularly problematic in cluttered environments, where small spatial errors can lead to unintended contacts or collisions. We propose MOSAIC, a modular spatial- and obstacle-aware framework that can be integrated with pretrained VLA policies to improve object-level scene understanding and action generation. Our method augments the VLA backbone with an auxiliary semantic grounding task that predicts role-specific masks for the target object, destination region, and surrounding obstacles. We further combine the target and destination masks with depth estimated from 3D scene reconstruction to construct role-specific geometric tokens that are injected directly into the action expert. In addition, we propose obstacle-aware attention supervision that emphasizes obstacles near the robot body during task execution. The resulting attention features are subsequently injected into later action-expert layers to further guide action generation. Together, these components provide explicit semantic, geometric, and obstacle-aware cues while preserving the underlying pretrained VLA architecture. We evaluate our framework on pretrained VLA model using the RoboPRO benchmark, including visual perturbation tests, and further validate it on real-world manipulation tasks. MOSAIC improves the success rate by 5.1% in cluttered scenes, and by 9.7% under visual perturbations, with gains of up to 25.0% in the most challenging environment. We will release our code and dataset upon acceptance at the following Github page: https://mmahdavian.github.io/MOSAIC/

</details>

#### 2026-11-11 - RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback

**Authors:** Kevin Avdiu, Seongjin Bien, Yannik Blei, Philine Meister, Johannes Hechtl, Philipp Schmitt, Kai Wurm, Georg von Wichert, Wolfram Burgard
**Links:** [abs](https://arxiv.org/abs/2611.15802) - [pdf](https://arxiv.org/pdf/2611.15802)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, augmented reality, virtual reality, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback
- 作者：Kevin Avdiu, Seongjin Bien, Yannik Blei, Philine Meister, Johannes Hechtl, Philipp Schmitt, Kai Wurm, Georg von Wichert, Wolfram Burgard
- 出版日期：2026-11-11T18:17:42Z
- 分类：主分类 Embodied / Robotics / AR Applications；次分类未提供
- 链接：摘要页 https://arxiv.org/abs/2611.15802 ；PDF https://arxiv.org/pdf/2611.15802

### 一句话总结
RUMI 是一种与 Robotiq 2F-85 夹爪几何和非线性力学相匹配的手持通用操作接口，结合可换指尖传感器、AR 运动可行性反馈与触觉反馈，用于采集力感知的机器人学习数据并支持遥操作。

### 研究问题
论文关注的问题是：许多操作任务需要精细控制的接触力，但大规模、力感知的数据集仍然稀缺；现有手持接口多针对简单线性夹爪设计，无法匹配广泛使用的机器人夹爪的非线性力学特性。因此，如何构建一种与目标夹爪匹配、既能自然输入又能在接触后测量力，并支持力感知遥操作与数据采集的接口，是本文的核心问题。

### 核心思路/方法
RUMI 的设计与 Robotiq 2F-85 夹爪匹配，保留目标夹爪几何结构，并配备可交换的指尖传感器：接触前支持自然输入，接触后实现力测量。方法将跟踪系统集成到虚拟现实头显中，提供关于目标机器人平台上运动学可行性的实时增强现实反馈。论文还引入触觉反馈机制，以支持仿真和真实机器人的力感知遥操作。作者通过用户研究比较有无 AR 时的关节限位违规情况，并使用由夹爪匹配硬件支持的两种指尖模态所采集的示范数据训练模仿策略，同时评估触觉接口在仿真中采集力感知遥操作数据集的能力。

### 主要贡献
- 提出 RUMI：一种与 Robotiq 2F-85 匹配的手持通用操作接口，保留目标夹爪几何并支持可交换指尖传感器。
- 将跟踪系统集成到 VR 头显中，提供目标机器人平台上运动学可行性的实时 AR 反馈。
- 引入触觉反馈机制，支持仿真和真实机器人的力感知遥操作。
- 用户研究显示：带实时机器人可视化和姿态初始化时，含关节限位违规的回合数为 3/50；无 AR 时为 16/50。
- 使用两种指尖模态采集的示范训练模仿策略，并评估触觉接口在仿真中采集力感知遥操作数据集的能力。

### 局限性
摘要未提供足够信息说明样本规模、任务多样性、真实机器人部署范围、触觉反馈精度、数据集规模、策略性能定量结果以及硬件成本或可用性等限制。仅可确认用户研究涉及 50 个回合的比较，以及仿真中的触觉数据采集评估；更广泛的局限需参考全文。

### 阅读优先级
中。理由：该工作与力感知数据采集、手持操作接口、AR 反馈和触觉遥操作直接相关，且提供了明确的用户研究对比结果；但摘要未给出模仿策略性能、真实机器人实验规模和数据集细节，是否优先精读取决于读者对 Robotiq 夹爪匹配接口或力感知示教数据采集的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Many manipulation tasks require carefully controlled contact forces for successful execution, yet large-scale, force-aware datasets remain scarce. Handheld interfaces can help by transmitting interaction forces directly through the operator's arm, but most existing designs are tailored to simple linear grippers and do not match the nonlinear mechanics of widely used robotic grippers. We present RUMI, a handheld universal manipulation interface matched to the Robotiq 2F-85 with exchangeable fingertip sensors that preserves the target gripper geometry while enabling natural input before contact and force measurement after contact. By integrating the tracking system into a virtual reality headset, our method provides real-time augmented reality feedback about the kinematic feasibility of motion on the target robot platform. We further introduce a haptic feedback mechanism that supports force-aware teleoperation for simulated and real robots. A user study shows fewer episodes containing joint-limit violations with live robot visualization and pose initialization (3/50) than without augmented reality (16/50). We additionally train imitation policies from demonstrations, collected using two different fingertip modalities enabled by the gripper-matched hardware, and assess the haptic interface's capability for collecting force-aware teleoperation datasets in simulation.

</details>

#### 2026-11-11 - Single-View RGB-D Force--Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials

**Authors:** Dezhi Sun, Marijn van Hilten, Kenan Niu
**Links:** [abs](https://arxiv.org/abs/2611.15650) - [pdf](https://arxiv.org/pdf/2611.15650)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Single-View RGB-D Force--Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials
- 作者：Dezhi Sun, Marijn van Hilten, Kenan Niu
- 出版日期：2026-11-11T16:00:58Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2611.15650

### 一句话总结
该论文研究使用标准机器人、单目手眼 RGB-D 相机和内在力估计，建立弹塑性材料在法向压入过程中的力—变形（体积）关系，并评估简单回归模型与累积变形定位的可行性。

### 研究问题
弹塑性材料在机器人操作中会产生持续变形，物理交互与空间分布的形状变化相互耦合，使操作复杂化。论文关注：在仅使用单视角 RGB-D 几何与内在力估计的条件下，如何测量并建模力与变形之间的关系，以及能否在多次交互中定位累积变形。

### 核心思路/方法
- 平台：7 自由度 Franka Emika FR3 执行法向压入（normal indentation），Intel RealSense L515 作为单目手眼 RGB-D 相机采集接触前与接触后的表面。
- 几何处理：通过点云处理定位变形区域并估计位移体积（displaced volume）。
- 力—体积表征：在 9 个力水平上进行 27 次测量。
- 模型：使用紧凑的多层感知机（MLP），在 4 个力水平上的 52 个力—体积对训练，报告留出集 RMSE 为 1.857 N、\(R^2=0.440\)。
- 对比：在 16 N 时二次模型误差更低，在 19 N 与 23.5 N 时 MLP 误差更低。
- 累积实验：进行每次交互 4 N 的八步实验，从第二次压入开始展示累积变形定位。

### 主要贡献
- 提出并验证一种基于标准机器人、单目手眼 RGB-D 相机与内在力估计的力—变形测量流程。
- 给出力—体积关系的实验表征数据（9 个力水平、27 次测量）。
- 评估紧凑 MLP 对力—体积关系的拟合表现，并与二次模型在部分力水平上进行比较。
- 通过八步、每次 4 N 的交互实验，展示从第二次压入起的累积变形定位能力。
- 作者总结这些结果为进一步的变形感知操作提供了实际测量基础。

### 局限性
- 摘要未提供足够信息说明实验材料的具体种类、样本数量与材料参数。
- 摘要未提供足够信息说明力估计的精度验证方法与误差来源分解。
- 摘要未提供足够信息说明 MLP 与二次模型比较的完整实验设计、统计显著性与泛化到其他力水平或材料的结果。
- 摘要未提供足够信息说明累积变形定位的定量精度指标。
- 摘要未提供足够信息说明单视角遮挡、相机位姿变化或不同机器人平台下的适用性。
- MLP 的留出集 \(R^2=0.440\) 表明拟合解释力有限，但摘要未提供足够信息分析其原因。

### 阅读优先级
中。理由：该论文聚焦弹塑性材料操作中的力—变形测量与单视角几何估计，问题定义清晰且与机器人操作相关；但摘要显示模型拟合指标有限（\(R^2=0.440\)），且关键实验细节（材料、统计验证、定位精度）未在摘要中给出。是否优先阅读取决于读者对力估计、单目 RGB-D 变形感知或弹塑性操作基准的兴趣；若关注高精度力—变形建模，则需进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Persistent deformation complicates elasto-plastic manipulation by coupling physical interaction with spatially distributed shape changes. We investigate the force--deformation relationship using a standard robot, a single eye-in-hand RGB-D camera, and intrinsic force estimates. A 7-DoF Franka Emika FR3 performs normal indentations while an Intel RealSense L515 captures pre- and post-contact surfaces. Point-cloud processing localizes deformation and estimates displaced volume. Force--volume characterization includes 27 measurements over nine force levels. A compact multilayer perceptron (MLP), trained on 52 force--volume pairs at four levels, achieves a held-out RMSE of 1.857 N and $R^2=0.440$. A separate comparison shows lower error for a quadratic model at 16 N and for the MLP at 19 and 23.5 N. An eight-step experiment at 4 N per interaction demonstrates cumulative deformation localization from the second indentation onward. These results establish a practical measurement basis for deformation-aware manipulation using intrinsic force estimates and single-view geometry.

</details>

#### 2026-11-10 - BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model

**Authors:** Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang, Seung Wook Kim
**Links:** [abs](https://arxiv.org/abs/2611.14815) - [pdf](https://arxiv.org/pdf/2611.14815)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model
- 作者：Junyoung Seo, Jaewoo Seo, Seungryong Kim, Laura Leal-Taixé, Xiuming Zhang, Seung Wook Kim
- 出版日期：2026-11-10T23:04:58Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2611.14815) / [PDF](https://arxiv.org/pdf/2611.14815)

### 一句话总结
BirdDreams 是一种自回归驾驶世界模型，通过联合生成透视视频与示意性 BEV 视频，将场景布局纳入预测未来，并借助 BEV 作为自车控制的几何接口，从单张相机图像实现更忠实于输入自车轨迹的驾驶场景模拟。

### 研究问题
驾驶世界模型需要模拟场景在不同自车动作下的展开过程，这既要求周围车辆运动合理，也要求精确控制自车轨迹。仅从透视视频学习车辆运动较为困难，因为运动与外观纠缠且车辆可能被遮挡。已有工作通过以指定车辆运动的布局作为条件来获得对周围车辆的控制，但需要未来轨迹作为输入。论文试图解决如何在不需要未来车辆轨迹、HD 地图或车辆状态输入的情况下，同时获得合理的周围车辆运动与精确的自车轨迹控制。

### 核心思路/方法
BirdDreams 将场景布局作为预测未来的一部分，联合生成两路视频：透视视频与示意性 BEV 视频。BEV 在训练时由场景标注渲染，以固定米制尺度将道路和车辆表示为简单形状，提供位置与运动的自上而下视角并减少车辆间遮挡；透视视频则保留 BEV 省略的场景细节，如交通信号和物体外观。两个视频扩散 Transformer 分别处理一路视频，并通过联合注意力在生成过程中相互提供信息。预测的 BEV 还作为自车控制的几何接口：沿输入自车轨迹平移和旋转其最新帧，并将得到的帧作为软条件，表示若仅自车运动时场景将如何变化。推理时，BirdDreams 从单张相机图像生成两路视频，不需要 HD 地图或车辆状态输入。

### 主要贡献
- 提出 BirdDreams，一种自回归驾驶世界模型，联合生成透视视频与示意性 BEV 视频，使场景布局成为预测未来的一部分。
- 通过两个视频扩散 Transformer 之间的联合注意力，让透视流与 BEV 流在生成过程中相互 inform。
- 利用预测 BEV 作为自车控制的几何接口，通过对最新 BEV 帧沿输入自车轨迹进行平移和旋转，形成软条件。
- 在 PhysicalAI-AV 和 nuScenes 上，BirdDreams 比先前驾驶世界模型更忠实地跟随输入自车轨迹，并在无自车动作条件下生成更合理的自车运动。
- 人工评估显示，BirdDreams 在生成真实的周围车辆行为方面优于仅透视视频的基线。

### 局限性
摘要未提供足够信息说明方法的具体失效场景、计算开销、对标注质量的依赖程度、BEV 表示在复杂遮挡或极端场景下的表现，以及定量实验的完整设置与指标细节。摘要也未提供足够信息说明模型在训练数据分布之外的泛化能力。

### 阅读优先级
中。理由：论文聚焦驾驶世界模型中透视视频与 BEV 联合生成、自车轨迹控制及无需未来轨迹输入的问题，与具身/机器人及自动驾驶仿真相关；摘要给出了明确的问题动机、方法框架和初步评估结论。但摘要未提供足够信息展示完整实验细节、定量指标和局限分析，是否高优先级需结合读者对驾驶世界模型或联合视频生成的具体兴趣判断。

</details>

<details>
<summary>Abstract</summary>

Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and vehicles can be occluded. Prior work therefore conditions video generation on layouts that specify vehicle motion, providing control over surrounding vehicles but requiring their future trajectories as inputs. We introduce BirdDreams, an autoregressive driving world model that jointly generates perspective video and a schematic bird's-eye-view (BEV) video, making scene layout part of the predicted future. The BEV, rendered from scene annotations for training, depicts roads and vehicles as simple shapes at a fixed metric scale, providing a top-down view of their positions and motion with reduced occlusion between vehicles. Perspective video, by contrast, retains scene details that the BEV omits, such as traffic signals and object appearance. Joint attention between two video diffusion transformers, one per stream, lets each stream inform the other during generation. The predicted BEV also provides a geometric interface for ego control: we translate and rotate its latest frame along an input ego trajectory and use the resulting frames as a soft condition that shows how the scene would appear to move if only the ego vehicle moved. At inference, BirdDreams generates both videos from a single camera image without requiring an HD map or vehicle-state inputs. On PhysicalAI-AV and nuScenes, BirdDreams follows input ego trajectories more faithfully than prior driving world models and generates more plausible ego motion without ego-action conditioning. Human evaluation shows that BirdDreams outperforms a perspective-only baseline in generating realistic surrounding-vehicle behavior.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
