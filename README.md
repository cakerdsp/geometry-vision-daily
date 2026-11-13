# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：66
- 分类分布：
  - Embodied / Robotics / AR Applications: 22
  - 3D Reconstruction & Multi-view Geometry: 22
  - Neural Scene Representations & Rendering: 13
  - Dynamic / 4D Reconstruction: 5
  - Geometry Foundation Models: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“基础模型 + 几何先验”正在从离线重建走向生产级系统。** Kosmo-GFM 把几何基础模型、位姿优化引擎与重建监督组织成一套面向生产的场景重建系统，并直接服务下游 3D/4D Gaussian Splatting；Multi-View 3D Reconstruction Using V-JEPA Features 则系统检验视频预训练特征用于纯 RGB 多视图重建时的组件归因问题（相机回归方式、联合相对目标、位姿与深度的竞争）。共同信号是：几何基础模型的研究重心正从“单点精度”转向“系统集成与可部署性”，并且越来越强调对组件贡献的隔离验证，而不是笼统归功于预训练表示。

2. **测试时/前馈式效率优化成为视图合成与重建的独立主线。** TTB 用“烘焙”把跨视图注意力映射进轻量 MLP，在 decoder-only 视图合成模型上追求接近 TTT 的效率而不牺牲质量；ThermalSplat 用前馈式、无位姿、无 RGB 引导的高斯泼溅替代逐场景优化；EG360 用蒸馏 + 球面跨层融合，在 6.593M 参数下兼顾零样本泛化与嵌入式实时性；MatrixSplat 则从渲染算子层把 alpha 合成改写为矩阵并行以适配 Tensor Cores。这些工作共同表明：效率不再只是工程收尾，而是与泛化性一起被当作建模目标（蒸馏、重参数化、算子重写、烘焙），且约束条件越来越贴近真实部署（嵌入式、稀疏视角、高维特征）。

3. **4D/动态重建开始处理“表示假设失效”的困难场景。** ReCan-GS 用形变场导出的 Jacobian 敏感性分数区分一致内容与干扰观测（遮挡物、阴影、烟雾），无需掩码与预训练分割器；Topo-4DGS 针对第一人称视频中的分裂、合并、开合等拓扑变化，指出固定表示形变这一 4DGS 根本假设在此失效，并配套提出 TopoEgo 基准。两者的共同点是：不再假设“场景是固定表示的可形变版本”，而是显式建模“什么该被抑制/激活/分离”，评估也从单一指标转向带专门基准的场景化评测。

4. **具身/机器人方向明显从“2D 感知接策略”转向“显式几何、运动学与力感知的中间表示”。** MOSAIC 给预训练 VLA 注入角色特定掩码、由深度构造的几何 token 和障碍物感知注意力监督；VOKE 在位姿估计器后接可插拔运动学模块，显式输出速度与加速度；VINE 指出外置相机下 PPO 端到端失败，改为先估计视角不变障碍图再交给策略或规划器；RUMI 与单视角 RGB-D 力—变形估计则补齐力感知数据与力—变形建模。趋势是：**不再指望大策略从奖励或 2D 图像中隐式恢复物理量，而是把这些量做成可监督、可注入、可测量的模块**。

5. **数据与基准建设同步跟进，且强调“共享参考系”和“受控变化”。** Spatial Foundry 用共享场景坐标连接跨视角、跨时间的多模态观测，并用可编辑源场景支持受控物体变化与额外相机路径；TopoEgo 专攻拓扑变化；RGB-D SLAM on the Edge 提供边缘硬件上的分阶段、函数级剖析数据；MiniPose 用缩微实体复制品缓解大物体真实数据采集负担并保留真实深度传感器误差特性。数据侧的共同取向是：**为“难以采集、难以对齐、难以复现”的条件（拓扑变化、传感器误差、边缘资源约束、跨模态对齐）专门造数据**，而不是继续堆规模。

#### 技术路线观察

- **几何基础模型路线**：以 Kosmo-GFM 为代表，走“预测相机/深度/对应/动态点 + 几何优化 + 重建派生监督”的闭环系统路线，强调生产可用与下游 3D/4DGS 衔接；Multi-View V-JEPA 则走“视频预训练特征 + 相机估计 + 极线传输 + 残差点图”的组件化路线，价值在于揭示位姿与深度之间的竞争性影响。两条路线的分歧点是：前者押注统一大模型加优化引擎，后者押注对预训练表示的可解释拆解。

