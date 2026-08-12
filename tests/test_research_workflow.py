from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from _roamlib import approval_present, changelog_present, glossary_present, read_org  # noqa: E402


class ResearchWorkflowTests(unittest.TestCase):
    def test_org_contract_helpers(self):
        text = """:PROPERTIES:\n:ID: example-id\n:END:\n#+title: Example\n#+description: Example doc\n#+status: DRAFT\n#+filetags: :test:\n\n* Approval Table\n\n| Approval area | Required authority | State | Evidence required | Evidence reference |\n|---------------+--------------------+-------+-------------------+--------------------|\n| Research | Maintainer | PENDING | Review | None |\n\n* Changelog\n\n| Date | Change | Author or actor | Evidence |\n|------+--------+-----------------+----------|\n| 2026-08-12 | Added | test | fixture |\n\n* Footnotes and Glossary\n\n- Term: definition.\n"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "example.org"
            path.write_text(text, encoding="utf-8")
            doc = read_org(path)
        self.assertEqual(doc.doc_id, "example-id")
        self.assertEqual(doc.metadata["status"], "DRAFT")
        self.assertTrue(approval_present(text))
        self.assertTrue(changelog_present(text))
        self.assertTrue(glossary_present(text))

    def test_skill_manifest_matches_files(self):
        manifest = json.loads((ROOT / "skills" / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["skill_count"], len(manifest["skills"]))
        for skill in manifest["skills"]:
            self.assertTrue((ROOT / skill["path"]).is_file(), skill["path"])


if __name__ == "__main__":
    unittest.main()
