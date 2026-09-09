# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：57
- 分类分布：
  - Embodied / Robotics / AR Applications: 19
  - Neural Scene Representations & Rendering: 18
  - 3D Reconstruction & Multi-view Geometry: 17
  - Dynamic / 4D Reconstruction: 2
  - Geometry Foundation Models: 1
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

**1. “零先验/免校准”成为核心设计哲学，追求从数据到部署的全链路去约束化**
多篇论文在不同任务上同时摆脱传统先验依赖。PROSE 提出完全无需 CAD 模型、模板或参考图像的"prior-free 相对 6D 姿态估计"；ArmPoser 直接在智能手表原生 IMU 坐标系下训练，消除了校准姿势和骨偏移校准；GoDeep 则抛弃 3D 训练语料库和专用 3D 编码器，仅用语言空间完成开放词汇 3D 分割。SyncWorld 更进一步，通过"视觉校准片段"在上下文中动态指定动作-视觉映射，使世界模型无需额外训练即可在未见环境充当零样本模拟器。这一趋势反映出：研究者正从"为每个场景/设备/对象单独适配"转向"让模型在推理时自适应理解环境"的范式迁移。

**2. 从静态重建走向"可交互、可模拟、闭环驱动"的动态/主动感知**
重建不再止于几何与外观，而是追求仿真就绪、可交互、可驱动规划闭环。FIRE3D 将单张 RGB 或视频变成"仿真就绪"的场景资产（对象物理解耦、可直接交互）；AURORA 将主动视角选择与手内重定向闭环，用重建不确定性直接驱动物理操作；RoboCousin 把用户观测自动变成可执行仿真任务，生成超百万条双臂操纵专家轨迹。同时两篇交互式 4D/动态工作（Point4D、EdMCGS）强调长序列与任意时刻插值，指向"场景理解必须支持持续交互与预测"的需求。

**3. 学习式占用/密集预测的"可信度"被重新审视，几何先验与物理一致性回归**
Rethinking Learned Occupancy 通过受控闭环实验证明：占用精度提升并不单调改进主动建图的闭环覆盖——这动摇了"预测越准、规划越好"的默认假设。TV-SGS 引入张量投票让高斯之间直接通信，在稀疏视图下通过几何信息传播增强结构一致性，本质是用传统几何先验约束神经表示。EdMCGS 则在动态场景中引入事件驱动的马尔可夫链和时间局部等距约束，以物理刚性假设约束传播运动。这些工作共同指向：在神经表示盛行的当下，经典几何工具（张量投票、等距约束、门控滤波）正以"外部监督或正则"的形式回归，用于补偿学习模型的盲目自信。

**4. 多模态/异构数据融合走向纵深，表征"空间不匹配"成为新研究前线**
多个工作聚焦不同传感器或表征域之间的鸿沟。Spheriverse 直面球面角域（观测）与笛卡尔坐标（物理世界）的跨空间差异，构建大规模球面图像-LiDAR 数据集并提出 SphereOcc 桥接；Dex-X 用仿真补全人类视频缺失的触觉通道，实现视觉-触觉策略的真实部署；EdMCGS 以事件流补全极低帧率 RGB 的帧间缺失证据。值得注意的是，这些工作不再简单做特征拼接，而是在"表征生成"阶段就解决域对齐（如 GoDeep 直接在纯语言空间中聚合），或通过仿真/物理引擎生成缺失模态。

**5. 训练后压缩与推理效率成为神经场景表示的工程化焦点**
CVT-GS 针对 3DGS 提出免训练的 post-hoc 简化框架，通过质心 Voronoi 剖分加轻量神经合并，实现上百倍压缩且可直接用于现有渲染器；PIC 则针对 INR 图像编码提出单次前馈架构，将编码提速至 20 FPS、解码优化至 2000 FPS；Marigold V2 也在扩散模型中引入单步推理与量化以降低运行成本。这反映了该领域从"追求质量上限"向"兼顾部署可行性"的成熟化转向。


#### 技术路线观察

| 方向 | 技术侧重点 | 代表论文 |
|------|-----------|---------|
| 几何基础模型与位姿 | 利用多模态基础特征免训练找对应 + 环一致性几何细化；摆脱对象级先验，朝"通用对应"路线演进 | PROSE, GoDeep |
| 3D/4D 重建 | 前馈化（feed-forward）是大势——FIRE3D 单次前馈输出组合场景表示，Point4D 以前馈方式处理数百帧；解耦轨迹预测与可见性，用 3D 查询避免重投影误差累积 | FIRE3D, Point4D |
| 神经场景表示与渲染 | 3DGS 生态继续扩张：CVT-GS 做后处理压缩（免训练、免微调）、TV-SGS 引入非渲染类 3D 损失、EdMCGS 将 3DGS 扩展到事件驱动的动态马尔可夫链 | CVT-GS, TV-SGS, EdMCGS |
| 机器人/AR 应用 | 仿真作为"数据与监督引擎"：Dex-X 用仿真补全触觉、RoboCousin 自动化仿真资产构建、SyncWorld 用世界模型做零样本 rollout 模拟器；主动感知强调不确定性驱动的闭环（AURORA）；主动建图开始反思学习式占用在规划中的"双角色困境" | Dex-X, RoboCousin, SyncWorld, AURORA, Rethinking Learned Occupancy |
| 成像与传感器融合 | 设备原生坐标系直接训练（ArmPoser）、球面-笛卡尔空间建模（SphereOcc）、多鱼眼+IMU 融合（MFVINS） | ArmPoser, Spheriverse, MFVINS |
| 视觉基础模型再思考 | 一面"再造"扩散模型——Marigold V2 将 DiT 改造成深度估计器；一面"泼冷水"——ProbeGen 严格评估图像生成器的零样本感知能力，揭示与专家模型的清晰权衡 | Marigold V2, ProbeGen |


#### 值得优先阅读的论文

**1. Point4D（2609.09145）** — 阅读优先级最高。它将 4D 重建从"几十帧短窗口"推进到"数百帧长序列"，提出的 3D 查询解码器在机制上简洁且优雅（轨迹预测与可见性解耦、直接端点重查询），不仅解决了一个公认瓶颈，而且为动态场景理解提供了一个可能成为"新基线"的范式。对关注动态重建或视频理解的研究者，这篇应当最先读。

**2. FIRE3D（2609.08848）** — 它以前馈、端到端、一分钟内将 RGB 视频变成"仿真就绪、对象级完整、可交互"的场景资产，横跨 3D 重建与机器人仿真两大社区。方法论上代表"重建即资产生成"的前沿方向，同时直接呼应下游机器人训练的数据需求，值得花时间精读其组合式场景表示设计。

**3. Rethinking Learned Occupancy（2609.09069）** — 这是一篇"反直觉"的论文：证明了占用精度与闭环覆盖绩效之间不存在单调关系。对任何从事"感知-规划耦合"系统的研究者（主动建图、自动驾驶、探索规划），该结论有重要警示意义——提升感知精度不必然带来更好的规划结果。其提出的观测门控滤波也为"不重训即修正"提供了务实思路。

**4. SyncWorld（2609.09155）** — 它以"视觉校准片段"实现零样本模拟器，概念上有较强前瞻性——用上下文示例指定动作-视觉映射，绕开了"动作不是像素空间通用语言"的根本矛盾。对研究 world model、机器人策略学习或仿真到现实迁移的读者，这篇提供了新角度。

**5. Spheriverse（2609.09012）** — 它一次性提供了大规模球面图像-LiDAR 数据集、三个任务的统一基准和 SphereOcc 框架，稀缺性在于"球面观测下的 3D 理解"这一相对空白但实际需求明确的领域。对做全景感知或野外机器人工作的研究者，数据与基准的参考价值极高。


#### 可能的研究机会

**1. "感知-规划耦合界面"的系统级研究**：Rethinking Learned Occupancy 揭示了感知精度与规划绩效的解耦，但目前对该现象缺乏更普适

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-09T12:36:09-04:00
**Total number of papers:** 57
**Number of papers added in the latest update:** 34
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

#### 2026-09-03 - Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations

