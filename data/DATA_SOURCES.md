# Data sources (all public, keyless, live-fetched 2026-10-04)

This repo verifies every claim against **live public data**. No private data. No keys.

| Source | URL / API | What we fetch | Status 2026-10-04 |
|---|---|---|---|
| ClinicalTrials.gov API v2 | `https://clinicaltrials.gov/api/v2/studies?query.term=cancer&filter.overallStatus=RECRUITING` | 5 recruiting oncology studies (NCTId, title, phase) | ok=True |
| OpenAlex | `https://api.openalex.org/works?search=oncology nursing symptom management&filter=from_publication_date:2024-01-01` | 5 works 2024+ (incl. ONS priorities 2024-27, AI precision) | ok=True |
| World Bank WDI | `https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json` | US GDP anchor for health-economics context | ok=True |
| CDC Socrata probe | `https://data.cdc.gov/api/views/metadata` | Negative control (expected fail, recorded honestly) | ok=False (recorded) |
| SEER / CDC USCS public-use | https://seer.cancer.gov/resources/ · https://www.cdc.gov/united-states-cancer-statistics/public-use/ (>42M cases since 2001, via SEER*Stat + DUA) | Manual step: request DUA, download, run `experiments/` | documented |
| NAACCR CiNA / data.gov SEER limited-use | https://www.naacccr.org/cina-public-use-data-set/ · https://catalog.data.gov/dataset/cancer-incidence-surveillance-epidemiology-and-end-results-seer-registries-limited-use | Manual step for second-primary + incidence validation | documented |
| NCCN / ASCO (web, no API) | NCCN Survivorship v3.2026; ASCO Survivorship Compendium; ONS 3E (2022) | Guideline drift (E5) — fetched via Agent-Reach websearch 2026-10-04 | quoted in README §2 |

Raw timestamped JSON: `results/live_snapshot.json` (200KB cap, audit-ready).
Re-run: `python -m src.live_verify`.

For SEER*Stat workflow (requires DUA — cannot be auto-fetched in Docker):
1. Request U.S. Cancer Statistics Database + SEER limited-use (see links above).
2. Export age-adjusted incidence/mortality 2016 vs 2024 for lung/breast/prostate/colorectal.
3. Drop CSVs in `data/` and run `python experiments/e2_epi_drift.py` (template below extends H2 with real rates).
