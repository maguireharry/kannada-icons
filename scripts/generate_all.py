#!/usr/bin/env python3
"""
Master SVG Generator and Metadata Builder for Kannada Icons Collection (500+ icons)
"""
import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(BASE_DIR, "svg")
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from icon_data import (
    script_typography,
    emblems_royalty,
    architecture_monuments,
    performing_arts_music,
    crafts_textiles_jewelry,
    wildlife_flora_fauna,
    geography_nature,
    cuisine_flavors,
    festivals_traditions_literature,
    modern_karnataka_lifestyle
)

MODULES = [
    ("script-typography", "Kannada Script & Aksharamale", "ಕನ್ನಡ ಲಿಪಿ ಮತ್ತು ಅಕ್ಷರಮಾಲೆ", script_typography),
    ("emblems-royalty", "Royal Dynasties & Historical Emblems", "ರಾಜಮನೆತನಗಳು ಮತ್ತು ಲಾಂಛನಗಳು", emblems_royalty),
    ("architecture-monuments", "Temple Architecture & Heritage Monuments", "ದೇವಾಲಯ ವಾಸ್ತುಶಿಲ್ಪ ಮತ್ತು ಸ್ಮಾರಕಗಳು", architecture_monuments),
    ("performing-arts-music", "Performing Arts, Folk Forms & Carnatic Music", "ರಂಗಕಲೆಗಳು, ಜಾನಪದ ಮತ್ತು ಸಂಗೀತ", performing_arts_music),
    ("crafts-textiles-jewelry", "Handicrafts, Textiles & Traditional Jewelry", "ಕರಕುಶಲ ವಸ್ತುಗಳು, ನೇಯ್ಗೆ ಮತ್ತು ಆಭರಣಗಳು", crafts_textiles_jewelry),
    ("wildlife-flora-fauna", "Karnataka Wildlife, Flora & Forest Sanctuary", "ವನ್ಯಜೀವಿಗಳು ಮತ್ತು ಸಸ್ಯಸಂಪತ್ತು", wildlife_flora_fauna),
    ("geography-nature", "Geography, Rivers, Hills & Coastline", "ಭೌಗೋಳಿಕ ಪರಿಸರ, ನದಿಗಳು, ಗಿರಿಶಿಖರಗಳು", geography_nature),
    ("cuisine-flavors", "Culinary Traditions, Dishes, Sweets & Flavors", "ಕರ್ನಾಟಕದ ಖಾದ್ಯ ವೈವಿಧ್ಯ ಮತ್ತು ಸಿಹಿತಿಂಡಿಗಳು", cuisine_flavors),
    ("festivals-traditions-literature", "Festivals, Traditions & Literature", "ಹಬ್ಬಗಳು, ಸಾಹಿತ್ಯ ಮತ್ತು ಸಂಸ್ಕೃತಿ", festivals_traditions_literature),
    ("modern-karnataka-lifestyle", "Modern Karnataka, Bengaluru Lifestyle & Heritage", "ಆಧುನಿಕ ಕರ್ನಾಟಕ, ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ಜನಜೀವನ", modern_karnataka_lifestyle),
]

def main():
    print("=" * 60)
    print("Generating Kannada Icons Collection (SVGs and Metadata)")
    print("=" * 60)

    all_icons = []
    seen_ids = set()
    category_summary = []

    for cat_slug, cat_title, cat_kn, module in MODULES:
        cat_icons = module.get_icons()
        cat_dir = os.path.join(SVG_DIR, cat_slug)
        os.makedirs(cat_dir, exist_ok=True)

        print(f"Processing '{cat_title}' ({len(cat_icons)} icons)...")

        for item in cat_icons:
            icon_id = item["id"]
            if icon_id in seen_ids:
                raise ValueError(f"Duplicate icon id detected: {icon_id}")
            seen_ids.add(icon_id)

            # Ensure category matches
            item["category_slug"] = cat_slug
            item["category_title"] = cat_title
            item["category_kannada"] = cat_kn

            # Relative paths
            item["svg_relative_path"] = f"svg/{cat_slug}/{icon_id}.svg"
            item["png_relative_path"] = f"png/{cat_slug}/{icon_id}.png"

            # Write individual SVG file
            svg_filepath = os.path.join(cat_dir, f"{icon_id}.svg")
            with open(svg_filepath, "w", encoding="utf-8") as f:
                f.write(item["svg"].strip() + "\n")

            all_icons.append(item)

        category_summary.append({
            "slug": cat_slug,
            "title": cat_title,
            "kannada": cat_kn,
            "count": len(cat_icons)
        })

    # Write master JSON
    json_path = os.path.join(BASE_DIR, "icons.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "collection": "Kannada & Karnataka Theme Icons",
            "kannada_collection": "ಕನ್ನಡ ಮತ್ತು ಕರ್ನಾಟಕ ಪರಂಪರೆ ಐಕಾನ್‌ಗಳ ಸಂಗ್ರಹ",
            "total_count": len(all_icons),
            "version": "1.0.0",
            "license": "MIT",
            "author": "Kannada Icons Community",
            "categories": category_summary,
            "icons": all_icons
        }, f, ensure_ascii=False, indent=2)

    print("-" * 60)
    print(f"Total Icons Generated: {len(all_icons)}")
    for cat in category_summary:
        print(f" - {cat['title']}: {cat['count']} icons")
    print(f"Master metadata saved to: {json_path}")
    print("=" * 60)

if __name__ == "__main__":
    main()