**Authors:** Denis M. Akola, David F. Fouhey
**Links:** [abs](https://arxiv.org/abs/2609.04174) - [pdf](https://arxiv.org/pdf/2609.04174)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** VGGT, 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations
- 作者：Denis M. Akola, David F. Fouhey
- 出版日期：2026-09-03（arXiv 发布时间）
- 分类：Geometry Foundation Models（几何基础模型）
- 链接：https://arxiv.org/abs/2609.04174

### 一句话总结
本文提出 Z3D 方法，利用 3D 基础模型（如 VGGT）的内部场景表征，通过潜在扩散在未见视角上合成真实的新颖深度图，实现零样本深度预测。

### 研究问题
3D 基础模型内部学习到的场景表征，是否包含可用于推断新视角下三维结构（尤其是隐藏表面）的通用知识？如何有效地从这些表征中解码出新视角的深度信息？

### 核心思路/方法
1. **假设验证**：作者假设 3D 基础模型在解决三维重建任务时，必须学习包含大量通用三维场景知识的内部表征，因此这些表征可能蕴含可解码的隐藏表面信息。
2. **先验验证**：首先证明可以从 3DFM 内部表征中解码出隐藏表面（即模型表征并非仅用于已知视角）。
3. **方法 Z3D**：在 3DFM 表征上执行潜在扩散（latent diffusion），以此估计未见视角下的点图（pointmaps），进而得到新颖视图的深度图。
4. **零样本能力**：该方法无需针对特定数据集进行训练，可直接在多个数据集上为新视角生成合理的深度预测。

### 主要贡献
- 首次研究从 3D 基础模型内部表征解码隐藏表面的可行性，并给出正面证据。
- 提出 Z3D 方法，将潜在扩散应用于 3DFM 表征，实现未见视角的深度估计。
- 实验表明 Z3D 能在多个数据集上为新视角预测真实合理的深度图，展示跨数据集的零样本泛化能力。

### 局限性
摘要未提供足够信息。具体局限（如对遮挡严重场景、复杂拓扑、计算成本、定量精度上限等）均未在摘要中明确说明，无法评估。

### 阅读优先级
**中**  
理由：该工作针对 3D 基础模型内部表征的可重用性进行探索，思想新颖且具有一定启发性，适合关注三维视觉与几何基础模型交叉方向的读者。但目前仅摘要显示初步可行性，未给出定量评测细节或应用场景深度，若追求具体方法实现或严格对比结论，需进一步阅读全文。对于非相关方向读者优先级可降低。

</details>

<details>
<summary>Abstract</summary>

3D Foundation Models (3DFMs) such as VGGT have recently pushed the boundaries of 3D vision by predicting rich unified representations with feed-foward transformers. The scene representations learned by these models enable strong performance on multiple 3D vision tasks. In this paper, we investigate using their internal representations to infer 3D in the scene from new views. Our hypothesis is that in order to solve the task of 3D reconstruction, these models need to learn a representation that includes a large amount of general knowledge about 3D scenes. After showing that it is possible to decode hidden surfaces from internal 3DFM representations, we propose a method, Z3D, that estimates pointmaps in unseen views by doing latent diffusion on 3DFM representation. We show that Z3D can predict realistic depth maps for new views across multiple datasets.

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

#### 2026-09-08 - EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction

**Authors:** Yuzhong Wang, Wenmin Wang, Xinxing Yu
**Links:** [abs](https://arxiv.org/abs/2609.08332) - [pdf](https://arxiv.org/pdf/2609.08332)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** 3D Reconstruction & Multi-view Geometry, Neural Scene Representations & Rendering
**Matched keywords:** dynamic scene reconstruction, dynamic 3D, scene reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EdMCGS: Event-Driven Markov Chain Gaussian Splatting for Extreme-Low-Frame-Rate Dynamic Scene Reconstruction
- 作者：Yuzhong Wang, Wenmin Wang, Xinxing Yu
- 出版日期：2026-09-08
- 分类：动态/4D重建（主分类）；3D重建与多视角几何、神经场景表征与渲染（副分类）
- 链接：https://arxiv.org/abs/2609.08332

### 一句话总结
本文提出EdMCGS，一种端到端方法，利用事件流将极低帧率RGB动态场景建模为事件驱动的马尔可夫链，实现对任意中间时刻的3D场景重建与渲染。

### 研究问题
如何从极低帧率RGB图像（帧间信息严重缺失）配合事件流，高质量重建动态3D场景并渲染任意中间时刻，避免仅依赖RGB时产生的伪影。

### 核心思路/方法
- 将场景运动建模为**事件驱动的马尔可夫链**：稀疏RGB帧作为状态锚点，区间内记录的事件驱动状态转移。
- 转移过程在推理时仍保持活跃，直接从事件产生3D高斯中间运动，而非通过插值（区别于仅将事件用于训练监督的先前工作）。
- 状态由一组紧凑的控制点承载，每个控制点由其图像投影邻域内采样的事件驱动。
- 引入**时间局部等距约束**，确保传播运动局部刚性。
- 实验显示该方法在合成与真实场景上优于基于RGB和基于事件的基线，且实时渲染所需高斯数量远少于最强事件基线。

### 主要贡献
- 提出事件驱动马尔可夫链高斯溅射（EdMCGS），实现极低帧率下的动态场景重建。
- 推理阶段直接从事件生成帧间运动，而非训练后插值。
- 使用紧凑控制点和局部等距约束保持运动刚性与效率。
- 在合成与真实场景上超越RGB基线与事件基线，并以更少高斯数实现实时渲染。
- 发布源码与新数据集（GitHub链接已提供）。

### 局限性
摘要未提供足够信息（未明确讨论失败场景、边界条件、对噪声/事件稀疏性的鲁棒性等）。

### 阅读优先级
**中**。理由：方法新颖（事件驱动马尔可夫链+高斯溅射），针对极低帧率重建这一实际痛点，且展示出明显效率与质量优势；但若您不关注动态/4D重建或事件相机方向，则该工作相关性不高。建议该领域研究者阅读。

</details>

<details>
<summary>Abstract</summary>

We present EdMCGS (Event-driven Markov chain Gaussian Splatting), an end-to-end method for reconstructing dynamic 3D scenes from extreme-low-frame-rate RGB together with an event stream, which can then be rendered at any intermediate timestamp. Methods relying solely on RGB images generate numerous artifacts due to the lack of evidence from between consecutive frames. To supply this missing evidence, we model the scene motion as an event-driven Markov chain, in which the sparse RGB frames anchor the state at their own timestamps while the events recorded within an interval drive the transition across it. Since the transition reads the events of the current interval, it remains active at inference and produces the in-between motion of the 3D Gaussians directly from the events rather than by interpolation, which sets our method apart from prior work that uses events only as training-time supervision. The state is carried by a compact set of control points, each driven by the events sampled in the neighborhood of its own image projection, and a temporal local isometry term keeps the propagated motion locally rigid. Experiments on synthetic and real-world scenes show that EdMCGS outperforms both RGB-based and event-based baselines, while rendering in real time with far fewer Gaussians than the strongest event-based baseline. We release our source code and a new dataset at https://github.com/joseclipse/EdMCGS.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

#### 2026-09-08 - Prior-free relative 6D pose estimation of multiple object instances

**Authors:** Behdad Khodabandehloo, Andrea Caraffa, Davide Boscaini, Fabio Poiesi
**Links:** [abs](https://arxiv.org/abs/2609.08949) - [pdf](https://arxiv.org/pdf/2609.08949)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Prior-free relative 6D pose estimation of multiple object instances
- 作者：Behdad Khodabandehloo, Andrea Caraffa, Davide Boscaini, Fabio Poiesi
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08949

### 一句话总结
本文提出一种完全无需对象先验（无需CAD模型、模板或参考图像）的多实例未知对象相对6D姿态估计方法PROSE，利用多模态基础特征建立实例间对应关系并估计相对姿态。

### 研究问题
如何在没有任何对象特定先验的前提下，在同一图像中估计未知对象多个实例之间的相对6D姿态。

### 核心思路/方法
- 提出新方法PROSE：利用多模态基础特征在对象实例之间寻找粗略对应关系，无需训练。
- 通过跨实例元组的环一致性约束来细化对应关系，使对应关系全局一致。
- 利用细化后的全局一致对应关系估计任意实例对之间的相对6D姿态。
- 设计新基准PRENCH：基于三个多实例BOP数据集构建，并增补任务特定元数据以支持系统评估。

### 主要贡献
- 提出“prior-free相对6D姿态估计”这一新设定，去除了“知道场景中待估姿态的目标对象”这一假设。
- 提出无需训练、无需对象先验的PROSE方法，采用多模态基础特征与环一致性细化实现相对姿态估计。
- 构建了PRENCH基准，用于该新任务的系统评估。
- 在基准上，PROSE一致优于将现有单图像方法适配到该设定所得的基线，且无需任务特定监督或额外学习组件。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作将6D姿态估计推向“零先验”新范式，具有方向性创新意义；方法无需训练，结合基础模型特征，实用性强；并配套新基准，适合关注姿态估计、少样本/零样本视觉任务或基础模型应用的读者。

</details>

<details>
<summary>Abstract</summary>

Object 6D pose estimation formulations have progressively reduced reliance on object-specific priors, evolving from explicit 3D models to multi-view object captures to single reference images. We take this progression to its extreme by introducing prior-free relative 6D pose estimation, which lifts the assumption of knowing which object is to be posed within the scene. This novel setting aims to estimate the relative poses of multiple instances of an unknown object within the same image, without requiring CAD models, templates, or reference images. We solve this by formulating a novel method (PROSE) that finds coarse correspondences between object instances using multimodal foundation features, thus requiring no training. We refine these correspondences by imposing cycle consistency across tuples of instances, and leverage the resulting globally consistent correspondences to estimate the relative 6D pose between any pair of instances. To enable systematic evaluation, we design a novel benchmark (PRENCH) built from three multi-instance BOP datasets and enriched with task-specific metadata. PROSE consistently outperforms baselines obtained by adapting state-of-the-art single-image methods to the proposed setting, while requiring neither task-specific supervision nor additional learned components. Project website: https://tev-fbk.github.io/PROSE/

</details>

#### 2026-09-08 - FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute

**Authors:** Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang
**Links:** [abs](https://arxiv.org/abs/2609.08848) - [pdf](https://arxiv.org/pdf/2609.08848)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, scene representation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：FIRE3D: Feed-forward Interactive 3D Scene Reconstruction Within A Minute
- 作者：Hongchi Xia, Tianhang Cheng, Wei-Chiu Ma, Shenlong Wang
- 出版日期：2026-09-08T15:01:49Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08848

### 一句话总结
FIRE3D 提出一个前馈端到端统一框架，可在一分钟内将单张 RGB 图像或随意 RGB 视频转化为面向游戏和交互应用的、仿真就绪的 3D 场景资产。

### 研究问题
如何在不进行测试时优化的前提下，快速（一分钟内）从单目 RGB 输入（单图或视频）重建出对象级完整、物理上可交互的仿真就绪 3D 场景。

### 核心思路/方法
- 以单个前馈端到端网络为核心，从输入的 RGB 采集数据中估计有姿态的 RGB-D 观测。
- 网络预测组合式场景表示，为每个对象输出 6-DoF 姿态、包围框、网格和纹理。
- 将场景建模为离散实体集合，从而生成“模态完整”（amodally complete）且仿真就绪的环境，其中的对象在物理上是解耦的、可直接交互。
- 无需测试时优化，直接前馈推理。

### 主要贡献
- 提出统一的单阶段前馈框架，可同时处理单张图像和视频输入。
- 相比先前的交互就绪方法，速度提升数个数量级，且无需测试时优化。
- 相比现有前馈 3D 方法，提供对象级别的完整性（模态完整），而非仅有场景级表面。
- 在多个数据集上，姿态精度、几何完整性和纹理质量达到具有竞争力或最优的结果，同时速度大幅领先。

### 局限性
摘要未提供足够信息（未明确讨论失败案例、输入约束、内存占用、对复杂场景或遮挡的鲁棒性等具体局限）。

### 阅读优先级
**高**。理由：该工作针对交互式 3D 场景重建这一活跃方向，提出了统一的端到端前馈方案，同时解决速度（分钟级）、对象级完整性和无测试时优化三个关键痛点，并声称在多个指标上达到先进水平。摘要中结果和效率优势明确，适合从事 3D 重建、仿真环境生成或交互应用相关研究的读者优先关注。

</details>

<details>
<summary>Abstract</summary>

We present FIRE3D, a unified framework that takes a single RGB image or casual RGB video and transforms it into simulation-ready 3D scene assets for games and interactive applications in under a minute. At the core of FIRE3D is a feed-forward, end-to-end network that predicts a compositional scene representation from posed RGB-D observations estimated from the RGB capture, including the 6-DoF pose, bounding box, mesh, and texture for every object. By modeling the scene as a collection of discrete entities, FIRE3D produces amodally complete and simulation-ready environments where objects are physically decoupled and ready for interaction. Our framework requires no test-time optimization, runs orders of magnitude faster than prior interaction-ready methods, and provides object-level completeness beyond existing feed-forward 3D approaches. We demonstrate competitive or state-of-the-art results across pose accuracy, geometry completeness, and texture quality across various datasets while being orders of magnitudes faster. Project page: https://xiahongchi.github.io/Fire3D/

</details>

#### 2026-09-08 - ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU

**Authors:** Bishnu Dev, Vasco Xu, Xi-Aan Loh, Chenfeng Gao, Henry Hoffmann, Karan Ahuja
**Links:** [abs](https://arxiv.org/abs/2609.08806) - [pdf](https://arxiv.org/pdf/2609.08806)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU
- 作者：Bishnu Dev, Vasco Xu, Xi-Aan Loh, Chenfeng Gao, Henry Hoffmann, Karan Ahuja
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08806

### 一句话总结
ArmPoser 提出一种无需用户校准、直接在智能手表原始 IMU 参考坐标系下训练的单手表手臂姿态估计系统，在公开基准与自采实验中匹配或超越需校准的基线方法。

### 研究问题
如何消除智能手表 IMU 手臂姿态估计中对用户校准（如校准姿势、骨偏移校准）的依赖，并避免因坐标变换和传感器漂移引入的误差，以支持日常场景下的稳定部署。

### 核心思路/方法
- **核心创新**：直接在消费级智能手表 IMU 数据固有的参考坐标系（设备原生轴）下训练模型，不再将原始测量量转换为标准化训练格式，从而省去坐标变换、显式对齐和骨偏移校准。
- **训练增强**：在训练中引入基于物理的腕表放置位置变化和手臂形态差异，以覆盖用户的个性化差异。
- **佩戴配置模块**：额外设计一个模块用于推断前臂朝向前/后（内外侧）以及表冠朝向，以辅助姿态估计。
- **评估方式**：在公开基准和一项包含 10 名参与者、30 项活动的真实实验（覆盖 watchOS 和 Android 智能手表）中验证系统性能。

### 主要贡献
1. 提出第一个无需校准的单智能手表 IMU 手臂姿态估计系统 ArmPoser。
2. 证明直接在设备原生参考坐标系训练模型可消除对校准流程和预处理管线的依赖。
3. 通过物理增强训练数据（腕表位置、手臂形态变化）提升对用户差异的鲁棒性。
4. 提出佩戴配置（前臂朝向与表冠方向）推断模块。
5. 在多项真实环境下与需校准的基线方法对比，ArmPoser 达到匹配或更优的性能。

### 局限性
摘要未提供足够信息，未明确说明系统在极端遮挡、快速运动或不同环境下的性能下降情况，也未提及计算成本、模型大小或电池消耗等部署细节。摘要未明确公开基准的具体名称、对比方法的配置及统计显著性分析。

### 阅读优先级
**高**。理由：该工作针对可穿戴 IMU 姿态估计中普遍存在的校准痛点，提出了一种直接贴合实际部署数据的训练范式，具有较强的实用价值；方法新颖性明确，且实验结果（含跨平台真实测试）为无校准方案的可行性提供了直接证据。发表于 2026 年，时效性高，适合对该方向感兴趣的研究者快速追踪前沿。

</details>

<details>
<summary>Abstract</summary>

Arm pose estimation enables applications in fitness, extended reality input, rehabilitation, and life logging. Prior smartwatch-based approaches rely on calibration poses and preprocessing pipelines that transform raw IMU measurements into standardized training formats. These steps hinder deployment in everyday settings and introduce errors due to imperfect calibration and sensor drift. We present ArmPoser, a calibration-free arm pose estimation system using a single smartwatch IMU. Our central contribution is training models directly in the reference frame native to consumer smartwatches, aligning learning with how IMU data is produced by deployed devices. By operating on device-native axes, ArmPoser removes the need for coordinate transformations, explicit alignment, and bone-offset calibration used in prior work. We further augment training with physically grounded variations in watch placement and arm morphology to account for user-specific variability. ArmPoser also includes a wear-configuration module that infers anterior or posterior forearm placement and crown orientation. We evaluate pose estimation on public benchmarks and on a 10-participant, 30-activity study using watchOS and Android smartwatches, where ArmPoser matches or exceeds calibrated baselines without any user calibration.

</details>

#### 2026-09-08 - MFVINS: Multiple Fisheye Camera-Based Visual Inertial System

**Authors:** Eunseong Jang, YuJin Chung, Sang Jun Lee, Jihyun Yoon, HyungGi Jo
**Links:** [abs](https://arxiv.org/abs/2609.08626) - [pdf](https://arxiv.org/pdf/2609.08626)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** simultaneous localization and mapping, SLAM, bundle adjustment, depth estimation, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MFVINS: Multiple Fisheye Camera-Based Visual Inertial System
- 作者：Eunseong Jang, YuJin Chung, Sang Jun Lee, Jihyun Yoon, HyungGi Jo
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08626

### 一句话总结
本文提出了一种基于多个鱼眼相机与IMU融合的视觉惯性系统MFVINS，通过IMU辅助的特征追踪、归一化平面去畸变外点过滤及带物理约束的重投影误差设计，提升了SLAM在遮挡与低纹理环境下的鲁棒性，并保持实时性。

### 研究问题
传统VINS仅使用单一相机作为视觉输入，在遮挡、光照变化和低纹理环境下容易出现误差累积，导致位姿估计精度下降。本文旨在利用多个鱼眼相机提升视觉惯性系统的鲁棒性，同时控制计算开销以实现实时运行。

### 核心思路/方法
- 构建多鱼眼相机+IMU的融合框架，扩展视野以应对遮挡和低纹理区域。
- 提出IMU辅助的FAST特征追踪器，用于多相机下的高效特征提取与鲁棒匹配。
- 在归一化图像平面上过滤由鱼眼畸变引起的外点。
- 提出带有物理有效性约束的新型重投影误差，并结合基于学习的深度估计用于束调整（bundle adjustment）。

### 主要贡献
- 提出了MFVINS，一个新颖的多鱼眼相机视觉惯性系统，兼顾鲁棒性与实时性。
- 设计了IMU辅助的多相机FAST特征追踪方法，提升特征提取与匹配效率。
- 在归一化图像平面上去除鱼眼畸变导致的外点，改善匹配质量。
- 引入带物理有效性约束的重投影误差用于束调整，并集成学习式深度估计。
- 在多种场景下与先前VINS方法比较，验证了方法的有效性，并实现了实时运行。

### 局限性
摘要未提供具体实验中的失败场景、计算资源需求、传感器配置细节（如鱼眼相机数量与布局）以及与其他方法的量化性能差异。摘要亦未提及方法在极端动态环境或大规模场景下的表现，因此这些方面的局限性无法判断。

### 阅读优先级
**中**  
理由：该研究面向多相机+IMU的SLAM系统，在鲁棒性设计（多鱼眼、畸变处理、深度学习深度融合）上有明确的新意，且强调实时性，对从事视觉惯性导航或多目SLAM的研究者有一定参考价值。然而，摘要缺乏定量实验对比细节，且发表于2026年，实际可用性和行业影响力仍需后续全文验证，因此优先级定为中等。

</details>

<details>
<summary>Abstract</summary>

A simultaneous localization and mapping (SLAM) method using a monocular camera and a low-cost inertial measurement unit (IMU) sensor is an effective way to fulfill a low-cost sensor configuration. Using this sensor configuration, visual-inertial system (VINS) focuses on fusing data from a camera and an IMU sensor to estimate the six degrees-of-freedom (DOF) of the sensor pose. Typically, VINS uses only a single camera as visual input, which lead to problems such as error accumulation due to occlusion, various illumination, and textureless environments. In this paper, we propose a new multiple fisheye camera-based visual-inertial system called MFVINS. We present an IMU-aided FAST feature tracker for multiple cameras that enables efficient extraction and robust matching of local features. Then, the proposed method filters out outliers caused by fisheye distortion on the normalized image plane. Subsequently, a new reprojection error with physical validity constraints is proposed for bundle adjustment using learning-based depth estimation. The proposed method is applied to various scenarios, and its effectiveness is demonstrated by comparing previous VINS methods. In particular, MFVINS is implemented in real-time process to leverage the advantages of using multiple cameras -- robustness against occlusion and textureless regions -- while reducing the computational burden.

</details>

#### 2026-09-08 - AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction

**Authors:** Feiyu Zhao, Yuetong Li, Chenxi Xiao
**Links:** [abs](https://arxiv.org/abs/2609.08493) - [pdf](https://arxiv.org/pdf/2609.08493)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, geometric reconstruction, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AURORA: Active Uncertainty-Driven Re-Orientation for In-Hand Reconstruction
- 作者：Feiyu Zhao, Yuetong Li, Chenxi Xiao
- 出版日期：2026-09-08
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08493

### 一句话总结
AURORA是一个主动3D重建框架，通过在线重建与手内重定向的闭环控制，基于不确定性驱动选择下一次最佳观察视角以提高被遮挡物体的重建质量。

### 研究问题
机器人手抓取物体时存在严重的视觉遮挡，现有手内操作策略多依赖预定义或开环的重定向方式，未显式针对未被充分观察的区域。因此需要一种主动的视角选择与重建策略，在收据新观测数据的同时引导手部旋转，以高效完成物体重建。

### 核心思路/方法
- 提出主动在环框架，连接在线目标中心重建与手内重定向过程。
- 核心模块为Ray-GPIS，它沿候选观察光线估计各方向的重建不确定性，并利用“不确定性-新颖性”目标函数选择下一次最佳观察视角。
- 所选视角通过条件于轴的手内旋转策略执行。
- 新获得的RGB-D观测基于无CAD模型的6D位姿跟踪和轻量级几何重建进行增量融合。

### 主要贡献
- 提出主动闭环的AURORA框架，将重建不确定性直接驱动手内重定向决策。
- 设计Ray-GPIS，支持基于光线的方向性不确定性估计与高效主动视角规划。
- 实验表明AURORA相对于非主动旋转策略，在重建质量和信息获取效率方面均有提升。
- Ray-GPIS在重建性能、动作排序质量和规划效率上优于主动视角规划的基线方法。
- 针对手部遮挡和位姿误差等扰动进行了消融验证，表明系统具有一定鲁棒性。

### 局限性
摘要未提供足够信息，无法获取作者在计算开销、实时性能、物体类别范围、硬件依赖或失败模式等方面的局限分析。

### 阅读优先级
**高**
理由：该工作将主动感知与手内操作闭环结合，面向机器人抓取中实际且棘手的遮挡重建问题；方法兼具不确定性建模与视角规划的创新性，实验验证了相对基线的多方面提升，对机器人操纵、主动视觉与3D重建交叉方向具有较广泛参考价值。

</details>

<details>
<summary>Abstract</summary>

Observing objects grasped by a robot hand is challenging due to severe visual occlusions. Although in-hand manipulation can expose hidden surfaces, existing approaches often rely on predefined or open-loop reorientation strategies that do not explicitly target under-observed regions. We propose AURORA, an active 3D reconstruction framework that closes the loop between online object-centric reconstruction and in-hand reorientation. At its core, Ray-GPIS estimates direction-wise reconstruction uncertainty along candidate viewing rays and selects next-best-view targets using an uncertainty--novelty objective, which are realized through an axis-conditioned in-hand rotation policy. The resulting RGB-D observations are fused incrementally using CAD-free 6D pose tracking and lightweight geometric reconstruction. Experiments demonstrate that AURORA improves reconstruction quality and information-acquisition efficiency over non-active rotation strategies, while Ray-GPIS also outperforms active view-planning baselines in reconstruction performance, action-ranking quality, and planning efficiency. Targeted ablations further validate its robustness to hand occlusion and pose errors. The project webpage is available at https://aurorahand.github.io/

</details>

#### 2026-09-08 - Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation

**Authors:** Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk, Dengxin Dai
**Links:** [abs](https://arxiv.org/abs/2609.08084) - [pdf](https://arxiv.org/pdf/2609.08084)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** scene reconstruction, depth estimation, monocular depth, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Marigold V2: Revisiting Diffusion Transformers for Monocular Depth Estimation
- 作者：Igor Pavlovic, Thiemo Wandel, Anton Obukhov, Luca Bartolomei, Andrey Davydov, Fabio Tosi, Matteo Poggi, Sabine Süsstrunk, Dengxin Dai
- 出版日期：2026-09-08
- 分类：3D重建与多视角几何
- 链接：https://arxiv.org/abs/2609.08084

### 一句话总结
本文提出Marigold V2，通过改进训练策略和损失函数，将扩散Transformer（DiT）模型高效转化为高性能的单目深度估计器，在泛化性、细节清晰度和多任务适用性上超越此前最优方法。

### 研究问题
如何在保持模型容量和运行效率的前提下，将预训练的图像生成/编辑扩散模型（基于DiT架构）重新用于单目深度估计，并解决现有方法在分布外泛化和深度图细节质量上的不足。

### 核心思路/方法
- 基于Marigold已有技术框架，提出针对DiT架构的改进配方，支持从预训练多步流匹配模型进行单步推理，并在需要时引入量化，以降低运行成本。
- 分析朴素训练产生的伪影，提出两种有效修正：一是将模型内部表示与从真值中提取的语义特征对齐；二是采用两阶段微调协议，并引入新颖的基于Sinkhorn的损失函数。

### 主要贡献
- 提出Marigold V2的全套技术方案，显著提升单目深度估计的分布外泛化能力和输出质量。
- 在KITTI和ETH3D基准上，AbsRel指标较此前最优提升16-26%。
- 定性上能恢复毛发、树叶、发丝级细边缘等此前模型难以处理的细节。
- 该方法可迁移至其他密集回归任务（如表面法线估计和固有图像分解），并取得最优结果。

### 局限性
摘要未提供足够信息。文中未明确讨论计算资源需求、失败案例、对极端输入的限制、训练数据依赖性或与其他方法在同等条件下的完整对比细节。

### 阅读优先级
**高**。理由：该方法在核心基准上带来显著量化提升（16-26%），并展示跨任务泛化能力；面向单目深度估计乃至密集预测任务的研究者具有直接参考价值，且基于扩散模型的高效推理方案也具有实用意义。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation is a ubiquitous yet highly ill-posed computer vision task, with downstream applications in scene reconstruction, computational photography, and robotics, among others. Despite the field's maturity, recent models still struggle to generalize to out-of-distribution inputs and to produce sharp and detailed depth maps. In this paper, we revisit Marigold, a set of techniques for repurposing modern image generation and editing models, powered by the diffusion transformer (DiT) architecture, into state-of-the-art monocular depth estimators. Our recipes target single-step inference from pretrained multi-step flow-matching models, with quantization where needed, preserving model capacity while remaining cheap to run. We analyze the artifacts of naive training and identify two effective remedies: aligning the model's internal representations with semantic features extracted from ground-truth, and adopting a 2-stage fine-tuning protocol built around a novel Sinkhorn-based loss. The results are crisper, cleaner depth maps that generalize well out-of-distribution, with 16-26% improvement in AbsRel over the previous best on KITTI and ETH3D. Qualitatively, our model resolves fur, foliage, and hair-thin edges that have eluded prior models. Furthermore, Marigold V2 achieves state-of-the-art results when applied to other dense regression tasks, such as surface normals estimation and intrinsic image decomposition. Project website: https://hf.co/spaces/huawei-bayerlab/marigold-v2-web

</details>

#### 2026-09-07 - A Black-Box Adversarial Attack on Human Pose Estimation and Keypoint-Based Action Recognition Models

**Authors:** Kacper Mroczek, Michal Kepski
**Links:** [abs](https://arxiv.org/abs/2609.08013) - [pdf](https://arxiv.org/pdf/2609.08013)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A Black-Box Adversarial Attack on Human Pose Estimation and Keypoint-Based Action Recognition Models
- 作者：Kacper Mroczek, Michal Kepski
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.08013

### 一句话总结
该论文提出一种基于OKS（Object Keypoint Similarity）反馈信号的决策级黑盒对抗攻击方法OKS Attack，用于针对人体姿态估计及基于关键点的动作识别模型，并在Penn Action数据集上验证其有效性。

### 研究问题
人体姿态估计和基于关键点的动作识别模型容易受到对抗攻击，但现有黑盒攻击方法多采用边界框重叠度量（如IoU）作为反馈，而姿态估计输出关键点结构而非包围框，导致框级相似度不适合衡量姿态退化。因此，研究如何设计一种直接针对人体姿态空间结构的黑盒对抗攻击方法。

### 核心思路/方法
提出OKS Attack，一种基于决策的黑盒对抗攻击方法。其核心是利用对象关键点相似度（OKS）替代IoU作为攻击反馈信号，从而直接度量并优化姿态估计结果的退化程度。攻击过程无需模型内部梯度信息，仅依赖查询得到的预测关键点反馈。

### 主要贡献
- 首次（摘要暗示）将OKS作为黑盒攻击反馈信号用于姿态估计任务，弥补框级相似度在关键点场景下的不适配问题。
- 在Penn Action数据集上的实验表明，OKS Attack能持续降低多个姿态估计器的姿态质量（平均OKS下降0.0802至0.1494）。
- 在跨数据集的下游动作识别评估中，攻击使识别准确率下降6.18至13.86个百分点，且优于查询匹配的随机噪声扰动。
- 攻击在自上而下和单阶段两种姿态估计模型上均有效。
- 将公开源代码（GitHub链接已在摘要中提供）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该研究填补了姿态估计任务在黑盒对抗攻击方面的空白，方法定义清晰且实验实证效果显著，对视频理解安全领域有一定参考价值；但创新点集中于攻击反馈信号的选择（OKS替换IoU），属于对既有黑盒攻击框架的适配性调整，可能对纯攻击方法学研究者吸引力更大，对交叉领域读者优先级中等。

</details>

<details>
<summary>Abstract</summary>

Human pose estimation and keypoint-based action recognition models are increasingly deployed as components of video understanding pipelines, yet their vulnerability to adversarial attacks remains insufficiently studied. Temporally coherent black-box attacks have been previously studied in visual object tracking, where the attack feedback can be defined using bounding-box overlap measures such as Intersection over Union (IoU). However, human pose estimation produces keypoint configurations rather than enclosing boxes, making box-level similarity poorly suited for measuring pose degradation. We propose OKS Attack, a decision-based black-box attack that uses Object Keypoint Similarity (OKS) as the attack feedback signal, directly targeting the spatial structure of human poses rather than their enclosing boxes. Experiments on the Penn Action dataset show that OKS Attack consistently reduces pose quality across evaluated pose estimators, with mean OKS decreases ranging from 0.0802 to 0.1494. In a downstream cross-dataset action-recognition evaluation, the attack reduces accuracy by 6.18 to 13.86 percentage points and outperforms query-matched random-noise perturbations. The attack is effective across both top-down and single-stage pose estimation models. The source code will be made publicly available at https://github.com/KacperM33/OKS_attack

</details>

#### 2026-09-07 - Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation

**Authors:** Shangzhe Di, Zhaokai Wang, Weidi Xie
**Links:** [abs](https://arxiv.org/abs/2609.07884) - [pdf](https://arxiv.org/pdf/2609.07884)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Are Image Generators Zero-Shot Perceivers? A Rigorous Evaluation
- 作者：Shangzhe Di, Zhaokai Wang, Weidi Xie
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.07884

### 一句话总结
本文提出ProbeGen基准，系统评估了20个图像生成器在零样本条件下执行深度估计、分割和计数等视觉感知任务的性能，发现其具备一定感知能力但与传统专家模型存在清晰权衡。

### 研究问题
预训练图像生成器在零样本设置下，能在多大程度上完成多种公开的视觉感知基准任务（如单目深度估计、指称/推理分割和目标计数）？它们的表现相对于专用感知模型和多模态大语言模型（MLLM）如何？

### 核心思路/方法
- 构建ProbeGen基准：将视觉感知任务（深度估计、分割、计数）转化为基于文本提示的条件生成任务，以便在统一的生成式框架下评估。
- 在11个已发表的基准上，总计比较20个模型，涵盖专有和开源权重的图像生成器、专用感知模型以及多模态大语言模型。
- 在零样本条件下评估各类模型的感知能力，并分析不同模型族群的表现差异。

### 主要贡献
- 提出ProbeGen，一个专门用于零样本生成式感知评估的基准，覆盖三类视觉感知任务。
- 首次对20个模型（包括多种生成器、专用模型和MLLM）进行系统性跨基准比较。
- 实证发现：预训练图像生成器展现出可测量的零样本感知能力，但存在明显权衡——专用模型在分布内准确性和效率上更强，而生成模型在分布漂移下更鲁棒，并更擅长组合语义推理。
- 为“零样本生成式感知”这一研究方向提供实证基础和未来研究框架。

### 局限性
摘要未提供足够信息用以说明具体实验限制（如任务划分细节、评估偏差、模型特定失败案例等）。仅能从摘要推断：该研究聚焦于零样本设定，可能未涵盖微调/适配后的生成器性能，且具体任务定义依赖文本条件化，可能无法完全等价于传统感知任务。其他局限性（如计算成本、基准覆盖范围）摘要未提及，需要阅读全文确认。

### 阅读优先级
**高**  
理由：该工作首次系统评估图像生成器的零样本感知能力，提出了统一的基准ProbeGen并覆盖多类任务和20个主流模型，主题处于生成与感知交叉的前沿，对理解生成模型的下游潜力具有重要参考价值。若你对视觉生成、多模态理解和基准构建感兴趣，此文值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent work, such as Vision Banana, shows that lightweight instruction tuning can enable an image generator to achieve state-of-the-art performance across multiple visual perception tasks. Motivated by this perspective, we ask how far image generators can go on public visual perception benchmarks in a zero-shot setting. We introduce ProbeGen, a benchmark for zero-shot generative perception that casts monocular depth estimation, referring/reasoning segmentation, and object counting as conditional generation tasks specified through text prompts, and compares 20 models in total---including proprietary and open-weight image generators, specialist perception models, and MLLMs---across 11 published benchmarks. We observe that pretrained image generators show measurable zero-shot perceptual competence, but with a clear trade-off: specialist models remain stronger for in-distribution accuracy and efficiency, while generative models are often more robust under distribution shift and better at compositional semantic reasoning. We hope this study helps establish zero-shot generative perception as a meaningful research direction and provides a useful foundation for future work at the intersection of visual generation and understanding.

</details>

#### 2026-09-07 - Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs

**Authors:** Xinggang Hu, Chenyangguang Zhang, Zihan Zhu, Ruida Zhang, Xiangkui Zhang, Xiangyang Ji
**Links:** [abs](https://arxiv.org/abs/2609.07497) - [pdf](https://arxiv.org/pdf/2609.07497)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, pose estimation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Functional-SLAM: Interaction-Aware Mapping with Online Functional Scene Graphs
- 作者：Xinggang Hu, Chenyangguang Zhang, Zihan Zhu, Ruida Zhang, Xiangkui Zhang, Xiangyang Ji
- 出版日期：2026-09-07
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.07497

### 一句话总结
Functional-SLAM 提出首个在线递归维护功能场景图的 SLAM 框架，将功能关系建模融入实时建图过程，以支持细粒度机器人交互。

### 研究问题
现有 SLAM 系统缺乏对功能关系的建模，无法支撑细粒度的机器人交互；而现有的功能 3D 场景图方法依赖离线重建，难以用于真实场景中的实时交互探索。因此目标是在线实时构建并维护功能场景图。

### 核心思路/方法
- 将功能场景图作为在线 SLAM 状态，持续递归地维护节点与边。
- 结合 anchor-keyframe 几何与功能上下文约束，实现持久节点维护。
- 通过时间关系累积多帧证据，提交稳定功能边。
- 在视觉回环检测中，利用功能拓扑作为补充线索，处理外观重复或纹理退化场景。

### 主要贡献
- 提出 Functional-SLAM，首个在线持续维护功能场景图的 SLAM 框架。
- 相比离线方法显著提升运行效率，同时保持较高精度。
- 在几何回环基础上引入功能拓扑辅助，进一步提升位姿估计精度。
- 提供公开代码。

### 局限性
摘要未提供足够信息，无法确认方法在动态物体、大规模场景、计算资源消耗或长期漂移等方面的具体局限性。

### 阅读优先级
**高**。理由：该工作首次将功能场景图纳入在线 SLAM 状态，直接填补了实时交互建图与功能语义建模之间的空白，对机器人交互与 SLAM 交叉方向具有较强的新颖性和应用价值，且已在精度与效率上报告了正面结果。

</details>

<details>
<summary>Abstract</summary>

Existing SLAM systems lack modeling of the functional relations required for fine-grained robotic interaction. Functional 3D scene graphs can represent relations between objects and interaction elements, but existing methods rely on offline reconstruction, making them inadequate for real-time interaction in real-world exploration. To address this limitation, we propose Functional-SLAM, the first framework that continuously and recursively maintains a functional scene graph as an online SLAM state. The framework combines anchor-keyframe geometry with functional-context constraints for persistent node maintenance, accumulates multi-frame evidence through temporal relations to commit stable functional edges, and supplements visual loop-closure candidates with functional topology in scenes with repetitive appearance or degraded texture. Experiments show that Functional-SLAM efficiently constructs stable functional maps online, substantially improving runtime over offline methods while maintaining highly competitive accuracy. Compared with peer SLAM systems, it further improves pose estimation accuracy through functional-topology-assisted loop closure. The code is publicly available at https://github.com/Hbelief1998/Functional-SLAM-CoRL_2026.

</details>

#### 2026-09-07 - Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting

**Authors:** Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou
**Links:** [abs](https://arxiv.org/abs/2609.07231) - [pdf](https://arxiv.org/pdf/2609.07231)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** pose estimation, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Generalizable 6D Pose Estimation of Textureless Objects with Planar-based Gaussian Splatting
- 作者：Jie Lu, Hengtan Zhang, Li Gong, Pengpeng Wang, Xianjia Yu, Jinxiang Deng, Tomi Westerlund, Zhongxue Gan, Lirong Zheng, Zhuo Zou
- 出版日期：2026-09-07T08:49:10Z
- 分类：3D Reconstruction & Multi-view Geometry（主要）；Neural Scene Representations & Rendering（次要）
- 链接：[摘要](https://arxiv.org/abs/2609.07231) | [PDF](https://arxiv.org/pdf/2609.07231)

### 一句话总结
PG-Pose 利用基于平面约束的高斯泼溅重建和几何驱动的位姿优化，在无 CAD 模型条件下实现了对无纹理物体的高精度、可泛化的 6D 位姿估计。

### 研究问题
如何在没有 CAD 模型且物体缺乏纹理特征的条件下，实现可泛化的 6D 位姿估计——现有通用方法在低纹理物体上精度不足，主要受限于底层表示的几何约束不充分。

### 核心思路/方法
整体框架分为两个阶段：**离线表示提取阶段**，利用多视角 RGB 参考图和已知位姿提取三种对象表示，通过 3D 高斯泼溅重建并渲染高保真深度图后反投影生成 3D 点云；**在线位姿推理阶段**，先在输入图像与重建的 3D 点云之间进行 2D-3D 对应匹配估计初始位姿，再由 PGS-Refiner 执行迭代位姿优化。

### 主要贡献
- 提出 PG-Pose：结合基于平面的高斯泼溅（PGS）重建与几何驱动位姿优化的几何感知框架，用于无纹理物体的可泛化 6D 位姿估计。
- 在 OnePose-LowTexture 数据集上，PG-Pose 达到 94.2% 的平均 ADD(S)@0.1d 精度，较 SOTA 高斯泼溅类方法平均精度提升 2.1%。
- 在双机械臂工业机器人上完成实际部署，成功实现对未见物体的抓取任务，验证了实用价值。

### 局限性
摘要未提供足够信息。摘要未明确讨论方法在极端光照、严重遮挡、大规模工业场景中的性能上限，也未提及计算开销或实时性限制，以及解算失败或精度下降的具体边界条件。

### 阅读优先级
**高**。理由：本文针对无纹理物体 6D 位姿估计这一实际工业痛点，在无 CAD 模型条件下将高斯泼溅与几何优化结合，在数据集上取得 SOTA 提升，并在真实双机械臂抓取任务中得到验证，同时覆盖重建、渲染、位姿优化与机器人应用多个维度，对于从事三维视觉、机器人操作及可泛化感知的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimating the 6D pose of textureless objects without prior CAD models remains a critical challenge due to the lack of appearance features. While recent generalizable approaches alleviate the dependence on object-specific models, their performance on low-texture objects is often limited by insufficient geometric constraints in the underlying representations. In this work, we propose PG-Pose, a geometry-aware framework combining Planar-based Gaussian Splatting (PGS) reconstruction and Geometry-driven pose optimization. In the offline representation extraction stage, three distinct representations of the object are extracted from multi-view reference RGB images with known poses. PG-Pose reconstructs a 3D Gaussian representation and renders high-fidelity depth maps to generate 3D point clouds through back projection. In the online pose inference stage, the initial pose of the input image is estimated by 2D-3D correspondence matching between the input image and the reconstructed 3D point clouds, followed by a PGS-Refiner for iterative pose optimization. Evaluations on the OnePose-LowTexture datasets, PG-Pose achieves an average accuracy of 94.2% ADD(S)@0.1d, with a 2.1% improvement average accuracy compared with the state-of-the-art (SOTA) GS-based approach. To further demonstrate the effectiveness of PG-Pose for industrial robots in grasping tasks, we deploy it on a dual-arm industrial robot and successfully realize the grasping task on an unseen object.

</details>

#### 2026-09-06 - Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features

**Authors:** Ali Rafiaei, Michael Greenspan
**Links:** [abs](https://arxiv.org/abs/2609.06726) - [pdf](https://arxiv.org/pdf/2609.06726)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, feature matching, AR

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Back to the Feature: Zero-Shot 6DoF Pose Estimation via Dense Local Features  
- 作者：Ali Rafiaei, Michael Greenspan  
- 出版日期：2026-09-06  
- 分类：3D Reconstruction & Multi-view Geometry  
- 链接：https://arxiv.org/abs/2609.06726  

### 一句话总结
提出B2TFPose，一种仅依赖冻结DINOv3视觉Transformer提取稠密局部特征、无需训练的零样本6DoF姿态估计方法，在BOP基准上达到训练无关RGB方法的最优性能。

### 研究问题
如何在无需针对特定物体微调或额外训练的情况下，仅利用RGB图像对未见物体进行准确的6DoF姿态估计，并跨越合成到真实的域差距。

### 核心思路/方法
- 使用单个冻结的DINOv3视觉Transformer作为唯一预训练组件，提取可跨合成-真实域泛化的稠密patch级特征，回归经典局部特征匹配范式。  
- 三项关键技术：  
  1. 测地线非极大值抑制（geodesic NMS）选取视角多样的模板集，进行粗到细的对应匹配。  
  2. 渲染引导的再对应（RRC）：在估计姿态处合成物体特定视角，重新建立稠密2D-3D对应以锐化初始估计，无需额外学习参数。  
  3. 多掩膜假设选择策略：联合评分多个分割候选以解决分割歧义。

### 主要贡献
- 提出完全无需训练的零样本6DoF姿态估计方法B2TFPose。  
- 三项技术（测地线NMS模板选择、RRC细化、多掩膜假设选择）共同推动训练无关方法的最优水平。  
- 在BOP Benchmark七个核心数据集上，无细化时平均AR为40.7，细化后达56.4，超越训练方法GigaPose和GenFlow，且推理速度有竞争力。

### 局限性
摘要未提供足够信息（未提及失败案例、对遮挡/纹理缺失物体的表现、对DINOv3特征的依赖范围或计算资源需求等具体局限）。

### 阅读优先级
**高**  
理由：该方法在零样本训练无关RGB姿态估计上达到最先进水平，并超越了若干有训练方法，具备较强的实用性和新颖性；结合基础模型特征与经典匹配范式的研究方向具有启发意义，适合计算机视觉、机器人操作与增强现实相关研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We present B2TFPose, a training-free zero-shot method for 6DoF pose estimation of unseen objects from RGB images. Using a single frozen DINOv3 vision transformer as its only pretrained component within the pose estimation pipeline, B2TFPose extracts dense patch-level features that generalize across the synthetic-to-real domain gap without any task-specific fine-tuning, revisiting the classical local feature matching paradigm through the lens of large-scale self-supervised foundation models. Three contributions advance the training-free state of the art. A geodesic non-maximum suppression strategy retrieves a viewpoint-diverse template set for coarse-to-fine correspondence matching. Render-guided Re-Correspondence (RRC) synthesizes object-specific views at the estimated pose and re-establishes dense 2D-3D correspondences to sharpen the initial estimate without additional learned parameters. A multi-mask hypothesis selection strategy jointly scores competing segmentation candidates to resolve segmentation ambiguity. On the seven core datasets of the BOP Benchmark, B2TFPose achieves 40.7 mean AR without refinement and 56.4 with refinement, establishing state-of-the-art performance among training-free RGB methods and outperforming trained counterparts including GigaPose and GenFlow, at competitive inference speed.

</details>

#### 2026-09-04 - CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation

**Authors:** Samer Abualhanud, Max Mehltretter
**Links:** [abs](https://arxiv.org/abs/2609.05397) - [pdf](https://arxiv.org/pdf/2609.05397)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, autonomous driving

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CrossDepth: Geometry-Constrained Attention for Generalizable Multi-View Surround Depth Estimation
- 作者：Samer Abualhanud, Max Mehltretter
- 出版日期：2026-09-04
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.05397

### 一句话总结
CrossDepth 提出一种基于几何约束注意力的多视角环视深度估计方法，通过相机感知射线嵌入与跨图像注意力提升深度精度与跨图像一致性，并在 DDAD 和 nuScenes 上优于现有自监督方法。

### 研究问题
在多视角环视相机系统中，相邻图像重叠极小，导致大多数像素的深度需要依赖单目外观线索推断；然而这些线索在不同图像间可能表现不一致（受相机内参差异和每张图像感受野有限影响），从而造成跨图像深度估计不一致。

### 核心思路/方法
- 针对相机内参差异：在特征上引入逐像素的相机感知射线嵌入，让网络适应相机相关的外观线索变化。
- 针对感受野有限：通过几何约束的跨图像注意力机制，将每个像素的上下文扩展到自身图像之外，仅关注由标定系统导出的几何合理区域。
- 训练方式：全自监督，基于光度一致性（photometric consistency）进行训练。

### 主要贡献
- 提出相机感知射线嵌入，以缓解不同相机内参导致的单目线索解释差异。
- 设计几何约束的跨图像注意力，在标定约束下扩展像素上下文，提升跨图像深度一致性。
- 在 DDAD 和 nuScenes 上的域内与跨域评估中，整体深度精度和跨图像一致性均优于现有自监督方法。
- 代码已公开。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法面向自动驾驶环视深度估计，提出可泛化的跨图像一致性改进思路，属于应用导向的增量创新；但摘要未给出具体数值比较或消融细节，适用性与改进幅度需进一步阅读原文验证。若您关注多视角几何或自监督深度估计方向，可考虑优先阅读。

</details>

<details>
<summary>Abstract</summary>

Reliable 3D understanding of the surrounding environment is a core requirement for autonomous driving. Multi-view surround camera rigs provide broad scene coverage, but the spatially adjacent images typically overlap only minimally. Consequently, the depth of most pixels must be inferred from monocular appearance cues. These cues can appear differently across images and may therefore be interpreted differently by the depth estimation model. We target two main sources of cross-image inconsistency: differences in camera intrinsics and the limited receptive field of each image. We address the former by conditioning the features on per-pixel camera-aware ray embeddings, enabling the network to account for camera-dependent variations in monocular cues. We address the latter by extending each pixel's context beyond its own image through cross-image attention constrained to geometrically plausible regions, derived from the calibrated rig setup. The model is trained in a fully self-supervised manner based on photometric consistency. Evaluations on DDAD and nuScenes show improved overall depth accuracy and cross-image depth consistency over state-of-the-art self-supervised methods under in-domain and cross-domain evaluation. Code is available at https://abualhanud.github.io/CrossDepthPage/.

</details>

#### 2026-09-03 - Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction

**Authors:** Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chen Chiu, Yu-Lun Liu
**Links:** [abs](https://arxiv.org/abs/2609.04201) - [pdf](https://arxiv.org/pdf/2609.04201)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D reconstruction

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction
- 作者：Chin-Yang Lin, Yang-Che Sun, Cheng Sun, Fu-En Yang, Min-Hung Chen, Yen-Yu Lin, Wei-Chi Chiu, Yu-Lun Liu
- 出版日期：2026-09-03T17:59:53Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.04201

### 一句话总结
Scal3R 提出一种基于多参考相对位姿查询的在线 3D 重建方法，通过轻量可学习 token 与冻结骨干网络的非对称注意力注入，配合在线位姿图优化，显著抑制长视频场景下的累积漂移。

### 研究问题
在线 3D 重建模型在长视频上表现不佳，原因是将位姿回归到固定的首帧锚点会导致外推远超训练分布，微小漂移逐渐累积并放大为严重的几何崩溃。

### 核心思路/方法
- 观察到逐帧深度在重建失败时仍保持稳定，即骨干网络的局部几何完好，只有全局位姿头崩溃，基于这一解耦现象进行设计。
- 将在线重建重构为多参考相对位姿查询：使用约占总参数 1% 的轻量可学习 token，通过非对称注意力注入到完全冻结的骨干网络中，查询相对多个历史关键帧的位姿。
- 引入在线位姿图优化系统，结合回环检测（loop closure）以抑制长距离漂移。

### 主要贡献
- 揭示在线重建中局部几何（深度）与全局位姿解耦的失败模式，并据此设计新方法。
- 提出 Scal3R，利用冻结骨干+轻量 token 进行多参考相对位姿查询，训练效率高（单 GPU 8 小时收敛）。
- 在 KITTI 上将平均 ATE（绝对轨迹误差）较在线基线降低超过 60%。
- 在 Virtual KITTI、Sintel、TUM-Dynamic、ScanNet 和 7-Scenes 上达到最先进性能。

### 局限性
摘要未提供足够信息，无法确知方法在极端退化场景（如严重遮挡、纹理缺失）下的表现、对回环检测失败的敏感性、内存/推理速度开销、以及不同数据集间的泛化边界等细节。

### 阅读优先级
**高**。理由：该工作针对在线 3D 重建中长期存在的长视频漂移问题提供了新的问题洞察（几何-位姿解耦），方法设计轻量且训练高效，在多个基准上取得显著提升，兼具理论动机与实际应用价值。摘要信息完整，适合快速阅读以了解核心思想；若需复现或深入比较，需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Online 3D reconstruction models perform poorly on long videos. This happens because regressing poses relative to a fixed first-frame anchor forces extrapolation far beyond the training distribution. Small drifts accumulate and amplify into significant geometric collapse. However, we observe that per-frame depth remains stable throughout this failure. The backbone's local geometry remains intact; only the global pose head breaks down. Motivated by this decoupling, we introduce Scal3R. This approach reformulates online reconstruction as multi-reference relative pose querying. We use lightweight learnable tokens, which make up about ~1% of the parameters, and inject them into a completely frozen backbone via asymmetric attention. This setup queries poses relative to multiple past keyframes. An online pose-graph optimization system with loop closure suppresses long-range drift. Scal3R reaches convergence in 8 hours on a single GPU. It reduces the average ATE by over 60% on KITTI compared to the online baseline. It also achieves state-of-the-art performance across Virtual KITTI, Sintel, TUM-Dynamic, ScanNet, and 7-Scenes. Project page: https://linjohnss.github.io/scal3r/

</details>

#### 2026-09-03 - Stable and Scalable Bundle Adjustment of Holistic 3D Structures

**Authors:** Shaohui Liu, Rémi Pautrat, Daniel Barath, Richard Hartley, Viktor Larsson, Marc Pollefeys
**Links:** [abs](https://arxiv.org/abs/2609.04026) - [pdf](https://arxiv.org/pdf/2609.04026)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** bundle adjustment

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stable and Scalable Bundle Adjustment of Holistic 3D Structures
- 作者：Shaohui Liu, Rémi Pautrat, Daniel Barath, Richard Hartley, Viktor Larsson, Marc Pollefeys
- 出版日期：2026-09-03T16:08:03Z
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.04026

### 一句话总结
本文提出一个统一框架，将束调整从稀疏点/线扩展至包含高阶几何关系（如共面、平行）的整体3D结构，并通过将组约束建模为类相机实体、以2D重投影误差表达，从而在保持传统点BA稀疏性和数值稳定性的同时，提升3D结构丰富度与几何精度。

### 研究问题
如何将束调整从仅优化稀疏点（及线）扩展为联合优化高阶几何关系（如共面性、平行性、线框结构），同时避免计算成本显著增加和数值稳定性下降的问题。

### 核心思路/方法
- 引入分类法：将具有直接2D测量的可扩展几何特征（点、线）与编码高阶关系的“组”区分开，并证明“组”可在BA框架中建模为类相机实体。
- 通过2D重投影测量同时表达组约束和跨特征关联（点-线关联），构造组诱导与跨特征的重投影误差。
- 在Schur消元下保持经典点BA的稀疏结构，避免直接3D正则化导致的病态条件和稳定性劣化。

### 主要贡献
- 提出统一框架，可联合优化几何特征与高阶关系，并保持经典BA的稀疏结构。
- 从理论上说明高阶关系组可被建模为类相机实体。
- 通过组与跨特征的重投影误差公式化，避免直接3D正则化带来的稳定性问题。
- 实验证明运行时间与经典点BA相当，同时生成显著更丰富的3D结构并提升几何精度。

### 局限性
摘要未提供足够信息来具体说明方法的局限（如对特定场景的退化情况、合成/真实数据上的失败案例、超参数敏感性等）。

### 阅读优先级
**高**
理由：该工作直接将经典束调整扩展至整体3D结构联合优化，且宣称在运行时间与经典BA相当的前提下提升结果丰富度与精度，对于多视角几何和3D重建方向的研究者具有重要参考价值；摘要提供的方法思路较完整，适合进一步精读原文验证实验细节。

</details>

<details>
<summary>Abstract</summary>

Bundle Adjustment (BA) is a cornerstone of 3D computer vision and has benefited from decades of advances in sparse optimization and numerical methods. It was originally developed for jointly optimizing camera intrinsics, poses and sparse 3D points. While extensions incorporate lines and other primitives, integrating richer geometric structures such as parallelism, coplanarity, or wireframes often introduces significantly increased computational cost and reduced numerical stability. In this paper, we propose a unified framework that extends bundle adjustment to jointly optimize geometric features and higher-order relations. We first introduce a taxonomy that distinguishes scalable geometric features with direct 2D measurements (e.g., points and lines), from groups encoding higher-order relations (e.g., coplanarity, parallelism, etc.), where we show that groups can be modeled as camera-like entities within the bundle adjustment framework. Building on this formulation, we propose that both group constraints and cross-feature relations (i.e., point-line associations) can be expressed through 2D reprojection measurements. By formulating group-induced and cross-feature reprojection errors, we preserve the sparsity structure of classical point-based BA under Schur elimination, while avoiding direct 3D regularization that degrades the conditioning and stability. Experiments on both real-world and synthetic datasets demonstrate runtime performance comparable to classical point-only bundle adjustment, while producing significantly richer 3D structures and improved geometric accuracy.

</details>

#### 2026-09-03 - Automated Weld Seam Recognition and 3D Mapping for Robotic Post Processing Using Photogrammetry and Semantic Segmentation

**Authors:** Augustin Raju, Abilash Madavath, Chandra Yuvesh Aubeeluck, Nicolas Pyschny, Felix Hackelöer, Florian Zwanzig
**Links:** [abs](https://arxiv.org/abs/2609.03970) - [pdf](https://arxiv.org/pdf/2609.03970)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** photogrammetry, 3D mapping, mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Automated Weld Seam Recognition and 3D Mapping for Robotic Post Processing Using Photogrammetry and Semantic Segmentation
- 作者：Augustin Raju, Abilash Madavath, Chandra Yuvesh Aubeeluck, Nicolas Pyschny, Felix Hackelöer, Florian Zwanzig
- 出版日期：2026-09-03T15:07:52Z
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03970

### 一句话总结
本文提出一种基于多视角图像语义分割与摄影测量的实验性视觉管线，用于焊缝的粗略定位与三维映射，作为高精度测量前的预定位阶段，以减少机器人在后处理任务中的扫描工作量与数据量。

### 研究问题
如何在大尺寸工件场景下，通过低成本、高效的视觉方法快速近似定位焊缝，且无需使用激光扫描仪或结构光传感器进行全表面高精度扫描，从而为机器人后处理（如打磨、精整、检测）提供引导。

### 核心思路/方法
1. 从多个视角拍摄工件图像。
2. 使用语义分割模型从图像中识别焊缝区域。
3. 利用摄影测量技术对工件进行三维重建。
4. 将图像中识别到的焊缝像素投影到重建的三维模型上，实现焊缝在三维空间中的映射与粗略定位。

该管线作为高精度测量前的预筛阶段，旨在缩小后续精确扫描的感兴趣区域。

### 主要贡献
- 提出一种面向机器人后处理的焊缝识别与三维映射的实验性视觉管线。
- 结合语义分割与摄影测量，实现对焊缝的近似空间定位，避免了高精度传感器全表面扫描带来的时间与数据开销。
- 强调该方案作为高精度测量前预阶段的实用性，可提升整体数据采集效率。

### 局限性
摘要未提供足够信息，包括：具体实验对象规模、焊缝分割精度、三维映射误差、与激光扫描的定量对比、计算耗时、场景光照或遮挡条件等细节均未在摘要中说明。摘要明确指出该方法是“experimental”且目标是“approximate localization”，且需在高精度测量前使用，具体精度性能数据无法从摘要获取。

### 阅读优先级
**中**
理由：论文聚焦于机器人后处理中的焊缝预定位，结合了语义分割与摄影测量，思路有一定工程应用价值。但摘要表明其为“experimental”的预定位阶段，且未给出定量性能结果，属于一种辅助性管线而非核心精度突破，适合对机器人视觉引导、三维重建与分割结合应用感兴趣的读者快速浏览。若追求高精度方法或详细对比实验，则优先级可下调。

</details>

<details>
<summary>Abstract</summary>

Accurate identification of weld seam geometries is essential for automated robotic post processing operations such as grinding, finishing, and inspection. For large workpieces, complete surface scanning using high precision laser scanners or structured light sensors can be time consuming and often generates substantial amount of data that are not relevant. This paper presents an experimental vision based pipeline for the approximate localization of weld seams. This serves as a preliminary stage before high precision measurement. The proposed approach aims to reduce the overall scanning effort and data acquisition efficiency. The proposed method includes capturing images of the workpiece from multiple viewpoints, identifying weld seams from the images using semantic segmentation, reconstructing the workpiece using photogrammetry, and projection of identified weld seams into the reconstructed model.

</details>

#### 2026-09-03 - OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping

**Authors:** Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang
**Links:** [abs](https://arxiv.org/abs/2609.03919) - [pdf](https://arxiv.org/pdf/2609.03919)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** 3D mapping, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping
- 作者：Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang
- 出版日期：2026-09-03
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.03919

### 一句话总结
OctWorld 提出一种基于八叉树3D记忆（OctMap）的视频扩散框架，从单张图像沿用户指定相机轨迹生成长距离、空间一致且可探索的高保真场景视频。

### 研究问题
如何解决长距离视频生成中——即当相机路径延伸、视角覆盖广泛且重新访问已生成区域时——保持全局空间一致性的挑战。

### 核心思路/方法
- 提出 OctMap：一种可扩展、空间自适应的3D记忆模块，渐进地将生成的视觉观测及其对应的深度图融合进全局表示。
- OctMap 在动态稀疏八叉树中执行 TSDF 融合，空间分辨率根据图像证据自适应变化，从而在不同场景尺度下保持几何和外观细节，同时维持较低内存开销。
- 框架整体为自回归式视频扩散模型：以单张图像为起点，沿用户指定轨迹迭代生成内容，并借助持久化3D记忆维持跨帧一致。

### 主要贡献
- 提出 OctWorld，一个具备持久3D记忆的长距离、世界一致视频生成框架。
- 设计 OctMap——基于稀疏八叉树与 TSDF 融合的可扩展3D记忆，兼顾自适应分辨率与内存效率。
- 实验表明 OctWorld 在现有基准及长距离生成挑战性设置上优于先前方法，并验证 OctMap 相比基于点云缓存和固定分辨率 TSDF 体素表示的显著优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
- 理由：论文针对视频生成中长距离空间一致性的核心难题，提出结构新颖的八叉树+TSDF融合3D记忆方案，且研究发表于2026年，方法具有明显创新性。适合关注生成式3D场景、世界模型及视频扩散模型的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

We present OctWorld, a video diffusion framework with persistent 3D memory for generating explorable, world-consistent, and high-fidelity visual scenes. Given a single image, OctWorld performs stable autoregressive world generation along user-specified camera trajectories. We focus on long-range generation, characterized by extended camera paths and wide viewpoint coverage, where preserving spatial consistency is particularly challenging when previously generated regions are revisited. To address this problem, we introduce OctMap, an extensible and spatially adaptive 3D memory that progressively fuses generated visual observations and their corresponding depth maps into a global representation. OctMap employs TSDF fusion within a dynamic sparse octree whose spatial resolution adapts to image evidence. This design preserves geometric and appearance details across diverse scene scales while maintaining low memory overhead. Experiments demonstrate that OctWorld generates long-range, spatially consistent videos and outperforms prior methods on both existing benchmarks and challenging long-range generation settings. OctMap also provides clear advantages over point-based caches and fixed-resolution TSDF volumes. Project page: https://maxtirerror.github.io/octworldpage/

</details>

#### 2026-09-03 - STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction

**Authors:** Bocheng Li, Wenjuan Zhang, Jie Pan. Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang
**Links:** [abs](https://arxiv.org/abs/2609.03447) - [pdf](https://arxiv.org/pdf/2609.03447)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** surface reconstruction, photogrammetry, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：STARS-GS: Structure-Aware Regularized Gaussian Splatting for Large-Scale Aerial Surface Reconstruction
- 作者：Bocheng Li, Wenjuan Zhang, Jie Pan, Dongxu Han, Xuesong Ma, Yiling Yao, Yaning Wang
- 出版日期：2026-09-03
- 分类：3D Reconstruction & Multi-view Geometry（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.03447

### 一句话总结
本文提出STARS-GS，一种结构感知正则化的3D高斯泼溅框架，通过改进场景划分、邻域高斯组织与自适应表面正则化，显著提升大规模航拍影像的3D表面重建精度。

### 研究问题
如何解决大规模复杂场景下基于3D高斯泼溅的表面重建存在三大挑战：（1）场景划分可能切断连续结构；（2）几何约束仅关注单个高斯而忽略其局部组织；（3）统一正则化难以适应异质几何结构。

### 核心思路/方法
- 结构感知场景划分策略：在划分时尽量保持连续场景结构，并通过边界细化减少跨区域几何不一致与拼接伪影。
- 邻域感知高斯组织：将几何约束从单个图元扩展到邻域组织，促使高斯更好地贴合局部表面几何。
- 自适应表面正则化：根据局部几何特征动态调整正则化强度，在结构化区域保持几何一致性，在非结构化区域保留合理变异。

### 主要贡献
- 提出STARS-GS框架，综合解决场景划分、高斯邻域组织与自适应正则化三方面问题。
- 在大规模航拍摄影测量基准上，平均F1分数从次优方法的0.640提升至0.698，相对提升约9.1%，验证了几何精度与表面完整性的有效改进。

### 局限性
摘要未提供足够信息。摘要仅提及实验在公开基准上验证优于现有高斯类方法，但未说明计算开销、内存消耗、对超参数敏感性、极端场景（如强遮挡/弱纹理区域）表现等潜在限制。

### 阅读优先级
**高**。该工作聚焦于当前热门的3D高斯泼溅技术在大规模航拍表面重建中的实际落地问题，提出了三项针对性改进且有效果量化提升（F1相对提高9.1%），对从事遥感三维重建、城市建模及神经渲染相关研究的读者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Large-scale 3D surface reconstruction from aerial imagery is fundamental to geospatial mapping and urban modeling. Recent advances in 3D Gaussian Splatting (3DGS) have demonstrated considerable potential for this task. However, existing methods still face three major challenges in large and complex scenes: scene partitioning may split continuous scene elements across independently optimized sub-regions; geometric constraints mainly focus on the attributes of individual Gaussians while overlooking their local organization; and uniform regularization struggles to accommodate heterogeneous geometric structures. To address these issues, we propose STARS-GS, a structure-aware 3DGS framework for large-scale surface reconstruction. First, we introduce a structure-aware scene partitioning strategy that better preserves continuous scene structures during partitioning and reduces cross-region geometric inconsistencies and stitching artifacts through boundary refinement. Second, we develop neighborhood-aware Gaussian organization that extends geometric constraints from individual primitives to their neighborhood organization, encouraging Gaussians to better conform to local surface geometry. Third, we introduce adaptive surface regularization that adjusts the regularization strength according to local geometric characteristics, promoting geometric consistency in structured regions while preserving plausible variations in unstructured regions. Extensive experiments on large-scale aerial photogrammetry benchmarks demonstrate that STARS-GS consistently outperforms the evaluated Gaussian-based methods in surface reconstruction. It increases the average F1-score from 0.640 for the second-best method to 0.698, corresponding to a relative improvement of approximately 9.1\%, demonstrating effective improvements in geometric accuracy and surface completeness.

</details>

## Neural Scene Representations & Rendering

### 2026-09

#### 2026-09-08 - PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding

**Authors:** Xiang Liu, Jinxiang Wang, Bin Chen, Zimo Liu, Mingyao Hong, Jiawei Li, Yaowei Wang, Shu-tao Xia
**Links:** [abs](https://arxiv.org/abs/2609.09020) - [pdf](https://arxiv.org/pdf/2609.09020)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PIC: Revisiting INR for Image Coding with Fast Encoding and Sub-Millisecond Decoding
- 作者：Xiang Liu, Jinxiang Wang, Bin Chen, Zimo Liu, Mingyao Hong, Jiawei Li, Yaowei Wang, Shu-tao Xia
- 出版日期：2026-09-08T16:52:00Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.09020

### 一句话总结
本文提出了一种前馈式隐式神经表示图像编码架构PIC，在保持实用编码速度的同时实现了超低延迟解码，并首次达到与JPEG在率失真性能和解码速度上同时可比或更优的学习型图像编解码器水平。

### 研究问题
如何克服基于隐式神经表示（INR）的图像编码方法中编码速度慢和解码效率利用不足的问题，使其具备实际应用可行性。

### 核心思路/方法
- 提出前馈式INR图像编码架构PIC：通过单次前向传播计算INR网络所需的全部信息，实现20 FPS的编码速度。
- 设计高度优化的解码器：达到2000 FPS解码速度，显著超过JPEG。
- 在率失真（RD）性能与JPEG相当的前提下，实现解码速度的超越。

### 主要贡献
- 提出PIC编码架构，将INR图像编码的编码速度提升至20 FPS（实时可用级别）。
- 实现亚毫秒级（2000 FPS）超高速解码，显著超越JPEG解码速度。
- 据作者所述，这是首个在RD性能和解码速度上同时优于或可比JPEG，且保持实用编码速度的学习型图像编解码器。
- 开源代码：https://github.com/actcwlf/PIC

### 局限性
摘要未提供足够信息。具体局限性评估（如与更多现代学习型编解码器的对比、泛化性、不同分辨率/内容类型的表现等）未在摘要中说明。

### 阅读优先级
**高**
理由：该工作首次声称在学习型图像编码中同时突破编码速度、解码速度和RD性能三重瓶颈，且直接与JPEG基准对比，对神经表示用于实际图像压缩的方向具有重要参考价值；同时公开代码，便于复现和进一步研究。

</details>

<details>
<summary>Abstract</summary>

Implicit neural representation (INR) has achieved remarkable progress in novel view synthesis and image/video coding in recent years.Compared to conventional end-to-end image codecs, INR-based compressors demonstrate significant advantages in decoding complexity. However, their practical application has been hindered by the inferior encoding speed and underutilized decoding efficiency.In this work, we propose a feedforward INR image coding architecture, Practical INR Image Codec (PIC), that computes all the necessary information for INR network in a single forward pass, achieving an encoding speed of 20 FPS. Additionally, we implement a highly optimized decoder that reaches 2000 FPS decoding speed, significantly surpassing JPEG's performance at comparable rate-distortion (RD) performance. To the best of our knowledge, this work presents the first learning-based image codec that simultaneously outperforms or is comparable with JPEG in both RD performance and decoding speed while maintaining practical encoding speed. Code is available at https://github.com/actcwlf/PIC.

</details>

#### 2026-09-08 - CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation

**Authors:** Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang
**Links:** [abs](https://arxiv.org/abs/2609.08730) - [pdf](https://arxiv.org/pdf/2609.08730)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, Gaussian primitive, novel view synthesis, view synthesis, differentiable rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation
- 作者：Bingxian Li, Yilong Li, Jingliang Peng, Peng-Shuai Wang, Fei Zhu, Guozheng Li, Chi Harold Liu, Guoping Wang, Bo Pang
- 出版日期：2026-09-08T13:26:32Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.08730

### 一句话总结
本文提出CVT-GS，一种无需优化的后处理框架，通过对已训练的3D高斯泼溅场景进行几何感知的质心Voronoi剖分和轻量神经单元合并，实现上百倍高斯点压缩且保持渲染质量。

### 研究问题
如何在不重新训练、不修改架构的前提下，直接压缩已训练好的3D高斯泼溅（3DGS）场景，以降低存储与计算开销，同时保持视觉保真度。

### 核心思路/方法
- 使用几何感知的质心Voronoi剖分（CVT）在高斯中心上构建空间连贯的单元。
- 设计轻量神经单元合并器，在可微渲染监督下为每个单元预测一个具有高度代表性的高斯原语。
- 将场景简化建模为感知渲染的多对一合并过程，而非朴素剪枝；输出仍为标准3DGS格式，可直接在现有渲染器中使用。

### 主要贡献
- 提出首个面向已训练3DGS场景的免训练后处理简化框架，无需侵入式训练或逐场景微调。
- 引入CVT聚类+神经合并的两阶段设计，兼顾几何空间结构感知与渲染质量。
- 在多种数据集上验证有效性；在将高斯点数压缩100倍时，处理速度比SOTA快12倍，PSNR提升1.3 dB。

### 局限性
摘要未提供足够信息：未说明方法对不同类型的场景（如复杂几何/高频纹理）的适应性，未提及可能的伪影、超参敏感性，也未报告在极低压缩比下或大场景中的具体性能边界。

### 阅读优先级
**高**。理由：该工作针对3DGS存储开销大的核心痛点提出免训练的通用后处理压缩方案，应用价值高；技术路线（CVT+神经合并）具有新颖性；实验显示在100倍压缩下仍有速度与质量上的显著优势，适合从事神经渲染、三维场景压缩等相关方向的研究者优先关注。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for real-time novel view synthesis, rendering high-fidelity scenes often relies on a massive number of Gaussian primitives, incurring substantial storage and computational overhead. Existing simplification techniques are largely intrusive, requiring training-time pruning, architectural modifications, or computationally expensive per-scene fine-tuning. These drawbacks limit their deployment on off-the-shelf pretrained models. In this paper, we propose CVT-GS, a novel optimization-free post-hoc simplification framework that directly compresses trained 3DGS scenes without sacrificing visual fidelity. Our approach first constructs spatially coherent cells over Gaussian centers via a geometry-aware Centroidal Voronoi Tessellation (CVT). Subsequently, a lightweight neural cell merger predicts the geometry and appearance of a single, highly representative Gaussian primitive for each cell under differentiable rendering supervision. By formulating simplification as a rendering-aware many-to-one merging process rather than naive primitive pruning, CVT-GS outputs a standard 3DGS scene that is seamlessly compatible with existing renderers. Experiments on various datasets demonstrate the superiority of our method. Notably, when achieving a 100-fold reduction in Gaussian points, our method operates 12 times faster than state-of-the-art methods while improving the PSNR by 1.3 dB.

</details>

#### 2026-09-07 - TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views

**Authors:** Harish N Sathishchandra, Philippos Mordohai
**Links:** [abs](https://arxiv.org/abs/2609.07734) - [pdf](https://arxiv.org/pdf/2609.07734)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, novel view synthesis, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TV-SGS: Gaussian Splatting with Geometric Information Propagation via Tensor Voting under sparse views
- 作者：Harish N Sathishchandra, Philippos Mordohai
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07734

### 一句话总结
本文提出一种基于张量投票的3D几何损失，使3D高斯溅射中的各个高斯在稀疏视图下能够直接通信，从而提升重建场景的几何精度与渲染质量。

### 研究问题
在稀疏视图条件下，现有高斯溅射方法中各高斯之间仅通过像素投影间接相互影响，缺乏直接的结构通信，导致重建的3D几何结构不够精确。本文旨在解决这一几何监督不足的问题。

### 核心思路/方法
- 引入经典张量投票（Tensor Voting）方法，其原本用于从噪声输入中推断结构，本文将其改造为测试时优化过程中的几何监督信号。
- 提出一类不依赖于渲染的新型3D损失，用于直接对各高斯形成的3D结构进行约束。
- 该3D损失可与文献中几乎所有已有损失组合使用，并易于集成到多种现有高斯溅射骨干网络（backbone）中。
- 在测试优化阶段，通过张量投票促进不同高斯之间的直接信息传播，从而提升整体场景几何的一致性与准确性。

### 主要贡献
- 提出一种使各高斯能够直接通信的新机制，增强了它们在3D空间中形成的几何结构。
- 首次将张量投票适配为高斯溅射中测试时优化的几何监督工具，实现更精确的场景几何。
- 引入一类通用的、无需渲染的3D损失，能够与主流现有损失兼容并插入多种骨干。
- 在DTU和Tanks-and-Temples数据集上的实验表明，相比骨干方法，TV-SGS改善了输出几何，同时保持或提升了渲染质量。

### 局限性
摘要提供了实验的整体结论，但未提供以下信息：具体的基线方法细节、各数据集上的定量指标（如PSNR/SSIM数值）、不同视图稀疏程度的实验设置、计算开销、张量投票在训练/推理各阶段的详细实现，以及该方法在极稀疏（如仅2-3视图）情况下的表现边界。以上均属于摘要未提供足够信息。

### 阅读优先级
**高**
- 理由：稀疏视图下的三维重建是当前神经渲染领域中的活跃难点，本文提出一种不依赖渲染的3D损失，具有较好的通用性和可插拔性，方法思路新颖（张量投票与高斯溅射结合），且实验覆盖多个公开数据集，对从事三维几何优化或神经渲染的研究者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Gaussian Splatting has been effective in inferring scene representations that excel in novel view synthesis. Multiple splats cooperate seamlessly to synthesize the pixels of novel views and are jointly optimized even though they only affect each other indirectly, via pixels they project to in common. We present an approach that enables direct communication among splats to enhance the geometric structures they form in 3D. This is accomplished by Tensor Voting, which was originally designed to infer structures from noisy inputs and has been adapted here to provide supervision during test-time optimization, leading to more accurate scene geometry. We introduce a new class of 3D losses that do not rely on rendering and can be combined with essentially all losses previously reported in the literature. Our 3D losses are especially effective when the input views are sparse and geometric regularization is essential due to limited supervision from the images. Our method is easy to integrate with a diverse set of backbones, and our experiments on the DTU and Tanks-and-Temples datasets demonstrate that TV-SGS improves the geometry of the outputs compared to the backbone, while maintaining or improving rendering quality.

</details>

#### 2026-09-07 - Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat

**Authors:** Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal
**Links:** [abs](https://arxiv.org/abs/2609.07557) - [pdf](https://arxiv.org/pdf/2609.07557)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, novel view synthesis, view synthesis, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Heat Kernel Textures: the Geodesic Gaussians That Do Not Splat
- 作者：Simone Foti, Caner Korkmaz, Stefanos Zafeiriou, Tolga Birdal
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07557

### 一句话总结
本文提出一种基于热核（Heat Kernel）的纹理表示方法 HKTex，在三角网格曲面上直接定义各向异性热核作为高斯核的测地线等价物，以消除 UV 映射的弊端并降低显存占用。

### 研究问题
如何设计一种无需 UV 展开、直接在任意三角网格曲面上定义的新型纹理表示，克服 UV 映射中存在的空间浪费、接缝、形变、顶点复制和分辨率不均等问题，同时降低内存占用。

### 核心思路/方法
- 受 3D Gaussian Splatting 启发，将“纹理”从传统的 UV 贴图重新定义为定义在网格曲面上的热核纹理。
- 基于离散黎曼几何，在任意以三角网格离散化的流形曲面上，使用各向异性热核作为高斯核的测地线等价物。
- 核的位置优化与自适应致密化策略全部重新设计，直接在待纹理化对象的曲面表面上进行。
- 与基于物理的渲染器完全集成，可从现有纹理或多视角图像进行优化。

### 主要贡献
- 提出 HKTex，一种全新的纹理表示，完全消除 UV 展开过程及其相关缺陷。
- 将热核作为测地线高斯核引入纹理建模，形成与曲面几何直接关联的表示。
- 在曲面表面而非参数域上重新定义优化与自适应致密化策略。
- 表示与物理渲染器集成，支持从已有纹理或多视图图像优化。

### 局限性
摘要未提供足够信息。文中未报告定量实验、对比基线、具体性能指标或失败场景等局限性内容。

### 阅读优先级
中。该工作将 3DGS 思想引入纹理领域，创新点明确且具有实用性潜力，但摘要中未给出实验证据；建议对纹理映射、几何处理或 3DGS 扩展方向感兴趣的读者优先阅读，否则可延后。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has recently revolutionised novel view synthesis as well as many other 3D vision methods and applications. Drawing inspiration from this representation, we now rethink textures to overcome the main issues of UV mapping while considerably lowering their memory footprint. Heat Kernel Textures (HKTex) eliminate UV unwrapping as well as their persistent issues of wasted UV space, seams, distortions, vertex-duplication, and varying resolution. Grounded in discrete Riemannian geometry and intrinsically defined on any manifold surface discretised as a triangular mesh, HKTex uses anisotropic heat kernels as geodesic equivalents to Gaussians. Like our kernels, also the optimisation of their position and the adaptive densification strategies were redefined to operate on the surface of the object to be textureised. Our novel representation is also fully integrated with a physically based renderer and can be optimised either from existing textures or multi-view images. Our project page and code are available at circle-group.github.io/research/HeatKernelTextures.

</details>

#### 2026-09-07 - RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting

**Authors:** Hejun Wang, Jinxi Li, Junwei Jiang, Shiwei Mao, Hu Cheng, Shouwang Huang, Bo Yang
**Links:** [abs](https://arxiv.org/abs/2609.07414) - [pdf](https://arxiv.org/pdf/2609.07414)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** inverse rendering, relighting, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting
- 作者：Hejun Wang, Jinxi Li, Junwei Jiang, Shiwei Mao, Hu Cheng, Shouwang Huang, Bo Yang
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07414

### 一句话总结
本文提出一种基于视频基础模型改进的前馈生成式Transformer——RelightFormer，直接从单视图或多视图输入预测目标光照下的物体重打光结果，不依赖显式的逆渲染或固有属性估计，并构建了大规模LOD数据集以支撑训练与泛化。

### 研究问题
传统图像重打光依赖复杂的逆渲染流程，存在病态优化问题；而单图像生成模型缺乏多视图线索，难以理解3D几何与材质交互。因此，本文旨在直接实现单/多视图前馈重打光，绕过显式固有属性分解。

### 核心思路/方法
- 采用前馈生成式Transformer架构，从视频基础模型适配而来，支持直接、前馈式的单/多视图图像重打光。
- 设计**潜在光照模块**（latent illumination module），通过交叉注意力将目标环境贴图动态注入空间特征中。
- 使用**置换不变的位置编码**，以对称方式处理无序多视图输入，避免顺序偏差。
- 构建大规模数据集**Laval Objaverse Dataset (LOD)**，包含90K个物体和39K种不同光照环境，用于训练数据驱动模型。

### 主要贡献
- 提出首个完全绕过显式固有属性估计的前馈生成Transformer，统一处理单视图和多视图重打光。
- 引入动态光照注入的潜在光照模块与置换不变编码机制，提升多视图处理的鲁棒性。
- 构建大规模多视图重打光数据集LOD（90K物体，39K光照）。
- 实验证明在视觉质量、真实感重打光效果以及单视图、多视图、新视角重打光任务的零样本泛化方面均达到当前最优水平。

### 局限性
- 摘要说明了方法的优点和数据集构建，但未提供训练/推理耗时、内存消耗等效率信息。
- 未提及模型对极端光照、复杂材质或输入遮挡等边缘情况的失败案例或边界条件分析。
- 零样本泛化能力虽有展示，但尚未报告对真实世界拍摄图像的验证结果。
- 摘要未提供足够信息以评估该方法与传统优化方法在鲁棒性上的定量对比细节。

### 阅读优先级
**高**

理由：该论文瞄准图像重打光中的核心痛点（逆渲染病态性、单视图信息不足），提出了一种绕过显式分解的全新前馈生成框架，结合大规模自建数据集并展示多任务SOTA及零样本泛化表现。研究价值和技术新颖性均较强，对3D视觉、生成模型和光照编辑领域的研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

Image relighting is traditionally tackled via complex inverse rendering pipelines, which suffer from ill-posed optimization, or single-image generative models that ignore crucial multi-view cues necessary for understanding 3D geometry and material interactions. To address these limitations, we introduce a feed-forward generative Transformer for direct single- and multi-view image relighting that entirely bypasses explicit intrinsic property estimation. Adapted from a video foundation model, our architecture features a latent illumination module that dynamically injects target environment maps into spatial features via cross-attention. Furthermore, we employ permutation-invariant positional encodings to symmetrically process unordered multi-view inputs without sequential bias. To train this robust data-driven model, we construct the massive Laval Objaverse Dataset (LOD), comprising 90K objects and 39K unique illuminations. Extensive experiments demonstrate state-of-the-art visual quality, photorealistic relighting quality, and strong zero-shot generalization across single-view, multi-view, and novel-view relighting tasks.

</details>

#### 2026-09-07 - From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment

**Authors:** Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens
**Links:** [abs](https://arxiv.org/abs/2609.07346) - [pdf](https://arxiv.org/pdf/2609.07346)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, radiance field, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, rendering, radiance, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Explicit References to Scene Manifolds: Distributional Fidelity and Realism for Radiance Field Quality Assessment
- 作者：Saeed Mahmoudpour, Gi-Mun Um, Hyon-Gon Choo, Peter Schelkens
- 出版日期：2026-09-07
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.07346

### 一句话总结
本文提出SCODA——一种轻量级、场景条件化的无参考质量评估方法，将辐射场（如3DGS、NeRF）的质量评估从显式图像对比转向场景流形建模，通过深度特征空间中的分布保真度与弱监督判别器给出的真实性信号联合打分。

### 研究问题
如何在不依赖对齐参考图像、且无法稳定选取近邻参考视角的情况下，对辐射场（3D Gaussian Splatting、NeRF等）生成的新视角图像进行可靠的感知质量评估，尤其是在宽基线、任意轨迹和姿态的评估场景中。

### 核心思路/方法
- 抛弃逐图像的比较范式，转向场景级建模：将每个场景的高质量观测表示为深度特征空间中的多元高斯分布，构造“语义保真度”分数，度量测试视图偏离该分布的程度。
- 引入一个弱监督的、面向失真的补丁鉴别器，提供互补的“真实性”信号。
- 通过无监督有界融合策略将以上两种线索结合为最终质量分数。
- 方法为轻量级且场景条件化，不要求对齐参考图，也无需固定的近邻参考视角选择。

### 主要贡献
- 提出SCODA框架，将辐射场质量评估从显式图像对比范式转化为场景流形建模范式。
- 设计基于场景分布的语义保真度指标与弱监督失真感知真实性指标的互补组合，并通过无监督方式融合。
- 在多个基准上验证了该方法与人类主观判断的高度一致性，以及在GS和NeRF生成视图与轨迹上的泛化性（摘要提供总体结论，未提供具体数值）。
- 开源代码（https://gitlab.com/saeedmp/scoda）。

### 局限性
摘要未提供足够信息。（未给出实验数据集规模、失败案例、计算开销对比或对无场景先验时的退化分析等。）

### 阅读优先级
**中。** 该工作针对辐射场质量评估这一较新但专门的方向，提出了范式转变（从参考对比到场景分布建模），对从事3DGS/NeRF渲染质量评测或感知优化研究的读者有参考价值；但摘要未展示具体实验数据和与SOTA的量化对比，影响对其性能的直观判断。若不在该细分领域则可暂缓阅读。

</details>

<details>
<summary>Abstract</summary>

Radiance field representations such as 3D Gaussian Splatting (3DGS) enable high-quality novel view synthesis but can introduce complex, view-dependent artifacts from reconstruction, rendering, and compression. Reliable perceptual quality assessment (QA) is thus essential for evaluating rendered views and guiding the design of perceptually faithful scene representations. Existing full-reference QA metrics require an aligned reference image, while recent cross-reference metrics relax this requirement by comparing a test view with non-aligned references. However, under wide-baseline radiance field settings, selecting a reliable nearby reference can be difficult, particularly when evaluating views along arbitrary trajectories and poses. We propose SCODA, a lightweight scene-conditioned objective QA method that shifts QA from explicit image-to-image comparison to scene-manifold modeling. High-quality observations of each scene are represented as a multivariate Gaussian distribution in deep feature space, producing a semantic fidelity score that measures deviation from the scene distribution. A weakly-supervised distortion-aware patch discriminator provides a complementary realism signal, and both cues are combined through an unsupervised bounded fusion strategy. Experiments on multiple benchmarks show strong agreement with human judgments and robust generalization across GS- and NeRF-generated views and trajectories. Code is publicly available at https://gitlab.com/saeedmp/scoda.

</details>

#### 2026-09-07 - LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure

**Authors:** Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü
**Links:** [abs](https://arxiv.org/abs/2609.07274) - [pdf](https://arxiv.org/pdf/2609.07274)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** SLAM, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LightSplat: Real-Time High-Fidelity 3D Gaussian SLAM with Loop Closure
- 作者：Junze Bao, Ye Gao, Yiming Huang, Xiaolong Yu, Chen Dong, Qing Gao, Wei Wang, Jinhu Lü
- 出版日期：2026-09-07T09:37:03Z
- 分类：神经场景表示与渲染（主）；三维重建与多视角几何（副）
- 链接：https://arxiv.org/abs/2609.07274

### 一句话总结
LightSplat 提出一种混合表征的 RGB-D SLAM 框架，通过稀疏特征加速追踪与双线程稠密高斯子图构建，实现支持回环检测的高保真实时三维高斯建图。

### 研究问题
现有 3D Gaussian Splatting（3DGS）SLAM 系统在实际部署中面临运行性能不足和地图可适应性差的问题，难以满足真实场景对实时性与重建质量的双重需求。

### 核心思路/方法
- 采用混合表征：局部稀疏特征用于快速稳健的追踪，双线程后端渐进构建稠密高斯子图。
- 实现在线回环检测：通过特征加速的 3DGS 配准，并利用位姿图优化来修正整体地图一致性。
- 最终在线重建高保真高斯地图，面向实际相机运动场景运行。

### 主要贡献
- 提出 LightSplat，一种兼顾追踪速度与稠密重建精度的 RGB-D SLAM 框架。
- 首次（据摘要所述）在 3DGS SLAM 中实现基于特征加速的在线回环闭合与位姿图优化。
- 在多个数据集和真实机器人平台上验证，重建质量接近当前最优水平，能适应实际相机运动，平均帧率达 8 FPS。

### 局限性
摘要未提供足够信息（例如：未提及对计算资源的具体需求、在极端运动或大场景下的退化情况、与最先进方法的具体量化差距等）。

### 阅读优先级
**高**。理由：该工作面向 3DGS SLAM 中关键的实时性与回环闭合问题，提出了工程上可行的混合架构与在线优化方案，实验覆盖多数据集与真实平台，对从事神经渲染与实时稠密建图的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

SLAM systems based on 3D Gaussian Splatting (3DGS) have recently demonstrated promising reconstruction accuracy for dense 3D scene representations. However, current 3DGS systems struggle to meet the strict demands of real-world deployments due to severe limitations in operational performance and map adaptability. To this end, we propose LightSplat, a hybrid-representation RGB-D SLAM framework. It synergizes local sparse features for robust and fast tracking with a dual-thread backend that progressively constructs dense Gaussian submaps. Crucially, we enable online loop closure through feature-accelerated 3DGS registration, refining overall map consistency through pose graph optimization. Ultimately, LightSplat achieves the online reconstruction of high-fidelity Gaussian map. Extensive experiments on multiple datasets and real-world robotic platform demonstrate that our method achieves near state-of-the-art reconstruction quality and the capability to accommodate practical camera motions, maintaining an average framerate of 8 FPS. Overall, LightSplat provides an efficient and robust foundation for deploying high-fidelity 3DGS in real-world environments.

</details>

#### 2026-09-07 - PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis

**Authors:** Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao
**Links:** [abs](https://arxiv.org/abs/2609.06948) - [pdf](https://arxiv.org/pdf/2609.06948)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3DGS, neural rendering, view synthesis, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis
- 作者：Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao
- 出版日期：2026-09-07T02:34:51Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.06948

### 一句话总结
PRG-Fusion 提出一种融合重建证据与生成先验的驾驶视图合成框架，通过区域划分策略（保留、修复、生成）来实现沿新轨迹的高保真视频生成。

### 研究问题
如何在自动驾驶场景中沿指定新轨迹合成逼真的驾驶视频，同时兼顾重建方法的几何一致性与生成方法的视觉真实感与灵活性。

### 核心思路/方法
- 融合两类方法优势：重建类方法（如神经渲染）几何一致但容易产生伪影和内容缺失；生成类方法可沿任意轨迹生成真实视图，但难以保证时间与几何一致性。
- 从重建驾驶场景中提取逐区域“退化证据”，将不同区域划分为三类标签：Preserve（保留）、Repair（修复）、Generate（生成）。
- 推理阶段，上述标签作为统一路由策略，指导三种区域分治处理：3DGS 外观保持（Preserve）、LiDAR 引导的结构修正（Repair）、视频先验驱动的内容补全（Generate）。
- 两阶段训练：第一阶段利用稀疏 LiDAR 投影建立几何控制，第二阶段学习基于稠密 3DGS 渲染的外观控制。

### 主要贡献
- 提出 PRG-Fusion 框架，以重建证据统一编排生成先验，兼顾几何一致性与视觉真实性。
- 设计区域级路由策略（Preserve/Repair/Generate），按场景局部退化情况自适应选择合成方式。
- 提出两阶段训练范式，先几何后外观，实现对 LiDAR 结构与渲染外观的分步控制。
- 在 Waymo 数据集上实验表明，PRG-Fusion 在新轨迹视频合成任务中综合性能最优，视觉质量与几何保真度更好，并在大幅轨迹偏移下保持有竞争力的视图一致性。

### 局限性
摘要未提供足够信息，例如对不同场景类型（如天气、光照变化）、计算开销、训练数据规模需求以及失败案例的具体分析均未提及。

### 阅读优先级
**中**
理由：该工作针对自动驾驶仿真中的视图合成问题，方法设计较完整且实验结果积极，涉及多模态融合（LiDAR、3DGS、视频先验）与区域路由机制，适合关注自动驾驶仿真或新视角合成的研究者阅读；但若与自身研究方向的直接关联不强，为非紧急优先文献。

</details>

<details>
<summary>Abstract</summary>

Synthesizing photorealistic driving videos along specified trajectories is essential for scalable closed-loop simulation. Reconstruction-based methods leverage neural rendering to synthesize geometrically consistent views, but often exhibit diverse artifacts and missing content when the viewpoint deviates from the training trajectory. In contrast, generative models can synthesize realistic views along arbitrary trajectories from vehicle sensor data, yet often struggle to maintain temporal and geometric consistency across frames. To combine the strengths of both, we propose PRG-Fusion, a framework for driving view synthesis that uses reconstruction evidence to orchestrate generative priors across regions. Specifically, we extract region-wise degradation evidence from reconstructed driving scenes and convert it into Preserve, Repair, and Generate (PRG) labels. At inference, these labels serve as a unified routing policy for region-aware spatiotemporal synthesis, orchestrating 3DGS appearance preservation, LiDAR-guided structural correction, and video-prior-driven content completion across Preserve, Repair, and Generate regions, respectively. We then follow a two-stage training paradigm, first establish geometric control from sparse LiDAR projections and subsequently learning appearance control from dense 3DGS renderings. Extensive experiments on Waymo demonstrate that PRG-Fusion achieves state-of-the-art overall performance in novel trajectory video synthesis, with superior visual quality and geometric fidelity while maintaining competitive view consistency under large trajectory shifts.

</details>

#### 2026-09-03 - Sparse auto-regressive modeling for scene generation from multi-view images

**Authors:** Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud
**Links:** [abs](https://arxiv.org/abs/2609.03931) - [pdf](https://arxiv.org/pdf/2609.03931)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, Gaussian Splatting, 3D Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Sparse auto-regressive modeling for scene generation from multi-view images
- 作者：Thomas Lucas, Maxime Pietrantoni, Philippe Weinzaepfel, Wonjune Cho, Bardienus Pieter Duisterhof, Vincent Leroy, Jerome Revaud
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03931

### 一句话总结
本文提出 SPAR3S，一种基于稀疏体素对齐的 3D 隐空间自回归生成模型，仅需多视图图像即可在无 3D 真值监督条件下完成条件场景补全与生成。

### 研究问题
如何从稀疏、无约束的多视图图像中生成完整 3D 场景，在无需大规模 3D 真值标注的前提下，兼顾超越可见内容的推理能力与计算可行性。

### 核心思路/方法
- 构建紧凑、稀疏的体素对齐 3D 隐空间，仅表示被占据的体素，避免高维密集表示的计算开销。
- 通过可微分的 3D Gaussian Splatting 与光度监督，直接从多视图图像学习该稀疏隐空间，无需 3D 真值。
- 将场景补全转化为在体素网格上预测缺失隐式令牌（latent tokens）及其空间位置（occupancy）的任务。
- 训练掩码自回归 Transformer，联合建模体素占据状态与隐式令牌数值，以实现高效且空间一致的未见区域生成。

### 主要贡献
- 提出一种无需 3D 真值监督的稀疏 3D 隐生成模型（SPAR3S），用于条件场景补全。
- 设计了由多视图图像经光度监督学习的稀疏体素对齐隐空间表征。
- 采用掩码自回归 Transformer 联合建模占据与隐特征，实现结构化场景生成。
- 在合成室内场景中取得优于现有工作的新视角合成质量，并在 RealEstate10k 上验证了真实世界数据的泛化性。

### 局限性
摘要未提供足够信息，未明确提及方法的具体失败案例、计算资源需求、对输入视图数量/分布的敏感性，或扩展至更大规模场景时的潜在瓶颈。

### 阅读优先级
高。理由：该工作聚焦 3D 场景补全这一核心挑战，提出无需 3D 真值监督的稀疏隐空间自回归方案，兼顾效率与生成质量，相关技术路线（Gaussian Splatting + 自回归 Transformer）具有较强创新性与应用潜力，适合场景生成与神经渲染方向研究者优先关注。

</details>

<details>
<summary>Abstract</summary>

Generating complete 3D scenes from sparse, unconstrained views is a fundamental challenge in 3D vision which requires reasoning beyond observed content while remaining computationally tractable. Existing feed-forward reconstruction methods are inherently limited to content visible in the input images, while 3D generative modeling is hindered by the high computational cost of dense volumetric representations and the scarcity of large-scale 3D supervision. We introduce SPAR3S, a sparse voxel-aligned 3D latent generative model for conditional scene completion without requiring ground-truth 3D data for supervision. Our key insight is to formulate 3D scene generation in a structured, compact, voxel-aligned 3D latent space where only occupied voxels are represented. We learn this sparse latent space directly from multi-view images using photometric supervision via differentiable 3D Gaussian Splatting. Given a partial set of observed voxels encoded from sparse input views, scene completion reduces to predicting the missing latent tokens and their spatial support within the voxel grid. To this end, we train a masked autoregressive transformer that jointly models voxel occupancy and latent token values, enabling efficient and spatially consistent generation of unseen regions. We demonstrate the effectiveness of our method on synthetic indoor scenes, achieving higher novel-view quality than prior work. We further validate its generalization on RealEstate10k, highlighting its applicability to real-world data.

</details>

#### 2026-09-03 - Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing

**Authors:** Cheng-Kang Ted Chao, Yotam Gingold
**Links:** [abs](https://arxiv.org/abs/2609.03897) - [pdf](https://arxiv.org/pdf/2609.03897)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Reparametrizing 3D Gaussian Splatting for Real-Time Palette-based Color and Luminance Editing
- 作者：Cheng-Kang Ted Chao, Yotam Gingold
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03897

### 一句话总结
本文提出一种对预训练3D高斯泼溅（3DGS）模型重新参数化球谐系数的方法，实现基于调色板的实时颜色与亮度独立编辑，并支持像素级颜色约束。

### 研究问题
如何在预训练3DGS表示上实现实时的、具备独立颜色（色调/饱和度）与亮度控制的调色板级交互式编辑，并克服先前基于图元空间（primitive-space）方法因alpha混合导致的编辑区域溢出问题。

### 核心思路/方法
- 对预训练vanilla 3DGS的球谐函数进行重新参数化，使其编码与视角相关的调色板权重，而非从零训练新表示。
- 通过基于图像空间稀疏性的损失函数，同时求解调色板权重和调色板颜色。
- 亮度编辑通过沿无彩色轴（achromatic axis）的逐像素权重偏移实现，等效于逐像素的调色板感知亮度编辑。
- 采用迭代重加权最小二乘（IRLS）与阻尼块坐标下降（damped block-coordinate descent）实现快速求解（数十毫秒）。
- 编辑结果可高效烘焙回vanilla 3DGS，保持标准查看器兼容性。

### 主要贡献
- 实现比先前基于调色板的3DGS方法更稀疏、更局部化的颜色编辑。
- 首次为3DGS提供每个调色板颜色的独立亮度控制。
- 支持视角一致的像素级颜色约束，这是先前3DGS方法不具备的能力。
- 编辑过程可实时运行，且与标准3DGS渲染管线兼容。

### 局限性
摘要称该方法较先前方法实现了更稀疏和更局部的编辑，但未提供定量比较数据、用户研究结果或对场景规模/复杂度的限制说明。亦未提及可能的伪影类型、处理失败场景或对预训练模型质量的依赖程度。摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向3DGS交互编辑这一细分应用方向，方法创新（重新参数化球谐、视角空间亮度编辑）有一定新颖性，但受众限于从事3D编辑/渲染交互的研究者；若读者关注实时3D编辑或调色板方法，则值得细读，否则非核心领域可暂缓。

</details>

<details>
<summary>Abstract</summary>

Professional color editing requires precise control over both color (hue and saturation) and lightness, ideally through separate, independent controls. We present a real-time interactive color editing framework for 3D Gaussian Splatting that supports palette-based recoloring, per-palette tone curves for color-aware luminance adjustment, and pixel-level color constraints. Rather than training a new representation from scratch, we reparameterize the spherical harmonics of a pretrained vanilla 3DGS to encode view-dependent palette weights. We simultaneously solve for weights and palette colors via a loss based on image-space sparsity. Luminance editing is realized as a per-pixel weight shift along the achromatic axis, which we show is equivalent to a per-pixel palette-aware luminance edit. This view-space formulation addresses a core limitation of prior primitive-space methods, where alpha-blending breaks per-Gaussian sparsity and causes edits to bleed into unintended regions. Our edits run in tens of milliseconds via an iteratively reweighted least squares and damped block-coordinate descent that couples tone curves and palette shifts under view-space sparsity. Our representation can be efficiently baked back into a vanilla 3DGS, preserving compatibility with standard viewers. We demonstrate sparser, more localized edits than prior palette-based 3DGS methods, while enabling independent luminance control per palette color and view-consistent pixel-level constraints, capabilities previously unavailable for 3DGS.

</details>

#### 2026-09-03 - Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations

**Authors:** Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
**Links:** [abs](https://arxiv.org/abs/2609.03657) - [pdf](https://arxiv.org/pdf/2609.03657)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, robotics, manipulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations
- 作者：Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
- 出版日期：2026-09-03T10:54:49Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03657

### 一句话总结

本文提出一种无需优化的3D形态扰动正则化方法，利用3D高斯泼溅的形态参数空间操作，提升稀疏视角下3D场景重建的质量和几何先验学习，并显著改善下游机器人操控策略的性能。

### 研究问题

NeRF和3DGS等3D场景表示在稀疏视角设置下存在严重伪影；现有的生成式3D伪影修复器依赖成对的受损/干净渲染数据，且需要针对不同视角配置进行昂贵的逐场景重建；而2D图像增强虽有即时正则化效果，但缺乏能保持跨视角空间一致性的显式3D等效方法。本文旨在回答：如何设计一种无需优化、能保持空间一致性的3D表示正则化方法，以支持3D感知训练？

### 核心思路/方法

 核心是提出3D形态扰动（3D Morphological Perturbations），将其作为无需优化的正则化器。具体地，利用显式3DGS表示，将每个高斯视为类似于2D像素的基本构建单元，并在其形态参数空间（尺度、旋转、剪枝）上施加扰动。该方法从数据集整理过程中消除了逐场景的3DGS优化循环，使模型能学习比稀疏视角基线更强的几何先验。

### 主要贡献

1. 提出一种无需优化的3D形态扰动正则化方法，显式作用于3DGS的形态参数空间，能够保持空间一致性。
2. 该方法避免了数据集构建中昂贵的逐场景3DGS重建/优化过程。
3. 在轻量视频扩散测试环境中验证，该方法相比稀疏视角基线有助于学到更强的几何先验。
4. 扩展到140亿参数的视频模型（经ControlNet），在保持视觉保真度的同时，相对最先进的图像到图像3D伪影修复器，将平均深度误差降低12.5%。
5. 在下游机器人操控策略中，在4项操纵任务中的3项上将成功率提升最多8.0%。

### 局限性

摘要未提供足够信息。具体而言，本文未明确讨论所提出方法的局限性，如对3DGS表示类型的依赖程度、扰动幅度选择的敏感性、在不同场景类型上的泛化边界，或计算开销的具体细节等。

### 阅读优先级

**高**。理由：该工作针对稀疏视角3D重建这一重要难题，提出一种简洁、无需优化的正则化方案，直接规避了昂贵的数据集构建流程；同时在大规模视频模型和下游机器人任务上展示了显著的定量改进，具有较强的方法普适性与应用价值。且论文归属神经场景表示与渲染方向，发表于2026年，新颖性较突出。

</details>

<details>
<summary>Abstract</summary>

3D scene representations like NeRF and 3D Gaussian Splatting (3DGS) suffer severe artifacts in sparse-view settings. Recent generative 3D artifact fixers attempt to address this, but rely on paired corrupted and clean renders requiring costly, per-scene reconstructions across varying view configurations. While 2D image augmentations act as instant regularizers, no explicit equivalents exist for 3D representations to preserve spatial consistency across views, an essential property for 3D-aware training. We propose 3D Morphological Perturbations as an optimization-free regularizer that preserves spatial consistency. Leveraging explicit 3DGS, we treat each Gaussian as a fundamental building block - analogous to a 2D pixel - and apply perturbations across its morphological parameter space via scale, rotation, and pruning. Our method eliminates per-scene 3DGS optimization loops from dataset curation while enabling models to learn stronger geometric priors than sparse-view baselines in diagnostic ablations conducted on a lightweight video diffusion sandbox. Scaled to a 14B-parameter video model via ControlNet, our approach maintains visual fidelity while reducing mean depth error by 12.5% over state-of-the-art image-to-image 3D artifact refiners, ultimately boosting downstream robotics policy success rates by up to 8.0% across 3 of 4 manipulation tasks.

</details>

#### 2026-09-03 - Stabilizing Camera-Controlled Novel View Synthesis at Inference Time

**Authors:** Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman
**Links:** [abs](https://arxiv.org/abs/2609.03639) - [pdf](https://arxiv.org/pdf/2609.03639)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, novel view synthesis, view synthesis

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Stabilizing Camera-Controlled Novel View Synthesis at Inference Time
- 作者：Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03639

### 一句话总结
本文提出一种无需训练、仅在推理阶段通过将相机运动分解为小自回归步长来稳定单图新视角合成的方法（CamTrol++），显著提升了大视角运动与长时程生成下的时间与几何一致性。

### 研究问题
如何在不重训练或修改扩散模型主干的情况下，提高基于预训练视频扩散模型的、无训练相机控制新视角合成在大相机运动和长生成长度下的稳定性？

### 核心思路/方法
- 核心发现：稳定性的主要来源很简单——将相机运动分解为小的自回归步骤，可限制每步几何畸变并减少误差累积。
- 通过受控相机步长研究，发现性能在小步长下保持稳定，当每步运动接近18°–20°时性能明显下降。
- 进一步评估了几何约束的空间注意力与低频外观锚定作为辅助改进，并结合高效的无配准（registration-free）变形流水线。
- 全程无需训练，也不修改扩散模型主干。

### 主要贡献
- 揭示了影响无训练相机控制新视图合成稳定性的关键因素是相机运动步长分解。
- 提出CamTrol++方法，在RealEstate10K和MegaScene数据集上提升时间与几何一致性、下游3D重建质量和生成效率，超越无训练基线。
- 方法在56帧生成及深度数据受到较大破坏时仍保持有效。

### 局限性
摘要未提供足够信息。具体而言，文中未提及方法在哪些场景下可能失效、是否有计算开销增加或潜在的内存限制，也未给出与其他可训练方法的完整对比结果。

### 阅读优先级
**高**。理由：该工作针对无训练相机控制新视图合成的稳定性问题，给出了简单有效的推理策略，不依赖额外训练，实用性较强；同时在大视角、长时程和深度退化条件下验证了效果，对相关研究方向具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Training-free, camera-controlled novel view synthesis from a single image using pre-trained video diffusion models often becomes unstable under large camera motion and long generation horizons. Existing approaches commonly combine several inference-time components, making it unclear which design choices are most important for stability. We show that the main source of stability is simple. Decomposing camera motion into small autoregressive steps limits per-step geometric distortion and reduces error accumulation. A controlled camera-step study shows that performance remains stable for small motions and degrades more strongly as the per-step motion approaches $18$-$20^\circ$. We further evaluate geometry-constrained spatial attention and low-frequency appearance anchoring as supporting refinements, together with an efficient registration-free warping pipeline. Across RealEstate10K and MegaScene, CamTrol++ improves temporal and geometric consistency, downstream 3D reconstruction quality, and generation efficiency over training-free baselines. The method remains effective for 56-frame generation and under substantial controlled depth corruption. These results show that careful control of camera motion at inference time can substantially improve the stability of camera-controlled novel view synthesis without retraining or modifying the diffusion backbone.

</details>

#### 2026-09-03 - TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization

**Authors:** Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
**Links:** [abs](https://arxiv.org/abs/2609.03613) - [pdf](https://arxiv.org/pdf/2609.03613)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TileGS: Tile-Local Depth Binning for Gaussian Splatting Rasterization
- 作者：Wei Tan, Matias Turkulainen, Lauri Ilola, Hamed Rezazadegan Tavakoli, Juho Kannala
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03613

### 一句话总结
TileGS 通过对高斯溅射栅格化过程进行瓦片内的深度局部重排，将每个长瓦片范围切分为更短的深度局部子范围并逐层前向光栅化，从而在保持与基线数值一致的前提下实现渲染加速。

### 研究问题
标准 3D Gaussian Splatting (3DGS) 栅格化需要遍历全局排序的瓦片流，导致每个瓦片对应的范围过长、几何属性传输开销大，限制了实时渲染效率。本文旨在通过瓦片内的局部重排机制减少栅格化遍历开销，同时维持输出质量。

### 核心思路/方法
- 提出 **TileGS**，对每个瓦片的高斯分布按深度进行局部重组织，将一个长范围瓦片拆分为一组更短的深度局部范围。
- 栅格化时按**前到后顺序**处理这些深度局部范围，实现更紧凑的遍历。
- 在粗排序不足以与基线合成结果对齐之处，引入**选择性修复**机制以保持合成质量。
- 设置了默认的 **No-GW（No Geometry-Write）** 变体，避免写出几何属性以降低内存压力。

### 主要贡献
- 提出一种瓦片局部深度分箱的 3DGS 栅格化重组方案，提升光栅化内核速度。
- 在 9 场景基准及桌面/笔记本 Ada GPU 上验证：RTX 4090 上实现平均 **1.44x** 栅格内核加速，端到端帧加速为 RTX 4090 上 **1.069x**、RTX 1000 Ada 上 **1.094x**（对比 gsplat）。
- 输出质量与 gsplat 匹配至数值噪声级别（|ΔPSNR|、|ΔSSIM|、|ΔLPIPS| 均 < 0.001）。
- 通过 Nsight Compute 全量分析，论证加速来源于**有效栅格遍历量减少**，而非字节量减少、合并改善、占用率提升或分歧降低；并定位几何属性为剩余内存压力主因（占光栅总流量 85.8%、超额扇区 88.6%）。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作聚焦于 3DGS 栅格化的工程优化层面，对渲染效率有明确量化提升，且通过详细 profiling 分析提供了机理性的解释；适合从事实时神经渲染、3DGS 系统优化的研究者关注。但摘要未披露方法在不同纹理/场景复杂度下的泛化性、修复策略的具体代价以及是否适用于大规模场景等细节，故优先级不设为最高。

</details>

<details>
<summary>Abstract</summary>

Real-time 3D Gaussian Splatting (3DGS) achieves high rendering quality, but standard rasterization still traverses a globally sorted tile stream that creates long per-tile ranges and heavy geometry-attribute traffic. We present TileGS, a tile-local reorganization of Gaussian splatting. TileGS turns each long tile range into a sequence of shorter depth-local ranges, rasterizes those ranges in front-to-back order, and applies selective repair where coarse ordering is insufficient to match baseline compositing. Across a 9-scene benchmark on desktop and laptop Ada GPUs, our default No-GW (No Geometry-Write) variant delivers a mean 1.44x raster-kernel speedup on RTX 4090 and mean end-to-end frame speedups of 1.069x on RTX 4090 and 1.094x on RTX 1000 Ada over gsplat--a widely used optimized open-source 3DGS implementation--while matching the gsplat output up to numerical noise (|Delta PSNR| < 0.001 dB, |Delta SSIM| < 0.001, |Delta LPIPS| < 0.001). Full-suite RTX 4090 Nsight Compute profiling reveals TileGS is faster despite lower SM throughput, lower active-warp occupancy, and higher DRAM traffic, while total SASS thread instructions fall by 1.26x. Source-attributed profiling confirms that geometry attributes dominate the remaining memory pressure (85.8% of total raster traffic and 88.6% of excess sectors). Together, these counters support the interpretation that TileGS improves raster performance by reducing effective raster traversal work, rather than by reducing byte volume, improving coalescing, increasing occupancy, or directly reducing measured warp divergence.

</details>

#### 2026-09-03 - TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates

**Authors:** Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua
**Links:** [abs](https://arxiv.org/abs/2609.03534) - [pdf](https://arxiv.org/pdf/2609.03534)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** dynamic Gaussian, scene reconstruction, Gaussian Splatting, 3D Gaussian Splatting, Gaussian primitive, novel view synthesis, view synthesis, scene representation, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TruncGradGS: Improved 3D Gaussian Splatting via Truncated Gradient Updates
- 作者：Theo Morales, Nhat-Quynh Le-Pham, Robin Atkins, Binh-Son Hua
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03534

### 一句话总结
该论文提出一种基于分段截断梯度的优化方法，以缓解3D高斯泼溅中的梯度消失问题，从而提升场景重建质量与优化稳定性。

### 研究问题
3D高斯泼溅在从视觉输入学习高斯原语时，优化过程易受梯度消失现象影响——离高斯原语较远的像素其梯度幅值过小，难以有效影响原语属性，导致场景重建次优。

### 核心思路/方法
提出使用分段截断梯度（piecewise truncated gradient）公式替代经典梯度更新，通过截断梯度机制增强远距离像素对高斯原语属性的梯度信号，从而改善训练稳定性，并提升对不同初始化方式的鲁棒性。

### 主要贡献
- 提出针对梯度消失问题的分段截断梯度方法，显著改进3D高斯泼溅的优化过程。
- 在随机初始化与COLMAP初始化下均能一致提升重建性能，且可泛化至静态与动态高斯泼溅场景。
- 指出现有动态场景基准的局限性，并引入基于合成3D场景的新动态高斯泼溅基准数据集。

### 局限性
摘要未提供足够信息来详细分析局限性，包括方法在特定场景下的潜在不足、计算开销、或与现有技术对比的失败案例均未说明。

### 阅读优先级
**高**。理由：该方法针对3D高斯泼溅中常见的梯度消失问题，提出简单且具通用性的改进方案，同时兼顾静态与动态场景，并附带新基准数据集，兼顾理论与应用价值，适合关注神经场景表示与渲染的研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting has become a de facto scene representation for novel view synthesis, yet robustly learning 3D Gaussian primitives from visual input remains challenging. Standard optimization relies on gradient-based updates, but a common issue is the gradient vanishing phenomenon: a pixel far from a Gaussian primitive often has diminishing gradient magnitudes to influence primitive attributes, resulting in suboptimal scene reconstruction. In this paper, we propose a method to address gradient vanishing with a piecewise truncated gradient formulation that improves the optimization stability and robustness to initializations. We show that our method consistently improves 3D Gaussian Splatting with random and COLMAP initializations while being generalizable across static and dynamic Gaussian Splatting. As a by-product, we also examine the limitations of current benchmarks for dynamic scenes, and introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes. We demonstrate the effectiveness of our method in both static and dynamic settings for the public benchmarks and our proposed dataset.

</details>

#### 2026-09-03 - P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing

**Authors:** Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi, Alireza Moazeni, Ke Li
**Links:** [abs](https://arxiv.org/abs/2609.03349) - [pdf](https://arxiv.org/pdf/2609.03349)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** multi-view reconstruction, NeRF, neural rendering, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：P-CORE: Self-Supervised Surface Consistency for Point-Based Neural Editing
- 作者：Yanshu Zhang, Shichong Peng, Mehran Aghabozorgi, Alireza Moazeni, Ke Li
- 出版日期：2026-09-03T04:12:39Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03349

### 一句话总结
本文提出一种自监督方法P-CORE，通过保证点云变形前后表面预测的一致性，提升基于点的神经表示在大变形自由编辑下的鲁棒性，减少空洞与不连续伪影。

### 研究问题
基于点的神经表示在无固定连接的情况下能自由编辑形状，但大变形时容易产生表面空洞与不连续。如何在不依赖变形后真实多视图图像的前提下，提升点表示方法对大形变的适应能力。

### 核心思路/方法
- 核心思想：生成随机变形，并约束“变形后点云预测的表面”等于“原始点云预测表面施加相同变形”的结果，从而在自监督信号下维持表面一致性。
- 实现载体：采用基于注意力的点表示（attention-based point representations），区别于基于splatting的点表示——前者使用点间的学习插值核，而后者在每个点周围使用固定高斯核。
- 该学习插值核能够适应大变形，而无需增删点。

### 主要贡献
- 提出新颖的自监督表面一致性约束，使点基神经表示无需变形真实图像即可适应大变形。
- 将方法集成到注意力式点表示中，利用可学习插值核替代高斯核，提升变形鲁棒性。
- 在合成编辑基准（Neural Editor、Objaverse）上，零样本编辑性能优于现有基于点的方法，显著减少伪影。
- 在DTU和Mip-NeRF 360数据集上的定性实验表明其在真实场景中的有效性。

### 局限性
摘要未提供足够信息（未提及计算开销、极端变形情况、失败案例、对训练数据规模的要求或与其他非点基表示方法的比较）。

### 阅读优先级
**中**
理由：该方法针对点基神经编辑在大变形下的鲁棒性问题，提出新颖的自监督一致性约束，具有明确技术动机和较好实验验证，适用于从事神经渲染与形状编辑方向的研究者。但摘要中缺乏方法细节与定量对比的完整描述，且未披露运行效率等信息，非核心方向读者可不优先精读。

</details>

<details>
<summary>Abstract</summary>

Advances in neural rendering have enabled high-fidelity multi-view reconstruction of 3D scenes. However, free-form non-rigid shape editing remains a significant challenge. Point-based neural representations are highly desirable for multi-view reconstruction because they lack fixed connectivity, which does not constrain the learned surface topology to that of the initialization. Yet this same property causes point-based representations to struggle with holes and surface discontinuities under large deformations. To address this, we propose a novel self-supervised method to enable point-based representations to adapt to large deformations without requiring ground truth multi-view images of deformed geometry. The key idea is to generate random deformations and to ensure consistency in the predicted surface before and after deformation. In particular, the surface prediction from the deformed point cloud should be the same as the deformation applied to the surface prediction from the original point cloud. We incorporate our approach into attention-based point representations, which differ from splatting-based point representations in their use of a learned interpolation kernel between points as opposed to a Gaussian kernel around each point. This learned interpolation kernel can learn to adapt to large deformations, without requiring addition or removal of points. We show that our framework significantly enhances its robustness to large deformations. Experiments on synthetic geometry editing benchmarks (Neural Editor, Objaverse) demonstrate that our approach outperforms existing point-based methods in zero-shot editing and significantly reduces artifacts. Furthermore, qualitative results on the DTU and Mip-NeRF 360 datasets demonstrate our method's effectiveness on real-world scenes.

</details>

#### 2026-09-03 - PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations

**Authors:** Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
**Links:** [abs](https://arxiv.org/abs/2609.03341) - [pdf](https://arxiv.org/pdf/2609.03341)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, view synthesis, rendering, splatting, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations
- 作者：Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03341

### 一句话总结
PointGT 提出了一种基于点的3D表示方法，使得对象几何形状与外观纹理能够同时进行编辑，并保持高渲染质量。

### 研究问题
如何在基于点的神经表示中，实现几何形变与高分辨率纹理编辑的兼容与同步操作，克服现有体积表示（如3D高斯溅射）难以同时支持几何与纹理编辑的局限。

### 核心思路/方法
PointGT 将适合几何形变的点基表示与一种学习得到的 UV 映射技术相结合：点基表示支撑几何变形，而UV映射支持高分辨率纹理编辑，从而实现两者的统一编辑框架。

### 主要贡献
- 提出 PointGT，一种支持同时编辑几何与外观的点基3D表示方法。
- 方法兼顾几何形变能力与高分辨率纹理编辑能力，据摘要所述，其精细编辑在渲染质量上表现良好。

### 局限性
摘要未提供足够信息（如对复杂场景的可扩展性、编辑操作的限制或计算开销等均未提及）。

### 阅读优先级
**中**。理由：该工作面向3D表示的可编辑性这一活跃方向，思路具有一定创新性，但摘要未提供定量实验对比或性能数据，实际效果与局限性需要进一步阅读正文判断。

</details>

<details>
<summary>Abstract</summary>

We present PointGT, a point-based 3D representation that enables simultaneous editing of object geometry and appearance. Existing reconstruction and view synthesis techniques produce volumetric 3D representations that are high-quality and photorealistic, but are difficult to edit. In particular, recent efforts to enable texture editing for 3D Gaussian Splatting representations are not compatible with geometry edits and deformations. Our method combines a point-based representation that is well-suited for geometry deformations with a learned UV mapping technique that enables high-resolution texture editing. We show that PointGT enables fine-grained editing of both geometry and texture in point-based neural representations with high rendering quality.

</details>

#### 2026-09-03 - Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training

**Authors:** Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang
**Links:** [abs](https://arxiv.org/abs/2609.03334) - [pdf](https://arxiv.org/pdf/2609.03334)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Laplacian Frequency Hierarchies for Efficient 3D Gaussian Splatting Training
- 作者：Yixiong Yang, Sisheng Zhang, Qingsong Yan, Shaohuai Shi, Qiang Wang
- 出版日期：2026-09-03
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.03334

### 一句话总结
本文提出一种基于拉普拉斯图像分解与由粗到细频率分阶段训练的3D高斯泼溅（3DGS）训练方案，通过归档低频高斯场、仅优化高频残差来减少训练中的活跃高斯数量，从而加速训练并保持重建质量。

### 研究问题
3DGS训练中的关键瓶颈是高斯原语（Gaussian primitives）的持续增长，导致优化成本上升和收敛变慢，尤其在高分辨率场景下更为严重。本文旨在通过减少训练过程中的活跃高斯数量来降低优化开销、加速训练。

### 核心思路/方法
本文提出“Laplacian Frequency Hierarchies”方案，结合拉普拉斯图像分解与由粗到细、按频率分阶段的训练过程。具体为：
1. 先拟合较低频率结构；
2. 将对应的低频高斯场归档（archive）；
3. 后续高斯场仅针对高频残差进行优化，无需承担全部原语负担；
4. 在推理阶段通过图像域内的拉普拉斯风格重建，将各渲染分量合成最终图像。

该方案为插件式（plug-and-play）设计，与现有3DGS加速方法正交，可结合Taming-3DGS、FastGS等强基座使用。

### 主要贡献
- 提出一种简单高效的3DGS训练方案，减少训练中活跃高斯数量，降低优化开销并加速训练。
- 设计插件式、与既有3DGS加速方法正交的方案，可与Taming-3DGS和FastGS直接结合。
- 实验显示在1K设置下分别获得1.73x和1.21x的平均加速，在4K设置下分别获得1.74x和1.33x的平均加速；在更具挑战性场景和高分辨率下收益更明显，同时保持有竞争力的重建质量。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对3DGS训练效率瓶颈提出了新颖且即插即用的训练方案，可直接与多个主流加速方法结合并获得显著加速（最高1.74x），且在高分辨率下优势更明显，对神经场景表示与渲染方向具有实际应用价值。摘要中已明确给出定量加速效果，适合该领域研究者快速了解最新加速思路。

（注：论文出版日期标注为2026年，摘要中未提供额外说明，请读者自行核实该日期合理性。）

</details>

<details>
<summary>Abstract</summary>

A key bottleneck in 3D Gaussian Splatting training is the continual growth of Gaussian primitives, which increases optimization cost and slows convergence, especially at high resolutions. We propose Laplacian Frequency Hierarchies, a simple yet efficient 3DGS scheme that combines Laplacian image decomposition with coarse-to-fine, frequency-staged training. After fitting lower-frequency structure, we archive the corresponding Gaussian field so that subsequent fields can optimize higher-frequency residuals without carrying the full primitive burden, and we compose the rendered components in the image domain via a Laplacian-style reconstruction at inference time. This design reduces the number of active Gaussians during training, thereby lowering optimization overhead and accelerating training. The proposed scheme is plug-and-play and orthogonal to prior 3DGS accelerations: it can be directly combined with strong backbones such as Taming-3DGS and FastGS to improve training speed with competitive reconstruction quality. It achieves average speedups of 1.73x and 1.21x at 1K setting, and 1.74x and 1.33x at 4K setting on Taming-3DGS and FastGS, with larger gains on more challenging scenes and increasingly pronounced benefits at higher resolutions.

</details>

#### 2026-09-02 - RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation

**Authors:** Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
**Links:** [abs](https://arxiv.org/abs/2609.02847) - [pdf](https://arxiv.org/pdf/2609.02847)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** feed-forward reconstruction, novel view synthesis, view synthesis, scene representation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation
- 作者：Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
- 出版日期：2026-09-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02847

### 一句话总结
RoGe提出一种端到端统一框架，将前馈隐式场景重建与视频扩散生成模型联合训练，通过射线查询注入几何条件，实现稀疏视角下的新视角合成。

### 研究问题
如何在稀疏输入视图下进行新视角合成，同时兼顾已观测区域的几何准确性（重建）与未观测区域的生成先验（生成），并克服现有混合方法中二者通过显式/有损中间表示桥接而导致的误差传播问题。

### 核心思路/方法
RoGe移除了重建与生成之间的显式3D中间桥梁，具体流程为：
1. 从稀疏输入视图出发，利用前馈重建模型构建隐式场景表示。
2. 用目标相机射线查询该隐式表示，获得逐视角的几何特征。
3. 将这些几何特征直接注入视频扩散模型作为条件，不经过图像渲染或显式3D表示。
4. 重建模型与生成模型端到端联合训练，使生成目标能反向塑造几何条件。

### 主要贡献
- 提出端到端的统一重建与生成框架RoGe，消除了重建与生成之间的显式桥接。
- 利用射线查询得到的隐式几何特征作为扩散模型条件，替代原始重建token或渲染图像。
- 联合训练使生成目标直接作用于几何条件，提升条件质量。
- 在DL3DV数据集上，图像级指标与视频级时序一致性上均优于重建式、生成式及混合式基线。
- 消融实验表明：射线查询的隐式特征优于原始重建token与渲染RGB；联合训练带来额外收益。

### 局限性
摘要未提供足够信息，未说明方法在DL3DV之外的泛化能力、计算开销、对极端稀疏视角或大轨迹的鲁棒性等问题。

### 阅读优先级
**高**

理由：该工作针对新视角合成中重建与生成结合的痛点提出端到端统一方案，方法设计新颖（移除显式3D桥梁、用射线查询注入条件），并在多类基线上取得一致性优势，对神经场景表示与生成模型结合方向具有较强参考价值。但具体实验结果细节（如数值指标、模型复杂度）需进一步查阅全文。

</details>

<details>
<summary>Abstract</summary>

Novel view synthesis from sparse inputs requires both geometric grounding from the observed views and generative priors of unobserved regions, motivating recent hybrid methods that combine reconstruction and generation. However, existing methods bridge the two with rendered images or explicit 3D representations such as point maps or 3D Gaussians. Generation is thus conditioned on a lossy and imperfect projection of the scene, inheriting its errors, and reconstruction receives no signal from generation to correct them. We present RoGe, an end-to-end unified reconstruction and generation framework that removes this explicit bridge. It targets roaming within a scene anchored by sparse views: given a few posed images and a camera trajectory, it synthesizes a temporally coherent video along that trajectory. From the sparse input views, RoGe builds an implicit scene representation with a feed-forward reconstruction model, and queries it with target camera rays to obtain per-view geometric features. These features are injected into a video diffusion model as conditioning, without any 3D intermediate. Both modules are trained jointly, so the generation objective directly shapes its own geometric conditioning. We conduct experiments on DL3DV, where RoGe outperforms reconstruction-based, generation-based, and hybrid baselines on image-level metrics and video-level temporal consistency. Ablations confirm that ray-queried implicit features outperform both raw reconstruction tokens and rendered RGB as conditioning, and that joint training brings further gains.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

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

#### 2026-09-08 - Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering

**Authors:** Jiahui Zhang, Bonian Han, Gongbo Liang, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2609.09069) - [pdf](https://arxiv.org/pdf/2609.09069)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Rethinking Learned Occupancy in Autonomous Active Mapping with Observation-Gated Filtering
- 作者：Jiahui Zhang, Bonian Han, Gongbo Liang, Yu Zhang
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09069

### 一句话总结
本文通过受控闭环基准实验揭示占用预测精度与主动建图覆盖性能之间不存在单调关系，并提出一种观测门控滤波器以在线修正规划器使用的占用几何。

### 研究问题
在自主三维主动建图中，学习式占用补全同时充当两个规划角色——打分期望表面增益与约束无碰撞运动，导致不准确的预测可能同时扭曲观测决策与可通行性判断。核心研究问题为：占用补全精度与闭环覆盖绩效之间是否存在一致的促进关系，以及如何在不重新训练或使用真值的情况下改进该耦合接口。

### 核心思路/方法
- 构建受控闭环基准，固定主动建图系统，仅改变规划器面对的占用条件：仅观测（observation-only）、学习式（learned）、Oracle校正（oracle-corrected）、真值（ground-truth）。
- 对比不同条件下的闭环覆盖率与收敛速度。
- 基于诊断结果设计观测门控滤波器：在欠观测区域保留补全预测；仅当预测区域经历多次视锥暴露却缺乏附近RGB-D支持时，抑制该预测。

### 主要贡献
1. 揭示占用精度提升并不单调改进闭环覆盖：与学习式基线相比，使用真值占用平均提前12.7步达到70%最终覆盖率，但最终覆盖率仅提升0.031。
2. 提出不依赖重训练或真值的观测门控滤波方法，显著改善针对性失败启动场景。
3. 结果表明自主任务应在通信间隔期间对规划器面向的几何进行在线修订。

### 局限性
- 摘要提及当前研究假设基准RGB-D观测和足够精确的位姿估计，行星感知条件与累积定位漂移的影响尚未评估。
- 观测门控滤波器在多种场景下的平均性能提升幅度、失败类型覆盖范围等具体数值摘要未提供足够信息。
- 与其它占用学习方法或滤波策略的横向对比摘要未提供足够信息。
- 受控基准之外的泛化性（真实平台部署等）摘要未提供足够信息。

### 阅读优先级
**中**。理由：该文关注主动建图中占用预测与规划耦合的诊断性发现，并对现有学习占用方法提出一个务实的轻量修正策略。对从事机器人主动感知、占用建图或规划交互的研究者有启发性，但方法针对性较窄且实验以受控基准为主，普适性尚未验证；若您专注于闭环自主感知系统设计，建议优先阅读。

</details>

<details>
<summary>Abstract</summary>

Autonomous 3D active mapping requires a space robot to choose where to sense while building the geometry needed for navigation. Learned occupancy completion extends spatial context beyond the current field of view, but one predicted map often serves two planning roles: it scores expected surface gain and constrains collision-free motion. Unsupported occupancy can therefore distort both where the robot looks and where it believes it can travel. We study this coupled interface in a controlled closed-loop benchmark by holding the active-mapping system fixed and varying only its planner-facing occupancy across observation-only, learned, oracle-corrected, and ground-truth conditions. Improving occupancy accuracy does not monotonically improve closed-loop coverage: across 25 starts, planning with ground-truth occupancy reaches 70% of the learned baseline's final coverage 12.7 steps earlier on average, while increasing final coverage by only 0.031. Guided by this diagnosis, we introduce an observation-gated filter that retains completion in insufficiently observed regions and suppresses predictions only after repeated frustum exposure without nearby RGB-D support. The filter improves both targeted failure-prone starts without retraining or ground truth. These results motivate online revision of planner-facing geometry during autonomous intervals between communication windows. The current study assumes benchmark RGB-D observations and sufficiently accurate pose estimates; planetary sensing conditions and accumulated localization drift remain to be evaluated.

</details>

#### 2026-09-08 - Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild

**Authors:** Fei Teng, Sheng Wu, Mengfei Duan, Guoqiang Zhao, Junhui Ma, Kai Luo, Siyu Li, Hao Shi, Zhiyong Li, Kailun Yang
**Links:** [abs](https://arxiv.org/abs/2609.09012) - [pdf](https://arxiv.org/pdf/2609.09012)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild
- 作者：Fei Teng, Sheng Wu, Mengfei Duan, Guoqiang Zhao, Junhui Ma, Kai Luo, Siyu Li, Hao Shi, Zhiyong Li, Kailun Yang
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.09012

### 一句话总结
本文提出Spheriverse数据集与SphereOcc框架，通过球面-笛卡尔空间建模与语义证据检索，提升球面观测下的3D场景理解（语义占用、语义建图、3D检测）性能。

### 研究问题
球面观测图像与笛卡尔坐标物理世界之间存在跨空间表示差异，导致几何对应和语义证据聚合困难，影响3D场景理解精度。

### 核心思路/方法
- 构建Spheriverse数据集：含64,400对时间对齐的球面图像-LiDAR数据，组织为644个序列，覆盖多样场景、光照和天气，带细粒度语义类别。
- 建立基准：针对语义占用预测、语义建图、3D物体检测三个任务，评估30余种方法。
- 提出SphereOcc占用框架：
  - 笛卡尔-球面表示重塑（CSRR）：将球面距离-方位角几何融入笛卡尔体素特征，通过区域调制实现。
  - 球面证据重查询（SER）：以体素内容及距离-高度-方位角几何为条件，自适应地从源球面图像特征中检索相关语义证据。

### 主要贡献
- 提出大规模球面图像-LiDAR数据集Spheriverse（644个序列、64,400对），覆盖多样野外场景。
- 建立三个任务（语义占用、语义建图、3D检测）的基准，统一评估30+方法（总量/分场景对比）。
- 提出SphereOcc框架，结合球面几何建模与语义证据检索，在语义占用任务上达到13.91% mIoU和24.65% GeoIoU，分别超过TPVFormer与SurroundOcc各1.70和2.10个百分点。
- 在所有五个场景中均排名第一，并在不同空间划分及减小的视场下保持优势。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：论文同时提供新的大规模数据集与新方法，覆盖多个3D感知任务，实验结果在多个指标上明显优于现有方法，且发布于该领域主流方向（Embodied/Robotics/AR），对球面-笛卡尔跨空间建模和3D语义感知研究者有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Spherical observations provide global visual context for 3D scene understanding. However, visual information is encoded in an angular domain, whereas the physical world is represented in Cartesian coordinates. This cross-space representation gap complicates geometric correspondence and semantic evidence aggregation. To delve into this challenge, we introduce Spheriverse, comprising $64,400$ temporally aligned spherical image-LiDAR pairs organized into 644 sequences. The dataset spans diverse scenes, illumination, and weather conditions, with fine-grained semantic classes. We further establish benchmarks for semantic occupancy prediction, semantic mapping, and 3D object detection, evaluating 30+ methods through overall and scene-wise comparisons. For dense prediction, we propose SphereOcc, an occupancy framework that couples spherical geometry modeling with semantic evidence retrieval. Cartesian-Spherical Representation Remodeling (CSRR) incorporates spherical range-azimuth geometry into Cartesian voxel features through region-wise modulation. Spherical Evidence Re-querying (SER) then conditions queries on voxel content and range-height-azimuth geometry to adaptively retrieve relevant semantic evidence from source spherical image features. SphereOcc achieves 13.91% mIoU and 24.65% GeoIoU, outperforming the respective best-performing methods, TPVFormer and SurroundOcc, by 1.70 and 2.10 percentage points. It also ranks first in both metrics across all five scenes, with consistent advantages across the evaluated spatial partitions and reduced fields of view. The established benchmark and source code will be available at https://feit-feiteng.github.io/Spheriverse.

</details>

#### 2026-09-08 - RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation

**Authors:** Jingxuan Zhu, Jingyi Li, LiangLiang Chen, Zhiyuan Jing, Jidong Zhang, Hongming Li
**Links:** [abs](https://arxiv.org/abs/2609.08339) - [pdf](https://arxiv.org/pdf/2609.08339)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation
- 作者：Jingxuan Zhu, Jingyi Li, LiangLiang Chen, Zhiyuan Jing, Jidong Zhang, Hongming Li
- 出版日期：2026-09-08
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.08339

### 一句话总结
RoboCousin 是一个可扩展的仿真数据生成平台，可将用户提供的物体观测自动转化为可复用资产、场景和专家轨迹，用以高效合成大规模双臂操纵训练数据。

### 研究问题
如何降低仿真中新增物体或环境所需的构造成本，从而规模化生成高质量的双臂操纵训练数据？

### 核心思路/方法
- 基于 RoboTwin 2.0 构建，将物体图像自动转换为仿真就绪资产（含视觉与碰撞几何、语义与物理元数据、自动生成的抓取接触候选）。
- 构建“数字表亲”（digital cousins）：在保持任务相关功能与空间关系不变的前提下，对物体、背景、布局和语言指令进行多样化变体生成。
- 同一资产系统支持桌面级与房间级场景构建，并带有碰撞感知的基座控制，支持超出固定工作空间的任务交互。
- 释放 RoboCousin-OBD 数据集（3000+ 标注物体、50 个背景环境），并生成超过 100 万条跨 50 个任务的专家轨迹。

### 主要贡献
- 提出 RoboCousin 平台，将观测数据到可执行仿真任务的全流程自动化。
- 构建大规模公开数据集 RoboCousin-OBD，含物体标注与背景环境。
- 生成超过 100 万条双臂操纵专家轨迹。
- 实验表明：自动生成交互标注与人工标注相当；生成资产有效支持 sim-to-real；桌面级变体可提升在单一重建场景之外的任务迁移能力。

### 局限性
摘要未提供足够信息（例如：未提及方法在哪些任务或场景下失效、计算成本、对特定物体类别或复杂环境的覆盖限制、仿真与真实之间的剩余差距等）。

### 阅读优先级
**高**
理由：该工作涉及双臂操纵、仿真数据生成与 sim-to-real 迁移，属于机器人学习中的热点方向；平台化思路具有较强实用潜力，且公开了大规模数据集与专家轨迹，便于后续复现与扩展；摘要提供的实验证据较为具体且积极。若你的研究关注仿真到真实的泛化或双臂操纵策略训练，该论文值得精读。

</details>

<details>
<summary>Abstract</summary>

Bimanual manipulation policies require large and diverse training datasets, yet collecting demonstrations on physical robots is expensive and difficult to scale. Simulation can generate data efficiently, but existing pipelines typically operate within closed asset libraries and predefined scenes: adding a newly observed object or environment still requires substantial effort to reconstruct geometry, specify physical and semantic properties, annotate interactions, and integrate the result into executable tasks. We present RoboCousin, an extensible simulation-based data-generation platform that turns user-provided observations into reusable assets, scenes, and expert trajectories for bimanual manipulation. Built on RoboTwin~2.0, RoboCousin converts object images into simulation-ready assets with visual and collision geometry, semantic and physical metadata, and automatically generated grasp-contact candidates. It further constructs digital cousins that vary compatible objects, backgrounds, layouts, and language instructions while preserving task-relevant affordances and spatial relations. The same asset system supports tabletop and room-level scene construction, with collision-aware base control for interaction beyond a fixed workspace. We release RoboCousin-OBD, containing more than 3,000 annotated object instances and 50 background environments, and use RoboCousin to generate over one million expert trajectories across 50 tasks. Simulation and real-robot experiments show that the automatically generated interaction annotations are comparable to curated annotations, generated assets provide effective sim-to-real supervision, and tabletop cousins can improve transfer beyond training on a single reconstructed scene. RoboCousin therefore provides a practical path for expanding both the scale and coverage of synthetic bimanual manipulation data.

</details>

#### 2026-09-07 - Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction

**Authors:** Ruoqu Chen, Feixiang Ruan, Liu Cao, Zihao Wang, Botian Xu, Shiqin Tong, Jiajun Liu, Mingzhi Pei, Chenyu Zhang, Wanli Xing, Kaifeng Zhang, Mengdi Xu
**Links:** [abs](https://arxiv.org/abs/2609.07747) - [pdf](https://arxiv.org/pdf/2609.07747)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Dex-X: Learning Visual-Tactile Dexterous Manipulation From Human Videos with Simulated Interaction
- 作者：Ruoqu Chen, Feixiang Ruan, Liu Cao, Zihao Wang, Botian Xu, Shiqin Tong, Jiajun Liu, Mingzhi Pei, Chenyu Zhang, Wanli Xing, Kaifeng Zhang, Mengdi Xu
- 出版日期：2026-09-07T16:47:39Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07747

### 一句话总结
Dex-X 提出利用仿真作为“触觉补全引擎”，从人类单目视频中重建手物交互过程，生成触觉监督，从而训练可在真实机器人上零样本部署的视觉-触觉灵巧操作策略。

### 研究问题
人类视频缺乏触觉信息，那么能否在没有机器人端数据采集的情况下，仅从人类视频演示中学习可部署的视觉-触觉灵巧操作策略？

### 核心思路/方法
- 核心洞察：仿真可作为触觉补全引擎，为人类视频中缺失的物理触觉信息提供监督。
- 流程：从单目人类演示视频中，在仿真中重建手-物交互，利用仿真中物理接地接触动力学产生触觉监督信号。
- 利用恢复出的触觉信息，训练视觉-触觉操作策略，并蒸馏为可使用点云观测和触觉传感的可部署策略。
- 验证方式：在灵巧手-手臂平台上进行零样本 sim-to-real 迁移，覆盖抓取和接触丰富的工具使用任务。

### 主要贡献
- 提出 DEX-X 框架，首次实现从人类视频（无机器人数据采集）经仿真学习可部署的视觉-触觉灵巧操作策略。
- 仿真中重建交互并产生触觉监督，弥补人类视频缺失的物理接触信息。
- 策略蒸馏为基于点云和触觉感知的部署形式，支持零样本真实世界迁移。
- 实验显示：六类任务上教师策略平均成功率为 65.9%；蒸馏后的视觉-触觉策略在真实立方体抓取上成功率 93%，具有挑战性的桌面清洁任务上为 53%；物体抓取任务中观察到对未见物体几何的零样本泛化。

### 局限性
摘要未提供足够信息。摘要仅报告了跨任务的成功率，未提供失败模式分析、对视频质量或多样性的敏感性、仿真域偏移的具体影响、以及真实环境中其他任务的具体表现细节。

### 阅读优先级
**高**
理由：该工作聚焦于从人类视频学习灵巧操作这一重要且活跃的方向，提出以仿真补全触觉的新颖范式，模型可在真实机器人上零样本部署并显示泛化能力，对机器人学习与具身智能研究人员有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Human videos are an abundant source of dexterous manipulation behaviors, but they lack tactile information that is crucial for contact-rich interaction. This raises a fundamental question: can robots learn deployable visual-tactile dexterous manipulation policies from human video demonstrations without robot-side data collection? We present DEX-X, a framework for learning visual-tactile dexterous manipulation from human videos through simulation. Our key insight is that simulation can serve as a tactile completion engine. Given monocular human demonstrations, DEX-X reconstructs hand-object interactions in simulation, where physically grounded contact dynamics provide tactile supervision unavailable in the original videos. Leveraging this recovered tactile information, we train visual-tactile dexterous manipulation policies and distill them into deployable policies operating on point-cloud observations and tactile sensing. We demonstrate zero-shot sim-to-real transfer on a dexterous hand-arm platform across diverse grasping and contact-rich tool-use tasks. The teacher policy achieves 65.9% average success across six task categories in simulation, while the distilled visual-tactile policy achieves 93% success on real-world cube picking and 53% on the challenging table-cleaning task. Zero-shot generalization to unseen object geometries is also observed on object-picking tasks. Our results suggest that simulated interaction is a key bridge between human videos and deployable dexterous manipulation policies, providing the missing physical supervision needed for scalable robot skill learning from Internet-scale human video data.

</details>

#### 2026-09-07 - Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection

**Authors:** Pu Luo, Cong Xu, Yumei Li, Kexin Zhang, Licheng Jiao, Wenping Ma, Lingling Li
**Links:** [abs](https://arxiv.org/abs/2609.07608) - [pdf](https://arxiv.org/pdf/2609.07608)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** localization, digital twin, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Solution for UCF UrbanTwin V2X-Real Track: Sim-to-Real Urban LiDAR 3D Object Detection
- 作者：Pu Luo, Cong Xu, Yumei Li, Kexin Zhang, Licheng Jiao, Wenping Ma, Lingling Li
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07608

### 一句话总结
本文提出一种多源协同训练与类别感知融合框架，通过整合多类仿真数据源并采用专家分支与融合路径，在UrbanTwin V2X-Real隐藏测试集上实现Sim2Real路侧LiDAR 3D检测的较好性能（综合得分0.7421）。

### 研究问题
如何弥合路侧LiDAR三维目标检测中仿真到现实的差距，该差距涉及场景几何、采样密度、回波模式与行人尺度等多重耦合不一致问题。

### 核心思路/方法
- 构建统一训练池：将数字孪生扫描、扩散重绘扫描、密度稳定扫描和行人形态对齐样本纳入同一个训练池，各数据源发挥互补作用。
- 多源协同训练：在统一的DSVT检测框架下，为不同数据源分别设置源专属专家分支，各分支针对同一检测目标进行优化，同时保留各自角色。
- 类别感知融合推理：采用预定义的类别感知融合路径——几何稳定与标定感知分支用于车辆，采样互补分支用于卡车，形态一致证据用于行人。
- 无标签点云中心混合：在推理阶段进一步通过无标签的点云中心混合操作细化几何定位。

### 主要贡献
- 提出多源协同训练与类别感知融合的统一框架，以稳定、可解释的方式组织多类仿真数据源协同工作。
- 在UrbanTwin V2X-Real隐藏测试集上取得综合得分0.7421，3D mAP@0.5为0.4518，真实感得分为0.8871。
- 实验结果表明，数据源之间的稳定、可解释协作优于模型输出的无约束聚合。

### 局限性
摘要未提供足够信息——包括对失败案例的分析、各模块的消融实验细节、不同数据源的具体贡献量化、方法的计算开销与推理效率等，摘要均未涉及。

### 阅读优先级
**中**。理由：该工作面向路侧LiDAR的Sim2Real特定赛道任务，方法框架完整且在公开隐藏测试集上给出了量化结果，对从事仿真到现实迁移、路侧感知或多源融合检测的研究者有一定参考价值。但摘要中未给出足够的组件级消融与泛化分析，通用方法论贡献的显著性较难评估，适合对该赛道或相关方向有具体需求的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Bridging the simulation-to-reality gap in roadside LiDAR requires addressing several coupled discrepancies, including scene geometry, sampling density, return patterns, and pedestrian scale. This report presents a multi-source collaborative training and class-aware fusion framework for Sim2Real 3D detection. The method organizes digital-twin scans, diffusion-redrawn scans, density-stabilized scans, and pedestrian morphology-aligned samples into a unified training pool with complementary roles. Within a common DSVT detection formulation, source-specialized expert branches preserve those roles while optimizing for the same detection objective. At inference, a predefined class-aware fusion pathway integrates geometry-stable and calibration-aware branches for vehicles, sampling-complementary branches for trucks, and morphology-consistent evidence for pedestrians. A label-free point-cloud center blend then refines geometric localization. On the UrbanTwin V2X-Real hidden test set, the unified system achieves a combined score of 0.7421, with 3D mAP@0.5 of 0.4518 and a realism score of 0.8871. The results indicate that a stable, interpretable collaboration among data sources is more valuable than unconstrained aggregation of model outputs.

</details>

#### 2026-09-07 - CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements

**Authors:** Hongxiang Zhao, Mutian Xu, Zeyu Jin, Yiming Hao, Shuguang Cui, Xiaoguang Han
**Links:** [abs](https://arxiv.org/abs/2609.07498) - [pdf](https://arxiv.org/pdf/2609.07498)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements
- 作者：Hongxiang Zhao, Mutian Xu, Zeyu Jin, Yiming Hao, Shuguang Cui, Xiaoguang Han
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07498

### 一句话总结
本文提出一个大规模手到夹爪演示数据集 CosmoH2G 及一套两阶段基线方法，旨在将从人手演示中学习到的复杂空间操作动作迁移到机器人夹爪上。

### 研究问题
如何将人手操作演示有效迁移到机器人夹爪，尤其是在涉及旋转、翻转等复杂空间运动的操作场景中。现有方法多局限于简单平面任务，难以处理复杂空间轨迹。

### 核心思路/方法
- 采用隐式、数据驱动的思路，以细粒度手部姿态运动为引导。
- 构建可扩展的数据采集流程，通过手持夹爪进行动作模仿，按运动复杂度协议收集配对手-夹爪演示数据。
- 提出两阶段框架：第一阶段预测稀疏的夹爪关键帧（初始和终止状态），以简化映射目标；第二阶段在关键帧条件下生成完整连续动作序列。
- 为缓解累积漂移，夹爪方向通过模型学习，而平移部分基于抓取启发式和运动学一致性进行后优化。

### 主要贡献
- 提出了大规模配对数据集，包含 6,189 个片段，覆盖 1,254 个不同物体，空间复杂度显著高于现有基准。
- 设计了可扩展的数据采集流程和协议，以优先保证运动复杂度。
- 提出两阶段生成框架并结合平移后优化策略，在仿真和真实机器人实验中优于传统基线方法。

### 局限性
摘要未提供足够信息。摘要仅提及实验在仿真和真实机器人上进行并优于基线，但未详述失败案例、泛化边界、对遮挡或物体类别变化的适用性等局限。

### 阅读优先级
**中**。理由：该工作在数据规模和空间运动复杂度上提供新资源，对机器人操作学习领域有一定参考价值；但方法细节与对比均在摘要中概括性描述，缺少具体量化结果，若需评估方法有效性需进一步阅读全文。若兴趣集中于手-夹爪迁移或操作数据集建设，可优先深入阅读。

</details>

<details>
<summary>Abstract</summary>

Transferring human hand demonstrations to robotic grippers has recently emerged as a cost-effective solution for robot learning. However, existing methods are largely confined to simple, planar tasks and fail to handle complex spatial movements (e.g., intricate trajectories involving rotations or flips) that are essential for robot manipulation. Motivated by this gap, we adopt an implicit, data-driven approach guided by fine-grained hand-pose motions. To this end, we introduce a scalable acquisition pipeline to collect hand-gripper paired demonstrations, governed by a rigorous protocol that prioritizes motion complexity and leverages a handheld gripper for seamless action mimicry. This yields a large-scale paired dataset comprising 6,189 episodes across 1,254 unique objects, exhibiting significantly higher spatial complexity than existing benchmarks. However, learning such complex mappings remains challenging. We observe that naive end-to-end generation of full gripper pose sequences is insufficient, as minor trajectory deviations compound rapidly under intricate dynamics. To address this, we propose a two-stage framework: Stage I predicts sparse gripper keyframes (initial and terminal) to simplify the mapping objective, while Stage II generates the full continuous action sequence conditioned on these keyframes. Furthermore, to mitigate cumulative drift, we keep the gripper's orientation being learned while post-optimizing its translation based on the grasping heuristic and kinematic consistency. In both simulation and real-robot experiments, our framework enables stable and precise hand-to-gripper transfer of complex spatial manipulations, significantly outperforming traditional baselines. Project page: https://cosmoh2g.github.io.

</details>

#### 2026-09-07 - PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout

**Authors:** Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv
**Links:** [abs](https://arxiv.org/abs/2609.07328) - [pdf](https://arxiv.org/pdf/2609.07328)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout
- 作者：Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07328

### 一句话总结
PV-WM 提出一种仅依赖历史轨迹的异构微观-宏观世界模型，将行人关节运动与车辆刚体状态同步滚动预测，以统一框架完成行人-车辆协同未来推演。

### 研究问题
现有行人-车辆预测方法割裂处理两类对象：道路代理预测器通常忽略行人关节细节，而姿态预测器又不覆盖车辆未来状态。如何在一个统一的递归模型中同步预测行人的根运动与15关节姿态，以及车辆的刚体运动状态，是本文要解决的核心问题。

### 核心思路/方法
- 构建历史观测驱动的世界模型（history-only），在同步异构状态空间中进行递归推进。
- 递归更新三部分：行人根运动、15关节姿态、车辆运动学状态。
- 生成的“行人块”和“车辆块”构成下一层递归的边界条件。
- 车辆边界框由预测的中心与朝向（结合观测到的尺寸）重建；每个转移步后重新计算行人-车辆（P-V）之间的几何关系。
- 所有道路代理共享同一网络，而非分模块专家系统。

### 主要贡献
1. 提出首个能协同滚动预测行人与车辆的异构世界模型，涵盖行人关节与车辆刚体两种动力学。
2. 相比匹配的一次性完整状态预测器，递归执行将 Root ADE 降低 12.7%、MPJPE 降低 14.8%。
3. 反馈干预实验表明，后序预测依赖所生成关节内容、时间顺序及行人身份。
4. 在 824 个对齐的 Waymo 场景（其中 797 个有有效车辆未来支持）中，相比验证集精选的 Modular Specialist，Root ADE 降低 5.2%、MPJPE 降低 7.6%、P-V 距离误差降低 11.9%、定向框最近距离误差降低 5.8%。
5. 模型架构更高效：参数量减少 57.1%，平均 FLOPs 降低 96.5%，实测 p95 延迟降低 25.5%。

### 局限性
摘要未提供关于失败模式、泛化边界、不同路况或极端场景表现的具体信息，因此该部分摘要未提供足够信息。另未提及对遮挡、检测噪声或长时递归误差积累的处理说明，亦属摘要未覆盖范围。

### 阅读优先级
**高**。理由：该工作同时解决行人关节预测与车辆预测之间的割裂问题，具有明显跨子领域整合价值；在 Waymo 基准上相对模块化专家系统有一致且多指标的增益，效率收益也很突出；对于多智能体仿真、自动驾驶规划与具身智能研究均有借鉴意义。

</details>

<details>
<summary>Abstract</summary>

Local pedestrian-vehicle forecasting spans heterogeneous physical scales: pedestrians combine root locomotion with articulated motion, whereas vehicles are rigid bodies described by kinematic state and oriented extent. Existing road-agent forecasters typically omit pedestrian articulation, while pose forecasters leave vehicle futures outside the learned rollout. We introduce PV-WM, a history-only world model over structured post-perception tracks. It recurrently advances pedestrian root motion, 15-joint articulation, and learned vehicle states within a synchronized heterogeneous state. The generated pedestrian and vehicle chunks supply the next recurrent boundary; vehicle boxes are reconstructed from predicted center and heading with observed extent, and P-V geometry is recomputed after every transition. Relative to a matched one-shot complete-state predictor, recurrent execution reduces Root ADE by 12.7% and MPJPE by 14.8%. Feedback interventions show that later predictions depend on the content, temporal order, and pedestrian identity of generated articulation. Across 824 aligned Waymo contexts, with 797 providing valid future vehicle support, PV-WM reduces Root ADE by 5.2%, MPJPE by 7.6%, P-V distance error by 11.9%, and oriented-box closest-approach error by 5.8% relative to a validation-selected Modular Specialist. The single-network model uses 57.1% fewer parameters, 96.5% lower average FLOPs per local scene, and 25.5% lower measured p95 latency. PV-WM unifies this heterogeneous future state while preserving type-specific pedestrian and vehicle dynamics.

</details>

#### 2026-09-07 - KODAMA: Multimodal Digital Twin Reconstruction for Urban RF Propagation Modelling

**Authors:** Maximiliano Wardle, A. Ryo Koblitz
**Links:** [abs](https://arxiv.org/abs/2609.07298) - [pdf](https://arxiv.org/pdf/2609.07298)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** 3D reconstruction, photogrammetry, digital twin

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：KODAMA: Multimodal Digital Twin Reconstruction for Urban RF Propagation Modelling
- 作者：Maximiliano Wardle, A. Ryo Koblitz
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications（主要）；3D Reconstruction & Multi-view Geometry（次要）
- 链接：https://arxiv.org/abs/2609.07298

### 一句话总结
KODAMA 是一种全自动的城市射频数字孪生（RFDT）重建管线，无需现场勘测或校准，仅凭公开地理空间数据即可生成可用于光线追踪的城市场景，其非校准预测误差与手工校准模型接近。

### 研究问题
如何在无需现场勘测与人工校准的前提下，自动构建城市场景中面向射频传播建模（RFDT）的、可直接用于光线追踪的三维重建结果，使通信信道行为与真实世界一致。

### 核心思路/方法
- 核心思想：以射频行为而非几何或视觉保真度为重建目标，自动构建"光线追踪可用"的RFDT。
- 输入数据：仅依赖现成的多模态地理空间数据——航拍影像、LiDAR、摄影测量以及街景图像。
- 技术流程：
  - 由航拍影像、LiDAR 与摄影测量生成地形和水密建筑网格；
  - 通过街景图像的曝光加权多视角融合，恢复立面细节、电磁材料属性以及杂波（clutter）。
- 输出：全自动、无校准的城市级RFDT，用于射频传播预测。

### 主要贡献
- 提出一种自动化管线，可在城市规模上由现成地理空间数据重建光线追踪就绪的RFDT，无需现场勘测或校准。
- 在3个站点（覆盖3.6–28 GHz频段）验证中，KODAMA的非校准预测达到个位数的RMSE；
- 与自动基线相比，点对点误差最多降低5.35 dB；
- 与手工构建且经测量校准的RFDT相比，误差仅相差0.22 dB。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作在无校准条件下实现了接近手工校准模型的射频预测精度，且误差显著优于自动基线，方法上同时涉及多模态三维重建与射频建模，对城市级数字孪生和无线信道预测方向具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

3D reconstruction typically strives for geometric fidelity or visual plausibility. Radio frequency digital twins (RFDT) are instead judged by whether communication channels behave in them as they do in the real world. RFDTs promise site-specific channel prediction but current practice forces a choice between coarse automated scenes and hand-built, measurement-calibrated models that take weeks to construct per-site. We present KODAMA, an automated pipeline that reconstructs ray tracing-ready RFDTs at city scale from off-the-shelf geospatial data alone: aerial imagery, LiDAR, and photogrammetry yield terrain and watertight building meshes, while exposure-weighted multi-view fusion of street-level imagery recovers façade relief, electromagnetic materials, and clutter---all without site visits or calibration. Across three sites spanning 3.6 to 28 GHz, KODAMA's uncalibrated predictions achieve single-digit RMSE, reducing point-to-point error by up to 5.35 dB over automated baselines and coming within 0.22 dB of a measurement-calibrated, hand-built RFDT.

</details>

#### 2026-09-07 - SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem

**Authors:** Soohyun Ryu, Sohee Kim, Eunho Yang
**Links:** [abs](https://arxiv.org/abs/2609.07064) - [pdf](https://arxiv.org/pdf/2609.07064)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, spatial intelligence

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking Problem
- 作者：Soohyun Ryu, Sohee Kim, Eunho Yang
- 出版日期：2026-09-07T05:41:13Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07064

### 一句话总结
本文提出通过合成积木堆叠任务数据集 SpatialBlock-15k 训练大型视觉语言模型（LVLMs），以提升其从2D图像推断3D结构信息的“空间智能”。

### 研究问题
大型视觉语言模型从2D图像中重建并推理场景3D结构的能力（即空间智能）存在不足；现有利用真实场景空间问答数据集的方法依赖密集几何标注，成本高、耗时长且因外部感知模块而产生噪声。

### 核心思路/方法
受人类认知发展启发，提出通过结构化积木操作任务来学习基础空间技能。具体构建了包含15,000个积木堆叠问题的合成数据集 SpatialBlock-15k，覆盖3D到2D投影、视角变换和结构组合三类任务。数据集中引入受控颜色调制作为视觉线索，以鼓励模型在视觉复杂条件下进行基于锚点（anchor-based）的推理。训练方式包括直接回答和基于推理链的预测两种范式。

### 主要贡献
1. 提出一种新的训练范式，通过合成积木堆叠问题提升LVLMs的空间智能，而非依赖真实场景标注数据集。
2. 构建并发布 SpatialBlock-15k 合成数据集，覆盖多种空间推理子任务，并包含颜色调制作为辅助视觉线索。
3. 实验表明，在该合成数据集上训练的LVLMs显著优于基线，并能泛化到真实世界空间任务，尽管数据集本身为合成且规模紧凑。
4. 公开代码与数据。

### 局限性
摘要未提供足够信息，未说明模型在何种具体真实任务上的泛化程度、最大性能上限、数据规模增长的效果以及颜色调制策略在不同模型架构上的通用性。也未见对失败案例或训练计算成本的详细讨论。

### 阅读优先级
**高**。理由：该工作针对LVLMs空间智能这一重要缺陷，提出合成数据驱动的低成本训练范式，且在真实任务上展示泛化能力。对于研究空间推理、合成数据训练或LVLMs能力增强的读者具有直接参考价值，且作者公开代码与数据，易于复现和延伸。

</details>

<details>
<summary>Abstract</summary>

Large Vision-Language Models (LVLMs) have achieved strong performance on diverse visual tasks, yet their ability to reconstruct and reason about the 3D structure of the scene depicted in 2D images -- referred to as spatial intelligence -- remains limited. Existing approaches attempt to address this gap by using real-scene spatial question answering datasets that require dense geometric annotations. However, constructing such labels is costly, time-consuming, and often noisy due to reliance on external perception modules. In this work, we propose a novel paradigm inspired by human cognitive development: learning foundational spatial skills through structured block-manipulation tasks. We introduce SpatialBlock-15k, a synthetic dataset of 15,000 block-stacking problems covering 3D-to-2D projection, viewpoint transformation, and structural combination. The dataset further incorporates controlled color modulation as visual cues to encourage anchor-based reasoning in visually complex conditions. Experiments demonstrate that LVLMs trained on our dataset through either direct answering or reasoning-based prediction significantly outperform baselines and generalize to real-world spatial tasks, despite the dataset's synthetic and compact nature. Code and data are available at https://github.com/rsoohyun/SpatialBlock.

</details>

#### 2026-09-07 - WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation

**Authors:** Jie Yin, Zeyuan Zhao, Xiaojing Tan, Yang Liu, Chiyu Wang, Xinyang Gu
**Links:** [abs](https://arxiv.org/abs/2609.07002) - [pdf](https://arxiv.org/pdf/2609.07002)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation
- 作者：Jie Yin, Zeyuan Zhao, Xiaojing Tan, Yang Liu, Chiyu Wang, Xinyang Gu
- 出版日期：2026-09-07
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.07002

### 一句话总结
本文提出WM-Craftnet，一种以世界模型为条件框架的灵巧手内操作策略，利用多模态潜动力学提升多物体旋转的泛化性与抗扰动能力。

### 研究问题
如何利用部分且有噪声的多模态观测（本体感觉、深度、触觉）推断物体位姿、几何、接触与滑动，以实现泛化且鲁棒的灵巧手内操作策略。

### 核心思路/方法
- 学习紧凑的动作条件潜动力学模型，输入来自本体感觉、深度、触觉和动作，由多模态重建和奖励预测信号监督。
- 并非将世界模型用于潜在想象或策略优化，而是将其学到的“World Synesthesia Model (WSM)”作为非对称Actor-Critic策略的循环任务上下文。
- WSM专门训练从带噪深度输入重建干净的深度目标，为真实机器人部署提供去噪的几何状态。
- 在9个z轴物体上预训练WSM，作为后续49个物体下游策略学习的可复用先验。

### 主要贡献
- 提出以世界模型为条件、用于灵巧手内操作的框架WM-Craftnet。
- 设计将WSM作为策略循环上下文而非用于想象的机制。
- 通过干净深度监督实现去噪几何状态，支持sim-to-real迁移。
- 预训练WSM可跨物体泛化，提升多物体旋转性能。
- 通过消融实验验证预测性世界建模、清洁深度监督和触觉接触线索对所学状态的作用。

### 局限性
摘要未提供足够信息，未明确说明失败的场景、计算开销、对传感噪声的鲁棒性边界，或与SOTA方法的定量对比细节。

### 阅读优先级
**中**
理由：该工作关注灵巧操作中的多模态融合与领域泛化，方法上有一定新颖性（世界模型作为上下文而非规划器），且展示了跨物体迁移与真实部署证据；但摘要中未给出与现有方法的直接性能比较，实验细节有限，适合对该方向有具体兴趣的读者作为参考，而非紧急必读。

</details>

<details>
<summary>Abstract</summary>

Generalizable and robust dexterous in-hand manipulation requires a policy to infer object pose, geometry, contact, and potential slip from partial and noisy observations. Although recent tactile and visuotactile RL methods achieve strong in-hand rotation in controlled settings, their robustness often degrades under pose shifts, force disturbances, and object variation. We propose WM-Craftnet, a world-model-conditioned framework that learns compact action-conditioned latent dynamics from proprioception, depth, tactile sensing, and actions, supervised by multimodal reconstruction and reward prediction. Rather than using the world model for latent imagination or policy optimization, WM-Craftnet uses the learned World Synesthesia Model (WSM) as recurrent task context for an asymmetric actor--critic policy. Importantly, WSM is trained to reconstruct clean depth targets from noisy depth inputs, providing a denoised geometric state for real-robot deployment. Ablations over recurrent baselines, auxiliary heads, tactile masking, and WSM modality heads show that predictive world modeling, clean-depth supervision, and tactile contact cues all shape the learned state. A WSM pretrained on nine \(z\)-axis objects serves as a reusable prior for \(49\)-object downstream policy learning. This context improves multi-object rotation, with quantitative and qualitative evidence for unseen-object, perturbation-recovery, and sim-to-real transfer.

</details>

#### 2026-09-06 - Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping

**Authors:** Jiahui Zhang, Gongbo Liang, Yu Zhang
**Links:** [abs](https://arxiv.org/abs/2609.06820) - [pdf](https://arxiv.org/pdf/2609.06820)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** mapping, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Diagnosing and Dynamically Filtering Occupancy World Models for Active Mapping
- 作者：Jiahui Zhang, Gongbo Liang, Yu Zhang
- 出版日期：2026-09-06
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.06820

### 一句话总结
本文诊断占用世界模型误差对主动建图规划的影响，发现单纯校正假阳性或假阴性并不总能提升覆盖率，并提出一种动态过滤策略以改善视点选择。

### 研究问题
占用世界模型（occupancy world models）中的预测误差如何影响主动建图（active mapping）中的视点规划与最终建图覆盖率？具体地，单独去除假阳性或恢复假阴性是否能提升规划性能，以及当几何模型准确时，规划和可达性是否仍是性能瓶颈？

### 核心思路/方法
- 固定规划器不变，仅改变提供给它的占用表示，构造五种条件进行对比：无补全、学习占用模型、经真值 oracle 去除假阳性、经 oracle 恢复假阴性、以及真值占用。
- 通过对比这些条件下的最终覆盖率和覆盖率效率，分析占用误差与下游规划性能之间的关联。
- 基于诊断结果，提出一种动态过滤策略：保留未探索空间中的预测，同时利用在线观测抑制被反复证伪的占用预测。

### 主要贡献
- 系统地诊断了占用世界模型误差对主动建图规划的影响，并指出占用准确性与规划性能之间存在差距。
- 发现真值占用对覆盖率效率的提升远大于对最终覆盖率的提升，说明规划和可达性即使在世界模型准确时仍是重要瓶颈。
- 提出一种动态过滤策略，初步实验表明其能将视点选择引向可达且原本会被遗漏的表面。

### 局限性
摘要未提供足够信息（如动态过滤策略的具体触发条件、定量实验对比结果、多种场景下的泛化性等均未披露）。

### 阅读优先级
**中**。理由：该文聚焦于主动建图与占用世界模型的诊断分析，方法新颖性一般，但研究问题针对当前基于学习完成模型的规划缺陷，结论具有实际参考价值；不过摘要显示实验规模为“初步示例”，定量深度有限，建议对相关方向感兴趣者阅读。

</details>

<details>
<summary>Abstract</summary>

Active mapping requires a robot to select camera viewpoints that efficiently reconstruct an unknown 3D scene. To reason about unobserved regions, recent systems use pretrained occupancy networks as world models that complete missing geometry. The predicted structure contributes to expected coverage gain and constrains feasible robot motion. Consequently, occupancy errors can change both what the robot chooses to explore and where it is able to move. We diagnose these effects by holding the planner fixed and varying only the occupancy representation provided to it. We consider planning without completion, with learned occupancy, with false positives removed by a ground truth oracle, with false negatives restored by an oracle, and with ground truth occupancy. Our experiments show that correcting false positives or false negatives alone does not consistently improve final coverage. This finding reveals a gap between occupancy accuracy and downstream planning performance. Ground truth occupancy provides a much larger improvement in coverage efficiency than in endpoint coverage, suggesting that planning and reachability remain important bottlenecks even when the geometric world model is accurate. Based on these findings, we introduce a dynamic filtering strategy that preserves predictions in unexplored space while suppressing repeatedly unsupported occupancy using online observations. Preliminary examples show that this strategy can redirect viewpoint selection toward reachable surfaces that would otherwise remain unobserved.

</details>

#### 2026-09-04 - WorldSculpt: Generating Compositional Worlds from Grounded Videos

**Authors:** Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
**Links:** [abs](https://arxiv.org/abs/2609.05416) - [pdf](https://arxiv.org/pdf/2609.05416)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 3DGS, robotics, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：WorldSculpt: Generating Compositional Worlds from Grounded Videos
- 作者：Muyao Niu, Jixuan He, Ruihan Yu, Lian Fu, Yonghao Yu, Zheng-Hui Huang, Yifan Zhan, Fengbo Lan, Yongtao Ge, Yinqiang Zheng, Kaipeng Zhang, Zhixiang Wang
- 出版日期：2026-09-04
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.05416

### 一句话总结
本文提出WorldSculpt方法，通过将强单物体3D生成先验扩展为多视角条件路径，仅用单物体数据微调即可生成包含数百个物体、严重遮挡场景的组合式3D网格表示。

### 研究问题
如何从多视角视频中生成由数百个独立物体网格组成的、处于共享世界坐标系下的组合式3D场景表示，尤其是在密集遮挡、单个视角仅能观测到部分几何的复杂场景下准确重建每个物体的完整形状。

### 核心思路/方法
采用"将强单物体3D生成先验适配到多视角观测"的范式：以Pixal3D为基础，扩展多视角条件路径，使模型在生成每个物体时能利用多个带位姿的观测信息进行grounding。关键设计是，模型仅在规范空间的单物体数据上微调，无需场景级训练即可泛化到包含严重遮挡的大规模场景。

### 主要贡献
- 提出WorldSculpt范式，证明复杂数百物体场景可通过适配单物体生成先验实现组合式生成，无需场景级训练。
- 引入UE-MeshyScene基准：包含密集杂乱场景、数百物体、逐物体标注和真值网格，用于评估此类任务。
- 在单物体、受控多物体及UE-MeshyScene上均优于先前方法，且场景越复杂、遮挡越严重，性能优势越明显。
- 展示将现有3DGS世界（如Marble、HY-World 2.0）转换为组合式网格场景的适用性。

### 局限性
摘要未提供足够信息，无法得知方法在实时性、内存开销、物体数量上限、泛化到未见场景类型等方面的局限。

### 阅读优先级
**高**
理由：该工作针对"密集遮挡场景的组合式3D生成"这一具挑战且具实际应用价值的问题，提出无需场景级训练的可扩展范式，并配套新基准，适合从事三维重建、生成模型及具身智能/AR应用的研究者关注。

</details>

<details>
<summary>Abstract</summary>

We study the problem of generating a compositional 3D representation of a cluttered scene containing hundreds of objects. The goal is to represent the scene as a collection of individual object meshes placed in a shared world frame, as required by downstream applications such as gaming, AR/VR, simulation, and robotics. This task is challenging in densely cluttered scenes, where objects heavily occlude one another and each view reveals only a fraction of their geometry. Geometry-based approaches typically reconstruct the scene as a single representation and leave incomplete geometry in occluded regions, while existing compositional methods with generative priors are largely limited to relatively simple scenes. We show that complex scenes with hundreds of objects can instead be generated compositionally by adapting a strong single-object 3D generative prior to multi-view observations. We instantiate this paradigm with Pixal3D, extending it with a multi-view conditioning pathway that grounds object generation in multiple posed observations. Although the model is finetuned entirely on single objects in canonical space, it generalizes to large scenes with severe occlusion without any scene-level training, demonstrating the feasibility and scalability of this paradigm. We further introduce UE-MeshyScene, a photorealistic benchmark of densely cluttered scenes with hundreds of objects, per-object annotations, and ground-truth meshes. Across single-object, controlled multi-object, and UE-MeshyScene evaluations, our method consistently outperforms prior approaches, with larger gains as scene complexity and occlusion increase. Finally, we demonstrate broader applicability by converting generated 3DGS worlds, such as Marble and HY-World 2.0, into compositional mesh scenes.

</details>

#### 2026-09-03 - GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation

**Authors:** Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
**Links:** [abs](https://arxiv.org/abs/2609.04193) - [pdf](https://arxiv.org/pdf/2609.04193)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：GIFT: Guided Intermediate Feature Training via Action-Oriented Structural Supervision for Robotic Manipulation
- 作者：Yupeng Zheng, Xiang Li, Songen Gu, Yuhang Zheng, Shuai Tian, Weize Li, Linbo Wang, Chaoyue Li, Qichao Zhang, Haoran Li, Zhongpu Xia, Ya-Qin Zhang, Shuicheng Yan, Dongbin Zhao
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.04193

### 一句话总结
本文提出GIFT框架，通过几何对齐、姿态预测与目标区域重建等结构监督来引导机器人操作的中间特征学习，弥补视觉丰富性与控制效用之间的“动作充分性差距”，并在多个操作任务上显著提升性能。

### 研究问题
机器人视觉语言预训练和世界模型提供的视觉特征虽丰富，但其原生的动作/视觉预测目标可能遗漏关键物理与任务结构，并保留与控制无关的视觉冗余。作者研究能否通过引导中间特征保留三种控制相关结构——几何（运动可行性）、姿态（指令相关实体）、目标（任务相关区域中的指令接地）——来弥合这一“动作充分性差距”。

### 核心思路/方法
提出GIFT（Guided Intermediate Feature Training）框架，一个架构灵活的中间特征学习方法。该方法将上述三种结构转化为训练时约束：
1. 几何对齐（geometry alignment）
2. 姿态预测（affordance prediction）
3. 目标区域重建（goal-region reconstruction）

GIFT被实例化到三种模型中：Vision-Language-Action（VLA）策略、直接动作世界动作模型（WAM）和逆动力学WAM，同时保留各模型原有的动作生成方式。

### 主要贡献
1. 提出动作充分性差距概念，指出视觉特征与控制效用之间的失配问题。
2. 提出GIFT框架，首次以显式结构监督（几何、姿态、目标区域）引导中间特征学习，跨模型架构适用。
3. 在LIBERO-Plus零样本迁移中，GIFT-VLA、GIFT-WAM-Fast、GIFT-WAM-IDM分别达到79.6%、72.6%、87.8%，较基线高出4.6、12.6、5.2个百分点。
4. 在RoboCasa上，三个变体分别达到61.4%、83.6%、82.3%，较对应基线高出12.6、9.0、8.4个百分点。
5. 尤其在与铰接物体任务及高精度真实操作中，在未见视觉与空间扰动下取得显著提升。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**

理由：该工作针对机器人操作中视觉-控制失配的核心问题，提出了一种不改变模型动作生成方式的轻量特征引导训练方法，且在多种模型架构和任务基准上均获得一致且显著提升。对从事视觉语言动作模型、世界模型与机器人操纵控制的研究者具有较强参考价值。

</details>

<details>
<summary>Abstract</summary>

Vision-language pre-training and predictive world modeling provide robot policies with rich semantic and dynamic visual features, but their native action and visual-prediction objectives may omit critical physical and task structure while retaining control-irrelevant visual redundancy. We call this mismatch between visual richness and control utility the action-sufficiency gap. We investigate whether this gap can be bridged by guiding intermediate features to preserve three control-relevant structure in robotic manipulation: geometry governing motion feasibility, affordance encoding instruction-relevant entities, and goals grounding instructions in task-relevant regions. To this end, we present GIFT (Guided Intermediate Feature Training), an architecture-flexible framework for learning intermediate features that translates these structures into training-time constraints through geometry alignment, affordance prediction, and goal-region reconstruction. We instantiate GIFT in a Vision-Language-Action (VLA) policy, a direct-action World-Action Model (WAM), and an inverse-dynamics WAM while retaining each model's action formulation. Under zero-shot transfer to LIBERO-Plus, GIFT-VLA, GIFT-WAM-Fast, and GIFT-WAM-IDM outperform StarVLA-OFT, Fast-WAM, and Fast-WAM-IDM by 4.6, 12.6, and 5.2 points, reaching 79.6%, 72.6%, and 87.8%, respectively. On RoboCasa, the three GIFT variants reach 61.4%, 83.6%, and 82.3%, outperforming their counterparts by 12.6, 9.0, and 8.4 points, respectively. Together, these results establish learning functionally structured intermediate features as a reusable principle across model-specific action formulations, with especially large gains on articulated-object tasks and high-precision real-world manipulation under unseen visual and spatial perturbations. Project page: https://openphoenix-team.github.io/GIFT-pages.

</details>

#### 2026-09-03 - A hybrid pipeline for dynamic ontology-based semantic mapping

**Authors:** Konstantinos Dimitropoulos, Ioannis Hatzilygeroudis
**Links:** [abs](https://arxiv.org/abs/2609.03891) - [pdf](https://arxiv.org/pdf/2609.03891)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** SLAM, mapping, localization, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：A hybrid pipeline for dynamic ontology-based semantic mapping
- 作者：Konstantinos Dimitropoulos, Ioannis Hatzilygeroudis
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：[摘要](https://arxiv.org/abs/2609.03891) | [PDF](https://arxiv.org/pdf/2609.03891)

### 一句话总结
本文提出了一种混合语义映射流程，结合外部标定摄像头、单应投影、对象检测与持续追踪，以及本体驱动的动态语义更新，构建机器人的动态语义世界模型。

### 研究问题
如何构建一个能够动态更新、具备上下文理解能力的机器人语义地图，并有效整合本体等先验知识以提升语义映射质量。

### 核心思路/方法
- 采用外部标定摄像头，通过单应投影完成几何映射与定位。
- 结合**对象检测**和**持续对象追踪**，获取实时感知数据。
- 使用**本体驱动**的语义更新机制，持续维护对象实例、空间属性和语义关系。
- 引入**线性回归模型**，对真实世界坐标的估计值进行校正。
- 选择本体作为知识表示形式，因其层级结构、语义表达能力及对动态世界建模的支持。

### 主要贡献
- 提出一个将几何映射、感知、追踪与本体语义更新相结合的混合语义映射流程。
- 引入本体驱动的动态更新，使语义模型可随实时数据持续调整。
- 使用回归模型校正坐标估计，提升映射精度。
- 展示了本体作为动态语义知识表示在机器人语义映射中的适用性。

### 局限性
摘要未提供足够信息。摘要中未提及实验设置、数据集、定量结果或对比基线，因此无法评估系统性能、适用范围及潜在限制。

### 阅读优先级
**中**

理由：该工作聚焦机器人语义映射，属于领域内较活跃方向，但摘要仅描述系统架构而未提供实验证据和定量评估。对于关注语义映射流程设计的读者有价值；若需评估方法有效性或复现对比，则需进一步阅读全文。

</details>

<details>
<summary>Abstract</summary>

Semantic mapping plays a crucial role in the ability of a robot to interact with objects, operate and navigate a complex environment. The most common pipeline for semantic mapping consists of geometric mapping and localization (SLAM), perception, semantic fusion and semantic representation. However, more recent works also integrate a form of prior knowledge in their application, most notably knowledge graphs or semantic scene graphs, to improve contextual understanding of the environment. In this paper, we present a hybrid pipeline for semantic mapping. Our system incorporates an external calibrated camera using homography projection for geometric mapping and localization, combined with object detection, persistent object tracking and ontology driven semantic updates to build a dynamic semantic world model. Linear regression models are also used for correction of the estimated values of real world coordinates. The system continuously updates object instances, spatial properties and semantic relations based on real time sensory data. Ontologies are selected as form of knowledge representation due to their hierarchical structure, semantic expressiveness and support for dynamic world modelling.

</details>

#### 2026-09-03 - MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?

**Authors:** Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
**Links:** [abs](https://arxiv.org/abs/2609.03715) - [pdf](https://arxiv.org/pdf/2609.03715)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?
- 作者：Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa
- 出版日期：2026-09-03
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03715

### 一句话总结
作者提出极小型视觉运动策略MINERVA（0.54M参数），在LIBERO基准上达到95.1%平均成功率，仅比使用7700倍参数的LeRobot π0.5低2.4个百分点，揭示该基准对模型容量的实际需求远低于当前主流超大模型。

### 研究问题
LIBERO操作基准实际需要的最小模型容量是多少？当前数十亿参数的VLA模型是否对该基准过度参数化？

### 核心思路/方法
- 设计MINERVA策略族（刻意紧凑的视觉运动策略），从0.25M到1M参数范围内扫描，衡量任务特定容量下限。
- 进行广泛的架构、训练和推理扫描，评估各因素（如action-chunk长度、视觉容量、流匹配vs直接L1回归）对性能的影响。
- 使用任务ID置换探针测试指令条件化是否只是记忆任务映射。
- 在LIBERO标准四套件（2000次rollout）、LIBERO-90（89个任务）和LIBERO-Plus扰动场景下评估。

### 主要贡献
- 首次实证估计LIBERO基准的任务特定容量下限：~0.25M以下性能崩溃，~1M处饱和。
- 0.54M参数策略达到95.1%平均成功率，与7,700倍参数的π0.5差距仅2.4点。
- 揭示action-chunk长度和视觉容量是唯二影响超出训练种子波动（±1点）的因素；流匹配相比L1回归无优势，且回归GPU速度快达3.8倍。
- 任务ID置换探针表明标准LIBERO指令条件化主要是在选择已记忆任务。
- 0.54M策略在笔记本电脑CPU上每chunk重规划仅5–9 ms，比SmolVLA快113倍、比π0.5快1,400倍。

### 局限性
- LIBERO-Plus扰动下性能降至46–56%，对光度扰动鲁棒性近乎为零，说明所测出的容量下限仅在标准LIBERO分布内成立，泛化性受限。
- 摘要未提供关于模型在真实机器人上部署的结果、训练数据规模、具体架构细节（如视觉编码器类型）等信息。
- 摘要未提及对更大规模模型蒸馏或容量自适应设计的实现方案。
- 摘要未提供其他基线（除LeRobot π0.5和SmolVLA外）的对比细节。

### 阅读优先级
**高**  
理由：该研究质疑当前VLA模型规模的必要性，提供LIBERO基准首个容量下限实证，结果极具实用价值（CPU实时推理、千倍参数压缩），对机器人策略设计和模型蒸馏方向有直接参考意义，且实验规模充分（多套件、多场景、多次seeds），结论可信度较高。

</details>

<details>
<summary>Abstract</summary>

Vision-language-action (VLA) models with billions of parameters now dominate the LIBERO manipulation benchmark, but the model capacity actually required by the benchmark remains unclear. We introduce MINERVA (MINimal Efficient Robotic Vision-Action policy), a family of deliberately compact visuomotor policies designed to measure this task-specific capacity floor. A 0.54M-parameter policy achieves 95.1% average success over 2,000 rollouts on the four standard LIBERO suites, only 2.4 points below the reported LeRobot $π_{0.5}$ result despite using 7,700$\times$ fewer parameters. Performance saturates near 1M parameters and collapses below 0.25M. Across broad architectural, training, and inference sweeps, only action-chunk length and vision capacity consistently exceed a $\pm$1-point training-seed band. Flow matching provides no detectable advantage over direct L1 regression across three seeds, while regression is up to 3.8$\times$ faster on GPU. A task-ID permutation probe shows that standard LIBERO instruction conditioning primarily selects among memorized tasks: changing only the task-ID mapping reduces success to near chance. The same recipe achieves 94.6% success across 89 LIBERO-90 tasks, while LIBERO-Plus perturbations reduce performance to 46--56%, with near-zero robustness to photometric shifts. The 0.54M policy replans every control step in 5--9 ms per chunk on a laptop CPU, 113$\times$ faster than SmolVLA and 1,400$\times$ faster than $π_{0.5}$, without a GPU. These results establish a first empirical estimate of LIBERO's task-specific capacity floor and motivate capacity-aware design and distillation for deployment-efficient robot policies.

</details>

#### 2026-09-03 - ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in Mixed Reality

**Authors:** Hongliang Yang, Yanjing Xu, Anhang Zhang, Hui Ye, Pengfei Xu
**Links:** [abs](https://arxiv.org/abs/2609.03596) - [pdf](https://arxiv.org/pdf/2609.03596)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, VR, mixed reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ReRoom: Blending Virtual and Physical Contexts for In Situ Room Planning in Mixed Reality
- 作者：Hongliang Yang, Yanjing Xu, Anhang Zhang, Hui Ye, Pengfei Xu
- 出版日期：2026年9月3日
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03596

### 一句话总结
ReRoom 是一个混合现实系统，通过将虚拟房间代理与真实房间空间对齐，支持用户在物理环境中进行原位房间布局设计、评估与迭代。

### 研究问题
真实家庭空间规划本质上是一个原位创作过程，但现有方法要么将布局编辑与物理房间分离，要么对在真实空间中原位评估和细化整体房间布局方案的支持有限。ReRoom 旨在解决如何在混合现实中实现高质量、可交互的原位房间布局规划问题。

### 核心思路/方法
ReRoom 提出了一种混合现实原位布局编辑系统，其核心思路包括：
1. 通过一个与目标房间空间对齐的虚拟房间代理，呈现共享布局状态，使交互和布局生成始终锚定在物理环境上下文中。
2. 用户可通过直接操作或语言输入来细化当前布局提案，系统保留用户已接受的摆放结果，使每次生成的更新都能延续同一个不断演进的设计过程。
3. 采用一种技能引导的布局智能体，该智能体将综合既有室内设计指南提炼出的三条原则，转化为可操作的房间布局设计技能，并基于扫描房间的归一化表示和可复用的几何检查来落地这些原则。

### 主要贡献
- 提出 ReRoom 混合现实系统，支持在真实房间环境中进行原位布局创作与迭代。
- 设计了一种技能引导的布局智能体，将室内设计指导原则形式化并用于真实房间布局生成。
- 实验表明 ReRoom 能针对非矩形房间生成高质量布局，且其原位工作流相比等效的离站 VR 工作流能改善房间规划体验。
- 论文接受后将公开代码。

### 局限性
摘要未提供足够信息，未明确提及系统在特定场景下的失败案例、交互复杂度上限、用户学习成本或计算资源需求等局限性。

### 阅读优先级
**中**。理由：本论文结合混合现实交互与自动化布局生成，聚焦原位房间规划这一具体场景，对开展 MR 交互设计、室内布局生成或人机协同设计研究的读者具有参考价值；评价实验仅提到“优于离站 VR”，未给出具体量化指标摘要，因此若不在相关方向的读者可暂缓精读。

</details>

<details>
<summary>Abstract</summary>

Planning a real domestic space is an in situ authoring process: users evaluate candidate layouts at true scale, refine their intent, and carry accepted decisions into later iterations. Existing approaches either separate layout editing from the physical room or provide limited support for evaluating and refining whole-room proposals in situ. We present ReRoom, a mixed-reality system for in situ room-layout authoring. ReRoom presents a shared layout state through a virtual room proxy spatially registered to the target room, allowing interaction and layout generation to remain grounded in the physical context. Users refine the current proposal through direct manipulation or language and preserve accepted placements, allowing each generated update to continue the same evolving design. To balance layout quality with generation efficiency, ReRoom uses a skill-guided layout agent whose room-layout design skill operationalizes three principles that we formulate by synthesizing established interior-design guidance for real-room layout generation. The skill grounds these principles in a normalized representation of the scanned room and reusable geometric checks. Evaluations show that ReRoom produces high-quality layouts for non-rectangular rooms, while its in situ workflow improves the room-planning experience over an otherwise equivalent off-site VR workflow. Code will be released upon acceptance of the paper.

</details>

#### 2026-09-02 - Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports

**Authors:** Yuqiao Xu, Erman Ayday
**Links:** [abs](https://arxiv.org/abs/2609.03055) - [pdf](https://arxiv.org/pdf/2609.03055)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robot perception

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports
- 作者：Yuqiao Xu, Erman Ayday
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.03055

### 一句话总结
本文提出任务限定感知导出框架TFPD，通过系统性评估发现机器人在隐私风险与任务效用之间不存在单一的“少看即安全”规律，不同表示方式在任务表现相同的情况下隐私泄露程度差异巨大。

### 研究问题
家庭机器人在将原始感知数据保留本地、仅导出结构化表示给下游规划器/云服务/日志/学习管道时，这些任务限定的感知导出仍可能通过语义、几何、空间结构及任务目标泄露家庭隐私；核心研究问题是如何系统衡量并缓解“任务限定”导出中的残余隐私风险，并检验更抽象或更少的感知信息是否必然带来更安全的隐私保护。

### 核心思路/方法
提出 Task-Functional Perception Distillation (TFPD) 框架，将丰富的感知保留在本地，同时对下游导出按照任务效用、直接暴露程度、和多种残余推断风险进行多维度刻画。实验采用120个AI2-THOR场景，划分场景不相交的训练/验证/测试集，使用冻结的攻击者选择和表示感知的留出攻击，评估导航、碰撞检测和目标目标执行三个任务。此外用ProcTHOR数据集进行复现，检验结论的稳健性。

### 主要贡献
- 揭示“字段移除或更强抽象不产生普遍性隐私排序”的现象，即减少感知信息并不自动带来更高隐私安全。
- 多个导航导出在任务表现完全一致（成功率为1.000，平均路径比为0.898）时，表示级链接性可在0.532至0.970之间大幅波动，隐私性能不能由任务效用推断。
- 将显式目标标签替换为目标区域使目标类别macro-F1从1.000降至0.077，同时保持任务成功率达0.995，验证了目标层面的隐私与效用可分离性。
- 几何粗化可使物体类别macro-F1从0.704降至0.556，但伴随可测的碰撞效用代价。
- ProcTHOR复现保持了任务等价性与隐私不等价性的核心发现，但改变了归一化与拓扑导出的相对排序，提示隐私评定需针对完整公开表示做任务特定、多风险评价。

### 局限性
摘要中未提供足够的局限性信息，例如计算开销、真实物理机器人场景验证、更广任务类型覆盖或对攻击者能力更细粒度的假设等均未提及。

### 阅读优先级
**中**。理由：该研究面向具身机器人感知导出的隐私评估，问题重要且方法框架（TFPD）具有参考价值，实验规模（120个场景）有限，但结论具备启发意义；若关注机器人隐私或具身AI安全方向，值得阅读；若属于其他方向，可暂缓。

</details>

<details>
<summary>Abstract</summary>

Domestic robots rely on rich perception to operate in private homes, but privacy risk persists even when raw sensor data remain local. Structured representations exported to downstream planners, cloud services, logs, or learning pipelines can still reveal household information through semantics, geometry, spatial structure, and task targets. We introduce Task-Functional Perception Distillation (TFPD), a task-scoped representation-export framework that keeps rich perception local and profiles downstream exports according to task utility, direct exposure, and multiple residual inference risks. Using 120 AI2-THOR scenes with scene-disjoint train/validation/test splits, frozen attacker selection, and representation-aware held-out attacks, we evaluate navigation, collision checking, and object-goal execution. Three navigation exports achieve identical success (1.000) and mean path ratio (0.898), yet representation-level linkability ranges from 0.532 to 0.970. Replacing an explicit target label with a target region reduces target-category macro-F1 from 1.000 to 0.077 while preserving success at 0.995, while geometric coarsening reduces object-category macro-F1 from 0.704 to 0.556 at a measurable collision-utility cost. A ProcTHOR replication preserves the navigation task-equivalence/privacy-inequivalence finding while changing the relative ordering of normalized and topological exports. These results show that neither field removal nor stronger abstraction induces a universal privacy ordering and motivate task-specific, multi-risk evaluation of the complete public representation.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
