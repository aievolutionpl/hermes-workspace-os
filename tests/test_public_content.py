import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
NEW_SKILLS = ['routing', 'verification', 'handoff', 'automation', 'delegation', 'hygiene']
PUBLIC = [ROOT / 'README.md', *sorted((ROOT / 'docs').glob('*.md')),
          *sorted((ROOT / 'templates').glob('*.md')),
          *sorted((ROOT / 'examples').glob('*.md')),
          *(ROOT / 'skills' / ('workflow-' + name) / 'SKILL.md' for name in NEW_SKILLS)]

class PublicContentTests(unittest.TestCase):
    def test_local_links(self):
        for file in PUBLIC:
            for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
                target = unquote(target.split('#', 1)[0])
                if not target or re.match(r'^[a-z]+:', target):
                    continue
                with self.subTest(file=file.relative_to(ROOT), target=target):
                    self.assertTrue((file.parent / target).exists())

    def test_modules(self):
        modules = sorted((ROOT / 'skills/hermes-workspace-os/modules').glob('[0-9][0-9]-*.md'))
        self.assertEqual([p.name[:2] for p in modules], [f'{n:02}' for n in range(1, 20)])
        self.assertNotIn('15 modułów', (ROOT / 'README.md').read_text(encoding='utf-8'))
        for path in [ROOT / 'README.md', ROOT / 'skills/hermes-workspace-os/SKILL.md']:
            self.assertNotIn('60 minut', path.read_text(encoding='utf-8'))

    def test_skill_frontmatter_and_steps(self):
        for name in NEW_SKILLS:
            path = ROOT / 'skills' / ('workflow-' + name) / 'SKILL.md'
            text = path.read_text(encoding='utf-8')
            with self.subTest(name=name):
                self.assertRegex(text, r'^---\nname: workflow-' + name + r'\ndescription: "Use when [^\n]+"\n---\n')
                self.assertGreaterEqual(len(re.findall(r'^\d+\. ', text, re.M)), 4)

    def test_templates_and_example(self):
        task = (ROOT / 'templates/task.md').read_text(encoding='utf-8')
        handoff = (ROOT / 'templates/handoff.md').read_text(encoding='utf-8')
        for term in ['Cel:', 'Zakres:', 'Kryteria akceptacji:', 'Weryfikacja:', 'Granice:']:
            self.assertIn(term, task)
        for term in ['Stan:', 'Artefakty:', 'Dowody:', 'Następna akcja']:
            self.assertIn(term, handoff)
        self.assertIn('fikcyjne', (ROOT / 'examples/fictional-handoff.md').read_text(encoding='utf-8').lower())

    def test_privacy_patterns(self):
        patterns = [r'/home/aibot', r'/mnt/[cd]/Users/', r'(?i)\bchris\b',
                    r'(?i)\b(?:api[_-]?key|password|secret)\s*[:=]\s*[\w-]{12,}',
                    r'\b[A-Za-z0-9._%+-]+@(?!example\.(?:com|org|net)\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b']
        for path in PUBLIC:
            for pattern in patterns:
                with self.subTest(file=path.relative_to(ROOT), pattern=pattern):
                    self.assertNotRegex(path.read_text(encoding='utf-8'), pattern)

if __name__ == '__main__':
    unittest.main()