- **3D/4D 重建路线**：EG360 与 ThermalSplat 都面向“稀疏/受限输入 + 可泛化”，前者用全景-透视蒸馏与球面融合压参数，后者用 soft census loss 与边界结构损失绕开热图像弱纹理与视角依赖发射率；ReCan-GS 与 Topo-4DGS 则面向“输入含不一致观测或拓扑变化”，前者用形变敏感性做分离与剪枝，后者用部件级独立刚性变换与高斯动态激活/停用。可以看到重建研究正从“更多视角、更好先验”转向“更少视角、更脏输入、更复杂事件”。

- **神经场景表示与渲染路线**：TTB 在 decoder-only 视图合成模型上做测试时烘焙，把全局场景信息压进轻量 MLP，本质是“注意力映射的显式蒸馏”；MatrixSplat 则在渲染管线层重构 alpha 合成的顺序依赖，把高维特征累加映射到矩阵单元。两者分别从模型侧和算子侧回应同一个压力：**高维特征与实时渲染的成本矛盾**。

- **机器人/AR 应用路线**：MOSAIC、VOKE、VINE 分别代表三种“中间表示注入”方式——语义/几何 token 注入 VLA、运动学状态注入位姿精化与 RL、视角不变障碍图注入策略或规划器；RUMI 与力—变形估计则从数据采集与物理建模两端补足力感知。与纯视觉重建论文相比，这一路线更关注接口设计（可插拔、模块化、不改主干）与失败模式归因（如 PPO 失败源于视角不匹配）。

- **交叉信号**：Spatial Foundry、TopoEgo、MiniPose、边缘 SLAM 基准共同说明，**评测与数据基础设施正在成为独立贡献**，且越来越强调“受控变化”和“硬件/传感器真实性”，这为前述方法提供了可比对的实验土壤。

#### 值得优先阅读的论文

1. **Kosmo-GFM**：唯一明确以“生产级”为目标的几何基础模型系统论文，涉及 GFM、位姿优化、重建监督与 3D/4DGS 下游的完整链路，且报告了深度、相对位姿、动态点与场景流多类指标。对判断几何基础模型能否落地最有信息量。
2. **TTB**：直接触及 decoder-only 视图合成模型的效率—质量权衡，且方法思路（把跨视图注意力显式烘焙进 MLP，而非完全替代）具有较强可迁移性，值得看其模态错位处理与消融细节。
3. **Topo-4DGS（含 TopoEgo）**：同时给出方法与基准，明确指出现有 4DGS 的固定表示形变假设在拓扑变化下失效，是动态重建方向少见的“问题形式化 + 评测建设”组合。
4. **ReCan-GS**：用形变场 Jacobian 作为重建歧义的代理分数，无需掩码/分割器/介质监督即可处理遮挡物、光度伪影与烟雾，思路简洁且对“脏输入 4D 重建”有普适参考价值。
5. **MOSAIC 或 VOKE（二选一，按兴趣）**：若关注 VLA 与几何结合选 MOSAIC（模块化注入、不改主干）；若关注感知到控制的物理量链路选 VOKE（可插拔运动学模块 + 位姿精化 + RL 应用），两者都体现了“显式中间表示”这一当前具身方向的核心取向。

#### 可能的研究机会

- **把“烘焙/蒸馏”思路推广到 4D 与多模态高斯表示**：TTB 在视图合成模型上做注意力烘焙，

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-13T15:29:12-05:00
**Total number of papers:** 66
**Number of papers added in the latest update:** 23
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

#### 2026-11-10 - RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals

