from scripts.classification import classify_paper, load_config


CONFIG = load_config()


def classify(title: str, abstract: str = "", categories: list[str] | None = None) -> dict:
    return classify_paper(title, abstract, categories or ["cs.CV"], CONFIG)


def test_vggt_title_maps_to_geometry_foundation_models() -> None:
    result = classify(
        "VGGT for Feed-Forward 3D Reconstruction",
        "We predict camera parameters, point maps, and dense geometry.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "Geometry Foundation Models"


def test_dust3r_and_pointmap_abstract_maps_to_geometry_foundation_models() -> None:
    result = classify(
        "A general visual geometry model",
        "The method builds on DUSt3R and predicts a pointmap for dense correspondence.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "Geometry Foundation Models"


def test_dynamic_gaussian_reconstruction_maps_to_dynamic_with_neural_secondary() -> None:
    result = classify(
        "Dynamic Gaussian Scene Reconstruction from Monocular Video",
        "A 4D Gaussian scene representation improves temporal reconstruction.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "Dynamic / 4D Reconstruction"
    assert "Neural Scene Representations & Rendering" in result["secondary_categories"]


def test_static_sfm_mvs_maps_to_3d_reconstruction() -> None:
    result = classify(
        "Incremental SfM and MVS for Accurate 3D Reconstruction",
        "The system estimates camera poses and dense point clouds for static scenes.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "3D Reconstruction & Multi-view Geometry"


def test_pure_nerf_novel_view_synthesis_maps_to_neural_rendering() -> None:
    result = classify(
        "Fast NeRF for Novel View Synthesis",
        "We optimize a neural radiance field for high-quality rendering.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "Neural Scene Representations & Rendering"


def test_robot_slam_geometry_mapping_primary_3d_secondary_embodied() -> None:
    result = classify(
        "Robot SLAM for 3D Mapping and Localization",
        "A robotics system performs geometric mapping for embodied navigation.",
        ["cs.RO", "cs.CV"],
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "3D Reconstruction & Multi-view Geometry"
    assert "Embodied / Robotics / AR Applications" in result["secondary_categories"]


def test_pure_text_to_image_diffusion_is_excluded() -> None:
    result = classify(
        "Text-to-Image Diffusion for Controllable Image Generation",
        "The paper studies prompt following and image generation.",
    )

    assert not result["is_relevant"]


def test_pure_medical_image_segmentation_is_excluded() -> None:
    result = classify(
        "Medical Image Semantic Segmentation with Transformers",
        "The method segments organs in medical imaging datasets.",
    )

    assert not result["is_relevant"]


def test_medical_3d_reconstruction_is_excluded_by_default() -> None:
    result = classify(
        "Sparse-View Lung Nodule Reconstruction from X-ray Radiographs",
        "A clinical radiance field reconstructs pulmonary nodules from thoracic medical images.",
    )

    assert not result["is_relevant"]


def test_pure_llm_paper_is_excluded() -> None:
    result = classify(
        "Large Language Model Reasoning with Tool Feedback",
        "The work studies language-only instruction following.",
    )

    assert not result["is_relevant"]


def test_segmentation_assisted_3d_reconstruction_is_not_excluded() -> None:
    result = classify(
        "Segmentation-Assisted 3D Reconstruction from Multi-view Images",
        "Semantic segmentation cues are used only to improve surface reconstruction.",
    )

    assert result["is_relevant"]
    assert result["primary_category"] == "3D Reconstruction & Multi-view Geometry"


def test_robot_perception_without_geometry_support_is_not_enough() -> None:
    result = classify(
        "A Sonar-Visual Dataset for Underwater Robot Perception",
        "The dataset supports cross-modal prediction and fish detection for underwater robots.",
        ["cs.RO"],
    )

    assert not result["is_relevant"]
