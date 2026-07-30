#!/usr/bin/env python3
"""Load config/daily_corpus_allowlist.yaml — single daily-hot canon for air + mini.

Used by:
  - source_manifest / build_daily_active_corpus (active bundle)
  - daily_corpus_to_khoj (bounded PUT path)

Never expands to whole SSD or whole ~/.pi.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ALLOWLIST_PATH = REPO_ROOT / "config" / "daily_corpus_allowlist.yaml"

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore


@dataclass(frozen=True)
class AllowlistEntry:
    id: str
    family: str
    path: Path
    suffixes: tuple[str, ...]
    recursive: bool
    max_files: int
    required: bool


@dataclass(frozen=True)
class AllowlistConfig:
    version: int
    hot_days: int
    max_file_bytes: int
    max_md_files: int
    deny_substrings: tuple[str, ...]
    entries: tuple[AllowlistEntry, ...]
    path: Path


def _expand(raw: str, home: Path) -> Path:
    raw = raw.strip()
    if raw.startswith("~/"):
        return (home / raw[2:]).resolve()
    p = Path(raw)
    if p.is_absolute():
        return p
    return (home / raw).expanduser().resolve()


def _load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML required to load daily_corpus_allowlist.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"allowlist root must be a mapping: {path}")
    return data


def resolve_entry_path(entry: dict[str, Any], home: Path) -> Path | None:
    """First existing path among path + alt_paths."""
    candidates = [entry["path"], *list(entry.get("alt_paths") or [])]
    for raw in candidates:
        p = _expand(str(raw), home)
        if p.exists():
            return p
    # return primary even if missing (caller handles required)
    return _expand(str(entry["path"]), home)


def load_allowlist(
    path: Path | None = None,
    *,
    home: Path | None = None,
) -> AllowlistConfig:
    path = (path or Path(os.environ.get("MYAPI_DAILY_ALLOWLIST", DEFAULT_ALLOWLIST_PATH))).expanduser()
    home = home or Path.home()
    if not path.is_file():
        raise FileNotFoundError(f"daily allowlist missing: {path}")

    data = _load_yaml(path)
    defaults = data.get("defaults") or {}
    deny = tuple(str(x) for x in (data.get("deny_substrings") or []))
    entries: list[AllowlistEntry] = []
    for raw in data.get("entries") or []:
        resolved = resolve_entry_path(raw, home)
        assert resolved is not None
        entries.append(
            AllowlistEntry(
                id=str(raw["id"]),
                family=str(raw.get("family") or raw["id"]),
                path=resolved,
                suffixes=tuple(str(s) for s in (raw.get("suffixes") or [".md"])),
                recursive=bool(raw.get("recursive", True)),
                max_files=int(raw.get("max_files") or 50),
                required=bool(raw.get("required", False)),
            )
        )
    return AllowlistConfig(
        version=int(data.get("version") or 1),
        hot_days=int(defaults.get("hot_days") or 30),
        max_file_bytes=int(defaults.get("max_file_bytes") or 512_000),
        max_md_files=int(defaults.get("max_md_files") or 150),
        deny_substrings=deny,
        entries=tuple(entries),
        path=path,
    )


def denied(path: Path, deny_substrings: tuple[str, ...]) -> bool:
    s = path.as_posix().lower()
    return any(part in s for part in deny_substrings)


def iter_entry_files(entry: AllowlistEntry, deny: tuple[str, ...]) -> list[Path]:
    """Bounded file list for one allowlist entry (newest first when capped)."""
    root = entry.path
    if not root.exists():
        return []
    if root.is_file():
        return [] if denied(root, deny) else [root]

    found: list[Path] = []
    if entry.recursive:
        for p in root.rglob("*"):
            if not p.is_file():
                continue
            if entry.suffixes and p.suffix not in entry.suffixes:
                continue
            if denied(p, deny):
                continue
            # prune heavy dirs
            parts = set(p.parts)
            if parts & {".git", "node_modules", ".venv", "venv", "__pycache__", "artifacts"}:
                continue
            found.append(p)
    else:
        for p in root.iterdir():
            if not p.is_file():
                continue
            if entry.suffixes and p.suffix not in entry.suffixes:
                continue
            if denied(p, deny):
                continue
            found.append(p)

    found.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return found[: entry.max_files]


def sources_for_manifest(cfg: AllowlistConfig | None = None):
    """Return source_manifest.Source tuples for build_corpus_manifest."""
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from scripts.source_manifest import Source  # local import avoids cycle at module load

    cfg = cfg or load_allowlist()
    out: list = []
    for e in cfg.entries:
        if e.required and not e.path.exists():
            raise FileNotFoundError(f"required allowlist path missing: {e.id} → {e.path}")
        if not e.path.exists():
            continue
        out.append(
            Source(
                source_family=e.family,
                path=e.path,
                parser_available=True,
                suffixes=e.suffixes,
            )
        )
    return tuple(out)


def main() -> int:
    cfg = load_allowlist()
    print(f"allowlist={cfg.path}")
    print(f"version={cfg.version} hot_days={cfg.hot_days} max_md={cfg.max_md_files}")
    total = 0
    for e in cfg.entries:
        files = iter_entry_files(e, cfg.deny_substrings)
        total += len(files)
        status = "ok" if e.path.exists() else "MISSING"
        print(f"  {e.id:28} {status:7} n={len(files):3}  {e.path}")
    print(f"total_files_capped={total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
