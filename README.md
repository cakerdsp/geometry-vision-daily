# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：60
- 分类分布：
  - 3D Reconstruction & Multi-view Geometry: 21
  - Embodied / Robotics / AR Applications: 18
  - Neural Scene Representations & Rendering: 13
  - Geometry Foundation Models: 4
  - Dynamic / 4D Reconstruction: 4
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **几何基础模型从“离线大模型”走向“可部署系统组件”**  
   Kosmo-GFM 把几何基础模型（GFM）、位姿优化引擎和重建派生监督整合为面向生产的场景重建系统；EG360 则用蒸馏与轻量主干把全景深度估计压到 6.593M 参数、面向 Jetson Orin NX 实时运行；MatrixSplat 从渲染侧解决 3DGS 与现代 GPU 的匹配问题。三者共同反映：几何/重建研究的评价重心正在从“指标领先”转向“精度—效率—可部署性”的联合权衡。

2. **“烘焙/蒸馏/前馈化”成为替代逐场景优化的主流效率路径**  
   TTB 把跨视图注意力烘焙进轻量 MLP，在保留 decoder-only 视图合成质量的同时逼近 TTT 效率；ThermalSplat 用前馈式高斯泼溅替代逐场景优化与 RGB 引导；EG360 用全景-透视蒸馏实现轻量泛化。这类工作共享同一模式：把昂贵的、逐场景的计算转移到训练时或蒸馏目标中，推理时只保留轻量通路。

3. **4D/动态重建开始显式处理“非刚性与拓扑变化”，而非仅形变固定表示**  
   ReCan-GS 用形变场导出的 Jacobian 敏感性分数区分一致场景与干扰观测；Topo-4DGS 针对第一人称视频中的分裂、合并、打开、关闭等拓扑事件，动态激活/停用高斯；Track4D 则把稠密 3D 跟踪表示为视频信号以复用 VDM 先验。趋势是从“对固定表示做形变”转向“让表示本身支持结构变化与观测不一致性”。

4. **机器人感知从静态位姿/掩码向显式运动学、力与几何关系扩展**  
   VOKE 在 6D 位姿之上补齐线/角速度与加速度；MOSAIC 把目标、目标区域与障碍物掩码和深度结合注入 VLA 动作专家；单视角 RGB-D 力—变形估计则尝试建立力与变形体积的显式关系。共同点是：不再让下游控制器从 2D 观测中隐式推断物理量，而是把运动学、几何、力显式建模为感知输出。

5. **数据与基准建设成为方法突破的前置条件**  
   Spatial Foundry 提供 5,280 个带家具住宅 3D 配置、共享坐标的多模态对齐数据；TopoEgo 是首个针对第一人称拓扑变化的基准；MiniPose 用缩微实体解决大型工业物体真实数据采集难题；RGB-D SLAM on the Edge 则补齐 ARM 边缘板上标准 SLAM 系统的公开基准数据。多个方向同时出现“先建数据/基准、再提方法”的组合，说明领域正从单点方法创新转向可复现的实验基础设施竞争。

#### 技术路线观察

- **几何基础模型方向**：Kosmo-GFM 走“系统集成”路线，将 GFM 预测（相机参数、深度、跨视图对应、动态 3D 点）与 PoseEngine 几何优化、KosmoWorld 重建监督闭环结合，强调生产可用；Multi-View 3D Reconstruction Using V-JEPA Features 则走“隔离归因”路线，系统比较全局/空间相机回归与联合相对目标，明确提示重建增益未必来自视频预训练特征本身。两者形成对照：一个做端到端系统，一个做组件级消融，说明该方向尚未形成统一的技术共识。

- **3D/4D 重建方向**：技术侧重点明显分化。ReCan-GS 与 Topo-4DGS 都基于 4DGS，但前者关注“干扰观测的分离”，后者关注“表面支撑的拓扑变化”，问题建模不同；Track4D 不直接重建几何，而是把 3D 跟踪重编码为视频表示以复用扩散模型先验；ThermalSplat 则面向纯热红外、无位姿、稀疏视角的极端条件，用 soft census loss 与边界结构损失替代 RGB 引导。整体看，4D 重建正从“统一形变场”走向“按问题类型定制表示与监督”。

