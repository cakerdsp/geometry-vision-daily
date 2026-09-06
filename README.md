# Geometry Vision Daily

A daily updated collection of papers on geometry foundation models, 3D reconstruction, 4D reconstruction, and neural scene representations.

<!-- DAILY_REPORT_START -->
## 每日 AI 分析

## 每日 AI 分析

来源：`data/papers.json`、`data/processed_papers.json`、`interests.md`。

### 数据概况

- 当前滚动窗口论文数：59
- 分类分布：
  - Neural Scene Representations & Rendering: 21
  - 3D Reconstruction & Multi-view Geometry: 15
  - Embodied / Robotics / AR Applications: 14
  - Dynamic / 4D Reconstruction: 6
  - Geometry Foundation Models: 3
- 当前兴趣方向：未指定
- 当前显式任务：未指定

### 科研趋势综合分析

#### 今日主要趋势

1. **从"重建"走向"完成"：可控生成与场景补全成为核心交汇点** — 今日多篇论文不约而同地将三维重建的目标从"恢复可见表面"扩展为"生成未观测内容"。SPAR3S 从稀疏多视图图像补全完整场景，OctWorld 从单图沿相机轨迹生成世界一致的长距离视频，Z3D 则尝试从 3D 基础模型的内部表征解码新视角深度。这三篇论文横跨生成模型与重建表征，反映出"重建+生成"一体化建模的加速势头。

2. **在线与长序列场景中的漂移抑制成为 3D 重建新焦点** — Scal3R 直接面向长视频在线重建的几何崩溃问题，将固定首帧锚点改为多参考相对位姿查询，并结合位姿图优化抑制累计漂移；OctWorld 则用持久化 3D 记忆（OctMap）解决长距离生成中重新访问区域的几何不一致。两篇论文从不同入口（在线重建 vs 视频生成）抵达同一问题——如何在大范围、长时间跨度下维持全局一致性。

3. **3DGS 工程化加速与训练效率优化进入精细化阶段** — 3DGS 的基础渲染与训练机制仍在大幅演进。TileGS 深入 GPU 光栅化内核，用瓦片级深度分箱重排加速渲染；Laplacian Frequency Hierarchies 通过频率分层归档降低训练中活跃高斯数量；TruncGradGS 从优化器角度修复梯度消失问题。三者分别从渲染管线、训练调度和梯度更新三个层面优化 3DGS 效率与稳定性，表明该领域已从"能否重建"走向"多快多稳地重建"。

4. **点基神经表示的几何与外观联合编辑成为可编辑渲染新主线** — P-CORE 与 PointGT 两篇论文均由同一组学者牵头，立足点基表示无固定拓扑的优势，分别提出自监督表面一致性（应对大形变）和几何与纹理同步编辑。连同标题涉及的 3DGS 调色板级编辑工作，可编辑渲染正在从单一属性（颜色或几何）走向多属性、多模态交互的集成框架。

5. **机器人领域的"容量质疑"与"知识蒸馏式感知出口"带来反思性研究** — MINERVA 以 0.54M 参数的紧凑策略在 LIBERO 上逼近 70 亿参数模型的性能，对当前 VLA 模型"越大越好"的范式提出实证层面的挑战；隐私泄漏论文则系统揭示了任务限定感知导出中"抽象程度 ≠ 安全程度"的反直觉结论。两篇论文共同折射出机器人社区对模型规模、感知表示与任务效用之间真实关系的重新审视。

---

#### 技术路线观察

- **几何基础模型（Geometry Foundation Models）** 仍然稀缺。今日仅 Z3D 一篇直接利用 VGGT 这类 3D 基础模型的内部表征做下游解码。值得注意的是，Z3D 选择对内部表征施加潜在扩散，而非简单地线性解码，暗示此类模型的表征虽然信息丰富但并非"可直接读取"，中间需要生成式解码器。这可能与 Scal3R 中"冻结骨干 + 轻量 token 注入"的技术路线互补：一个在输入端用少量参数引导模型，一个在输出端用生成模型挖掘隐含几何知识。

- **3D/4D 重建** 明显分化为两个技术阵营：其一，经典几何路线（Bundle Adjustment、摄影测量）仍在演进——有论文将高阶几何关系（共面、平行）建模为"类相机实体"从而在保持 BA 稀疏结构的同时扩展优化对象；其二，生成式重建路线（SPAR3S、OctWorld）将扩散或自回归模型与显式空间结构（稀疏体素、八叉树）结合。这两条线路并非互相替代，而是逐步形成"几何提供约束、生成提供先验"的互补格局。

- **神经场景表示与渲染** 高度集中在 3DGS 生态的增量改良与编辑功能扩展。渲染层面关注内核效率（TileGS）与训练策略（Laplacian Frequency Hierarchies、TruncGradGS）；编辑层面则分化为基于点表示的统一编辑（PointGT、P-CORE）与基于 3DGS 的调色板/亮度专业编辑。前者走"通用理论"路线，后者走"工业可用"路线。

- **机器人/AR 应用** 的技术谱系更广：从 MINERVA 对操作策略容量的极限压测，到 GIFT 对 VLA 中间特征施加结构化监督（几何、姿态、目标区域），从焊缝识别的多视角摄影测量+语义分割管线，到本体驱动的动态语义建图。值得注意的是，这些工作中反复出现的共同技术元件是：几何先验（无论是焊缝的 3D 映射还是机器人的运动可行性）与语义/指令约束的关系——这正是 GIFT 称为"动作充分性差距"的核心问题。

---

#### 值得优先阅读的论文

1. **Scal3R（2609.04201）** — 它对"深度保持稳定但位姿头崩溃"这一失败模式的观察与利用极具启发性，暗示局部几何与全局位姿的解耦可能成为一种通用设计原则；此外"冻结骨干 + 1% 参数 token"的高效范式与其在 KITTI 上 60% 以上的 ATE 降幅均值得仔细验证。

2. **OctWorld（2609.03919）** — 它将 3D 表示（TSDF + 八叉树）作为扩散模型的持久记忆，直面长距离生成中最棘手的"重访区域一致性"问题。论文将 3D 重建技术反哺视频生成，这种交叉方向很可能成为后续热点。

3. **SPAR3S（2609.03931）** — 它提出无 3D 真值、仅靠多视图图像光度监督学习的稀疏体素隐空间，配合掩码自回归 Transformer 生成。该方法完全回避了 3D 标注瓶颈，思路简洁却有很强的扩展性，值得关注其在真实数据上的完整表现。

4. **Stable and Scalable Bundle Adjustment（2609.04026）** — 经典 BA 领域少有的统一化扩展。将高阶几何关系（共面、平行）建模为类相机实体并保持经典稀疏结构，这一数学构造既优雅又具有明确的实际管线价值，对多视几何研究者是必读。

5. **MINERVA（2609.03715）** — 以极小参数规模逼近超大 VLA 模型的性能，并系统揭示了 action-chunk 长度和视觉容量是唯一显著影响因子。这项研究对 LIBERO 基准的"任务容量下限"给出了迄今最直接的实证估计，对机器人社区理解当前基准的真实难度具有方法论意义。

---

#### 可能的研究机会

- **"重建-生成"的统一中间表征**：SPAR3S 的稀疏体素隐空间与 OctWorld 的动态八叉树记忆在概念上高度相似，都在寻找一种既能高效存储已观测几何、又能支持生成模型补齐未观测内容的中间状态。如果引入 Scal3R 的"冻结 3D 基础模型 + 旁路 token"策略，可能得到一种无需从头训练、直接对现有重建大模型进行场景补全的快捷路径。

- **在线一致性保持方法的跨域迁移**：Scal3R 的多参考位姿查询解决的是在线重建的累积漂移，OctWorld 的 3D 记忆解决的是长视频生成的重访不一致——两者本质都服务于"持续积累中的全局一致性"。这套方法论有望迁移到增量式语义建图、长期 SLAM、在线场景编辑等需要随数据流入持续性更新全局状态的任务中。

- **点基表示 + 3DGS 的编辑生态整合**：PointGT/P-CORE 展示的点基统一编辑框架与 3DGS 调色板级编辑（基于 SH 重参数化）各有优势：前者支持几何大形变，后者渲染质量和生态成熟度更高。目前尚未见到一个能同时支持自由几何形变和高效 SH/纹理编辑的统一框架；此外，如何将编辑能力扩展为多实例、跨场景可复用的"编辑先验"，也是一个开放问题。

- **面向可编辑性与生成性的正则化理论**：TruncGradGS 针对

### interests.md 指令分析

未指定额外兴趣方向或任务。

<!-- DAILY_REPORT_END -->

**Last updated:** 2026-09-04T12:19:32-04:00
**Total number of papers:** 59
**Number of papers added in the latest update:** 20
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

#### 2026-09-01 - Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison

