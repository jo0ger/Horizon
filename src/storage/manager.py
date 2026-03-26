"""Storage manager for configuration and state persistence."""

import json
import shutil
from pathlib import Path
from typing import Optional

from ..models import Config


class StorageManager:
    """Manages file-based storage for configuration and state."""

    def __init__(
        self,
        data_dir: str | Path = "data",
        *,
        root_dir: str | Path | None = None,
        config_path: str | Path | None = None,
        summaries_dir: str | Path | None = None,
    ):
        self.root_dir = Path(root_dir).resolve() if root_dir else Path.cwd().resolve()
        self.data_dir = self.resolve_path(data_dir)
        self.config_path = self.resolve_path(config_path) if config_path else self.data_dir / "config.json"
        self.summaries_dir = self.resolve_path(summaries_dir or "data/summaries")

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def resolve_path(self, raw_path: str | Path | None) -> Path:
        if raw_path is None:
            return self.root_dir
        path = Path(raw_path).expanduser()
        if not path.is_absolute():
            path = (self.root_dir / path).resolve()
        else:
            path = path.resolve()
        return path

    def load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return Config.model_validate(data)

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config.model_dump(mode="json"), f, indent=2, ensure_ascii=False)
            f.write("\n")

        return self.config_path

    def save_daily_summary(
        self,
        date: str,
        markdown: str,
        language: str = "en",
        industry_slug: Optional[str] = None,
    ) -> Path:
        filename = f"horizon-{date}-{language}.md"
        if industry_slug:
            filename = f"horizon-{industry_slug}-{date}-{language}.md"
        filepath = self.summaries_dir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown)

        return filepath

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        with open(subscribers_path, "w", encoding="utf-8") as f:
            json.dump(subscribers, f, indent=2)
