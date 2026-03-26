"""Helpers for loading legacy and layered Horizon configuration."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import Config


@dataclass
class LoadedConfig:
    """Resolved runtime config and related filesystem paths."""

    config: Config
    config_path: Path
    storage_data_dir: Path
    mode: str
    base_config_path: Path | None = None
    industry_config_path: Path | None = None


def load_runtime_config(
    repo_root: Path,
    *,
    industry: str | None = None,
    base_config_path: str | None = None,
    industry_config_path: str | None = None,
    legacy_config_path: str | None = None,
) -> LoadedConfig:
    """Load either layered config or the legacy single-file config."""

    repo_root = repo_root.resolve()

    if industry or base_config_path or industry_config_path:
        return load_layered_config(
            repo_root,
            industry=industry,
            base_config_path=base_config_path,
            industry_config_path=industry_config_path,
        )

    return load_legacy_config(
        repo_root,
        config_path=legacy_config_path,
    )


def load_legacy_config(repo_root: Path, config_path: str | None = None) -> LoadedConfig:
    """Load the original single-file config format."""

    repo_root = repo_root.resolve()
    path = _resolve_path(repo_root, config_path or "data/config.json")
    payload = _read_json(path)
    config = Config.model_validate(payload)

    return LoadedConfig(
        config=config,
        config_path=path,
        storage_data_dir=path.parent.resolve(),
        mode="legacy",
        base_config_path=None,
        industry_config_path=None,
    )


def load_layered_config(
    repo_root: Path,
    *,
    industry: str | None,
    base_config_path: str | None = None,
    industry_config_path: str | None = None,
) -> LoadedConfig:
    """Load base + industry config, then validate the merged payload."""

    repo_root = repo_root.resolve()
    base_path = _resolve_path(repo_root, base_config_path or "data/config/base.json")
    if industry_config_path:
        industry_path = _resolve_path(repo_root, industry_config_path)
    else:
        if not industry:
            raise FileNotFoundError(
                "Industry config was requested but no industry id or industry config path was provided."
            )
        industry_path = _resolve_path(repo_root, f"data/config/industries/{industry}.json")

    base_payload = _read_json(base_path)
    industry_payload = _read_json(industry_path)
    merged = _deep_merge(base_payload, industry_payload)
    config = Config.model_validate(merged)

    return LoadedConfig(
        config=config,
        config_path=industry_path,
        storage_data_dir=(repo_root / "data").resolve(),
        mode="layered",
        base_config_path=base_path,
        industry_config_path=industry_path,
    )


def _resolve_path(repo_root: Path, raw_path: str) -> Path:
    path = Path(raw_path).expanduser()
    if not path.is_absolute():
        path = (repo_root / path).resolve()
    else:
        path = path.resolve()

    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    return path


def _read_json(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    if not isinstance(payload, dict):
        raise ValueError(f"Configuration file must contain a JSON object: {path}")
    return payload


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if value is None:
            merged[key] = None
            continue

        base_value = merged.get(key)
        if isinstance(base_value, dict) and isinstance(value, dict):
            merged[key] = _deep_merge(base_value, value)
        else:
            merged[key] = value
    return merged