**Authors:** Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit
**Links:** [abs](https://arxiv.org/abs/2609.01530) - [pdf](https://arxiv.org/pdf/2609.01530)
**Primary category:** Geometry Foundation Models
**Secondary categories:** None
**Matched keywords:** CroCo, pointmap, pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Revisiting Cross-View Completion: Self-Supervised Pre-Training via Reconstruction Error Comparison  
- 作者：Thibaut Loiseau, Guillaume Bourmaud, Vincent Lepetit  
- 出版日期：2026-09-01  
- 分类：Geometry Foundation Models  
- 链接：https://arxiv.org/abs/2609.01530

### 一句话总结
本文提出Gekko，一种将跨视图补全与掩码自编码的误差差异作为共视性代理信号、从而为所有掩码区域提供双目监督的自监督预训练方法。

### 研究问题
跨视图补全自监督预训练方法在重建非共视区域时参考视图提供信息不足，导致这些区域实质上退化为单目训练信号；如何将这一局限转化为有用的双向（双目）监督信号。

### 核心思路/方法
- 观察：跨视图重建误差相对于掩码自编码误差的相对改进程度可作为共视性的自监督代理——改进大表示共视区域，改进小表示非共视区域。
- 设计：Gekko网络从零开始联合训练三个任务：跨视图补全、掩码自编码，以及逐像素预测上述相对误差改进。
- 通过该相对改进预测，为所有掩码区域提供额外的双目信号，无需任何真值3D标注。
- 支持直接从原始视频训练，采用基于步长的课程学习，免去先前方法的复杂3D预处理。

### 主要贡献
- 提出Gekko框架，将跨视图补全的局限性转为可用的共视性代理信号，并引入额外的双目监督。
- 在零样本对应估计、相对位姿估计和点图回归上一致优于CroCo；在最严格相对位姿阈值下精度提升高达6倍，ETH3D端点误差降低22%。
- Gekko学习的额外通道本身即成为强共视性检测器；冻结特征优于同规模或更大规模的已发布跨视图骨干网络。
- 可从原始视频训练，匹配基于精选数据训练的模型，同时去除繁琐的3D预处理。

### 局限性
摘要未提供足够信息：未讨论方法在何种场景下失效、计算开销、对训练数据规模/多样性的依赖、与更大规模模型的比较细节等局限性均未提及。

### 阅读优先级
**高**。理由：该方法在3D视觉自监督预训练核心方向上提出新训练信号，并报告了跨多任务的一致性能提升；附带公开代码和模型，便于复现与验证，适合该领域研究者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Self-supervised pre-training via cross-view completion learns strong features for 3D vision from co-visible regions of image pairs. However, the reference view provides little information for reconstructing non-co-visible patches, implicitly yielding a monocular training signal in these regions. We introduce Gekko, which turns this limitation into a useful signal. The relative improvement of the cross-view reconstruction error over a masked-autoencoder error is a self-supervised proxy for co-visibility: large improvements indicate co-visible regions, negligible ones non-co-visible areas. Gekko is a network, trained from scratch, that jointly performs cross-view completion, masked autoencoding, and per-pixel prediction of this relative improvement, providing an additional binocular signal for all masked regions without any ground-truth 3D annotation. Under identical architectures and training data, Gekko consistently outperforms CroCo on zero-shot correspondence estimation, relative pose estimation, and pointmap regression, with up to 6 times higher accuracy at the strictest relative-pose threshold and a 22% drop in end-point error on ETH3D. The extra channel it learns is itself a strong co-visibility detector on unseen scenes, and Gekko's frozen features outperform released cross-view backbones of comparable or larger size. It can also be trained directly from raw videos with a simple stride-based curriculum, removing the cumbersome 3D preprocessing prior methods require while matching models trained on curated data. Code and pre-trained models are publicly available.

</details>

### 2026-08

#### 2026-08-30 - OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes

**Authors:** Muxin Liu, Tianbo Liu, Jing Xia, Xiaoyang Lyu, Xiaoshan Wu, Bo Wang, Peng Dai, Zhongrui Wang, Shaoshuai Shi, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2608.29881) - [pdf](https://arxiv.org/pdf/2608.29881)
**Primary category:** Geometry Foundation Models
**Secondary categories:** 3D Reconstruction & Multi-view Geometry
**Matched keywords:** monocular geometry, depth estimation, monocular depth, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：OptiGeo: Efficient Monocular Geometry for Embodied Perception in Optically Challenging Scenes
- 作者：Muxin Liu, Tianbo Liu, Jing Xia, Xiaoyang Lyu, Xiaoshan Wu, Bo Wang, Peng Dai, Zhongrui Wang, Shaoshuai Shi, Xiaojuan Qi
- 出版日期：2026-08-30
- 分类：Geometry Foundation Models（主分类）；3D Reconstruction & Multi-view Geometry（副分类）
- 链接：https://arxiv.org/abs/2608.29881

### 一句话总结
OptiGeo 提出一种偏差感知训练框架，利用少量透明目标渲染数据对单目深度估计模型进行局部几何矫正，以高效应对透明、反射等光学挑战场景中的传感器偏差问题。

### 研究问题
如何在透明、反射和高光等光学挑战性场景中，提升单目深度估计模型对真实传感器缺失或偏差数据的鲁棒性，避免对通用几何模型造成过度专门化，同时保持高效的部署规模。

### 核心思路/方法
- 将光学失效问题重新定义为基础模型训练中的局部失效模式，识别出传感器引发的监督偏差是关键瓶颈（模型从有偏的真实深度监督中继承了传感器失效模式）。
- 提出 OptiGeo，一种偏差感知训练框架：利用干净几何教师模型和残差裁剪对齐（residual-trimmed alignment）来修正有偏的真实监督。
- 将透明目标渲染重新定位为“干净光学几何”的紧凑来源，而非大规模领域专用微调数据集；仅用少量渲染数据即可学习透明物体及区域的几何结构，纠正真实传感器难以监督的局部几何失真。
- 模型参数量仅 30M，保持高效性。

### 主要贡献
- 提出传感器监督偏差是光学挑战场景下单目深度估计模型失效的关键瓶颈，并给出新的问题视角。
- 提出 OptiGeo 偏差感知训练框架，结合干净几何教师与残差裁剪对齐，有效修正有偏监督。
- 以少量透明目标渲染数据实现局部几何矫正，避免架构冗余和过度专门化。
- 在透明场景基准上以 30M 参数超越 300M 级单目模型及十亿级多视图基线方法，同时在通用零样本深度和边界锐度上保持竞争力。
- 通过真实世界导航案例验证了作为光学挑战场景中高效感知模块的实用性。

### 局限性
摘要未提供足够信息。未提及 OptiGeo 在非光学挑战场景（如极端光照、动态物体、遮挡严重等）下的表现，也未报告训练渲染数据的具体规模、生成成本或训练时间，以及与其他方法在计算开销上的详细对比。

### 阅读优先级
**高**。理由：该工作针对机器人部署中真实存在的传感器失效问题（透明/反射/高光），提出了一种参数高效（30M）且不依赖大规模特定领域数据的训练框架，在基准上显著超越更大规模模型，具备实际应用价值；同时问题定义新颖（传感器监督偏差），对单目几何领域的研究有启发性。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has achieved strong open-domain generalization, yet reliable robotic deployment remains difficult in transparent, reflective, and specular environments, where depth sensors often produce missing or biased depth. Existing methods often handle such optical failures with scene-specific preprocessing, auxiliary modules, or post-hoc fine-tuning. While effective in constrained settings, these designs increase architectural redundancy and can over-specialize general geometry models to narrow optical scenarios. We revisit this problem as a localized failure mode within base-model training and identify sensor-induced supervision bias as a key bottleneck: models inherit sensor failure patterns from biased real-depth supervision in optically challenging regions. We then introduce OptiGeo, a bias-aware training framework that rehabilitates biased real supervision using a clean-geometry teacher and residual-trimmed alignment. We redefine transparency-targeted rendering as a compact source of clean optical geometry, rather than a large domain-specific fine-tuning set. With only a small targeted rendering set, OptiGeo learns the geometric structure of transparent objects and regions, correcting local geometry distortions that real sensors cannot reliably supervise. Despite only 30M parameters, OptiGeo outperforms substantially larger 300M-scale monocular models and billion-scale multi-view baselines on transparent-scene benchmarks, while remaining competitive on general zero-shot depth and boundary sharpness. Real-world navigation cases further validate its practicality as an efficient perception module in optically challenging scenes.

</details>

## Dynamic / 4D Reconstruction

### 2026-09

#### 2026-09-02 - Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations

**Authors:** Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
**Links:** [abs](https://arxiv.org/abs/2609.02664) - [pdf](https://arxiv.org/pdf/2609.02664)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering, Embodied / Robotics / AR Applications
**Matched keywords:** 4D Gaussian, localization, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Query Rewriting for Complex Object Segmentation in 4D Gaussian Representations
- 作者：Thanh-Khoi Nguyen, Thien-Phuc Tran, Minh-Triet Tran
- 出版日期：2026-09-02
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02664

### 一句话总结
本文提出一种无需训练的查询改写策略，将冗长叙事性语言查询转化为精简关键词形式，从而显著提升4D高斯表示中复杂物体的时间定位与空间分割性能。

### 研究问题
现有4D高斯表示框架在进行语言引导的动态场景理解时，对冗长、叙事风格且包含噪声上下文信息的查询高度敏感，导致分割性能下降。本文研究查询改写对复杂物体分割的影响，探索如何通过压缩查询中的语言噪声来提升时空分割精度。

### 核心思路/方法
- 借鉴检索增强语言模型与关键词引导的查询重构思想，提出一种**无需训练的再解释策略**。
- 将长描述性查询逐步转化为**简洁的关键词接地形式**，在去除语言噪声的同时保留与物体中心表征相关的语义锚点。
- 在HyperNeRF和Neu3D数据集上进行验证，评估改写后查询对时间定位和空间分割的影响。

### 主要贡献
- 首次系统性研究查询改写对4D高斯表示中复杂物体分割的影响。
- 提出无需微调即可应用的查询重写策略，有效降低查询中的语言噪声。
- 实验显示：平均时间准确率从60.92%提升至92.21%，平均vIoU从20.08%提升至76.94%。
- 消融实验表明，更短、关键词聚焦的查询能带来更稳定的视频特征相似度分布，并与物体中心高斯表征更好对齐。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**
理由：该方法无需训练即可带来显著的性能提升（时间准确率提升超30个百分点，vIoU提升近57个百分点），且面向4D动态场景理解这一活跃研究方向，思路简洁、实用性强，值得快速阅读。

</details>

<details>
<summary>Abstract</summary>

Recent 4D Gaussian representation frameworks have demonstrated strong performance in language-guided dynamic scene understanding. However, these methods remain highly sensitive to verbose and narrative-style queries that contain noisy contextual information. In this paper, we investigate the impact of query rewriting for complex object segmentation in 4D Gaussian representations. Inspired by recent findings in retrieval-augmented language models and keyword-guided query reformulation, we propose a training-free reinterpretation strategy that transforms long descriptive queries into concise keyword-grounded forms. Our approach progressively reduces linguistic noise while preserving semantic anchors relevant to object-centric representations. Experiments on HyperNeRF and Neu3D demonstrate that concise rewritten queries significantly improve both temporal localization and spatial segmentation performance. In particular, our method improves average temporal accuracy from 60.92% to 92.21% and average vIoU from 20.08% to 76.94% without any additional fine-tuning. Extensive ablation studies further reveal that shorter, keyword-focused queries consistently yield stable video-feature similarity distributions and better alignment with object-centric Gaussian representations

</details>

#### 2026-09-02 - CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting

**Authors:** Kyungdae Park, Chae Eun Rhee
**Links:** [abs](https://arxiv.org/abs/2609.02184) - [pdf](https://arxiv.org/pdf/2609.02184)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, 4D Gaussian, Gaussian Splatting, view synthesis, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CC-4DGS: Computational Deformation and Point-Cloud Compression for Storage-Efficient Dynamic Gaussian Splatting
- 作者：Kyungdae Park, Chae Eun Rhee
- 出版日期：2026-09-02
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02184

### 一句话总结
CC-4DGS通过计算变形场与点云属性压缩两项技术，将动态4D高斯溅射的每场景存储量降至20–30 MB，同时保持与现有先进方法相当的渲染质量与实时性能。

### 研究问题
如何减少动态4D高斯溅射方法对大型多分辨率哈希表和高维高斯属性的存储依赖，实现存储高效且可扩展的动态场景表示。

### 核心思路/方法
- 提出**计算变形场（CDF）**：用确定性密集哈希编码和紧凑神经解码器替代大型可学习多分辨率哈希表，动态生成变形特征，将变形存储压缩至每场景1–3 MB。
- 提出**规范点云属性压缩（CCA）**：通过条件自编码、选择性量化与残差码本，压缩高维球谐外观项及辅助高斯属性，实现3–5倍点云数据缩减且质量损失可忽略。
- 两者结合形成统一表示，在保持实时渲染的前提下将总存储降至20–30 MB。

### 主要贡献
- 重新设计动态高斯溅射的变形建模与规范属性存储，提升存储效率。
- 计算变形场将变形存储大幅压缩至1–3 MB/场景。
- 点云属性压缩管线实现3–5倍压缩，且质量损失极小。
- 在N3DV与Technicolor Light Field数据集上，重建精度与Swift4D等先进方法相当，同时显著提升存储效率与运行时内存权衡。

### 局限性
摘要未提供足够信息：未说明方法在处理极长序列、大尺度场景或极端动态时的表现限制；未报告具体GPU内存占用数值、训练时间或对部署硬件的要求；未讨论压缩后在高帧率或高分辨率下的边界情况质量。

### 阅读优先级
**高** — 理由：该工作直击动态4D高斯溅射的存储瓶颈，提出了一种兼具明显压缩收益与质量保持的实际解决方案；实验覆盖两个公开数据集并与强基线对比，结果可信度高；对于从事动态场景表示、神经渲染及高效存储相关研究的人员具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Dynamic four-dimensional (4D) Gaussian Splatting has emerged as a powerful explicit representation for high-quality view synthesis, yet existing methods still require tens to hundreds of megabytes per scene due to their heavy reliance on large multi-resolution hash tables and high-dimensional Gaussian attributes. This paper presents CC-4DGS, a storage-efficient and scalable framework that rethinks both deformation modeling and canonical attribute storage. First, we introduce a computational deformation field (CDF) that replaces large multi-resolution learnable hash tables with deterministic dense hash encoding and compact neural decoders, enabling on-the-fly synthesis of deformation features while reducing deformation storage to only 1--3 MB per scene. Second, we propose a compression of canonical point-cloud attributes (CCA) pipeline that compresses high-dimensional spherical harmonic appearance terms and auxiliary Gaussian attributes via conditional autoencoding, selective quantization, and residual codebooks, achieving 3--5$\times$ point-cloud reduction with negligible quality loss. Together, these components yield a unified representation that preserves real-time rendering performance while reducing total storage to 20--30 MB. Extensive experiments across the N3DV and Technicolor Light Field datasets demonstrate that CC-4DGS achieves reconstruction accuracy comparable to state-of-the-art methods such as Swift4D, while offering significantly improved storage efficiency and favorable runtime-memory trade-offs.

</details>

#### 2026-09-01 - EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting

**Authors:** Wei Dong, Shahram Shirani, Jun Chen, Han Zhou
**Links:** [abs](https://arxiv.org/abs/2609.00994) - [pdf](https://arxiv.org/pdf/2609.00994)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic reconstruction, dynamic Gaussian, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：EvoGS: Modeling Deformation Evolution for Dynamic Gaussian Splatting
- 作者：Wei Dong, Shahram Shirani, Jun Chen, Han Zhou
- 出版日期：2026-09-01
- 分类：Dynamic / 4D Reconstruction（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2609.00994

### 一句话总结
EvoGS 将动态 3D 高斯变形建模为时间演化过程，通过持久化状态、历史外推与自适应校正，提升动态场景新视角合成的鲁棒性与质量。

### 研究问题
现有基于 MLP 的动态 3D 高斯泼溅（3DGS）方法在每个时间戳独立估计变形，难以应对大幅度或突变运动；如何利用时间连续性建模变形演化以提升动态重建质量是核心问题。

### 核心思路/方法
- 为每个高斯体维护持久化变形状态，而非逐时刻独立估计。
- 从历史变形状态外推未来状态，再使用 MLP 获得的观测进行校正。
- 校正权重自适应调节，利用时间残差记忆以及变形速度、轨迹偏差等演化统计量。
- 提出变形感知的稠密化策略：沿校正后的变形方向执行克隆与分裂，并用不确定性感知策略抑制变形历史不稳定区域的稠密化。

### 主要贡献
- 提出将动态高斯变形视为时间演化过程的新框架，替代逐时刻独立估计。
- 设计状态外推加 MLP 观测校正的双阶段机制，并引入自适应权重调节。
- 提出变形感知的稠密化方法，利用变形方向与不确定性提高重建质量。
- 实验表明在动态新视角合成任务上质量提升，并在多个基准上取得有竞争力的结果。

### 局限性
摘要未提供足够信息：未提及方法在特定场景（如极端运动、遮挡、实时性）下的限制，也未报告计算开销、内存占用或失败案例等详细局限性。

### 阅读优先级
**高**。理由：该工作直接针对动态 3D 高斯泼溅中变形估计的共性问题（对大幅/突变运动鲁棒性不足），提出新颖的演化建模思路，且引入变形感知稠密化作为辅助改进，方法层面具有较强创新性；适合关注动态/4D 重建与神经渲染的读者优先阅读。

</details>

<details>
<summary>Abstract</summary>

Recent extensions of 3D Gaussian Splatting (3DGS) enable real-time novel view synthesis in dynamic scenes by learning time-conditioned Gaussian deformations. However, existing MLP-based methods typically estimate deformations independently at each timestamp, making them less robust to large or abrupt motions. To address this issue, we propose \textbf{EvoGS}, a 3DGS-based dynamic reconstruction framework that models Gaussian deformation as a temporal evolution process. EvoGS maintains persistent deformation states for each Gaussian, extrapolates future states from historical deformation states, and corrects the predictions with MLP-derived observations. The correction is adaptively weighted using a temporal residual memory and evolution statistics such as deformation velocity and trajectory deviation. To further improve reconstruction quality, EvoGS introduces deformation-aware densification. Clone and split operations are performed along corrected deformation directions, while an uncertainty-aware strategy suppresses densification for Gaussians with unstable deformation histories. Experiments show that EvoGS improves dynamic novel view synthesis quality and achieves competitive performance across benchmarks.

</details>

#### 2026-09-01 - DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments

**Authors:** Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin
**Links:** [abs](https://arxiv.org/abs/2609.00619) - [pdf](https://arxiv.org/pdf/2609.00619)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic 3D, scene representation, rendering, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DSG: Dynamic 3D Scene Graph Construction for Embodied Agents in Changing Indoor Environments
- 作者：Ming Liao, Chao Ye, Jianing Fei, Weiyang Lin
- 出版日期：2026-09-01
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.00619

### 一句话总结
本文提出DSG，一个面向动态室内环境的3D场景图构建框架，通过3D高斯表示中的物体变化检测和基于多粒度视觉上下文的空间关系推理，提升场景图的动态更新与关系识别精度。

### 研究问题
室内环境中物体位置常因人类活动或智能体交互而改变，导致已有场景图与当前场景不一致，本文旨在解决动态环境下3D场景图的准确构建与更新问题。

### 核心思路/方法
1. 构建语义感知的3D高斯场景表示，提出基于双视角渲染的物体变化检测方法，以实现场景图节点的可靠更新。
2. 提出融合多粒度视觉上下文的空间关系推理方法，使大语言模型能识别更丰富的物体间空间关系。
3. 基于AI2-THOR仿真平台构建动态室内场景图基准DynTHOR，用于动态环境下场景图构建的评估。

### 主要贡献
- 提出DSG动态3D场景图构建框架，支持物体变化检测与空间关系推理。
- 设计基于双视角渲染的物体变化检测机制，提升节点更新的可靠性。
- 提出多粒度视觉上下文的空间关系推理方法，增强空间关系识别能力。
- 构建动态场景图基准DynTHOR，并在DynTHOR、3RScan及真实场景中验证方法有效性。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作面向具身智能与动态场景图构建，方法新颖且包含新基准，适合从事场景理解、具身智能相关研究的人员阅读；但摘要未给出量化性能对比或具体实验设置细节，论文重要程度需结合正文进一步判断。

</details>

<details>
<summary>Abstract</summary>

In indoor environments, object positions frequently change due to human activities or embodied-agent interactions, causing previously constructed scene graphs to become inconsistent with the current scene. To address this issue, we propose DSG, a dynamic 3D scene graph construction framework that detects object changes and performs spatial relationship reasoning. First, we construct a semantic-aware 3D Gaussian scene representation and develop a dual-view rendering-based object change detection method to enable reliable scene graph node updates. Second, we propose a spatial relationship reasoning method that incorporates multi-granularity visual context, enabling a large language model to identify a richer set of interobject spatial relationships. Furthermore, we introduce DynTHOR, a dynamic indoor scene graph benchmark built on the AI2-THOR simulation platform for evaluating scene graph construction in dynamic environments. Extensive experiments on Dyn-THOR, 3RScan, and real-world scenes demonstrate that DSG consistently outperforms existing methods in both object node construction and spatial relationship reasoning, significantly improving the accuracy of dynamic scene graph construction.

</details>

### 2026-08

#### 2026-08-31 - SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting

**Authors:** Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan
**Links:** [abs](https://arxiv.org/abs/2608.31023) - [pdf](https://arxiv.org/pdf/2608.31023)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** dynamic Gaussian, Gaussian Splatting, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：SMG: Semantic Motion Graph for Monocular Dynamic Gaussian Splatting
- 作者：Haozheng Yu, Xinyu Yang, Rundong Luo, Jennifer J. Sun, Bharath Hariharan
- 出版日期：2026-08-31
- 分类：Dynamic / 4D Reconstruction；Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.31023

### 一句话总结
本文提出语义运动图（Semantic Motion Graph, SMG），通过低秩语义运动建模单目动态高斯场景，以缓解无约束区域的过拟合与运动不确定性。

### 研究问题
动态高斯泼溅在单目视频重建中常对训练视角过拟合，在遮挡或复杂运动场景下因缺乏可靠正则化信号而失效。如何在弱约束区域获得可靠的运动建模？

### 核心思路/方法
- 关键洞察：真实场景运动具有语义一致性——空间接近且语义相关的区域往往具有相似动态。
- 构建语义运动图（SMG），将高斯运动建模为低秩语义运动：高斯运动由SMG节点驱动。
- 针对运动不确定性的来源（不可靠的现成先验和优化中弱约束区域），利用可靠图节点引导邻近不可靠节点的运动。

### 主要贡献
- 提出SMG方法，将高斯运动建模为低秩语义运动，利用语义一致性约束动态场景。
- 通过可靠节点引导不可靠节点，解决运动不确定性问题。
- 引入新的多视角数据集（ego-exo采集设置），用于评估现实场景下的动态高斯泼溅。
- 在多个具有挑战性的真实世界基准上达到单目动态高斯泼溅的最新性能。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对单目动态场景重建中的过拟合和弱约束问题提出新方法，具有明确的问题动机和创新点（语义驱动低秩运动建模），并附带新数据集，对动态场景建模方向具有较大参考价值。

</details>

<details>
<summary>Abstract</summary>

We study dynamic Gaussian Splatting from monocular videos. While recent advancements in dynamic Gaussian splatting offer a promising foundation for modeling dynamic scenes, they often overfit to the training views and fail under occlusion or complex scene motion due to the lack of reliable regularization signals in under-constrained regions. We propose Semantic Motion Graph (SMG), a novel approach models the Gaussian motion as the low-rank semantic motion. Our key insight is that the real-world scene motion is often structured by semantic coherence: regions that are spatially close and semantically related tend to exhibit consistent dynamics. To leverage this prior, we construct SMG to model structured motion of the scene. The Gaussian motion is driven by the motion of SMG nodes. We further observe that the uncertainty of Gaussian motion arises from both unreliable off-the-shelf priors and weakly constrained regions during optimization. SMG addresses this by using reliable graph nodes to guide the motion of nearby unreliable nodes. To evaluate dynamic Gaussian splatting under challenging real-world scenarios, we introduce a new multiview dataset collected under an ego-exo setup. Extensive experiments demonstrate that SMG achieves state-of-the-art performance on monocular dynamic Gaussian splatting across challenging real-world benchmarks. Project page: https://smg-gaussian.github.io/.

</details>

#### 2026-08-31 - Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction

**Authors:** Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won
**Links:** [abs](https://arxiv.org/abs/2608.30218) - [pdf](https://arxiv.org/pdf/2608.30218)
**Primary category:** Dynamic / 4D Reconstruction
**Secondary categories:** Neural Scene Representations & Rendering
**Matched keywords:** 4D reconstruction, scene flow, 4D Gaussian

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Amortized Anchor Refinement for Deployable Continuous-Time 4D Gaussian Reconstruction
- 作者：Jingong Chen, Qingwen Zhang, Sanghyeon Jun, Chulwoo Pack, Kyle Gao, Kwanghee Won
- 出版日期：2026-08-31
- 分类：Dynamic / 4D Reconstruction（次要：Neural Scene Representations & Rendering）
- 链接：https://arxiv.org/abs/2608.30218

### 一句话总结
本文提出一种面向可部署连续时间4D重建的“摊销锚点细化”方法，通过冻结骨干网络加短时优化，在固定计算预算下实现高质量重建，并可直接在独立XR头显上播放。

### 研究问题
如何使连续时间4D重建在独立XR头显等部署设备上变得可行，同时避免逐场景优化带来的过高计算成本，并解决前馈预测难以恢复场景细节的问题。

### 核心思路/方法
- 使用**冻结的骨干网络**预测初始高斯表示，获得快速的前馈估计。
- 在此基础上进行**短时、固定预算的优化**，专门化该表示以恢复场景细节。
- 引入**容量下限（capacity floor）**机制，保持表示密度，防止低预算下重建坍缩。
- 在无训练阶段，应用**持久同调约束**修剪不稳定的高斯体，同时保留拓扑持久结构。
- 将修剪后的轨迹直接作为**场景流**输出，用于最终渲染。

### 主要贡献
- 提出摊销锚点细化框架，结合前馈预测与短时优化，兼顾效率与细节恢复。
- 设计容量下限机制，确保低计算预算下不会发生重建坍缩。
- 提出训练无关的持久同调约束策略，用于稳定高斯修剪与结构保持。
- 在Stage-Capture基准上达到24.31±2.22dB，并在单个消费级GPU上完成目标预算内重建，实现XR头显端播放。

### 局限性
摘要未提供足够信息，未涉及方法在不同场景泛化性、处理大规模动态场景的显存需求、与现有全优化方法的性能差距的具体量化对比，以及持久同调约束在极端动态或稀疏视角下的鲁棒性。

### 阅读优先级
**高**
理由：论文面向XR头显等实际部署场景，提出结合前馈与短时优化的新范式，且报告了端到端可用结果（消费级GPU重建、头显播放），对4D重建与实时渲染方向具有较强实用价值。核心方法（摊销细化+拓扑约束）具备一定新颖性，值得深入阅读。

</details>

<details>
<summary>Abstract</summary>

Continuous-time 4D reconstruction remains impractical on standalone XR headsets. Per-scene optimization demands deployment-infeasible compute, and lower budgets cause collapse rather than degrade gradually. Feed-forward prediction is fast, but struggle to recover scene-specific detail. We present Amortized Anchor Refinement, which uses a frozen backbone to predict an initial Gaussian representation and a short optimization to specialize it under a fixed compute budget, with a capacity floor preserving representational density. A training-free stage then applies a persistent-homology constraint to prune unstable Gaussians while preserving topologically persistent structures, and streams the resulting trajectories directly as scene flow. On the Stage-Capture benchmark, Amortized Anchor Refinement achieves 24.31$\pm$2.22dB, while our deployment experiments demonstrate reconstruction within the target budget on a single consumer GPU and playback on a standalone XR headset.

</details>

## 3D Reconstruction & Multi-view Geometry

### 2026-09

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

#### 2026-09-02 - Adapting a Foundation Model for Lunar Surface Height Estimation

**Authors:** Patrick Bauer, Marius Schwinning, Melanie Siegel, Andreas Weinmann, Hichem Snoussi
**Links:** [abs](https://arxiv.org/abs/2609.02448) - [pdf](https://arxiv.org/pdf/2609.02448)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adapting a Foundation Model for Lunar Surface Height Estimation
- 作者：Patrick Bauer, Marius Schwinning, Melanie Siegel, Andreas Weinmann, Hichem Snoussi
- 出版日期：2026-09-02
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.02448

### 一句话总结
本文提出对基础模型 Depth Anything V2（DAV2）进行微调，使其能够可靠地估计月球表面的相对高度，为着陆危险地形检测提供辅助信息。

### 研究问题
如何将通用单目相对深度估计基础模型 DAV2 适配到月球表面场景，从而获得准确、可靠的相对高度估计，辅助危险地形定位？

### 核心思路/方法
作者指出已有工作仅将 DAV2 作为零样本基线用于月球 DEM 估计，未针对目标域做适配，因而可能表现不佳。为此，他们提出使用公开的、由立体摄影测量（SPG）生成的月球表面 DEM 数据，对 DAV2 模型进行微调，将其转变为适用于月球表面的相对高度估计器。

### 主要贡献
- 提出一种基于微调 DAV2 的月球表面相对高度估计方法；
- 利用公开 SPG 衍生的月球 DEM 数据进行领域适配；
- 实验表明，与零样本模型相比，微调后的模型在性能上有显著提升，能够作为可靠的月球表面相对高度估计器。

### 局限性
摘要未提供足够信息：未报告具体实验数据集规模、评测指标、定量结果数值、与现有方法的详细对比，以及微调带来的计算成本或潜在的过拟合问题等细节。

### 阅读优先级
**中**。理由：该方法针对未来月球任务的危险地形检测需求，对基础模型进行领域微调，思路直接且结果有提升，具有一定实用价值；但摘要未给出定量实验细节，创新性主要体现在“适配策略”而非新的网络架构，建议对月球感知或深度估计微调感兴趣的研究者可阅读，非核心领域者可暂缓。

</details>

<details>
<summary>Abstract</summary>

Digital elevation models (DEMs) can provide accurate height information, making it invaluable for analyzing the lunar surface. As the European Space Agency (ESA) prepares for future lunar missions that aim to land on the Moon, a precise method for height estimation will be essential for hazardous terrain that could endanger the landing approach. Traditional approaches to generate DEMs from imagery, such as shape from shading (SfS) and stereophotogrammetry (SPG) have been proven highly valuable for this task. However, due to advancements in machine learning, especially computer vision, the focus has shifted towards monocular depth estimation via deep learning. The lunar surface is covered by rocks and craters, and classic hazard detection methods rely solely on 2D image data. Our goal is to address this issue by developing a relative lunar surface height estimator that can provide additional information for hazard localization. In this letter, we present a methodology that builds on the well-known zero-shot relative depth estimation model Depth Anything V2 (DAV2). Other works have been using it as a state-of-the-art comparison for their proposed lunar DEM estimation method, but without adaptations to the target domain. Thus, it may underperform. Therefore, we propose a fine-tuning strategy with publicly available SPG-derived DEM data of the lunar surface. Our results demonstrate a significant improvement in performance compared to the zero-shot model, effectively transforming DAV2 into a reliable relative depth estimator of the lunar surface.

</details>

#### 2026-09-01 - Seeing the World and the Self from Egocentric Video

**Authors:** Kai Guan, Minchao Jiang, Ruichen WangLi, Wentao Zhu, Lei Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01276) - [pdf](https://arxiv.org/pdf/2609.01276)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** geometry foundation model, scene reconstruction, depth estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Seeing the World and the Self from Egocentric Video（从第一视角视频中感知世界与自身）
- 作者：Kai Guan, Minchao Jiang, Ruichen WangLi, Wentao Zhu, Lei Zhang
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.01276

### 一句话总结
本文提出统一框架 RESELF，从第一视角视频中联合恢复环绕场景的确定性度量几何与穿戴者的生成式全身运动，并显著优于各单独任务上的现有方法。

### 研究问题
如何从第一视角（自我中心）视频中，在共享度量坐标系下同时重建周围三维场景几何和穿戴者的全身运动？其中场景可见性高适合确定性几何回归，而身体被严重遮挡需要生成式运动推断，两类任务表现出不对称可见性与不同预测范式，联合恢复具有挑战性。

### 核心思路/方法
- 提出 RESELF（REconstructing the Scene and the sELF），统一框架将确定性度量几何重建与几何条件运动生成相结合。
- 将在大规模外部（exocentric）数据上预训练的几何基础模型适配到第一视角视频，采用逐帧尺度和相对位姿一致性目标。
- 利用产生的相机轨迹和潜在几何特征，作为扩散模型的条件来恢复穿戴者运动。
- 引入闭环运动学反馈阶段，在保持重建场景几何的同时进一步优化相机头部位姿。
- 从 EgoExo4D 中整理 EE4D-JSM 数据集，对齐第一视角视频、稀疏度量场景几何、相机轨迹与全身运动标注。

### 主要贡献
1. 提出首个（据摘要推断）统一处理第一视角场景重建与全身运动生成的框架 RESELF，解决两类任务不对称可见性与不同预测范式的问题。
2. 设计将大规模预训练几何基础模型适配到第一视角视频的训练目标（逐帧尺度与相对位姿一致性）。
3. 采用扩散模型进行几何条件化的身体运动生成，并加入闭环运动学反馈精化相机轨迹。
4. 构建 EE4D-JSM 基准数据集。
5. 实验表明 RESELF 在深度估计、相机跟踪和全身运动估计上均超过针对单个任务设计的现有最先进方法。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的失败情形、计算成本、对极端遮挡或复杂场景的鲁棒性等局限，也未提供消融分析或定量对比的具体数据。

### 阅读优先级
**高**。理由：该工作解决第一视角视频中场景重建与全身运动估计相互割裂的问题，提出统一定性几何重建与生成式运动推断的框架，属于 3D 视觉与人体运动分析的交叉热点方向。同时构造了新的数据基准，并在三个子任务上取得优于现有技术的性能，对相关研究者具有较高的参考价值。

</details>

<details>
<summary>Abstract</summary>

Complete 3D perception from egocentric video requires recovering the surrounding scene and the wearer's full-body motion in a shared metric frame. Existing methods typically address scene reconstruction and motion estimation separately: scene reconstruction methods ignore the wearer, whereas motion estimation methods lack explicit scene geometry and often depend on external trajectories. Joint recovery is challenging because the two tasks exhibit asymmetric visibility and require different prediction paradigms. The largely visible scene supports deterministic geometric regression, whereas the severely occluded body requires generative motion inference. We therefore propose RESELF (REconstructing the Scene and the sELF), a unified framework that couples deterministic metric geometry reconstruction with geometry-conditioned motion generation. RESELF adapts a geometry foundation model pre-trained on large-scale exocentric data to egocentric video using frame-wise scale and relative-pose consistency objectives. The resulting camera trajectory and latent geometric features condition a diffusion model that recovers the wearer's motion. A subsequent closed-loop kinematic feedback stage further refines the camera head while preserving the reconstructed scene geometry. To support training and evaluation, we curate EE4D-JSM from EgoExo4D by aligning egocentric video, sparse metric scene geometry, camera trajectories, and full-body motion annotations. Experiments show that RESELF outperforms state-of-the-art methods designed for the individual tasks across depth estimation, camera tracking, and full-body motion estimation. Code, models, and datasets will be available at https://ka1guan.github.io/RESELF/.

</details>

#### 2026-09-01 - Monocular Depth Estimation from a Single Image: Progress and Opportunities

**Authors:** Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, Ziyi Yang, Peng Dai, Xiaojuan Qi
**Links:** [abs](https://arxiv.org/abs/2609.01172) - [pdf](https://arxiv.org/pdf/2609.01172)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** metric depth, 3D reconstruction, SLAM, visual SLAM, depth estimation, monocular depth, robotics, robot perception, autonomous driving, augmented reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Monocular Depth Estimation from a Single Image: Progress and Opportunities
- 作者：Muxin Liu, Xiaoyang Lyu, Yang-Tian Sun, Yi-Hua Huang, Ziyi Yang, Peng Dai, Xiaojuan Qi
- 出版日期：2026-09-01T12:48:10Z
- 分类：3D Reconstruction & Multi-view Geometry；Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.01172

### 一句话总结
这是一篇关于单目深度估计（MDE）领域的综述论文，系统梳理了从早期学习方法到以基础模型（foundation models）为代表的最新进展，并展望了未来研究方向。

### 研究问题
单目深度估计（从单一图像中估计场景深度）作为计算机视觉的基础挑战，其研究演进路径、核心方法分类、代表性模型对比，以及该领域在基础模型时代面临的开放问题与机遇。

### 核心思路/方法
该综述按时间与范式将领域发展分为几个阶段进行梳理：
- 首先明确问题定义，区分相对深度估计与度量深度估计，指出十年研究中面临的关键挑战；
- 介绍常见的问题形式化方法以及广泛使用的数据集（室内、室外、合成数据）；
- 回顾基础模型时代之前的主要进展，提炼具有影响力的方法在精度、效率与鲁棒性方面带来的核心洞见；
- 聚焦近期基于基础模型的方法，将其划分为判别式（discriminative）与生成式（generative）两大范式，强调大规模预训练（如DINOv3）和合成数据的关键作用；
- 通过定量基准和定性示例比较代表性模型，并讨论向视频深度估计的自然扩展；
- 展示深度估计在视觉SLAM、内容生成、机器人感知等实际应用中的集成；
- 最后指出开放挑战和有前景的研究方向。

### 主要贡献
- 提供单目深度估计领域从早期到基础模型时代的全面综述，涵盖问题定义、数据集、方法演进与应用集成的完整链条；
- 将基础模型时代的方法归类为判别式与生成式两大范式，并指出大规模预训练与合成数据的核心价值；
- 通过定量与定性对比，帮助读者理解代表性模型的差异；
- 讨论深度估计向视频任务的自然延伸及其在视觉SLAM、内容生成、机器人感知等真实场景中的应用；
- 总结开放挑战与未来研究方向，为领域后续发展提供指引。

### 局限性
摘要未提供足够信息：未包含关于具体遗漏的研究方向、方法对比的详细量化结果，或综述所覆盖文献范围的明确边界等局限性说明。

### 阅读优先级
**高**。理由：单目深度估计是计算机视觉核心问题，与3D重建、机器人、自动驾驶、AR等领域直接相关。该综述覆盖了从经典方法到基础模型时代的最新技术进展（含DINOv3等前沿预训练模型），且作者团队来自知名机构，发表于2026年，时效性强，适合希望快速把握该领域全貌与未来趋势的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

Monocular depth estimation has long stood as a fundamental challenge in computer vision, enabling a wide range of applications including 3D reconstruction, robotics, autonomous driving, and augmented reality. This survey traces the field's evolution from early learning-based methods to the emergence of transformative foundation models. We begin by framing the problem, distinguishing between relative and metric depth estimation, and highlighting the key challenges that have shaped a decade of research. We then present common problem formulations and introduce the most widely used datasets, covering indoor, outdoor, and synthetic data. Following this, we review major advances prior to the foundation model era, distilling core insights from influential methods that contributed to improvements in accuracy, efficiency, and robustness. The survey then turns to the recent surge of foundation-model-based approaches, categorizing them into discriminative and generative paradigms and emphasizing the critical roles of large-scale pretraining (e.g., DINOv3) and synthetic data. We compare representative models using both quantitative benchmarks and qualitative examples, and discuss natural extensions to video-based depth estimation. Further, to illustrate real-world impact, we highlight the integration of depth estimation into applications such as visual SLAM, content generation, and robot perception. Finally, we outline open challenges and promising research directions as the field advances further into the era of foundation models.

</details>

#### 2026-09-01 - Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration

**Authors:** Yiran Zhou, Yingyu Wang, Shoudong Huang, Liang Zhao
**Links:** [abs](https://arxiv.org/abs/2609.01089) - [pdf](https://arxiv.org/pdf/2609.01089)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation, bundle adjustment, robotics

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Adaptive Depth-Map-Guided Bundle Adjustment for Correspondence-Free Multi-View Point Cloud Registration
- 作者：Yiran Zhou, Yingyu Wang, Shoudong Huang, Liang Zhao
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.01089

### 一句话总结
提出一种自适应的分层深度图引导束调整框架，用于无对应关系的多视角点云配准，以提升工业不规则钢废料场景下的三维重建精度与鲁棒性。

### 研究问题
在具有光滑金属表面、重复结构、遮挡和部分重叠的工业场景中，现有基于特征提取与数据关联的多视角配准方法容易建立错误对应关系，导致位姿估计不准确和重建失真。该文旨在解决这一问题，实现无需显式特征对应的多视角点云配准。

### 核心思路/方法
- 采用全局2.5D栅格表示场景，每个栅格单元可自适应维护多个深度假设。
- 将原始深度观测直接投影到全局地图中形成深度约束，无需显式特征对应。
- 当多个表面在同一栅格产生深度冲突时，通过基于softmax的层分配将每个观测关联到兼容的深度假设。
- 构建非线性最小二乘问题，联合优化传感器位姿与分层深度图；对应关系由深度图表示和投影模型隐式推导。

### 主要贡献
- 提出一种无对应关系的多视角点云配准框架，避免错误特征对应导致的问题。
- 通过自适应分层深度图表示处理多表面深度冲突。
- 在自采集工业数据集上验证，该方法在挑战性工业场景中达到稳定的重建精度，同时保持鲁棒性和低计算开销。
- 公开了开源代码。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该方法面向工业特种场景（不规则钢废料处理），核心贡献在无对应关系的多视角配准和分层深度图束调整，对从事三维重建、机器人感知相关研究的读者有参考价值；但实验仅基于作者自采集数据，缺少与主流方法的定量对比细节，普适性尚待验证。

</details>

<details>
<summary>Abstract</summary>

Robotic processing of irregular steel scrap requires dense 3-D measurement to replace manual visual assessment in hazardous cutting workcells. The reconstructed map is used to estimate piece dimensions, boundary geometry, feasible preheating and cutting regions, and collision-aware torch paths. The reconstruction errors therefore propagate directly to downstream measurement and planning. Existing multi-view registration methods commonly rely on feature extraction and data association to establish correspondences between views. In workcells with smooth metallic surfaces, repeated structures, occlusions, and partial overlaps, however, wrong correspondences may be established, leading to inaccurate pose estimation and distorted reconstruction. This paper presents an adaptive layered depth-map-guided bundle adjustment framework for correspondence-free multi-view point cloud registration. The scene is represented by a global 2.5-D grid, where each cell can adaptively maintain multiple depth hypotheses. Raw depth observations are directly projected into the global map to form depth constraints without explicit feature correspondences. At grid cells where multiple surfaces produce conflicting depths, a softmax-based layer assignment links each observation to compatible depth hypotheses. The resulting nonlinear least-squares formulation jointly refines sensor poses and the layered depth map, with correspondences implicitly induced by the depth-map representation and projection model. Experiments on self-collected industrial datasets show that the proposed method achieves consistently competitive reconstruction accuracy while maintaining robustness and low computational cost in challenging industrial scenarios. We release the open-source code implementation at: https://github.com/YiranZhou-Robotics/ADM-BA.git

</details>

#### 2026-09-01 - On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios

**Authors:** Zhe Shen, Liyuan Lou, Yifei Yu, Guanbo Wang, Quanjian Ji, Xin Wang, Zongqian Zhan
**Links:** [abs](https://arxiv.org/abs/2609.00923) - [pdf](https://arxiv.org/pdf/2609.00923)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** feed-forward 3D reconstruction, 3D reconstruction, rendering, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：On-the-Fly3R: Towards Robust Online 3D Reconstruction with Feed-Forward 3R Models for Large-Scale UAV Scenarios
- 作者：Zhe Shen, Liyuan Lou, Yifei Yu, Guanbo Wang, Quanjian Ji, Xin Wang, Zongqian Zhan
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.00923

### 一句话总结
提出一种无需训练的在线渐进式三维重建框架 On-the-Fly3R，通过检索引导的动态子集构建和验证-拒绝-重试机制，将前馈 3R 模型扩展到大规模无人机无序影像序列上。

### 研究问题
前馈 3D 重建模型在大规模无人机航测场景中面临 Transformer 注意力显存开销过大、以及对弱有序或无序影像流适应性不足的问题，现有可流式 3R 方法依赖时间和空间连续的输入，无法直接用于跨航线无人机作业。

### 核心思路/方法
- 提出 **训练无关的渐进式在线重建框架**，可适配多种现有 3R 骨干网络。
- 通过 **检索引导的动态子集构建** 从无序输入中选择空间相关的影像子集进行重建。
- 设计 **验证-拒绝-重试机制**：进行预集成一致性检查，自动拒绝错位影像并改用替代子集重试，以保证全局一致性。
- 借鉴 VSLAM 思想，基于检索闭环进行 **位姿图优化**，缓解相机漂移。

### 主要贡献
- 提出 On-the-Fly3R，首个面向大规模无人机场景的无需训练的在线三维重建框架，支持无序影像输入。
- 在多个 UAV 基准上将多种 3R 模型扩展到 5000+ 张影像、覆盖平方公里级场景。
- 相比多种 SOTA 流式 3R 方法，重建精度显著更优。
- 开源代码：https://github.com/Sh1nZzz/On_the_Fly3R

### 局限性
摘要未提供足够信息（未讨论时间效率、位姿图优化引入的额外计算开销、具体失败场景或对极端无序输入的上限等）。

### 阅读优先级
**中** — 该工作针对无人机大规模无序影像的三维重建提出了实用框架，对从事 UAV 测绘与在线重建的研究者有参考价值，但若您的兴趣不在此方向，影响力可能有限。框架无需训练便迁移到多种 3R 模型，适配性较强，建议相关方向读者关注。

</details>

<details>
<summary>Abstract</summary>

While feed-forward 3D reconstruction (3R) offers efficient end-to-end modeling, its application in large-scale UAV mapping is hindered by the prohibitive memory cost of Transformer attention. Current scalable streaming 3R methods assume temporally and spatially continuous inputs, rendering them ineffective for the weakly ordered or unordered image streams common in cross-strip UAV operations. To address this, we propose On-the-Fly3R, a training-free, progressive online 3D reconstruction framework for large-scale UAV images that upgrades various 3R backbones for large-scale UAV scenarios. Our method enables reconstruction from unordered inputs via retrieval-guided dynamic subset construction, which adaptively selects spatially relevant images. To further improve the robustness, a validation-rejection-retry mechanism is designed to guarantee global consistency, performing a pre-integration consistency check and automatically rejecting misaligned images and retrying with alternative subset. Finally, inspired by VSLAM, pose graph optimization based on the retrieval loop closure is employed to mitigate camera drift. Evaluations on several UAV benchmarks show that our On-the-Fly3R successfully scales various 3R models to over 5,000 images across square-kilometer UAV scenes, delivering substantially superior accuracy compared to several SOTA streaming 3R methods. Code is available at https://github.com/Sh1nZzz/On_the_Fly3R

</details>

#### 2026-09-01 - Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement

**Authors:** Hu Cao, Qianyi Yang, Xinyi Li, Jiong Liu, Yinlong Liu, Alois Knoll
**Links:** [abs](https://arxiv.org/abs/2609.00713) - [pdf](https://arxiv.org/pdf/2609.00713)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient and Robust Absolute Pose Estimation via Gravity-Prior-Driven Transformation Decoupling and Pose Refinement
- 作者：Hu Cao, Qianyi Yang, Xinyi Li, Jiong Liu, Yinlong Liu, Alois Knoll
- 出版日期：2026-09-01
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2609.00713

### 一句话总结
本文提出一种利用重力先验对绝对位姿估计进行变换解耦的方法，将6自由度问题降为4自由度，并配合全局投票与位姿精化算法，实现了高效且鲁棒的绝对位姿估计。

### 研究问题
如何在存在大量错误匹配的情况下，利用重力方向先验信息，高效且鲁棒地求解物体的绝对位姿（6自由度），并进一步从内点对应关系中获取精确的位姿解。

### 核心思路/方法
- 利用重力先验推导几何关系，通过变换解耦将原始6自由度绝对位姿估计问题简化为4自由度问题：1自由度旋转角 + 3自由度平移。
- 对1自由度旋转角采用一维全局投票算法进行最优估计。
- 获得最优旋转后，初步过滤错误匹配；平移估计退化为线性问题，易于求解。
- 引入一种新的位姿精化算法，同时提升旋转和平移的精度。

### 主要贡献
- 提出基于重力先验的变换解耦策略，将6自由度位姿估计简化为4自由度问题，显著提升效率。
- 设计1自由度旋转角的全局投票估计方法，增强对误匹配的鲁棒性。
- 提出新的位姿精化算法，进一步提升位姿精度。
- 在合成数据和三个公开真实数据集（TUM RGB-D、ETH3D、RobotCar）上验证了优于现有最先进方法的性能。
- 将方法集成到ORB-SLAM2中，在KITTI数据集上确认其能有效减少漂移并改善重定位时的轨迹对齐；代码将在论文接收后开源。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对机器人领域的基础问题（绝对位姿估计），在利用重力先验方面提出了新的变换解耦思路，显著降低问题维度，并在多个真实数据集及SLAM系统集成中验证了有效性。方法新颖且实用性强，对从事位姿估计、视觉SLAM及3D重建相关研究的人员具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

Estimation of the absolute pose of an object is an essential task for various robotic applications. Recently, incorporating gravity direction as prior information has emerged as a popular approach to simplify absolute pose estimation. However, developing a robust and efficient algorithm to solve this challenging problem remains a difficult question due to large amounts of mismatches. In addition, obtaining an accurate pose solution from selected inlier correspondences with gravity prior is still a research gap. In this paper, we propose a novel transformation strategy that exploits geometric relations derived from the gravity prior. Through transformation decoupling, the original 6 degrees of freedom (DoF) absolute pose estimation problem is simplified into a 4-DoFs problem: 1-DoF for the rotation angle and 3-DoFs for translation, significantly improving the efficiency. For the 1-DoF rotation angle, we apply a one-dimensional global voting algorithm for optimal estimation. Once the optimal rotation is obtained, the mismatched correspondences are preliminarily filtered, and translation estimation, a linear problem, can be easily solved. Furthermore, to obtain accurate pose results, we introduce a novel pose refinement algorithm to enhance the accuracy of both rotation and translation. Extensive experiments on synthetic data and three publicly available real-world datasets (TUM RGB-D, ETH3D, and RobotCar) demonstrate that the proposed method achieves stronger performance compared to existing state-of-the-art (SOTA) approaches. To further validate our method, we integrated it into ORB-SLAM2. The results on the KITTI dataset show it effectively reduces drift and improves trajectory alignment during relocalization. The source code will be released upon acceptance.

</details>

### 2026-08

#### 2026-08-31 - Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring

**Authors:** Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang, Supavadee Aramvith
**Links:** [abs](https://arxiv.org/abs/2608.31074) - [pdf](https://arxiv.org/pdf/2608.31074)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** pose estimation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Video Anomaly Detection Using YOLO Pose Estimation and CLIP-Based Semantic Scoring
- 作者：Vanodhya G. Warnasooriya, Amir Hajian, Watchara Ruangsang, Supavadee Aramvith
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry（主要类别）；无次要类别
- 链接：https://arxiv.org/abs/2608.31074

### 一句话总结
本文提出一个两阶段轻量级实时视频异常检测框架，利用YOLO v11n-pose提取人体关键点，并通过CLIP对裁剪人物区域与预定义异常行为文本进行语义相似度评分，在保持较高AUROC的同时实现了约51 FPS的端到端吞吐量。

### 研究问题
如何在不依赖光流、独立姿态估计器和基于密度的评分模块的情况下，设计一个轻量且实时的视频异常检测框架，同时维持可接受的检测精度。

### 核心思路/方法
- 第一阶段：使用YOLO v11n-pose在单次前向传播中检测人物并提取17个骨骼关键点。
- 第二阶段：将每个人物裁剪区域通过CLIP ViT-B/32编码，并与预定义的异常行为文本描述计算余弦相似度，以此进行语义评分。
- 整体架构取消了光流、独立姿态估计器和密度评分模块，实现端到端检测。

### 主要贡献
- 提出一个轻量级两阶段框架，简化了传统视频异常检测的复杂流程。
- 在CUHK Avenue、ShanghaiTech Campus以及朱拉隆功大学自建的室内数据集上进行了实验验证。
- 在NVIDIA Titan XP GPU上实现约51 FPS的端到端吞吐量，相比多特征基线获得3.36倍加速。
- 在三个数据集上分别取得89.26%、70.26%和84.13%的帧级AUROC。

### 局限性
摘要未提供足够信息。摘要未说明模型在特定异常类型上的表现差异、失败案例、对光照/遮挡等环境条件的鲁棒性、以及CLIP文本描述设计对结果的影响程度。

### 阅读优先级
**中**。理由：该工作结合了当前主流的人体姿态估计和CLIP语义特征，思路简洁且实时性突出，适合关注高效视频异常检测的读者；但上海科技大学的AUROC仅为70.26%，精度表现一般，且摘要未提供与SOTA的全面对比细节，因此优先级为中等。

</details>

<details>
<summary>Abstract</summary>

We propose a lightweight two-stage framework for real-time video anomaly detection. The first stage employs YOLO v11n-pose to detect persons and extract seventeen skeletal keypoints in a single forward pass. The second stage encodes each cropped person region through CLIP ViT-B/32 and computes cosine similarity against predefined textual descriptions of anomalous behaviors. This architecture eliminates the need for optical flow, standalone pose estimators, and density-based scoring modules. Experiments on CUHK Avenue, ShanghaiTech Campus, and a custom indoor dataset collected at Chulalongkorn University demonstrate an end-to-end throughput of approximately 51 FPS on an NVIDIA Titan XP GPU, a 3.36x speedup over the multi-feature baseline, while maintaining frame-level AUROC values of 89.26%, 70.26%, and 84.13%, respectively.

</details>

#### 2026-08-31 - Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling

**Authors:** Minghan Qin, Yuang Wang, Xiuyu Yang, Yushi Long, Yujian Zhang, Ruihuan Wang, Kai Ye, Yangang Zhang, Hang Li
**Links:** [abs](https://arxiv.org/abs/2608.30821) - [pdf](https://arxiv.org/pdf/2608.30821)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** Embodied / Robotics / AR Applications
**Matched keywords:** scene reconstruction, pose estimation, embodied AI, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling
- 作者：Minghan Qin, Yuang Wang, Xiuyu Yang, Yushi Long, Yujian Zhang, Ruihuan Wang, Kai Ye, Yangang Zhang, Hang Li
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry（主分类）；Embodied / Robotics / AR Applications（次分类）
- 链接：https://arxiv.org/abs/2608.30821

### 一句话总结
Lucida提出了一种“解析-生成-放置”的可组合真实到仿真场景建模流水线，通过重新分配各步骤的输入要求，使每步仅依赖真实捕获中可靠提供的信息，最终在场景级检测、位姿估计和重建等任务上显著优于现有方法。

### 研究问题
如何在杂乱的真实室内场景捕获中，恢复出“完整、可编辑、按观测排列”的物体资产，以构建可直接用于机器人仿真和具身AI的仿真场景副本——即解决现有“解析-生成-放置”三步管线中每一步都因真实捕获不理想（实例几何不精确、视角遮挡、资产与观测不匹配）而失败的问题。

### 核心思路/方法
Lucida保持“解析-生成-放置”的顺序，但重新分配了各步骤对输入的要求，使每步只消费真实捕获中可靠提供的信息，并将精度需求推迟到管线末端而非在起点强求。具体来说：
- **解析**：将视频解析为场景图，图中节点携带每个实例的多视角证据；
- **生成**：根据每个实例的多视角证据，生成该实例的完整资产；
- **放置**：使用GizmoAct（一个视觉语言模型策略），将放置问题转化为多轮GUI交互，通过闭环地操作物体的gizmo并在自身判断对齐达成时停止，完成资产放置。

### 主要贡献
- 提出Lucida，一种可组合真实到仿真场景建模的新流水线，其核心思想是重新分配各步骤的输入要求，使每一步仅依赖真实捕获中可靠提供的信息；
- 提出GizmoAct，一种基于视觉语言模型的放置策略，将物体放置建模为多轮GUI交互，支持闭环对齐和自主终止；
- 实验结果表明：在场景级3D物体检测上，Lucida在R2S-Scene上相对Boxer的mAP提升69%；在CA-1M上，ADD-SB@0.05从57.8%提升至83.4%；场景重建F-Score从SAM3D的0.794提升至0.924。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该论文针对真实到仿真场景建模这一对机器人仿真和具身AI有直接应用价值的任务，提出了一种重新分配各步骤要求的新颖流水线，并在三个任务上均取得了大幅度的性能提升（如mAP提升69%、ADD-SB提升约25个百分点、F-Score从0.794升至0.924），改进效果显著，值得重点关注。

</details>

<details>
<summary>Abstract</summary>

Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations. We propose Lucida, which keeps this order but redistributes the requirements, so each step consumes only what a real capture reliably provides and precision is reached at the end of the pipeline rather than demanded at its start. Lucida parses the video into a scene graph whose nodes carry per-instance multi-view evidence, generates a complete asset for each instance from its evidence, and places assets with GizmoAct, a VLM policy that casts placement as multi-turn GUI interaction, manipulating the object's gizmo in a closed loop and deciding itself when alignment is reached. Across scene-level 3D object detection, object pose estimation, and scene reconstruction, Lucida improves mAP over Boxer by 69% on R2S-Scene, raises ADD-SB@0.05 from 57.8% to 83.4% on CA-1M, and increases scene F-Score from 0.794 for SAM3D to 0.924.

</details>

#### 2026-08-31 - Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions

**Authors:** Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
**Links:** [abs](https://arxiv.org/abs/2608.30690) - [pdf](https://arxiv.org/pdf/2608.30690)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** SLAM, visual SLAM

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Failure or Drift? Evaluating Monocular SLAM under Synthetic and Real-World Corruptions
- 作者：Abhay Skaria Thomas, Shashank Agnihotri, Margret Keuper
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.30690

### 一句话总结
本文系统比较了单目SLAM系统在合成退化与真实恶劣条件下的表现，发现学习型跟踪器倾向于将灾难性丢失转化为持续漂移，且合成退化的物理保真度直接影响对真实世界系统排序的预测能力。

### 研究问题
合成退化压力测试能否有效替代真实世界恶劣条件，用于单目SLAM的鲁棒性评估？特别是，不同退化类型（图像空间、几何感知、复合）下，经典特征法与学习型跟踪器的失败模式（显式跟踪失败 vs 漂移积累）有何差异？

### 核心思路/方法
- 评估对象：一个经典特征法SLAM系统 + 两个学习型跟踪器。
- 退化类型：图像空间退化、几何感知退化、复合退化，以及与4Seasons真实恶劣条件的对比。
- 评估方式：不将鲁棒性简化为单一轨迹误差，而是区分“显式跟踪失败”与“方法保持运行但积累的漂移”两类行为。
- 核心比较：检验合成退化是否能得出与真实条件相同的工程结论（如系统排序是否一致）。

### 主要贡献
- 提出将“跟踪失败”与“漂移”分离评估单目SLAM鲁棒性的视角。
- 发现学习型跟踪器在退化下主要将灾难性丢失转化为持续性（有时严重）漂移。
- 揭示合成退化的物理保真度影响工程结论：结构化雨和雾代理能保持真实世界中的系统排序，而简单光照代理则不能。
- 提供代码开源：https://github.com/abhaythomas/master_thesis_vslamlab_robustness

### 局限性
摘要未提供足够信息（例如：未说明具体数据集规模、各退化参数设置、量化指标细节、失败/漂移的具体阈值或度量方式，以及经典方法在大幅退化下是否完全失效等）。

### 阅读优先级
**高**。理由：该工作直接挑战合成退化测试的效度假设，对SLAM鲁棒性评估方法论有重要参考价值；且发现学习型系统“以漂移换失败”的行为模式，对选择/开发鲁棒视觉里程计有实际指导意义。

</details>

<details>
<summary>Abstract</summary>

Visual SLAM is commonly evaluated on clean trajectories, although deployment failures are often caused by adverse weather, illumination, blur, and sensor artifacts. Controlled corruptions are attractive because they isolate such factors, but a synthetic stress test is useful only when it leads to the same engineering conclusion as the condition it is intended to approximate. This work examines that question for monocular SLAM. We evaluate a classical feature-based system and two learned trackers under image-space, geometry-aware, and compound corruptions, and compare their behavior with adverse conditions from 4Seasons. Rather than reducing robustness to a single trajectory error, the evaluation separates explicit tracking failure from drift accumulated by methods that remain active. The results show that learned trackers largely replace catastrophic loss with sustained, and sometimes severe, drift. More importantly, the apparent ordering of the learned systems changes with the physical fidelity of the corruption: structured rain and fog proxies preserve the real-world ordering, whereas a simple illumination proxy does not. Code is available at: https://github.com/abhaythomas/master_thesis_vslamlab_robustness.

</details>

#### 2026-08-31 - Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention

**Authors:** Bingde Liu, Wu Ran, Jinglei Zhang, Huanhuan Yuan, Chao Ma
**Links:** [abs](https://arxiv.org/abs/2608.30129) - [pdf](https://arxiv.org/pdf/2608.30129)
**Primary category:** 3D Reconstruction & Multi-view Geometry
**Secondary categories:** None
**Matched keywords:** depth estimation, monocular depth

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention
- 作者：Bingde Liu, Wu Ran, Jinglei Zhang, Huanhuan Yuan, Chao Ma
- 出版日期：2026-08-31
- 分类：3D Reconstruction & Multi-view Geometry
- 链接：https://arxiv.org/abs/2608.30129（PDF: https://arxiv.org/pdf/2608.30129）

### 一句话总结
本文提出Lapis，一种基于线性注意力的像素空间单步扩散生成框架，在保持高精度深度估计的同时大幅降低推理延迟。

### 研究问题
生成式框架在单目深度估计中表现优异，但其标准注意力的O(N²)复杂度和多步去噪过程在扩展到高分辨率图像时计算成本过高。如何在不牺牲结构一致性和细节质量的前提下，实现高效的一步式生成深度估计，是本文要解决的核心问题。

### 核心思路/方法
Lapis采用粗到细的层级设计：
- **Patch-level Consistency Module**：通过整合语义和空间先验来恢复结构的连贯性；
- **Pixel-level Refinement Module**：利用基于跳跃连接的像素对应关系恢复清晰的几何边界；
- **直接x预测策略**：借助流形假设，通过直接预测干净数据流形来减轻单步扩散中的采样噪声。

### 主要贡献
- 提出Lapis框架，将线性注意力与像素空间单步扩散结合，实现高效深度估计；
- 通过粗到细的模块设计，解决了直接应用线性注意力和一步预测导致的结构不一致、细节丢失和噪声问题；
- 在多个基准上达到SOTA精度和边界清晰度，推理延迟相比此前SOTA生成模型在1080P下降低最多7.6倍、在1440P下降低最多10.9倍。

### 局限性
摘要未提供足够信息。摘要中未讨论方法的失败案例、对特定场景（如弱纹理、动态物体）的鲁棒性、训练成本或模型参数量等潜在局限。

### 阅读优先级
**高**。理由：该工作直接针对生成式深度估计的计算瓶颈提出解决方案，在精度和效率上均取得显著改进，且适用于高分辨率场景，对从事深度估计、生成模型及高效注意力机制研究的读者具有较高参考价值。

</details>

<details>
<summary>Abstract</summary>

This work presents $\textbf{Lapis}$, a $\textbf{l}$inear-$\textbf{a}$ttention-based $\textbf{pi}$xel-$\textbf{s}$pace generative framework that achieves efficient and high-fidelity depth estimation with one-step diffusion. While generative frameworks have significantly advanced monocular depth estimation with superior detail fidelity, the $\mathcal{O}(N^2)$ complexity of standard attention and the multi-step denoising process introduce prohibitive computational costs when scaling them to high-resolution image applications. Although linear attention and one-step prediction are intuitively viable, directly applying them leads to poor structural consistency, detail loss, and noise. Lapis rectifies these limitations through a coarse-to-fine hierarchy. Specifically, a Patch-level Consistency Module restores structural coherence by integrating semantic and spatial priors. Subsequently, a Pixel-level Refinement Module recovers sharp geometric boundaries via skip-connection-based pixel correspondence. Furthermore, to mitigate sampling noise inherent in one-step diffusion, we leverage the manifold assumption and adopt a direct $\mathbf{x}$-prediction strategy to target the clean data manifold. Extensive evaluations on multiple benchmarks demonstrate that Lapis consistently achieves state-of-the-art (SOTA) accuracy and boundary sharpness across various resolutions, reducing inference latency by up to 7.6$\times$ at 1080P and 10.9$\times$ at 1440P resolution compared to previous SOTA generative models.

</details>

## Neural Scene Representations & Rendering

### 2026-09

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

#### 2026-09-02 - InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling

**Authors:** Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang
**Links:** [abs](https://arxiv.org/abs/2609.02747) - [pdf](https://arxiv.org/pdf/2609.02747)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under Unstructured View Sampling
- 作者：Tianheng Lu, Guangyu Wang, Ruqi Huang, Lu Fang
- 出版日期：2026-09-02
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02747

### 一句话总结
InceptionGS 通过将重建与生成先验巧妙结合，对大规模场景的高斯泼溅进行引导式自举修复，以应对非结构化视角采样下因部分区域视图稀疏而导致的渲染质量问题。

### 研究问题
在大规模场景数字化中，当采集到的多视角图像分布高度非结构化（大部分区域覆盖良好但局部区域观测不足）时，如何实现所有可能视角下一致且视觉上令人满意的渲染输出。

### 核心思路/方法
- 从初始高斯泼溅（Gaussian Splatting）出发，采用“生成式自举”（Generative Bootstrapping）策略。
- 在重建与生成之间进行巧妙权衡：对因视图稀缺导致的问题区域进行重新思考与修复，同时保持其余区域的重建质量。
- 通过软性引入场景自适应与视角自适应的生成先验（generative priors），实现对缺失观测区域的合理补全。
- 算法流程为迭代式引导修复，而非端到端单一生成或纯重建。

### 主要贡献
- 提出 InceptionGS 框架，首次在统一框架中平衡重建与生成，解决非结构化视角采样下的大规模高斯泼溅痛点。
- 引入场景与视角双自适应的生成先验软融合机制，使修复过程适应不同区域的稀疏程度。
- 在真实大规模场景上验证了方法的优越性与广泛适用性，证明其能处理非结构化影像并提升高保真高斯泼溅质量。
- 补充视频提供更直观的视觉演示效果。

### 局限性
摘要中提到“大规模真实场景”的实验均未在摘要中给出具体数据集、量化对比指标或失败案例细节，因此实验层面的局限性（如计算开销、极端稀疏下的表现上限、先验失效场景等）无法判断——**摘要未提供足够信息**。

### 阅读优先级
**高**，理由：  
- 该工作针对大规模场景重建中“真实且普遍”的视图非均匀覆盖问题，具有明确的实际应用价值。  
- 将生成模型与传统神经渲染结合是当前热点方向，框架设计上有新颖性（软性生成先验引导自举）。  
- 作者团队及发表时间具备一定新鲜度，适用于关注大规模渲染、高斯泼溅或神经场景表示的前沿研究者。

</details>

<details>
<summary>Abstract</summary>

Achieving truly immersive large-scale scene digitization necessitates consistent and visually pleasing rendering across all possible viewing perspectives. However, collecting multi-view images covering every fine detail of a large-scale scene is prohibitive due to scene complexity, capture cost, negligence, or accessibility constraints. As a result, the sampled views tend to be highly unstructured -- the majority of the scene is well covered yet certain regions inevitably lack sufficient observations. Existing reconstruction based methods are vulnerable to view scarcity while generation based approaches suffer from generalization, controllability, and 3D consistency issues. To address this challenge, we propose InceptionGS, which bootstraps Gaussian splatting by subtly balancing reconstruction and generation. Starting from an initial Gaussian splatting, InceptionGS reasonably rethinks and repairs problematic regions caused by view scarcity while preserving the quality elsewhere, by softly incorporating scene- and view-adaptive generative priors. Extensive experiments on real-world large-scale scenes demonstrate the superiority and broad applicability of our approach in handling unstructured imagery and boosting high-fidelity Gaussian splatting. Please refer to the supplementary video for better visual demonstrations.

</details>

#### 2026-09-02 - LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting

**Authors:** Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu
**Links:** [abs](https://arxiv.org/abs/2609.02543) - [pdf](https://arxiv.org/pdf/2609.02543)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, inverse rendering, relighting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：LightBridge: Feed-Forward Generative Relighting for 3D Gaussian Splatting
- 作者：Hezhi Cao, Panhao Cheng, huangsheng du, Qibiao Li, Youcheng Cai, Ligang Liu
- 出版日期：2026-09-02T12:58:24Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.02543

### 一句话总结
LightBridge 提出一种前馈式生成框架，无需逐场景优化即可对完整 3DGS 资产实现单次前向的可控重打光。

### 研究问题
如何在保持 3D Gaussian Splatting (3DGS) 高质量实时渲染优势的同时，实现高效且可控的重打光，避免传统逆向渲染方法的低效和生成式方法所需的逐场景优化阶段。

### 核心思路/方法
1. 构建大规模多光照重打光数据集（Multi-Illumination Relighting Dataset），包含同场景的成对源光照与目标光照观测，以支持前馈训练。
2. 提出 Latent Bridge Relighting Diffusion 模型，将重打光建模为潜空间中的源到目标传输（transport），实现无需迭代扩散采样的一步式 2D 视觉 token 提取。
3. 设计 Gaussian Propagation Transformer，利用点变换器结合稀疏图像到点自注意力与点到图像交叉注意力，将视觉线索高效传播到完整 3DGS，避免对所有图像和高斯 token 进行全注意力计算。

### 主要贡献
- 提出首个面向完整 3DGS 资产的单次前馈可控重打光生成框架。
- 基于数据集的构造和潜空间传输扩散设计，实现无需逐场景优化的一步式重打光预测。
- 提出高斯传播变换器，通过稀疏注意力机制高效地将 2D 线索传播到 3DGS。
- 实验验证了该设计在重打光质量和单次前向预测效率上的竞争力，并将公开代码和数据集。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作针对 3DGS 重打光这一活跃研究方向提出了无需逐场景优化的前馈式解决方案，在方法设计和效率上具有显著创新性，对生成式神经渲染和场景编辑领域有较强参考价值；且代码与数据集将公开，便于复现和后续研究。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) achieves high-quality, real-time novel view synthesis, but the resulting assets have baked-in illumination and cannot be easily relit. Inverse rendering methods optimize simplified reflectance and illumination models for each scene, limiting efficiency and relighting quality. Recent generative approaches leverage large diffusion models for realistic lighting edits, but applying them to 3DGS typically requires an additional per-scene optimization stage to bake the edited appearance into the representation. We present LightBridge, a feed-forward generative framework for controllable relighting of complete 3DGS assets in a single pass. To enable feed-forward training, we construct a large-scale Multi-Illumination Relighting Dataset with paired source and target observations of the same scenes. Latent Bridge Relighting Diffusion models relighting as source-to-target transport in latent space, enabling one-step extraction of 2D visual tokens without iterative diffusion sampling. A Gaussian Propagation Transformer uses a point transformer with sparse image-to-point self-attention followed by point-to-image cross-attention to efficiently propagate these cues across the complete 3DGS, while avoiding full attention over all image and Gaussian tokens. Experiments validate these designs, demonstrating competitive relighting quality and efficient single-pass prediction of complete relit 3DGS assets without scene-specific optimization. The code and dataset will be made publicly available upon acceptance.

</details>

#### 2026-09-01 - DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting

**Authors:** Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang
**Links:** [abs](https://arxiv.org/abs/2609.01516) - [pdf](https://arxiv.org/pdf/2609.01516)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** 3D reconstruction, Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：DualDiff3D: Dual Structure-Appearance Diffusion Priors for Reliability-Enhanced 3D Gaussian Splatting
- 作者：Qian Wang, Yu Wang, Weiqi Li, Xinhua Cheng, Xiandong Meng, Ronggang Wang, Jian Zhang
- 出版日期：2026-09-01T16:45:53Z
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.01516（摘要页）/ https://arxiv.org/pdf/2609.01516（PDF）

### 一句话总结
本文提出DualDiff3D，通过引入结构-外观双扩散先验及可靠性增强的渲染-细化-优化循环，改善少视图条件下3D高斯泼溅的重建质量和新视角渲染效果。

### 研究问题
在输入视图数量有限的情况下，3D高斯泼溅（3DGS）重建质量差、渲染的新视角存在伪影。现有利用扩散先验的方法通常将渲染视图与参考视图沿额外维度拼接输入单一网络，忽略了不同视图间“外观应相似但结构因视角变化而不同”的固有特性，导致两类属性相互冲突并产生模糊。

### 核心思路/方法
- 提出**DualDiff**管线：利用双扩散先验，其中一个扩散分支专注从低质量新视角中提取结构信息，另一分支确保与参考视图的外观一致性；引入**结构-外观注意力（SAA）模块**实现参考引导，细化从有缺陷的3D表示中渲染出的低质量新视角。
- 提出**DualDiff3D**重建框架：集成**可靠性增强的渲染-细化-优化（RRO）循环**，逐步且鲁棒地将细化后的新视角融入优化过程，从而获得更精确的3DGS模型。

### 主要贡献
- 提出DualDiff双扩散先验管线及SAA模块，分别处理结构信息与外观一致性，避免单一网络中的属性冲突。
- 提出DualDiff3D框架及RRO循环，稳健集成细化新视角以提升3DGS重建精度。
- 实验表明，在仅推理（inference-only）设置下即取得优于现有方法的效果，且通过训练可进一步提升性能。
- 开源代码与预训练权重。

### 局限性
摘要未提供足够信息，无法获取关于方法在极端少视图、复杂场景、计算开销或失败案例等方面的局限性。

### 阅读优先级
**高**。理由：该工作针对3DGS在少视图下的关键缺陷提出双扩散先验与注意力机制，创新性强；且在推理-only设置下即优于现有方法，训练后进一步提升，具备实际应用潜力；代码与权重已开源，便于复现和后续研究。该方向属于3D重建与渲染的热点领域，适合相关研究者优先精读。

</details>

<details>
<summary>Abstract</summary>

While 3D Gaussian Splatting (3DGS) has revolutionized 3D reconstruction and novel-view synthesis, scenarios with limited input views often lead to poor reconstruction quality and artifacts in rendered novel views. Recent efforts attempt to utilize powerful diffusion priors, yet they typically process rendered and reference views concatenated along an additional dimension in a single network. These methods overlook an inherent nature that different views should maintain appearance similarity but differ in structure due to view shifts, leading to blur caused by conflicts between the two properties. In this paper, we propose DualDiff, a novel pipeline that leverages dual diffusion priors with a Structure-Appearance Attention (SAA) module to introduce reference guidance for refining low-quality novel views rendered from flawed 3D representations. Specifically, we retain one diffusion branch to focus on extracting structural information from the low-quality novel views, while introducing another branch to ensure appearance consistency with reference views. Furthermore, we present a 3D reconstruction framework named DualDiff3D, which integrates a reliability-enhanced Render-Refine-Optimize (RRO) loop to progressively and robustly incorporate the refined novel views, yielding more accurate 3DGS. Extensive experiments demonstrate that our approach outperforms state-of-the-art methods even in the inference-only setting, with further performance gains achievable through training. Our code and pre-trained weights are available at https://github.com/Akaneqwq/DualDiff3D.

</details>

#### 2026-09-01 - MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering

**Authors:** Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu
**Links:** [abs](https://arxiv.org/abs/2609.01306) - [pdf](https://arxiv.org/pdf/2609.01306)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** neural rendering, rendering

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MeshSplatBench: A Unified Benchmark for Triangle-Based Neural Rendering
- 作者：Kaixuan Zhang, Minxian Li, Mingwu Ren, Xiatian Zhu
- 出版日期：2026-09-01
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.01306

### 一句话总结
MeshSplatBench 是一个统一的基准测试，系统评估基于三角形的神经渲染方法从原生优化到游戏引擎部署全流程的可部署性与保真度。

### 研究问题
现有基于三角形的神经渲染方法几乎仅在定制研究渲染器中评估，其在生产级引擎中的实际可部署性不明确。因此，本文旨在填补这一空白，统一度量该类方法在完整管线（原生优化到游戏引擎）中的真实表现。

### 核心思路/方法
MeshSplatBench 提出并实施三部分方法：1) 建立标准化评估协议，同时保留各方法的原生优化语义，可在0.8% PSNR偏差内复现已发表结果；2) 引入分层Unity部署协议，包含三个渲染层级（原生CUDA渲染器、方法专用的引擎着色器、标准不透明网格管线），以隔离引擎适配与表示简化分别造成的保真度损失；3) 对重建表面进行拓扑审计，检查非流形结构、碎片化组件和边界伪影等影响资产可用性的问题。

### 主要贡献
- 首次提出统一基准 MeshSplatBench，系统化覆盖三角形神经渲染从原生优化到游戏引擎部署的完整管线。
- 建立标准化评估协议，可高保真复现（0.8% PSNR偏差内）现有方法的已发表结果。
- 设计分层Unity部署协议，用于分离不同来源的保真度损失（引擎适配 vs. 表示简化）。
- 通过拓扑审计揭示：仅依赖显式连接与共享索引不足以确保生产级资产质量，仍普遍存在非流形结构、碎片化组件及边界伪影。

### 局限性
摘要未提供足够信息（例如：具体测试方法数量、基准的数据集范围、计算资源开销、对实时性的量化评估等均未在摘要中说明）。

### 阅读优先级
**中**。理由：该工作为领域提供了缺失的统一基准和跨引擎部署评估协议，对需要将神经渲染用于实际图形管线的研究者具有参考价值；但摘要未展示具体的对比结果、定量发现或创新性评估指标，故非同领域内的高优先阅读项。对专注游戏引擎部署或三角形网格渲染的读者，可适当上调优先级。

</details>

<details>
<summary>Abstract</summary>

Triangle-based neural rendering bridges neural scene representations and conventional graphics pipelines by optimizing explicit geometric primitives compatible with standard rasterization hardware. However, existing approaches are evaluated almost exclusively within custom research renderers, obscuring their practical deployability in production engines. To bridge this gap, we introduce \textbf{MeshSplatBench}, a unified benchmark that systematically investigates triangle-based neural rendering across the complete pipeline from native optimization to game-engine deployment. MeshSplatBench establishes a standardized evaluation protocol while preserving each method's native optimization semantics, reproducing published results within $0.8\%$ PSNR deviation. Furthermore, we introduce a hierarchical Unity deployment protocol spanning three rendering tiers: native CUDA renderers, method-specific dedicated engine shaders, and standard opaque mesh pipelines, isolating the exact fidelity losses caused by engine adaptation \textit{vs.} representation reduction. Finally, we conduct a topological audit of reconstructed surfaces, demonstrating that explicit connectivity and shared indexing alone are insufficient to guarantee production-ready assets due to prevalent non-manifold structures, fragmented components, and boundary artifacts. Overall, MeshSplatBench demonstrates that rasterizability is merely a primitive-level attribute, whereas graphics readiness requires jthe holistic alignment of representation, topology, and engine compatibility. Source code will be released.

</details>

#### 2026-09-01 - Inverse Rendering for Modeling with Line Primitives

**Authors:** Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel
**Links:** [abs](https://arxiv.org/abs/2609.00625) - [pdf](https://arxiv.org/pdf/2609.00625)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** radiance field, inverse rendering, rendering, radiance, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Inverse Rendering for Modeling with Line Primitives
- 作者：Kenji Tojo, Ariel Shamir, Nobuyuki Umetani, Bernd Bickel
- 出版日期：2026-09-01
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2609.00625

### 一句话总结
提出一种基于显式线段图元的逆向渲染方法，在保持与标准图形管线兼容的同时，实现具有模糊、各向异性结构（如毛发、纤维、纺织品）的物体重建与高质量渲染。

### 研究问题
如何利用显式的低维图元（线段）而非体素化图元（如3D高斯），从多视角图像中重建具有半透明、模糊结构外观的真实物体，同时兼容标准图形渲染、反射建模和物理模拟流程。

### 核心思路/方法
- 使用显式线段作为重建图元，并在亚像素网格上进行光栅化以实现抗锯齿，从而再现半透明外观。
- 提出一种针对线段的随机可微光栅化器，能够为顶点位置、属性和离散连通性提供有效梯度，便于优化大量线段图元以匹配目标图像。

### 主要贡献
- 首次将显式线段用于逆向渲染重建模糊几何，避免了体表表示的不兼容问题。
- 设计了针对线段的随机可微光栅化器，解决了在线段图元上优化众多参数的难题。
- 实验证明该方法在捕捉模糊边界上优于基于表面的方法，且质量与体素表示相当，同时完全依赖显式几何。
- 输出表示可无缝集成至标准图形管线，支持跨平台渲染、多种着色模型和物理模拟。

### 局限性
摘要未提供足够信息（包括对线数规模、内存/计算开销、在极端复杂场景下的表现、算法鲁棒性、实时性能指标、以及与特定体素方法定量对比的详细实验设置均未在摘要中说明）。

### 阅读优先级
**中**。理由：该方法在图形学与逆向渲染领域具有创新性，解决了显式几何与体积质量的权衡问题，但论文涉及的表示与优化技术相对专门，若研究兴趣不在模糊几何建模或可微渲染方向，则参考价值有限。

</details>

<details>
<summary>Abstract</summary>

Faithfully capturing diverse real-world objects with fuzzy, anisotropic structures, such as hair, fur, fibers, and textiles, for efficient real-time visualization remains challenging. Recent radiance field reconstruction methods capture these structures from multi-view images using translucent volumetric primitives such as 3D Gaussians rather than opaque low-dimensional primitives (e.g., triangles, line segments, and polylines), thereby limiting compatibility with standard depth-tested rasterization, reflection modeling, and physical simulation. We present an inverse rendering method for reconstructing fuzzy geometry using explicit line segments, which are rasterized on a subpixel grid for anti-aliasing to reproduce a semi-transparent appearance. While straightforward to render, optimizing numerous line primitives to match target images poses a significant challenge. We address this by introducing a stochastic differentiable rasterizer for line segments that produces informative gradients with respect to vertex positions, attributes, and discrete connectivity. Experiments on synthetic and real-world datasets show that our method outperforms surface-based approaches in capturing fuzzy boundaries and achieves quality comparable to volumetric representations while relying entirely on explicit geometry. The resulting representation integrates seamlessly with standard graphics pipelines, enabling cross-platform rendering, various shading models, and physical simulation.

</details>

### 2026-08

#### 2026-08-31 - VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement

**Authors:** Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang
**Links:** [abs](https://arxiv.org/abs/2608.30870) - [pdf](https://arxiv.org/pdf/2608.30870)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, splatting, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：VCAR: Training-Free 3DGS Segmentation via View Completeness and Axis-Aware Boundary Refinement
- 作者：Kun Cao, Di Wang, Haibin Zhu, Haozhi Huang, Xu Wang, Zheng Shi, Guanghua Yang
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30870

### 一句话总结
VCAR 提出一种无需训练的 3D 高斯泼溅（3DGS）分割方法，通过可见性加权多视角投票、球面螺旋采样补全视角以及轴感知边界细化，实现粗到精的精确分割，并显著降低训练开销。

### 研究问题
现有 3DGS 语义分割方法依赖特征蒸馏，导致每个场景需要大量训练开销且分割边界模糊。本文指出边界伪影部分源于视点覆盖不足和各向异性高斯原语的边界溢出，旨在无需训练的情况下提升分割精度和效率。

### 核心思路/方法
VCAR 采用粗到精的两阶段策略：
- **粗阶段**：基于可见性加权的多视角投票方案，快速定位目标物体。
- **细阶段**：根据粗分割结果构建以物体为中心的球体，通过球面螺旋采样（SSS）生成补充视点，在增强视点上进行多视角投票，精确细化目标边界并抑制无关 3D 高斯。
- **轴感知边界细化（ABR）**：将投影后的二维协方差分解为逐轴贡献，识别导致边界泄漏的主轴，仅沿该轴进行定向各向异性压缩，缓解各向异性原语带来的伪影。

### 主要贡献
- 提出无需训练的训练-free 粗到细 3DGS 分割框架，避免逐场景训练开销。
- 设计可见性加权多视角投票和球面螺旋采样以补全视点、精确细化边界。
- 引入轴感知边界细化机制，针对各向异性高斯原语的边界泄漏进行定向修正。
- 在 NVOS 和 LERF 数据集上达到最先进的分割精度和效率（实验细节以论文原文为准）。

### 局限性
摘要未提供足够信息。未提及方法在特定复杂场景（如遮挡严重、物体重叠或大规模场景）下的表现，也未说明内存占用、推理耗时等具体量化指标。

### 阅读优先级
**高**。理由：该工作针对 3DGS 分割中训练开销大和边界模糊的关键痛点，提出无需训练的高效方案，兼具方法创新性与实用价值，且实验验证了其有效性，对关注神经场景表示与渲染的研究者有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

Semantic segmentation in 3D Gaussian Splatting (3DGS) is crucial for advancing 3D scene understanding. Existing methods predominantly rely on feature distillation, which incurs substantial per-scene training overhead and often yields blurred segmentation boundaries. We identify that these boundary artifacts are driven in part by insufficient viewpoint coverage and boundary overflow of anisotropic Gaussian primitives. To address these challenges, we propose VCAR, a training-free coarse-to-fine segmentation strategy based on View Completeness and Axis-aware Boundary Refinement. In the coarse stage, a visibility-based weighted multi-view voting scheme rapidly localizes the target. In the fine stage, an object-centric sphere derived from the coarse result generates supplementary viewpoints via Spherical Spiral Sampling (SSS), allowing multi-view voting on the augmented views to precisely refine object boundaries and suppress irrelevant 3D Gaussians. Moreover, we introduce Axis-aware Boundary Refinement (ABR) to mitigate artifacts from anisotropic primitives. By decomposing the projected 2D covariance into per-axis contributions, ABR identifies the dominant axis responsible for boundary leakage and applies targeted anisotropic compression exclusively along that axis. Extensive experiments on NVOS and LERF demonstrate that VCAR achieves state-of-the-art segmentation accuracy and efficiency without training. Our code is available at https://github.com/DDKK0526/VCAR.

</details>

#### 2026-08-31 - ObjectSplat: Improving Mesh Fidelity and Interactivity for 3D Scenes via Object-Level Mesh Splatting

**Authors:** Minhas Kamal, Hiranya Garbha Kumar, Mahedi Kamal, Balakrishnan Prabhakaran
**Links:** [abs](https://arxiv.org/abs/2608.30423) - [pdf](https://arxiv.org/pdf/2608.30423)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ObjectSplat: Improving Mesh Fidelity and Interactivity for 3D Scenes via Object-Level Mesh Splatting
- 作者：Minhas Kamal, Hiranya Garbha Kumar, Mahedi Kamal, Balakrishnan Prabhakaran
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30423

### 一句话总结
本文提出一种“先分解再重建”的物体级网格溅射方法，将场景中的实例与背景分别重建后合成，以提升网格保真度、新视角合成质量，并支持物体级编辑和交互。

### 研究问题
现有基于溅射（splatting）的3D场景重建方法将整个场景表示为单一整体场，缺乏物体级结构，导致下游编辑和交互不可行；同时，输入扫描中未被直接观察到的区域会被周围纹理污染且无法修正，限制了网格保真度和新视角合成质量。

### 核心思路/方法
采用“分解-再重建”流程：
1. 从每一帧中分割出各个实例（物体）；
2. 将剩余部分视为背景，并进行修复（inpainting）；
3. 使用网格溅射（mesh splatting）独立重建每个实例和背景；
4. 将重建结果组合成单一场景，实现物体级可修改性和交互性。

### 主要贡献
- 提出物体级网格溅射方法，显著提升网格保真度（F-score提升超过5%）；
- 改善新视角合成质量；
- 支持物体级（逐对象）的修改性和交互性；
- 代码将公开。

### 局限性
摘要中未提供关于方法失败场景、性能瓶颈、计算成本或对真实复杂场景的鲁棒性等局限性的具体信息，因此局限性部分摘要未提供足够信息。

### 阅读优先级
**中**  
理由：该方法针对3D场景重建的物体级结构和交互性提出明确改进，且有量化增益（F-score提升>5%），属于领域内的实际工程改进。但摘要未提供具体技术细节（如分割方法、修复策略、基准对比等），且尚未提及实验规模与下游应用验证，故适合对该方向感兴趣的读者快速了解，而非必读的高优先级论文。

</details>

<details>
<summary>Abstract</summary>

Splatting-based algorithms reconstruct photorealistic, real-time-renderable, and mesh-exportable 3D scenes from regular images, but they represent a scene as a single monolithic field. Therefore, the reconstruction has no object-level structure, leaving it infeasible for downstream editing or interaction. Moreover, regions that are never directly observed in the input scans are contaminated by the surrounding texture and left uncorrected, capping both mesh fidelity and novel-view synthesis. We propose a decompose-before-reconstruct approach: we segment the instances out of every frame, consider the remaining as background and inpaint it, reconstruct each instance and the background independently with mesh splatting, and compose them into a single scene. Our method significantly improves mesh fidelity (over a 5\% gain in F-score) and novel-view synthesis, while supporting object-wise modifiability and interactivity. The code will be made publicly available.

</details>

#### 2026-08-31 - CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels

**Authors:** Jirong Li, Satoshi Ikehata, Shuhei Kurita, Ikuro Sato
**Links:** [abs](https://arxiv.org/abs/2608.30342) - [pdf](https://arxiv.org/pdf/2608.30342)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, novel view synthesis, view synthesis, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels
- 作者：Jirong Li, Satoshi Ikehata, Shuhei Kurita, Ikuro Sato
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30342

### 一句话总结
本文提出新任务TIVG（文本指令视角定位）及方法CapFrame，通过将语言指令转换为几何伪标签，在3D高斯场景中优化相机位姿，使渲染画面与文本描述对齐。

### 研究问题
现有语言引导的3D场景方法多聚焦于物体级定位（确定“看什么”），但难以控制单帧画面中的“如何看”（如主体朝向或构图布局）。本文研究如何在3D高斯场景中根据文本指令确定6自由度相机位姿，使渲染出的帧与指令语义一致。

### 核心思路/方法
CapFrame采用“检索-翻译-精炼”（Retrieve-Translate-Refine）流水线：
1. **检索**：从3D高斯场景中检索相关视图，并通过多模态大语言模型（MLLMs）的问题评估（Question-Evaluation）过程对视图排序。
2. **翻译**：将文本指令转换为朝向（orientation）和布局（layout）两类几何伪标签。
3. **精炼**：利用布局损失和朝向损失，在3DGS中进行可微分的相机位姿优化。整体框架为部分可微分。

### 主要贡献
1. 提出新任务TIVG，弥补现有方法在语言引导视角控制方面的空白。
2. 提出CapFrame框架，实现从语言到几何伪标签的转换及位姿优化。
3. 在38个真实场景、135条指令上进行实验，相比启发式视角搜索和改造的轨迹生成基线，CapFrame生成的视角与文本更对齐，经由VLM指标、MLLM评估和用户研究验证。

### 局限性
摘要未提供足够信息（包括失败案例、对复杂指令的鲁棒性、计算开销、对3DGS重建质量的依赖等均未提及）。

### 阅读优先级
**高**。理由：该工作提出新的任务定义（TIVG），且方法新颖（利用几何伪标签连接语言与相机位姿优化），实验规模较大并包含多种评估方式（自动指标+人工评估），对文本驱动的3D场景交互与视图合成方向有明显推进意义。

</details>

<details>
<summary>Abstract</summary>

3D Gaussian Splatting (3DGS) enables photorealistic real-time novel view synthesis, yet placing a virtual camera to capture a desired frame remains largely manual. Existing language-guided approaches in 3D scenes mainly focus on object-centric grounding, determining what to observe but rarely controlling how it should appear in a single frame, such as subject orientation or frame layout. To address this limitation, we introduce a new task, Text-Instructed Viewpoint Grounding (TIVG), which aims to identify a 6-DoF camera pose in a 3D Gaussian scene whose rendered frame aligns with a text instruction. To solve this task, we propose CapFrame, a partially differentiable framework that converts language into geometric pseudo labels for camera pose optimization. CapFrame follows a Retrieve-Translate-Refine pipeline: it retrieves relevant views and ranks them through a Question-Evaluation process with MLLMs, translates the instruction into orientation and layout pseudo labels, and refines the camera pose via differentiable optimization with layout and orientation losses in 3DGS. Experiments on 38 real-world scenes with 135 instructions indicate that CapFrame produces viewpoints better aligned with texts than heuristic viewpoint search and adapted trajectory generation baselines, validated by VLM metrics, MLLM judges, and user studies. Code is available at: https://github.com/jirongli/CapFrame

</details>

#### 2026-08-31 - ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation

**Authors:** Jiahao Wu, Jie Liang, Die Hu, Jiayu Yang, Kaiqiang Xiong, Xiang Li, Xiaoyun Zheng, Chao Wang, Ronggang Wang
**Links:** [abs](https://arxiv.org/abs/2608.30184) - [pdf](https://arxiv.org/pdf/2608.30184)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** video reconstruction, Gaussian Splatting, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：ATGS: Anchored Temporal Gaussian Splatting for Long Volumetric Video Representation
- 作者：Jiahao Wu, Jie Liang, Die Hu, Jiayu Yang, Kaiqiang Xiong, Xiang Li, Xiaoyun Zheng, Chao Wang, Ronggang Wang
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30184

### 一句话总结
本文提出一种基于锚定时间高斯溅射（ATGS）的框架，通过时间条件锚点与多级特征设计，提升长序列体积视频重建的时空稳定性与视觉质量。

### 研究问题
现有体积视频重建方法在处理长序列和复杂运动时存在时间不稳定和视觉伪影问题，即如何实现对长度较长、动作复杂的动态场景进行高质量自由视角渲染。

### 核心思路/方法
- 关键洞察：用单个高斯基元显式跟踪长期复杂运动本质上是不可靠的，因此将高斯围绕时间条件锚点组织，以定位其空间和时间支持范围，降低长程运动复杂度。
- 时间窗口策略：仅激活与查询时间相关的锚点，提升可扩展性和时间连贯性。
- 多级锚点特征：使用紧凑的全局特征、局部空间特征和局部时间特征联合约束高斯生成，保障时空稳定性。

### 主要贡献
1. 提出ATGS框架，基于锚定时间高斯溅射实现长序列体积视频重建。
2. 引入时间条件锚点机制，降低长程运动跟踪的复杂性。
3. 设计时间窗口激活策略，兼顾可扩展性与时间一致性。
4. 提出紧凑的多级锚点特征编码，联合约束高斯生成，提高时空稳定性。
5. 实验表明在长序列复杂运动场景下，ATGS consistently优于已有方法。

### 局限性
摘要未提供足够信息。例如，摘要未提及计算开销、实时性、适用范围（如特定场景类型）或失败案例等限制性讨论。

### 阅读优先级
**中**。理由：该方法针对体积视频重建中长序列和复杂运动的痛点，提出了锚点+时间窗口的创新思路，具有一定学术价值；但摘要中未披露足够实验细节（如定量指标、对比基准范围等），难以评估其实际幅度提升，适合对动态场景渲染或高斯溅射方向感兴趣的读者阅读。

</details>

<details>
<summary>Abstract</summary>

Volumetric video enables immersive free viewpoint rendering of dynamic real world scenes, yet existing methods struggle with long sequences and complex motions, often leading to temporal instability and visual artifacts. To address these challenges, we propose \ourname, a Gaussian splatting based framework for volumetric video reconstruction. Our key insight is that explicitly tracking long term complex motion with individual Gaussian primitives is inherently unstable. Instead, we organize Gaussians around time conditioned anchors that localize their spatial and temporal support, thereby reducing long range motion complexity. We further introduce a temporal windowing strategy to activate only anchors relevant to the queried time, which improves scalability and temporal coherence. In addition, to ensure spatial and temporal stability, we design a compact set of multi level anchor features that encode global features, local spatial features, and local temporal features, jointly constraining Gaussian generation. Extensive experiments demonstrate that \ourname \ consistently outperforms prior methods on long sequence volumetric videos with complex motions. Project page: https://github.com/WuJH2001/ATGS.

</details>

#### 2026-08-31 - AI-enabled Low-Cost 3D Maize Ear Morphometry Platform at Breeding Scale

**Authors:** Therin Young, Elijah Rodriguez, Lisa Coffey, Talukder Zaki Jubery, Adarsh Krishnamurthy, Patrick Schnable, Baskar Ganapathysubramanian
**Links:** [abs](https://arxiv.org/abs/2608.30161) - [pdf](https://arxiv.org/pdf/2608.30161)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** NeRF, neural radiance field, radiance field, radiance

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：AI-enabled Low-Cost 3D Maize Ear Morphometry Platform at Breeding Scale（AI驱动的低成本玉米果穗三维形态测量平台，适用于育种规模）
- 作者：Therin Young, Elijah Rodriguez, Lisa Coffey, Talukder Zaki Jubery, Adarsh Krishnamurthy, Patrick Schnable, Baskar Ganapathysubramanian
- 出版日期：2026-08-31
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30161

### 一句话总结
本文提出并验证了一种基于消费级相机和神经辐射场（NeRF）的低成本玉米果穗三维重建与形态测量流水线，可在育种规模下高效获取果穗长度、体积等几何指标。

### 研究问题
现有高通量表型分析平台因成本高、劳动密集且依赖专用硬件而受限，本文旨在开发一种低成本、易操作且可扩展的三维玉米果穗形态测量方案。

### 核心思路/方法
- 使用消费级数码单反相机在电动转盘和均匀LED照明下拍摄20秒视频，重建果穗密闭三维网格。
- 通过多种子COLMAP流程估计相机位姿，初始化NeRF进行三维重建。
- 利用视频中可见的已知直径圆柱支架，实现自动公制尺寸缩放和几何质量控制。
- 对300个来自玉米自交系多样群体的果穗进行验证，其中250个通过自动化处理和质量控制。
- 将骨架长度与游标卡尺测量值、凸包体积与水置换体积进行比较，评估测量准确性。

### 主要贡献
- 开发并验证了低成本三维果穗表型流水线，硬件成本约607美元。
- 操作时间从约5分钟降至每穗1分钟，下游处理全自动运行。
- 在250个果穗上，骨架长度与卡尺测量高度一致（R²=0.964，RMSE=4.68 mm）；15穗子集的凸包体积与水置换体积一致（R²=0.982，RMSE=5.26 mL）。
- 分析了长度残差与弯曲度的关系，指出残差源于测量定义差异（卡尺测弦长，骨架长度测测地弧长）。
- 为育种规模的三维果穗表型分析提供了可行基础。

### 局限性
摘要未提供足够信息，如：对未通过质量控制（约16.7%）果穗的失败原因分析、平台在不同环境或品种间的泛化性、以及与其他高吞吐量平台的直接成本效益对比均未提及。

### 阅读优先级
**中**。该研究在低成本3D表型方向具有实用价值，且验证结果扎实，适合关注作物表型、农业AI或NeRF应用的读者。但若您不从事相关领域，其创新性主要在于工程集成，而非新的算法或理论突破，优先级相应降低。

</details>

<details>
<summary>Abstract</summary>

Maize ear geometry (length, width, curvature, and volume) is closely tied to yield and grain-filling outcomes, but existing high-throughput phenotyping pipelines remain constrained by the cost, labor, and specialized hardware they require. We developed and validated a low-cost pipeline that reconstructs a watertight 3-D mesh of a maize ear from a single 20-second video captured with a consumer-grade DSLR on a motorized turntable under uniform LED illumination. Camera poses from a multi-seed COLMAP procedure initialize a Neural Radiance Field (NeRF), and a cylindrical holder of known diameter, visible in every frame, provides automatic metric scaling with downstream geometric quality control. Applied to 300 ears spanning a diverse maize inbred panel, 250 (83.3%) passed automated processing and quality control. Skeleton length agreed with manual caliper measurements across all 250 ears (R^2 = 0.964, RMSE = 4.68 mm), and convex-hull volume agreed with water-displacement volume on a 15-ear subset spanning the full size range (R^2 = 0.982, RMSE = 5.26 mL). Residual length error grew with ear curvature, whereas bounding-box height, which records the same straight-line chord as calipers, showed no such trend; the discrepancy therefore originates in the measurement definition, since calipers record the chord while skeleton length traces the geodesic arc. The capture hardware costs approximately 607 USD, and operator involvement fell from roughly five minutes to one minute per ear, with all downstream processing running unattended. The platform provides a foundation for breeding-scale 3-D ear phenotyping.

</details>

#### 2026-08-30 - When 3D Gaussian Splatting Recovers Real Surfaces

**Authors:** Songhe Wang, David Johnathan Miller
**Links:** [abs](https://arxiv.org/abs/2608.30054) - [pdf](https://arxiv.org/pdf/2608.30054)
**Primary category:** Neural Scene Representations & Rendering
**Secondary categories:** None
**Matched keywords:** Gaussian Splatting, 3D Gaussian Splatting, 3DGS, rendering, splatting

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：When 3D Gaussian Splatting Recovers Real Surfaces
- 作者：Songhe Wang, David Johnathan Miller
- 出版日期：2026-08-30
- 分类：Neural Scene Representations & Rendering
- 链接：https://arxiv.org/abs/2608.30054

### 一句话总结
本文通过数学框架证明3D高斯溅射（3DGS）在角向容量受限时偏好表面一致的几何重建，而角向容量过高则可能导致错误的不透明广告牌式几何解。

### 研究问题
3D高斯溅射在什么条件下能够恢复真实场景表面，而非仅仅过拟合视角相关的外观？具体而言，几何错位与角向容量如何影响表面一致解与错误几何解之间的可辨识性。

### 核心思路/方法
作者建立了一种基于“首次命中”（first-hit）渲染抽象的数学框架，该框架将几何与外观清晰分离。利用视差效应证明几何错位会将空间纹理强制转化为高频角向信号。在此基础上，推导出一个严格的可辨识窗口：
- 若角向容量有界，表面一致解在数学上更受偏好；
- 若角向容量无限制，相同图像可被不正确的、不透明广告牌几何完美解释。

### 主要贡献
- 提出一个将几何与外观分离的首次命中渲染数学框架；
- 证明几何错位通过视差将空间纹理转化为高频角向信号的机制；
- 建立表面一致解与广告牌几何解之间的严格可辨识条件；
- 通过合成压力测试验证预测：广告牌失败恰在高角向容量处出现；
- 在真实世界数据集中表明标准采集协议下重建在SH高阶时仍保持表面一致，与理论预测吻合。

### 局限性
摘要仅提及合成实验确认了广告牌失败出现在高角向容量处，但未提供实验数据集的具体规模、评价指标、失败临界点的定量数值，也未讨论框架假设（如首次命中抽象）在真实复杂场景（遮挡、透明物体、反射表面等）中的适用边界。摘要未提供足够信息。

### 阅读优先级
**中**。理由：该论文在理论层面为3DGS的几何可辨识性提供了清晰的数学解释，对理解3DGS的失败模式有价值；但由于摘要未提供充分的定量结果、方法实现细节和广泛的实验对比，其实际工程指导意义需阅读全文后评估。适合关注3DGS理论分析的读者阅读。

</details>

<details>
<summary>Abstract</summary>

When does 3D Gaussian Splatting (3DGS) recover the true scene surface rather than just overfitting view-dependent appearance? We answer this by developing a mathematical framework based on a first-hit rendering abstraction that cleanly isolates geometry from appearance. We prove that geometric misalignment forcefully converts spatial textures into high-frequency angular signals via parallax. This establishes a strict identifiability window: if angular capacity is bounded, surface-consistent solutions are mathematically preferred; if unrestricted, the same images can be perfectly explained by an incorrect, opaque billboard geometry. Experiments on synthetic stress tests confirm this prediction, showing billboard failures emerge precisely at high angular capacities. Conversely, in the real-world datasets we evaluate under standard capture protocols, reconstructions remain surface-consistent even at high SH degrees, which is consistent with the prediction that rich spatial texture can push billboard solutions outside the tested angular-capacity range.

</details>

## Embodied / Robotics / AR Applications

### 2026-09

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

#### 2026-09-02 - From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images

**Authors:** Annalisa Gallina, Marco Fiorucci, Marco Brigo, Federica Battisti, Lamberto Ballan
**Links:** [abs](https://arxiv.org/abs/2609.02640) - [pdf](https://arxiv.org/pdf/2609.02640)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：From Detection to Localization: A Unified Forensics Framework for Fully Synthetic and Tampered Images
- 作者：Annalisa Gallina, Marco Fiorucci, Marco Brigo, Federica Battisti, Lamberto Ballan
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02640

### 一句话总结
本文提出一个统一的多分类图像取证框架，能同时区分真实、全生成和篡改图像，并通过分割分支实现篡改区域的像素级定位。

### 研究问题
现有图像篡改检测方法通常将问题简化为二分类（真实 vs. 生成），无法区分和定位不同类型的篡改操作，限制了取证能力的细粒度。本文旨在解决这一局限，实现更全面的图像伪造识别与定位。

### 核心思路/方法
- 在已有检测器基础上进行扩展，引入统一的多分类框架（真实 vs. 全生成 vs. 篡改三类）。
- 除图像真实性分类外，框架中加入分割分支，以支持篡改区域的像素级定位。
- 该框架将检测与定位任务整合于同一模型，提升取证效率。

### 主要贡献
- 提出了一个统一的多分类取证框架，突破了传统二分类的局限。
- 结合分类与分割两个任务，实现篡改区域的像素级定位。
- 在分类准确率和定位IoU指标上优于所选的近期基准方法。
- 公开了代码实现。

### 局限性
摘要未提供足够信息：摘要未提及方法的失败案例、计算开销、对特定伪造类型的鲁棒性、数据集构成或实验范围的局限。

### 阅读优先级
**中**。理由：该工作面向多媒体取证中的实用需求，提出统一分类与定位的方案，方法较完整且有基准对比，但属于对现有检测器的改进型扩展，创新幅度有限；若研究领域相近（图像取证、伪造检测/定位），可重点阅读框架设计与分割分支的整合方式。

</details>

<details>
<summary>Abstract</summary>

The rapid advancement of generative models has significantly worsened the problem of manipulated image detection, as these methods are capable of producing highly realistic forgeries, reinforcing the importance of multimedia forensics. Conventional approaches typically frame image manipulation detection as a binary classification task (real vs. generated), which limits the capability to distinguish and localize different forms of manipulation. To address these constraints, this work extends an existing detector by introducing a unified multiclass framework (real vs. fully generated vs. tampered). In addition to classifying image authenticity, the framework incorporates a segmentation branch to enable pixel-level localization of tampered regions. The proposed approach outperforms selected recent benchmarks, offering an efficient solution with improved classification accuracy and higher IoU scores for the localization task. Find the code at https://github.com/anngal01/From-Detection-to-Localization-A-Unified-Forensics-Framework-for-Fully-Synthetic-and-Tampered-Images.

</details>

#### 2026-09-02 - Spatially Aware World Action Model via Geometric Latent Diffusion

**Authors:** Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid
**Links:** [abs](https://arxiv.org/abs/2609.02531) - [pdf](https://arxiv.org/pdf/2609.02531)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** depth prediction, world model, world modeling

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Spatially Aware World Action Model via Geometric Latent Diffusion
- 作者：Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02531

### 一句话总结
本文提出SA-WAM，在预训练视频扩散模型中同时引入深度预测与动作预测，使世界动作模型具备3D空间感知能力，并在仿真与真实机器人基准上取得领先结果。

### 研究问题
现有的世界动作模型（WAMs）仅基于RGB观测进行未来预测与动作生成，未利用3D几何信息，限制了其在机器人策略学习中的空间理解能力。如何在不破坏预训练先验的前提下，将几何信息融入统一的世界模型与动作预测框架是核心问题。

### 核心思路/方法
- 在单一扩散骨干网络中，将预训练视频模型扩展为联合预测动作、RGB和深度图的三模态输出。
- 使用非线性编码将无界深度信号映射到冻结VAE tokenizer所预期的有界输入域，从而无需针对3D进行微调即可复用现有tokenizer，保留预训练的视频与物理先验。

### 主要贡献
- 提出SA-WAM，首个在单扩散骨干中实现RGB、深度与动作联合预测的3D感知世界动作模型。
- 设计非线性深度编码方法，支持冻结tokenizer直接消费几何信息，避免3D专用微调带来的先验损失。
- 在RoboCasa和LIBERO-Plus基准上取得最先进结果，并提升未来状态预测质量。
- 在真实UR5机械臂评估中超越强基线，尤其在随机化环境中增益显著。
- 分析了世界模型预测质量与任务成功率之间的相关性，为WAM性能改进提供依据。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作首次将3D几何信息以轻量方式整合进预训练视频世界模型，同时兼顾动作预测与未来状态预测，在仿真和真实机器人上均验证了有效性；面向具身智能和机器人策略学习方向的研究者具有较高参考价值，且分析预测质量与成功率的关系对后续工作有启发意义。

</details>

<details>
<summary>Abstract</summary>

World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale video. This has made them a promising paradigm for robot policy learning, yet the prevailing models operate exclusively on RGB observations and do not leverage 3D information. To bridge this gap, we introduce a Spatially Aware World Action Model (SA-WAM), which repurposes a pretrained video model for joint action, RGB, and depth prediction, enabling 3D-aware world modeling and action prediction within a single diffusion backbone. We use a nonlinear encoding that maps the unbounded depth signal into the bounded input domain expected by the frozen VAE tokenizer. This allows us to reuse the tokenizer without 3D-specific fine-tuning, incorporating geometric information without sacrificing the pretrained priors. SA-WAM achieves state-of-the-art results on the RoboCasa and LIBERO-Plus benchmarks, while simultaneously improving future-state predictions. Furthermore, SA-WAM outperforms strong baselines in real-world evaluation using a UR5 robotic arm, with strong gains in randomized environments. We analyze the correlation between world model prediction quality and rollout success, providing insights into WAM performance and avenues for its improvement.

</details>

#### 2026-09-02 - MS-MEM: Multi-Skill Manipulation-Enhanced Mapping via Uncertainty- and Disturbance-Aware Action Selection

**Authors:** Yitian Shi, Jesper Mücke, Nils Dengler, Sicong Pan, Rania Rayyes, Maren Bennewitz
**Links:** [abs](https://arxiv.org/abs/2609.02493) - [pdf](https://arxiv.org/pdf/2609.02493)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, mapping, scene understanding

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：MS-MEM: Multi-Skill Manipulation-Enhanced Mapping via Uncertainty- and Disturbance-Aware Action Selection
- 作者：Yitian Shi, Jesper Mücke, Nils Dengler, Sicong Pan, Rania Rayyes, Maren Bennewitz
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02493

### 一句话总结
本文提出 MS-MEM，一种结合主动视点选择、物体推动与抓取的多技能操作增强建图框架，通过不确定性感知与扰动约束的统一动作选择，在提高建图精度的同时减少对场景的干扰。

### 研究问题
如何在狭窄、杂乱的空间（如货架）中，通过多技能操作与主动感知的协同，实现高效且低干扰的场景建图与物体定位，以应对严重遮挡和受限可达性的挑战。

### 核心思路/方法
1. 构建场景级度量-语义证据信念估计器，用于不确定性感知建图和环境表示。
2. 引入不确定性感知的抓取表示，基于一种全证据抓取估计器进行学习，同时建模抓取可行性与朝向不确定性。
3. 设计统一的动作选择管线，以共同的信息增益准则评估候选的感知与操作动作（视点选择、推动、抓取）。
4. 针对操作动作，提出附带扰动约束，抑制对场景信念中高置信区域的过度改变，在降低建图不确定性的同时控制场景扰动。

### 主要贡献
1. 提出 MS-MEM 框架，整合主动视点选择、物体推动与抓取三种能力，实现多技能协同的建图增强。
2. 提出基于全证据估计的不确定性感知抓取表示，同时估计抓取可行性与朝向不确定性。
3. 提出统一信息增益驱动的动作选择机制，并设计附带扰动约束，以实现建图精度与场景扰动之间的平衡。
4. 实验表明，相比单技能基准与忽略扰动的无约束基准，MS-MEM 可实现更高建图精度并显著降低场景扰动。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**中**。理由：该工作在机器人建图与操作交叉领域具有一定创新性，统一了多技能动作选择与不确定性/扰动建模；但由于摘要未给出具体实验设置、定量结果与部署细节，且面向较为特定的货架场景任务，适合对主动感知或多技能操作建图感兴趣的读者作为方法参考，而非常规通用视觉或建图研究者必须优先精读的工作。

</details>

<details>
<summary>Abstract</summary>

Accurate scene understanding in confined, cluttered spaces such as shelves is essential for service robots, as many everyday tasks require them to locate and retrieve objects reliably. Yet, it remains challenging due to severe occlusions, restricted accessibility, and the need to avoid excessive scene changes. In this paper, we propose Multi-Skill Manipulation-Enhanced Mapping (MS-MEM), an evidential framework for uncertainty-aware mapping that integrates active viewpoint selection, object pushing, and grasping. MS-MEM combines scene-level metric-semantic evidential belief estimators with an uncertainty-aware grasp representation. This representation is learned using a novel full-evidential grasp estimator that models both grasp affordance and orientation uncertainty. In our framework, candidate perception and manipulation actions are evaluated within a unified action selection pipeline using a common information gain criterion. For manipulation actions, we further introduce a collateral disturbance constraint (CDC) that discourages excessive changes to confident regions of the scene belief. This enables MS-MEM to select actions that effectively reduce map uncertainty while limiting collateral scene changes. Experimental results show that, compared with single-skill and unconstrained baselines that ignore scene disturbance, MS-MEM achieves higher mapping accuracy while substantially reducing scene disturbance, highlighting the synergistic effects of active viewpoint selection, push, and grasp actions.

</details>

#### 2026-09-02 - Evidence-Guided Detection, Localization and Explanation for Text-Centric Image Forensics

**Authors:** Peifeng Liu, Bin Li, Qingsong Zhang, Yangxin Yu, Leqing Chen, Xiaoye Qiu
**Links:** [abs](https://arxiv.org/abs/2609.02097) - [pdf](https://arxiv.org/pdf/2609.02097)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Evidence-Guided Detection, Localization and Explanation for Text-Centric Image Forensics（面向文本中心图像取证的证据引导检测、定位与解释）
- 作者：Peifeng Liu, Bin Li, Qingsong Zhang, Yangxin Yu, Leqing Chen, Xiaoye Qiu
- 出版日期：2026-09-02
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.02097

### 一句话总结
本文提出一个“检测器-定位器-推理器”三模块级联的证据引导系统，在 ACM Multimedia 2026 的 GenText-Forensics 挑战赛中以 0.638 分获得第二名，用于文本中心图像的取证检测、篡改区域定位与可解释性报告生成。

### 研究问题
针对 AIGC 技术使文本中心图像篡改变得日益普及所带来的新取证挑战——不仅需要判断图像真伪（检测），还需要空间锚定篡改位置（定位），并基于证据给出可解释的说明（解释）。

### 核心思路/方法
- 构建三级系统：图像级检测器提供全局真实性先验；专用定位器提取篡改区域作为空间定位证据；基于 MLLM 的推理器依据专家取证证据生成结构化取证报告。
- 模块间通过级联证据流连接：检测器门控后续定位与提示过程；定位器将篡改响应转换为定位框；推理器训练融合检测决策与定位证据生成最终报告。
- 关键技术手段：引入迭代困难感知挖掘提升定位质量；采用报告-掩码一致性后处理，使报告定位结果与预测掩码对齐。

### 主要贡献
- 提出证据引导的检测-定位-推理取证系统框架，实现从全局判断到局部定位再到自然语言解释的完整取证链路。
- 设计级联证据流机制，使三个模块协同工作，检测结果门控下游任务，定位证据支撑解释生成。
- 引入迭代困难感知挖掘与报告-掩码一致性后处理，分别提升定位精度与报告与空间证据的一致性。
- 在官方隐藏测试集上取得 0.638 综合分并获得挑战赛第二名，验证系统有效性，并开源代码。

### 局限性
摘要未提供足够信息。摘要仅提及系统性能数据和模块设计，未报告失败案例、计算开销、泛化能力评估、数据集分布特征或与基线方法的详细对比等信息。

### 阅读优先级
**中**。理由：该文是挑战赛解决方案的技术报告，系统设计思路清晰（级联证据引导），对从事图像取证、AIGC 检测或多模态可解释推理方向的研究者有一定参考价值；但由于是竞赛技术方案，本质更偏工程集成而非方法论重大突破，且摘要未给出实验细节和深入分析，泛化学术参考价值有限。

</details>

<details>
<summary>Abstract</summary>

The rapid progress of AIGC has made text-centric image manipulation increasingly accessible, creating new forensic challenges that require not only authenticity detection but also spatial grounding and evidence-based explanation. This paper presents our solution to the GenText-Forensics Challenge at ACM Multimedia 2026. We propose an evidence-guided detector-localizer-reasoner system, where an image-level detector provides a global authenticity prior, a dedicated localizer extracts tampered regions as spatial grounding evidence, and an MLLM-based reasoner generates structured forensic reports grounded in this expert forensic evidence. These modules are connected through a cascaded evidence flow: the detector gates the subsequent localization and prompting process, the localizer converts tamper responses into grounding boxes, and the reasoner is trained to synthesize the detector decision and localized evidence into the final report. As a key part of our method, we introduce iterative difficulty-aware mining to improve localization quality and apply report-mask consistency post-processing to align report grounding with predicted masks. On the official hidden test set, our system achieves a final score of 0.638 and ranks second in the challenge, validating the effectiveness of the proposed evidence-guided system. The code is available at https://github.com/peifengLiu42/ACMMM26-evidence-guided-detector-localizer-reasoner-system.

</details>

#### 2026-09-01 - TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views

**Authors:** Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman, Yi Yang, Ignacio Rocco, Jeet Thakwani, Rishabh Kabra, Andrew Zisserman, Joao Carreira, Siyu Tang, Carl Doersch, Gabriel Brostow
**Links:** [abs](https://arxiv.org/abs/2609.01899) - [pdf](https://arxiv.org/pdf/2609.01899)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** 4D reconstruction, SfM, SLAM, robotics, autonomous driving, AR, VR, simulation

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：TAPVid-MV: A Benchmark for Tracking Any Point in 3D Across Multiple Views
- 作者：Skanda Koppula, Frano Rajic, Abdullah Faiz Ur Rahman, Yi Yang, Ignacio Rocco, Jeet Thakwani, Rishabh Kabra, Andrew Zisserman, Joao Carreira, Siyu Tang, Carl Doersch, Gabriel Brostow
- 出版日期：2026-09-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.01899

### 一句话总结
本文提出 TAPVid-MV，一个用于跨多个同步、移动相机视角下进行 3D 点跟踪的新基准，并发现现有方法在该任务上表现不佳，几何恢复是主要瓶颈。

### 研究问题
现有点跟踪基准仅针对单视频或静态多相机设置，缺乏对相机运动下、多同步视角中长期 3D 点跟踪的评估；因此需要一个专门的基准来测试和推动该方向的发展。

### 核心思路/方法
- 构建包含 284 个序列、1,142 个标定相机流和 109,769 条点轨迹的基准，覆盖室内外、机器人、人类活动、驾驶及合成程序化场景等 7 个子集。
- 通过数据集特有的辅助模态（如传感器深度、LiDAR、SLAM/SfM 点、人体网格、带姿态物体网格和仿真）获取轨迹，并由人类标注者进行视觉验证。
- 在同一数据集上联合评估重建与点跟踪，以区分几何恢复错误与点对应错误，并对比多视角与单目点跟踪器性能。

### 主要贡献
- 提出首个面向运动多相机设置下长期 3D 点跟踪的基准 TAPVid-MV。
- 提供大规模、经过人工验证的点轨迹标注，覆盖多种室内外场景。
- 通过 30 多个基线评估显示现有方法远未解决该任务，且多视角点跟踪器并未稳定优于单目点跟踪器。
- 通过联合分析指出几何恢复是准确 3D 点跟踪的主要瓶颈。
- 释放的标注还支持单目 2D/3D 点跟踪、未来轨迹预测和 4D 重建等下游任务。

### 局限性
摘要未提供足够信息（未说明基准在特定场景类型上的失败模式、对标注噪声的敏感性、评估指标的具体细节或计算开销等）。

### 阅读优先级
**高**。理由：该工作提出了一个全新且具有明确实际需求（机器人、AR/VR、自动驾驶）的基准，覆盖广泛场景并附有大规模人工验证数据；同时揭示了现有方法在该任务上的明显不足和关键瓶颈（几何恢复），对点跟踪、多视角重建及 3D 感知领域的研究者具有直接参考价值。

</details>

<details>
<summary>Abstract</summary>

Multi-camera systems are increasingly practical for robotics, AR/VR, and autonomous driving because complementary views reduce depth ambiguity and preserve visibility under occlusion. Existing point-tracking benchmarks, however, focus on a single video or static multi-camera rigs. None test long-term 3D point tracking across several synchronized views under camera motion. We introduce TAPVid-MV (Tracking Any Point in Video across Multiple Views), the first benchmark for this setting. It contains a curated set of 284 sequences, 1,142 calibrated camera streams, and 109,769 point tracks across seven subsets spanning indoor and outdoor domains, from robotics and human activity to driving and synthetic procedural scenes. We obtain these trajectories using dataset-specific auxiliary modalities: sensor depth, LiDAR, SLAM and SfM points, human meshes, posed object meshes, and simulation. Every sequence and trajectory is visually verified by human annotators. Across more than 30 baselines, no method comes close to solving the task. Surprisingly, existing multi-view point trackers do not consistently outperform monocular point trackers. By evaluating reconstruction and point tracking on the same datasets, TAPVid-MV helps distinguish errors in recovered geometry from errors in point correspondence. Through this joint analysis, we identify geometry recovery as a major bottleneck for accurate 3D point tracking. Beyond multi-view 3D point tracking, our released annotations support monocular 2D and 3D point tracking, future-trajectory prediction, and 4D reconstruction.

</details>

#### 2026-09-01 - One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems

**Authors:** Jaehyung Jang, Zhenish Zhakypov, Jasmin Elena Palmer, Melissa Klein, Jee-Hwan Ryu, Allison Mariko Okamura
**Links:** [abs](https://arxiv.org/abs/2609.00751) - [pdf](https://arxiv.org/pdf/2609.00751)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** robotics, VR, virtual reality

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：One Print, Many Moves: Monolithic Origami-inspired Folding Actuator for Composable Soft Multi-DoF Systems
- 作者：Jaehyung Jang, Zhenish Zhakypov, Jasmin Elena Palmer, Melissa Klein, Jee-Hwan Ryu, Allison Mariko Okamura
- 出版日期：2026-09-01
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.00751

### 一句话总结
本文提出一种名为MONORIGAMI的单材料、单次3D打印、免装配的折纸启发式软体折叠致动器，通过空间编程的刚度各向异性，在保持柔顺性的同时实现精确、可组合的多自由度运动。

### 研究问题
传统软体机器人致动器虽具有良好的柔顺性，但其不可控变形导致精度不足，且难以扩展至多自由度系统。本文旨在解决如何在保持材料柔顺性的前提下，实现高精度、可扩展的软体多自由度驱动。

### 核心思路/方法
- 提出“空间编程的刚度各向异性”设计策略：沿期望折叠方向保持柔顺性，同时在非期望方向选择性限制变形。
- 基于材料厚度设计“刚度层级”，并按照折纸启发的几何结构（包含折面和折痕）进行图案化排布，从而将无约束的软体变形转化为精确、可重复的折叠运动。
- 整个设计只需单材料、单次3D打印，无需任何装配。
- 每个致动器作为可扩展的运动基元，通过链接和定向多个致动器即可机械编程多自由度轨迹。

### 主要贡献
1. 提出MONORIGAMI致动器设计范式，通过刚度各向异性和折纸几何在软体材料中实现空间编程变形控制。
2. 实现完全单材料、单次打印、免装配的制造流程，无需额外增强结构。
3. 基于同一基础模块展示了三个不同应用领域的3D打印软体多自由度系统：
   - 面向VR高保真皮肤反馈的紧凑型4自由度可穿戴触觉设备；
   - 用于遥操作动觉反馈的3自由度操纵杆；
   - 可水下作业、具有几何编码抓取轨迹的模块化机械爪。
4. 论证了该平台在紧凑多轴集成、受控物理交互和跨环境几何编程操作方面的通用性、可组合性、可访问性、可靠性和可扩展性。

### 局限性
摘要未提供足够信息，文中未明确讨论该致动器在负载能力、寿命、疲劳性能、控制复杂度或制造精度容差等方面的潜在局限性。

### 阅读优先级
**高**

理由：该工作提出了一种全新的软体致动器设计范式，解决了软体机器人向高精度多自由度系统扩展的长期难题，且实现了单次打印免装配的高可制造性。同时，论文在三个截然不同的实际领域（VR触觉、遥操作、水下抓取）中进行了系统级验证，具有较高的科学影响力和工程转化潜力，值得优先阅读。

</details>

<details>
<summary>Abstract</summary>

Conventional soft robot actuators excel in compliance, but their uncontrolled deformations compromise accuracy and hinder scaling to multi-degree-of-freedom (DoF) systems. We introduce a MONOlithic ORIGAMI-inspired soft folding actuator design (MONORIGAMI) that establishes a design strategy based on spatially programmed stiffness anisotropy to preserve material compliance along desired folding directions while selectively restricting deformation in unwanted directions. The actuator leverages stiffness tiers based on material thickness, patterned in an origami-inspired geometry with facets and creases, converting unconstrained soft deformation into accurate, repeatable, and composable folding motions without additional reinforcements. The design is fully 3D-printable through a single-material, single-print process that requires no assembly. Each actuator serves as a scalable motion primitive, and linking and orienting multiple actuators mechanically programs multi-DoF trajectories. Using the same fundamental module, we demonstrate three 3D-printed soft multi-DoF robotic systems spanning distinct application domains: (1) a compact 4-DoF wearable haptic device for high-fidelity cutaneous feedback in virtual reality (VR), (2) a 3-DoF joystick for kinesthetic feedback in teleoperation, and (3) a modular robotic gripper capable of underwater operation with geometry-encoded grasp trajectories. These systems demonstrate the module's capabilities for compact multi-axis integration, controlled physical interaction, and geometry-programmed operation across different environments. Together, these results show that MONORIGAMI provides a general, composable, accessible, reliable, and scalable platform for high-precision soft multi-DoF robotics, addressing long-standing limitations in both soft actuator design and fabrication.

</details>

### 2026-08

#### 2026-08-31 - IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training

**Authors:** Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu, Haisheng Su, Xin Zhang, Wei Wu, Chen Gao, Yong Li, Zhibo Chen
**Links:** [abs](https://arxiv.org/abs/2609.00161) - [pdf](https://arxiv.org/pdf/2609.00161)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** manipulation, world model

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training
- 作者：Rongze Tang, Jianjie Fang, Zhaolu Wang, Ziyou Wang, Xvyuan Liu, Haisheng Su, Xin Zhang, Wei Wu, Chen Gao, Yong Li, Zhibo Chen
- 出版日期：2026-08-31
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2609.00161

### 一句话总结
本文提出IMPACT框架，通过将跨注意力作为内部时空先验来生成交互图并对去噪监督进行加权，从而在不依赖外部表示或推理时改动的情况下提升世界模型在交互生成中的物理合理性与视觉质量。

### 研究问题
世界模型在动作条件下未来预测中难以建模物理上合理的交互；现有方法依赖外部表示（如运动、几何、语义）约束生成，但这些表示获取成本高（需辅助估计器或人工标注），限制了训练的可扩展性。作者指出根本原因在于全局平均MSE去噪目标下存在监督分配失配问题——静态内容主导优化信号，动态交互区域被欠监督。

### 核心思路/方法
IMPACT的核心是识别MSE监督分配失配问题，并提出无需外部表示的解决方案：
1. 使用与操作对象token关联的交叉注意力作为动作条件变化的内部时空先验；
2. 从该先验中采样候选区域，并用分离的局部预测误差对候选区域进行校准，构建“交互图”；
3. 利用交互图对去噪监督进行重新加权，使稀疏的动态交互区域获得更充分的监督。
该方法无需外部表示，也不需要在推理时修改模型。

### 主要贡献
- 识别了全局平均MSE去噪目标下的监督分配失配问题，指出其是限制世界模型交互建模能力的根本原因之一；
- 提出IMPACT训练框架，利用内部交叉注意力先验与局部预测误差构建交互图以重新加权监督，免除了外部表示和人工标注的需求；
- 在机械臂与机械手操作任务上，跨越不同控制模态和DiT骨干网络，一致优于MSE训练的基线，在交互保真度、物理合理性、视觉质量上均有提升。

### 局限性
摘要未提供足够信息以判断该方法在非操作类交互场景、更大规模数据集、长时程预测等方面的泛化性能，也未讨论计算开销或失败案例。

### 阅读优先级
**高**。理由：该工作针对世界模型交互建模这一重要难题提出了无需外部标注的通用训练方案，核心思路（从监督分配失配切入并用内部注意力构建交互图）具有一定新颖性和可扩展性；实验覆盖多个任务与骨干网络，适合关注具身智能、世界模型与扩散模型训练的研究者阅读。

</details>

<details>
<summary>Abstract</summary>

World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions. Existing approaches address this limitation by constraining the generation process with external representations encoding motion, geometry, or semantics. Obtaining these spatiotemporally dense representations typically requires auxiliary estimators or manual annotations, limiting training scalability. We instead revisit the training objective and identify a supervision-allocation mismatch under the globally averaged mean squared error (MSE) denoising objective: prevalent static content dominates the optimization signal, leaving sparse dynamic-object regions critical to interaction generation disproportionately under-supervised. Motivated by this observation, we introduce IMPACT, a scalable Interaction-aware Model training framework with Prior-guided Attention Calibration and Targeting. IMPACT uses cross-attention associated with manipulated-object tokens as an internal spatiotemporal prior for action-conditioned changes. It samples candidate regions from this prior, calibrates them with detached local prediction errors to construct an interaction map, and uses the map to reweight denoising supervision, requiring neither external representations nor inference-time modifications. Extensive experiments on robot-arm and human-hand manipulation, spanning diverse control modalities and DiT backbones, show that IMPACT consistently outperforms the corresponding MSE-trained baselines, improving interaction fidelity, physical plausibility, and visual quality.

</details>

#### 2026-08-31 - APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images

**Authors:** Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, Sung-eui Yoon
**Links:** [abs](https://arxiv.org/abs/2608.30656) - [pdf](https://arxiv.org/pdf/2608.30656)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** rendering, manipulation, localization

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：APT: Anchor-aligned Perturbations for Tamper Localization in Fully Regenerated Images
- 作者：Suhyeon Ha, Woo Jae Kim, Joonsung Jeon, Sooel Son, Sung-eui Yoon
- 出版日期：2026-08-31
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.30656

### 一句话总结
本文提出APT（锚点对齐扰动）方法，通过在潜在空间嵌入密集向量定位信号，实现对扩散模型完全重建图像中篡改区域的像素级定位，在COCO数据集上达到0.92的FR IoU，显著优于现有基线。

### 研究问题
现有主动篡改定位方法基于拼接（SP）设定，即合成区域叠加在原始背景之上，嵌入信号得以保留。然而真实场景中基于扩散模型的修复（inpainting）属于完全重建（FR）设定——整张图像都经过去噪过程，背景信号被破坏，导致现有框架失效。因此需要针对FR设定设计新的篡改定位方案。

### 核心思路/方法
APT采用半脆弱的潜在空间扰动，在图像分发前嵌入密集的向量级定位信号。具体做法：
- 将每个空间特征向量对齐到固定的锚点方向；
- 修复（inpainting）后，通过合成前景与锚点对齐背景特征之间的对齐差异来定位篡改区域；
- 引入难负样本挖掘（hard negative mining）损失和噪声扰动分支，进一步增强对齐的均匀性。

### 主要贡献
1. 提出APT框架，首次针对扩散模型完全重建（FR）设定下的篡改定位问题；
2. 实现FR IoU 0.92，超过最强基线WAM（0.84），而现有方法在该设定下性能接近随机（AUC 0.5）；
3. 框架可泛化到测试时未知的篡改类型。

### 局限性
摘要未提供足够信息。

### 阅读优先级
**高**。理由：该工作切入了一个实际但被忽视的场景（扩散模型完全重建下的篡改检测），给出了明确的量化优势（FR IoU 0.92 vs 0.84），且指出现有方法在该设定下完全失效（AUC 0.5），具有清晰的实践意义和对比价值。

</details>

<details>
<summary>Abstract</summary>

Proactive tamper localization embeds an imperceptible signal into an image prior to distribution, enabling pixel-level manipulation detection. Existing methods assume a spliced (SP) setting, where synthesized regions are composited onto the original background, leaving embedded signals intact. However, real-world diffusion-based inpainting operates in a fully regenerated (FR) setting, where the entire image undergoes denoising, disrupting background signals and rendering existing frameworks ineffective. We propose APT, a semi-fragile latent-space perturbation that embeds a dense, vector-wise localization signal. By aligning each spatial feature vector toward a fixed anchor direction, APT localizes tampering via the alignment disparity between synthesized foreground and anchor-aligned background features after inpainting. The proposed hard negative mining loss and noisy perturbation branch further enforce uniform alignment. Experiments on COCO demonstrate that APT achieves an FR IoU of 0.92, outperforming the strongest baseline (WAM, 0.84), while existing methods collapse to near-random performance (AUC 0.5), establishing APT as a practical forensic framework generalizable across tampering types unknown at test time.

</details>

#### 2026-08-31 - Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection

**Authors:** Gongzhe Li, Linwei Qiu, Peibei Cao, Fengying Xie, Xiangyang Ji, Qilin Sun
**Links:** [abs](https://arxiv.org/abs/2608.30400) - [pdf](https://arxiv.org/pdf/2608.30400)
**Primary category:** Embodied / Robotics / AR Applications
**Secondary categories:** None
**Matched keywords:** autonomous driving, mapping

<details>
<summary>AI 简析</summary>

### Metadata
- 标题：Real-Time Scene-Adaptive Tone Mapping for High-Dynamic Range Object Detection
- 作者：Gongzhe Li, Linwei Qiu, Peibei Cao, Fengying Xie, Xiangyang Ji, Qilin Sun
- 出版日期：2026-08-31T07:52:53Z
- 分类：Embodied / Robotics / AR Applications
- 链接：https://arxiv.org/abs/2608.30400

### 一句话总结
本文提出一种面向高动态范围（HDR）图像目标检测的场景自适应实时色调映射方法，通过端到端优化弥合HDR RAW输入与检测网络所需的LDR sRGB输入之间的差距。

### 研究问题
HDR图像包含丰富的色调与细节信息，对自动驾驶等计算机视觉系统具有潜力，但多数嵌入式神经网络基于低动态范围（LDR）输入训练，在处理高比特深度HDR图像时会因极端动态范围而出现显著性能下降。本文旨在解决该差距问题。

### 核心思路/方法
- 提出一种新颖的色调映射方法，将HDR RAW输入与检测网络所需的LDR sRGB要求相连接，并与下游任务实现端到端联合优化。
- 不依赖传统图像信号处理（ISP）流程，引入神经光度校准（neural photometric calibration）对动态范围进行正则化，并使用缩放不变局部色调映射模型（scaling-invariant local tone mapping model）保留图像细节。
- 架构支持性能迁移微调（performance transfer finetuning），能以最小成本从LDR sRGB图像高效适配至HDR RAW图像。

### 主要贡献
- 提出一种端到端可优化的色调映射方法，兼顾HDR输入与LDR检测网络需求。
- 引入神经光度校准与缩放不变局部色调映射模型，替代传统ISP流程。
- 支持性能迁移微调，降低从LDR到HDR输入的适配成本。
- 在挑战性汽车HDR场景中优于传统色调映射算法及先进AI-ISP方法。
- 在NVIDIA Jetson平台上实现对4K高比特深度HDR输入的实时处理。

### 局限性
摘要未提供足够信息（如对极端动态范围的具体量化表现、模型规模、训练数据细节、在非汽车场景下的泛化能力、微调所需的具体数据量等均未提及）。

### 阅读优先级
**高**

理由：该工作针对自动驾驶等实际应用中HDR图像与现有LDR检测网络不匹配的关键问题，提出端到端可优化的实时色调映射方案，并展示在嵌入式平台（NVIDIA Jetson）上的实时处理能力，兼具算法创新与实际部署价值，对相关领域研究者具有较高参考意义。

</details>

<details>
<summary>Abstract</summary>

High-dynamic-range (HDR) images, with their rich tone and detail reproduction, hold significant potential to enhance computer vision systems, particularly in autonomous driving. However, most neural networks for embedded systems are trained on low-dynamic-range (LDR) inputs and suffer substantial performance degradation when handling high-bit-depth HDR images due to the challenges posed by extreme dynamic ranges. In this paper, we propose a novel tone mapping method that not only bridges the gap between HDR RAW inputs and the LDR sRGB requirements of detection networks but also achieves end-to-end optimization with downstream tasks. Instead of relying on the traditional image signal processing (ISP) pipeline, we introduce neural photometric calibration to regularize dynamic ranges and a scaling-invariant local tone mapping model to preserve image details. In addition, our architecture also supports performance transfer finetuning, enabling efficient adaptation from the LDR sRGB images to the HDR RAW images with minimal cost. The proposed method outperforms traditional tone mapping algorithms and advanced AI-ISP methods in challenging automotive HDR scenes. Moreover, our pipeline achieves real-time processing of 4K high-bit-depth HDR inputs on NVIDIA Jetson platforms.

</details>

## Data Source and Disclaimer

Paper metadata is retrieved from the arXiv API. PDF files are not mirrored or redistributed by this project. Links direct users to the original abstract and PDF pages.

Thank you to arXiv for use of its open access interoperability. This project was not reviewed or approved by, nor does it necessarily express or reflect the policies or opinions of, arXiv.
