"""守护 README 索引与笔记文件的一致性（与 CI 同一套逻辑）。"""

from __future__ import annotations

from pathlib import Path

from scripts.check_links import ROOT, check, note_files, readme_links


def test_index_and_notes_are_consistent():
    assert check() == []


def test_there_is_at_least_one_note():
    assert note_files()


def test_all_readme_links_are_note_paths():
    links = readme_links((ROOT / "README.md").read_text(encoding="utf-8"))
    assert links, "README 应当至少索引一篇笔记"
    for link in links:
        assert link.startswith("notes/") and link.endswith(".md")


def test_detects_missing_file(tmp_path: Path):
    """校验器确实能发现问题（避免它永远返回空列表）。"""
    from scripts import check_links

    original_readme = check_links.README
    try:
        fake = tmp_path / "README.md"
        fake.write_text("见 [x](notes/nope/missing.md)", encoding="utf-8")
        check_links.README = fake
        assert check_links.check()  # 非空即发现问题
    finally:
        check_links.README = original_readme