- **神经场景表示与渲染方向**：TTB 与 MatrixSplat 代表两条不同的效率路线——前者在模型层面把注意力映射烘焙进 MLP，后者在系统层面把 alpha 合成改写为顺序无关的加权累加以利用 Tensor Cores。两者都指向同一个瓶颈：高质量视图合成的成本结构正在从“训练成本”转向“推理与特征累加成本”，尤其是多模态/语义增强 3DGS 的高维特征聚合。

- **机器人/AR 应用方向**：VOKE、MOSAIC、RUMI、VINE 与力—变形估计呈现出“感知输出与控制器需求对齐”的共同逻辑。VINE 明确指出外置相机与机载相机之间的视角不匹配使 PPO 端到端失败，转而用监督学习估计视角不变障碍图；MOSAIC 在不改 VLA 主干的前提下注入几何与障碍物线索；RUMI 则从数据采集端解决力感知数据稀缺。与纯视觉重建论文相比，这一方向的评价标准更偏向任务成功率、接触安全与数据采集效率，而非重建指标。

#### 值得优先阅读的论文

1. **TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models**  
   理由：它提出了一种可复用的效率范式——把注意力映射烘焙进轻量 MLP，而非用 TTT 层整体替代注意力。该思路可能迁移到其他依赖 KV-cache 的视图合成或视频生成模型，且论文明确处理了 context prefilling 与 novel-view rendering 之间的模态错位，属于方法层面的结构性贡献。

2. **Kosmo-GFM: A Production-Ready Geometry Foundation Model**  
   理由：它是本批论文中少有的“系统级”工作，把 GFM、位姿优化与重建派生监督组织成闭环，并在 SpatialBench 上报告深度、相对位姿与动态点/场景流误差。对关心几何基础模型如何落地、以及 GFM 与 3D/4DGS 下游如何衔接的读者，优先级最高。

3. **ReCan-GS: Distractor-free 4D Gaussian Splatting**  
   理由：用形变场导出的 Jacobian 敏感性分数作为重建歧义代理，无需掩码、预训练分割器或介质专属监督，这一“自监督信号来自模型自身”的设计较通用，可能扩展到其他动态重建中的干扰物抑制问题。

4. **Topology-Aware 4D Gaussian Splatting for Egocentric Videos（Topo-4DGS + TopoEgo）**  
   理由：同时提出方法与基准，且拓扑变化（分裂、合并、打开、关闭）是现有 4DGS 固定表示形变范式的明确盲区。对具身 AI 与第一人称视频重建交叉方向的研究者，基准本身可能比方法更具长期价值。

5. **Spatial Foundry: A Multimodal Dataset for Spatial Intelligence**  
   理由：共享场景坐标、可编辑源场景、多模态对齐（平面图、透视/全景 RGB、度量深度、点云、网格、实例 3D 框、相机轨迹与视频），使其具备支撑空间智能与世界模型研究的潜力。若研究依赖受控相机路径与物体变化，该数据集值得优先评估。

#### 可能的研究机会

- **把 TTB 的烘焙思路与 4D/动态重建结合**：TTB 目前面向 decoder-only 视图合成，若能把跨视图注意力烘焙扩展到动态场景的时序注意力，可能缓解 4DGS 与视频扩散模型在推理效率上的压力。需验证的是动态场景下“全局场景信息”是否仍可被轻量 MLP 充分压缩。

- **用 ReCan-GS 的敏感性分数与 Topo-4DGS 的拓扑激活机制互补**：前者识别“不一致观测”，后者处理“表面出现/消失/分离”。两者若结合，可能形成统一的“动态场景结构变化 + 干扰观测抑制”框架，尤其适用于第一人称视频中既有拓扑事件又有瞬态遮挡的场景。

-

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-11-13T15:29:12-05:00
**Total number of papers:** 36
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

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
