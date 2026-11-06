"""Regression guard for the shared chapter stylesheet (stdlib only)."""
from pathlib import Path
import re
import unittest

CSS = Path(__file__).resolve().parents[1] / "theme.css"


class ThemeCssTest(unittest.TestCase):
    def test_css_comment_and_reset_selector(self):
        text = CSS.read_text(encoding="utf-8")
        self.assertFalse(text.lstrip().startswith("<!--"), "HTML comments are not CSS comments")
        without_comments = re.sub(r"/\\*.*?\\*/", "", text, flags=re.S).lstrip()
        self.assertRegex(without_comments, r"^\\*\\s*\\{")

    def test_responsive_rules_remain(self):
        text = CSS.read_text(encoding="utf-8")
        self.assertIn("@media (max-width: 768px)", text)
        self.assertIn(".sidebar", text)


if __name__ == "__main__":
    unittest.main()
