# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：73
- 分类分布：
  - Neural Scene Representations & Rendering: 25
  - Embodied / Robotics / AR Applications: 23
  - 3D Reconstruction & Multi-view Geometry: 18
  - Dynamic / 4D Reconstruction: 5
  - Geometry Foundation Models: 2
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **“几何基础模型 + 分辨率/规模解耦”成为多视图重建的新主线。**
   ReDT 直接指出高分辨率输入下帧内注意力与编码器注意力开销未被解决，提出用固定大小基元 token 空间做对应计算；SpaRV 则从机器人数据出发，用稀疏辐射体素 + LiDAR 监督解决几何约束不足与显存随场景增长的问题。两者共同反映：重建模型正在从“堆叠视图/分辨率”转向“把几何推理与输入规模解耦”。

2. **前馈式 4D/动态重建与生成式视频模型加速合流。**
   Drive2Gauss 把联合生成的 RGB、度量深度、动态流前馈转换为 4D 高斯，避免逐序列优化；Holo4D 把前馈 4D 重建得到的 3D 轨迹投影到目标视角，作为视频扩散模型的几何控制。两者都体现“重建提供几何骨架、生成补全未观测区域”的分工模式，动态 4D 重建正从优化型管线转向可复用前馈表示。

3. **稀疏视角/受限观测下的表示正则化被系统化重述。**
   稀疏视角 3DGS 论文把高斯基元当神经元、以少样本学习视角统一数据监督增强与训练正则化；MCSplat 用规范外观空间解耦几何与相机外观，并用 Fisher 信息不确定性加权几何自监督。这说明 3DGS 社区的关注点正从“表示能力”转向“在弱监督、跨相机不一致条件下如何防止几何退化”。

4. **机器人操作正在从单一策略转向“触觉/形态条件化 + 仿真到真实适配 + 未知物体可用性”。**
   LEAP Hand 论文比较拟人化与对称式手指布局在完整触觉、二值接触、仅本体感觉下的表现，把手部几何与触觉反馈作为可分析变量；农业 VLA 论文用 MuJoCo 演示适配 Octo 与 π₀.₅ 并在真实 Franka 上微调；OV-PEAR 面向未知工业物体做观测验证的位姿-尺度估计与重建。共同趋势是：不再假设物体已知或工作单元稳定，而是强调对未见物体的适应与多模态反馈的作用量化。

5. **具身智能评测开始从“问答/静态任务”转向“主动探索与地图式推理”。**
   SpatialScout 要求 VLM 智能体在有限交互预算下主动控制相机、完成对象级 3D 度量建图；ForagerSim 提供可独立调节感知、尺度、拓扑、动态的任务平台，并指出地图式推理可能是瓶颈。这反映评测设计正在向“主动获取证据 + 构建一致空间表示”迁移，而非仅考查单帧识别或空间问答。

#### 技术路线观察

- **几何基础模型方向**：ReDT 的路线是“内部表示与输入分辨率解耦”，以固定大小基元空间承载对应计算；PnP-Transformer 则把位姿求解本身神经化、可微化，试图替代 PnP-RANSAC 的迭代流程。两者分别从“特征侧”和“求解侧”推进几何基础能力，但 PnP-Transformer 摘要中 EPnP-RANSAC 替换后反超的结果提示：神经求解器的收益可能高度依赖对应场质量与训练/集成方式。

- **3D/4D 重建方向**：Drive2Gauss 与 Holo4D 都采用“多模态生成/重建 → 显式 4D 表示 → 下游渲染或条件控制”的前馈路线；MCSplat 与 ReDT 则更关注多视图一致性、分辨率和几何监督可靠性。整体上，4D 重建正从“每场景优化”转向“前馈 + 可组合表示”，但跨相机光度一致性、动态流可靠性和大场景扩展仍是共同难点。

- **神经场景表示与渲染方向**：RxGS 把风格化从 RGB 外观转移到 BRDF 分解后的漫反射反照率场，使风格化结果可重光照；SpaRV 用稀疏体素替代稠密辐射场以控制显存；稀疏视角 3DGS 论文用少样本学习框架统一监督增强与正则化。三条路线分别对应“物理可分解”“内存可扩展”“监督可正则化”，显示 3DGS/辐射场研究正在向可编辑、可扩展、抗退化三个维度分化。

- **机器人/AR 应用方向**：LEAP Hand 论文把触觉观测条件作为消融变量，量化完整触觉相对本体感觉的提升（拟人化 94.8%、对称 66.9%）；农业 VLA 论文强调仿真演示降低真实采集成本；OV-PEAR 强调观测验证抑制生成幻觉；CAOS-SLAM 强调无需预定义类别的动态物体过滤。共同技术侧重点是“在真实部署约束（成本、未知物体、动态环境、传感器噪声）下保持可用性”，而非追求单一基准分数。

- **交叉趋势**：单目 MAV 飞行论文用跨模态蒸馏把深度专家的规划特征迁移到 RGB 规划器，并借助 3DGS 模拟器做数据生成；这与 Drive2Gauss、Holo4D 形成呼应：3DGS/4D 表示不仅用于渲染，也越来越多地充当机器人学习的仿真数据与几何监督来源。

#### 值得优先阅读的论文

1. **ReDT: Resolution-Decoupled Visual Geometry Transformer**（2610.25517）
   理由：直接处理视觉几何 Transformer 在高分辨率下的计算扩展问题，提出“基元 token 空间”这一可复用的架构思路。对多视图重建、几何基础模型和 HD 输入落地都有直接参考价值，且属于方法层面的结构性改进。

2. **Drive2Gauss**（2610.26585）与 **Holo4D**（2610.25276）可对照阅读
   理由：两篇分别代表“生成多模态 → 前馈 4D 高斯”和“前馈 4D 重建 → 条件化视频扩散”两种互补路线。对照阅读能看清 4D 重建与生成模型的分工边界、几何控制信号的形式，以及哪些区域交给生成先验。

3. **SpatialScout**（2610.26659）
   理由：把 VLM 智能体的评测从空间问答推进到主动探索与对象级度量建图，任务定义（视角选择、跨视角关联、几何估计、地图修正、有限交互预算）清晰，适合作为具身空间智能评测设计的参考基准。

4. **Tactile In-Hand Object Rotation**（2610.26759）
   理由：以手部形态与触觉观测条件为控制变量，给出仿真与硬件对照的量化结果（完整触觉相对本体感觉提升 94.8%/66.9%），对触觉操作、低成本硬件和强化学习框架的可复现实验设计有较高参考价值。

5. **OV-PEAR**（2610.25840）
   理由：面向未知工业物体的位姿-尺度估计与重建，强调观测验证抑制生成幻觉并产出可复用物体模型，贴近工业操作落地中的“无 CAD、无物体专用训练数据”场景，方法三阶段流程较完整。

#### 可能的研究机会

- **分辨率解耦思想向 4D/动态重建迁移**：ReDT 的基元 token 空间主要用于多视图静态重建；若把时间维度纳入固定大小基元表示，可能缓解 Drive2Gauss/Holo4D 在长序列或高分辨率驾驶视频上的计算压力。可探索“时空基元 token + 动态流关联”的前馈 4D 架构。

- **触觉条件化与手部形态的联合优化**：LEAP Hand 论文把形态作为固定变量比较；一个自然空白是“形态-触觉-策略”联合设计或形态参数化搜索，并验证仿真中触觉收益在硬件多朝向条件下是否保持。可与农业 VLA 的仿真到真实适配流程结合，形成跨任务的触觉策略迁移评估。

- **未知物体重建中的观测验证与不确定性量化**：OV-PEAR 用体素占用验证抑制幻觉，MCSplat 用 Fisher 信息不确定性加权几何监督。两者可组合为“生成假设

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-10-21T13:11:19-04:00
**Total number of papers:** 74
**Number of papers added in the latest update:** 27
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

#### 2026-10-20 - EchoNav: Evidential BEV Completion from Historical Observations for Visual Navigation

