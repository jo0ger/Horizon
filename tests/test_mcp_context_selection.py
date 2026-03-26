from __future__ import annotations

from pathlib import Path

from src.mcp.service import HorizonPipelineService


def test_service_default_industry_selection_is_used() -> None:
    service = HorizonPipelineService(
        default_horizon_path="/repo",
        default_industry="healthcare",
        default_base_config_path="/repo/data/config/base.json",
    )

    selection = service._resolve_selection(
        run_id=None,
        horizon_path=None,
        config_path=None,
        industry=None,
        base_config_path=None,
        industry_config_path=None,
    )

    assert selection.horizon_path == "/repo"
    assert selection.industry == "healthcare"
    assert selection.base_config_path == "/repo/data/config/base.json"
    assert selection.config_path is None


def test_run_meta_selection_overrides_service_default() -> None:
    service = HorizonPipelineService(
        runs_root=Path("/tmp/mcp-runs"),
        default_industry="healthcare",
    )
    run_id = service.run_store.create_run("run-gaming")
    service.run_store.update_meta(
        run_id,
        {
            "horizon_path": "/repo",
            "industry": "gaming",
            "base_config_path": "/repo/data/config/base.json",
            "industry_config_path": "/repo/data/config/industries/gaming.json",
        },
    )

    selection = service._resolve_selection(
        run_id=run_id,
        horizon_path=None,
        config_path=None,
        industry=None,
        base_config_path=None,
        industry_config_path=None,
    )

    assert selection.industry == "gaming"
    assert selection.base_config_path == "/repo/data/config/base.json"
    assert selection.industry_config_path == "/repo/data/config/industries/gaming.json"


def test_run_meta_layered_selection_clears_default_legacy_config() -> None:
    service = HorizonPipelineService(
        runs_root=Path("/tmp/mcp-runs-legacy"),
        default_config_path="/repo/data/config.json",
    )
    run_id = service.run_store.create_run("run-layered")
    service.run_store.update_meta(
        run_id,
        {
            "industry": "gaming",
            "base_config_path": "/repo/data/config/base.json",
            "industry_config_path": "/repo/data/config/industries/gaming.json",
        },
    )

    selection = service._resolve_selection(
        run_id=run_id,
        horizon_path=None,
        config_path=None,
        industry=None,
        base_config_path=None,
        industry_config_path=None,
    )

    assert selection.config_path is None
    assert selection.industry == "gaming"


def test_explicit_legacy_config_clears_layered_defaults() -> None:
    service = HorizonPipelineService(
        default_industry="healthcare",
        default_base_config_path="/repo/data/config/base.json",
    )

    selection = service._resolve_selection(
        run_id=None,
        horizon_path=None,
        config_path="/repo/data/config.json",
        industry=None,
        base_config_path=None,
        industry_config_path=None,
    )

    assert selection.config_path == "/repo/data/config.json"
    assert selection.industry is None
    assert selection.base_config_path is None
    assert selection.industry_config_path is None


def test_explicit_layered_selection_clears_legacy_default() -> None:
    service = HorizonPipelineService(
        default_config_path="/repo/data/config.json",
    )

    selection = service._resolve_selection(
        run_id=None,
        horizon_path=None,
        config_path=None,
        industry="gaming",
        base_config_path="/repo/data/config/base.json",
        industry_config_path="/repo/data/config/industries/gaming.json",
    )

    assert selection.config_path is None
    assert selection.industry == "gaming"
    assert selection.base_config_path == "/repo/data/config/base.json"
    assert selection.industry_config_path == "/repo/data/config/industries/gaming.json"


def test_explicit_industry_clears_stale_default_industry_config_path() -> None:
    service = HorizonPipelineService(
        default_industry="healthcare",
        default_industry_config_path="/repo/data/config/industries/healthcare.json",
    )

    selection = service._resolve_selection(
        run_id=None,
        horizon_path=None,
        config_path=None,
        industry="gaming",
        base_config_path=None,
        industry_config_path=None,
    )

    assert selection.industry == "gaming"
    assert selection.industry_config_path is None
