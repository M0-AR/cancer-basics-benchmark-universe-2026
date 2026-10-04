# Demo (60–90 seconds)

## What you will show
1. `pytest -q` → 2 passed
2. `python -m src.live_verify` → `results/live_snapshot.json` (3/4 live)
3. `python -m src.hidden_patterns` → H1 41.2%, H2 +25%, H3 ~0.58
4. Open `preview.html` in browser (hero + KPIs + beginner guide)
5. `docker compose up research` (one-command full run)

## Record it
```bash
# terminal + browser side-by-side, 1080p, mic on, captions on
bash docs/make_screenshots.sh
# record with your OS recorder (or: ffmpeg -f x11grab -s 1920x1080 -i :0 -t 90 docs/demo.mp4)
ls -lh docs/*.png docs/*.mp4 preview.html
```

## Files
- `preview.html` — beautiful offline preview (this repo's landing page)
- `docs/screenshot-hero.png` — browser hero (Playwright, below)
- `docs/screenshot-terminal.png` — terminal run (script below)
- `docs/demo.mp4` — 60–90s video (you record once, commit, README player lights up)
- GitHub renders `preview.html` via Pages, and `demo.mp4` inline in README.

## Screenshot automation
```bash
bash docs/make_screenshots.sh
```
