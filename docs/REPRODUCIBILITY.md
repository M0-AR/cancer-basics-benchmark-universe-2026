# Reproducibility (Turing Way + DOME)

## One-command reproduction
```bash
docker compose build
docker compose up research   # pytest + live_verify + hidden_patterns
docker compose up lab        # Jupyter on :8888
```

Without Docker:
```bash
pip install -r requirements.txt
pytest -q
python -m src.live_verify
python -m src.hidden_patterns
```

## Determinism
- Seed fixed: 2026 (`numpy.random.default_rng(2026)` in `src/hidden_patterns.py`).
- Timestamps: UTC ISO8601 in `results/*.json`.
- Live APIs: keyless, User-Agent identified, 10–20s timeouts; failures recorded, never hidden (see CDC probe ok=False).
- Textbook grounding: TOC counts exact (6+8+14+6=34); H3 demo is **labeled synthetic teaching demo**; real validation = cited cluster literature + NCCN guidance.

## DOME checklist
- **Data:** public/keyless; snapshot in `results/live_snapshot.json`; SEER DUA path documented for follow-up PhD work.
- **Optimization:** no training; demo correlations illustrative.
- **Model:** no fitted ML; future work = Cox/logistic on SEER limited-use + TCGA (needs DUA/HPC).
- **Evaluation:** pytest (counts + pipeline smoke) + live ok-flags. Not a clinical guideline.
