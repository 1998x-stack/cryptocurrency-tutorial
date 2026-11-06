# Portfolio improvement history

### 2026-11-06 06:14 UTC — ChatGPT Portfolio Iteration
- Run ID: 20261106T061431Z-4c82
- Repo / Base SHA: 1998x-stack/cryptocurrency-tutorial / b72f7b8ca03d5101e994c283def0fe4b4649fdd9
- Historical context: docs/improvements.md returned GitHub 404 on default branch (first initialization); PR search returned no prior PRs. No previous history to preserve.
- Product problem & expected user value: Chapter readers see inconsistent base spacing because the shared stylesheet's first rule is malformed; restoring the reset improves consistent layout without changing content.
- Engineering diagnosis & evidence: theme.css begins with an HTML comment, which is not a valid CSS comment; the leading text becomes part of the universal selector prelude, so the universal reset rule does not match. The remaining body rules remain intact.
- Options & decision: (1) CSS comment fix P2 score 5+3+5+5-1-1=16; (2) index.html file:// fetch fallback P2 score 5+2+5+3-3-2=10; (3) index error innerHTML safety P3 score 2+3+3+4-2-1=9. Choose isolated CSS fix.
- Changes: theme.css changes only first-line comment syntax; tests/test_theme_css.py adds stdlib regression guards. No dependency or public API changes.
- Validation: A: connector-side JavaScript assertions on GitHub-fetched old/new stylesheet verified invalid old prefix, valid new prefix, preserved remaining bytes, restored universal selector and retained mobile media query (6/6). D: python -m unittest discover -s tests -v authored but not run in a checkout; browser visual regression not run. No CI success claimed.
- Security & regression review: No secret, workflow, license, permission, deployment or production changes; scoped to static CSS and tests.
- Risk & rollback: Low risk; revert this PR if browser rendering differs. Browser E2E and full test suite remain outstanding.
- Follow-up: Run Python unittest in a checkout and browser comparison of a chapter on desktop/mobile; separately investigate file:// loading UX.
- Commit: pending (see PR head for verified SHA)
- PR: pending (see GitHub Draft PR)
