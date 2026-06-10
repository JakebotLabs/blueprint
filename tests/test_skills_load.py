"""Smoke tests for skills/ — no external dependencies.

Runs as both pytest (pytest tests/) and standalone (python tests/test_skills_load.py).
Exit non-zero on failure either way.

What this catches:
- A skill folder added without SKILL.md
- SKILL.md missing YAML frontmatter or missing the `name` / `description` fields
- The `name:` field disagreeing with the directory name (load-by-name failure)
- An internal markdown reference link pointing at a path that does not exist
  (caught the `../../brainstorm-v2/...` bug during Stage 1 round 2)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# Every skill in this fork.  Adding a new skill?  Add it here AND the smoke test
# below will require its SKILL.md + frontmatter + link targets to be correct.
EXPECTED_SKILLS: list[str] = [
    "blueprint",
    "blueprint-generate",
    "brainstorm-v2",
    "brainstorm-generate-v2",
]

_FRONTMATTER_RE = re.compile(r"^---\n(?P<body>.*?)\n---\n", re.DOTALL)
_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<href>[^)]+\.md)\)")


def _parse_frontmatter(skill_md: Path) -> dict[str, str]:
    """Tiny YAML-subset parser — just `key: value` lines, one per line."""
    text = skill_md.read_text(encoding="utf-8")
    m = _FRONTMATTER_RE.match(text)
    assert m, f"No YAML frontmatter block in {skill_md}"
    fields: dict[str, str] = {}
    for line in m.group("body").splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def test_all_expected_skills_exist() -> None:
    for name in EXPECTED_SKILLS:
        skill_md = SKILLS_DIR / name / "SKILL.md"
        assert skill_md.exists(), f"Missing SKILL.md for expected skill: {skill_md}"


def test_frontmatter_has_required_fields() -> None:
    for name in EXPECTED_SKILLS:
        skill_md = SKILLS_DIR / name / "SKILL.md"
        fields = _parse_frontmatter(skill_md)
        assert fields.get("name") == name, (
            f"name field in {skill_md} = {fields.get('name')!r}, "
            f"expected {name!r} (must match directory)"
        )
        description = fields.get("description", "")
        assert description, f"description field missing or empty in {skill_md}"


def test_internal_md_links_resolve() -> None:
    """Every internal .md link in every .md under skills/ must resolve to a real file."""
    broken: list[str] = []
    for md_file in SKILLS_DIR.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        for href in _LINK_RE.findall(text):
            if href.startswith(("http://", "https://")):
                continue
            target = (md_file.parent / href).resolve()
            if not target.exists():
                broken.append(f"{md_file} -> {href} (resolves to missing {target})")
    assert not broken, "Broken internal links:\n  " + "\n  ".join(broken)


def _run_standalone() -> int:
    """Manual runner — pytest is preferred but not required."""
    tests = [
        test_all_expected_skills_exist,
        test_frontmatter_has_required_fields,
        test_internal_md_links_resolve,
    ]
    failures: list[tuple[str, str]] = []
    for fn in tests:
        try:
            fn()
        except AssertionError as exc:
            failures.append((fn.__name__, str(exc)))
            print(f"FAIL {fn.__name__}")
            print(f"  {exc}")
        else:
            print(f"PASS {fn.__name__}")
    print()
    print(f"{len(tests) - len(failures)}/{len(tests)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(_run_standalone())
