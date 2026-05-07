"""Render L1-L6 and R1-R6 annotation labels in matching circle style."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path(__file__).parent / "annotations"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FONT_PATH = Path("C:/Github/Contrail/contrail-shopify-theme/assets/SquadaOne-Regular.ttf")
FONT_URL = FONT_PATH.resolve().as_uri()

SIZE = 512
DEVICE_SCALE = 2
MARGIN = 40
INNER = SIZE - MARGIN * 2
BORDER_W = 10

YELLOW = "#F4D134"
DARK_BG = "#21242D"
SHADOW = "0 6px 18px rgba(0,0,0,0.55)"

HTML_TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><style>
@font-face {{
  font-family: 'Squada One';
  src: url('{font_url}') format('truetype');
  font-weight: 400;
}}
html, body {{ margin: 0; padding: 0; background: transparent; }}
body {{
  width: {size}px; height: {size}px;
  display: flex; align-items: center; justify-content: center;
}}
.circle {{
  width: {inner}px; height: {inner}px;
  border-radius: 50%;
  background: {bg};
  border: {border}px solid {yellow};
  box-shadow: {shadow};
  display: flex; align-items: center; justify-content: center;
  font-family: 'Squada One', Impact, sans-serif;
  color: {yellow};
  font-size: {fs}px;
  line-height: 1;
  letter-spacing: 0.5px;
  padding-bottom: 4px;
  box-sizing: border-box;
}}
</style></head>
<body><div class="circle">{text}</div></body></html>
"""


def html_for(text: str) -> str:
    # 2-char letter+digit fits same as 2-digit numbers
    fs = int(INNER * 0.58)
    return HTML_TEMPLATE.format(
        font_url=FONT_URL, size=SIZE, inner=INNER, border=BORDER_W,
        yellow=YELLOW, bg=DARK_BG, shadow=SHADOW, fs=fs, text=text,
    )


def main():
    labels = [f"L{i}" for i in range(1, 7)] + [f"R{i}" for i in range(1, 7)]
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": SIZE, "height": SIZE},
            device_scale_factor=DEVICE_SCALE,
        )
        page = ctx.new_page()
        for label in labels:
            page.set_content(html_for(label), wait_until="load")
            page.evaluate("document.fonts.ready")
            out = OUT_DIR / f"annotation-label-{label}.png"
            page.screenshot(path=str(out), omit_background=True, full_page=False)
            print(f"wrote {out.name}")
        browser.close()


if __name__ == "__main__":
    main()
