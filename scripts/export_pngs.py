#!/usr/bin/env python3
"""
High-resolution 512x512 Transparent PNG Exporter using Playwright & Chrome
"""
import os
import glob
import time
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(BASE_DIR, "svg")
PNG_DIR = os.path.join(BASE_DIR, "png")
os.makedirs(PNG_DIR, exist_ok=True)

def main():
    print("=" * 60)
    print("Exporting High-Resolution 512x512 Transparent PNGs...")
    print("=" * 60)

    # Find all categories
    categories = [d for d in os.listdir(SVG_DIR) if os.path.isdir(os.path.join(SVG_DIR, d))]
    categories.sort()

    total_exported = 0
    start_time = time.time()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
        )
        page = browser.new_page(viewport={"width": 512, "height": 512})

        for cat in categories:
            cat_svg_dir = os.path.join(SVG_DIR, cat)
            cat_png_dir = os.path.join(PNG_DIR, cat)
            os.makedirs(cat_png_dir, exist_ok=True)

            svg_files = sorted(glob.glob(os.path.join(cat_svg_dir, "*.svg")))
            print(f"Exporting '{cat}' ({len(svg_files)} icons)...")

            for svg_path in svg_files:
                filename = os.path.basename(svg_path)
                png_name = os.path.splitext(filename)[0] + ".png"
                png_path = os.path.join(cat_png_dir, png_name)

                with open(svg_path, "r", encoding="utf-8") as f:
                    svg_content = f.read()

                html = f"""<!DOCTYPE html>
<html>
<head><style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: transparent; overflow: hidden; }}
  #wrap {{ width: 512px; height: 512px; display: flex; align-items: center; justify-content: center; }}
  svg {{ width: 100%; height: 100%; display: block; }}
</style></head>
<body>
  <div id="wrap">{svg_content}</div>
</body>
</html>"""
                page.set_content(html)
                page.locator("#wrap").screenshot(path=png_path, omit_background=True)
                total_exported += 1

                if total_exported % 50 == 0:
                    elapsed = time.time() - start_time
                    rate = total_exported / elapsed
                    print(f"  Processed {total_exported} icons ({rate:.1f} icons/sec)...")

        browser.close()

    total_time = time.time() - start_time
    print("-" * 60)
    print(f"Successfully exported {total_exported} PNG icons in {total_time:.1f} seconds!")
    print(f"Output directory: {PNG_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
