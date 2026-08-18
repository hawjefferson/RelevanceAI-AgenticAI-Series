#!/usr/bin/env python3
"""Render the SVG diagrams to PNG at 2x via headless Chromium."""
import os
import re
import sys
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SVG = HERE
PNG = os.path.dirname(HERE)
os.makedirs(PNG, exist_ok=True)
SCALE = 2


def main(names=None):
    files = sorted(f for f in os.listdir(SVG) if f.endswith(".svg"))
    if names:
        files = [f for f in files if any(n in f for n in names)]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for f in files:
            src = os.path.join(SVG, f)
            svg = open(src, encoding="utf-8").read()
            m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
            w, h = int(m.group(1)), int(m.group(2))
            page = b.new_page(viewport={"width": w, "height": h},
                              device_scale_factor=SCALE)
            page.set_content(
                f'<html><body style="margin:0;padding:0;overflow:hidden">{svg}</body></html>',
                wait_until="load")
            page.wait_for_timeout(220)
            out = os.path.join(PNG, f[:-4] + ".png")
            page.screenshot(path=out, clip={"x": 0, "y": 0, "width": w, "height": h})
            page.close()
            print(f"  {os.path.basename(out)}  {w}x{h} @{SCALE}x  "
                  f"({os.path.getsize(out)/1024:.0f} KB)")
        b.close()


if __name__ == "__main__":
    print("Rendering PNGs:")
    main(sys.argv[1:] or None)
    print("Done.")
