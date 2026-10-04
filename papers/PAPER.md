# PhD paper track (from README → submission)

Full publishable manuscript is `README.md` (§1–10: Abstract → Methods → E1–E5 → Checklist → DOME → 6 PhD extensions → References).

To turn into a journal submission:
1. Copy `README.md` → `papers/PAPER.md` and add author block + journal template (e.g., ONF, JCO Oncology Practice, BMJ Open).
2. Expand `data/answers.json` (170 Qs + rationales, seek ONS permissions for verbatim text; paraphrase + cite otherwise).
3. Replace H3 demo with real PRO data (PRO-CTCAE) or SEER-MHOS; keep seed + audit JSONs.
4. Add CBKB-170 LLM leaderboard (10 models, item analysis, DIF by section).
5. Monthly living-guideline diff job (NCCN/ASCO RSS → NLP diff → alert).
6. Mint Zenodo DOI from GitHub release; cite snapshot date 2026-10-04.

Ethics: no PHI, no local-repo code reused, minimal fair-use quoting, all live fetches timestamped.
