"""CLI entry point for Horizon."""

import argparse
import asyncio
import json
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .config_loader import load_runtime_config
from .storage.manager import StorageManager
from .orchestrator import HorizonOrchestrator


console = Console()


def print_banner():
    """Print the application banner."""
    banner = r"""
[bold blue]
  _    _            _
 | |  | |          (_)
 | |__| | ___  _ __ _ ___  ___  _ __
 |  __  |/ _ \| '__| |_  / / _ \| '_ \
 | |  | | (_) | |  | |/ / | (_) | | | |
 |_|  |_|\___/|_|  |_/___| \___/|_| |_|
[/bold blue]
[cyan]  AI-Driven Information Aggregation System[/cyan]
    """
    console.print(banner)


def main():
    """Main CLI entry point."""
    print_banner()

    parser = argparse.ArgumentParser(description="Horizon - AI-Driven Information Aggregation System")
    parser.add_argument("--hours", type=int, help="Force fetch from last N hours")
    parser.add_argument("--source", type=str, help="Force fetch from a specific source")
    parser.add_argument("--industry", type=str, help="Load layered config for a specific industry")
    parser.add_argument("--base-config", type=str, help="Override the default base config path")
    parser.add_argument("--industry-config", type=str, help="Override the default industry config path")
    parser.add_argument(
        "--print-effective-config",
        action="store_true",
        help="Print the merged config and exit without running the pipeline",
    )
    args = parser.parse_args()

    try:
        # Load environment variables from .env file
        load_dotenv()

        project_root = Path.cwd()

        # Load configuration
        try:
            loaded = load_runtime_config(
                project_root,
                industry=args.industry,
                base_config_path=args.base_config,
                industry_config_path=args.industry_config,
            )
            config = loaded.config
        except FileNotFoundError:
            console.print("[bold red]❌ Configuration file not found![/bold red]\n")
            console.print(
                "Run [bold cyan]uv run horizon-wizard[/bold cyan] to create the legacy config,\n"
                "or create [cyan]data/config/base.json[/cyan] and [cyan]data/config/industries/<industry>.json[/cyan].\n"
            )
            print_config_template()
            sys.exit(1)
        except Exception as e:
            console.print(f"[bold red]❌ Error loading configuration: {e}[/bold red]")
            sys.exit(1)

        if args.print_effective_config:
            console.print_json(json.dumps(config.model_dump(mode="json"), ensure_ascii=False, indent=2))
            sys.exit(0)

        storage = StorageManager(
            data_dir=str(loaded.storage_data_dir),
            root_dir=project_root,
            config_path=loaded.config_path,
            summaries_dir=config.output.summaries_dir,
        )
        
        if args.source is not None:
            args.source = [part.strip() for part in args.source.split(",") if part.strip()]
          
        # Create and run orchestrator
        orchestrator = HorizonOrchestrator(config, storage)
        asyncio.run(orchestrator.run(force_hours=args.hours, force_source=args.source))

    except KeyboardInterrupt:
        console.print("\n[yellow]⚠️  Interrupted by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]❌ Fatal error: {e}[/bold red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def print_config_template():
    """Print configuration template."""
    template = """
Recommended layered config:

data/config/base.json
{
  "ai": {
    "provider": "openai",
    "model": "gpt-4",
    "api_key_env": "OPENAI_API_KEY",
    "languages": ["en", "zh"]
  },
  "filtering": {
    "ai_score_threshold": 6.5,
    "time_window_hours": 24
  },
  "output": {
    "summaries_dir": "data/summaries",
    "docs_posts_dir": "docs/_posts",
    "publish_to_docs": true,
    "include_industry_in_filename": true
  }
}

data/config/industries/healthcare.json
{
  "industry": {
    "id": "healthcare",
    "name": "Healthcare",
    "slug": "healthcare"
  },
  "sources": {
    "rss": [
      {
        "name": "Example Feed",
        "url": "https://example.com/feed.xml",
        "enabled": true
      }
    ]
  }
}
    """
    console.print(template)


if __name__ == "__main__":
    main()
