"""Render right-pointing arrows with 6 different shaft lengths.

Arrow head is constant; only shaft length varies. Naming: annotation-arrow-1
(shortest) through annotation-arrow-6 (longest).
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path(__file__).parent / "annotations"
OUT_DIR.mkdir(parents=True, exist_ok=True)
DEVICE_SCALE = 2
YELLOW = "#F4D134"

# fixed head + canvas geometry (CSS px)
H = 256
PAD_X = 40       # horizontal margin for shadow
PAD_Y = 40       # vertical margin for shadow
HEAD_W = 140     # head length
HEAD_H = 176     # head full height
SHAFT_H = 60     # shaft thickness

# 6 shaft lengths (the flat shaft portion only, before head base)
SHAFT_LENGTHS = [60, 180, 300, 440, 600, 800]

HTML_TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
html, body {{ margin: 0; padding: 0; background: transparent; }}
body {{
  width: {w}px; height: {h}px;
  display: flex; align-items: center; justify-content: center;
}}
svg {{
  display: block;
  filter: drop-shadow(0 6px 14px rgba(0,0,0,0.55))
          drop-shadow(0 0 6px rgba(0,0,0,0.4));
}}
</style></head>
<body>
<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">
  <polygon
    points="{points}"
    fill="{yellow}"
    stroke="rgba(0,0,0,0.25)"
    stroke-width="1.5"
    stroke-linejoin="round"
  />
</svg>
</body></html>
"""


def make_html(shaft_len: int) -> tuple[str, int, int]:
    w = PAD_X * 2 + shaft_len + HEAD_W
    cy = H // 2
    x0 = PAD_X
    x1 = PAD_X + shaft_len            # shaft end / head base
    x_tip = x1 + HEAD_W
    shaft_top = cy - SHAFT_H // 2
    shaft_bot = cy + SHAFT_H // 2
    head_top = cy - HEAD_H // 2
    head_bot = cy + HEAD_H // 2

    points = " ".join(
        f"{px},{py}" for px, py in [
            (x0, shaft_top),
            (x1, shaft_top),
            (x1, head_top),
            (x_tip, cy),
            (x1, head_bot),
            (x1, shaft_bot),
            (x0, shaft_bot),
        ]
    )
    html = HTML_TEMPLATE.format(w=w, h=H, points=points, yellow=YELLOW)
    return html, w, H


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for i, shaft in enumerate(SHAFT_LENGTHS, start=1):
            html, w, h = make_html(shaft)
            ctx = browser.new_context(
                viewport={"width": w, "height": h},
                device_scale_factor=DEVICE_SCALE,
            )
            page = ctx.new_page()
            page.set_content(html, wait_until="load")
            out = OUT_DIR / f"annotation-arrow-{i}.png"
            page.screenshot(path=str(out), omit_background=True, full_page=False)
            ctx.close()
            print(f"wrote {out.name}  ({w}x{h})")
        browser.close()


if __name__ == "__main__":
    main()
