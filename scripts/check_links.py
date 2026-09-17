"""校验 README 索引与笔记文件是否一致。

两条规则：
1. README 中指向 `notes/*.md` 的链接，文件必须真实存在；
2. `notes/` 下的每个 `.md` 都必须被 README 索引（避免"孤儿笔记"）。

用法：uv run python scripts/check_links.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTES_DIR = ROOT / "notes"

LINK_RE = re.compile(r"\]\((notes/[^)\s]+\.md)\)")


def readme_links(text: str) -> set[str]:
    """README 中所有指向笔记的链接（形如 notes/.../*.md）。"""
    return set(LINK_RE.findall(text))


def note_files() -> set[str]:
    """notes/ 下所有 .md 的相对路径。"""
    return {p.relative_to(ROOT).as_posix() for p in NOTES_DIR.rglob("*.md")}


def check() -> list[str]:
    """返回问题列表；为空表示一切正常。"""
    links = readme_links(README.read_text(encoding="utf-8"))
    files = note_files()

    problems: list[str] = []
    for link in sorted(links):
        if not (ROOT / link).exists():
            problems.append(f"README 链接指向不存在的文件：{link}")
    for path in sorted(files):
        if path not in links:
            problems.append(f"笔记未被 README 索引：{path}")
    return problems


def main() -> int:
    problems = check()
    if problems:
        print(f"发现 {len(problems)} 个问题：")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"✅ README 索引与笔记文件一致（{len(note_files())} 篇笔记）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
