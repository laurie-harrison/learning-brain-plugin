#!/usr/bin/env python3
"""Install the Learning Brain plugin into a user's local Codex plugin marketplace."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


PLUGIN_NAME = "learning-brain"
MARKETPLACE_ENTRY = {
    "name": PLUGIN_NAME,
    "source": {
        "source": "local",
        "path": f"./.codex/plugins/{PLUGIN_NAME}",
    },
    "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL",
    },
    "category": "Productivity",
}


def copy_plugin(source_root: Path, destination_root: Path) -> Path:
    destination = destination_root / PLUGIN_NAME
    destination_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(
        source_root,
        destination,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"),
    )
    return destination


def load_marketplace(path: Path) -> dict:
    if not path.exists():
        return {
            "name": "personal-local",
            "interface": {"displayName": "Personal Plugins"},
            "plugins": [],
        }

    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object.")

    plugins = payload.setdefault("plugins", [])
    if not isinstance(plugins, list):
        raise ValueError(f"{path} field 'plugins' must be an array.")

    interface = payload.setdefault("interface", {})
    if not isinstance(interface, dict):
        raise ValueError(f"{path} field 'interface' must be an object.")

    payload.setdefault("name", "personal-local")
    interface.setdefault("displayName", "Personal Plugins")
    return payload


def upsert_marketplace_entry(path: Path) -> None:
    payload = load_marketplace(path)
    plugins = payload["plugins"]
    assert isinstance(plugins, list)

    for index, entry in enumerate(plugins):
        if isinstance(entry, dict) and entry.get("name") == PLUGIN_NAME:
            plugins[index] = MARKETPLACE_ENTRY
            break
    else:
        plugins.append(MARKETPLACE_ENTRY)

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def main() -> int:
    script_path = Path(__file__).resolve()
    plugin_root = script_path.parent.parent
    home = Path.home()
    destination_root = home / ".codex" / "plugins"
    marketplace_path = home / ".agents" / "plugins" / "marketplace.json"

    copy_plugin(plugin_root, destination_root)
    upsert_marketplace_entry(marketplace_path)

    print("Installed Learning Brain for Codex.")
    print(f"- Plugin copy: {destination_root / PLUGIN_NAME}")
    print(f"- Marketplace: {marketplace_path}")
    print("")
    print("Next steps:")
    print("1. Restart Codex.")
    print("2. Open Plugins and look under your personal marketplace.")
    print("3. Install or enable Learning Brain.")
    print("4. Authenticate when Codex prompts you for the Learning Brain MCP server.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover - installer UX path
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