**Authors:** Mario Alberto Tapia de la Cruz, Charalambos Poullis
**Links:** [abs](https://arxiv.org/abs/2611.14763) - [pdf](https://arxiv.org/pdf/2611.14763)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RECALL: Real-Time Recalibration of Multi-Camera Rigs via Learned OEM-Anchored Residuals
- 作者：Mario Alberto Tapia de la Cruz, Charalambos Poullis
- 出版日期：2026-11-10T21:39:57Z
- 分类：Geometry Foundation Models
- 链接：摘要页 https://arxiv.org/abs/2611.14763 ；PDF https://arxiv.org/pdf/2611.14763

### 一句话总结
RECALL 以厂商标定为锚点、结合对已知物体的短暂观测，用前馈神经网络单次预测并迭代精化多相机装置的当前内参和外参，实现实时重标定。

### 研究问题
多相机装置出厂时已预标定，但在重新摆放后标定会失效，并因磨损、热循环和振动持续漂移。经典捆绑调整需要新的多视角采集和全局优化，计算成本随装置规模增长，难以实时使用。论文要解决的是：如何在可移动多相机装置上实现实时、高精度的在线重标定。

### 核心思路/方法
RECALL 是一种前馈方法，单次完成可移动多相机装置的重标定。它以名义 OEM 标定作为锚点，利用对已知物体的短暂观测，预测每个相机的当前内参和外参。标定被表示为装置共享的全局旋转与每相机小漂移的组合。方法不一次性回归标定，而是使用学习到的、与装置耦合的循环算子迭代精化估计：每一步通过可微投影进行重投影，并在相机间施加注意力；共享旋转规范通过网络内学习的高斯-牛顿步求解，而非直接回归。由于真值可合成，训练数据全部在线生成，无需采集数据集。

### 主要贡献
- 提出 RECALL，一种单次前馈的可移动多相机装置实时重标定方法。
- 以 OEM 标定为锚点，将标定分解为共享全局旋转与每相机小漂移，并用学习到的循环算子、可微重投影和跨相机注意力迭代精化。
- 在网络内用学习的高斯-牛顿步求解共享旋转规范，而非直接回归。
- 训练完全依赖在线合成数据，无需捕获数据集。
- 在合成 10 相机基准上，精度优于逐相机和装置耦合联合捆绑调整（旋转 $0.26^\circ$ vs $0.47^\circ$，焦距 $5.4$ vs $8.9$ px），速度约快 $10^5\times$，每装置约 $0.12$ ms。
- 在真实数据（TotalCapture、CMU Panoptic）上，绝对和相对旋转匹配或优于离线装置耦合捆绑调整，速度快四到五个数量级；在 Panoptic 环绕装置上相对位姿匹配最强纯图像基础模型（VGGT、VGGT-$Ω$、$π^3$），同时保持度量性，焦距精度约高 $15\times$。

### 局限性
摘要未提供足够信息。摘要未说明方法对未知物体或非已知观测条件的依赖程度、合成到真实的泛化边界、极端漂移下的表现，也未给出失败案例或计算资源需求等细节。

### 阅读优先级
高。理由：该工作直接针对多相机装置在线重标定的实时性与精度矛盾，声称在合成和真实数据上均优于或匹配捆绑调整及强基础模型，且速度提升显著；若关注多相机几何标定、实时视觉系统或几何基础模型应用，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Multi-camera rigs ship pre-calibrated from the manufacturer, but their calibration goes stale each time the rig is repositioned, and drifts continuously through wear, thermal cycling, and vibration. Recovering it on-the-fly is hard: classical bundle adjustment needs a fresh multi-view capture and a global optimization whose cost grows with the rig, ruling out real-time use. In this paper we present RECALL, a feed-forward method that recalibrates a movable multi-camera rig in a single pass. From the nominal OEM calibration as an anchor and a brief observation of a known object, it predicts each camera's current intrinsics and extrinsics, written as a shared global rotation of the rig composed with a small per-camera drift. Instead of regressing the calibration in one shot, RECALL refines its estimate with a learned, rig-coupled recurrent operator that reprojects through a differentiable projection and applies attention across the cameras at each step, and solves for the shared rotational gauge in-network with a learned Gauss-Newton step rather than regressing it. Because the ground truth is synthesizable, we train entirely on data generated on-the-fly and need no captured dataset. On a synthetic 10-camera benchmark, RECALL is more accurate than per-camera and rig-coupled joint bundle adjustment ($0.26^\circ$ vs $0.47^\circ$ rotation, $5.4$ vs $8.9$ px focal) and runs about $10^5\times$ faster at about $0.12$ ms per rig. On real data (TotalCapture, CMU Panoptic) it matches or beats offline rig-coupled bundle adjustment on absolute and relative rotation while running four-to-five orders of magnitude faster, and on the Panoptic surround rig it also matches the strongest image-only foundation models (VGGT, VGGT-$Ω$, $π^3$) on relative pose while staying metric and about $15\times$ more accurate in focal length. Code: https://github.com/theICTlab/RECALL-multicam

</details>

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