**Authors:** Diwen Liu, Yiyang Shao, Borui Wang, Chi Zhang, Yunhui Liu
**Links:** [abs](https://arxiv.org/abs/2610.27616) - [pdf](https://arxiv.org/pdf/2610.27616)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, simulation

<details>
<summary>Abstract</summary>

Visual navigation in cluttered environments requires robots to recover previously observed structure and infer obstacles and free space that remain occluded. We present a framework that combines temporal aggregation and occupancy completion in an evidential bird's-eye-view (BEV) representation predicted from short RGB sequences. A decoder adapts frozen VGGT-Omega features and combines historical residual proposals using cellwise weights and a learned no-update option. The BEV predictor produces a local map in the latest ego frame without depth or camera-pose inputs or explicit geometric warping. The evidential model treats observed free space separately and predicts occupancy with associated confidence across the remaining supported region. We train the predictor on simulated RGB sequences paired with complete and visibility-masked occupancy annotations. Our experiments evaluate navigation in simulation and on a wheeled robot, with additional demonstrations on quadruped and humanoid robots. In simulated sequential two-goal navigation, our system achieves 89.6% success, outperforming the strongest evaluated baseline by 32.5 percentage points. Across 60 wheeled-robot trials in 20 scenes, it achieves 73.3% success, compared with 33.3% for the strongest evaluated baseline.

</details>

#### 2026-10-18 - ReDT: Resolution-Decoupled Visual Geometry Transformer

**Authors:** Abteen Arab, Guile Wu, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.25517) - [pdf](https://arxiv.org/pdf/2610.25517)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, 3D reconstruction, multi-view reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReDT: Resolution-Decoupled Visual Geometry Transformer
- 作者：Abteen Arab, Guile Wu, Dongfeng Bai
- 出版日期：2026-10-18T20:17:29Z
- 分类：Geometry Foundation Models；3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.25517) / [PDF](https://arxiv.org/pdf/2610.25517) / [项目网站](https://redt.github.io)

### 一句话总结
ReDT 是一种前馈视觉几何 Transformer，通过将多视图重建的内部注意力表示与输入分辨率解耦，使高分辨率（HD/2K）多视图重建在质量和计算效率上均优于现有方法。

### 研究问题
现有视觉几何 Transformer 通常在固定标准定义（SD）分辨率上训练，面对高输入分辨率时重建质量下降、计算扩展性差。已有高效架构主要降低帧间注意力复杂度，但帧内注意力与编码器注意力的高昂开销仍未解决，导致 HD 重建在现有架构下不切实际。

### 核心思路/方法
ReDT 的核心是分辨率解耦：先将每个视图映射为固定大小的基元 token 集合，在这个紧凑、恒定大小的基元空间中计算对应关系，再将输出投影回原始分辨率进行稠密预测。由于注意力阶段的内部表示与输入分辨率解耦，高分辨率 3D 重建的计算成本大幅降低，同时模型在各分辨率下的性能得到改善。

### 主要贡献
- 提出 ReDT，一种面向高分辨率输入扩展的前馈视觉几何 Transformer。
- 通过固定大小基元 token 空间进行对应计算，解耦内部表示与输入分辨率，缓解帧内与编码器注意力的高开销。
- 在 SD 到 FHD（2K）的多个数据集上取得优于现有视觉几何 Transformer 的重建质量与计算效率。
- 摘要给出的具体结果：在 ETH3D（2K）上相对 VGGT-$Ω$ 实现 $16\times$ 加速、峰值 GPU 内存降低 $34\%$、chamfer distance 降低 $33\%$。

### 局限性
摘要未提供足够信息。未说明方法在极低分辨率、稀疏视图、动态场景或训练数据分布外场景下的表现；未提供消融实验细节、失败案例或计算成本的具体测量条件。

### 阅读优先级
高。理由：该工作直接针对视觉几何 Transformer 在高分辨率多视图重建中的计算瓶颈，提出分辨率解耦的架构思路，并在摘要中给出明确的效率与精度改进数据，与 3D 重建和多视图几何方向高度相关。

</details>

<details>
<summary>Abstract</summary>

We introduce ReDT, a feed-forward visual geometry transformer designed to scale multi-view reconstruction to high-definition (HD) inputs. Existing visual geometry transformers are typically trained at fixed, standard definition (SD) resolutions and exhibit degraded reconstruction quality and poor computational scaling to high input resolutions. While recent efficient architectures reduce the complexity of inter-frame attention, expensive intra-frame and encoder attention remain largely unaddressed, making HD reconstruction impractical with existing architectures. ReDT addresses both limitations with a resolution-aware architecture designed to scale to high-resolution inputs. The key idea of ReDT is to first map each view to a fixed-size set of basis tokens, compute correspondences in this compact constant-size basis space, and then project the outputs back to the original resolution for dense prediction. By decoupling the internal representation from input resolution during attention, ReDT substantially reduces the computational cost of high-resolution 3D reconstruction and improves model performance at all resolutions. Extensive experiments on multiple datasets spanning SD to FHD (2K) show that ReDT outperforms state-of-the-art visual geometry transformers in both reconstruction quality and computational efficiency. For instance, on the ETH3D (2K) dataset, ReDT achieves a $16\times$ speedup, a $34\%$ reduction in peak GPU memory usage, and a $33\%$ reduction in chamfer distance over VGGT-$Ω$. \href{https://redt.github.io}{Project Website.}

</details>

#### 2026-10-15 - Motion- and Gravity-Aware Feedforward 3D Reconstruction

**Authors:** Shiyao Qian, Yuan Ren, Dongfeng Bai
**Links:** [abs](https://arxiv.org/abs/2610.22177) - [pdf](https://arxiv.org/pdf/2610.22177)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** VGGT, feed-forward 3D reconstruction, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Motion- and Gravity-Aware Feedforward 3D Reconstruction
- 作者：Shiyao Qian, Yuan Ren, Dongfeng Bai
- 出版日期：2026-10-15T16:34:04Z
- 分类：主分类 Geometry Foundation Models；次分类 3D Reconstruction & Multi-view Geometry
- 链接：摘要页 https://arxiv.org/abs/2610.22177 ；PDF https://arxiv.org/pdf/2610.22177

### 一句话总结
该论文在 LUPI（Learning Using Privileged Information）框架下，将残差光流和重力方向作为训练期的特权信号注入前馈 Transformer，以提升多视角 3D 重建在动态场景和弱几何线索下的精度与鲁棒性，且不增加推理阶段复杂度。

### 研究问题
前馈 Transformer 在多视角 3D 重建中表现良好，但主要依赖基于外观的注意力机制，在存在动态物体、几何线索薄弱等情形时仍面临困难。论文关注的问题是：如何在不增加测试时复杂度的前提下，把运动信息与物理先验（重力）引入前馈重建模型，以改善动态场景与困难相机运动下的重建表现。

### 核心思路/方法
- 采用 LUPI 范式：训练阶段额外提供残差光流和重力方向作为特权信号，用于指导几何表示学习；推理阶段仅使用标准视觉输入。
- 将这些先验以轻量级结构改动集成到 Transformer 骨干中，保持前馈效率。
- 考察不同注入阶段的影响，发现最优注入阶段依赖骨干网络：对 VGGT 通常中间层集成更优，对 π3 则后期集成更有效。

### 主要贡献
- 提出运动与重力感知的前馈 3D 重建框架，在 LUPI 范式下引入残差光流与重力方向作为训练期特权信号。
- 通过轻量级架构改动将上述先验注入 Transformer 骨干，保持前馈推理效率，不增加测试时复杂度。
- 在标准基准上取得重建精度与鲁棒性的一致提升，尤其在动态物体、结构歧义和挑战性相机运动场景中。
- 分析表明先验注入的最优阶段与骨干相关：VGGT 偏好中间层，π3 偏好后期阶段，为 LUPI 在前馈 3D 重建中的实际应用提供了参考。

### 局限性
- 摘要未提供足够信息说明具体数据集、评价指标、定量提升幅度及消融实验的详细设置。
- 摘要未提供足够信息说明模型规模、训练成本、推理速度或对特权信号质量的敏感度。
- 摘要未提供足够信息说明该方法在非动态或强几何线索场景中的表现，以及是否对特定骨干存在依赖性限制。
- 摘要未提供足够信息说明重力方向与残差光流的具体获取方式及其在真实部署中的可行性。

### 阅读优先级
中。理由：该论文面向多视角 3D 重建中的动态场景与弱几何线索问题，提出的 LUPI 训练期特权信息注入思路具有明确的问题针对性，且强调不增加推理复杂度，对前馈 3D 重建与几何基础模型方向有参考价值；但摘要未给出定量结果与实验细节，是否值得深入阅读需结合具体基准表现和实现细节进一步判断。

</details>

<details>
<summary>Abstract</summary>

Feed-forward transformer models have recently achieved strong performance in multi-view 3D reconstruction, but they still rely primarily on appearance-based attention and often struggle in dynamic scenes with weak geometric cues. In this work, we introduce a motion- and gravity-aware framework under the Learning Using Privileged Information (LUPI) paradigm. During training, residual optical flow and gravity direction are provided as privileged signals to guide geometric representation learning; during inference, the model uses standard visual inputs only. We integrate these priors into transformer backbones with lightweight architectural changes, preserving feed-forward efficiency. Experiments on standard benchmarks show consistent gains in reconstruction accuracy and robustness, especially in scenes with dynamic objects, ambiguous structure, and challenging camera motion. Our analysis further shows that the optimal injection stage is backbone-dependent: middle-layer integration is generally preferable for VGGT, while late-stage integration is more effective for π3. These results suggest that LUPI offers a practical way to inject motion and physical priors into feed-forward 3D reconstruction without increasing test-time complexity.

</details>

## Dynamic / 4D Reconstruction

### 2026-10

#### 2026-10-20 - AEON: Unifying Video and 3D World Models

**Authors:** Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou
**Links:** [abs](https://arxiv.org/abs/2610.28631) - [pdf](https://arxiv.org/pdf/2610.28631)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D reconstruction, 4D Gaussian, Gaussian Splatting, rendering, splatting, simulation, world modeling

<details>
<summary>Abstract</summary>

Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: https://weiqi-zhang.github.io/AEON

</details>

#### 2026-10-20 - RayCo4D: Ray-Conditioned Continuous Motion Model for Monocular 4D Dynamic Reconstruction

**Authors:** Yuanxiang Ni, Xianliang Huang, Ruihan Hou, Feng Xie, Hao Zhang
**Links:** [abs](https://arxiv.org/abs/2610.28351) - [pdf](https://arxiv.org/pdf/2610.28351)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic reconstruction, dynamic 3D, novel view synthesis, view synthesis, rendering

<details>
<summary>Abstract</summary>

Reconstructing dynamic 3D scenes from monocular video requires inferring motion from noisy and intermittently visible observations. Long-range tracks provide valuable geometric constraints, but integrating their fragmented temporal coverage into shared, continuous motion remains challenging. We introduce \textbf{RayCo4D}, a ray-conditioned continuous motion model for monocular 4D reconstruction that explicitly separates visual measurements from latent 3D motion states. Each track is associated with a reference-time 3D query constrained to its camera ray, and its image and depth observations constrain shared latent motion nodes through local many-to-many associations. Each node maintains an $\mathrm{SE}(3)$ pose and body-frame velocity at sparse support times. A white-noise-on-acceleration process prior couples neighboring states and defines continuous-time interpolation, allowing observations across visibility intervals to jointly constrain the same latent state sequence.The inferred shared motion is transferred to Gaussian primitives through dual-quaternion blending, while reference-anchored local $\mathrm{SE}(3)$ residuals capture fine-scale non-rigid deformation beyond the shared scaffold. Experiments on diverse monocular dynamic scenes show that RayCo4D achieves competitive novel-view synthesis quality, improves structural and temporal consistency under rapid motion and incomplete tracks, and supports continuous-time rendering.

</details>

#### 2026-10-20 - SplatFlux: Feed-Forward 4D Gaussian Reconstruction and Generation from Video Latents

**Authors:** Runmin Zhang, Binglin Ren, Zhu Yu, Fudong Wang, Jiangke Lin, Yichun Shentu, Si-Yuan Cao, Yi Yuan, Hui-Liang Shen
**Links:** [abs](https://arxiv.org/abs/2610.28257) - [pdf](https://arxiv.org/pdf/2610.28257)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, dynamic Gaussian, 4D Gaussian

<details>
<summary>Abstract</summary>

This work presents SplatFlux, a feed-forward latent-to-4DGS framework for both video-based 4D reconstruction and conditional 4D generation. Our key observation is that observed videos and conditionally generated content can be represented in the same pretrained video latent space, allowing both tasks to be formulated as latent-to-4DGS decoding. To construct compact and temporally coherent 4D scenes, SplatFlux introduces a static-dynamic decoupled 4D Gaussian representation that explicitly predicts dynamic probabilities for Gaussian primitives. This representation separates static scene structures from moving regions, enabling complete 4D scene construction in a feed-forward manner through static aggregation and dynamic motion interpolation. To learn static-dynamic decomposition and dynamic Gaussian motion without costly annotations, we further develop an auxiliary distillation strategy that provides pseudo dynamic masks and optical-flow cues. Extensive experiments across 3D and 4D reconstruction and generation demonstrate that SplatFlux achieves state-of-the-art performance.

</details>

#### 2026-10-20 - Causal Spatiotemporal State Evolution for Monocular 4D Reconstruction

**Authors:** Qiaowei Miao, Yijing Guo, Lipei Zhang, Qifeng Cheng, Yuru Xiao, Ziqian Ni, Sheng Yang
**Links:** [abs](https://arxiv.org/abs/2610.27594) - [pdf](https://arxiv.org/pdf/2610.27594)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, dynamic 4D

<details>
<summary>Abstract</summary>

While feed-forward models excel in static 3D geometry estimation, extending them to dynamic 4D scenes requires modeling visual geometry as a causally evolving state. Current methods typically rely on unordered temporal aggregation, which lacks the directional structure of physical time. Furthermore, existing supervision often treats geometry and motion as disjoint objectives, failing to exploit their inherent physical coupling. Consequently, they lack a unified constraint to effectively supervise temporal state transitions, leading to inconsistent 4D scene representations. To address this, we propose a feed-forward framework for causal 4D visual geometry learning from monocular videos. At its core, Causal Spatiotemporal Mamba augments temporal aggregation with directional state propagation. Through complementary Temporal-Spatial and Spatial-Temporal Scans, CSM continuously propagates geometry-aware states across frames to model spatiotemporal evolution. To align this causal state evolution with observable dynamics, we introduce Unified Motion Supervision. Rather than treating motion as an independent objective, UMS leverages geometry-aware predictions from the camera and depth heads to construct a unified forward motion field that is consistent with the underlying 3D structure. This geometry-grounded supervision explicitly constrains inter-frame state transitions, enabling stable states propagation across frames. Extensive evaluations on dynamic benchmarks demonstrate state-of-the-art performance across video depth, camera pose, and optical flow estimation. These results validate that the synergy between the directional state propagation of Causal Spatiotemporal Mamba and Unified Motion Supervision effectively captures continuous scene evolution, significantly reducing temporal drift and reinforcing spatial-temporal consistency in 4D representation learning.

</details>

#### 2026-10-19 - Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos

**Authors:** Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
**Links:** [abs](https://arxiv.org/abs/2610.26585) - [pdf](https://arxiv.org/pdf/2610.26585)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** metric depth, dynamic 4D, 4D Gaussian, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Drive2Gauss: FeedForward 4D Gaussian Reconstruction from Multimodal Generative Driving Videos
- 作者：Tong Zhao, Zhiyuan Han, Lin Chen, Bowen Xie, Yunxi Qiao, Bohan Li, Weiqing Xiao, Gen Li, Shu Han, Xuyang Dai, Cheng Bi, Hao Zhao, Chaojian Li
- 出版日期：2026-10-19T15:34:28Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：摘要页 https://arxiv.org/abs/2610.26585；PDF https://arxiv.org/pdf/2610.26585

### 一句话总结
Drive2Gauss 提出一种前馈框架，将从参考多视角图像与未来控制信号联合生成的 RGB、度量深度和动态流转换为动态 4D 高斯场景，从而避免逐序列优化。

### 研究问题
生成可复用的驾驶环境需要：既可控制未来观测，又要有支持不同视角渲染的显式表示。然而现有方法仍需针对每条生成 RGB 视频逐序列优化来恢复显式场景，效率与可复用性受限。论文即针对这一“生成视频到显式动态场景”的重建问题展开。

### 核心思路/方法
方法由两部分构成：
1. **多模态视频生成器**：从参考多视角图像和未来控制信号预测 RGB、度量深度和动态流三种模态；
2. **高斯查询解码器**：用深度初始化稀疏 3D 查询，用动态流在时间维度关联查询，并通过时空特征聚合与迭代查询细化融合外观信息。

重建阶段以单次前馈完成，无需针对每个场景做优化。

### 主要贡献
- 提出 Drive2Gauss 前馈框架，把联合生成的 RGB、度量深度与动态流转换为动态 4D 高斯场景。
- 设计高斯查询解码器，利用深度初始化稀疏 3D 查询、利用动态流建立跨时间关联，并结合时空特征聚合与迭代细化。
- 重建不再依赖逐场景优化，实现单次前馈推理。
- 在 nuScenes 上报告：未来 RGB 生成 FID 6.38、FVD 12.43；重建其生成观测的 PSNR 为 29.91 dB；并支持横向相机偏移下的直接渲染与下游视频修复。

### 局限性
摘要未提供足够信息。摘要未说明方法在更多数据集上的泛化性、失败案例、计算开销、对生成模态质量的敏感性，也未给出与逐序列优化方法的系统性对比细节。

### 阅读优先级
**中**。理由：该工作与“生成式驾驶视频驱动的 4D 重建”直接相关，核心思路（多模态生成 + 前馈高斯查询解码）清晰，且有 nuScenes 上的量化结果；若关注动态 4D 重建或驾驶场景生成，值得阅读。但摘要未提供与优化式方法的对比细节和泛化性证据，且兴趣方向未额外指定，因此不列为高优先级。

</details>

<details>
<summary>Abstract</summary>

Generating reusable driving environments requires both controllable future observations and an explicit representation that supports rendering from different viewpoints, yet existing methods still recover explicit scenes from generated RGB videos through optimization for each sequence. To overcome these limitations, we present Drive2Gauss, a feedforward framework that converts jointly generated RGB, metric depth, and dynamic flow into dynamic 4D Gaussian scenes. A Multimodal Video Generator predicts the three modalities from reference multiview images and future control signals. Furthermore, we introduce a Gaussian Query Decoder that uses depth to initialize sparse 3D queries and flow to associate the queries across time, and integrates appearance information through spatiotemporal feature aggregation and iterative query refinement. The reconstruction stage operates in a single feedforward pass without optimization for each scene. Extensive results on nuScenes demonstrate that our approach attains an FID of 6.38 and an FVD of 12.43 for future RGB generation, a PSNR of 29.91 dB when reconstructing its generated observations, and supports both direct rendering under lateral camera shifts and downstream video fixing. Code and more visualizations are available at https://zttt04. github.io/Drive2Gauss_page/.

</details>

#### 2026-10-18 - Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion

**Authors:** Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
**Links:** [abs](https://arxiv.org/abs/2610.25276) - [pdf](https://arxiv.org/pdf/2610.25276)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion
- 作者：Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi
- 出版日期：2026-10-18T13:47:01Z
- 分类：主分类 Dynamic / 4D Reconstruction；次分类 Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25276)｜[PDF](https://arxiv.org/pdf/2610.25276)

### 一句话总结
Holo4D 将前馈 4D 重建得到的 3D 轨迹投影到目标视角，作为几何与外观的条件引导预训练视频扩散模型，实现单目视频的新相机轨迹重拍。

### 研究问题
从新相机轨迹合成单目视频，需要同时保持已观测场景的几何与运动，并补全新变为可见的区域。前馈 4D 重建器能恢复观测场景结构，视频扩散模型提供生成先验；论文关注如何将两者结合，以重建立足生成、以生成补全未观测区域。

### 核心思路/方法
提出名为 Holo4D 的视频重拍框架：将重建的 3D 轨迹作为整体性的源视角 4D 脚手架（scaffold）；把这些轨迹投影到请求的目标视角，并编码其几何与源外观，用于引导预训练视频扩散模型。结合源视频与目标相机，脚手架使生成以重建观测为依据，而未支持区域交由生成先验补全。框架可适配不同的 4D 重建器，无需重新训练视频生成器。

### 主要贡献
- 提出以重建 3D 轨迹作为整体源视角 4D 脚手架来条件化视频扩散模型的视频重拍框架。
- 将轨迹投影到目标视角并编码几何与源外观，以引导预训练视频扩散模型。
- 实验表明基于轨迹的条件化对相机控制和新视角合成具有价值。
- 框架可容纳不同 4D 重建器且无需重训视频生成器，从而有望受益于源重建的后续进展。

### 局限性
摘要未提供足够信息（未给出失败情形、计算开销、重建器依赖程度或评测细节等具体局限）。

### 阅读优先级
高。理由：论文聚焦 4D 重建与视频扩散的结合，以重建轨迹作为几何控制，且强调无需重训生成器即可适配不同重建器；对动态/4D 重建与神经场景表示渲染方向具有直接相关性。

</details>

<details>
<summary>Abstract</summary>

Synthesizing a monocular video from a new camera trajectory requires preserving the observed scene geometry and motion while completing regions that become newly visible. Feed-forward 4D reconstructors recover the structure of the observed scene, whereas video diffusion models provide a generative prior for completing unseen content. We introduce Holo4D, a video reshooting framework that uses reconstructed 3D trajectories as a holistic source-view 4D scaffold. We project these trajectories into the requested views and encode their geometry and source appearance to guide a pretrained video diffusion model. Together with the source video and target cameras, the scaffold grounds generation in reconstructed observations while leaving unsupported regions to the generative prior. Experiments demonstrate the value of trajectory-based conditioning for camera control and novel-view synthesis. The framework accommodates different 4D reconstructors without retraining the video generator, allowing it to benefit from future advances in source reconstruction. More details can be found in our project page.

</details>

#### 2026-10-14 - DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning

**Authors:** Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han, Hang Xu, Xiaodan Liang, Jia-Wang Bian
**Links:** [abs](https://arxiv.org/abs/2610.20598) - [pdf](https://arxiv.org/pdf/2610.20598)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** None
**Matched keywords:** dynamic 4D, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DynThinker: Unifying Static 3D and Dynamic 4D Spatial Reasoning
- 作者：Qihang Cao, Haoyuan Li, Zihan Guo, Sensen Gao, Zihui Gao, Huixin Zhang, Fan He, Jianhua Han, Hang Xu, Xiaodan Liang, Jia-Wang Bian
- 出版日期：2026-10-14T17:59:31Z
- 分类：主分类 Dynamic / 4D Reconstruction；二级分类未提供
- 链接：摘要链接 https://arxiv.org/abs/2610.20598 ；PDF 链接 https://arxiv.org/pdf/2610.20598

### 一句话总结
DynThinker 提出统一框架，通过 D-EMA 与 Spatial-Dynamic Fusion 缓解静态 3D 与动态 4D 空间推理之间的相互干扰，从而在同一个模型中同时增强两类空间推理能力。

### 研究问题
论文关注的问题是：实现通用空间智能需要同时理解静态 3D 与动态 4D，但现有模型难以在两者上都表现优异。摘要指出，3D 后训练可能削弱动态理解，而 4D 专用模型往往缺乏强静态 3D 推理能力。作者进一步分析认为，这种“空间—动态干扰”在不同参数组之间高度不均匀，静态与动态能力之间的平衡对后层 MLP 的变化尤其敏感。

### 核心思路/方法
针对上述干扰，论文提出统一框架 DynThinker，用于联合增强静态与动态空间推理。方法包含两个核心组件：
1. **Decoupled Exponential Moving Average (D-EMA)**：对参数进行可配置的分组平均，以约束对干扰敏感的预训练参数发生漂移，同时保留能力增强的灵活性。
2. **Spatial-Dynamic Fusion (SDF)**：在语义引导下，选择性地将动态几何编码器中的空间先验和时间先验整合进 VLM 的中间表示，与 D-EMA 形成互补。

### 主要贡献
- 发现并指出静态 3D 与动态 4D 空间推理之间存在非均匀的“空间—动态干扰”，且该平衡对后层 MLP 变化尤为敏感。
- 提出 DynThinker 统一框架，联合增强静态 3D 与动态 4D 空间推理。
- 提出 D-EMA，用于约束干扰敏感预训练参数的漂移。
- 提出 SDF，在语义引导下将动态几何编码器的空间与时间先验选择性融合进 VLM 中间表示。
- 在覆盖九个静态 3D 与动态 4D 基准的十个指标上，DynThinker 取得所有评估模型中的最高平均分；并在 ReVSI、DSR-Bench、DSI-Bench 的 sample-wise 与 group-wise 评测协议上分别取得 56.0、67.2、51.2 和 40.1，在统一模型下于这四项评测中刷新所比较开源模型的最优结果。

### 局限性
摘要未提供足够信息说明 DynThinker 的局限性，例如失败场景、计算开销、对特定基准或数据分布的依赖、消融实验的完整结果，以及 D-EMA 与 SDF 各自贡献的详细定量分析，均未在摘要中给出。

### 阅读优先级
高。理由：该论文直接针对静态 3D 与动态 4D 空间推理之间的干扰问题，提出统一框架，并在摘要中报告了跨九个基准、十个指标的领先平均成绩，以及四项评测中的开源模型最优结果，主题明确且结果陈述集中，适合优先阅读以了解统一空间推理方法的设计思路。

</details>

<details>
<summary>Abstract</summary>

Achieving general spatial intelligence requires a unified understanding of both static 3D and dynamic 4D. However, we find that existing models struggle to excel at both: 3D post-training can weaken dynamic understanding, while 4D-specialized models often lack strong static 3D reasoning. Our analysis reveals that this spatial--dynamic interference is highly non-uniform across parameter groups, with the balance between static and dynamic capabilities particularly sensitive to changes in late-layer MLPs. To address this interference, we propose DynThinker, a unified framework for jointly strengthening static and dynamic spatial reasoning. Decoupled Exponential Moving Average (D-EMA) applies configurable group-wise averaging to constrain drift in interference-sensitive pretrained parameters while preserving flexibility for capability enhancement. Spatial-Dynamic Fusion (SDF) complements D-EMA by selectively integrating spatial and temporal priors from a dynamic geometry encoder into intermediate VLM representations under semantic guidance. Across ten metrics spanning nine static 3D and dynamic 4D benchmarks, DynThinker achieves the highest average score among all evaluated models. Notably, DynThinker achieves 56.0 on ReVSI, 67.2 on DSR-Bench, and 51.2 and 40.1 under the sample-wise and group-wise evaluation protocols of DSI-Bench, respectively, setting new state-of-the-art results among the compared open-source models across all four evaluations within a unified model.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-10

#### 2026-10-20 - SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images

**Authors:** Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian
**Links:** [abs](https://arxiv.org/abs/2610.28585) - [pdf](https://arxiv.org/pdf/2610.28585)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, robotics, manipulation, simulation

<details>
<summary>Abstract</summary>

Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system that turns a single image into an editable, simulation-ready scene. SceneRig combines geometric, visual, and physical tools to reconstruct a faithful 3D scene. An agent then performs edit-and-validate loops inside a physics simulator to achieve physical stability. Across diverse inputs, SceneRig improves instance segmentation, object-centric appearance, and 3D placement while keeping the reconstructed scenes physically stable. Furthermore, SceneRig is effective for downstream robotics: its scenes predict real-robot policy outcomes more accurately than the baseline method and more reliably support replay of recorded manipulations without trajectory adaptation.

</details>

#### 2026-10-20 - Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment

**Authors:** Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang
**Links:** [abs](https://arxiv.org/abs/2610.28521) - [pdf](https://arxiv.org/pdf/2610.28521)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, geometric reconstruction

<details>
<summary>Abstract</summary>

Video generation and feed-forward 3D reconstruction typically use separate representations, requiring RGB decoding and visual re-encoding to recover geometry from generated latents. We propose Latent Bridge, which connects video generative latent spaces with geometric feature spaces to directly predict 3D geometry from video latents. We develop representation-specific bridges for Wan2.1 and V-RAE, enabling feed-forward prediction of cameras, depth, and 3D point clouds without the intermediate RGB pathway. Each bridge is trained on RGB videos through feature distillation, while the video encoder and geometry model remain frozen. Training requires neither ground-truth geometry nor execution of the downstream geometric aggregator or prediction heads. At inference, the same video latents support both RGB decoding and geometry prediction. The same trained bridge can be reused for image-to-video and text-to-video generation within the same video latent space, without bridge retraining. Experiments on Co3Dv2 and WildRGB-D demonstrate competitive geometric reconstruction quality, efficient end-to-end generation and reconstruction, and faster latent-to-geometry decoding, highlighting latent alignment as a practical and reusable interface between video generation and 3D reconstruction. Our code is available at: https://github.com/hustvl/Latent-Bridge.

</details>

#### 2026-10-20 - CrossFit-GS: Out-of-Fold Pose Estimation for COLMAP-Free 3D Gaussian Splatting

**Authors:** Zijian Wu, Jinliang Wang, Mingfeng Jiang, Zidian Lin, Ying Song, Ziqian Lu
**Links:** [abs](https://arxiv.org/abs/2610.28190) - [pdf](https://arxiv.org/pdf/2610.28190)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** structure from motion, SfM, camera pose estimation, pose estimation, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>Abstract</summary>

Pose-free 3D Gaussian Splatting (3DGS) aims to bypass cumbersome Structure-from-Motion (SfM) by directly reconstructing scenes from unposed image sequences. In this work, we present CrossFit-GS, a deferred-commitment progressive framework that mitigates cumulative trajectory drift and breaks the self-reinforcing loop of distorted-map error propagation. Specifically, we partition the input sequence into interleaved subsets and maintain two complementary submaps. Each candidate pose is cross-refined against a frozen opposite submap that has never been optimized using the target frame, thereby providing an independent geometric reference for pose estimation. Checkerboard validation and spatial coverage safeguards further reject unreliable updates, and only verified poses are committed to their corresponding owner submap. Once the trajectory has been refined, the intermediate submaps are discarded and the final global representation is trained from scratch using the fixed refined poses. Extensive evaluations across multiple benchmarks demonstrate that CrossFit-GS substantially reduces cumulative trajectory drift and consistently improves both camera pose estimation and novel-view synthesis over existing methods.

</details>

#### 2026-10-20 - Radar-Based 3D Human Pose Estimation via Motion-Aware Pose Initialization and Observation-Guided Refinement

**Authors:** Woo-Jin Jung, Chan-Bin Lim, Seung-Hyun Kong
**Links:** [abs](https://arxiv.org/abs/2610.27774) - [pdf](https://arxiv.org/pdf/2610.27774)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, localization

<details>
<summary>Abstract</summary>

3D Human Pose Estimation (3D HPE) is used in indoor environments, such as smart homes, to analyze human movement and monitor human states. Millimeter-wave (mmWave) radar is suitable for this task because it is robust to lighting variations and does not capture images of human appearance. However, radar observations often provide insufficient information about certain body parts or contain overlapping reflections from multiple body parts, limiting accurate 3D joint localization. To address these limitations, we propose the Initialization-to-Refinement Pose Framework (I2R-Pose), comprising two stages: Motion-Aware Pose Initialization and Observation-Guided Refinement. In the first stage, joint-wise features are learned by incorporating temporal relationships across consecutive radar observations and human skeletal structure to compensate for insufficient joint information and estimate an initial 3D pose sequence. In the second stage, separately extracted radar observation features predict joint-wise positional corrections that refine the initial pose and generate the final pose sequence. The framework supports individual and fused inputs of time-Doppler/time-range (TD/TR) maps and radar point clouds (PCs). To evaluate performance across indoor activities, we construct the Radar Motion and Spatial Information for 3D Human Pose Estimation (RaMoS-Pose) dataset, providing synchronized TD/TR maps, radar PCs, and 3D joint ground truth (GT). Evaluations on RaMoS-Pose and the publicly available MVDoppler-Pose dataset show that I2R-Pose reduces mean per-joint position error (MPJPE) by 39.50% on MVDoppler-Pose and by 15.13% on RaMoS-Pose with fused inputs, compared with the best-performing existing methods evaluated on each dataset.

</details>

#### 2026-10-20 - SynCalib: Breaking Dataset Shortcuts in LiDAR-Camera Calibration via Extrinsic-Controllable Synthesis

**Authors:** Huihua Zhu, Shuyang Zhang, Dongqing Chen, Zhuo Yu, Jianhao Jiao, Yilong Zhu, Siyu Teng, Xiaopin Zhong, Zongze Wu
**Links:** [abs](https://arxiv.org/abs/2610.27547) - [pdf](https://arxiv.org/pdf/2610.27547)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera calibration, robotics

<details>
<summary>Abstract</summary>

Online LiDAR-camera calibration remains a fundamental yet challenging task in the field of robotics. Recently, deep learning-based data-driven approaches have emerged, offering high-precision, targetless calibration capabilities. However, existing methods often suffer from a critical dataset shortcut phenomenon due to the lack of extrinsic diversity in their training data. Networks tend to overfit to fixed nominal extrinsic configurations, leading to severe performance degradation and poor generalization in real-world deployments. To address this limitation, we propose a highly generalizable data generation framework tailored for training LiDAR-camera calibration networks. Our framework leverages existing omnidirectional image datasets annotated with depth ground truth to synthesize multi-modal calibration data under rigorous extrinsic constraints. Extensive experiments demonstrate that the data generated by our pipeline significantly enhances the generalization and robustness of typical learning-based calibration networks. Furthermore, we conduct comprehensive real-world evaluations across various camera-LiDAR configurations, validating the zero-shot transfer capability of models trained exclusively on our synthetic data. To facilitate future research and community use, the code for data generation, the pre-trained models, and online benchmark datasets will be made publicly available.

</details>

#### 2026-10-20 - OmniVLoc: Topo-metric Visual Localization for Omnidirectional Cameras

**Authors:** Zhuo Yu, Shuyang Zhang, Huihua Zhu, Wenjia Ouyang, Zuo Zuo, Jianhao Jiao, Yilong Zhu, Xiaopin Zhong, Zongze Wu
**Links:** [abs](https://arxiv.org/abs/2610.27522) - [pdf](https://arxiv.org/pdf/2610.27522)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** bundle adjustment, depth estimation, monocular depth, localization

<details>
<summary>Abstract</summary>

Omnidirectional cameras provide surround-view information, significantly overcoming the field-of-view constraints for traditional visual localization systems. However, existing localization systems fail to fully exploit the characteristics of omnidirectional cameras, struggling to deliver accurate and robust localization performance amidst scene content variations and illumination-induced appearance changes. In this work, we propose OmniVLoc, a surround-view localization system based on a topo-metric framework. By integrating state-of-the-art global place recognition and monocular depth estimation methods, we introduce a multi-constrained visual localization paradigm. By solving a scale-aware pose graph and performing precise spherical bundle adjustment, we accurately recover the metric-level pose for each query frame.Furthermore, a hierarchical verification mechanism is designed to filter out erroneous outputs across different stages, effectively bolstering the overall system robustness. Extensive experiments on both public and our custom datasets validate the superior accuracy and reliability of OmniVLoc. To benefit the community, our source code and dataset will be made publicly available upon publication.

</details>

#### 2026-10-19 - MatchCityLoc: Aerial Localization in LoD City Models via Surface Normal Matching

**Authors:** Oussema Dhaouadi, Zuria Bauer, Johannes Michael Meier, Marc Pollefeys, Daniel Cremers, Olaf Wysocki
**Links:** [abs](https://arxiv.org/abs/2610.27110) - [pdf](https://arxiv.org/pdf/2610.27110)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** pose estimation, feature matching, localization

<details>
<summary>Abstract</summary>

Autonomous Unmanned Aerial Vehicle (UAV) navigation in urban environments requires precise pose estimation. Because Global Navigation Satellite System (GNSS) signals are often unreliable in cities, visual localization serves as a crucial complement. Within this domain, textureless Level-of-Detail (LoD) city models provide a lightweight and privacy-preserving substitute for heavy 3D textured meshes. However, localizing against abstract geometry is challenging. Existing pipelines typically score 2D silhouette overlaps, which can suffer from severe geometric ambiguities. We present MatchCityLoc, a framework that shifts this paradigm to direct feature matching from a noisy 6-DoF pose prior. By extracting surface normals from the query image using a zero-shot foundation model and matching them against rendered LoD normals, we establish explicit 3D-to-2D correspondences. This enables a Perspective-n-Point (PnP) pose solve, which we iteratively refine through a render-and-match loop. Experiments demonstrate strong pose recall and accurate translation and rotation among the evaluated off-the-shelf LoD-based methods with very few renderings. By bridging the modality gap between aerial imagery and texture-free geometry, MatchCityLoc enables accurate localization using lightweight, privacy-preserving city models.

</details>

#### 2026-10-19 - SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?

**Authors:** Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
**Links:** [abs](https://arxiv.org/abs/2610.26659) - [pdf](https://arxiv.org/pdf/2610.26659)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D mapping, camera calibration, mapping, localization, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?
- 作者：Zhaoxi Zhang, Hao Liang, Linxuan Wu, Yiming Wu, Yifu Yuan, Kun Liang, Chenming Tang, Meiyi Qiang, Wentao Zhang, Weikang Li
- 出版日期：2026-10-19T16:17:48Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26659) / [PDF](https://arxiv.org/pdf/2610.26659) / [代码](https://github.com/JesseZZZZZ/SpatialScout)

### 一句话总结
论文提出 SpatialScout 基准，用于评估视觉语言模型（VLM）智能体在主动探索室内场景时构建对象级三维度量地图的能力，并揭示当前前沿模型在精确定位与目标覆盖上的显著不足。

### 研究问题
摘要指出，空间智能要求智能体主动获取视觉证据，并将观测整合为对三维世界的一致表示；然而，现有的空间问答任务难以充分证明模型能否通过自主探索构建准确的度量地图。论文因此关注：VLM 智能体能否在有限交互预算下主动探索场景，并在统一坐标系中估计目标物体中心，从而完成对象级三维建图。

### 核心思路/方法
- 构建 SpatialScout 基准，包含 80 个多样室内场景和 3,140 个目标物体。
- 任务输入包括目标物体清单、RGB 观测、相机标定和相机位姿；智能体控制相机探索场景，并估计各目标物体中心在共享坐标系中的位置。
- 任务要求智能体协调视角选择、跨视角关联、几何估计和地图修正，且交互预算有限。
- 评估同时衡量定位精度与目标覆盖度，采用对象尺度重叠分数并对遗漏预测进行惩罚。
- 论文对前沿 VLM 进行实验评估。

### 主要贡献
- 提出面向主动对象级三维建图的 VLM 智能体基准 SpatialScout，强调通过自主探索构建度量地图，而非仅回答空间问题。
- 设计了结合定位精度与目标覆盖度的评估方式，使用对象尺度重叠分数并惩罚遗漏预测。
- 通过实验揭示当前前沿 VLM 的明显局限：最强评估模型 Claude Opus 5.5 的平均重叠分数为 41.71%，仅 47.23% 的目标超过 IoU 0.5，超过 IoU 0.9 的目标仅 3.25%。
- 指出模型在恢复粗略物体布局与构建完整、精确度量地图之间存在显著差距，并提供可量化测试平台与代码链接。

### 局限性
- 摘要未提供足够信息说明基准场景的具体来源、数据采集方式及场景多样性细节。
- 摘要未提供足够信息说明交互预算的具体数值、相机控制接口或动作空间设计。
- 摘要未提供足够信息说明除 Claude Opus 5.5 外参与评估的完整模型列表及各自详细结果。
- 摘要未提供足够信息说明失败模式分析、消融实验或方法改进建议。
- 摘要未提供足够信息说明评估指标的具体计算细节及与真实标注的匹配方式。

### 阅读优先级
高。理由：该论文直接针对 VLM 智能体主动三维感知与建图能力提出新基准，任务定义和评估指标明确，且摘要给出了量化结果与显著能力差距；对三维重建、多视角几何、具身智能和机器人应用方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploration. We introduce SpatialScout, a benchmark for evaluating vision-language model (VLM) agents on active object-level 3D mapping. SpatialScout comprises 80 diverse indoor scenes containing 3,140 target objects. Given an object inventory, RGB observations, camera calibration, and camera poses, agents control a camera to explore each scene and estimate object centers in a shared coordinate frame. The task requires coordinating viewpoint selection, cross-view association, geometric estimation, and map revision under bounded interaction budgets. Evaluation jointly measures localization accuracy and target coverage through object-scale overlap scores that penalize missing predictions. Experiments with frontier VLMs reveal substantial limitations: the strongest evaluated model, Claude Opus 5.5, achieves a mean overlap score of 41.71%, with 47.23% of targets exceeding an intersection-over-union (IoU) threshold of 0.5 and only 3.25% exceeding 0.9. These results reveal a substantial gap between recovering coarse object layouts and constructing complete, precise metric maps. SpatialScout provides a quantitative testbed for developing agents that build reliable 3D spatial representations through active perception. Code is available at https://github.com/JesseZZZZZ/SpatialScout.

</details>

#### 2026-10-19 - EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation

**Authors:** Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
**Links:** [abs](https://arxiv.org/abs/2610.26641) - [pdf](https://arxiv.org/pdf/2610.26641)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoRayFormer: Ray-Space Stereo Refinement for Egocentric 3D Human Pose Estimation
- 作者：Haozhe Wang, Songyuan Wu, Jihai Xu, Jie Zhao
- 出版日期：2026-10-19T16:03:20Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；未提供二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26641) / [PDF](https://arxiv.org/pdf/2610.26641)

### 一句话总结
EgoRayFormer 面向头戴式双目鱼眼相机下的第一人称 3D 人体姿态估计，在射线空间中耦合双目特征采样与几何细化，以引入显式双目约束，并在几何约束较弱时保留学习式更新的灵活性。

### 研究问题
头戴式双目鱼眼相机能提供穿戴者身体的紧凑视角，但强畸变、部分可见性和短基线使 3D 姿态估计困难。摘要指出现有细化解码器在各视图中独立采样图像特征，不要求这些采样对应共同的 3D 假设，因而缺少显式双目几何约束。论文即针对这一问题提出改进。

### 核心思路/方法
论文提出因果姿态估计器 EgoRayFormer，将双目特征采样与几何细化耦合在射线空间中。对每个关节，解码器沿其视线射线并在射线周围，把共享的 3D 假设投影到两幅图像中；随后几何分支校正投影后的关节位置，并对所得射线进行相交；一个学习到的门控将几何估计与学习到的姿态更新融合。该形式化方法引入显式双目约束，同时在射线提供弱深度约束时保留灵活性。

### 主要贡献
- 提出 EgoRayFormer，在射线空间中耦合双目特征采样与几何细化，用于第一人称 3D 人体姿态估计。
- 通过将共享 3D 假设沿/绕观测射线投影到双视图，并对校正后的射线求交，引入显式双目约束；再用学习门控融合几何估计与学习姿态更新。
- 摘要报告在官方设备相对测试划分上的本地评估结果：UnrealEgo2 上三随机种子平均 MPJPE 为 17.64 mm，UnrealEgo-RW 上为 49.55 mm，使用 UnrealEgo2 预训练后提升至 47.57 mm。
- 配对验证消融显示，在两种输入分辨率下移除几何分支均使三个随机种子的 MPJPE 增加。
- 在相同 ResNet-18 编码器和输入分辨率下，相较设备相对的 EgoPoseFormer 基线，将 RW 测试 MPJPE 降低 9.09 mm。
- 另有一项协议分析量化设备相对评估与 oracle-root 评估之间的差异。

### 局限性
摘要未提供足够信息说明方法在真实场景泛化、计算开销、对极端遮挡或强畸变的失败模式等方面的局限；也未提供跨数据集以外的完整实验细节。仅从摘要可知，部分结果来自本地评估与特定测试划分，且预训练依赖 UnrealEgo2。

### 阅读优先级
中。理由：该论文聚焦第一人称双目鱼眼 3D 人体姿态估计中的显式双目几何约束与射线空间细化，问题定义和方法动机较清晰，并报告了 MPJPE 改进与消融结果；但摘要未提供真实场景验证、计算成本及更广泛失败模式的信息，是否高优先级取决于读者对第一人称姿态估计或多视图几何细化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Head-mounted stereo fisheye cameras provide a compact view of the wearer's body, but strong distortion, partial visibility and a short baseline make 3D pose estimation difficult. Existing refinement decoders sample image features independently in each view, without requiring the samples to correspond to a common 3D hypothesis. We introduce EgoRayFormer, a causal pose estimator that couples stereo feature sampling and geometric refinement in ray space. For each joint, the decoder projects shared 3D hypotheses along and around its viewing ray into both images. A geometric branch then corrects the projected joint locations and intersects the resulting rays; a learned gate blends this geometric estimate with a learned pose update. This formulation introduces an explicit stereo constraint while retaining flexibility when the rays provide weak depth constraints. In local evaluations on the official device-relative test splits, EgoRayFormer achieves three-seed mean MPJPEs of 17.64 mm on UnrealEgo2 and 49.55 mm on UnrealEgo-RW, improving to 47.57 mm with UnrealEgo2 pre-training. In paired validation ablations, removing the geometric branch increases MPJPE in all three seeds at both input resolutions. With a common ResNet-18 encoder and input resolution, our system reduces RW test MPJPE by 9.09 mm relative to the device-relative EgoPoseFormer baseline. A separate protocol analysis quantifies the difference between device-relative and oracle-root evaluation.

</details>

#### 2026-10-19 - CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments

**Authors:** Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
**Links:** [abs](https://arxiv.org/abs/2610.26633) - [pdf](https://arxiv.org/pdf/2610.26633)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CAOS-SLAM: Class-Agnostic Object-Aware Real-Time vSLAM for Dynamic Environments
- 作者：Gaia Borghi, João Carlos Virgolino Soares, Angelo Bratta, Shahab Heshmati-Alamdari, Claudio Semini
- 出版日期：2026-10-19T16:00:00Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.26633) | [PDF](https://arxiv.org/pdf/2610.26633)

### 一句话总结
CAOS-SLAM 在 ORB-SLAM3 基础上引入混合感知流程，实时检测、跟踪并过滤语义已知与未见过的运动物体，以减少动态特征对定位与建图的干扰。

### 研究问题
动态环境中的运动物体会引入错误观测，破坏地图重建并降低定位精度。现有 vSLAM 方法常依赖预定义语义类别或昂贵的逐像素分类，限制了其在真实场景中的鲁棒性或适用性。论文旨在解决对语义已知和此前未见运动物体的实时检测、跟踪与动态特征剔除问题。

### 核心思路/方法
论文提出 CAOS-SLAM，一个动态 vSLAM 框架，扩展 ORB-SLAM3 并加入混合感知流程，用于实时检测、跟踪和过滤语义已知及此前未见过的运动物体。方法包括：按需执行全景分割用于物体发现；通过未分类区域的深度聚类实例化候选未知物体；在全景分割更新之间，利用可用的轻量检测或基于世界坐标系 Kalman 预测、深度一致性和外观相似性的时序掩码传播来更新持续物体轨迹；随后利用估计的物体运动从 SLAM 流程中剔除动态特征。

### 主要贡献
- 提出 CAOS-SLAM 动态 vSLAM 框架，扩展 ORB-SLAM3，支持对语义已知和未见运动物体的实时检测、跟踪与过滤。
- 设计混合感知流程：按需全景分割、基于深度聚类的未知物体实例化，以及结合轻量检测或时序掩码传播的持续物体跟踪。
- 利用估计的物体运动剔除动态特征，提升动态环境下的定位表现。
- 摘要称在多个动态 RGB-D 数据集和真实实验上优于现有动态 vSLAM 方法：未知动态物体场景定位误差最高降低 59%，严重遮挡场景最高降低 88%，在笔记本电脑上达到 30 FPS 的中位处理速率。
- 跟踪模块提供物体轨迹和速度估计，摘要称可支持动态环境下感知、导航和运动规划等潜在应用。

### 局限性
摘要未提供足够信息说明方法在极端场景、计算资源受限平台、长期运行稳定性或失败模式方面的局限。摘要提到代码和数据集将在接收后发布，但未提供具体实验细节、数据集名称或消融结果。

### 阅读优先级
高。理由：该论文直接针对动态环境下 vSLAM 的鲁棒性与实时性问题，提出类无关物体感知与动态特征剔除框架，并给出定位误差降低和 30 FPS 的摘要级结果；对动态 SLAM、机器人感知与导航相关研究具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Robust visual Simultaneous Localization and Mapping (vSLAM) in dynamic environments faces challenges due to the presence of moving objects that may introduce erroneous observations, corrupt the map reconstruction and overall degrade localization accuracy. Existing vSLAM approaches often rely on predefined semantic classes or costly pixel-wise classification, limiting their robustness or applicability in real-world scenarios. This paper presents CAOS-SLAM, a dynamic vSLAM framework that extends ORB-SLAM3 with a hybrid perception pipeline to detect, track, and filter both semantically known and previously unseen moving objects in real-time. On-demand panoptic segmentation is performed for object discovery, with candidate unknown objects instantiated through depth-based clustering of unclassified regions. Between panoptic updates, persistent object tracks are updated using lightweight detection when available or temporal mask propagation based on world-frame Kalman prediction, depth consistency, and appearance similarity. The estimated object motion is then used to reject dynamic features from the SLAM pipeline. Experimental results on multiple dynamic RGB-D datasets and real-world experiments demonstrate improved localization accuracy over state-of-the-art dynamic vSLAM approaches, achieving up to 59% lower localization error in scenes characterized by unknown dynamic objects and up to 88% lower error in heavily occluded scenes, while achieving a median processing rate of 30 FPS on a laptop. Furthermore, the tracking module provides estimates of object trajectories and velocities, supporting potential future applications in perception, navigation, and motion-planning tasks in dynamic environments. Code and dataset will be released upon acceptance.

</details>

#### 2026-10-19 - PnP-Transformer: A Neural Pose Solver for Zero-Shot 6D Object Pose Estimation

**Authors:** Emirkan Burak Yilmaz, Yakup Genc
**Links:** [abs](https://arxiv.org/abs/2610.26096) - [pdf](https://arxiv.org/pdf/2610.26096)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, mapping, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PnP-Transformer: A Neural Pose Solver for 6D Object Pose Estimation
- 作者：Emirkan Burak Yilmaz, Yakup Genc
- 出版日期：2026-10-19T09:57:44Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；无次分类
- 链接：[摘要](https://arxiv.org/abs/2610.26096) / [PDF](https://arxiv.org/pdf/2610.26096)

### 一句话总结
论文提出 PnP-Transformer，一种无需迭代、可微的神经位姿求解器，用来替代经典 PnP-RANSAC，并在零样本 6D 物体位姿估计流程中评估其精度与延迟表现。

### 研究问题
论文关注 6D 物体位姿估计中的位姿求解环节：如何以无需迭代、可微的方式，从预测的半稠密 2D-3D 对应场及置信度分数中回归 6D 物体位姿，作为经典 PnP-RANSAC 的替代方案，并考察其在实际零样本流程中的精度和延迟权衡。

### 核心思路/方法
- 设计 PnP-Transformer 作为神经位姿求解器，输入为预测的半稠密 2D-3D 对应场及置信度分数。
- 将几何输入映射到连续潜空间，并直接回归 6D 物体位姿。
- 定位为无需迭代、可微的经典 PnP-RANSAC 替代方案。
- 将其集成到零样本 6D 位姿估计流程中，对应模块与位姿求解器分开训练。
- 与 EPnP-RANSAC 替换实验对比，分析精度与延迟的权衡。

### 主要贡献
- 提出 PnP-Transformer 神经位姿求解器，作为经典 PnP-RANSAC 的无需迭代、可微替代方案。
- 在七个核心 BOP 基准数据集上取得 41.2% 平均 AR，延迟为 0.46 s/obj；摘要称其超过除 Co-op（58.4% AR）之外的所有先前基线，例如 RayPose（39.1% AR）。
- 通过零样本 6D 位姿估计流程的集成评估，展示了求解器的实际可用性。
- 通过替换为 EPnP-RANSAC 的对照，揭示了精度-延迟权衡：RANSAC 替代方案在七个数据集中的六个上更优，平均 AR 达 52.2%，但每物体额外增加 60 ms。
- 摘要提供代码与预训练模型链接。

### 局限性
- 摘要未提供足够信息说明方法在大规模场景、遮挡、对称物体或不同对应质量下的具体鲁棒性细节。
- 摘要未提供足够信息说明训练数据规模、网络结构细节、推理硬件条件及延迟测量环境。
- 摘要未提供足够信息解释 PnP-Transformer 与 EPnP-RANSAC 精度差距的具体原因。
- 摘要未提供足够信息说明在七个 BOP 数据集上的逐数据集完整结果与失败案例分析。

### 阅读优先级
中。理由：论文主题集中在 6D 位姿估计的位姿求解环节，涉及经典 PnP-RANSAC 的可微神经替代与精度-延迟权衡，对相关方向有参考价值；但摘要已明确显示其平均 AR 低于同流程下的 EPnP-RANSAC 替代方案，且摘要未提供足够信息判断其更广泛适用性，因此优先级定为中。

</details>

<details>
<summary>Abstract</summary>

We present PnP-Transformer, a neural pose solver designed as an iterative-free, differentiable alternative to classical PnP-RANSAC algorithms. PnP-Transformer regresses the 6D object pose by processing predicted semi-dense 2D-3D correspondence fields alongside confidence scores, while mapping geometric inputs into a continuous latent space. To evaluate its practical utility, we integrate PnP-Transformer into a zero-shot 6D pose estimation pipeline, where the correspondence module and pose solver are trained separately. PnP-Transformer achieves a 41.2% mean AR score with low latency (0.46 s/obj) on seven core BOP benchmark datasets, surpassing all prior baselines (such as RayPose with 39.1% AR) but one (Co-op with 58.4% AR). When the pose solver is replaced with EPnP-RANSAC (similar to Co-op) while keeping the correspondence module unchanged, the RANSAC alternative outperforms PnP-Transformer on six of the seven datasets by reaching 52.2% mean AR at a cost of an additional 60 ms per object, revealing an accuracy-latency trade-off. Code and pretrained models are available at https://github.com/ebylmz/pnp-transformer.

</details>

#### 2026-10-19 - OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects

**Authors:** Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
**Links:** [abs](https://arxiv.org/abs/2610.25840) - [pdf](https://arxiv.org/pdf/2610.25840)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, pose estimation, manipulation, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OV-PEAR: Observation-Verified Pose-Scale Estimation and Reconstruction for Unknown Industrial Manipulation Objects
- 作者：Guoqin Tang, Qingxuan Jia, Yichen Tan, Zihang Lv, Ruiquan Wang, Zeyuan Huang, Gang Chen
- 出版日期：2026-10-19T05:51:41Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要页](https://arxiv.org/abs/2610.25840)｜[PDF](https://arxiv.org/pdf/2610.25840)

### 一句话总结
OV-PEAR 面向未知工业操作物体，提出一个经观测验证的三阶段框架，同时完成物体级 3D 重建和位姿-尺度估计，以摆脱对 CAD 模型、物体专用训练数据或稳定工作单元的依赖。

### 研究问题
精细工业机器人操作需要 6D 位姿、尺度以及可直接用于操作的 3D 模型。摘要指出，现有工业位姿估计依赖 CAD 模型、物体专用训练数据或稳定工作单元，因此难以用于未见物体；零样本方法则受单视角遮挡、生成偏差和尺度不确定性影响。论文要解决的问题是：对未知工业物体，如何在不依赖上述先验或假设的情况下，获得可用的 3D 模型以及位姿和尺度估计。

### 核心思路/方法
论文提出 OV-PEAR，一个以物体为中心、包含三个阶段并经观测验证的流水线：

1. 分割 RGB-D 实例，并生成物体级 3D 假设；
2. 通过外观感知的视角检索、显式尺度搜索和可见性敏感配准，将假设锚定到机器人坐标系；
3. 将多视角 RGB-D 证据反投影到物体规范坐标系，验证体素占用、抑制幻觉，并生成可复用的可信物体模型。

摘要还提到，模型库和位姿-尺度日志支持短期的物体级状态维护。

### 主要贡献
- 提出 OV-PEAR 框架，用于未知工业物体的 3D 重建与位姿-尺度估计，并以观测验证作为核心机制。
- 设计三阶段物体中心流水线，涵盖实例分割与 3D 假设生成、机器人坐标系锚定、多视角体素占用验证与可信模型生成。
- 在 BOP-Industrial 上报告平均 AR 为 0.657，并在真实场景中改善位姿与体素级几何一致性。
- 在真实机器人连接器装配任务中报告 99.67% 抓取成功率和 84.00% 装配成功率。
- 模型库与位姿-尺度日志支持短期的物体级状态维护，报告速度为 0.02 ms/frame。

### 局限性
- 摘要未提供足够信息说明方法对极端遮挡、严重传感器噪声或高度透明/反光工业物体的具体表现。
- 摘要未提供足够信息说明三阶段各模块的消融实验、失败案例和计算资源需求。
- 摘要未提供足够信息说明 BOP-Industrial 上的评测协议细节、对比方法完整列表，以及真实场景实验规模。
- 摘要未提供足够信息说明“短期物体级状态维护”的时间范围、适用边界与长期稳定性。
- 摘要未提供足够信息说明方法对机器人坐标系标定误差、视角检索失败或尺度搜索失败的鲁棒性。

### 阅读优先级
中。理由：该论文与未知物体 6D 位姿、尺度估计、机器人操作和 3D 重建直接相关，且摘要给出了量化结果和真实机器人验证；但摘要未展开方法细节、消融与失败分析。若关注零样本工业物体位姿估计、观测验证式重建或机器人装配，优先级可提高至高；若仅关心通用 6D 位姿跟踪或大规模场景重建，则优先级为中等。

</details>

<details>
<summary>Abstract</summary>

Fine industrial robotic manipulation requires 6D pose, scale, and an operation-ready 3D model. Existing industrial pose estimation relies on CAD models, object-specific training data, or stable workcells, limiting use with unseen objects; zero-shot methods suffer from single-view occlusion, generative bias, and scale uncertainty. We present OV-PEAR, an observation-verified framework for 3D reconstruction and pose-scale estimation of unknown industrial objects. Its three-stage object-centric pipeline: (1) segments RGB-D instances and generates object-level 3D hypotheses; (2) anchors them to the robot frame via appearance-aware view retrieval, explicit scale search, and visibility-sensitive registration; (3) back-projects multi-view RGB-D evidence into the object-canonical frame to verify voxel occupancy, suppress hallucinations, and produce reusable trusted object models. On BOP-Industrial, OV-PEAR achieves 0.657 average AR and improves pose and voxel-level geometric consistency in real scenes; real-robot connector assembly reaches 99.67% grasp and 84.00% assembly success. The model library and pose-scale log enable short-term object-level state maintenance at 0.02 ms/frame.

</details>

#### 2026-10-19 - Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions

**Authors:** Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
**Links:** [abs](https://arxiv.org/abs/2610.25622) - [pdf](https://arxiv.org/pdf/2610.25622)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Recurrent Vision Transformers for Event-Based Spacecraft Pose Estimation Under Slow Relative Motions
- 作者：Sofia McLeod, Mohsi Jawaid, Carl Seubert, Tat-Jun Chin
- 出版日期：2026-10-19T00:52:34Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；二级分类：摘要未提供足够信息
- 链接：摘要页 https://arxiv.org/abs/2610.25622 ；PDF https://arxiv.org/pdf/2610.25622

### 一句话总结
论文提出用循环视觉 Transformer（RVT）处理慢速相对运动下事件相机航天器位姿估计中事件率低、信噪比差的问题，并在真实慢速运动事件数据上验证了位姿估计精度与稳定性优于逐事件帧或固定时间窗方法。

### 研究问题
基于视觉的航天器位姿估计对交会与近距离操作（RPO）很重要，事件相机因高动态范围在轨道强光照条件下具有鲁棒性。但基于事件的航天器位姿估计（EBSPE）在追踪器与目标相对运动很慢时表现变差：事件率显著下降，数据信噪比低；而真实 RPO 轨迹出于安全常包含慢速相对运动，例如低至 1 mm/s；低照度还会加剧该问题。因此，如何处理慢速相对运动是提升 EBSPE 实用性的关键。

### 核心思路/方法
论文提出将循环视觉 Transformer（RVT）用于 EBSPE。核心思想是利用循环记忆在稀疏事件流中捕捉更长时程信息，并从完整轨迹中学习时间注意力跨度，而不是固定时间窗口。作者开发了一个基于 RVT 的热图回归器，用于产生位姿估计所需的 2D-3D 对应关系，并在代表 RPO 轨迹的慢速相对运动条件下采集的真实事件数据上进行验证。

### 主要贡献
- 针对慢速相对运动导致事件率低、信噪比差的问题，提出使用 RVT 进行基于事件的航天器位姿估计。
- 利用循环记忆捕捉稀疏事件流中的长期信息，并学习时间注意力跨度而非固定时间窗。
- 构建基于 RVT 的热图回归器以生成 2D-3D 对应关系用于位姿估计。
- 在慢速相对运动的真实事件数据上验证，结果显示相较此前逐事件帧或固定时间窗的 EBSPE 方法，位姿估计精度和稳定性更优。

### 局限性
摘要未提供足够信息。仅能看出验证基于真实事件数据，但具体数据集规模、轨迹范围、光照条件覆盖、计算开销、实时性、失败案例等均未在摘要中说明；也未给出定量指标数值和与基线方法的详细对比设置。

### 阅读优先级
高。理由：该论文直接针对 EBSPE 在真实 RPO 慢速运动场景下的关键失效模式，问题定义明确且具有实际应用背景；方法上引入 RVT 的循环记忆与可学习时间注意力跨度，针对稀疏事件流的时程建模；摘要声称在真实慢速运动事件数据上优于逐事件帧和固定时间窗方法。若关注事件相机位姿估计、航天器 RPO 或稀疏事件流时序建模，该论文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Vision-based object pose estimation is vital for conducting spacecraft rendezvous and proximity operations (RPO). Recent research has demonstrated the robustness of event cameras against the harsh lighting conditions that often occur in orbit, thanks to the extremely high dynamic range of event sensors. However, event-based spacecraft pose estimation (EBSPE) suffers when the relative motion between the chaser and target is slow, since the event rate drops significantly, leading to data with low signal-to-noise ratio. Unfortunately, for safety reasons, real RPO trajectories often involve slow relative motions (e.g., down to 1 mm/s), and operating under low illumination exacerbates the problem. Addressing slow relative motions is thus crucial to raise the practicality of EBSPE. To this end, we propose using recurrent vision transformers (RVT) for EBSPE. The key idea is to exploit recurrent memory to capture longer-term information across sparse event streams, and to learn the temporal attention span from full trajectories rather than fixing the time window. We developed an RVT-based heatmap regressor to produce 2D-3D correspondences for pose estimation, which was validated on real event data collected under slow relative motions representative of RPO trajectories. Results indicate the superior pose estimation accuracy and stability of our RVT-based method, relative to previous per-event-frame-based or fixed-time-window EBSPE methods.

</details>

#### 2026-10-15 - Gen4P: Video Generators are 4D Perceivers

**Authors:** Yitong Xia, Zeren Jiang, Chuanxia Zheng
**Links:** [abs](https://arxiv.org/abs/2610.22371) - [pdf](https://arxiv.org/pdf/2610.22371)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** camera pose estimation, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Gen4P: Video Generators are 4D Perceivers
- 作者：Yitong Xia, Zeren Jiang, Chuanxia Zheng
- 出版日期：2026-10-15T17:59:48Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.22371

### 一句话总结
Gen4P 提出将预训练视频生成器改造为无需迭代去噪的前馈式 4D 感知器，从单目视频中统一恢复 4D 几何与运动。

### 研究问题
如何从单目视频中恢复 4D 几何与运动，并利用预训练视频生成器的能力实现统一、前馈式的 4D 感知，而非依赖迭代去噪过程。

### 核心思路/方法
- 将预训练视频生成器重新利用为前馈式 4D 感知器，无需迭代去噪。
- 基于按需查询（on-demand querying），Gen4P 在单次编码器前向中处理干净的视频 latent，并通过轻量级 cross-attention 解码器预测所请求的 4D 属性。
- 按需查询形式支持灵活的空间采样；提出的连续时间查询进一步提供时间灵活性。
- 为增强几何知识，提出一种简单的插件式方案：将预训练的视频-深度 LoRA 作为冻结的几何先验引入，在不增加额外可训练参数的情况下提升整体性能。

### 主要贡献
- 提出 Gen4P，一个从单目视频恢复 4D 几何与运动的统一框架。
- 展示预训练视频生成器可被改造为前馈式 4D 感知器，且无需迭代去噪。
- 通过按需查询与连续时间查询，分别实现灵活的空间采样与时间灵活性。
- 提出将预训练视频-深度 LoRA 作为冻结几何先验的插件式方案，在不增加可训练参数的情况下提升性能。
- 在 3D 点跟踪、视频深度和相机位姿估计任务上取得 state-of-the-art 或具竞争力的性能；在野外视频上的定性结果展示其跟踪复杂运动并保持精细结构的能力。

### 局限性
摘要未提供足够信息。

### 阅读优先级
中。理由：该工作将视频生成预训练与统一 4D 感知结合，涉及 3D 点跟踪、视频深度和相机位姿估计等多任务，并声称达到 state-of-the-art 或具竞争力性能，对 3D 重建与多视图几何方向有参考价值；但摘要未给出具体实验细节、量化结果与失败情形，需进一步阅读原文确认适用范围与局限。

</details>

<details>
<summary>Abstract</summary>

We introduce Gen4P, a unified framework for recovering 4D geometry and motion from monocular video. We show that a pretrained video generator can be repurposed into a feed-forward 4D perceiver without iterative denoising. Building on on-demand querying, Gen4P processes clean video latents in a single encoder pass and predicts the requested 4D attributes through a lightweight cross-attention decoder. The on-demand query formulation enables flexible spatial sampling, and our proposed continuous-time queries further provide temporal flexibility. To strengthen geometric knowledge, we propose a straightforward plug-in solution by incorporating a pretrained video-depth LoRA as a frozen geometry prior, improving overall performance without adding extra trainable parameters. Gen4P achieves state-of-the-art or competitive performance on tasks of 3D point tracking, video depth and camera pose estimation. Qualitative results on in-the-wild videos illustrate its capability of tracking complex motion while maintaining the delicate structure. Together, these results demonstrate the potential of video generative pretraining for unified 4D perception. See https://gen4p.github.io for more visual results.

</details>

#### 2026-10-15 - GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama

**Authors:** Jing OU, Zidong Cao, Liaoyuan Fan, Zhuoxiao Li, Shuai Zhang, Yinrui Ren, Dongli Wu, Haoang Li, Hui Xiong, Wufan Zhao
**Links:** [abs](https://arxiv.org/abs/2610.21297) - [pdf](https://arxiv.org/pdf/2610.21297)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** 3D reconstruction, robotics, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoPano: Towards Geometrically Accurate 3D Reconstruction from a Single Panorama
- 作者：Jing OU, Zidong Cao, Liaoyuan Fan, Zhuoxiao Li, Shuai Zhang, Yinrui Ren, Dongli Wu, Haoang Li, Hui Xiong, Wufan Zhao
- 出版日期：2026-10-15T05:42:59Z
- 分类：主分类为 3D Reconstruction & Multi-view Geometry；次分类为 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.21297) / [PDF](https://arxiv.org/pdf/2610.21297)

### 一句话总结
GeoPano 是一个面向单张全景图的馈送式（feed-forward）3D 重建框架，通过全景感知注意力聚合与混合监督策略，从单张全景图中恢复几何准确且一致的点云。

### 研究问题
从全景图（ERP 图像）直接估计几何会受到球面畸变的固有限制。常见做法是将全景图分解为无畸变的透视视图，但独立处理这些视图往往引入跨视图的几何不一致。论文旨在解决单张全景图三维重建中的球面投影畸变与跨视图几何一致性问题。

### 核心思路/方法
论文提出 GeoPano，一个单视图全景 3D 重建的馈送式框架，从单张全景图恢复几何准确且一致的点云。其方法由两项关键创新驱动：
1. **全景感知注意力聚合器**：采用精简的注意力架构，配备新颖的 Pano-Attention 机制，显式利用全景图内在的球面几何来引导跨视图交互，从而抑制几何不一致。
2. **混合监督策略**：联合在透视空间中约束细粒度局部细节，并在球面空间中约束全局结构一致性。

### 主要贡献
- 提出 GeoPano，一个用于单视图全景 3D 重建的馈送式框架，可从单张全景图恢复几何准确且一致的点云。
- 提出全景感知注意力聚合器，包含 Pano-Attention 机制，显式利用全景球面几何引导跨视图交互，以抑制几何不一致。
- 提出混合监督策略，在透视空间与球面空间中联合约束局部细节与全局结构一致性。
- 摘要称实验表明该方法在重建精度、几何一致性和视觉保真度上显著优于此前的 SOTA 方法。

### 局限性
摘要未提供足够信息。摘要未给出具体实验设置、数据集、评价指标数值、失败案例或方法适用边界等细节，因此无法基于摘要判断其局限性。

### 阅读优先级
高。理由：该论文聚焦单张全景图 3D 重建中的球面畸变与跨视图一致性这两个核心难点，提出明确的注意力机制与混合监督设计，且摘要声称在重建精度、几何一致性和视觉保真度上显著优于此前 SOTA；对 3D 重建、多视图几何以及机器人 / AR/VR 应用方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Panoramic 3D reconstruction enables the holistic recovery of complete 360 $^\circ$ scene geometry, offering significant benefits for robotics and AR/VR applications. However, directly estimating geometry from ERP images is inherently challenged by spherical distortions. To reduce spherical projection distortions, a common strategy is to decompose panoramas into distortion-free perspective views, but independently processing these views often introduces cross-view geometric inconsistencies. To address these challenges, we introduce GeoPano, a feed-forward framework for single-view panoramic 3D reconstruction that recovers a geometrically accurate and consistent point cloud from a single panorama. Our approach is driven by two key innovations: First, we propose a panoramic-aware attention aggregator, featuring a streamlined attention architecture equipped with a novel Pano-Attention mechanism, which explicitly exploits the intrinsic spherical geometry of the panorama to guide cross-view interactions, thereby suppressing geometric inconsistencies. Furthermore, we formulate a hybrid supervision strategy to jointly enforce fine-grained local details in perspective space and global structural coherence in spherical space. Experiments demonstrate that our method significantly outperforms previous SOTA approaches in reconstruction accuracy, geometric consistency, and visual fidelity.

</details>

#### 2026-10-15 - LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation

**Authors:** Shiqi Che, Yijie Liu, Shuo Wang, Wenxin Liu
**Links:** [abs](https://arxiv.org/abs/2610.21199) - [pdf](https://arxiv.org/pdf/2610.21199)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LIN-SLAM: Lightweight LiDAR--Inertial Neural SLAM for Real-Time Onboard Navigation
- 作者：Shiqi Che, Yijie Liu, Shuo Wang, Wenxin Liu
- 出版日期：2026-10-15T03:58:47Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：[摘要](https://arxiv.org/abs/2610.21199) / [PDF](https://arxiv.org/pdf/2610.21199)

### 一句话总结
LIN-SLAM 将高频几何 LiDAR--惯性估计与神经隐式跟踪、持续建图和全局优化相耦合，在保持实时性的同时提升定位精度。

### 研究问题
论文指出，几何 LiDAR--惯性 SLAM 虽然状态估计高效，但缺乏神经隐式 SLAM 所具备的连续地图表示和全局优化能力；而神经隐式方法通常计算开销较大，难以兼顾实时机载运行。

### 核心思路/方法
提出一种混合方法 LIN-SLAM：将高频几何 LiDAR--惯性估计与神经隐式跟踪、持续建图以及全局优化耦合，用于准确且实时的机载 SLAM。

### 主要贡献
- 在三个数据集、覆盖 32、64、128 通道 LiDAR 配置的十二个代表性序列上，LIN-SLAM 在所评估的几何与神经隐式最先进方法中取得最低总体平均绝对轨迹误差（ATE），同时相较现有神经隐式 SLAM 方法显著降低运行时间。
- 在搭载 NVIDIA Jetson Orin NX 和 16 通道 LiDAR 的 Unitree Go2 上，LIN-SLAM 在 1.47 km 室内轨迹、具有挑战性的重复走廊环境中持续进行实时定位和神经建图，端点闭合误差仅为 0.141 m。
- 据作者所述，LIN-SLAM 是首个在移动机器人平台上实现实时在线运行、并保持最先进定位精度的神经隐式后端 LiDAR--惯性 SLAM 系统。
- 代码将在接收后发布。

### 局限性
摘要未提供足够信息。摘要未给出失败场景、传感器退化条件、不同平台泛化能力、长期运行稳定性或计算资源下限等方面的具体限制。

### 阅读优先级
高。理由：该论文提出轻量级 LiDAR--惯性神经 SLAM，直接面向实时机载导航；摘要报告了多数据集、多种 LiDAR 通道配置下的精度与运行时间对比，以及真实机器人平台上的长轨迹实时运行结果，并声称是首个实现实时在线运行的神经隐式后端 LiDAR--惯性 SLAM 系统，具有较强的问题针对性和工程应用价值。

</details>

<details>
<summary>Abstract</summary>

Geometric light detection and ranging (LiDAR)--inertial simultaneous localization and mapping (SLAM) provides efficient state estimation but lacks the continuous map representation and global refinement capabilities of neural implicit SLAM, while neural implicit methods remain computationally expensive. We propose Lightweight LiDAR--Inertial Neural SLAM (LIN-SLAM), a hybrid method that couples high-rate geometric LiDAR--inertial estimation with neural implicit tracking, continual mapping, and global refinement for accurate real-time onboard SLAM. Experiments on twelve representative sequences from three datasets spanning 32-, 64-, and 128-channel LiDAR configurations show that LIN-SLAM achieves the lowest overall mean absolute trajectory error (ATE) among the evaluated state-of-the-art geometric and neural implicit methods, while substantially reducing runtime compared with existing neural implicit SLAM methods. On a Unitree Go2 equipped with an NVIDIA Jetson Orin NX and a 16-channel LiDAR, LIN-SLAM sustains real-time localization and neural mapping over a 1.47-km indoor trajectory through challenging repetitive corridor environments, with an endpoint closure error of only 0.141~m. To the best of our knowledge, LIN-SLAM is the first LiDAR--inertial SLAM system with a neural implicit backend to achieve real-time online operation on a mobile robotic platform while maintaining state-of-the-art localization accuracy. The code will be released upon acceptance.

</details>

#### 2026-10-15 - RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching

**Authors:** Liangjing Shao, Wanhao Liu, Zhiwei Fang, Rulin Zhou, Quanlu Zhang, Changjing Liu, Beilei Cui, Yiming Huang, Hongliang Ren
**Links:** [abs](https://arxiv.org/abs/2610.21086) - [pdf](https://arxiv.org/pdf/2610.21086)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, rendering, robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoPE-Flow: Monocular Vision-based Robot Pose Estimation via 2D Graph-Conditioned 3D Flow Matching
- 作者：Liangjing Shao, Wanhao Liu, Zhiwei Fang, Rulin Zhou, Quanlu Zhang, Changjing Liu, Beilei Cui, Yiming Huang, Hongliang Ren
- 出版日期：2026-10-15T01:40:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.21086，https://arxiv.org/pdf/2610.21086

### 一句话总结
RoPE-Flow 提出一种基于流匹配的端到端单目相机到机器人位姿估计框架，利用 2D 关键点热图构造图条件并生成 3D 位姿，同时通过拓扑与尺度相关损失提升不同机器人上的位姿估计表现。

### 研究问题
从单目图像估计相机到机器人的位姿对基于视觉的机器人导航与控制具有重要意义，但从 2D 观测恢复 3D 结构特征仍然困难。现有方法要么依赖耗时的迭代渲染，要么涉及复杂的 2D-3D 配准，并面临投影歧义、远端关节误差累积以及不同关节学习不均衡等问题。

### 核心思路/方法
论文提出 RoPE-Flow，一个端到端的、基于流匹配的相机到机器人位姿估计框架。方法从预测的 2D 热图出发，使用 Keypoint-centered Feature Extractor 从关键点为中心的多尺度图像块中获取位置特征与上下文表示；引入 Graph-guided Condition Generator，通过可学习邻接图，基于关键点之间的相关性为流匹配生成条件；并引入 Bone Length Loss 与 Ray-Depth Loss，用于拓扑一致性和尺度稳定性，同时采用逐关节加权以缓解不同关节预测难度不一致的问题。

### 主要贡献
- 提出 RoPE-Flow，一个端到端的基于流匹配的相机到机器人位姿估计框架。
- 设计 Keypoint-centered Feature Extractor，从预测的 2D 热图中提取关键点为中心的多尺度位置特征与上下文表示。
- 引入 Graph-guided Condition Generator，使用可学习邻接图，根据关键点相关性为流匹配生成条件。
- 引入 Bone Length Loss 和 Ray-Depth Loss，以增强拓扑一致性与尺度稳定性，并通过逐关节加权处理不同关节预测难度差异。
- 摘要称该方法在多类机器人和多相机设置下优于现有位姿估计方法，并建立了新的跨场景基准，展示零样本跨场景机器人位姿估计性能。

### 局限性
摘要未提供足够信息。摘要未提供足够信息说明方法的具体失败场景、计算开销、对特定机器人结构或相机设置的依赖程度，也未给出定量实验结果、数据集细节和与基线方法的完整比较。

### 阅读优先级
高。理由：该论文面向单目机器人位姿估计这一重要问题，提出流匹配与图条件结合的端到端框架，并声称在多类机器人、多相机以及零样本跨场景设定下取得优于现有方法的表现；若关注单目 3D 位姿估计、机器人视觉或流匹配应用，该论文具有较高相关性。

</details>

<details>
<summary>Abstract</summary>

Camera-to-robot pose estimation from a monocular image is significant for vision-based robot navigation and control. However, recovering 3D structural features from 2D observations remains a challenging task. Existing camera-to-robot pose estimation methods either rely on time-consuming iterative rendering or involve sophisticated 2D-3D registration which suffers from projection ambiguity, accumulated errors for distal joints and imbalanced learning for different joints. In this work, we propose RoPE-Flow, an end-to-end flow matching-based framework for camera-to-robot pose estimation. From the predicted 2D heatmaps, we propose a Keypoint-centered Feature Extractor to obtain positional features along with contextual representations from keypoints-centered multi-scale patches. Moreover, we introduce Graph-guided Condition Generator, which embeds a learnable adjacency map to generate condition for flow matching based on correlation among keypoints. Besides, we introduce Bone Length Loss and Ray-Depth Loss for topological consistency and scale stability, with joint-wise weighting to mitigate varied prediction difficulty across joints. The proposed method outperforms state-of-the-art methods for pose estimation across different types of robots with mutiple cameras. Besides, we establish a novel cross-scene benchmark to demonstrate the outstanding performance of RoPE-Flow on zero-shot cross-scene robot pose estimation. Meanwhile, animated visualizations are shown on the website: ropeflow.netlify.app

</details>

#### 2026-10-14 - Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments

**Authors:** Dara Molloy, Terry Wu, Wonju Lee, Abhilash Nand Kumar, David Adley, Conor Ferguson, Hesam Rabeti
**Links:** [abs](https://arxiv.org/abs/2610.20958) - [pdf](https://arxiv.org/pdf/2610.20958)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM, bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Line-Augmented cuVSLAM: Robust Visual Odometry in Low-Texture Environments
- 作者：Dara Molloy, Terry Wu, Wonju Lee, Abhilash Nand Kumar, David Adley, Conor Ferguson, Hesam Rabeti
- 出版日期：2026-10-14T21:29:40Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2610.20958 ；https://arxiv.org/pdf/2610.20958

### 一句话总结
该论文在 CUDA 加速的视觉 SLAM 系统 cuVSLAM 中引入线特征扩展，以提升仓库、生产设施等低纹理环境下的视觉里程计鲁棒性。

### 研究问题
仓库和生产设施中的自主移动机器人常处于缺乏点特征的环境，例如无特征通道、均匀墙面、重复货架和镜面地板，这些环境会使基于点特征的视觉里程计失效。论文关注的核心问题是：在点特征稀缺的低纹理环境下，如何利用环境中丰富的直线边缘结构来提升视觉里程计的鲁棒性与精度。

### 核心思路/方法
论文提出对 cuVSLAM 的线特征扩展，以恢复低纹理环境中直线边缘所提供的信号。方法要点包括：
- 线段使用 Plücker 坐标进行几何传输，并使用 Bartoli 和 Sturm 的最小 4-DOF 正交表示进行优化。
- 将 Cauchy 鲁棒的点到线残差及其解析雅可比直接融入 cuVSLAM 的逐帧 Gauss-Newton 位姿求解。
- 在 Schur 补滑动窗口 bundle adjustment 中联合优化相同的线状态。
- 使用自适应信息权重，使线特征在点特征变得稀缺时承担更多估计任务。
- 该扩展通过向现有求解器添加残差块实现，而不是引入第二个估计器；关闭时完全退化为未修改的点特征管线。

### 主要贡献
- 提出一种面向 cuVSLAM 的线特征扩展，用于低纹理环境下的鲁棒视觉里程计。
- 将 Plücker 坐标、Bartoli-Sturm 最小 4-DOF 表示、Cauchy 鲁棒点到线残差及解析雅可比集成到 cuVSLAM 的位姿求解与滑动窗口 bundle adjustment 中。
- 设计自适应信息权重，使线特征在点特征稀缺时承担更多估计负担。
- 在 RGB-D 模式下，使用 SE(3) Umeyama 对齐且无尺度校正进行评估，线特征在 TUM RGB-D Freiburg3 的 22 个序列上将平均绝对轨迹误差降低 38.5%，在 8 个 Replica 房间和办公室序列上降低 30.1%；其中中位平移误差降低 38.9%，中位旋转误差降低 66.4%，所有测试配置中零跟踪失败。
- 该扩展以添加残差块的方式实现，不引入第二估计器，关闭时完全退化为原始点特征管线。

### 局限性
摘要未提供足够信息。摘要未说明方法的计算开销、实时性能、内存占用、不同硬件平台上的表现、失败案例、参数敏感性、与其它线特征 SLAM 方法的对比细节，也未说明在非 RGB-D 模式或真实室外环境中的泛化能力。

### 阅读优先级
高。理由：该论文针对低纹理环境下点特征视觉里程计失效这一明确且实际的问题，提出了与 CUDA 加速 cuVSLAM 集成的线特征扩展，并给出了在 TUM RGB-D 与 Replica 数据集上的量化提升和零跟踪失败结果；对于关注视觉 SLAM、视觉里程计、低纹理鲁棒性和机器人导航的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Autonomous mobile robots in warehouses and production facilities operate in precisely the environments that defeat point-feature visual odometry: featureless aisles, uniform walls, repetitive racking and specular floors. Such environments are, however, rich in straight-edge structure: rack uprights, door frames, wall junctions and cabinet outlines present high-contrast linear edges stable across wide viewpoint changes. A line-feature extension to cuVSLAM, a CUDA-accelerated visual-SLAM system, is presented that recovers this signal. Lines are parameterised as Plücker coordinates for geometric transport and as the minimal 4-DOF orthonormal representation of Bartoli and Sturm for optimisation; a Cauchy-robust point-to-line residual with analytic Jacobians is folded directly into cuVSLAM's per-frame Gauss-Newton pose solve, and the same line state is jointly refined in the Schur-complement sliding-window bundle adjustment. An adaptive information weight causes lines to assume more of the estimation burden exactly as point features become scarce, and the extension adds residual blocks to existing solvers rather than introducing a second estimator, reducing exactly to the unmodified point pipeline when disabled. Evaluated in RGB-D mode under SE(3) Umeyama alignment with no scale correction, line features reduce mean absolute trajectory error by 38.5% over the 22 sequences of the TUM RGB-D Freiburg3 collection and by 30.1% over the 8 Replica room and office sequences, where median translation error falls by 38.9% and median rotation error by 66.4%, with zero tracking failures in any configuration tested.

</details>

## Neural Scene Representations & Rendering

### 2026-10

#### 2026-10-20 - KoalaGS: Complexity-Aware Continuous Level of Detail for Gaussian Splatting

**Authors:** Radu Beche, Raoul de Charette
**Links:** [abs](https://arxiv.org/abs/2610.28615) - [pdf](https://arxiv.org/pdf/2610.28615)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Deploying a trained 3D Gaussian Splatting scene under shrinking compute budgets requires one primitive set to remain effective when rendered at smaller prefixes. In this continuous level of detail (LoD) setting, the challenge is to decide which Gaussians should retain capacity as the budget decreases. A pilot study on 3DGS-MCMC reconstructions shows that image complexity, computed from the input views before optimization, predicts where reconstruction error concentrates in image and 3D space. It also reveals that simple regions contain too many Gaussians and degrade as much as complex ones at lower budgets, despite being inherently cheaper to represent. Subsequently, in KoalaGS, during training we use this complexity prior to bias relocation toward poorly reconstructed areas while ensuring smooth degradation across LoDs. A primitive importance score then enables inference at low-capacity, while preserving the scene structure. Tested across three datasets, KoalaGS maintains competitive full-capacity quality while significantly improving quality across the budget spectrum, yielding smoother transitions across LoDs, and enabling faster progressive streaming.

</details>

#### 2026-10-20 - Learning from Automatic 3D Gaussian Splatting Edits for Online Bayesian Scene Change Detection

**Authors:** Changrui Zhu, Simon Julier
**Links:** [abs](https://arxiv.org/abs/2610.28490) - [pdf](https://arxiv.org/pdf/2610.28490)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>Abstract</summary>

Online scene change detection requires integrating incoming observations to determine which regions have changed relative to a reference scene. We update change beliefs as new images arrive using generalised Bayesian evidence fusion. However, the prior probability of change and evidence models are unknown beforehand, and numerical Bayesian inference can be costly. We address these challenges by learning offline from automatic edits to a reference 3D Gaussian Splatting (3DGS) model. These edits generate labelled training views without manual annotations. Together with unchanged reference observations, they provide supervision for learning scene-specific evidence models and estimating the effective pixel prior and response statistics. Online prediction combines current evidence with historical support, while closed-form local Bayes factors, parameterized by the learned response statistics, update an accumulated 3D Gaussian field. Object-guided refinement produces the final change masks. Our method achieves state-of-the-art accuracy on PASLCD and CCS3D, with $67.64\%$ and $75.82\%$ mIoU, respectively. On PASLCD, the complete pipeline runs at $17.2$\,FPS over complete query sequences, the fastest among the evaluated online methods.

</details>

#### 2026-10-20 - HRoPE: Homography Relative Positional Encoding

**Authors:** Huachen Gao, Yang Yang, Xiaoqian Liang, Xingyu Chen, Youjia Zhang, Qi Zhang, Baorui Ma, Anpei Chen, Wei Yang
**Links:** [abs](https://arxiv.org/abs/2610.28284) - [pdf](https://arxiv.org/pdf/2610.28284)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view stereo, novel view synthesis, view synthesis

<details>
<summary>Abstract</summary>

Geometric Relative Positional Encoding has become the primary mechanism for injecting spatial inductive biases into multi-view transformers. Existing designs condition attention on camera-level frustums or ray-marched depth, associating cross-view tokens through the sensor geometry. Such sensor-centric formulations, however, describe only where a token is observed from, leaving the rich surface geometry of the scene region depicted by the token. In this paper, we advocate a shift toward surface-aware positional encoding that explicitly grounds patch tokens in the geometry of physical surfaces. We introduce HRoPE, which represents the local geometry of each patch as a slanted 3D plane, following the slanted support-window assumption of classical multi-view stereo. We inject token-level, plane-induced homographies into attention as relative transformations. This equips the transformer with a geometric prior for rectifying perspective distortions and aligning patch features across viewpoints. Our encoding requires no ground-truth geometry: the plane parameters can be predicted end-to-end under a view-synthesis objective alone, or derived from foundation models. Extensive experiments on RealEstate10K, CO3Dv2, and DL3DV show that our best variant of HRoPE consistently outperforms the evaluated geometric positional encodings for novel view synthesis. Extensive ablations and analysis show the effectiveness of the proposed encoding. Please refer to our project page at: https://gaohchen.github.io/HRoPE

</details>

#### 2026-10-20 - OV-Foam: How 3D Representations Shape Semantic Feature Lifting

**Authors:** Yousef Rajeh, Alejandra Esparza Pelcastre, Ivan Viola, Dominik Engel
**Links:** [abs](https://arxiv.org/abs/2610.28131) - [pdf](https://arxiv.org/pdf/2610.28131)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>Abstract</summary>

Existing feature lifting approaches for open-vocabulary segmentation rely on simple backprojection to assign features to primitives. In the case of 3D Gaussian splatting reconstruction, the primitives overlap heavily, leading to suboptimal reconstructions, governed by many primitives per ray. Backprojection, however, reduces to a least-squares solvable problem, exactly when no two primitives share a ray. Motivated by this insight, we propose OV-Foam, which uses PowerFoam as the underlying representation. This representation uses a power-diagram to partition the scene, resulting in zero overlap between primitives and a substantial reduction in primitives per ray, which ultimately simplifies the lifting problem and allows for closer-to-optimal feature assignment. We show that the space partitioning primitives of OV-Foam reach near-optimal assignment, and our experiments demonstrate improved open-vocabulary segmentation over Gaussian baselines.

</details>

#### 2026-10-20 - Differentiable Task-Driven Coded Aperture Camera Design with 3D Gaussian Scene Representations

**Authors:** Chengyang Yan, Donald G. Dansereau
**Links:** [abs](https://arxiv.org/abs/2610.28004) - [pdf](https://arxiv.org/pdf/2610.28004)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** depth estimation, Gaussian Splatting, 3D Gaussian Splatting, splatting, simulation

<details>
<summary>Abstract</summary>

Camera design heavily influences perception task performance, yet cameras are typically designed by domain experts through costly experimentation, in isolation from the tasks they serve. Existing joint-design methods either rely on differentiable simulation limited to pre-captured 2D images, restricting them to optics or image-processing pipeline design, or use non-differentiable camera simulators optimised with derivative-free or reinforcement-learning methods that scale poorly with the number of design parameters. We present a differentiable framework for jointly designing complex camera systems and downstream perception tasks. We use it to design two coded-aperture depth-from-defocus cameras, a monocular and a stereo configuration, by jointly optimising the coded aperture mask, camera parameters, and a depth estimation network end-to-end. Our framework represents scenes with 3D Gaussian Splatting reconstructed from real-world captures, providing a differentiable image formation process for gradient-based optimisation over design spaces intractable for prior differentiable approaches. Results demonstrate that our differentiable method improves over existing coded aperture design and non-differentiable camera design baselines, offering a step forward in automated and principled camera design for autonomous systems.

</details>

#### 2026-10-20 - Geometry Regularization for Vanilla NeRF via Self-Supervised Cross-Ray Consistency

**Authors:** Zongji Wang
**Links:** [abs](https://arxiv.org/abs/2610.27776) - [pdf](https://arxiv.org/pdf/2610.27776)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, novel view synthesis, view synthesis, radiance

<details>
<summary>Abstract</summary>

Neural Radiance Fields (NeRF) achieve high-quality novel-view synthesis by representing a scene as a continuous volumetric radiance field. However, the geometry encoded by the density field of vanilla NeRF can be noisy and inaccurate, since different combinations of shape and radiance may explain the same input images. To reduce this ambiguity, we augment vanilla NeRF with a geometry-optimization branch based on self-supervised cross-ray consistency. Specifically, this branch samples candidate surface points from the density field, generates virtual rays that intersect at each point from different directions, and renders their appearance using the NeRF network. Based on the visibility-weighted color consistency across these rays, we constrain the implicit geometry. We further regularize the implicit geometry by penalizing opacity at candidates with inconsistent appearance predictions and encouraging local normal smoothness. These geometric constraints are derived from the NeRF predictions and require no ground-truth depth or surface-normal supervision. Experiments on eight Replica scenes show that the proposed method reduces the mean Chamfer distance by 30.8% compared with vanilla NeRF.

</details>

#### 2026-10-20 - World2HOSI: A Multi-Expert Harness for Long-Horizon Human-Object-Scene Interaction Generation

**Authors:** Jiushu Li, Haoran Wang, Yumeng Liu, Zhiyang Dou, Yuan Liu, Yuexin Ma, Cheng Lin
**Links:** [abs](https://arxiv.org/abs/2610.27725) - [pdf](https://arxiv.org/pdf/2610.27725)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, embodied AI, manipulation, simulation

<details>
<summary>Abstract</summary>

Long-horizon human-object-scene interaction (HOSI) is central to embodied AI, animation, and game development. Existing human-object interaction (HOI) and human-scene interaction (HSI) models excel in their respective domains, but none alone covers tasks requiring multiple interaction skills. Training unified HOSI models is hindered by scarce and costly data. We introduce World2HOSI, a multi-expert orchestration harness that generates continuous HOSI data from 3D Gaussian Splatting (3DGS) scenes and natural language instructions. Our key insight is that long-horizon HOSI hinges not on a stronger single model but on orchestration. Given a shared, structured scene state and an orchestration harness grounded in it, existing experts can jointly accomplish tasks beyond the reach of any of them alone. World2HOSI realizes this insight as a closed loop around a persistent scene state built from decoupled background and object assets. A harness plans action stages over this state, invokes experts via their native conditioning interfaces, and writes each action's effects back, so that every invocation is grounded in the evolving world. To reduce physical artifacts, bounded residual optimization and contact-driven physics simulation further ensure the physical plausibility of human motion and object manipulation, respectively, while preserving interaction intent. Experiments and a perceptual user study show that World2HOSI achieves the best task completion and interaction quality on the evaluated HOSI tasks, while generating more diverse data.

</details>

#### 2026-10-20 - RLSplat: Resource-Linear Budget Control for Feed-forward 3D Gaussian Splatting

**Authors:** Injae Kim, Minseok Joo, Jihwan Park, Sehyung Kim, Minseong Bae, Hyunwoo J. Kim
**Links:** [abs](https://arxiv.org/abs/2610.27712) - [pdf](https://arxiv.org/pdf/2610.27712)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (FF3DGS) reconstructs 3D scenes from images in a single forward pass, making it well-suited to applications that must operate within limited resource budgets. To further improve its practicality, recent budget-controllable FF3DGS methods allow the number of Gaussians to be adjusted at inference, so that the output meets a given storage limit or rendering-latency constraint. However, these methods overlook the cost of inference itself: to produce a representation with the target number of Gaussians, they first predict a dense set of Gaussians and then prune or select from it, requiring nearly constant latency and peak memory regardless of the budget. We therefore propose RLSplat, a resource-linear budget-controllable FF3DGS framework whose representation size, inference latency, and peak memory all decrease linearly as the Gaussian budget is reduced. Instead of pruning or selection, RLSplat learns a Gaussian allocation policy that distributes the budget across local scene regions, so that exactly the requested number of Gaussians is generated. These Gaussians are then refined through resource-linear Gaussian decoding, in which each Gaussian attends only to nearby Gaussians found via an efficient hierarchical neighbor search, so that the decoding cost decreases linearly with fewer Gaussians. In zero-shot evaluation, RLSplat outperforms prior budget-controllable methods at every budget, surpassing the strongest baseline even with 4$\times$ fewer Gaussians, while running up to 4.1$\times$ faster with 9.6$\times$ less peak memory at low budgets.

</details>

#### 2026-10-20 - PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting

**Authors:** Jinghan Gao, Siyu Wang, Dongyu Feng, Yiyuan Pan, Rong Xiong
**Links:** [abs](https://arxiv.org/abs/2610.27696) - [pdf](https://arxiv.org/pdf/2610.27696)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3DGS, scene representation, splatting, scene understanding

<details>
<summary>Abstract</summary>

3D scene graphs support language-guided navigation by organizing physical entities and their containment and spatial relations into hierarchical maps. Building such structured maps requires a scene representation that consistently distinguishes semantic regions and object instances across viewpoints. To this end, we present PanoGraphGS, a unified framework that integrates panoptic 3D Gaussian representation learning with hierarchical 3D scene graph construction. The framework learns semantic and instance features on shared Gaussian geometry. Prototype-based semantic learning and association-based instance learning produce consistent panoptic predictions across viewpoints. The learned representation supports novel-view panoptic segmentation and direct Gaussian-level panoptic decoding. A semantic-aware scene graph module further recovers a floor-room-stuff-object hierarchy with containment and spatial relations. We further release NaviGS, a real-world dataset for panoramic scene understanding. The dataset provides 3DGS, mesh, RGB, semantic, and depth data. For 3D scene graph identification, PanoGraphGS outperforms the strongest evaluated baseline in object-node accuracy by more than 50\% points on average across Replica and NaviGS. PanoGraphGS also achieves state-of-the-art performance among the evaluated methods in 2D panoptic segmentation. These results demonstrate the effectiveness of PanoGraphGS in both hierarchical 3D scene understanding and 2D panoptic segmentation. The project website is available at: https://github.com/gaojh0333/PanoGraphGS.

</details>

#### 2026-10-19 - Counting Contributions, Not Views: Occlusion-Aware Densification for 3D Gaussian Splatting

**Authors:** Marcel Rogge, René Schuster, Didier Stricker
**Links:** [abs](https://arxiv.org/abs/2610.27108) - [pdf](https://arxiv.org/pdf/2610.27108)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>Abstract</summary>

3D Gaussian Splatting grows a dense scene from a sparse initialization through adaptive density control (ADC), driven by per-Gaussian statistics gathered during rendering. These statistics pass a frustum-based visibility filter blind to occlusion: fully occluded Gaussians still count as observed, diluting the averaged gradient signal and suppressing densification precisely where geometry is occluded. We correct this with an occlusion-aware filter that restricts densification statistics to views in which a Gaussian actually contributes, and replace the criterion's raw view-count normalizer with an average-contribution one. Integrated into a StopThePop-based framework, the two together improve every image-quality metric over the occlusion-blind baseline on occlusion-heavy scenes (up to 6% lower LPIPS), at less than half the Gaussians a view-count normalizer requires. Under the longer schedules these large scenes require, the count stays bounded where most criteria diverge, and on smaller benchmarks our method stays competitive at a fraction of the competitors' count.

</details>

#### 2026-10-19 - Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision

**Authors:** Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
**Links:** [abs](https://arxiv.org/abs/2610.26508) - [pdf](https://arxiv.org/pdf/2610.26508)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Geometry-Aware Planning Representations for Monocular Flight with Cross-Modal Supervision
- 作者：Wencan Feng, Bailing Tian, Yulin Hui, Zhiyu Li, Junjie Lu
- 出版日期：2026-10-19T14:44:16Z
- 分类：主分类 Neural Scene Representations & Rendering；无二级分类
- 链接：[摘要](https://arxiv.org/abs/2610.26508) / [PDF](https://arxiv.org/pdf/2610.26508)

### 一句话总结
该论文提出一种面向单目 MAV 飞行的几何感知规划框架，通过将深度专家学习到的规划相关特征跨模态蒸馏到 RGB 规划器中，在不显式重建深度的前提下实现避障规划，并声称在仿真中训练后可零微调迁移到真实环境。

### 研究问题
现有 MAV 高速导航系统多依赖深度相机、立体视觉或 LiDAR 获取显式几何信息，而单目相机更轻量、低成本。但单目飞行仍面临挑战：RGB 图像不提供直接度量线索，且视觉外观在不同环境中变化显著。论文旨在解决如何让单目 RGB 规划器获得与规划相关的几何信息，从而支持避障飞行的问题。

### 核心思路/方法
论文提出一个几何感知的单目视觉规划框架，输入为两帧图像、它们的相对位姿以及 MAV 状态，输出轨迹。方法不显式重建深度，而是通过跨模态蒸馏，将特权深度专家学习到的、与规划相关的表示迁移到 RGB 规划器，以特征级几何监督补充下游规划目标。框架训练流程为：首先训练基于深度的几何专家；然后利用成对 RGB-D 观测，将其规划特征蒸馏到单目分支；最后使规划器适配下游轨迹规划目标。该设计促使策略学习与规划相关的几何特征，从而支持避障。数据收集、成对 RGB-D 监督和仿真评估使用 3D Gaussian Splatting（3DGS）模拟器渲染视觉观测。仿真中训练的规划器随后部署到真实环境，无需真实世界微调，并声称实现最高 6.5 m/s 速度下的避障。

### 主要贡献
- 提出一种几何感知单目视觉规划框架，从两帧图像、相对位姿和 MAV 状态预测轨迹，不显式重建深度。
- 引入跨模态蒸馏：先训练深度几何专家，再将其规划相关特征通过成对 RGB-D 观测蒸馏到单目分支，最后适配下游轨迹规划目标。
- 使用 3DGS 模拟器进行视觉观测渲染、数据收集、成对 RGB-D 监督和仿真评估。
- 声称仿真训练的规划器可零真实世界微调部署，并在最高 6.5 m/s 速度下实现避障。

### 局限性
摘要未提供足够信息说明方法在真实环境中的泛化边界、失败案例、计算开销、对不同场景或光照条件的敏感性，以及定量评估指标和对比基线细节。摘要未提供足够信息说明 3DGS 模拟器与真实环境之间域差异的具体影响。摘要未提供足够信息说明蒸馏过程中特征对齐的假设与限制。

### 阅读优先级
中。理由：该论文关注单目 MAV 高速避障与跨模态蒸馏规划表示，问题明确且方法路线清晰，并声称零微调真实部署；但摘要未给出定量结果、对比基线和详细实验设置，是否值得深入阅读需结合全文实验部分判断。

</details>

<details>
<summary>Abstract</summary>

Existing high-speed navigation systems for micro aerial vehicles (MAVs) commonly rely on depth cameras, stereo vision, or LiDAR to obtain explicit geometric information, while monocular cameras offer a lighter and lower-cost alternative. However, monocular flight remains challenging because RGB images offer no direct metric cues and visual appearance varies considerably across environments. We propose a geometry-aware monocular visual planning framework that predicts trajectories from two image frames, their relative pose, and the MAV state. Without explicitly reconstructing depth, the proposed method complements the downstream planning objective with feature-level geometric supervision by transferring the planning-relevant representation learned by a privileged depth expert to the RGB planner through cross-modal distillation. The framework first trains a depth-based geometric expert, then distills its planning features into a monocular branch using paired RGB-D observations, and finally adapts the planner to the downstream trajectory planning objective. This design encourages the policy to learn planning-relevant geometric features, enabling collision avoidance. We further use a 3D Gaussian Splatting (3DGS) simulator to render visual observations for data collection, paired RGB-D supervision, and simulation evaluation. The planner trained in simulation is then deployed in real-world environments without real-world fine-tuning, achieving obstacle avoidance at speeds of up to 6.5 m/s.

</details>

#### 2026-10-19 - Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention

**Authors:** Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25887) - [pdf](https://arxiv.org/pdf/2610.25887)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, novel view synthesis, view synthesis, splatting, AR, VR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking Sparse-View 3D Gaussian Splatting: A Few-Shot Learning Perspective on Overfitting Prevention
- 作者：Lejia Ye, Bin Wu, Jingjing Gao, Yiyang Wu, Xiaohu Zhang
- 出版日期：2026-10-19T06:44:19Z
- 分类：Neural Scene Representations & Rendering
- 链接：摘要页面 https://arxiv.org/abs/2610.25887 ；PDF https://arxiv.org/pdf/2610.25887

### 一句话总结
论文将稀疏视角 3D Gaussian Splatting 重新建模为少样本学习问题，把每个高斯基元视为神经元，并借助深度学习正则化思路，从数据监督增强与训练时正则化两方面抑制过拟合。

### 研究问题
稀疏视角新视角合成在 AR/VR 与实时通信中很重要，但从有限视角重建 3D 场景仍然困难。3DGS 在稠密视角下表现好，在稀疏输入下却容易出现 overfitting 与 geometry degradation。现有方法多从局部入手，分别处理数据质量或训练正则化，缺少统一且可解释的系统改进框架。

### 核心思路/方法
论文提出新的视角：从 few-shot learning 出发重新审视稀疏视角 3DGS，把每个 Gaussian primitive 当作 neuron，并利用深度学习正则化技术。在该统一框架下，通过两种策略从稀少观测中生成更有效的监督：
1. 数据相关监督增强：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization；
2. 训练时正则化：motion-aware dropout 与 early stopping，用于抑制过拟合并保持动态场景稳定性。

### 主要贡献
- 提出将稀疏视角 3DGS 视为少样本学习问题的新视角，并把高斯基元类比为神经元，借助深度学习正则化形成统一框架。
- 设计数据相关监督增强策略：optical flow-guided pseudo-view synthesis 与 joint camera-scene optimization。
- 设计训练时正则化策略：motion-aware dropout 与 early stopping，以抑制过拟合并保持动态场景稳定性。
- 在 SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset 上取得显著改进，作者称系统在该挑战赛 sparse-view track 中获得第一名。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销、对光流质量或相机优化的敏感性、消融实验细节、与各基线的定量差距，也未说明方法在非挑战数据或更极端稀疏条件下的泛化表现。

### 阅读优先级
高。理由：该工作针对稀疏视角 3DGS 的过拟合问题提出统一且可解释的少样本学习框架，并声称在 SIGGRAPH Asia 2025 相关挑战赛稀疏视角赛道获得第一，问题重要且结果信号较强；但摘要未提供实验细节，阅读全文时需重点核查方法假设、消融与泛化证据。

</details>

<details>
<summary>Abstract</summary>

Sparse-view novel view synthesis (NVS) is essential for AR/VR and real-time communication applications, yet remains challenging when reconstructing 3D scenes from limited viewpoints. While 3D Gaussian Splatting (3DGS) excels in dense-view scenarios, it suffers from overfitting and geometry degradation under sparse inputs. Current approaches often tackle these problems from a local perspective, addressing either data quality or training regularization individually, lacking a unified and interpretable framework for systematic improvement. We introduce a new perspective that reframes sparse-view 3DGS from a few-shot learning viewpoint, treating each Gaussian primitive as a neuron and leveraging deep learning regularization techniques. Under this unified framework, our approach generates more effective supervision from scarce observations through two strategies: (1) data-related supervision enrichment via optical flow-guided pseudo-view synthesis and joint camera-scene optimization; and (2) training-time regularization via motion-aware dropout and early stopping, which suppress overfitting while preserving dynamic-scene stability. Extensive experiments on the SIGGRAPH Asia 2025 volumetric video challenge sparse-view dataset demonstrate significant improvements over state-of-the-art optimization-based and feed-forward baselines. Our system won first place in the sparse-view track of the SIGGRAPH Asia 2025 challenge.

</details>

#### 2026-10-19 - RxGS: Relightable Gaussian Stylization via BRDF Decomposition

**Authors:** Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
**Links:** [abs](https://arxiv.org/abs/2610.25681) - [pdf](https://arxiv.org/pdf/2610.25681)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feature matching, NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, inverse rendering, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RxGS: Relightable Gaussian Stylization via BRDF Decomposition
- 作者：Wanrong Hong, Liu Jiang, Mukesh Prasad, Jun Li
- 出版日期：2026-10-19T02:31:17Z
- 分类：主分类为 Neural Scene Representations & Rendering；二级分类未提供
- 链接：摘要页 https://arxiv.org/abs/2610.25681 ；PDF https://arxiv.org/pdf/2610.25681

### 一句话总结
RxGS 提出一种基于 BRDF 感知 3D 高斯表示的可重光照 3D 场景风格化框架，通过仅优化逆渲染得到的漫反射反照率场，使风格化后的场景仍可在不同光照条件下重新渲染。

### 研究问题
论文关注基于参考图像的 3D 场景风格化问题：将参考图像的外观迁移到重建的 3D 场景上，同时保持场景几何。现有方法通常优化 NeRF 或 3DGS 等神经场景模型的 RGB 外观表示，而单点颜色混合了材质反射率、环境光照、着色效果以及观察方向等因素。当风格化修改这种混合颜色时，风格化过程中的光照效果会被“烘焙”进存储的外观中，导致风格化场景无法在不同光照下重新渲染。论文旨在解决这一限制。

### 核心思路/方法
RxGS 构建在 BRDF 感知的 3D 高斯表示之上，而不是修改逐点 RGB 颜色。方法仅优化通过逆渲染恢复的漫反射反照率场，同时保持粗糙度、金属度、表面法线以及估计的环境光照不变。这样，风格化场景除被编辑的反照率外，仍保留基于物理渲染器所需的其他组件，因此仍可重光照。在优化反照率场时，RxGS 使用最近邻特征匹配损失，并对高斯中心施加空间平滑先验。评估方面，论文采用基于光流扭曲误差的 Geometry Consistency Cost（GCC）。

### 主要贡献
- 提出 RxGS，一个可重光照的 3D 场景风格化框架，基于 BRDF 感知的 3D 高斯表示。
- 与修改逐点 RGB 颜色的做法不同，仅优化逆渲染得到的漫反射反照率场，保留粗糙度、金属度、表面法线和估计环境光照不变，从而支持风格化后的重光照。
- 使用最近邻特征匹配损失与高斯中心上的空间平滑先验优化反照率场。
- 采用基于光流扭曲误差的 GCC 进行评估；摘要称 RxGS 在所有评估的 NeRF-Synthetic 场景上取得最低 GCC，并在真实拍摄场景上保持竞争力，同时支持现有基于参考的 3D 场景风格化方法不具备的可重光照风格化能力。

### 局限性
摘要未提供足够信息。仅从摘要无法确定方法在计算开销、训练时间、对逆渲染质量的依赖、真实场景泛化能力、重光照一致性的定量评估以及失败案例等方面的具体局限。

### 阅读优先级
中。理由：论文聚焦 3D 场景风格化与可重光照表示的交叉问题，提出通过 BRDF 分解仅编辑反照率以保留重光照能力的思路，对神经场景表示与渲染方向具有相关性；但摘要未提供充分的实验细节、定量重光照评估和局限性信息，是否需要优先精读取决于读者对 3DGS、逆渲染或可重光照风格化的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Reference-based 3D scene stylization transfers the appearance of a reference image onto a reconstructed 3D scene while preserving scene geometry. Recent methods perform this transfer by optimizing the appearance representation of neural scene models including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). These methods optimize an RGB appearance representation, in which a single per-point colour combines the effects of material reflectance, environment illumination, together with the shading it produces, and the viewing direction. When stylization modifies this combined colour, the illumination effects present during stylization are baked into the stored appearance, so the stylized scene cannot be rendered under different illumination. To address this limitation, we present RxGS, a relightable 3D scene stylization framework built on a Bidirectional Reflectance Distribution Function (BRDF)-aware 3D Gaussian representation. Rather than modifying a per-point RGB colour, RxGS optimizes only the diffuse albedo field recovered by inverse rendering, while leaving roughness, metallicity, surface normals, and the estimated environment lighting unchanged. As a result, the stylized scene keeps all the components a physically-based renderer needs other than the edited albedo, and can therefore still be relit. RxGS optimizes the albedo field using a nearest-neighbour feature matching loss together with a spatial smoothness prior over Gaussian centres. We evaluate the method using a Geometry Consistency Cost (GCC) based on optical-flow warping error. RxGS achieves the lowest GCC on all evaluated NeRF-Synthetic scenes and remains competitive on real-captured scenes, while additionally supporting relightable stylization, which existing reference-based 3D scene stylization methods do not provide.

</details>

#### 2026-10-19 - SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering

**Authors:** Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
**Links:** [abs](https://arxiv.org/abs/2610.25665) - [pdf](https://arxiv.org/pdf/2610.25665)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** rendering, radiance, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpaRV: Sparse Radiance Voxels for Scalable Geometrically Consistent LiDAR-Visual Mapping and Rendering
- 作者：Jianheng Liu, Yunfei Wan, Fangming Cheng, Xiangyu Hong, Zuhao Zou, Haotian Li, Longji Yin, Chunran Zheng, Jiarong Lin, Fu Zhang
- 出版日期：2026-10-19T02:12:26Z
- 分类：Neural Scene Representations & Rendering（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：摘要页 https://arxiv.org/abs/2610.25665；PDF https://arxiv.org/pdf/2610.25665

### 一句话总结
SpaRV 是一种稀疏辐射体素地图，通过可微光线步进进行渲染，并用不规则 LiDAR 扫描与图像共同监督，以在机器人采集数据条件下实现几何一致、可扩展的 LiDAR-视觉建图与渲染。

### 研究问题
论文针对从机器人数据构建辐射场时面临的三个挑战：1）机器人轨迹服务于任务而非重建，少量视角导致几何约束不足；2）相机位姿与内参的残余误差使地图模糊；3）地图的 GPU 内存随场景规模增长，限制大场景中的细节水平。目标是同时获得照片级真实感和几何准确的地图，并支持大规模场景。

### 核心思路/方法
- 使用稀疏辐射体素地图，并以可微光线步进进行渲染。
- 让不规则 LiDAR 扫描与图像共同监督该地图；LiDAR 深度和占据信息用于锚定约束不足的几何，法向与平滑正则项用于保持 LiDAR 点之间的平滑性。
- 为校正相机误差，SpaRV 交替进行地图训练与对相机位姿和焦距的光度优化。
- 为限制训练和渲染中的 GPU 内存，SpaRV 同时仅以一个子图保持全分辨率，其余子图保持在较粗的八叉树层级。

### 主要贡献
- 提出 SpaRV：稀疏辐射体素地图，结合可微光线步进渲染，并利用不规则 LiDAR 扫描与图像共同监督。
- 利用 LiDAR 深度与占据锚定几何，并用正则项保持 LiDAR 点间平滑。
- 通过交替地图训练与相机位姿、焦距的光度优化来校正相机误差。
- 通过“一个子图全分辨率、其余子图粗八叉树层级”的策略约束 GPU 内存。
- 摘要报告：SpaRV 在远离采集轨迹处保持几何一致，并通过优化相机参数锐化纹理；在单张 24 GB GPU 上重建了由 63,582 张图像捕获的大学校园，并模拟其他相机和 LiDAR。

### 局限性
摘要未提供足够信息。摘要未给出定量精度、运行时间、内存占用对比、失败案例或与其他方法的系统比较等细节。

### 阅读优先级
中。理由：该工作面向机器人建图与渲染中的几何一致性、相机参数优化和大场景内存可扩展性问题，与 Neural Scene Representations & Rendering 及机器人应用相关；摘要给出了明确的问题、方法要点和大规模重建结果，但未提供定量实验细节。是否优先精读取决于读者对 LiDAR-视觉联合辐射场、可扩展建图或机器人仿真/导航/巡检应用的兴趣；仅就摘要信息而言，定为中。

</details>

<details>
<summary>Abstract</summary>

Robotic simulation, navigation, and inspection need photorealistic and geometrically accurate maps. Radiance fields achieve photorealism, but building them from robot data raises three challenges. A robot's trajectory serves its task, not reconstruction, so images from few viewpoints leave the geometry under-constrained. Residual errors in camera poses and intrinsics blur the map. The map's GPU memory grows with scene size, which limits its level of detail in large scenes. We present \textbf{SpaRV}, a \textbf{Spa}rse \textbf{R}adiance \textbf{V}oxel map rendered by differentiable ray marching, which lets irregular LiDAR scans supervise it alongside images. LiDAR depth and occupancy anchor the under-constrained geometry, and normal and smoothness regularizers keep it smooth between LiDAR points. To correct camera errors, SpaRV alternates map training with photometric optimization of the camera poses and focal lengths. To bound GPU memory in training and rendering, SpaRV holds one submap at a time at full resolution and the rest at coarser octree levels. Experiments show that SpaRV keeps the geometry consistent away from the captured trajectory and sharpens textures by optimizing the camera parameters. On one 24\,GB GPU, SpaRV reconstructs a university campus captured in 63{,}582 images and simulates other cameras and LiDARs. Our code will be released at \url{https://github.com/hku-mars/SpaRV}.

</details>

#### 2026-10-18 - MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes

**Authors:** Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
**Links:** [abs](https://arxiv.org/abs/2610.25345) - [pdf](https://arxiv.org/pdf/2610.25345)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, splatting, driving scene

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MCSplat: Multi-View Photometric and Geometric Consistent Feed-Forward Gaussian Splatting for Driving Scenes
- 作者：Yifei Wang, Wei Tian, Wenhua Bao, Jia Zhou, Hanshi Wang, Fudong Ge, Jianhua Wu, Shuai Yuan, Zhipeng Zhang, Xingliang Liu, Xianming Zeng, Jianyun Xu, Bingzhao Gao
- 出版日期：2026-10-18T15:40:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.25345) / [PDF](https://arxiv.org/pdf/2610.25345)

### 一句话总结
MCSplat 是一个面向驾驶场景的前馈高斯泼溅框架，通过构建规范外观空间解耦几何与相机外观，并用基于 Fisher 信息的不确定性自适应加权几何自监督，以提升多视角光度一致性与几何可靠性。

### 研究问题
论文针对稀疏多视角图像前馈高斯泼溅重建驾驶场景中的两个挑战：
1. **跨相机光度不一致**：曝光、ISP 和光照变化导致的多相机光度差异，可能被错误地吸收进高斯几何中。
2. **局部几何监督不可靠**：在深度不连续区域附近，基于法向的约束提供的局部几何监督不可靠。

### 核心思路/方法
- 从深度引导的多相机对应关系构建**规范外观空间**，将几何学习与相机特定外观解耦。
- 提出**多尺度双边网格 Transformer**，从规范渲染结果恢复原始相机外观，从而在光度监督时不污染高斯几何。
- 从光度敏感性估计**基于 Fisher 信息的不确定性**，并用其自适应加权面向表面的自监督，以提升局部几何可靠性。

### 主要贡献
- 提出 MCSplat：一个多视角一致的前馈高斯泼溅框架，面向驾驶场景。
- 构建规范外观空间以解耦几何学习与相机特定外观，缓解跨相机光度不一致对几何的污染。
- 设计多尺度双边网格 Transformer 恢复原始相机外观，支持不污染几何的光度监督。
- 引入基于 Fisher 信息的不确定性，自适应加权表面朝向自监督，改善局部几何可靠性。
- 摘要称实验显示重建质量和跨驾驶数据集泛化性提升，几何评估显示跨视角深度一致性和局部表面法向一致性增强，定性结果显示几何伪影更少、重叠视角结构更连贯。

### 局限性
摘要未提供足够信息。摘要未给出具体数据集名称、实验设置、计算开销、实时性、失败案例或定量指标细节。

### 阅读优先级
**中**。理由：该论文聚焦驾驶场景稀疏多视角前馈高斯泼溅中的光度一致性与几何监督可靠性，问题定义清晰且方法组合有针对性；但摘要未提供具体实验细节与量化结果，是否适合优先精读取决于读者对驾驶场景重建、前馈高斯泼溅或多相机光度一致性方向的兴趣。

</details>

<details>
<summary>Abstract</summary>

Driving-scene reconstruction via feed-forward Gaussian splatting from sparse multi-view images remains challenging due to two factors. First, cross-camera photometric inconsistency, caused by variations in exposure, ISP, and illumination, can be incorrectly absorbed into Gaussian geometry. Second, unreliable local geometric supervision arises from normal-based constraints near depth discontinuities. To address these issues, we present \textbf{MCSplat}, a multi-view consistent feed-forward Gaussian splatting framework for driving scenes. MCSplat constructs a canonical appearance space from depth-guided multi-camera correspondences to decouple geometry learning from camera-specific appearance. A multi-scale Bilateral Grid Transformer restores raw camera appearance from canonical renderings, enabling photometric supervision without contaminating Gaussian geometry. To improve local geometric reliability, we estimate Fisher-information-based uncertainty from photometric sensitivity and use it to adaptively weight surface-oriented self-supervision. Extensive experiments demonstrate improved reconstruction quality and generalization across driving datasets. Geometry-oriented evaluations further reveal enhanced cross-view depth consistency and local surface-normal agreement, while qualitative results show fewer geometric artifacts and more coherent structures across overlapping views.

</details>

#### 2026-10-18 - GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation

**Authors:** Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
**Links:** [abs](https://arxiv.org/abs/2610.25261) - [pdf](https://arxiv.org/pdf/2610.25261)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, splatting, robot navigation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GOFusion: Real-Time Gaussian-Occupancy Submap Fusion for Fisher-Informed Autonomous Robot Navigation
- 作者：Boxin Bu, Simon Boche, Haoming Zhang, Jaehyung Jung, Jiaxin Wei, Hannah Schieber, Daniel Roth, Angela P. Schoellig, Stefan Leutenegger
- 出版日期：2026-10-18T13:31:50Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25261 ；PDF https://arxiv.org/pdf/2610.25261 ；代码 https://github.com/Bennnoo/GOFusion ；补充视频 https://youtu.be/pLQKbxQvb6I

### 一句话总结
GOFusion 是一种面向自主机器人导航的实时视觉建图系统，将 3D 高斯原语锚定到局部占据地图上，并利用栅格化集成的 Fisher 近似实现在线敏感度量化，以支持高斯剪枝和下一最佳视角规划。

### 研究问题
论文关注自主机器人导航中的实时视觉建图问题：如何同时提供用于路径规划的空间感知能力与高保真外观信息，并在位姿校正、GPU 内存受限和大规模场景下保持几何与视觉一致性。摘要还指出需要一种在线不确定性/敏感度度量，作为信息驱动的高斯剪枝与下一最佳视角规划启发式。

### 核心思路/方法
- 从视觉-惯性 SLAM 获得的位姿估计与局部占据地图构建 3D 高斯地图，并将高斯原语锚定到局部占据地图。
- 支持位姿校正，以维持几何与视觉一致性。
- 将 3D Gaussian Splatting 优化限制在活跃子图（active submaps）内，以约束 GPU 内存使用。
- 提出栅格化集成的 Fisher 近似，在线量化每个高斯原语的敏感度，并将其作为信息驱动启发式用于高斯剪枝和下一最佳视角规划。
- 在公共数据集和真实无人机飞行中进行评估，并展示利用 Fisher 启发式的全自主无人机探索以细化高斯地图。

### 主要贡献
- 提出 GOFusion 实时视觉建图系统，将高斯原语锚定到局部占据地图，兼顾路径规划所需的空间感知与高保真外观。
- 设计基于活跃子图的 3D Gaussian Splatting 优化，以限制 GPU 内存占用。
- 引入栅格化集成的 Fisher 近似，在线量化逐原语敏感度，并用于高斯剪枝与下一最佳视角规划。
- 摘要称其在建图质量上优于若干基线，并实现实时、高保真、不确定性感知的大规模建图。
- 展示使用 Fisher 信息启发式的全自主无人机探索与高斯地图细化。

### 局限性
摘要未提供足够信息。摘要未给出具体失败场景、计算开销细节、对 SLAM 位姿质量的依赖程度、不同数据集上的定量局限，也未说明 Fisher 近似在何种条件下可能失效。

### 阅读优先级
高。理由：该论文直接面向自主机器人导航中的实时建图、内存约束、不确定性感知与主动探索规划，且提供代码与补充视频；摘要明确声称在公共数据集和真实无人机飞行中验证，并展示全自主无人机探索，适合关注神经场景表示与机器人/具身应用交叉方向的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

In this letter, we present GOFusion, a real-time visual mapping system for autonomous robot navigation that anchors Gaussian primitives to local occupancy maps, providing both spatial awareness for path planning and high-fidelity appearance that enables information-driven robot navigation. GOFusion builds 3D Gaussian maps from pose estimates and local occupancy maps obtained via visual-inertial SLAM and enables pose corrections to maintain both geometric and visual consistency. Furthermore, it restricts the 3D Gaussian Splatting optimization to active submaps to bound GPU memory usage. Building on the appearance-rich Gaussian map, we introduce a rasterizer-integrated Fisher approximation that quantifies per-primitive sensitivity online, serving as an information-driven heuristic for Gaussian pruning and next-best-view planning. We evaluate GOFusion on public datasets and in real-world drone flights. It not only outperforms several baselines in mapping quality, but also achieves real-time, high-fidelity and uncertainty-aware mapping at scale. Finally, we demonstrate fully autonomous drone exploration for Gaussian map refinement using the proposed Fisher-informed heuristic. Code is available at https://github.com/Bennnoo/GOFusion. We provide a supplementary video demonstration at https://youtu.be/pLQKbxQvb6I.

</details>

#### 2026-10-18 - GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation

**Authors:** Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
**Links:** [abs](https://arxiv.org/abs/2610.25245) - [pdf](https://arxiv.org/pdf/2610.25245)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** novel view synthesis, view synthesis, autonomous driving, driving scene, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoV2V: Geometry-Grounded Video Diffusion Model for Driving Scene Generation
- 作者：Yuchen Xi, Yuhan Guo, Chenwei Hou, Zixu Liu, Jin Fang, Jason Liu, Ruigang Yang
- 出版日期：2026-10-18T13:05:08Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25245 ；PDF https://arxiv.org/pdf/2610.25245 ；项目页 https://xiyuche.github.io/GeoV2V/

### 一句话总结
GeoV2V 是一个以几何为约束的视频到视频扩散框架，旨在沿新轨迹合成时序一致的驾驶场景视频，并配套提出 Para4D 合成数据集以提供跨车道变换的同步多轨迹监督。

### 研究问题
论文关注轨迹变化下的新视角合成，尤其是外推到车道偏移等未见视角时，现有方法难以生成一致视频的问题。摘要指出两类现有方法存在不足：基于重建的方法几何一致但在大视角变化下视觉质量下降；先重建后修复的方法帧视觉上看似合理，但存在几何与时序不一致。核心挑战在于真实数据集缺乏同步多轨迹监督，使跨车道变换学习困难。

### 核心思路/方法
GeoV2V 被描述为一个几何锚定的视频到视频扩散框架：它将 LiDAR 与深度导出的几何先验，与 Wan 2.1 骨干中的全视频条件相结合，用于沿新轨迹合成时序一致的驾驶视频。为缓解跨车道变换监督不足，论文引入 Para4D 合成数据集，捕获动态场景中同步的多车道驾驶视频，为车道偏移生成提供显式监督，并作为几何一致视角合成的训练先验。

### 主要贡献
- 提出 GeoV2V：几何锚定的视频到视频扩散框架，在 Wan 2.1 骨干中融合 LiDAR 和深度几何先验与全视频条件，面向新轨迹驾驶视频生成。
- 识别并针对真实数据缺乏同步多轨迹监督的问题，提出 Para4D 合成数据集，提供车道偏移生成的显式监督。
- 摘要称在 Waymo、nuScenes 和 Para4D 上的实验显示出在视觉质量、几何一致性以及大轨迹偏移下复杂光照动态鲁棒性方面的最先进性能。

### 局限性
摘要未提供足够信息。摘要未给出具体失败案例、计算成本、对 LiDAR/深度先验质量的依赖程度、Para4D 与真实数据分布差异的量化影响，也未提供各数据集上的详细指标与消融结果。

### 阅读优先级
中。理由：该论文聚焦自动驾驶仿真中的新轨迹视角合成，问题定义清晰，且同时提出方法与大轨迹偏移监督数据集；摘要声称在 Waymo、nuScenes 与 Para4D 上取得最先进表现。但仅凭摘要无法判断实验细节、复现难度与实际部署成本，因此优先级定为中，适合关注驾驶场景生成、几何一致视频扩散与仿真数据构建的读者进一步阅读全文核实。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis under trajectory changes is essential for autonomous driving simulation, yet existing methods struggle to generate consistent videos when extrapolating to unseen viewpoints such as lane shifts. Reconstruction-based approaches maintain geometric consistency but degrade in visual quality under large viewpoint changes, while reconstruct-then-restore methods often produce visually plausible frames yet suffer from geometric and temporal inconsistencies. We present GeoV2V, a geometry-grounded video-to-video diffusion framework that synthesizes temporally coherent driving videos along novel trajectories by integrating LiDAR and depth-derived geometric priors with full-video conditioning in the Wan 2.1 backbone. A key challenge in learning cross-lane transformations is the lack of synchronized multi-trajectory supervision in real-world datasets. To address this, we also introduce Para4D, a synthetic dataset capturing synchronized multi-lane driving videos within dynamic scenes, which provides explicit supervision for lane-shift generation and serves as a strong training prior for geometry-consistent view synthesis. Experiments on Waymo, nuScenes, and Para4D demonstrate state-of-the-art performance in visual quality, geometric consistency, and robustness to complex lighting dynamics under large trajectory shifts. Project page: https://xiyuche.github.io/GeoV2V/

</details>

#### 2026-10-18 - Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots

**Authors:** Que Haohua, Mingkai Liu, Handong Yao
**Links:** [abs](https://arxiv.org/abs/2610.25068) - [pdf](https://arxiv.org/pdf/2610.25068)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** SfM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Localization and Neural Splatting on the Edge: An FPGA Scene Memory for Robots
- 作者：Que Haohua, Mingkai Liu, Handong Yao
- 出版日期：2026-10-18T07:18:24Z
- 分类：主分类 Neural Scene Representations & Rendering；次分类 Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25068) / [PDF](https://arxiv.org/pdf/2610.25068)

### 一句话总结
LENS 在 AMD KR260 低功耗 FPGA/ARM 平台上协同设计 SCR 定位加速器与定点 3DGS 渲染器，将 ACEsplat 风格场景记忆工作负载带到边缘设备。

### 研究问题
资源受限的机器人与自动驾驶车辆需要能在无桌面 GPU 条件下定位相机并渲染附近视图的场景记忆。SCR 与 3DGS 因无需 SfM 阶段而适用，但 ACEsplat 风格流水线以 GPU 为中心，迁移到边缘 FPGA 存在困难：SCR 对位姿敏感，3DGS 渲染不规则且对容量敏感。

### 核心思路/方法
论文提出 LENS，一个运行于 AMD KR260 的边缘场景记忆加速系统，将 ACEsplat 风格工作负载带到低功耗 FPGA/ARM 平台。作者不提出新的场景模型，而是将两个主导内核与板级数据通路协同设计：一是保持位姿精度的 INT16 SCR 加速器；二是位精确定点有序 3DGS 渲染器，将 alpha 透射率改写为 log-sum-exp 递推，并剔除可证明无用的流式高斯。摘要称所有 LENS 延迟、功耗与质量结果均为板级实测。

### 主要贡献
- 提出 LENS 边缘场景记忆加速系统，在 AMD KR260 上实现 ACEsplat 风格工作负载。
- 设计 INT16 SCR 加速器，保持 DSAC* 定位精度，延迟为 25.42 ms。
- 设计位精确定点有序 3DGS 渲染器，采用 log-sum-exp 递推表达 alpha 透射率，并移除可证明无用的流式高斯。
- 板载渲染器在 Cambridge 上达到 34.11 dB，高于 ACEsplat 的 33.20；RealEstate10K 新视图合成达到 27.84 dB，高于 26.11；全部十个 Wayspots 场景达到 ACEsplat 渲染目标。
- 与 Jetson Orin NX 相比，LENS 在每个部署任务上性能功耗比更优，提升 1.9x 至 5.7x，功耗约为其四分之一，并在定位与 Wayspots 渲染上绝对延迟更快。
- 设备端训练达到 ACEsplat 级质量，但未达到 GPU 的时间或能耗水平，作者将其标记为未来训练加速器的剩余边界。

### 局限性
- 设备端训练在时间或能耗上未达到 GPU 水平，摘要未提供具体差距数值。
- 摘要未提供功耗绝对值、FPGA 资源占用、散热或部署环境细节。
- 摘要未提供失败案例、泛化范围或更多数据集的定量结果。
- 摘要未提供与除 Jetson Orin NX 外其他边缘平台的比较。
- 摘要未提供训练加速器设计或时间表。

### 阅读优先级
中。理由：该论文聚焦边缘 FPGA 上的场景记忆加速，涉及 SCR 定位与 3DGS 渲染的协同设计，对机器人、AR 与边缘视觉系统读者有参考价值；摘要给出了板级实测的延迟、质量与性能功耗比结果，但未提供功耗绝对值、资源占用与训练差距细节，是否高优先级取决于读者对 FPGA 部署与 3DGS 边缘加速的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Resource-constrained robots and autonomous vehicles need scene memories that localize a camera and render nearby views without a desktop GPU. Scene-coordinate regression (SCR) and 3D Gaussian splatting (3DGS) fit because they avoid an SfM stage, but ACEsplat-style pipelines are GPU-centered, and moving them to an edge FPGA is hard because SCR is pose-sensitive and 3DGS rendering is irregular and capacity-sensitive. We present LENS, an edge scene-memory acceleration system on the AMD KR260 that brings an ACEsplat-style workload to a low-power FPGA/ARM platform. Rather than proposing a new scene model, LENS co-designs the two dominant kernels with the board data path: an INT16 SCR accelerator that preserves pose accuracy, and a bit-exact fixed-point ordered 3DGS renderer that rewrites alpha transmittance as a log-sum-exp recurrence and removes provably useless streamed Gaussians. All LENS latency, power, and quality results are board-measured. The SCR engine preserves DSAC* localization accuracy at 25.42 ms, the on-board renderer reaches 34.11 dB on Cambridge against ACEsplat's 33.20, novel-view synthesis on RealEstate10K reaches 27.84 dB against 26.11, and all ten Wayspots scenes reach the ACEsplat rendering target. LENS wins performance per watt over a Jetson Orin NX on every deployment task, by 1.9x to 5.7x at about a quarter of the power, and is faster in absolute latency on localization and Wayspots rendering. On-device training reaches ACEsplat-level quality but not the GPU's time or energy, marking the remaining boundary for a future training accelerator.

</details>

#### 2026-10-18 - FineSplat: Fine Patches, Local Groups, Detailed Splats

**Authors:** Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
**Links:** [abs](https://arxiv.org/abs/2610.25011) - [pdf](https://arxiv.org/pdf/2610.25011)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FineSplat: Fine Patches, Local Groups, Detailed Splats
- 作者：Hyebin Kim, Hwasik Jeong, Joonhyuk Park, Gyeongjin Kang, Jungwoo Kim, Younghyun Kim, Eunbyung Park
- 出版日期：2026-10-18T04:44:10Z
- 分类：Neural Scene Representations & Rendering（无二级分类）
- 链接：[摘要](https://arxiv.org/abs/2610.25011) / [PDF](https://arxiv.org/pdf/2610.25011)

### 一句话总结
FineSplat 是一个围绕细粒度图像块构建的前馈式 3D Gaussian Splatting 框架，通过双重分组策略、重建误差反馈和紧凑高斯生成，在保持效率与紧凑性的同时恢复更丰富的几何与外观细节。

### 研究问题
前馈式 3D Gaussian Splatting 虽然有望实现即时场景重建与高质量新视角合成，但在细粒度几何和外观的恢复上仍然困难。作者因此重新审视前馈模型如何表示、聚合与精炼细节视觉信息。具体而言，当图像块分辨率很高、token 数量很大时，全局多视图注意力代价过高，需要更高效的局部交互机制；同时，单次前馈预测在细节恢复上存在局限。

### 核心思路/方法
论文提出 FineSplat，其核心设计包括：
1. **以细粒度图像块为基础**：框架围绕 fine-grained image patches 构建，以提升细节表达能力。
2. **双重分组策略**：由于高 token 分辨率下全局多视图注意力过于昂贵，方法结合两种互补的局部性——按视图分组（view-wise grouping）使邻近视图间高效交互；3D 空间分组则将几何相关的 token 提升到 3D 场景空间中重新连接，这些 token 在视图分组下可能从未交互。
3. **重建误差作为直接反馈**：利用重建误差提供显式的、基于渲染的信号，以恢复细粒度结构和外观，从而克服单次前馈预测的限制。
4. **紧凑高斯生成方案**：在享受细粒度特征收益的同时，避免不必要地增加高斯基元数量。

### 主要贡献
- 提出 FineSplat 前馈式 3DGS 框架，围绕细粒度图像块进行细节表示与聚合。
- 设计双重分组策略，在视图局部性与 3D 空间局部性之间互补，缓解高分辨率 token 下全局注意力的开销问题。
- 引入基于重建误差的显式渲染反馈，弥补单次前馈预测在细粒度结构恢复上的不足。
- 提出紧凑高斯生成方案，在不显著增加基元数量的前提下保留细粒度特征优势。
- 摘要声称在相同或更小的高斯预算下，以较大幅度取得 state-of-the-art 结果，同时保持效率与紧凑性。

### 局限性
- 摘要未提供足够信息说明方法的具体失败场景或适用范围限制。
- 摘要未提供足够信息说明双重分组策略在不同场景规模、视图数量或分辨率下的敏感性。
- 摘要未提供足够信息说明重建误差反馈的具体计算方式、训练成本或收敛行为。
- 摘要未提供足够信息说明“state-of-the-art by a substantial margin”所对应的数据集、指标与定量结果。
- 摘要未提供足够信息说明紧凑高斯生成方案对基元数量的具体控制机制与压缩程度。

### 阅读优先级
**高**。理由：该论文聚焦前馈式 3DGS 中细粒度几何与外观恢复这一明确难题，提出的双重分组、渲染误差反馈与紧凑高斯生成均属于方法层面的实质性设计；且摘要声称在相同或更小高斯预算下显著优于现有方法。若关注前馈 3D 重建、3D Gaussian Splatting 的效率与细节平衡，该论文具有较高阅读价值。但需注意，摘要未给出实验细节，定量结论需查阅正文验证。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) promises instant scene reconstruction with high-quality novel-view synthesis. Yet, fine-grained geometry and appearance remain difficult to recover, motivating us to revisit how feed-forward models represent, aggregate, and refine detailed visual information. We introduce FineSplat, a feed-forward 3DGS framework built around fine-grained image patches. Since global multi-view attention becomes prohibitively expensive at such high token resolutions, we develop a dual-grouping strategy that combines two complementary forms of locality: view-wise grouping enables efficient interaction among neighboring views, while 3D spatial grouping reconnects geometrically related tokens that may never have interacted under view-wise grouping by lifting them into the 3D scene space. We further leverage reconstruction error as direct feedback, providing an explicit rendering-based signal to recover fine-grained structures and appearance, thereby overcoming the limitations of one-pass feed-forward prediction. Finally, a compact Gaussian generation scheme preserves the benefits of fine-grained features without unnecessarily increasing the number of primitives. Together, these designs enable FineSplat to recover richer geometry and appearance while remaining efficient and compact, achieving state-of-the-art results by a substantial margin, under the same or smaller Gaussian budgets than existing methods.

</details>

#### 2026-10-17 - SwitchSplat: Learning Discrete Object States from Casually Captured Scenes

**Authors:** Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
**Links:** [abs](https://arxiv.org/abs/2610.24812) - [pdf](https://arxiv.org/pdf/2610.24812)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SwitchSplat: Learning Discrete Object States from Casually Captured Scenes
- 作者：Yizheng Xie, Yalda Foroutan, George Shramko, Daniel Rebain, Shrisudhan Govindarajan, Andrea Tagliasacchi
- 出版日期：2026-10-17T18:35:44Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24812) | [PDF](https://arxiv.org/pdf/2610.24812)

### 一句话总结
SwitchSplat 提出一种基于 3D Gaussian Splatting 的“基础 + 槽位”分解表示，用于从随性拍摄视频中学习可交互物体的离散二值状态，并支持在推理时自由组合状态进行新视角渲染。

### 研究问题
现有 3D Gaussian Splatting 表示假设世界是静态的，无法建模随性拍摄中用户与环境交互（如开门、拨动开关、移动物体）带来的离散状态变化。时间条件动态方法（如 4DGS）将“状态被观察到的时间”与“场景处于何种状态”混为一谈，只能回放已见序列，难以组合任意物体配置。

### 核心思路/方法
论文提出 base+slot 分解：一个共享的静态 base 捕捉不变场景，每个可交互物体对应一个 slot，独立持有该物体的两种二值状态（on/off）。由于高斯到 slot 的分配完全可微，模型可直接从视频中发现各状态的几何，无需人工标注。推理时用户可自由组合各 slot 状态，并从任意视角渲染结果场景。

### 主要贡献
- 提出 SwitchSplat，据摘要称为首个通过 base+slot 分解处理离散物体状态变化的 3DGS 表示。
- 实现无需人工标注的可微状态几何发现。
- 支持推理时自由组合 slot 状态，渲染捕捉时从未见过的状态组合。
- 在新随性拍摄数据集上验证，并在新视角合成质量上优于静态与动态基线。

### 局限性
摘要未提供足够信息（未说明方法对非二值状态、复杂拓扑变化、遮挡或大规模场景的适用性，也未给出计算开销、数据集规模与失败案例等细节）。

### 阅读优先级
中。理由：该工作针对 3DGS 静态假设与动态表示状态混淆的问题，提出可组合离散状态的表示，问题定义清晰且与可交互场景重建相关；但摘要未提供定量结果、数据集细节与局限分析，需阅读全文后才能判断其实际效果与适用范围。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has made high-fidelity 3D reconstruction fast and accessible, yet existing representations assume a static world. This assumption breaks down in casual captures, where a user naturally interacts with the environment -- opening doors, toggling switches, or moving objects -- introducing discrete state changes that no current framework can model. Time-conditioned dynamic methods such as 4DGS conflate when a state was observed with what state the scene is in, limiting them to replaying seen sequences rather than composing arbitrary object configurations. We present SwitchSplat, the first 3DGS representation to address this gap via a base+slot decomposition: a shared static base captures the invariant scene, while each slot independently holds the two binary states (on/off) of one interactable object. Because the assignment of Gaussians to slots is fully differentiable, the model discovers the geometry of each state directly from video, without manual annotation. At inference, the user can freely combine slot states and render the resulting scene from any viewpoint. We validate SwitchSplat on a new casual-capture dataset and show that it outperforms static and dynamic baselines in novel-view synthesis quality, while uniquely supporting rendering of state combinations never seen during capture. Project page: https://switchsplat.github.io

</details>

#### 2026-10-17 - Directionally Factorized Illumination with Spherical Harmonic Rotation

**Authors:** Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
**Links:** [abs](https://arxiv.org/abs/2610.24811) - [pdf](https://arxiv.org/pdf/2610.24811)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, neural rendering, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Directionally Factorized Illumination with Spherical Harmonic Rotation
- 作者：Yimeng Dou, Adam M. Saunders, Andre T. S. Hucke, Michael E. Kim, Adam W. Anderson, Eric R. Tkaczyk, Bennett A. Landman, Daniel Moyer
- 出版日期：2026-10-17T18:35:02Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.24811) / [PDF](https://arxiv.org/pdf/2610.24811)

### 一句话总结
论文提出可插入任意新视角合成管线的 DaFISH，将逐点发射颜色分解为表面反照率与球谐表示的光照因子，以缓解相机与光源刚性同装导致的姿态相关光照问题。

### 研究问题
许多真实采集场景中，主动光源（如相机闪光灯、水下载具灯、内窥镜或腹腔镜光源）与相机刚性连接；相机移动时光源随之移动，造成每个表面点的光照方向随视角变化。NeRF、Gaussian Splatting 等神经渲染方法会把这种姿态相关光照编码为表面颜色，从而产生外观不一致，并增加恢复底层场景的难度。

### 核心思路/方法
- 提出 **DaFISH**，可插入任意新视角合成（NVS）管线（如 NeRF）。
- 将逐点发射颜色分解为**表面反照率**与**球谐（SH）表示的光照因子**。
- 训练时直接评估 SH 光照，从而稳定地联合优化反照率、光照与几何。
- 基于闭式 SH 到辐照度的转换，训练流程从 SH 评估到体渲染完全可微。
- 提供解析式光照泛化到任意相机姿态的能力，无需重新训练。

### 主要贡献
- 针对相机同装主动光源导致的姿态相关光照问题，提出可插拔的光照分解方案 DaFISH。
- 将反照率与 SH 光照因子分解，并实现从 SH 评估到体渲染的完全可微训练。
- 支持对任意相机姿态的解析式光照泛化，无需重训练。
- 摘要在五个场景的留出帧上报告：DaFISH 在所有对比方法中取得最佳平均 PSNR（38.91 dB）、SSIM（0.9613）与 LPIPS（0.0582），并优于最强的 splatting 基线及最接近的 NeRF 基线；相较先前方法能跨视角更一致地恢复场景。

### 局限性
- 摘要未提供足够信息说明方法在非刚性光源、多光源或复杂全局光照条件下的适用性。
- 摘要未提供足够信息说明计算开销、训练时间与显存需求。
- 摘要未提供足够信息说明五个场景的具体构成、数据规模及基线方法的完整列表。
- 摘要未提供足够信息说明对极端相机姿态或稀疏视角的鲁棒性。

### 阅读优先级
**中**。理由：该工作针对相机同装主动光源这一明确且具有实际采集意义的场景，方法可插入现有 NVS 管线，并给出定量指标；但摘要仅概述核心分解与结果，未展开实验细节与适用边界，适合作为该方向的方法参考而非必须优先精读的综述性文献。

</details>

<details>
<summary>Abstract</summary>

Many real-world capture scenarios involve an active light source rigidly attached to the camera: camera flashes for dark-environment imaging, underwater vehicle lights, and endoscopic/laparoscopic medical procedures. As the camera moves, the co-mounted light moves with it, causing the illumination direction at each surface point to change across views. Neural rendering methods (NeRF, Gaussian Splatting) encode this pose-dependent illumination as surface coloration, producing appearance inconsistencies and making it harder to recover the underlying scene. We present \textbf{DaFISH}, which can be plugged into any novel-view synthesis (NVS) pipeline such as NeRF. It factorizes per-point emitted color into surface albedo and a spherical harmonic (SH)-represented illumination factor. During training, the SH illumination is evaluated directly, enabling stable joint optimization of albedo, lighting, and geometry. \textbf{DaFISH} provides analytical generalization of illumination to arbitrary camera poses without retraining. Building on the closed-form SH-to-irradiance conversion, the training pipeline is fully differentiable from SH evaluation through volume rendering. Averaged over the held-out frames of the five scenes, \textbf{DaFISH} attains the best mean PSNR (38.91\,dB), SSIM (0.9613), and LPIPS (0.0582) among all compared methods. It improves over the strongest splatting baseline as well as the closest NeRF-based baseline, while recovering the scene consistently across views compared to prior methods.

</details>

#### 2026-10-15 - CF-Splat: Closed-Form Triangle Splatting with Mesh Priors

**Authors:** Yixin Fang, Liang Zhao
**Links:** [abs](https://arxiv.org/abs/2610.22108) - [pdf](https://arxiv.org/pdf/2610.22108)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, 3DGS, novel view synthesis, view synthesis, radiance, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CF-Splat: Closed-Form Triangle Splatting with Mesh Priors
- 作者：Yixin Fang, Liang Zhao
- 出版日期：2026-10-15T15:49:34Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.22108

### 一句话总结
CF-Splat 提出一种基于已知网格先验的闭式三角 splatting 框架，将多视图外观估计转化为全局线性最小二乘问题，从而避免迭代非线性优化，在保持竞争性或更优新视角合成质量的同时大幅降低计算时间与显存占用。

### 研究问题
现有基于 splatting 的辐射场表示通常依赖迭代非线性优化，需要联合优化数百万个相互耦合的图元参数，导致计算时间长、峰值 GPU 显存消耗大，并且容易陷入局部极小值。论文关注的问题是如何在已知网格几何与已标定相机的条件下，高效地估计场景外观，避免上述迭代非线性优化带来的代价与不稳定性。

### 核心思路/方法
论文的关键洞察是：在给定网格几何和标定相机的条件下，通过适当形式化问题，渲染像素颜色可以表示为关于每个顶点球谐（SH）系数的线性函数。因此，多视图场景外观估计可被建模为一个全局线性最小二乘（LLS）问题，无需迭代非线性优化。为保证在多视图观测覆盖不均匀时解仍适定，作者引入自适应 SH 正则化，约束支持不足的高阶 SH 系数，从而得到唯一的全局极小值。为扩展到大规模场景，作者开发了三角形结构的无矩阵预条件共轭梯度求解器，避免显式构造大型稀疏法方程系统，同时产生与 LLS 相同的解。

### 主要贡献
- 提出 CF-Splat，一种面向已知网格（预先存在或由上游建图/重建流程提供）的闭式三角 splatting 框架，用于高效场景外观估计。
- 将多视图外观估计形式化为关于每顶点 SH 系数的全局线性最小二乘问题，避免迭代非线性优化。
- 引入自适应 SH 正则化，以在观测覆盖不均匀时保证适定性并得到唯一全局极小值。
- 开发三角形结构的无矩阵预条件共轭梯度求解器，避免显式构造大型稀疏法方程系统，提升大规模场景可扩展性。
- 在多种真实世界数据集上的实验表明，与最先进 splatting 方法相比，CF-Splat 达到竞争性或更优的 NVS 质量；在不同规模场景下，相比 3DGS 在消费级笔记本上平均减少约 27.5–378.0 倍计算时间，峰值 GPU 显存平均降低约 1.8 倍。

### 局限性
摘要未提供足够信息。摘要未说明该方法是否依赖高质量网格先验、对网格误差或缺失的鲁棒性、在无网格或网格质量较差场景下的适用性，以及具体数据集、评价指标和消融实验细节。

### 阅读优先级
中。理由：该论文聚焦于基于网格先验的闭式 splatting 外观估计，针对迭代优化耗时长、显存高、易陷局部极小值的问题提出线性最小二乘与无矩阵求解方案，并报告了显著效率提升，对神经渲染与机器人感知中的高效 NVS 有潜在价值。但摘要未提供网格先验依赖程度、鲁棒性边界和实验细节，且方法前提是已知网格几何，适用场景相对受限，因此优先级为中等而非高。

</details>

<details>
<summary>Abstract</summary>

Splatting-based radiance-field representations have recently gained popularity in robotic perception, enabling high-quality novel-view synthesis (NVS) through explicit scene primitives. However, existing splatting methods typically rely on iterative nonlinear optimization that jointly optimizes millions of coupled primitive parameters, resulting in substantial computation time, peak GPU memory consumption, and susceptibility to local minima. In this paper, we propose CF-Splat, a novel closed-form triangle-splatting framework for efficient scene appearance estimation over a known mesh either pre-existing or provided by upstream mapping or reconstruction pipelines. Our key insight is that, by properly formulating the problem over the given mesh geometry and calibrated cameras, the rendered pixel colors can be expressed linearly with respect to the per-vertex spherical harmonics (SH) coefficients, allowing multi-view scene appearance estimation to be formulated as a global linear least-squares (LLS) problem without the need of iterative nonlinear optimization. To guarantee a well-posed solution under uneven multi-view observation coverage, we introduce adaptive SH regularization that constrains insufficiently supported high-order SH coefficients and yields a unique global minimizer. To ensure the scalability to large-scale scenes, we develop a triangle-structured matrix-free preconditioned conjugate-gradient solver that avoids explicitly constructing the large sparse normal system while producing the same LLS solution. Experiments on diverse real-world datasets demonstrate that CF-Splat achieves competitive or superior NVS quality compared with state-of-the-art splatting methods. While, CF-Splat requires approximately 27.5-378.0 times less computation time and 1.8 times lower peak GPU memory on average than 3DGS across scenes of different scales on a consumer-grade laptop.

</details>

#### 2026-10-15 - Edit4D: Editable 4D Scene Generation with Textual Control

**Authors:** Chanwoo Kim, Tackgeun You, Hwasup Lim
**Links:** [abs](https://arxiv.org/abs/2610.21668) - [pdf](https://arxiv.org/pdf/2610.21668)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Edit4D: Editable 4D Scene Generation with Textual Control
- 作者：Chanwoo Kim, Tackgeun You, Hwasup Lim
- 出版日期：2026-10-15T10:52:22Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21668 ；PDF：https://arxiv.org/pdf/2610.21668 ；项目页：https://chanwo0kim.github.io/Edit4D/

### 一句话总结
Edit4D 是一个可编辑的文本到 4D 场景生成框架，通过将背景与动态角色分开表示并分阶段生成，以支持相机控制和对象级编辑。

### 研究问题
摘要指出，现有文本驱动动态场景生成方法通常生成整体场景视频，背景与动态角色相互耦合，因此难以进行对象级编辑和灵活的相机控制；同时可编辑 4D 场景生成还需在编辑时保持空间几何与时间动态，这仍是挑战。

### 核心思路/方法
- 采用阶段特定（stage-specific）的生成流程，将 4D 场景拆分为背景与动态角色两个独立表示。
- 给定用户指令后，先将其分解为背景、动态角色、场景-角色合成对应的阶段提示。
- 使用文本到图像与相机条件生成先验合成多视角场景图像，并重建背景的 3D Gaussian splatting 表示。
- 生成角色图像，用图像条件视频先验进行动画化，重建 4D mesh，并绑定 Gaussian primitives 得到角色表示。
- 通过文本引导分割与接触感知优化将两部分组合，再进行全局场景细化以提升协调性与渲染一致性。

### 主要贡献
- 提出 Edit4D，一个可编辑的文本到 4D 场景生成框架，从分离的背景与动态角色表示构建 4D 场景。
- 通过阶段特定提示分解与分阶段生成流程，缓解背景与角色耦合带来的编辑和相机控制困难。
- 整合阶段特定组件后，支持可控相机运动、灵活的对象级编辑，以及可编辑 4D 场景的实际构建。

### 局限性
摘要未提供足够信息。摘要未给出定量或定性实验细节、失败案例、计算成本、编辑类型覆盖范围、评估指标或用户研究结果。

### 阅读优先级
中。理由：该工作聚焦文本到 4D 场景生成中的可编辑性与对象级编辑，问题定位明确，方法流程具有结构性；但摘要未提供实验验证细节，是否显著优于现有方法、适用边界与实际可用性尚无法仅凭摘要判断。

</details>

<details>
<summary>Abstract</summary>

We introduce Edit4D, an editable text-to-4D scene generation framework that constructs 4D scenes from separate background and dynamic character representations. Recent advances in generative models have enabled text-driven dynamic scene synthesis, but editable 4D scene generation remains challenging due to the need to preserve spatial geometry and temporal dynamics. Existing approaches typically generate holistic scene videos, where the background and dynamic characters are coupled, making object-level editing and flexible camera control difficult. Edit4D addresses these limitations through a stage-specific generation pipeline. Given a user instruction, Edit4D first decomposes it into stage-specific prompts for background, dynamic character, and scene-character composition. Using these prompts, we synthesize multi-view scene images with text-to-image and camera-conditioned generative priors and reconstruct a background 3D Gaussian splatting representation. We then generate a character image, animate it with an image-conditioned video prior, reconstruct a 4D mesh, and bind Gaussian primitives to obtain a character representation. Finally, both components are composed through text-guided segmentation and contact-aware optimization. A global scene refinement is then performed to improve harmonization and rendering consistency. By integrating stage-specific components, Edit4D enables controllable camera motion, flexible object-level editing, and the practical construction of editable 4D scenes. Project page: https://chanwo0kim.github.io/Edit4D/

</details>

#### 2026-10-15 - Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation

**Authors:** Sheng Ye, Jiangke Lin, Fudong Wang, Yi Yuan, Zhen-Hui Dong, Yong-Jin Liu
**Links:** [abs](https://arxiv.org/abs/2610.21634) - [pdf](https://arxiv.org/pdf/2610.21634)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anchor3DGS: Feed-Forward 3D Gaussian Splatting with Compact Anchor-Based Representation
- 作者：Sheng Ye, Jiangke Lin, Fudong Wang, Yi Yuan, Zhen-Hui Dong, Yong-Jin Liu
- 出版日期：2026-10-15T10:18:41Z
- 分类：Neural Scene Representations & Rendering
- 链接：[摘要](https://arxiv.org/abs/2610.21634) / [PDF](https://arxiv.org/pdf/2610.21634)

### 一句话总结
Anchor3DGS 提出一种无位姿、前馈式的 3D 高斯泼溅框架，用基于信息熵放置的紧凑 3D 锚点表示替代逐像素预测范式，在大幅减少高斯原语数量的同时提升新视角合成质量。

### 研究问题
现有前馈式 3DGS 方法多采用“像素对齐”范式，即每个输入像素预测一个高斯原语。这带来两个问题：
1. 高斯原语数量与输入分辨率及视角数量直接耦合，难以灵活控制表示规模；
2. 在无纹理区域产生冗余原语，而在几何复杂区域覆盖不足。

### 核心思路/方法
- 用**紧凑的锚点表示**替代像素对齐预测：在场景中放置一组 3D 锚点，由信息熵引导，将锚点集中在视觉复杂度较高的区域，同时保持较广的空间覆盖。
- 每个锚点执行**遮挡感知的多视角图像特征聚合**，并与其他锚点进行信息交换，随后被解码为一组局部高斯原语。
- 引入**轻量级特征增强模块**，对高斯泼溅输出的粗略 RGB 结果进行细化，以提升渲染保真度。
- 整体为**无位姿（pose-free）前馈框架**。

### 主要贡献
- 提出 Anchor3DGS，以基于锚点的紧凑表示取代逐像素预测范式，使高斯原语数量与输入分辨率/视角数解耦。
- 利用信息熵引导锚点放置，缓解无纹理区域冗余与几何复杂区域覆盖不足的问题。
- 设计锚点间的遮挡感知聚合与信息交换机制，以及轻量级特征增强模块以改善渲染质量。
- 在多个基准数据集上的实验表明，方法在达到当前最优新视角合成质量的同时，仅使用约一个数量级更少的高斯原语。

### 局限性
摘要未提供足够信息（未提及失败案例、计算开销、锚点数量上限、对特定场景类型的适用性限制等）。

### 阅读优先级
**高**。理由：该工作针对前馈式 3DGS 中“原语数量与输入耦合”这一明确痛点，提出信息熵引导的锚点表示，并声称在显著减少高斯原语数量的同时达到 SOTA 新视角合成质量；若结论成立，对高效 3D 重建与渲染方向具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Recent feed-forward 3D Gaussian Splatting (3DGS) methods have enabled effective multi-view 3D reconstruction by predicting Gaussian primitives in a single forward pass. However, existing approaches predominantly adopt a pixel-aligned paradigm that predicts one Gaussian per input pixel, coupling the Gaussian count to the input resolution and number of views. This also leads to redundant primitives in textureless regions and insufficient coverage in geometrically complex areas. We present Anchor3DGS, a pose-free feed-forward 3DGS framework that replaces pixel-aligned prediction with a compact anchor-based representation. Guided by information entropy, our method places a set of 3D anchors in the scene, concentrating them in regions of higher visual complexity while maintaining broad spatial coverage. Each anchor performs occlusion-aware aggregation of multi-view image features, exchanges information with other anchors, and is decoded into a set of local Gaussians. A lightweight feature enhancement module further refines the coarse RGB output from Gaussian splatting and improves rendering fidelity. Extensive experiments on diverse benchmark datasets demonstrate that our Anchor3DGS achieves state-of-the-art novel view synthesis quality while only using an order of magnitude fewer Gaussian primitives.

</details>

#### 2026-10-15 - Training-Free Target-Aware Refinement of 3D Gaussian Language Map

**Authors:** Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
**Links:** [abs](https://arxiv.org/abs/2610.21619) - [pdf](https://arxiv.org/pdf/2610.21619)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, splatting, robotics, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Training-Free Target-Aware Refinement of 3D Gaussian Language Map
- 作者：Sibaek Lee, Kyeongsu Kang, Seongbo Ha, Yewon Jeon, Joonyeol Choi, Daegeol Ko, Jaehyuk Hur, Taemin Choi, Minsu Kim, Hyungjoo Ahn, Wonsok Yoo, Hyeonwoo Yu
- 出版日期：2026-10-15T10:00:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21619 ；PDF：https://arxiv.org/pdf/2610.21619

### 一句话总结
提出一种无需训练、面向指定目标的三维高斯语言地图精修方法，在保留开放词汇查询能力的同时，提高用户指定目标的定位与分割可靠性。

### 研究问题
将视觉—语言特征蒸馏到 3D Gaussian Splatting 后可得到可用任意文本查询的语言地图，但在实际部署中，当前蒸馏地图往往难以可靠定位一小部分用户指定目标，同时又必须保持对其他词的开放词汇查询能力。因此，问题在于：如何在不重新训练、且不破坏通用查询能力的前提下，对已蒸馏语言地图进行目标感知精修。

### 核心思路/方法
方法是对已蒸馏语言地图进行无需训练的目标感知精修。由可文本提示的分割器引导，在每个检测到的目标区域内，将视觉嵌入与目标文本嵌入进行混合，采用凸组合，其系数决定注入先验的强度；非目标区域保持不变。由于注入过多会覆盖外观线索并影响通用查询能力，方法为每个目标寻找仍能使其“胜出”的最小系数，并以闭式解获得所有系数，从而无需调参。作者还指出语言目标定位中的一种注入失败模式：文本嵌入共享共同分量，注入后会使标准余弦读出变得与查询无关，而在读出中加入中心化步骤可消除该问题。

### 主要贡献
- 提出一种无需训练、目标感知的三维高斯语言地图精修方法。
- 通过凸组合将目标文本嵌入注入检测到的目标区域，并为每个目标以闭式解求取最小注入系数，避免超参数调优。
- 识别出注入文本嵌入导致语言目标定位中标准余弦读出与查询无关的失败模式，并通过读出中的中心化步骤解决。
- 在三个基准上持续提升开放词汇分割，在 Replica 上约为基线 mIoU 的两倍，并比基础地图更可靠地定位语言目标。
- 该方法可作为插件迁移到现成的基于场和对象级的语言地图，并支持四足机器人导航到自然语言目标的真实世界演示。

### 局限性
摘要未提供足够信息。摘要未说明方法在哪些具体场景下会失效、对分割器质量的依赖程度、计算开销、基准细节、失败案例范围以及真实世界演示的具体限制。

### 阅读优先级
中。理由：论文关注 3D Gaussian Splatting 语言地图在部署中的目标定位可靠性，提出无需训练、无超参数的精修方案，并涉及开放词汇分割与机器人导航演示，方向具有实用性；但摘要未提供足够实验细节与局限分析，是否值得深入阅读取决于读者对 3D 语言地图、开放词汇查询或机器人导航的具体兴趣。

</details>

<details>
<summary>Abstract</summary>

Distilling vision-language features into 3D Gaussian Splatting yields a language map that can be queried with arbitrary text. In deployment, however, a small set of user-specified targets must be reliably located, which current distilled maps often miss, while open-vocabulary queryability for other words must remain intact. We propose a training-free, target-aware refinement of an already-distilled language map. Guided by a text-promptable segmenter, the visual embedding inside each detected target region is blended with the target text embedding, a convex combination whose coefficient sets the amount of injected prior, while non-target regions are left untouched. Injecting too much overwrites appearance cues and general queryability, so we seek, for each target, the smallest coefficient that still lets it win, and we obtain every coefficient in closed form, leaving no hyperparameters to tune. We further identify a failure mode of injection in language-goal localization. Text embeddings share a common component, and injecting them makes the standard cosine read-out query-agnostic, which a centering step in the read-out removes. Across three benchmarks, the refinement consistently improves open-vocabulary segmentation, roughly doubling the base mIoU on Replica, and localizes language goals more reliably than the base map. It also transfers as a plug-in to off-the-shelf field-based and object-level language maps and supports a real-world demonstration in which a legged robot navigates to natural-language goals. Project page and code: https://lab-of-ai-and-robotics.github.io/target-aware-langmap/

</details>

#### 2026-10-15 - ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming

**Authors:** Haoran Liu, Di Wu, Wang Luo, Hengyuan Na, Miao Hu, Guocong Quan
**Links:** [abs](https://arxiv.org/abs/2610.21121) - [pdf](https://arxiv.org/pdf/2610.21121)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ResStreamGS: Residual-Sensitive Dual-Stream Gaussian Splatting for Mobile Volumetric Video Streaming
- 作者：Haoran Liu, Di Wu, Wang Luo, Hengyuan Na, Miao Hu, Guocong Quan
- 出版日期：2026-10-15T02:25:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.21121 ；PDF：https://arxiv.org/pdf/2610.21121

### 一句话总结
ResStreamGS 针对移动体积视频流中“所有高斯点都按帧变化编码”不适配全场景内容的问题，提出按高斯点时间行为分流的双流框架，将稳定高斯点按 GOP 复用、仅对残差敏感高斯点进行逐帧视频编码传输。

### 研究问题
实时移动体积视频需要沉浸式自由视角体验，但在带宽和计算受限条件下高质量 3D 内容传输仍然困难。现有 3D Gaussian Splatting 流式系统（如 V³）通过视频编解码器与硬件解码传输随时间变化的高斯属性，但将全部高斯点都视为逐帧变化信号，不适合包含大量时间稳定区域的全场景内容。摘要指出，逐帧适配并编码所有高斯点会导致复杂全场景内容的质量退化，尤其是在时间稳定区域。

### 核心思路/方法
- 根据高斯点的时间行为进行处理，提出残差敏感的双流框架。
- 通过轻量级探针适配识别残差敏感基元。
- 在每个 Group of Pictures（GOP）内复用稳定高斯点。
- 稳定高斯点每个 GOP 只传输一次。
- 仅残差敏感高斯点保留在逐帧、可硬件解码的视频流中。

### 主要贡献
- 提出 ResStreamGS，一种残差敏感双流高斯泼溅框架，用于移动体积视频流。
- 通过轻量级探针适配识别残差敏感基元，并在 GOP 内复用稳定高斯点。
- 将传输拆分为 GOP 级稳定高斯点与逐帧硬件可解码的残差敏感高斯点视频流。
- 在复杂全场景体积视频实验中，相比受控的 V³ 风格全高斯基线，编码后 PSNR 提升 7.51–8.35 dB，摊销负载最多降低 56.5%，并在 Qualcomm Snapdragon 778G 平台上达到 30.883 FPS。

### 局限性
摘要未提供足够信息。摘要未说明探针适配的具体开销、不同场景类型下的泛化性、在更高移动性或动态内容中的表现、端到端延迟与能耗细节，也未提供与更多现有方法的完整对比。

### 阅读优先级
高。理由：该工作直接面向移动体积视频流的关键瓶颈，提出明确的双流传输机制，并在摘要中报告了显著的 PSNR、负载和端侧帧率指标；对 3DGS 流式传输、移动端实时渲染与体积视频编码方向具有较强相关性。

</details>

<details>
<summary>Abstract</summary>

Real-time mobile volumetric video enables immersive free-viewpoint experiences, but delivering high-quality 3D content under constrained bandwidth and computation remains challenging. Recent 3D Gaussian Splatting (3DGS) systems, such as V$^3$, enable efficient mobile streaming by encoding time-varying Gaussian attributes with commodity video codecs and hardware decoding. However, existing pipelines treat all Gaussians as frame-varying signals, which is poorly suited to full-scene content where large portions remain temporally stable. Our empirical study shows that frame-wise adaptation and video coding of all Gaussians cause quality degradation in complex full-scene content, particularly in temporally stable regions. To address this issue, we propose ResStreamGS, a residual-sensitive dual-stream framework that processes Gaussians according to their temporal behavior. ResStreamGS identifies residual-sensitive primitives through lightweight probe adaptation and reuses stable Gaussians within each Group of Pictures (GOP). Stable Gaussians are transmitted once per GOP, while only residual-sensitive Gaussians remain in the frame-wise hardware-decodable video stream. Experiments on complex full-scene volumetric videos show that ResStreamGS improves post-codec PSNR by 7.51--8.35~dB over a controlled V$^3$-style all-Gaussians baseline, reduces amortized payload by up to 56.5%, and achieves 30.883~FPS on a Qualcomm Snapdragon 778G platform.

</details>

#### 2026-10-14 - Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting

**Authors:** Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo, Tae-Gwon Park, Hui Yong Kim
**Links:** [abs](https://arxiv.org/abs/2610.20590) - [pdf](https://arxiv.org/pdf/2610.20590)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Feed-Forward Multi-View Feature Coding for 3D Gaussian Splatting
- 作者：Seungmi Choi, Ji-Hyoun Choi, Suhyun Jo, Tae-Gwon Park, Hui Yong Kim
- 出版日期：2026-10-14T17:58:28Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2610.20590

### 一句话总结
本文提出 MFGS，一种端到端前馈的多视角特征编码框架，通过直接编码多视角特征而非显式高斯表示，联合表示几何与外观，从而提升 3DGS 场景编码的率失真性能并降低计算开销。

### 研究问题
现有前馈 3DGS 场景编码流程通常先“生成完整高斯表示”，再分别编码其几何与外观属性，往往包含不可微操作。这种“先生成后压缩”的管道需要复杂的属性专用编解码器设计，并且由于限制了跨属性冗余的利用，率失真性能受到制约。论文旨在解决这一编码流程复杂、性能受限的问题。

### 核心思路/方法
MFGS 不再压缩显式高斯表示，而是从输入图像中提取多视角特征，并将其编码为紧凑比特流。通过端到端的率失真训练，MFGS 学习能够联合表示几何与外观的紧凑多视角特征，接收端则从解码后的特征预测高斯属性。此外，论文引入重要性引导的高斯选择，以适应不同渲染预算，使接收端能够从同一比特流中调整用于渲染的高斯数量。

### 主要贡献
- 提出 MFGS，一种端到端前馈的场景编码框架，直接编码多视角特征而非显式高斯表示。
- 通过端到端率失真训练，学习联合表示几何与外观的紧凑多视角特征，接收端可据此预测高斯属性。
- 引入重要性引导的高斯选择，支持从同一比特流调整渲染所需高斯数量，以适应不同渲染预算。
- 在 RE10K、ACID 和 DL3DV 上，按 BD-rate 衡量，相比“先生成后压缩”管道实现 99.76–99.86% 的比特率节省，同时总 GMACs 降低 52–55%，并提供约 12 倍的端到端加速。

### 局限性
摘要未提供足够信息。摘要未说明方法在特定场景类型、极端稀疏视角、训练数据规模或泛化能力方面的限制，也未提供失败案例或消融实验的负面结果。

### 阅读优先级
高。理由：该论文针对前馈 3DGS 场景编码中“先生成后压缩”管道的关键瓶颈提出端到端替代方案，报告了显著的比特率节省、计算量降低和速度提升，且涉及跨属性冗余利用与可变渲染预算，属于神经场景表示与渲染方向中较有潜力的工作。

</details>

<details>
<summary>Abstract</summary>

Feed-forward 3D Gaussian Splatting (3DGS) methods enable efficient reconstruction of 3D scenes from sparse multi-view images in a single forward pass, without scene-specific optimization. However, existing feed-forward scene-coding pipelines first generate a complete Gaussian representation and then encode its geometry and appearance attributes separately, often involving non-differentiable operations. The resulting 'generate-then-compress' pipeline requires complex attribute-specific codec designs and limits rate-distortion performance by restricting the exploitation of cross-attribute redundancy. We propose multi-view feature coding for Gaussian splatting (MFGS), an end-to-end feed-forward framework for scene coding. Instead of compressing an explicit Gaussian representation, MFGS extracts multi-view features from the input images and encodes them into a compact bitstream. Through end-to-end rate-distortion training, MFGS learns compact multi-view features that jointly represent geometry and appearance, enabling the receiver to predict Gaussian attributes from the decoded features. We further introduce importance-guided Gaussian selection to accommodate different rendering budgets, allowing the receiver to adjust the number of Gaussians used for rendering from the same bitstream. Across RE10K, ACID, and DL3DV, MFGS achieves 99.76-99.86% bitrate savings over the generate-then-compress pipeline, as measured by BD-rate, while reducing total GMACs by 52-55% and providing an approximately 12 times end-to-end speedup.

</details>

## Embodied / Robotics / AR Applications

### 2026-10

#### 2026-10-20 - MindView: Benchmarking Generative Multi-View Spatial Intelligence

**Authors:** Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu, Tai Wang, Yu Qiao, Yihao Liu, Jiwen Lu
**Links:** [abs](https://arxiv.org/abs/2610.28622) - [pdf](https://arxiv.org/pdf/2610.28622)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>Abstract</summary>

Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while semantics-dominant tasks require inferring target viewpoints by grounding referred objects and interpreting spatial relations and reference-frame cues. Evaluation of eleven generators reveals substantial room for improvement on MindView. A paired context analysis further shows that all eleven generators obtain lower overall scores under the expanded context setting. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis. MindCue reverses the drop in overall score under expanded context and outperforms the standard-context baseline. Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.

</details>

#### 2026-10-20 - CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding

**Authors:** Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan
**Links:** [abs](https://arxiv.org/abs/2610.28530) - [pdf](https://arxiv.org/pdf/2610.28530)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>Abstract</summary>

Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Gaussian-based collaborative semantic occupancy prediction framework. CoGaussian represents a scene as a set of foundation model-aligned sparse 3D Gaussians, which serve as a compact representation for communicating and fusing geometric and semantic information across multiple agents. On the Semantic-OPV2V benchmark, our method outperforms existing open-vocabulary single-agent approaches, highlighting the effectiveness of open-vocabulary collaborative scene understanding.

</details>

#### 2026-10-20 - Decoupling Action from Egocentric Observation for World Simulation

**Authors:** Yue Ma, Pengjie Song, Xinyu Wang, Yi He, Zeqian Long, Fangneng Zhan, Kaichen Zhou, Hongyu Liu, Hongfa Wang, Peihao Li, Haoyang Huang, Nan Duan, Qifeng Chen
**Links:** [abs](https://arxiv.org/abs/2610.27946) - [pdf](https://arxiv.org/pdf/2610.27946)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>Abstract</summary>

Egocentric action transfer aims to decouple the semantic action from egocentric observations and reproduce them in new visual contexts, enabling scalable world simulation, embodied policy learning, and robotic data generation. Existing approaches to transferring actions rely on condition-guided video generation, which converts the observation video into explicit geometric controls (e.g., hand poses or meshes) to drive synthesis. However, these methods introduce geometric estimation errors, making it difficult to preserve physically plausible interactions when transferred to new scenes. Alternatively, motion transfer methods directly extract motion patterns from the observation video, yet motion-level features alone cannot encode rich contact dynamics, frequently leading to severe hand structural collapse and implausible contact layout. To address both limitations, we present EgoACT, a test-time framework for egocentric action transfer that operates directly on the denoising process of video diffusion models without requiring additional geometric estimators. EgoACT uses Velocity-guided Structure Anchoring to stabilize reference-consistent hand-object structure in the early denoising stage, and Sparse Correspondence Calibration to refine reliable local correspondences in the mid-to-late denoising stages. Together, these two components preserve transferable action semantics while improving temporal coherence and interaction realism. We further establish EgoActionBench, a benchmark for evaluating action preservation, visual quality, and hand-object plausibility across diverse egocentric manipulation scenarios. Experiments show that EgoACT generates more coherent and physically plausible interaction videos than strong baselines.

</details>

#### 2026-10-20 - VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement

**Authors:** Ruoyu Wang, Jiahan Li, Yong Liu, Kexin Zhang
**Links:** [abs](https://arxiv.org/abs/2610.27704) - [pdf](https://arxiv.org/pdf/2610.27704)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene representation, mapping, scene understanding

<details>
<summary>Abstract</summary>

Semantic occupancy mapping supports embodied perception during exploration and detailed scene understanding afterward, giving rise to two complementary requirements: online incremental mapping for maintaining an up-to-date global map under causal constraints, and offline global map refinement for improving the completed scene representation with additional computation. We present VEOcc++, a unified voxel-centric framework that connects both stages through a persistent sparse voxel feature map. During exploration, the map expands with newly observed regions and integrates aligned local features through reliability-guided updates, while context-aware decoding produces the current semantic occupancy map. After exploration, cached local features are consolidated as complementary evidence and combined with the completed online representation for multi-scale spatial refinement. On EmbodiedOcc-ScanNet, VEOcc++ achieves 67.12\% IoU and 58.40\% mIoU, establishing new state-of-the-art performance for online incremental mapping. With the local predictor fixed, our online mapping pipeline outperforms VEOcc fusion by 3.70 IoU and 3.74 mIoU points, demonstrating substantial gains from the proposed global mapping design. Offline global map refinement further improves the completed map to 67.79% IoU and 59.37% mIoU using only the observations acquired during exploration. Zero-shot deployment on a mobile robot further demonstrates transferability to unseen environments, onboard feasibility, and scalability to large-scale indoor mapping. Project page: https://wryzju.github.io/VEOccpp/.

</details>

#### 2026-10-20 - Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving

**Authors:** Tingxu Han, Zijie Shen, An Guo, Lyuke Wang, Chunrong Fang, Zhenyu Chen, Wei Song
**Links:** [abs](https://arxiv.org/abs/2610.27617) - [pdf](https://arxiv.org/pdf/2610.27617)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving

<details>
<summary>Abstract</summary>

LiDAR-based 3D object detection is a core perception service for autonomous driving, but deployment requires robustness to point-cloud corruption while meeting latency and memory requirements. Existing approaches address robustness and resource efficiency separately, resulting in compact detectors that are fragile under corruption or robust detectors that remain costly to deploy. We therefore formulate LiDAR perception provisioning as constructing a detector that remains accurate under point-cloud corruptions while meeting constraints on inference latency and peak GPU memory. To achieve robustness, we first craft corrupted samples that mimic extreme weather conditions. Then we train candidate detectors offline by ordering clean and corrupted samples by perturbation sensitivity, through which detectors learn more from hard corrupted samples. We estimate perturbation sensitivity using an ensemble of seven heterogeneous 3D detectors by tracking changes in confidence, BEV overlap, and unmatched detections. To improve efficiency, we narrow the network and use offline neighborhood-density measurements to determine how many points and neighbors each sampling stage processes. We evaluate our method using AP (Average Precision) under clean and corrupted conditions, inference latency, and peak allocated GPU memory. On KITTI for Car detection with PointRCNN, our method improves Moderate AP under corruption by 3.32 points over the original detector while reducing mean latency by 19.8% and peak allocated GPU memory by 53.9%. Across two datasets, two detector architectures, and three object classes, our method improves AP under corruption by 4.03 points on average over the corresponding original detectors, while reducing mean inference latency and peak allocated GPU memory by 14.4% and 38.0%, respectively. Our code is available at https://github.com/drunklibai/robust-efficient-lidar-perception.

</details>

#### 2026-10-19 - Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware

**Authors:** Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
**Links:** [abs](https://arxiv.org/abs/2610.26759) - [pdf](https://arxiv.org/pdf/2610.26759)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Tactile In-Hand Object Rotation: A Comparative Study of Hand Morphology in Simulation and Hardware
- 作者：Wenhao He, Max Yang, Chenghua Lu, Yijiong Lin, David A. W. Barton, Nathan F. Lepora
- 出版日期：2026-10-19T17:18:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.26759 ；PDF https://arxiv.org/pdf/2610.26759

### 一句话总结
该论文比较两种低成本 LEAP Hand 手指布局（拟人化与对称式）在配备 TacTip 视触觉传感器、共享强化学习框架下的在手物体连续旋转表现，并结合仿真与硬件实验分析触觉信息、手指参与度和指尖载荷之间的关系。

### 研究问题
论文关注连续在手旋转中接触维持与接触更新如何协调，并探究手部几何结构（手指排布）与触觉反馈分别如何影响操作表现。具体比较拟人化与对称式手指布局在旋转进展、手指参与和指尖载荷上的差异，同时考察不同触觉观测条件对仿真任务表现的影响。

### 核心思路/方法
- 使用两种版本的 LEAP Hand：拟人化手指布局与对称式手指布局。
- 两种手均集成 TacTip 视触觉传感器，并采用共享的强化学习框架。
- 仿真中在 12 个未见物体上评估三种观测条件：完整触觉、二值接触、仅本体感觉。
- 硬件实验中在 10 个物体、多种手部朝向下评估完整触觉策略。
- 分析指标包括旋转进展、手指参与度、指尖载荷与操作持续时间；硬件中还记录接触测量与力数据。

### 主要贡献
- 在仿真中显示，完整触觉观测相比仅本体感觉可提高每回合平均归一化旋转量：拟人化手提高 94.8%，对称手提高 66.9%，同时平均回合持续时间更长、平均总指尖载荷更低。
- 硬件接触测量显示，拟人化手的手指参与更差异化，而对称手各手指的累积载荷分布更均匀。
- 报告对称手取得更高的平均旋转次数（高 32.0%）、更高的总体旋转速率（高 25.8%）以及更长操作持续时间。
- 额外硬件力记录显示，该对称布局的平均总指尖载荷低 19.9%。
- 将手指排布与接触组织、载荷分担联系起来，并表明更丰富的触觉信息在两种仿真本体上均支持更大的任务进展与更低的平均载荷。

### 局限性
- 摘要未提供足够信息说明仿真中不同触觉观测条件在硬件上的对应验证范围；硬件实验主要评估完整触觉策略。
- 摘要未提供足够信息说明 12 个未见物体与 10 个硬件物体的具体类别、形状分布或难度划分。
- 摘要未提供足够信息说明强化学习框架的网络结构、训练细节、奖励设计及统计显著性检验。
- 摘要未提供足够信息说明 TacTip 传感器的具体配置、校准方式及硬件力测量的完整实验协议。
- 摘要未提供足够信息说明不同手部朝向对结果的单独影响，以及仿真与硬件结果差异的系统性原因。

### 阅读优先级
中。理由：该论文涉及触觉感知、手部形态与强化学习在手内旋转中的比较研究，主题对具身操作与触觉机器人研究者有参考价值；摘要给出了明确的定量比较结果，但未提供实验细节与统计信息。若关注低成本触觉手、手指布局设计或仿真到硬件比较，可优先阅读；若仅需一般性了解，摘要已覆盖主要结论。

</details>

<details>
<summary>Abstract</summary>

Continuous in-hand rotation requires coordinated contact maintenance and renewal, linking manipulation performance to both hand geometry and tactile feedback. We investigate these relationships through rotational progress, finger participation, and fingertip loading on two versions of the low-cost LEAP Hand with anthropomorphic and symmetric finger arrangements. Both hands are integrated with TacTip vision-based tactile sensors and use a shared reinforcement learning framework. Simulation evaluates full tactile, binary touch, and proprioception-only observations on 12 unseen objects; hardware experiments evaluate full tactile policies on ten objects under multiple hand orientations. In simulation, full tactile observations increase mean normalized rotation per episode over proprioception alone by 94.8% for the anthropomorphic hand and 66.9% for the symmetric hand, with longer mean episode durations and lower mean total fingertip loads. Hardware contact measurements reveal more differentiated finger participation in the anthropomorphic hand, while cumulative loading is more evenly distributed across the symmetric hand's fingers. Overall, the symmetric hand achieves a 32.0% higher mean rotation count and a 25.8% higher aggregate rotation rate, together with longer manipulation duration. Additional hardware force recordings show a 19.9% lower mean total fingertip load for this layout. These findings relate finger arrangement to contact organization and load sharing, and show that richer tactile information supports greater task progress at lower mean loading in both simulated embodiments.

</details>

#### 2026-10-19 - Robot Learning with Vision-Language-Action Models for Agricultural Manipulation

**Authors:** Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
**Links:** [abs](https://arxiv.org/abs/2610.26717) - [pdf](https://arxiv.org/pdf/2610.26717)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Robot Learning with Vision-Language-Action Models for Agricultural Manipulation
- 作者：Hamid Hafezi, Javad Mohammadpour Velni, Mohammadreza Davoodi
- 出版日期：2026-10-19T16:49:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.26717) / [PDF](https://arxiv.org/pdf/2610.26717)

### 一句话总结
该论文构建了一个面向农业到达与抓取任务的仿真到真实机器人学习框架，先在基于 MuJoCo 的农业仿真环境中采集专家演示，并对 Octo 与 π_{0.5} 两个预训练通用机器人策略进行适配，随后在真实 Franka Research 3 机械臂上进一步微调与评估。

### 研究问题
论文关注农业机器人操作中的困难：植物几何结构变化、遮挡以及相机视角变化。预训练视觉-语言-动作（VLA）模型和通用机器人策略有望通过多模态观测与语言指令学习操作行为来应对这些挑战，但将其适配到农业任务需要领域特定演示，而在真实机器人上采集这些演示成本高、耗时长。因此，论文研究如何通过仿真到真实的机器人学习框架，将预训练通用策略适配到农业到达与抓取任务。

### 核心思路/方法
论文提出一个面向农业到达与抓取的仿真到真实机器人学习框架，整合任务特定演示采集与预训练策略适配。具体包括：
- 构建基于 MuJoCo 的农业环境，包含多样化的番茄植株结构，用于支持演示采集与受控评估；
- 通过操纵杆遥操作采集专家演示，并使用低层控制器执行机器人动作；
- 使用仿真演示对两个预训练通用机器人策略 Octo 和 π_{0.5} 进行适配；
- 随后在真实 Franka Research 3 机械臂上使用真实机器人演示进一步微调；
- 在仿真中评估适配策略在分布内、视角/空间偏移和分布外条件下的表现，并进行真实机器人实验；
- 还研究了本体感知信息对策略性能的影响。

### 主要贡献
- 提出了一个用于农业到达与抓取的仿真到真实机器人学习框架，结合任务特定演示采集与预训练策略适配；
- 开发了基于 MuJoCo 的农业环境，包含多样化番茄植株结构，支持演示采集与受控评估；
- 将 Octo 和 π_{0.5} 两个预训练通用机器人策略适配到农业操作任务，并在仿真与真实 Franka Research 3 机械臂上进行评估；
- 比较了两种策略在分布内、视角/空间偏移和分布外条件下的表现，并考察了本体感知信息对策略性能的影响；
- 摘要报告的结果显示，π_{0.5} 的任务性能得分高于 Octo，且在分布偏移下退化更小。

### 局限性
- 摘要仅提到在仿真中评估分布内、视角/空间偏移和分布外条件，并进行了真实机器人实验，但未提供真实机器人实验的具体规模、任务数量或统计细节；
- 摘要未提供演示采集数量、训练时长、硬件配置、评估指标定义等实验细节；
- 摘要未说明该方法在更广泛农业任务、不同作物或更复杂自然环境中的泛化能力；
- 摘要未提供失败案例分析或方法在真实农业场景中部署的限制；
- 摘要未提供足够信息说明仿真环境与真实环境之间的差距及其对结果的具体影响；
- 其他未在摘要中提及的实验细节、消融设置和定量结果：摘要未提供足够信息。

### 阅读优先级
中。理由：该论文聚焦于 VLA/通用机器人策略在农业操作中的仿真到真实适配，问题明确且与农业机器人操作相关；摘要给出了框架、策略比较和主要结果，但未提供详细实验数据与真实部署规模。对于关注机器人学习、VLA 策略适配和农业操作的研究者具有参考价值；若需要具体实验细节或复现信息，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Robotic manipulation in agricultural environments remains challenging due to variations in plant geometry, occlusion, and camera viewpoints. Pretrained vision-language-action (VLA) and generalist robot policies offer a promising approach to addressing these challenges by learning manipulation behaviors from multimodal observations and language instructions. However, adapting these policies to agricultural tasks requires domain-specific demonstrations, which are costly and time-consuming to collect on physical robots. In this work, we develop a simulation-to-real robot-learning framework for agricultural reaching and grasping that integrates task-specific demonstration collection and pretrained policy adaptation. A MuJoCo-based agricultural environment is developed with diverse tomato plant structures to support demonstration collection and controlled evaluation. Expert demonstrations are collected through joystick teleoperation, with a low-level controller used to execute robot actions. Two pretrained generalist robot policies, Octo and $π_{0.5}$, are adapted using simulated demonstrations, followed by further fine-tuning on a physical Franka Research 3 manipulator using real-robot demonstrations. The adapted policies are evaluated under in-distribution, viewpoint/spatial-shift, and out-of-distribution conditions in simulation, followed by physical-robot experiments. The influence of proprioceptive information on policy performance is also investigated. Results show that $π_{0.5}$ achieves higher task-performance scores than Octo and exhibits less degradation under distribution shifts. These findings demonstrate the potential of integrating pretrained generalist policies with task-specific demonstration learning for agricultural manipulation.

</details>

#### 2026-10-19 - ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds

**Authors:** Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
**Links:** [abs](https://arxiv.org/abs/2610.26395) - [pdf](https://arxiv.org/pdf/2610.26395)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** embodied AI, robotics, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ForagerSim: Evaluating Embodied Map-Based Reasoning in Large-Scale Dynamic Worlds
- 作者：Tomáš Musil, Martin Kotík, Michal Vavrečka, Karla Štěpánová, Sebastian Scherer, Martin Saska
- 出版日期：2026-10-19T13:40:47Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.26395

### 一句话总结
论文提出 ForagerSim，一个用于评估具身智能体在大规模动态世界中进行“基于地图的推理”的跨学科仿真平台，并通过对比强化学习基线、工程化机器人栈和人类玩家，指出复杂场景中地图式推理可能是性能瓶颈。

### 研究问题
当前具身 AI 系统要么依赖手工设计的建图流程（在未建模动态下易失效且局限于度量空间），要么依赖很少形成地图式表示的学习策略；同时，缺少真正要求“基于地图推理”的具身 AI 基准，导致难以发展能像动物一样灵活构建和使用地图式表示的架构。论文试图提供这样的评估环境。

### 核心思路/方法
ForagerSim 是一个高度模块化的研究平台与仿真环境，聚焦需要地图式推理的具身任务，场景覆盖移动机器人搜救、复杂迷宫与广阔甚至可能无限的开放区域中的动物觅食等。平台允许独立调节多个难度轴：感知（从抽象 2D 感知到完整 RGB 或 LiDAR）、尺度（房间级到多公里级）、拓扑（开放场地到复杂迷宫）、动态（烟雾、碎片、感知运动故障等）以及任务（从简单 2D 覆盖到受觅食启发的井交替任务）。论文在 8 个示例世界上比较了强化学习基线、简单工程化机器人栈和人类玩家，以观察不同难度轴对现有方法的影响。

### 主要贡献
- 提出 ForagerSim：一个面向“基于地图推理”的具身任务仿真平台，具有跨学科定位。
- 提供多维度可独立调节的难度设计，涵盖感知、尺度、拓扑、动态和任务。
- 在 8 个示例世界上对比强化学习基线、工程化机器人栈与人类玩家，分析不同难度轴对方法表现的影响。
- 报告发现：当感知简化为 2D 时，学习策略在简单拓扑中的多目标搜索和井交替任务上表现 surprisingly well，但在更大或拓扑更复杂的环境中低于人类表现，而基于地图的基线表现良好，提示地图式推理是这些场景的瓶颈。

### 局限性
摘要未提供足够信息说明具体实验规模、统计显著性、各难度轴的系统消融细节、工程化机器人栈与人类玩家的具体配置，以及平台在真实机器人上的部署验证情况。摘要也未提供足够信息说明 ForagerSim 的开源许可、计算开销与可复现性细节。

### 阅读优先级
中。理由：该工作与具身 AI、机器人导航和地图式表示学习评估直接相关，且明确指出现有学习策略在复杂拓扑和大尺度场景中的瓶颈，对基准设计有参考价值；但摘要仅给出 8 个示例世界的对比结果，缺少更细的实验与可复现信息，需阅读全文后才能判断其方法深度与结论稳健性。

</details>

<details>
<summary>Abstract</summary>

Animals build cognitive maps of vast environments, use them to perform map-based navigation, and might even be reusing the same circuitry used in spatial reasoning for creating and using maps of arbitrary task-spaces. In contrast, current embodied AI systems either rely on hand-engineered mapping pipelines, which break in the presence of unmodeled dynamics and are restricted to metric space, or on learned policies that rarely form map-like representations at all. Developing architectures that could learn to build and use map-like representations as flexibly as animals is, however, difficult because few embodied AI benchmarks actually require map-based reasoning. To address this, we present ForagerSim --- an interdisciplinary research platform and simulation environment focused on embodied tasks that require map-based reasoning, with scenarios ranging from mobile-robot search and rescue to animal foraging in both complex mazes and vast, potentially infinite open areas. ForagerSim is highly modular and allows modifying independent axes of difficulty related to perception (abstract 2D sensing to full RGB or LiDAR), scale (room-scale to multi-km scale), topology (open-fields to complex mazes), dynamics (smoke, debris, sensorimotor failures and others) and tasks (from simple 2D coverage to foraging-inspired well-alternation tasks). We compare reinforcement learning baselines with a simple engineered robotics stack and a human player on 8 example worlds which show how different difficulty axes affect existing methods. Our results show that, when sensing is simplified to 2D, learned policies can perform multi-object search and well-alternation tasks surprisingly well in simple topologies, but they fall short of human performance in larger or more complex-topology environments where map-based baselines perform well, suggesting that map-based reasoning is the bottleneck in these scenarios.

</details>

#### 2026-10-19 - Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving

**Authors:** Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
**Links:** [abs](https://arxiv.org/abs/2610.25734) - [pdf](https://arxiv.org/pdf/2610.25734)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Think Densely, Act Sparsely: Latent Expert Cognitive Chains for Vision-Language-Action Autonomous Driving
- 作者：Jie Wang, Guang Li, Zhijian Huang, Jinlong Li, Chenxu Dang, Hangjun Ye, Yahong Han, Long Chen
- 出版日期：2026-10-19T03:37:38Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要页 https://arxiv.org/abs/2610.25734 ；PDF https://arxiv.org/pdf/2610.25734

### 一句话总结
论文提出“Think Densely, Act Sparsely”的驾驶智能范式及 LECDrive 框架，通过在 VLA 模型内嵌入由任务特定潜在 token 承载的渐进式“潜在专家认知链”，让模型在保持高效推理的同时内化稠密视觉、语义与几何知识。

### 研究问题
现有 Vision-Language-Action（VLA）自动驾驶模型通常以稀疏监督（如语言指令或轨迹信号）训练，而自动驾驶本质上需要稠密理解视觉、语义和几何信息。摘要指出，从稠密视觉观察到稀疏表示的直接映射会迫使模型压缩甚至丢弃对安全驾驶至关重要的场景信息。作者认为该限制并非源于模型容量不足，而是缺乏显式机制来鼓励在潜在空间中形成稠密世界表示。

### 核心思路/方法
论文提出“Think Densely, Act Sparsely”范式，并实例化为 LECDrive 框架。其核心是模仿人类分层感知过程，在 VLA 模型中嵌入一条渐进式的潜在专家认知链。具体而言，方法注入一小组任务特定的潜在 token 作为载体，使模型能够从基础视觉模型内化稠密知识，包括视觉表示（DINOv3）、语义结构（SAM3）和空间几何（DepthAnything3），同时保持高效推理。该相互依赖的认知链遵循课程学习原则，监督信号从表示到语义再到几何逐步结构化。

### 主要贡献
- 提出“Think Densely, Act Sparsely”的驾驶智能范式，主张通过显式机制在潜在空间中构建稠密世界表示，而非仅依赖稀疏监督的直接映射。
- 提出 LECDrive 框架，将渐进式潜在专家认知链嵌入 VLA 模型，并以任务特定潜在 token 作为载体，内化来自 DINOv3、SAM3、DepthAnything3 的视觉、语义和几何知识。
- 设计遵循课程学习原则的监督结构，使认知链从表示到语义再到几何逐步组织，并强调保持高效推理。
- 摘要称大量实验表明 LECDrive 在多个自动驾驶基准上持续提升基础 VLM 的性能，覆盖物体感知、状态预测和轨迹规划等关键任务。

### 局限性
- 摘要未提供足够信息说明具体实验设置、数据集规模、基线细节和定量结果。
- 摘要未提供足够信息说明潜在 token 的数量选择、课程学习各阶段的具体监督形式及训练成本。
- 摘要未提供足够信息说明“高效推理”的具体效率指标或与其它方法的计算开销对比。
- 摘要未提供足够信息说明方法在不同基础 VLM 或不同驾驶场景下的泛化边界与失败案例。

### 阅读优先级
中。理由：该论文针对 VLA 自动驾驶中“稠密感知与稀疏监督”的矛盾提出明确范式，方法思路清晰，且涉及视觉、语义、几何三类基础模型知识的潜在空间整合，与具身智能/机器人视觉语言动作方向相关。但当前仅依据摘要，缺少实验细节与定量证据，是否值得深入精读需结合全文的实验充分性与可复现性进一步判断。

</details>

<details>
<summary>Abstract</summary>

Autonomous driving fundamentally demands dense understanding of visual, semantic, and geometric information, yet existing Vision-Language-Action (VLA) models are typically trained with sparse supervision such as language instructions or trajectory signals. This direct mapping from dense visual observations to sparse representations forces the model to compress or even discard critical scene information essential for safe driving. We argue that this limitation does not stem from insufficient model capacity, but from the lack of explicit mechanisms that encourage the formation of dense world representations in the latent space. In this spirit, we propose a novel paradigm for driving intelligence, Think Densely, Act Sparsely, and instantiate it with an efficient and interpretable framework, LECDrive (Latent Expert Cognitive Chains for Vision-Language-Action autonomous Driving). The core idea is to mimic the hierarchical perception process of humans by embedding a progressive chain of latent expert cognition within the VLA model. Concretely, we inject a compact set of task-specific latent tokens as carriers, enabling the model to internalize dense knowledge from foundational vision models, including visual representations (DINOv3), semantic structures (SAM3), and spatial geometry (DepthAnything3), while maintaining efficient inference. This interdependent cognitive chain follows a curriculum learning principle, where supervision is progressively structured from representation to semantics and geometry. Extensive experiments demonstrate that LECDrive consistently improves the performance of base VLMs across multiple autonomous driving benchmarks, covering key tasks such as object perception, state prediction, and trajectory planning. These findings suggest that constructing dense world models through structured latent expert chains is a promising direction for VLA-based autonomous driving.

</details>

#### 2026-10-18 - Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding

**Authors:** Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
**Links:** [abs](https://arxiv.org/abs/2610.25429) - [pdf](https://arxiv.org/pdf/2610.25429)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Preserving the Manifold: Frozen Expert Alignment for Label-Efficient SAR Scene Understanding
- 作者：Eli A. Underwood, I. Taylor McKechnie, Leslie M. Collins
- 出版日期：2026-10-18T17:43:57Z
- 分类：主分类为 Embodied / Robotics / AR Applications；无次级分类
- 链接：[摘要](https://arxiv.org/abs/2610.25429)｜[PDF](https://arxiv.org/pdf/2610.25429)

### 一句话总结
该论文提出一种“冻结专家”框架：保持 SAR 编码器与 CLIP 文本编码器均冻结，只学习一个轻量、受约束且保持结构的残差桥接模块，以缓解 SAR—文本跨模态对齐中的模态失配与“物理遗忘”，并在标签高效设定下提升零样本 SAR 场景分类表现。

### 研究问题
论文指出 SAR 图像与自然语言跨模态对齐面临两类失败：
1. **模态失配**：在光学图像上预训练的文本编码器（如 CLIP）难以高效迁移到 SAR；主动微波后向散射与被动光学反射在物理上不兼容，且现有 SAR 描述数据集规模比所需小几个数量级，难以在不显著破坏已学语义流形的情况下弥合差距。
2. **物理遗忘**：在大规模自监督目标上预训练的 SAR 编码器编码了雷达物理特性，但在有限描述数据上为文本对齐而微调编码器时，这些特性会被逐步抹除。

### 核心思路/方法
- **单一设计原则**：保持两个编码器冻结，仅学习一个受约束、保持结构的桥接模块。
- **Frozen Expert 框架**：将冻结的 CROMA SAR 编码器与冻结的 CLIP 文本编码器通过轻量级“受约束残差桥”对齐。
- **物理遗忘的形式化**：通过 Procrustes disparity 定义物理遗忘，并报告其桥接方法比微调更好地保持 SAR 几何（disparity：0.210 对 0.351）。
- **泛化验证**：摘要称在多种 SAR 骨干与文本编码器上验证了通用性。

### 主要贡献
- 提出冻结双专家、仅学习受约束残差桥的 SAR—文本对齐框架。
- 用 Procrustes disparity 形式化“物理遗忘”，并给出桥接优于微调的几何保持证据。
- 在零样本 SAR 场景分类上，以最多少 8 倍训练数据超过微调基线：
  - DFC2020：+10.3% R@1，+15.5% mAP
  - EuroSAT-SAR：+15.7% R@1，+12.2% mAP
  - BigEarthNet-MM：+14.7% R@1
- 将“冻结流形对齐”定位为高差异跨模态设定下相对微调的原则性、数据高效替代方案。

### 局限性
- 摘要未提供足够信息说明桥接模块的具体结构、参数量与训练细节。
- 摘要未提供足够信息说明各数据集的划分、训练数据规模绝对值、基线配置与统计显著性。
- 摘要未提供足够信息说明方法在非分类任务（如检索、描述生成、分割）上的表现。
- 摘要未提供足够信息说明失败案例、计算开销或对 SAR 成像条件变化的鲁棒性。
- 摘要未提供足够信息说明“物理遗忘”Procrustes disparity 的完整定义与计算协议。

### 阅读优先级
**中**。理由：论文聚焦 SAR—文本跨模态对齐中的模态失配与物理遗忘，提出冻结双编码器加轻量桥接的数据高效方案，并给出零样本分类的量化提升，问题定义清晰、方法原则简洁；但摘要未展开桥接结构、训练细节与更广泛任务验证，是否适合精读取决于读者对 SAR 跨模态对齐、冻结骨干适配或标签高效场景理解的兴趣。

</details>

<details>
<summary>Abstract</summary>

Cross-modal alignment of synthetic aperture radar (SAR) imagery to natural language is constrained by two distinct failures. The first is modality mismatch: text encoders pre-trained on optical imagery, such as CLIP, cannot be efficiently fine-tuned on SAR, because active microwave backscatter is physically incompatible with passive optical reflectance and the available SAR caption datasets are orders of magnitude too small to bridge this gap without substantially degrading the learned semantic manifold. The second is physical forgetting: SAR encoders pre-trained on large-scale self-supervised objectives encode radar physics that are progressively erased when the encoder is fine-tuned for text alignment on limited caption data. A single design principle addresses both failures: keep both encoders frozen and learn only a constrained, structure-preserving bridge. Our Frozen Expert framework aligns a frozen CROMA SAR encoder with a frozen CLIP text encoder via a lightweight constrained residual bridge. We formally define physical forgetting via Procrustes disparity and show our bridge preserves SAR geometry significantly better than fine-tuning (disparity: 0.210 vs. 0.351). We validate generality across multiple SAR backbones and text encoders. On zero-shot SAR scene classification, our approach outperforms fine-tuned baselines using up to 8x less training data: DFC2020 (+10.3% R@1, +15.5% mAP), EuroSAT-SAR (+15.7% R@1, +12.2% mAP), BigEarthNet-MM (+14.7% R@1). These results establish frozen manifold alignment as a principled, data-efficient alternative to fine-tuning in high-disparity cross-modal settings.

</details>

#### 2026-10-18 - Learning Lane-Structured Conditioning Fields for Online HD Mapping

**Authors:** Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
**Links:** [abs](https://arxiv.org/abs/2610.25284) - [pdf](https://arxiv.org/pdf/2610.25284)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Learning Lane-Structured Conditioning Fields for Online HD Mapping
- 作者：Andrea Bertogalli, Anthony Dell'Eva, Marcello Ceresini, Federico Pirazzoli, Lorenzo Cipelli, Filippo D'Addeo, Nicola Marinello, Massimo Bertozzi
- 出版日期：2026-10-18T14:04:25Z
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2610.25284) / [PDF](https://arxiv.org/pdf/2610.25284)

### 一句话总结
论文提出一种与 BEV 对齐的密集“Lane Field”表示来编码局部车道结构，并基于该表示构建即插即用框架，通过 BEV 特征调制和可变形注意力引导来提升在线高清地图构建。

### 研究问题
在线高清地图构建中，现有方法常依赖外部先验来提升精度与鲁棒性，但先验表示存在权衡：密集栅格易集成却忽略某些地图几何属性；稀疏向量保留几何结构却需要专用编码器、难以接入现有架构。此外，外部先验可能不准确、获取成本高或难以维护。论文希望找到一种既能提供几何引导、又可学习且广泛适用的结构表示。

### 核心思路/方法
论文提出 Lane Field：一种密集的、与 BEV 对齐的几何表示，在每个空间位置编码局部车道结构，并可由车载观测预测，或由外部地图先验构建。在此基础上，作者设计了一个即插即用框架，通过两种互补机制增强在线高清地图构建：
1. BEV 特征调制：将车道结构线索注入潜在 BEV 特征；
2. 可变形注意力引导：将查询采样引导至底层车道几何。

论文主要在 OpenLane-V2 上评估，摘要称该方法能持续改进现有方法，并在车道段感知上达到 state-of-the-art。

### 主要贡献
- 提出 Lane Field，一种密集 BEV 对齐的局部车道结构表示，可由观测预测或由外部地图先验构建。
- 提出基于 Lane Field 的即插即用框架，通过 BEV 特征调制和可变形注意力引导增强在线高清地图构建。
- 在 OpenLane-V2 上评估，摘要报告其方法持续改进现有方法，并在车道段感知上取得 state-of-the-art 性能。

### 局限性
摘要未提供足够信息说明计算开销、实时性、不同数据集上的泛化能力、对不准确外部先验的鲁棒性，以及失败案例或消融实验细节。摘要也未提供足够信息说明该框架在非车道类地图元素上的适用性。

### 阅读优先级
中。理由：该论文关注在线高清地图构建中的先验表示与即插即用增强，问题定义清晰，且摘要声称在 OpenLane-V2 上取得 state-of-the-art；但摘要未提供足够实验细节与局限性信息。是否优先阅读取决于读者对 BEV 表示、车道段感知或可变形注意力引导的兴趣。

</details>

<details>
<summary>Abstract</summary>

High-definition maps provide critical structural information for downstream autonomous driving tasks. Recent methods increasingly rely on external priors to improve prediction accuracy and robustness. Yet, existing prior representations expose a trade-off: dense rasters are easy to integrate but ignore certain map geometric properties, while sparse vectors preserve geometric structure but require dedicated encoders and are difficult to plug into existing architectures. Moreover, external priors can be inaccurate, costly to acquire, or difficult to maintain, motivating a structural representation that can provide geometric guidance while remaining learnable and broadly applicable. We address this limitation with the Lane Field, a dense BEV-aligned geometric representation that encodes local lane structure at each spatial location and can be either predicted from onboard observations or constructed from external map priors. Building on this representation, we introduce a plug-and-play framework that enhances online HD mapping through two complementary mechanisms: BEV feature modulation, which injects lane-structured cues into latent BEV features, and deformable attention guidance, which steers query sampling toward the underlying lane geometry. We primarily evaluate our method on OpenLane-V2, showing that conditioning BEV features and guiding deformable attention with local lane geometry enables our framework to consistently improve existing methods and achieve state-of-the-art performance on lane segment perception. Project page: https://andberto.github.io/LaneField/

</details>

#### 2026-10-15 - GeoState: Learning View-Decoupled Geometry States for 3D World Modeling

**Authors:** Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
**Links:** [abs](https://arxiv.org/abs/2610.22343) - [pdf](https://arxiv.org/pdf/2610.22343)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoState: Learning View-Decoupled Geometry States for 3D World Modeling
- 作者：Hongchang Liu, Jian Liu, Yujuan Ding, Liang Peng, Xun Jiang, Fei Ma, Xing Xu, Yi Bin
- 出版日期：2026-10-15T17:56:18Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.22343 ；PDF：https://arxiv.org/pdf/2610.22343 ；项目页：https://hongchang-liu.github.io/GeoState-project-page/

### 一句话总结
GeoState 提出一种视角解耦的几何表示，将场景状态演化与相机相关观测分离，以提升预测式 3D 世界建模的稳定性与跨视角查询一致性。

### 研究问题
现有 3D 世界模型常将几何基础模型（GFM）的特征作为预测用的世界状态，但这些特征具有视角依赖性，会把场景动态与相机引起的变化纠缠在一起，使状态演化更难预测。论文试图解决由此带来的视角依赖与预测困难问题。

### 核心思路/方法
GeoState 将场景状态演化与相机相关观测分离。具体而言，一个场景 tokenizer 将多视角 GFM 特征聚合为视角解耦的场景状态；一个几何解码器使用相机射线对该状态进行查询；随后，一个自回归世界模型预测未来场景状态，而相机运动被单独建模。预测出的状态可以在预测相机或外部指定相机下解码，并在整个 rollout 中保持来自单一上下文的尺度，无需逐帧尺度对齐。

### 主要贡献
- 提出 GeoState，一种用于预测式 3D 世界建模的视角解耦几何表示，将场景状态演化与相机相关观测分离。
- 设计场景 tokenizer 聚合多视角 GFM 特征为视角解耦场景状态，并用相机射线通过几何解码器查询。
- 采用自回归世界模型预测未来场景状态，同时单独建模相机运动。
- 支持在预测或外部指定相机下解码预测状态，并在 rollout 中保持单一上下文尺度，无需逐帧尺度对齐。
- 实验表明 GeoState 在 Waymo 上优于先前 3D 世界模型，支持几何一致的跨视角查询，并零样本泛化到 KITTI 和 nuScenes。

### 局限性
摘要未提供足够信息。摘要未提供关于失败案例、计算开销、具体限制条件或方法适用范围之外不足的详细信息。

### 阅读优先级
高。理由：该论文针对 3D 世界模型中视角依赖导致状态预测困难的关键问题，提出明确的解耦建模思路，并在 Waymo 上报告优于先前方法、支持跨视角查询且零样本泛化到 KITTI 和 nuScenes；若关注 3D 世界模型、具身智能或自动驾驶场景建模，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution harder to predict. We propose GeoState, a view-decoupled geometry representation for predictive 3D world modeling that separates scene-state evolution from camera-dependent observation. Specifically, a scene tokenizer aggregates multi-view GFM features into a view-decoupled scene state, which a geometry decoder queries using camera rays. An autoregressive world model then predicts future scene states, while camera motion is modeled separately. The predicted states can therefore be decoded under either predicted or externally specified cameras, while retaining a single context-derived scale throughout the rollout without per-frame scale alignment. Experiments show that GeoState outperforms prior 3D world models on Waymo, supports geometrically consistent cross-view querying, and generalizes zero-shot to KITTI and nuScenes. Project page: https://hongchang-liu.github.io/GeoState-project-page/

</details>

#### 2026-10-15 - Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation

**Authors:** Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
**Links:** [abs](https://arxiv.org/abs/2610.22342) - [pdf](https://arxiv.org/pdf/2610.22342)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation
- 作者：Tianxing Chen, Wenwei Lin, Chuqiao Lyu, Peicheng Xiang, Junyuan Tang, Tian Nian, Zijian Cai, Kehe Ye, Chenze Yu, Wenxuan Zhu, Eric J. Chen, Yan Qin, Yue Chen, Tongyu Wu, Junhao Gong, Kai-Chong Lei, Jiahao Zhang, Kailun Su, Qiwei Liang, Renjing Xu, Ping Luo, Wenbo Ding
- 出版日期：2026-10-15T17:56:17Z
- 分类：Embodied / Robotics / AR Applications
- 链接：摘要链接 https://arxiv.org/abs/2610.22342 ；PDF 链接 https://arxiv.org/pdf/2610.22342 ；项目网站 https://xsparkai.com/Spark-0

### 一句话总结
Spark-0 提出一种空间对齐的视觉-触觉-语言-动作（VTLA）模型，将触觉既作为预训练监督信号又作为策略输入，用于提升机器人在接触密集的灵巧操作任务中的表现。

### 研究问题
通用机器人策略从大规模视觉预训练中获益，但在接触密集的灵巧操作中往往表现不佳，因为力、柔顺性和早期滑动难以仅从图像中观测。论文关注的核心问题是：如何利用触觉信息，既改善视觉运动预训练，又作为部署时的策略条件，从而提升灵巧操作能力。

### 核心思路/方法
Spark-0 以两种互补方式使用触觉：
1. **预训练阶段**：由触觉手套导出的图像空间接触图（image-space contact maps）与冻结的 3D 几何教师（frozen 3D geometry teacher）特征共同监督视觉 token；这些监督目标在推理阶段被移除。
2. **并行触觉通路**：编码区域力历史（regional force histories）与 3D taxel 状态，用于条件化动作专家（action expert）。
因此，单个检查点（single checkpoint）可同时支持纯视觉部署和触觉条件化部署。

为扩展这种监督，论文构建了 **HumanTouch**：一个 1,000 小时的全手触觉人类操作数据集，并将 Spark-0 与自我中心视频、机器人数据、仿真数据一起预训练。论文还发布了 **SparkArena**，在同一灵巧本体（one dexterous embodiment）上配对纯视觉仿真任务与触觉条件化真实机器人任务。

### 主要贡献
- 提出 Spark-0，一种空间对齐的 VTLA 模型，将触觉同时用作可扩展的预训练监督信号和部署时的策略输入。
- 构建 HumanTouch，1,000 小时全手触觉人类操作数据集，用于规模化触觉预训练。
- 发布 SparkArena，在同一灵巧本体上配对纯视觉仿真任务与触觉条件化真实机器人任务。
- 实验结果表明：Spark-0 在 SparkArena 两个赛道上均取得最高平均成功率，并在 Ego Humanoid Manipulation Benchmark 的全部八项聚合指标上排名第一。
- 关键对比：在相同数据与计算量下，相比丢弃触觉的纯视觉预训练，保留 1,000 小时 HumanTouch 触觉使 Ego Humanoid 上的纯视觉成功率从 52.5% 提升至 71.7%，使 SparkArena-Real（部署时也使用触觉）成功率从 44.0% 提升至 52.0%，说明触觉不仅是策略输入，也是灵巧视觉运动预训练的可扩展监督。

### 局限性
摘要未提供足够信息。摘要未说明方法的失败案例、计算成本细节、触觉硬件泛化性、仿真到真实迁移的具体限制，也未提供与更多基线方法的全面对比或消融实验细节。

### 阅读优先级
**高**。理由：该工作同时涉及触觉预训练规模化、VTLA 模型、大规模数据集（1,000 小时 HumanTouch）与基准（SparkArena），并给出触觉监督显著提升视觉运动预训练效果的定量证据，对灵巧操作、多模态机器人策略和触觉学习方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Generalist robot policies benefit from large-scale visual pretraining but often struggle with contact-rich dexterous manipulation, where force, compliance, and incipient slip are hard to observe from images. We present Spark-0, a spatially aligned vision-tactile-language-action (VTLA) model that uses touch in two complementary ways. During pretraining, image-space contact maps derived from tactile gloves, together with features from a frozen 3D geometry teacher, supervise the visual tokens; these objectives are removed at inference. In parallel, a tactile pathway encodes regional force histories and 3D taxel states to condition the action expert. A single checkpoint therefore supports both vision-only and tactile-conditioned deployment. To scale this supervision, we build HumanTouch, a 1,000-hour dataset of full-hand tactile human manipulation, and pretrain Spark-0 on it together with egocentric video, robot data, and simulation. We also release SparkArena, which pairs vision-only simulated tasks with tactile-conditioned real-robot tasks on one dexterous embodiment. Spark-0 achieves the highest mean success rate on both SparkArena tracks and ranks first on all eight aggregate metrics of the Ego Humanoid Manipulation Benchmark. Compared with vision-only pretraining on the same data and compute with touch discarded, retaining the touch of 1,000 hours of HumanTouch raises vision-only success on Ego Humanoid from 52.5% to 71.7%, and success on SparkArena-Real, where touch is also used at deployment, from 44.0% to 52.0%, indicating that touch serves not only as a policy input but also as scalable supervision for dexterous visuomotor pretraining. The Website is available at: https://xsparkai.com/Spark-0.

</details>

#### 2026-10-15 - VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models

**Authors:** Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
**Links:** [abs](https://arxiv.org/abs/2610.21985) - [pdf](https://arxiv.org/pdf/2610.21985)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VeriVLA: Adaptive Test-Time Verification for Flow-Based VLAs with Latent World Models
- 作者：Xueli Sun, Yuxiang Lu, Yantong Liu, Xianzhe Fan, Xi Chen, Zhe Liu, Hengshuang Zhao
- 出版日期：2026-10-15T14:34:44Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.21985

### 一句话总结
针对基于流的 VLA 策略在测试时只执行单一噪声样本、缺乏质量评估的问题，提出一种免训练的两轴触发机制，并在触发时用基于 JEPA 的潜在世界模型对候选动作块进行排序，在真实与仿真任务中提升完成度与成功率。

### 研究问题
基于流的 Vision-Language-Action（VLA）策略本质上是随机的：同一观测下，不同噪声种子会生成质量不一的动作块。但测试时策略通常只提交单一采样，且没有对其质量的显式估计。在细粒度操作任务中，执行次优动作可能不可逆地破坏任务进程并导致失败。因此需要解决：如何在测试时利用策略的随机性，检测关键状态并选择更优的动作块。

### 核心思路/方法
- 引入一个免训练的两轴触发机制，使用两个初始样本，分别测量块内时间变化与跨样本方差，用以检测关键状态。
- 一旦触发，使用基于 JEPA 的潜在世界模型对候选动作块进行排序。
- 排序依据是预测动作条件下的未来潜在状态以及相应的任务进展变化。
- 由于在潜在空间中操作，验证器避免了像素重建，从而实现高效且更准确的排序。

### 主要贡献
- 提出免训练的两轴触发机制，利用两个初始样本的块内时间变化与跨样本方差检测关键状态。
- 提出基于 JEPA 的潜在世界模型验证器，在潜在空间中对候选动作块按预测的未来潜在状态与任务进展变化排序，避免像素重建。
- 在三个真实任务（钢笔插入、移液、苹果放置）上，将平均完成分数从 50.8% 提升至 65.5%，在单张 RTX 4090 上每个触发决策增加 326 ms 的采样与验证时间。
- 在仿真中取得一致增益：RoboTwin 2.0 干净设置下平均成功率从 66.4% 升至 73.6%，随机化设置下从 62.8% 升至 69.6%，LIBERO 上从 96.9% 升至 97.6%。

### 局限性
摘要未提供足够信息。摘要未说明方法在未触发状态下的表现、触发机制的误判率、不同任务对 326 ms 额外延迟的容忍度、候选动作块数量与验证开销的关系，也未提供失败案例或与其他验证方法的对比。真实任务仅列出三个，泛化性边界未在摘要中说明。

### 阅读优先级
高。理由：该工作针对基于流的 VLA 测试时随机性与次优动作执行的现实问题，提出免训练触发与潜在世界模型验证的组合方案，并在真实任务与多个仿真基准上报告了明确提升；若关注机器人操作策略的测试时验证与潜在世界模型应用，具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Flow-based Vision-Language-Action (VLA) policies are inherently stochastic: different noise seeds can produce action chunks of varying quality from the same observation. At test time, however, the policy typically commits to a single sample without an explicit estimate of its quality. In fine-grained manipulation, executing a suboptimal action can irreversibly disrupt task progress and lead to failure. To exploit policy stochasticity, we introduce a training-free two-axis trigger that uses two initial samples to measure within-chunk temporal variation and cross-sample variance, detecting the critical states. Once triggered, a JEPA-based latent world model ranks candidate action chunks by predicting action-conditioned future latent states and the corresponding changes in task progress. By operating in latent space, the verifier avoids pixel reconstruction and enables efficient and more accurate ranking. Across three real-world tasks, $\textit{i.e.,}$ pen insertion, pipetting, and apple placement), our method raises the average completion score from 50.8% to 65.5%, while adding 326 ms for sampling and verification per triggered decision on a single RTX 4090. Consistent gains are also observed in simulation, where the average success rate rises from 66.4% to 73.6% in the clean setting of RoboTwin 2.0, from 62.8% to 69.6% in its randomized setting, and from 96.9% to 97.6% on LIBERO.

</details>

#### 2026-10-15 - Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation

**Authors:** Weilin Ruan, Bohan Zhou, Jinghao Li, Yangkai Wei, Wenqian Li, Peiran Dong, Yingjie Xu, Leyi Wu, Haojian Huang, Binghui Xie, Han Yang, Kaiwen Zhou, Yinchuan Li, Ying-Cong Chen, James Cheng
**Links:** [abs](https://arxiv.org/abs/2610.21882) - [pdf](https://arxiv.org/pdf/2610.21882)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Anvil: Scaling Embodied Spatial Intelligence through Knowledge Recirculation
- 作者：Weilin Ruan, Bohan Zhou, Jinghao Li, Yangkai Wei, Wenqian Li, Peiran Dong, Yingjie Xu, Leyi Wu, Haojian Huang, Binghui Xie, Han Yang, Kaiwen Zhou, Yinchuan Li, Ying-Cong Chen, James Cheng
- 出版日期：2026-10-15T13:47:08Z
- 分类：Embodied / Robotics / AR Applications（二级分类：摘要未提供足够信息）
- 链接：摘要页 https://arxiv.org/abs/2610.21882 ；PDF https://arxiv.org/pdf/2610.21882

### 一句话总结
论文提出 Anvil 统一框架，通过数据生成、训练与评测三个组件，将具身空间智能中的异构空间知识进行循环整合，并以 9B 学生模型 Anvil-MOPD 在七个公开基准上取得相对基线约 9–11 个百分点的平均提升。

### 研究问题
具身空间智能要求模型不仅做视觉识别，还需定位实体、推理实体间关系，并以动作相关形式表达这些知识。然而不同阶段所需的监督信号分散在互不兼容的几何与语义输出形式中，联合训练会将这些阶段所需知识混为一谈。论文关注的问题是：如何在数据生成、训练与评测层面统一处理这种异构性，使模型能够学习多样化的具身空间能力，并区分阶段能力不足与错误传播。

### 核心思路/方法
论文提出 Anvil 统一框架，包含三个部分：
1. Anvil-Gen：异构数据飞轮，结合形式特定生成、跨阶段一致性校验和失败驱动的回采，覆盖 11 种 Ground–Relation–Act 形式。
2. Anvil-Ben：提供场景对齐的监督，用于学习多样的具身空间能力；并提供场景关联的评测，以区分阶段能力与错误传播。
3. Anvil-MOPD：一个 9B 学生模型，通过从专家教师蒸馏来整合异构空间知识；其中“语义优先故障路由”将教师监督对准学生最早的决定性失败，“阶段归一化”用于控制不同长度原生输出的损失尺度。

数据方面，论文构建了 5.8M 条基于来源的记录，覆盖 160K 张图像，其中 580K 条空间记录留作留出评测，其余 5.22M 条用于训练。

### 主要贡献
- 提出 Anvil 统一框架，覆盖具身空间智能的数据生成、训练与评测。
- 提出 Anvil-Gen 异构数据飞轮，覆盖 11 种 Ground–Relation–Act 形式，并包含跨阶段一致性验证与失败驱动回采。
- 提出 Anvil-Ben，用于场景对齐监督与区分阶段能力和错误传播的评测。
- 提出 Anvil-MOPD 9B 学生模型，结合语义优先故障路由与阶段归一化，从专家教师蒸馏异构空间知识。
- 构建 5.8M 条来源可溯记录（160K 图像），并划分 580K 留出评测与 5.22M 训练记录。
- 在七个公开基准上，Anvil-MOPD 平均分别超过 Qwen3.5-9B 和 RynnBrain-8B 9.29 与 11.03 个百分点，并在 VABench-Point 上达到 80.67%。
- 通过受控研究支持“定向覆盖”“选择性迁移”“反馈引导修复”作为互补框架组件。

### 局限性
- 论文的具体实验设置、基线配置、消融细节、数据构建流程细节、教师模型构成、训练成本、推理开销等，摘要未提供足够信息。
- 七个公开基准的具体名称与逐项结果，除 VABench-Point 的 80.67% 外，摘要未提供足够信息。
- “定向覆盖”“选择性迁移”“反馈引导修复”的受控研究具体设计与量化结论，摘要未提供足够信息。
- 框架在真实机器人或 AR 场景中的部署验证、泛化边界与失败案例分析，摘要未提供足够信息。

### 阅读优先级
高。理由：该论文面向具身空间智能这一核心方向，同时提出数据生成、训练方法和评测基准三方面统一框架，并给出 9B 模型在七个公开基准上的平均提升与具体指标。对关注具身空间推理、多阶段监督异构性、知识蒸馏与数据飞轮的研究者具有较高参考价值。但需注意，摘要未提供实验细节与局限性讨论，深入评估需阅读全文。

</details>

<details>
<summary>Abstract</summary>

Embodied spatial intelligence requires more than visual recognition: models must localize entities, reason about their relations, and express this knowledge in action-relevant forms. Yet joint training can conflate the knowledge needed at different stages because supervision is fragmented across incompatible geometric and semantic outputs. We introduce Anvil, a unified framework for data generation, training, and benchmarking for embodied spatial intelligence. (1) Anvil-Gen is a heterogeneous data flywheel that combines form-specific generation, cross-stage consistency verification, and failure-driven recollection across 11 Ground--Relation--Act forms. (2) Anvil-Ben provides scene-aligned supervision for learning diverse embodied spatial capabilities and scene-linked assessments that distinguish stage competence from error propagation. (3) Anvil-MOPD is a 9B student that consolidates heterogeneous spatial knowledge through distillation from specialist teachers. Semantic-first-fault routing targets teacher supervision to the student's earliest decisive failure, while stage normalization controls the loss scale across native outputs of different lengths. We construct 5.8M source-grounded records spanning 160K images, reserving 580K spatial records for held-out evaluation and using the remaining 5.22M records for training. On average across seven public benchmarks, Anvil-MOPD outperforms Qwen3.5-9B and RynnBrain-8B by 9.29 and 11.03 percentage points, respectively, while reaching 80.67% on VABench-Point. Controlled studies support targeted coverage, selective transfer, and feedback-guided repair as complementary framework components.

</details>

#### 2026-10-15 - CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation

**Authors:** Yanchen Ding, Jiayi Chen, Jianfeng Xu, Wei Zhao, Li Yi, He Wang
**Links:** [abs](https://arxiv.org/abs/2610.21349) - [pdf](https://arxiv.org/pdf/2610.21349)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CQDC-Warp: GPU-Accelerated Differentiable Quasi-Dynamic Simulation for Contact-Rich Manipulation
- 作者：Yanchen Ding, Jiayi Chen, Jianfeng Xu, Wei Zhao, Li Yi, He Wang
- 出版日期：2026-10-15T06:30:20Z
- 分类：主分类为 Embodied / Robotics / AR Applications；二级分类未提供
- 链接：[摘要](https://arxiv.org/abs/2610.21349) / [PDF](https://arxiv.org/pdf/2610.21349)

### 一句话总结
论文提出 CQDC-Warp，一个面向批量模型预测控制的 GPU 加速可微准动态仿真器，用于研究接触引导的轨迹优化，并在多项接触丰富操作任务上报告了成功率和速度优势。

### 研究问题
论文关注接触丰富操作轨迹的高效合成问题。摘要指出，基于梯度的规划是有前景的方向，但联合优化运动与接触决策仍然困难；同时，许多现有规划器运行在 CPU 上，吞吐量有限。

### 核心思路/方法
论文提出 CQDC-Warp，一个用于批量模型预测控制的 GPU 加速可微准动态仿真器。其核心设定是接触引导的轨迹优化：在规划前指定期望的机器人与物体接触，并通过软代价鼓励这些接触；接触几何与摩擦响应由仿真动力学决定，而不依赖预先规定的接触模式调度。

### 主要贡献
- 提出 CQDC-Warp：面向批量 MPC 的 GPU 加速可微准动态仿真器。
- 将其用于接触引导的轨迹优化：接触意图预先指定并由软代价鼓励，接触几何和摩擦响应由仿真动力学决定，无需预设接触模式调度。
- 在 17 物体 Allegro 手内旋转基准上进行 17,408 次试验，报告成功率为 79.8%，高于 CFree 的 73.7% 和 IMPACT 的 65.2%；平均轨迹生成时间分别缩短为后两者的 1/27.0 和 1/50.2。
- 在单张 NVIDIA RTX 4090 上使用 2,048 个并行世界，前向与反向吞吐分别达到 2.06×10^5 和 2.25×10^5 world-steps per second。
- 进一步实验涵盖 LEAP 和 Shadow 手操作、环境接触利用、双臂操作、全身控制，以及在 Sharpa 手上的真实世界轨迹回放。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、泛化边界、仿真到现实差距的定量评估、消融实验细节、计算资源之外的扩展性限制，以及真实世界回放的成功率或误差指标。摘要仅报告了部分基准结果和任务覆盖范围，未提供完整局限性讨论。

### 阅读优先级
高。理由：该工作直接针对接触丰富操作中运动与接触联合优化的难题，并同时报告了基准成功率、相对基线提升、GPU 吞吐和多种任务扩展；对机器人学习、接触规划、可微仿真和批量 MPC 方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Efficient synthesis of contact-rich manipulation trajectories is essential for downstream robot learning. Gradient-based planning offers a promising approach, but jointly optimizing motion and contact decisions remains challenging. Meanwhile, many existing planners run on CPUs with limited throughput. We present CQDC-Warp, a GPU-accelerated differentiable quasi-dynamic simulator for batched model predictive control (MPC). We use it to study contact-guided trajectory optimization, in which intended robot--object contacts are specified before planning and encouraged through soft costs, while the simulated dynamics determine contact geometry and frictional response without a prescribed contact-mode schedule. Across $17{,}408$ trials on the $17$-object Allegro in-hand rotation benchmark, our framework achieves $79.8\%$ success, compared with $73.7\%$ for CFree and $65.2\%$ for IMPACT, and reduces mean trajectory-generation time by factors of $27.0$ and $50.2$, respectively. On a single NVIDIA RTX 4090 with $2{,}048$ parallel worlds, forward and backward throughput reach $2.06\times10^5$ and $2.25\times10^5$ world-steps per second, respectively. Further experiments cover manipulation with LEAP and Shadow hands, environmental contact exploitation, bimanual manipulation, whole-body control, and real-world trajectory replay on a Sharpa hand.

</details>

#### 2026-10-14 - EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos

**Authors:** Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang, Daolin Ma, Ian Reid, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.20904) - [pdf](https://arxiv.org/pdf/2610.20904)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EgoJEPA: Beyond Retargeting for Dexterous Manipulation from Egocentric Videos
- 作者：Meng Cao, Can Zhao, Jinjie Wei, Haonan Zhao, Yulong Zhang, Duo Han, Xiaofan Li, Ziwu Song, Rongtao Xu, Ruyi Gan, Hao Wang, Qian Wang, Daolin Ma, Ian Reid, Xiaodan Liang
- 出版日期：2026-10-14T20:34:18Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20904 ；PDF：https://arxiv.org/pdf/2610.20904

### 一句话总结
EgoJEPA 提出一个三阶段框架，试图绕开基于规则的人到机器人重定向，从第一视角人类视频中学习与具体机器人本体无关的表征，用于灵巧操作。

### 研究问题
第一视角人类视频可为机器人演示提供可扩展替代方案，但如何把其中的操作先验迁移到机器人控制仍是挑战。常见做法是基于重定向：通过手工设计的几何映射，将人类手腕和手指姿态转换为特定本体的动作命令。摘要指出这种映射存在两个问题：一是跨不同本体时需要细致重新校准；二是可能把手势跟踪误差传播到下游机器人控制流程中。

### 核心思路/方法
论文提出 EgoJEPA，一个三阶段框架，目标是在不依赖基于规则的人到机器人重定向的情况下，从第一视角人类视频中学习本体无关表征：

1. 人类动作预训练：通过 JEPA 风格的视觉预测，并以手部运动差异为条件，学习具有效果感知的潜在动作。
2. 基于潜在动作的世界建模：联合预测未来视觉动态和潜在动作，从而将人类先验预训练与机器人特定的控制参数化解耦。
3. 本体特定调优：通过轻量级动作适配器，将预训练模型适配到不同机器人。

### 主要贡献
- 提出 EgoJEPA 三阶段框架，用于从第一视角人类视频学习本体无关表征，避免基于规则的人到机器人重定向。
- 将人类动作预训练、潜在动作世界建模与本体特定调优结合，以解耦人类先验预训练和机器人特定控制参数化。
- 摘要报告在三个机器人本体、五个真实世界操作任务上验证了有效性和效率：域外评估平均成功率为 74%，重定向基线为 65%；跨本体累计挂钟成本降低 47.2%，从 743.2 小时降至 392.7 小时。

### 局限性
摘要未提供足够信息说明方法的具体失败模式、适用边界、任务难度分布、机器人本体类型、是否存在仿真到现实差距、对外观或视角变化的鲁棒性、以及轻量级动作适配器的具体结构与训练成本。摘要未提供足够信息说明其与更多基线或更广泛任务集的比较结果。摘要未提供足够信息说明手部跟踪质量对方法的影响。摘要未提供足够信息说明其方法在非第一视角视频或非灵巧操作任务上的泛化能力。

### 阅读优先级
高。理由：该论文直接针对第一视角人类视频到机器人灵巧操作迁移中的重定向瓶颈，提出替代性表征学习框架，并在摘要中给出跨三个机器人本体、五个真实任务的量化结果与成本对比；若关注机器人学习、第一视角视频利用、跨本体迁移或 JEPA 类方法在具身控制中的应用，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Egocentric human videos offer a scalable alternative to costly robot demonstra- tions, yet transferring their manipulation priors to robot control remains chal- lenging. The commonly adopted retargeting-based approaches convert human wrist and finger poses into embodiment-specific action commands through hand- crafted geometric mappings. However, such mappings require meticulous recal- ibration across different embodiments and risk propagating hand-tracking errors into downstream robot control pipelines. To this end, we propose EgoJEPA, a three-stage framework that learns embodiment-agnostic representations from ego- centric human videos without rule-based human-to-robot retargeting: 1) Human- action pre-training learns effect-aware latent actions through JEPA-style visual prediction conditioned on hand-motion differences; 2) Latent-action-based world modeling jointly predicts future visual dynamics and latent actions, which decou- ples human prior pre-training from robot-specific control parameterizations; 3) Embodiment-specific tuning adapts the pretrained model to diverse robots through lightweight action adapters. Experiments on five real-world manipulation tasks across three robot embodiments demonstrate the effectiveness and efficiency of EgoJEPA. It achieves a 74% average success rate under the out-of-domain evalu- ation, compared with 65% for the retargeting baseline, while reducing cumulative cross-embodiment wall-clock cost by 47.2%, from 743.2 to 392.7 hours.

</details>

#### 2026-10-14 - BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments

**Authors:** Mani Amani, Mohammed Alyaseen, Zhirui Dai, Ki Myung Brian Lee, Nikolay Atanasov, Jorge Cortes
**Links:** [abs](https://arxiv.org/abs/2610.20895) - [pdf](https://arxiv.org/pdf/2610.20895)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot navigation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：BubbleCBF: Constructive Safety for Second-Order Systems and Application to Autonomous Robot Navigation in Unknown Environments
- 作者：Mani Amani, Mohammed Alyaseen, Zhirui Dai, Ki Myung Brian Lee, Nikolay Atanasov, Jorge Cortes
- 出版日期：2026-10-14T20:24:47Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20895

### 一句话总结
该论文提出 BubbleCBF，一种针对二阶控制仿射系统的构造性安全约束设计方法，通过从有符号距离函数（SDF）构造位置空间中的无碰撞球（bubble），并利用其二次几何与重叠关系构建速度相关安全约束，以二次规划安全滤波器实现，并应用于差分驱动机器人在未知环境中的自主导航。

### 研究问题
二阶动力学系统的安全约束满足具有挑战性，因为位置约束可能要求不可行的减速度。高阶控制屏障函数（CBF）可用于表达此类系统的安全条件，但其可行性依赖于系统动力学和可用控制权限。论文旨在为二阶控制仿射系统构造可行的安全约束。

### 核心思路/方法
- 从有符号距离函数（SDF）出发，在位置空间中构造无碰撞球（bubble）。
- 利用这些球的二次几何及重叠关系，构造速度相关的安全约束。
- 将相关安全集表示为若干交集组成的并集，并通过二次规划安全滤波器进行约束执行。
- 在关于动力学、球重叠和设计参数的温和假设下，证明基于二次规划的控制器是良定义的、关于系统状态连续，并使该集合前向不变。
- 推导有界输入下的可行性充分条件。
- 将 BubbleCBF 应用于差分驱动机器人，展示在未知环境中的安全自主导航。

### 主要贡献
- 提出面向二阶控制仿射系统的构造性可行安全约束设计方法。
- 基于 SDF 构造位置空间中的无碰撞球，并利用其二次几何与重叠建立速度相关安全约束。
- 将安全集表示为交集之并，并通过二次规划安全滤波器实现。
- 在温和假设下证明控制器的良定义性、状态连续性和集合前向不变性。
- 推导有界输入下的可行性充分条件。
- 在差分驱动机器人上验证 BubbleCBF 用于未知环境安全自主导航。

### 局限性
摘要未提供足够信息。摘要未说明实验规模、环境复杂度、与基线方法的定量对比、计算开销、假设在实际系统中的满足程度，以及除差分驱动机器人外的泛化验证情况。

### 阅读优先级
高。理由：该论文聚焦二阶系统安全约束的可行构造与理论保证，并直接应用于未知环境下的机器人导航，主题明确且兼具理论证明与机器人验证；但具体实验细节和对比结果需查阅原文，摘要未提供足够信息。

</details>

<details>
<summary>Abstract</summary>

Satisfying safety constraints for systems with second-order dynamics is challenging because a position constraint may require infeasible deceleration. Higher-order control barrier functions (CBFs) provide an approach for expressing safety conditions for such systems but feasibility depends on the system dynamics and available control authority. We develop a constructive approach for designing feasible safety constraints for second-order control-affine systems. Starting from a signed distance function (SDF), we construct collision-free spheres, i.e., bubbles, in position space, and use their quadratic geometry and overlap to construct a velocity-dependent safety constraint. The associated safe set is represented as a union of intersections and enforced through a quadratic-program safety filter. Under mild assumptions on the dynamics, bubble overlap, and design parameters, we prove that the quadratic-program-based controller is well defined, continuous in the system state, and renders the set forward invariant. We also derive sufficient conditions for feasibility under bounded inputs. We demonstrate that our BubbleCBF, applied to a differential-drive robot, achieves safe autonomous navigation in unknown environments. Videos and results are available at: https://existentialrobotics.org/bubblecbf/.

</details>

#### 2026-10-14 - GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence

**Authors:** Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang
**Links:** [abs](https://arxiv.org/abs/2610.20592) - [pdf](https://arxiv.org/pdf/2610.20592)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GeoThinker-$F$: Endogenous Predictive World Representations for Fast Spatial Intelligence
- 作者：Haoyuan Li, Qihang Cao, Huanyuan Zhou, Xin Hu, Sijia Chen, Zihan Guo, Kun Xiang, Yunshuang Nie, Tao Tang, Xinlong Zheng, Jia-Wang Bian, Xianming Liu, Xiaodan Liang
- 出版日期：2026-10-14T17:59:03Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2610.20592 ；PDF: https://arxiv.org/pdf/2610.20592

### 一句话总结
GeoThinker-$F$ 通过将因果 MLLM 隐状态转化为预测性潜在世界表示，在移除推理阶段外部 3D 几何编码器依赖的同时，保持有竞争力的空间智能表现并显著加速推理。

### 研究问题
现有几何感知多模态大语言模型（MLLMs） increasingly 依赖外部 3D 编码器提供结构先验，但在推理时执行这些额外编码器路径会带来显著的延迟和计算开销。论文关注的问题是：能否在不依赖外部 3D 编码器的情况下，让 MLLM 自身内化时空感知能力，从而兼顾空间智能性能与推理效率。

### 核心思路/方法
论文提出 GeoThinker-$F$，核心洞察是中间语义表示已包含足够信息来预测当前几何的有用表示和未来语义表示，而不需要精确复现专用 3D 编码器的特征。方法采用解耦的两阶段训练策略：
- 第一阶段：冻结 MLLM 主干，轻量级 Latent Frame Prediction (LFP) 头从离线 3D 几何专家和下一帧语义目标中学习。
- 第二阶段：移除外部专家，通过专门的 Spatial-Grounded Temporal (SGT) Fusion 模块，联合优化模型以生成并选择性整合其自预测先验。

### 主要贡献
- 提出 GeoThinker-$F$ 框架，通过将因果 MLLM 隐状态转化为预测性潜在世界表示，内化时空感知。
- 采用解耦两阶段训练策略，先由 LFP 头学习离线 3D 几何专家与下一帧语义目标，再移除外部专家并通过 SGT Fusion 模块联合优化自预测先验的生成与选择性整合。
- 实验评估显示，GeoThinker-$F$ 消除了运行时对外部 3D 几何编码器的依赖，同时在多样空间智能基准上保持有竞争力的性能。
- 实现最高 $3.6\times$ 推理加速，将延迟从 $1.45\,\mathrm{s}$ 降至 $0.40\,\mathrm{s}$，并保留较强的空间推理性能。

### 局限性
摘要未提供足够信息。摘要未说明具体基准名称、数据集规模、失败案例、方法在哪些场景下可能退化、训练成本细节、LFP 头与 SGT Fusion 模块的具体结构，以及与其他方法逐项对比的完整结果。

### 阅读优先级
高。理由：该论文针对几何感知 MLLM 推理效率这一明确痛点，提出去除外部 3D 编码器依赖的内生预测表示方案，并报告了最高 $3.6\times$ 推理加速与延迟从 $1.45\,\mathrm{s}$ 降至 $0.40\,\mathrm{s}$ 的量化结果；若关注具身智能、机器人、AR 中的实时空间推理，该工作具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Existing geometry-aware Multimodal Large Language Models (MLLMs) increasingly rely on external 3D encoders to provide structural priors, but executing these additional encoder paths at inference introduces substantial latency and computational overhead. We propose GeoThinker-$F$, an efficient framework that internalizes spatiotemporal perception by transforming causal MLLM hidden states into predictive latent world representations. Our key insight is that intermediate semantic representations contain sufficient information to predict useful representations of current geometry and future semantics, without requiring an exact reproduction of features from a dedicated 3D encoder. To realize this idea, GeoThinker-$F$ adopts a decoupled two-stage training strategy. In the first stage, the MLLM backbone is frozen while lightweight Latent Frame Prediction (LFP) heads learn from an offline 3D geometry expert and next-frame semantic targets. In the second stage, the external expert is removed, and the model is jointly optimized to generate and selectively integrate its self-predicted priors through a specialized Spatial-Grounded Temporal (SGT) Fusion module. Extensive evaluations show that GeoThinker-$F$ eliminates runtime dependence on external 3D geometry encoders while maintaining competitive performance across diverse spatial intelligence benchmarks. It achieves up to a $3.6\times$ inference speedup, reducing latency from $1.45\,\mathrm{s}$ to $0.40\,\mathrm{s}$ while retaining strong spatial reasoning performance.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
