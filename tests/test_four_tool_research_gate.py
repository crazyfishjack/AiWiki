from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / ".cursor"
    / "skills"
    / "wiki-research"
    / "scripts"
    / "four_tool_research.py"
)


spec = importlib.util.spec_from_file_location("four_tool_research", MODULE_PATH)
assert spec is not None
research = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["four_tool_research"] = research
spec.loader.exec_module(research)


class SourceGateTests(unittest.TestCase):
    def test_gate_records_include_kept_rejected_and_merged_sources(self) -> None:
        candidates = [
            research.Candidate("https://docs.example.com/a", "官方文档", "tavily", 0.8, ""),
            research.Candidate("https://docs.example.com/a", "官方文档重复", "exa", 1.0, ""),
            research.Candidate("https://example.com/blog", "普通博客", "exa", 1.0, ""),
            research.Candidate("https://quora.com/question", "问答页", "tavily", 0.9, ""),
            research.Candidate("https://news.example.com/weak", "低分新闻", "tavily", 0.2, ""),
        ]

        kept, records = research.apply_source_gate(candidates, tavily_min_score=0.4)

        self.assertEqual([item.url for item in kept], ["https://docs.example.com/a", "https://example.com/blog"])
        statuses = [(item.url, item.status, item.reason) for item in records]
        self.assertIn(("https://news.example.com/weak", "rejected", "score 低于 0.4"), statuses)
        self.assertIn(("https://quora.com/question", "rejected", "已知低质域名"), statuses)
        self.assertIn(("https://docs.example.com/a", "merged", "重复 URL，已合并到最高分结果"), statuses)

    def test_markdown_contains_gate_and_conflict_templates(self) -> None:
        candidates = [research.Candidate("https://docs.example.com/a", "官方文档", "tavily", 0.8, "")]
        records = [
            research.SourceGateRecord(
                url="https://docs.example.com/a",
                title="官方文档",
                source_tool="tavily",
                score=0.8,
                status="kept",
                source_grade="A",
                reason="官方文档",
                next_step="进入精读",
            )
        ]

        markdown = research.build_markdown(
            query="测试主题",
            mode="standard",
            candidates=candidates,
            reads=[],
            notes=[],
            stats={"candidate_count": 1, "deep_read_count": 0, "mode": "standard"},
            excerpt_char_limit=2000,
            gate_records=records,
        )

        self.assertIn("## 信源质量门控记录", markdown)
        self.assertIn("## 跨源矛盾检测结论", markdown)
        self.assertIn("A/B → `source-quality: high`", markdown)


if __name__ == "__main__":
    unittest.main()
