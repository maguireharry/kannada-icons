"""
Category 5: Heritage Textiles, Handicrafts, Jewelry & GI Products (50 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "crafts-textiles-jewelry",
            "tags": ["craft", "textile", "handicraft", "jewelry", "mysore", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Mysore Silk Saree Folded
    add("craft_01_mysore_silk_saree", "Mysore Silk Saree Fold", "ಮೈಸೂರು ರೇಷ್ಮೆ ಸೀರೆ", ["silk", "saree", "mysore", "zari"], f"""
    <!-- Folded rich silk saree with golden border -->
    <rect x="14" y="20" width="36" height="28" rx="3" fill="{PURPLE}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Gold Zari Border Band -->
    <rect x="14" y="20" width="10" height="28" rx="2" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <line x1="19" y1="20" x2="19" y2="48" stroke="{YELLOW}" stroke-width="1" stroke-dasharray="2 1"/>
    <!-- Fold creases -->
    <line x1="24" y1="32" x2="50" y2="32" stroke="{GOLD}" stroke-width="1.5"/>
    <line x1="24" y1="40" x2="50" y2="40" stroke="{GOLD}" stroke-width="1.5"/>
    <circle cx="36" cy="26" r="1.5" fill="{GOLD}"/>
    """)

    # 2. Mysore Silk Pallu
    add("craft_02_mysore_silk_pallu", "Mysore Silk Woven Pallu", "ರೇಷ್ಮೆ ಸೀರೆಯ ಪಲ್ಲು", ["pallu", "zari", "motifs"], f"""
    <rect x="12" y="14" width="40" height="36" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <!-- Rich Golden Zari bands -->
    <rect x="12" y="14" width="40" height="8" fill="{GOLD}"/>
    <rect x="12" y="42" width="40" height="8" fill="{GOLD}"/>
    <!-- Paisley / Mango motifs in pallu center -->
    <circle cx="22" cy="30" r="3" fill="{YELLOW}"/>
    <circle cx="32" cy="30" r="3" fill="{YELLOW}"/>
    <circle cx="42" cy="30" r="3" fill="{YELLOW}"/>
    <!-- Fringe / Tassels -->
    <line x1="16" y1="50" x2="16" y2="56" stroke="{GOLD}" stroke-width="2"/>
    <line x1="24" y1="50" x2="24" y2="56" stroke="{GOLD}" stroke-width="2"/>
    <line x1="32" y1="50" x2="32" y2="56" stroke="{GOLD}" stroke-width="2"/>
    <line x1="40" y1="50" x2="40" y2="56" stroke="{GOLD}" stroke-width="2"/>
    <line x1="48" y1="50" x2="48" y2="56" stroke="{GOLD}" stroke-width="2"/>
    """)

    # 3. Ilkal Saree Tope Teni
    add("craft_03_ilkal_saree_tope_teni", "Ilkal Saree Tope Teni Pallu", "ಇಳಕಲ್ ಸೀರೆ ತೋಪೆ ತೇನಿ", ["ilkal", "topeteni", "temple", "weaving"], f"""
    <rect x="12" y="16" width="40" height="34" fill="{RED}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Tope Teni triangular temple motifs in white and red -->
    <polygon points="18,34 22,22 26,34" fill="{WHITE}" stroke="{RED}" stroke-width="1"/>
    <polygon points="26,34 30,22 34,34" fill="{WHITE}" stroke="{RED}" stroke-width="1"/>
    <polygon points="34,34 38,22 42,34" fill="{WHITE}" stroke="{RED}" stroke-width="1"/>
    <!-- Kasuti embroidery stripes on border -->
    <line x1="12" y1="42" x2="52" y2="42" stroke="{YELLOW}" stroke-width="2"/>
    <line x1="12" y1="46" x2="52" y2="46" stroke="{YELLOW}" stroke-width="2"/>
    """)

    # 4. Molakalmuru Silk Saree
    add("craft_04_molakalmuru_silk_saree", "Molakalmuru Silk Saree Border", "ಮೊಳಕಾಲ್ಮುರು ರೇಷ್ಮೆ ಸೀರೆ", ["molakalmuru", "chitradurga", "border"], f"""
    <rect x="14" y="16" width="36" height="36" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <!-- Double border with geometric bird / temple peaks -->
    <polygon points="18,24 22,18 26,24" fill="{GOLD}"/>
    <polygon points="26,24 30,18 34,24" fill="{GOLD}"/>
    <polygon points="34,24 38,18 42,24" fill="{GOLD}"/>
    <polygon points="42,24 46,18 50,24" fill="{GOLD}"/>
    <line x1="14" y1="28" x2="50" y2="28" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="32" cy="40" r="4" fill="{GOLD}"/>
    """)

    # 5. Channapatna Rocking Horse
    add("craft_05_channapatna_rocking_horse", "Channapatna Wooden Rocking Horse", "ಚನ್ನಪಟ್ಟಣದ ಮರದ ಕುದುರೆ", ["channapatna", "toy", "horse", "lacquer"], f"""
    <!-- Curved rocking runner -->
    <path d="M 10 50 Q 32 60 54 50" stroke="{RED}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <!-- Horse Body -->
    <ellipse cx="32" cy="36" rx="14" ry="8" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <!-- Horse Head & Mane -->
    <path d="M 40 32 L 46 20 C 48 16 46 12 42 14 L 38 22 Z" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="42" cy="18" r="1.5" fill="{WHITE}"/>
    <!-- Rocking struts -->
    <line x1="22" y1="42" x2="18" y2="53" stroke="{GREEN}" stroke-width="2.5"/>
    <line x1="42" y1="42" x2="46" y2="53" stroke="{GREEN}" stroke-width="2.5"/>
    """)

    # 6. Channapatna Spinning Top (Buguri)
    add("craft_06_channapatna_spinning_top", "Channapatna Wooden Top (Buguri)", "ಚನ್ನಪಟ್ಟಣದ ಬುಗುರಿ", ["buguri", "top", "wooden", "lacquer"], f"""
    <!-- Lathe turned top with bright circular colored bands -->
    <polygon points="32,54 18,24 46,24" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <!-- Color bands -->
    <path d="M 21 30 L 43 30" stroke="{RED}" stroke-width="3"/>
    <path d="M 24 38 L 40 38" stroke="{GREEN}" stroke-width="3"/>
    <path d="M 28 46 L 36 46" stroke="{RED}" stroke-width="2.5"/>
    <!-- Rounded crown & spindle -->
    <path d="M 18 24 C 18 16 46 16 46 24 Z" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <line x1="32" y1="16" x2="32" y2="8" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
    <!-- Steel tip -->
    <circle cx="32" cy="56" r="2" fill="{SILVER}"/>
    """)

    # 7. Channapatna Stacking Rings
    add("craft_07_channapatna_stacking_rings", "Channapatna Rainbow Stacker", "ಚನ್ನಪಟ್ಟಣ ಬಣ್ಣದ ರಿಂಗುಗಳ ಆಟಿಕೆ", ["stacker", "rings", "rainbow"], f"""
    <rect x="12" y="50" width="40" height="6" rx="2" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Center spindle -->
    <line x1="32" y1="50" x2="32" y2="14" stroke="{BROWN}" stroke-width="3"/>
    <!-- Graduated color rings -->
    <ellipse cx="32" cy="46" rx="18" ry="4" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
    <ellipse cx="32" cy="38" rx="15" ry="3.5" fill="{ORANGE}" stroke="{DARK}" stroke-width="1"/>
    <ellipse cx="32" cy="30" rx="12" ry="3" fill="{YELLOW}" stroke="{DARK}" stroke-width="1"/>
    <ellipse cx="32" cy="22" rx="9" ry="2.5" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
    <!-- Top ball topper -->
    <circle cx="32" cy="14" r="5" fill="{SKY_BLUE}" stroke="{DARK}" stroke-width="1"/>
    """)

    # 8. Channapatna Toy Train
    add("craft_08_channapatna_toy_train", "Channapatna Wooden Toy Train", "ಚನ್ನಪಟ್ಟಣದ ಮರದ ರೈಲು", ["train", "wooden", "toy"], f"""
    <!-- Engine Body -->
    <rect x="14" y="24" width="24" height="18" rx="3" fill="{RED}" stroke="{SLATE}" stroke-width="2"/>
    <rect x="30" y="16" width="16" height="26" rx="3" fill="{YELLOW}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Chimney / Funnel -->
    <rect x="18" y="16" width="6" height="8" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Wheels -->
    <circle cx="20" cy="46" r="5" fill="{YELLOW}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="32" cy="46" r="5" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="44" cy="46" r="5" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Headlight -->
    <circle cx="12" cy="32" r="2" fill="{GOLD}"/>
    """)

    # 9. Channapatna Wooden Beads
    add("craft_09_channapatna_wooden_beads", "Channapatna Lacquer Bead Chain", "ಚನ್ನಪಟ್ಟಣದ ಮರದ ಮಣಿಗಳು", ["beads", "lacquer", "necklace"], f"""
    <!-- String of glossy beads in primary Karnataka colors -->
    <circle cx="16" cy="32" r="5" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="24" cy="24" r="5" fill="{YELLOW}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="32" cy="18" r="6" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="40" cy="24" r="5" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="48" cy="32" r="5" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="32" cy="44" r="7" fill="{GOLD}" stroke="{DARK}" stroke-width="2"/>
    <path d="M 12 34 C 18 48 46 48 52 34" stroke="{BROWN}" stroke-width="1.5" fill="none"/>
    """)

    # 10. Channapatna Pen Stand
    add("craft_10_channapatna_pen_stand", "Channapatna Wooden Pen Stand", "ಚನ್ನಪಟ್ಟಣದ ಲೇಖನಿ ಪಾತ್ರೆ", ["penstand", "lathe", "wooden"], f"""
    <rect x="20" y="24" width="24" height="28" rx="4" fill="{YELLOW}" stroke="{SLATE}" stroke-width="2"/>
    <line x1="20" y1="32" x2="44" y2="32" stroke="{RED}" stroke-width="3"/>
    <line x1="20" y1="40" x2="44" y2="40" stroke="{GREEN}" stroke-width="3"/>
    <!-- Pens sticking out -->
    <line x1="26" y1="12" x2="26" y2="24" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="34" y1="8" x2="32" y2="24" stroke="{SKY_BLUE}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="40" y1="14" x2="38" y2="24" stroke="{DARK}" stroke-width="2.5" stroke-linecap="round"/>
    """)

    # 11-50 Crafts, Textiles, Jewelry batch
    crafts_batch = [
        ("craft_11_bidriware_vase", "Bidriware Silver Inlay Vase", "ಬಿದರಿ ಹೂದಾನಿ", ["bidriware", "silver", "bidar", "vase"], f"""
        <!-- Black zinc alloy vase with fine silver floral inlay -->
        <path d="M 24 16 L 40 16 L 36 26 C 46 32 46 44 38 52 L 26 52 C 18 44 18 32 28 26 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Fine silver floral vines inlaid -->
        <circle cx="32" cy="38" r="4" fill="{SILVER}" stroke="{WHITE}" stroke-width="1"/>
        <path d="M 26 36 Q 32 30 38 36" stroke="{SILVER}" stroke-width="1.5" fill="none"/>
        <line x1="24" y1="16" x2="40" y2="16" stroke="{SILVER}" stroke-width="2"/>
        """),
        ("craft_12_bidriware_floral_plate", "Bidriware Silver Plate (Thali)", "ಬಿದರಿ ಬೆಳ್ಳಿ ತಟ್ಟೆ", ["bidriware", "plate", "silver", "thali"], f"""
        <circle cx="32" cy="32" r="22" fill="{DARK}" stroke="{SLATE}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="16" stroke="{SILVER}" stroke-width="1.5" stroke-dasharray="2 2" fill="none"/>
        <!-- Central silver rosette -->
        <circle cx="32" cy="32" r="5" fill="{SILVER}"/>
        <circle cx="32" cy="32" r="2" fill="{WHITE}"/>
        <!-- 8 radiating floral leaves -->
        <circle cx="32" cy="22" r="2" fill="{SILVER}"/>
        <circle cx="32" cy="42" r="2" fill="{SILVER}"/>
        <circle cx="22" cy="32" r="2" fill="{SILVER}"/>
        <circle cx="42" cy="32" r="2" fill="{SILVER}"/>
        """),
        ("craft_13_bidriware_hookah_base", "Bidriware Hookah Base", "ಬಿದರಿ ಹುಕ್ಕಾ ಪಾತ್ರೆ", ["bidriware", "hookah", "antique"], f"""
        <!-- Bell-shaped blackened metal vessel -->
        <path d="M 28 14 L 36 14 L 36 24 L 46 44 C 48 48 44 52 38 52 L 26 52 C 20 52 16 48 18 44 L 28 24 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="38" r="4" fill="{SILVER}"/>
        <line x1="24" y1="46" x2="40" y2="46" stroke="{SILVER}" stroke-width="1.5"/>
        """),
        ("craft_14_bidriware_silver_box", "Bidriware Silver Trinket Box", "ಬಿದರಿ ಆಭರಣ ಪೆಟ್ಟಿಗೆ", ["bidriware", "box", "silver"], f"""
        <rect x="14" y="24" width="36" height="22" rx="3" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Silver geometric lattice on lid -->
        <rect x="14" y="20" width="36" height="6" rx="2" fill="{SLATE}" stroke="{SILVER}" stroke-width="1.5"/>
        <line x1="20" y1="32" x2="44" y2="32" stroke="{SILVER}" stroke-width="1.5"/>
        <line x1="20" y1="38" x2="44" y2="38" stroke="{SILVER}" stroke-width="1.5"/>
        <circle cx="32" cy="35" r="2" fill="{WHITE}"/>
        """),
        ("craft_15_mysore_rosewood_inlay_panel", "Mysore Rosewood Inlay Panel", "ಮೈಸೂರು ಬೀಟೆ ಮರದ ಕಲಾಕೃತಿ", ["rosewood", "inlay", "mysore", "ivory"], f"""
        <rect x="12" y="14" width="40" height="36" rx="3" fill="{BROWN}" stroke="{DARK}" stroke-width="2.5"/>
        <!-- Wood grain / border inlay -->
        <rect x="16" y="18" width="32" height="28" stroke="{CREAM}" stroke-width="1.5" fill="none"/>
        <!-- Inlaid ivory-look Elephant in center -->
        <circle cx="32" cy="30" r="6" fill="{CREAM}"/>
        <path d="M 32 30 L 38 38 M 28 36 L 28 42 M 34 36 L 34 42" stroke="{CREAM}" stroke-width="2"/>
        """),
        ("craft_16_mysore_rosewood_elephant", "Mysore Rosewood Elephant Figurine", "ಮೈಸೂರು ಬೀಟೆ ಮರದ ಆನೆ", ["rosewood", "elephant", "statue"], f"""
        <ellipse cx="32" cy="34" rx="16" ry="11" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- White bone / ivory tusks -->
        <path d="M 44 34 Q 50 32 48 26" stroke="{WHITE}" stroke-width="2.5" fill="none"/>
        <!-- Trunk -->
        <path d="M 44 32 C 48 38 46 44 42 44" stroke="{BROWN}" stroke-width="3" fill="none"/>
        <rect x="22" y="42" width="5" height="12" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="36" y="42" width="5" height="12" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("craft_17_kinhal_kamadhenu_cow", "Kinhal Painted Cow (Kamadhenu)", "ಕಿನ್ನಾಳದ ಕಾಮಧೇನು", ["kinhal", "kamadhenu", "cow", "painted"], f"""
        <ellipse cx="30" cy="36" rx="14" ry="10" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Horns & Ears -->
        <path d="M 42 22 L 40 14 M 46 22 L 48 14" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="42" cy="26" r="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Painted decorative floral saddle blanket -->
        <rect x="24" y="30" width="12" height="10" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="30" cy="35" r="2" fill="{YELLOW}"/>
        """),
        ("craft_18_kinhal_wooden_parrot", "Kinhal Lacquer Green Parrot", "ಕಿನ್ನಾಳದ ಮರದ ಗಿಳಿ", ["kinhal", "parrot", "green", "wooden"], f"""
        <ellipse cx="30" cy="32" rx="10" ry="16" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Red curved beak -->
        <path d="M 38 22 Q 46 24 40 30 Z" fill="{RED}"/>
        <circle cx="34" cy="22" r="2" fill="{YELLOW}"/>
        <circle cx="34" cy="22" r="1" fill="{DARK}"/>
        <!-- Long tail feather -->
        <path d="M 24 44 L 14 58 L 20 48 Z" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("craft_19_kinhal_cradle", "Kinhal Festive Cradle (Thottilu)", "ಕಿನ್ನಾಳದ ತೊಟ್ಟಿಲು", ["kinhal", "cradle", "thottilu"], f"""
        <!-- Hanging swing cradle with painted peacocks -->
        <rect x="16" y="32" width="32" height="16" rx="3" fill="{YELLOW}" stroke="{RED}" stroke-width="2"/>
        <line x1="20" y1="12" x2="20" y2="32" stroke="{GOLD}" stroke-width="2"/>
        <line x1="44" y1="12" x2="44" y2="32" stroke="{GOLD}" stroke-width="2"/>
        <line x1="16" y1="12" x2="48" y2="12" stroke="{BROWN}" stroke-width="3"/>
        <circle cx="32" cy="40" r="3" fill="{RED}"/>
        """),
        ("craft_20_sandalwood_carved_elephant", "Sandalwood Jali Carved Elephant", "ಗಂಧದ ಮರದ ಕೆತ್ತನೆಯ ಆನೆ", ["sandalwood", "elephant", "jali", "carving"], f"""
        <ellipse cx="32" cy="34" rx="16" ry="12" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Jali perforations inside body revealing baby elephant -->
        <circle cx="28" cy="34" r="2" fill="{BROWN}"/>
        <circle cx="36" cy="34" r="2" fill="{BROWN}"/>
        <circle cx="32" cy="38" r="2" fill="{BROWN}"/>
        <circle cx="32" cy="30" r="2" fill="{BROWN}"/>
        <!-- Ornate caparison -->
        <path d="M 22 28 Q 32 24 42 28" stroke="{RED}" stroke-width="2" fill="none"/>
        """),
        ("craft_21_sandalwood_carved_fan", "Sandalwood Carved Fan (Bisoorike)", "ಗಂಧದ ಬೀಸಣಿಗೆ", ["sandalwood", "fan", "bisoorike"], f"""
        <!-- Fan of perforated sandalwood blades radiating -->
        <path d="M 14 42 C 14 18 50 18 50 42 Z" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Slats radiating -->
        <line x1="32" y1="42" x2="20" y2="22" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="42" x2="32" y2="18" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="42" x2="44" y2="22" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="44" r="3" fill="{RED}"/>
        <line x1="32" y1="44" x2="32" y2="56" stroke="{BROWN}" stroke-width="3"/>
        """),
        ("craft_22_sandalwood_chariot", "Sandalwood Miniature Chariot", "ಗಂಧದ ಮರದ ಪುಟ್ಟ ರಥ", ["sandalwood", "miniature", "ratha"], f"""
        <polygon points="32,10 20,26 44,26" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <rect x="22" y="26" width="20" height="16" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="22" cy="46" r="5" stroke="{BROWN}" stroke-width="2" fill="{CREAM}"/>
        <circle cx="42" cy="46" r="5" stroke="{BROWN}" stroke-width="2" fill="{CREAM}"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        """),
        ("craft_23_mysore_ganjifa_card", "Mysore Ganjifa Circular Card", "ಮೈಸೂರು ಗಂಜೀಫಾ ಎಲೆ", ["ganjifa", "playingcard", "mysore", "circular"], f"""
        <!-- Round painted traditional card -->
        <circle cx="32" cy="32" r="22" fill="{CREAM}" stroke="{RED}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="18" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
        <!-- Royal figure / deity motif in center -->
        <circle cx="32" cy="26" r="4" fill="{GOLD}"/>
        <path d="M 26 38 Q 32 32 38 38" stroke="{RED}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="42" r="2" fill="{GREEN}"/>
        """),
        ("craft_24_ganjifa_matsya_card", "Ganjifa Matsya Avatar Card", "ಗಂಜೀಫಾ ಮತ್ಸ್ಯಾವತಾರ ಎಲೆ", ["ganjifa", "matsya", "fish", "avatar"], f"""
        <circle cx="32" cy="32" r="20" fill="rgba(2,132,199,0.15)" stroke="{GOLD}" stroke-width="2"/>
        <!-- Fish avatar silhouette -->
        <path d="M 20 32 C 26 22 38 22 44 32 C 38 42 26 42 20 32 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <polygon points="18,32 10,26 10,38" fill="{GOLD}"/>
        <circle cx="38" cy="30" r="1.5" fill="{RED}"/>
        """),
        ("craft_25_kasuti_gopuram_motif", "Kasuti Embroidery Gopuram Motif", "ಕಸೂತಿ ಕಲೆಯ ಗೋಪುರ", ["kasuti", "embroidery", "gopuram", "dharwad"], f"""
        <!-- Geometric cross-stitch temple gopuram -->
        <path d="M 32 12 L 26 20 L 38 20 Z" stroke="{RED}" stroke-width="2" fill="none"/>
        <path d="M 24 20 L 20 28 L 44 28 L 40 20" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 18 28 L 14 38 L 50 38 L 46 28" stroke="{GREEN}" stroke-width="2" fill="none"/>
        <rect x="14" y="38" width="36" height="12" stroke="{PURPLE}" stroke-width="2" fill="none"/>
        <line x1="32" y1="38" x2="32" y2="50" stroke="{RED}" stroke-width="2"/>
        """),
        ("craft_26_kasuti_lotus_motif", "Kasuti Sacred Lotus (Kamala)", "ಕಸೂತಿ ಕಮಲ ಚಿತ್ತಾರ", ["kasuti", "lotus", "kamala", "embroidery"], f"""
        <!-- 8-petal geometric needlework lotus -->
        <polygon points="32,16 36,26 46,26 38,32 41,42 32,36 23,42 26,32 18,26 28,26" stroke="{RED}" stroke-width="2" fill="rgba(200,16,46,0.15)"/>
        <circle cx="32" cy="31" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("craft_27_kasuti_chariot_motif", "Kasuti Embroidery Chariot (Theru)", "ಕಸೂತಿ ತೇರು (ರಥ)", ["kasuti", "theru", "chariot", "needlework"], f"""
        <path d="M 32 12 L 22 28 L 42 28 Z" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <rect x="20" y="28" width="24" height="14" stroke="{RED}" stroke-width="2" fill="none"/>
        <!-- Cross stitch wheels -->
        <circle cx="20" cy="46" r="4" stroke="{GREEN}" stroke-width="2" fill="none"/>
        <circle cx="44" cy="46" r="4" stroke="{GREEN}" stroke-width="2" fill="none"/>
        """),
        ("craft_28_kasuti_peacock_motif", "Kasuti Geometric Peacock", "ಕಸೂತಿ ನವಿಲು ಚಿತ್ತಾರ", ["kasuti", "peacock", "motifs"], f"""
        <circle cx="24" cy="26" r="4" stroke="{GREEN}" stroke-width="2" fill="none"/>
        <path d="M 28 26 L 36 34 L 28 42 L 20 34 Z" stroke="{RED}" stroke-width="2" fill="none"/>
        <!-- Geometric stepped tail -->
        <path d="M 36 34 L 46 24 M 36 34 L 50 34 M 36 34 L 46 44" stroke="{SKY_BLUE}" stroke-width="2"/>
        <line x1="24" y1="42" x2="24" y2="52" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("craft_29_kasuti_tulsi_vrindavan", "Kasuti Tulsi Vrindavan Motif", "ಕಸೂತಿ ತುಳಸಿ ಕಟ್ಟೆ", ["kasuti", "tulsi", "embroidery"], f"""
        <rect x="22" y="32" width="20" height="18" stroke="{BROWN}" stroke-width="2" fill="none"/>
        <line x1="18" y1="50" x2="46" y2="50" stroke="{SLATE}" stroke-width="2"/>
        <!-- Holy Tulsi plant on top -->
        <line x1="32" y1="32" x2="32" y2="18" stroke="{GREEN}" stroke-width="2"/>
        <circle cx="28" cy="22" r="2" fill="{GREEN}"/>
        <circle cx="36" cy="22" r="2" fill="{GREEN}"/>
        <circle cx="32" cy="16" r="2" fill="{GREEN}"/>
        """),
        ("craft_30_lambani_mirror_patch", "Lambani Banjara Mirror Patch", "ಲಂಬಾಣಿ ಕನ್ನಡಿ ಕಸೂತಿ", ["lambani", "banjara", "mirror", "tribal"], f"""
        <!-- Real reflective mirror circle with heavy colorful herringbone embroidery -->
        <circle cx="32" cy="32" r="22" stroke="{RED}" stroke-width="3" fill="rgba(234,88,12,0.1)"/>
        <circle cx="32" cy="32" r="14" stroke="{YELLOW}" stroke-width="3" fill="{SILVER}"/>
        <circle cx="32" cy="32" r="10" fill="{WHITE}"/>
        <!-- Embroidered chevron points radiating -->
        <polygon points="32,6 30,10 34,10" fill="{BLUE}"/>
        <polygon points="32,58 30,54 34,54" fill="{BLUE}"/>
        <polygon points="6,32 10,30 10,34" fill="{BLUE}"/>
        <polygon points="58,32 54,30 54,34" fill="{BLUE}"/>
        """),
        ("craft_31_lambani_cowrie_border", "Lambani Cowrie Shell Border", "ಲಂಬಾಣಿ ಕವಡೆ ಸರಪಳಿ", ["cowrie", "shell", "lambani"], f"""
        <!-- Row of oval cowrie shells with center slit -->
        <ellipse cx="20" cy="32" rx="6" ry="10" fill="{CREAM}" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="20" y1="26" x2="20" y2="38" stroke="{BROWN}" stroke-width="1.5"/>
        <ellipse cx="32" cy="32" rx="6" ry="10" fill="{CREAM}" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="32" y1="26" x2="32" y2="38" stroke="{BROWN}" stroke-width="1.5"/>
        <ellipse cx="44" cy="32" rx="6" ry="10" fill="{CREAM}" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="44" y1="26" x2="44" y2="38" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="10" y1="18" x2="54" y2="18" stroke="{RED}" stroke-width="2"/>
        <line x1="10" y1="46" x2="54" y2="46" stroke="{RED}" stroke-width="2"/>
        """),
        ("craft_32_lambani_coin_tassel", "Lambani Coin Tassel", "ಲಂಬಾಣಿ ನಾಣ್ಯದ ಗೊಂಚಲು", ["tassel", "coins", "lambani"], f"""
        <circle cx="32" cy="18" r="4" fill="{RED}"/>
        <!-- Wool strands -->
        <line x1="26" y1="22" x2="22" y2="42" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="32" y1="22" x2="32" y2="42" stroke="{RED}" stroke-width="2"/>
        <line x1="38" y1="22" x2="42" y2="42" stroke="{GREEN}" stroke-width="2"/>
        <!-- Brass coin bells at bottom -->
        <circle cx="22" cy="46" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <circle cx="32" cy="46" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <circle cx="42" cy="46" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        """),
        ("craft_33_navalgund_jamkhana", "Navalgund Jamkhana Rug", "ನವಲಗುಂದ ಜಮಖಾನ", ["navalgund", "jamkhana", "durrie", "carpet"], f"""
        <rect x="12" y="16" width="40" height="32" fill="{RED}" stroke="{DARK}" stroke-width="2"/>
        <!-- Geometric central diamonds (Navalgund signature) -->
        <polygon points="32,22 42,32 32,42 22,32" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <polygon points="32,26 38,32 32,38 26,32" fill="{SKY_BLUE}"/>
        <!-- Fringes -->
        <line x1="12" y1="12" x2="12" y2="16" stroke="{WHITE}" stroke-width="2"/>
        <line x1="52" y1="12" x2="52" y2="16" stroke="{WHITE}" stroke-width="2"/>
        """),
        ("craft_34_guledgudd_khana", "Guledgudd Khana Textile", "ಗುಳೇದಗುಡ್ಡ ಖಣ", ["khana", "guledgudd", "blouse", "choli"], f"""
        <rect x="14" y="18" width="36" height="28" fill="{PURPLE}" stroke="{GOLD}" stroke-width="2"/>
        <!-- Small woven square lattice with Siddheshwara temple motifs -->
        <line x1="14" y1="26" x2="50" y2="26" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="14" y1="34" x2="50" y2="34" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="26" y1="18" x2="26" y2="46" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="38" y1="18" x2="38" y2="46" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="20" cy="22" r="1.5" fill="{YELLOW}"/>
        <circle cx="32" cy="30" r="1.5" fill="{YELLOW}"/>
        <circle cx="44" cy="38" r="1.5" fill="{YELLOW}"/>
        """),
        ("craft_35_silk_cocoon", "Karnataka Silk Cocoon", "ರೇಷ್ಮೆ ಗೂಡು", ["silkworm", "cocoon", "sericulture"], f"""
        <!-- Golden-yellow oblong silk cocoon -->
        <ellipse cx="32" cy="32" rx="14" ry="20" transform="rotate(-25 32 32)" fill="{YELLOW}" stroke="{GOLD}" stroke-width="2"/>
        <!-- Mulberry leaf behind it -->
        <path d="M 14 46 C 10 38 16 26 24 32 C 22 42 16 46 14 46 Z" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Fine silk thread unspooling -->
        <path d="M 38 18 Q 48 10 52 14 Q 54 22 58 18" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
        """),
        ("craft_36_handloom_weaving_shuttle", "Weaver Handloom Shuttle (Naale)", "ಮಗ್ಗದ ನsample / ನಾಳೆ", ["shuttle", "handloom", "weaver", "silk"], f"""
        <!-- Boat-shaped polished wooden shuttle -->
        <path d="M 10 32 C 20 24 44 24 54 32 C 44 40 20 40 10 32 Z" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Silk pirn / spool in center -->
        <rect x="24" y="29" width="16" height="6" rx="2" fill="{GOLD}" stroke="{YELLOW}" stroke-width="1"/>
        <line x1="32" y1="29" x2="32" y2="20" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("craft_37_kuthu_vilakku_brass_lamp", "Traditional Brass Samayi Lamp", "ಹಿತ್ತಾಳೆ ಸಮಾಯಿ ದೀಪ", ["samayi", "brass", "lamp", "vilakku"], f"""
        <!-- Stepped base -->
        <ellipse cx="32" cy="54" rx="14" ry="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Pillar shaft -->
        <line x1="32" y1="54" x2="32" y2="24" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="32" cy="38" r="3" fill="{DARK_GOLD}"/>
        <!-- 5-wick oil dish -->
        <ellipse cx="32" cy="24" rx="12" ry="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Swan / Hamsa finial with flame -->
        <path d="M 32 20 C 30 14 36 12 34 8" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="34" cy="7" r="2" fill="{RED}"/>
        """),
        ("craft_38_hanging_brass_bell_lamp", "Hanging Brass Chain Lamp", "ತೂಗು ದೀಪ", ["hanginglamp", "brass", "chain"], f"""
        <!-- Chain links -->
        <line x1="32" y1="6" x2="32" y2="30" stroke="{GOLD}" stroke-width="2" stroke-dasharray="3 2"/>
        <circle cx="32" cy="30" r="3" fill="{GOLD}"/>
        <!-- Oil bowl -->
        <path d="M 20 38 C 20 46 44 46 44 38 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Little brass bells hanging below -->
        <circle cx="24" cy="48" r="1.5" fill="{YELLOW}"/>
        <circle cx="32" cy="48" r="1.5" fill="{YELLOW}"/>
        <circle cx="40" cy="48" r="1.5" fill="{YELLOW}"/>
        """),
        ("craft_39_kempu_jhumki", "Kempu Temple Ruby Jhumki", "ಕೆಂಪು ಜುಮುಕಿ", ["jhumki", "earring", "kempu", "ruby"], f"""
        <!-- Ear stud with ruby -->
        <circle cx="32" cy="18" r="5" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="18" r="2" fill="{YELLOW}"/>
        <line x1="32" y1="23" x2="32" y2="28" stroke="{GOLD}" stroke-width="2"/>
        <!-- Hanging bell dome -->
        <path d="M 20 38 C 20 28 44 28 44 38 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Pearl / Ruby hanging drops -->
        <circle cx="22" cy="44" r="1.5" fill="{WHITE}"/>
        <circle cx="27" cy="44" r="1.5" fill="{RED}"/>
        <circle cx="32" cy="44" r="1.5" fill="{WHITE}"/>
        <circle cx="37" cy="44" r="1.5" fill="{RED}"/>
        <circle cx="42" cy="44" r="1.5" fill="{WHITE}"/>
        """),
        ("craft_40_kempu_vanki", "Kempu Vanki (V-Armlet)", "ಕೆಂಪು ವಂಕಿ (ಬಾಜುಬಂದ್)", ["vanki", "armlet", "kempu", "jewelry"], f"""
        <!-- Inverted V-shape armlet with cobra or peacock crest -->
        <path d="M 14 36 L 32 20 L 50 36" stroke="{GOLD}" stroke-width="4" stroke-linecap="round" fill="none"/>
        <path d="M 18 38 L 32 26 L 46 38" stroke="{RED}" stroke-width="2" fill="none"/>
        <!-- Central Goddess Lakshmi / Ruby medallion atop -->
        <circle cx="32" cy="14" r="5" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="14" r="2" fill="{YELLOW}"/>
        """),
        ("craft_41_chandrahaara", "Mysore Chandrahaara Necklace", "ಮೈಸೂರು ಚಂದ್ರಹಾರ", ["chandrahaara", "necklace", "gold"], f"""
        <!-- Multi-tier crescent chains linked to side clips -->
        <path d="M 16 22 Q 32 30 48 22" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 16 28 Q 32 38 48 28" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 16 34 Q 32 46 48 34" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 16 40 Q 32 54 48 40" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <!-- Side floral clasps -->
        <circle cx="16" cy="22" r="3" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="48" cy="22" r="3" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("craft_42_kasina_sara", "Kasina Sara (Lakshmi Coin Necklace)", "ಕಾಸಿನ ಸರ", ["kasinasara", "coinnecklace", "lakshmi"], f"""
        <!-- Arched string of overlapping gold coins -->
        <path d="M 14 20 C 14 44 50 44 50 20" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="18" cy="30" r="3.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="24" cy="37" r="3.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="32" cy="40" r="4" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="40" cy="37" r="3.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="46" cy="30" r="3.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="32" cy="40" r="1.5" fill="{RED}"/>
        """),
        ("craft_43_mavinakayi_sara", "Mavinakayi Sara (Mango Necklace)", "ಮಾವಿನಕಾಯಿ ಸರ", ["mavinakayi", "mango", "paisley", "necklace"], f"""
        <!-- Paisley / mango motif gold beads -->
        <path d="M 16 20 C 16 44 48 44 48 20" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 22 34 C 20 30 26 28 26 34 C 26 38 22 38 22 34 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        <path d="M 32 40 C 30 36 36 34 36 40 C 36 44 32 44 32 40 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        <path d="M 42 34 C 40 30 46 28 46 34 C 46 38 42 38 42 34 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("craft_44_kadaga_bangle", "Kadaga Elephant Head Bangle", "ಕಡಗ ಬಳೆ", ["kadaga", "bangle", "elephant", "gold"], f"""
        <circle cx="32" cy="32" r="18" stroke="{GOLD}" stroke-width="4" fill="none"/>
        <!-- Two elephant heads facing each other at top opening -->
        <circle cx="26" cy="15" r="3" fill="{GOLD}"/>
        <circle cx="38" cy="15" r="3" fill="{GOLD}"/>
        <circle cx="26" cy="15" r="1" fill="{RED}"/>
        <circle cx="38" cy="15" r="1" fill="{RED}"/>
        """),
        ("craft_45_kempu_mangtikka", "Kempu Nethi Chutti (Maang Tikka)", "ನೆತ್ತಿ ಚುಟ್ಟಿ", ["mangtikka", "forehead", "kempu"], f"""
        <line x1="32" y1="8" x2="32" y2="30" stroke="{GOLD}" stroke-width="2"/>
        <!-- Ornate circular pendant -->
        <circle cx="32" cy="38" r="9" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="38" r="4" fill="{YELLOW}"/>
        <circle cx="32" cy="50" r="2" fill="{WHITE}"/>
        """),
        ("craft_46_daabu_waist_belt", "Oddiyana / Daabu Gold Waist Belt", "ಒಡ್ಯಾಣ / ಡಾಬು", ["oddiyana", "daabu", "belt", "gold"], f"""
        <!-- Broad ornate gold belt -->
        <path d="M 10 32 Q 32 38 54 32" stroke="{GOLD}" stroke-width="5" fill="none"/>
        <!-- Center Lakshmi medallion buckle -->
        <rect x="26" y="28" width="12" height="12" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="34" r="2.5" fill="{YELLOW}"/>
        """),
        ("craft_47_kolusu_silver_anklet", "Silver Kolusu Anklet", "ಬೆಳ್ಳಿಯ ಕಾಲು ಸರ (ಕೊಲುಸು)", ["kolusu", "anklet", "silver"], f"""
        <path d="M 12 32 Q 32 42 52 32" stroke="{SILVER}" stroke-width="3" fill="none"/>
        <!-- Tinkling silver bells (Muggulu) hanging -->
        <circle cx="18" cy="38" r="2" fill="{SILVER}"/>
        <circle cx="25" cy="40" r="2" fill="{SILVER}"/>
        <circle cx="32" cy="41" r="2" fill="{SILVER}"/>
        <circle cx="39" cy="40" r="2" fill="{SILVER}"/>
        <circle cx="46" cy="38" r="2" fill="{SILVER}"/>
        """),
        ("craft_48_mookuthi_nose_stud", "Traditional Ruby Nose Stud", "ಮೂಗುತಿ", ["mookuthi", "nosestud", "ruby"], f"""
        <circle cx="32" cy="32" r="6" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <!-- Center sparkling stone -->
        <circle cx="32" cy="32" r="2.5" fill="{WHITE}"/>
        <!-- 4 Petal prongs -->
        <circle cx="32" cy="24" r="1.5" fill="{GOLD}"/>
        <circle cx="32" cy="40" r="1.5" fill="{GOLD}"/>
        <circle cx="24" cy="32" r="1.5" fill="{GOLD}"/>
        <circle cx="40" cy="32" r="1.5" fill="{GOLD}"/>
        """),
        ("craft_49_surya_chandra_hair_jewels", "Surya & Chandra Hair Brooches", "ಸೂರ್ಯ ಚಂದ್ರ ಕೂದಲಿನ ಒಡವೆ", ["surya", "chandra", "hairjewelry"], f"""
        <!-- Sun (Surya) disc -->
        <circle cx="22" cy="32" r="8" fill="{YELLOW}" stroke="{RED}" stroke-width="1.5"/>
        <line x1="22" y1="20" x2="22" y2="16" stroke="{RED}" stroke-width="1.5"/>
        <line x1="22" y1="44" x2="22" y2="48" stroke="{RED}" stroke-width="1.5"/>
        <!-- Moon (Chandra) crescent -->
        <path d="M 44 24 C 40 28 40 36 44 40 C 40 38 38 34 38 32 C 38 28 40 25 44 24 Z" fill="{SILVER}" stroke="{WHITE}" stroke-width="1.5"/>
        """),
        ("craft_50_channapatna_yo_yo", "Channapatna Wooden Yo-Yo", "ಚನ್ನಪಟ್ಟಣದ ಯೋ-ಯೋ", ["yoyo", "toy", "channapatna"], f"""
        <!-- Double disc with colorful concentric lacquer rings -->
        <ellipse cx="32" cy="32" rx="16" ry="16" fill="{YELLOW}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="32" cy="32" r="11" fill="{RED}"/>
        <circle cx="32" cy="32" r="6" fill="{GREEN}"/>
        <circle cx="32" cy="32" r="2" fill="{WHITE}"/>
        <!-- String trailing out -->
        <path d="M 32 16 Q 34 8 42 6" stroke="{WHITE}" stroke-width="1.5" fill="none"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in crafts_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
