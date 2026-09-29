"""
Category 7: Geography, Nature, Rivers, Hills & Coastline of Karnataka (45 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "geography-nature",
            "tags": ["geography", "landscape", "western_ghats", "rivers", "hills", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Karnataka State Map Outline
    add("geo_01_karnataka_state_map_outline", "Karnataka State Map Outline", "ಕರ್ನಾಟಕ ರಾಜ್ಯದ ನಕ್ಷೆ", ["map", "karnataka", "state", "borders"], f"""
    <!-- Stylized accurate geographical silhouette of Karnataka -->
    <path d="M 28 8 C 36 8 44 10 46 16 C 48 22 40 24 42 30 C 46 36 44 42 42 46 C 40 50 36 56 32 58 C 26 56 24 50 20 44 C 18 36 18 24 22 16 C 24 10 26 8 28 8 Z" fill="rgba(200,16,46,0.15)" stroke="{RED}" stroke-width="2.5" stroke-linejoin="round"/>
    <!-- Capital mark at Bengaluru -->
    <circle cx="36" cy="46" r="2.5" fill="{RED}"/>
    <circle cx="36" cy="46" r="5" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
    """)

    # 2. Karnataka Map Yellow-Red Flag Fill
    add("geo_02_karnataka_map_yellow_red", "Karnataka Map Dual Flag Colors", "ಹಳದಿ-ಕೆಂಪು ಕರ್ನಾಟಕ ನಕ್ಷೆ", ["map", "flag", "bicolor"], f"""
    <!-- State map split horizontally: yellow on top, red on bottom -->
    <clipPath id="knMapClip">
        <path d="M 28 8 C 36 8 44 10 46 16 C 48 22 40 24 42 30 C 46 36 44 42 42 46 C 40 50 36 56 32 58 C 26 56 24 50 20 44 C 18 36 18 24 22 16 C 24 10 26 8 28 8 Z"/>
    </clipPath>
    <g clip-path="url(#knMapClip)">
        <rect x="10" y="6" width="44" height="26" fill="{YELLOW}"/>
        <rect x="10" y="32" width="44" height="28" fill="{RED}"/>
    </g>
    <path d="M 28 8 C 36 8 44 10 46 16 C 48 22 40 24 42 30 C 46 36 44 42 42 46 C 40 50 36 56 32 58 C 26 56 24 50 20 44 C 18 36 18 24 22 16 C 24 10 26 8 28 8 Z" stroke="{DARK_GOLD}" stroke-width="2" fill="none"/>
    """)

    # 3. Western Ghats Sahyadri Peaks
    add("geo_03_western_ghats_sahyadri_peaks", "Western Ghats (Sahyadri Ridges)", "ಪಶ್ಚಿಮ ಘಟ್ಟಗಳು (ಸಹ್ಯಾದ್ರಿ)", ["mountains", "sahyadri", "westernghats", "peaks"], f"""
    <!-- Layered mountain ridges with mist -->
    <polygon points="6,50 24,20 42,50" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <polygon points="22,50 40,16 58,50" fill="{DARK_GOLD}" stroke="{GREEN}" stroke-width="1.5"/>
    <polygon points="14,50 32,26 50,50" fill="{LIGHT_GREEN}" stroke="{GREEN}" stroke-width="1.5"/>
    <!-- Floating cloud mist -->
    <path d="M 12 36 Q 22 32 32 36 Q 42 32 52 36" stroke="{WHITE}" stroke-width="2" stroke-linecap="round" fill="none"/>
    """)

    # 4. Mullayanagiri Peak
    add("geo_04_mullayanagiri_highest_peak", "Mullayanagiri (Highest Peak)", "ಮುಳ್ಳಯ್ಯನಗಿರಿ ಶಿಖರ", ["mullayanagiri", "peak", "chikmagalur", "highest"], f"""
    <polygon points="10,52 32,14 54,52" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
    <!-- Small temple shrine at summit -->
    <rect x="29" y="10" width="6" height="5" fill="{WHITE}" stroke="{RED}" stroke-width="1"/>
    <polygon points="32,6 28,10 36,10" fill="{RED}"/>
    <!-- Winding trekking trail path -->
    <path d="M 14 52 Q 28 44 26 36 Q 36 28 32 18" stroke="{YELLOW}" stroke-width="2" fill="none" stroke-dasharray="2 1"/>
    """)

    # 5. Kudremukh Horse-Face Peak
    add("geo_05_kudremukh_horse_face_peak", "Kudremukh (Horse-Face Peak)", "ಕುದುರೆಮುಖ ಶಿಖರ", ["kudremukh", "horseface", "nationalpark"], f"""
    <!-- Mountain ridge distinctly resembling a horse head profile -->
    <path d="M 10 52 L 20 32 C 24 24 30 16 38 16 C 44 16 46 22 50 24 C 54 26 52 32 46 34 L 54 52 Z" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
    <path d="M 28 30 Q 38 24 46 34" stroke="{LIGHT_GREEN}" stroke-width="2" fill="none"/>
    <!-- Sun rising behind -->
    <circle cx="18" cy="18" r="6" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
    """)

    # 6. Jog Falls (Sharavathi)
    add("geo_06_jog_falls_sharavathi", "Jog Falls (Gersoppa)", "ಜೋಗ ಜಲಪಾತ", ["jogfalls", "waterfall", "sharavathi", "shimoga"], f"""
    <!-- Deep vertical granite cliff -->
    <rect x="8" y="10" width="48" height="42" rx="3" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
    <!-- 4 Cascades: Raja, Roarer, Rocket, Rani -->
    <line x1="16" y1="12" x2="16" y2="50" stroke="{WHITE}" stroke-width="3" stroke-linecap="round"/>
    <line x1="26" y1="14" x2="26" y2="48" stroke="{SKY_BLUE}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="36" y1="12" x2="36" y2="48" stroke="{WHITE}" stroke-width="2" stroke-linecap="round"/>
    <line x1="46" y1="16" x2="46" y2="50" stroke="{SKY_BLUE}" stroke-width="3" stroke-linecap="round"/>
    <!-- Pool mist at bottom -->
    <ellipse cx="32" cy="50" rx="20" ry="4" fill="rgba(255,255,255,0.7)"/>
    """)

    # 7-45 Geography, Rivers, Waterfalls, Hills, Coastline batch
    geo_batch = [
        ("geo_07_shivanasamudra_falls", "Shivanasamudra Waterfalls", "ಶಿವನಸಮುದ್ರ ಜಲಪಾತ", ["shivanasamudra", "falls", "cauvery"], f"""
        <rect x="10" y="14" width="44" height="38" rx="2" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Gaganachukki & Bharachukki roaring wide falls -->
        <rect x="16" y="14" width="12" height="34" fill="{WHITE}"/>
        <rect x="36" y="14" width="12" height="34" fill="{WHITE}"/>
        <ellipse cx="32" cy="48" rx="20" ry="4" fill="{SKY_BLUE}"/>
        """),
        ("geo_08_abbey_falls_coorg", "Abbey Falls (Madikeri)", "ಅಬ್ಬಿ ಜಲಪಾತ (ಮಡಿಕೇರಿ)", ["abbeyfalls", "coorg", "falls"], f"""
        <path d="M 12 12 L 20 48 L 44 48 L 52 12 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 24 12 L 26 48 M 32 12 L 32 48 M 40 12 L 38 48" stroke="{WHITE}" stroke-width="3"/>
        <!-- Hanging bridge cables in front -->
        <path d="M 8 36 Q 32 44 56 36" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("geo_09_hebbe_falls_kemmangundi", "Hebbe Falls (Two-Stage)", "ಹೆಬ್ಬೆ ಜಲಪಾತ", ["hebbefalls", "kemmangundi", "chikmagalur"], f"""
        <polygon points="12,50 24,14 36,50" fill="{SLATE}"/>
        <polygon points="28,50 40,14 52,50" fill="{SLATE}"/>
        <line x1="26" y1="14" x2="26" y2="30" stroke="{WHITE}" stroke-width="3"/>
        <line x1="36" y1="30" x2="36" y2="48" stroke="{WHITE}" stroke-width="4"/>
        <ellipse cx="32" cy="50" rx="16" ry="4" fill="{SKY_BLUE}"/>
        """),
        ("geo_10_dudhsagar_falls_border", "Dudhsagar Sea of Milk Falls", "ದೂದ್‌ಸಾಗರ್ ಜಲಪಾತ", ["dudhsagar", "falls", "train"], f"""
        <polygon points="10,50 32,10 54,50" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <line x1="32" y1="12" x2="32" y2="48" stroke="{WHITE}" stroke-width="6"/>
        <!-- Railway arched viaduct across falls -->
        <rect x="14" y="28" width="36" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1"/>
        <line x1="14" y1="31" x2="50" y2="31" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("geo_11_unchehalli_falls", "Unchalli (Lushington) Falls", "ಉಂಚಳ್ಳಿ ಜಲಪಾತ", ["unchalli", "falls", "sirsi", "aghanashini"], f"""
        <rect x="12" y="12" width="40" height="40" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 28 12 Q 30 30 34 50" stroke="{WHITE}" stroke-width="5" fill="none"/>
        <ellipse cx="32" cy="50" rx="18" ry="4" fill="{SKY_BLUE}"/>
        """),
        ("geo_12_magod_falls", "Magod Falls Canyon", "ಮಾಗೋಡು ಜಲಪಾತ", ["magod", "falls", "bedti", "yellapur"], f"""
        <polygon points="10,12 24,50 8,50" fill="{BROWN}"/>
        <polygon points="54,12 40,50 56,50" fill="{BROWN}"/>
        <line x1="28" y1="12" x2="32" y2="50" stroke="{WHITE}" stroke-width="4"/>
        <ellipse cx="32" cy="50" rx="12" ry="4" fill="{SKY_BLUE}"/>
        """),
        ("geo_13_sathodi_falls", "Sathodi Jungle Waterfall", "ಸಾತೊಡ್ಡಿ ಜಲಪಾತ", ["sathodi", "falls", "forest", "uttarakannada"], f"""
        <rect x="14" y="14" width="36" height="38" rx="2" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="32" y1="14" x2="32" y2="48" stroke="{WHITE}" stroke-width="8"/>
        <ellipse cx="32" cy="48" rx="16" ry="5" fill="{SKY_BLUE}"/>
        """),
        ("geo_14_cauvery_river_stream", "Holy Cauvery River", "ಪುಣ್ಯ ಕಾವೇರಿ ನದಿ", ["cauvery", "river", "holy", "karnataka"], f"""
        <!-- Meandering river through lush green plains -->
        <path d="M 12 12 Q 44 26 20 40 Q 36 50 48 56" stroke="{ROYAL_BLUE}" stroke-width="6" stroke-linecap="round" fill="none"/>
        <path d="M 12 12 Q 44 26 20 40 Q 36 50 48 56" stroke="{SKY_BLUE}" stroke-width="3" stroke-linecap="round" fill="none"/>
        <circle cx="16" cy="24" r="2" fill="{GREEN}"/>
        <circle cx="46" cy="38" r="2.5" fill="{GREEN}"/>
        """),
        ("geo_15_talakaveri_holy_spring", "Talakaveri Kundike Spring", "ತಲಕಾವೇರಿ ಕುಂಡಿಕೆ", ["talakaveri", "kundike", "origin", "coorg"], f"""
        <!-- Holy square stone tank / Kundike with sacred water and kalasha -->
        <rect x="16" y="24" width="32" height="26" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <rect x="22" y="30" width="20" height="14" fill="{SKY_BLUE}" stroke="{WHITE}" stroke-width="1.5"/>
        <!-- Golden Kalasa at head of spring -->
        <circle cx="32" cy="18" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="12" r="2" fill="{RED}"/>
        """),
        ("geo_16_sangama_mekedatu", "Mekedatu (Goat's Leap Gorge)", "ಮೇಕೆದಾಟು", ["mekedatu", "gorge", "cauvery", "kanakapura"], f"""
        <!-- Two sheer granite rock walls very close together -->
        <path d="M 10 12 L 28 32 L 24 54 L 8 54 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 54 12 L 36 32 L 40 54 L 56 54 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Deep rushing river canyon between them -->
        <path d="M 28 32 L 24 54 L 40 54 L 36 32 Z" fill="{SKY_BLUE}"/>
        <!-- Goat leaping across -->
        <path d="M 28 24 Q 32 18 36 24" stroke="{BROWN}" stroke-width="2" fill="none"/>
        """),
        ("geo_17_tungabhadra_river", "Tungabhadra River & Boulders", "ತುಂಗಭದ್ರಾ ನದಿ", ["tungabhadra", "river", "hampi", "boulders"], f"""
        <path d="M 8 36 Q 32 24 56 36" stroke="{ROYAL_BLUE}" stroke-width="8" fill="none"/>
        <path d="M 8 36 Q 32 24 56 36" stroke="{SKY_BLUE}" stroke-width="4" fill="none"/>
        <!-- Hampi boulders on banks -->
        <ellipse cx="20" cy="22" rx="8" ry="6" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <ellipse cx="42" cy="46" rx="10" ry="7" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        """),
        ("geo_18_krishna_river", "Sacred Krishna River", "ಕೃಷ್ಣಾ ನದಿ", ["krishna", "river", "bagalkot"], f"""
        <path d="M 10 20 Q 32 40 54 20" stroke="{ROYAL_BLUE}" stroke-width="6" fill="none"/>
        <path d="M 10 32 Q 32 52 54 32" stroke="{SKY_BLUE}" stroke-width="4" fill="none"/>
        <circle cx="32" cy="14" r="4" fill="{YELLOW}"/>
        """),
        ("geo_19_sharavathi_valley_backwaters", "Sharavathi Valley Backwaters", "ಶರಾವತಿ ಹಿನ್ನೀರು", ["sharavathi", "backwaters", "valley"], f"""
        <!-- Calm expanse of water with forested islands -->
        <rect x="10" y="24" width="44" height="26" fill="{SKY_BLUE}" stroke="{ROYAL_BLUE}" stroke-width="1.5"/>
        <!-- Forested island -->
        <ellipse cx="26" cy="34" rx="8" ry="4" fill="{GREEN}"/>
        <ellipse cx="40" cy="40" rx="6" ry="3" fill="{GREEN}"/>
        <circle cx="26" cy="30" r="3" fill="{DARK_GOLD}"/>
        """),
        ("geo_20_netravathi_river_dakshina_kannada", "Netravathi River Mangalore", "ನೇತ್ರಾವತಿ ನದಿ", ["netravathi", "river", "mangalore", "dharmasthala"], f"""
        <path d="M 12 16 C 26 28 36 32 52 44" stroke="{ROYAL_BLUE}" stroke-width="7" stroke-linecap="round" fill="none"/>
        <path d="M 12 16 C 26 28 36 32 52 44" stroke="{SKY_BLUE}" stroke-width="4" stroke-linecap="round" fill="none"/>
        <circle cx="44" cy="22" r="3" fill="{GOLD}"/>
        """),
        ("geo_21_kabini_backwaters_dead_trees", "Kabini Dead Trees Silhouette", "ಕಬಿನಿ ಹಿನ್ನೀರು ಮರಗಳು", ["kabini", "deadtrees", "wildlife", "safari"], f"""
        <line x1="8" y1="44" x2="56" y2="44" stroke="{SKY_BLUE}" stroke-width="3"/>
        <!-- Iconic bare gnarled dead trees rising from water -->
        <path d="M 24 44 L 24 18 L 18 12 M 24 24 L 30 16 M 24 30 L 16 26" stroke="{DARK}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
        <path d="M 42 44 L 42 22 L 46 16 M 42 28 L 38 20" stroke="{DARK}" stroke-width="2" stroke-linecap="round" fill="none"/>
        <!-- Sunset glow -->
        <circle cx="32" cy="18" r="6" fill="{ORANGE}"/>
        """),
        ("geo_22_karavali_coastline_palm_beach", "Karavali Palm Coast Beach", "ಕರಾವಳಿ ತೀರ ಮತ್ತು ತೆಂಗಿನ ಮರ", ["karavali", "coast", "beach", "palm"], f"""
        <!-- Coastline sand and turquoise sea -->
        <path d="M 8 50 Q 32 44 56 50" stroke="{GOLD}" stroke-width="6" fill="none"/>
        <path d="M 8 42 Q 32 36 56 42" stroke="{SKY_BLUE}" stroke-width="4" fill="none"/>
        <!-- Leaning Coconut Palm -->
        <path d="M 20 48 Q 28 32 30 18" stroke="{BROWN}" stroke-width="3" fill="none"/>
        <path d="M 30 18 Q 18 14 14 20 M 30 18 Q 42 14 46 20 M 30 18 Q 30 8 32 6" stroke="{GREEN}" stroke-width="2" fill="none"/>
        """),
        ("geo_23_om_beach_gokarna", "Gokarna Om Beach (Coastline ॐ)", "ಗೋಕರ್ಣ ಓಂ ಬೀಚ್", ["ombeach", "gokarna", "om", "beach"], f"""
        <!-- Natural Om-shaped twin semicircular coves -->
        <path d="M 12 36 C 18 20 28 20 32 36 C 36 20 46 20 52 36" stroke="{GOLD}" stroke-width="5" stroke-linecap="round" fill="none"/>
        <path d="M 12 40 C 18 24 28 24 32 40 C 36 24 46 24 52 40" stroke="{SKY_BLUE}" stroke-width="3" fill="none"/>
        <circle cx="32" cy="14" r="2.5" fill="{RED}"/>
        """),
        ("geo_24_st_marys_island_hexagonal_basalt", "St. Mary's Island Basalt Columns", "ಸೇಂಟ್ ಮೇರೀಸ್ ದ್ವೀಪದ ಕಂಬಗಳು", ["stmarys", "basalt", "malpe", "columns", "geology"], f"""
        <!-- Columnar hexagonal jointed basalt lava rocks -->
        <polygon points="18,34 26,30 34,34 34,54 26,58 18,54" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <polygon points="34,30 42,26 50,30 50,52 42,56 34,52" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <polygon points="26,18 34,14 42,18 42,34 34,38 26,34" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("geo_25_kaup_lighthouse", "Kaup Black & White Lighthouse", "ಕಾಪು ಲೈಟ್‌ಹೌಸ್ (ದೀಪಸ್ತಂಭ)", ["kaup", "lighthouse", "kapu", "beacon", "sea"], f"""
        <!-- Cylindrical tower with horizontal bands -->
        <polygon points="26,48 28,18 36,18 38,48" fill="{WHITE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Black stripes -->
        <rect x="27.5" y="24" width="9" height="6" fill="{DARK}"/>
        <rect x="26.5" y="36" width="11" height="6" fill="{DARK}"/>
        <!-- Lantern room and dome -->
        <rect x="28" y="14" width="8" height="4" fill="{YELLOW}" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 28 14 C 28 10 36 10 36 14" fill="{RED}"/>
        <!-- Light beams -->
        <line x1="36" y1="16" x2="52" y2="10" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="28" y1="16" x2="12" y2="10" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("geo_26_bhatkal_lighthouse", "Bhatkal Headland Lighthouse", "ಭಟ್ಕಳ ಲೈಟ್‌ಹೌಸ್", ["bhatkal", "lighthouse", "coastal"], f"""
        <polygon points="26,50 28,22 36,22 38,50" fill="{WHITE}" stroke="{RED}" stroke-width="2"/>
        <rect x="27" y="32" width="10" height="6" fill="{RED}"/>
        <circle cx="32" cy="18" r="4" fill="{YELLOW}"/>
        <ellipse cx="32" cy="52" rx="16" ry="4" fill="{SLATE}"/>
        """),
        ("geo_27_murudeshwar_sea_cliff", "Murudeshwar Cliff & Coast", "ಮುರುಡೇಶ್ವರ ಕಡಲತೀರ", ["murudeshwar", "cliff", "sea", "promontory"], f"""
        <path d="M 10 46 C 24 38 34 38 54 46" stroke="{GOLD}" stroke-width="4" fill="none"/>
        <path d="M 10 52 C 24 44 34 44 54 52" stroke="{SKY_BLUE}" stroke-width="4" fill="none"/>
        <!-- Hillock promontory -->
        <polygon points="20,40 32,18 44,40" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="14" r="3" fill="{CREAM}"/>
        """),
        ("geo_28_malpe_sea_walk", "Malpe Sea Walk Pier", "ಮಲ್ಪೆ ಸೀ ವಾಕ್", ["malpe", "seawalk", "pier", "udupi"], f"""
        <!-- Long stone walkway extending into blue waves -->
        <polygon points="12,52 28,26 36,26 52,52" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <line x1="32" y1="26" x2="32" y2="52" stroke="{YELLOW}" stroke-width="2"/>
        <!-- Sea on both sides -->
        <path d="M 8 36 Q 18 34 24 38" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        <path d="M 40 38 Q 46 34 56 36" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("geo_29_yana_twin_limestone_karsts", "Yana Black Karst Rock Spires", "ಯಾಣದ ಬೃಹತ್ ಶಿಖರಗಳು", ["yana", "limestone", "karst", "spires"], f"""
        <!-- Bhairaveshwara & Mohini Shikhara pointed black monoliths -->
        <polygon points="12,54 22,12 32,54" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <polygon points="30,54 40,16 50,54" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <polygon points="20,16 22,12 24,16" fill="{SLATE}"/>
        <polygon points="38,20 40,16 42,20" fill="{SLATE}"/>
        """),
        ("geo_30_hampi_granite_boulder_landscape", "Hampi Boulder Landscape", "ಹಂಪಿಯ ಕಲ್ಲು ಬಂಡೆಗಳ ತಾಣ", ["hampi", "boulder", "granite", "landscape"], f"""
        <!-- Stacked balance rock boulders -->
        <ellipse cx="32" cy="48" rx="18" ry="8" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <ellipse cx="32" cy="34" rx="14" ry="7" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <ellipse cx="32" cy="22" rx="9" ry="6" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Blazing sun -->
        <circle cx="48" cy="14" r="5" fill="{ORANGE}"/>
        """),
        ("geo_31_madikeri_coorg_misty_hills", "Madikeri Scotland of India", "ಮಡಿಕೇರಿ ಮಂಜಿನ ಬೆಟ್ಟ", ["madikeri", "coorg", "misty", "hills"], f"""
        <path d="M 8 50 Q 24 30 40 50 Q 50 36 56 50" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Morning mist swirling -->
        <path d="M 12 34 Q 24 28 36 34 Q 48 38 52 32" stroke="{WHITE}" stroke-width="2.5" fill="none"/>
        <path d="M 16 24 Q 28 18 40 24" stroke="{WHITE}" stroke-width="2" fill="none"/>
        """),
        ("geo_32_kemmangundi_z_point", "Kemmangundi Z-Point Ridge", "ಕೆಮ್ಮಣ್ಣುಗುಂಡಿ Z-ಪಾಯಿಂಟ್", ["kemmangundi", "zpoint", "ridge", "view"], f"""
        <path d="M 10 24 L 30 38 L 22 52 L 48 52" stroke="{RED}" stroke-width="3" stroke-linecap="round" fill="none"/>
        <polygon points="10,52 30,38 48,52" fill="{GREEN}"/>
        <circle cx="44" cy="18" r="5" fill="{YELLOW}"/>
        """),
        ("geo_33_nandi_hills_sunrise", "Nandi Hills Sunrise & Sea of Clouds", "ನಂದಿ ಬೆಟ್ಟದ ಸೂರ್ಯೋದಯ", ["nandihills", "sunrise", "clouds", "chikkaballapur"], f"""
        <polygon points="10,50 32,26 54,50" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Radiant Sun -->
        <circle cx="32" cy="16" r="6" fill="{ORANGE}" stroke="{YELLOW}" stroke-width="2"/>
        <!-- Sea of clouds enveloping hills -->
        <ellipse cx="20" cy="42" rx="10" ry="4" fill="{WHITE}"/>
        <ellipse cx="36" cy="44" rx="12" ry="4" fill="{WHITE}"/>
        <ellipse cx="48" cy="40" rx="8" ry="3" fill="{WHITE}"/>
        """),
        ("geo_34_savandurga_monolith_hill", "Savandurga Monolithic Rock", "ಸಾವನದುರ್ಗ ಏಕಶಿಲಾ ಬೆಟ್ಟ", ["savandurga", "monolith", "magadi", "rock"], f"""
        <!-- Massive smooth rounded granite dome -->
        <path d="M 12 52 C 12 20 52 20 52 52 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2.5"/>
        <path d="M 24 36 Q 32 30 40 36" stroke="{CREAM}" stroke-width="1.5" fill="none"/>
        <rect x="29" y="16" width="6" height="5" fill="{RED}"/>
        """),
        ("geo_35_madhugiri_monolith_fort", "Madhugiri Asia's Largest Monolith", "ಮಧುಗಿರಿ ಬೆಟ್ಟ", ["madhugiri", "monolith", "fort", "tumkur"], f"""
        <path d="M 10 52 C 10 16 54 16 54 52 Z" fill="{DARK_GOLD}" stroke="{DARK}" stroke-width="2.5"/>
        <!-- Fort ramparts on rock -->
        <line x1="20" y1="36" x2="44" y2="36" stroke="{DARK}" stroke-width="2"/>
        <rect x="28" y="32" width="8" height="4" fill="{DARK}"/>
        """),
        ("geo_36_deccan_plateau_semi_arid", "Bayaluseeme Deccan Plateau", "ಬಯಲುಸೀಮೆ ಪ್ರಸ್ಥಭೂಮಿ", ["bayaluseeme", "plateau", "deccan"], f"""
        <!-- Flat horizon line -->
        <line x1="8" y1="42" x2="56" y2="42" stroke="{BROWN}" stroke-width="3"/>
        <!-- Solitary Acacia tree -->
        <line x1="24" y1="42" x2="24" y2="26" stroke="{DARK}" stroke-width="2.5"/>
        <path d="M 16 26 C 16 20 32 20 32 26 Z" fill="{GREEN}"/>
        <circle cx="44" cy="22" r="5" fill="{YELLOW}"/>
        """),
        ("geo_37_krishnaraja_sagara_krs_dam", "KRS Dam (Kannambadi Katte)", "ಕೆ.ಆರ್.ಎಸ್ ಅಣೆಕಟ್ಟು", ["krsdam", "mandya", "reservoir", "visvesvaraya"], f"""
        <!-- Sluice gate masonry wall -->
        <rect x="12" y="24" width="40" height="26" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Arched water spillways -->
        <path d="M 18 36 C 18 30 22 30 22 36 M 26 36 C 26 30 30 30 30 36 M 34 36 C 34 30 38 30 38 36 M 42 36 C 42 30 46 30 46 36" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <!-- Water spraying out -->
        <line x1="20" y1="38" x2="16" y2="52" stroke="{SKY_BLUE}" stroke-width="2"/>
        <line x1="28" y1="38" x2="26" y2="52" stroke="{SKY_BLUE}" stroke-width="2"/>
        <line x1="36" y1="38" x2="38" y2="52" stroke="{SKY_BLUE}" stroke-width="2"/>
        <line x1="44" y1="38" x2="48" y2="52" stroke="{SKY_BLUE}" stroke-width="2"/>
        """),
        ("geo_38_almatti_dam_bagalkot", "Almatti Dam (Lal Bahadur Shastri)", "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು", ["almatti", "dam", "bagalkot", "krishna"], f"""
        <rect x="12" y="22" width="40" height="28" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <rect x="16" y="26" width="6" height="12" fill="{WHITE}"/>
        <rect x="26" y="26" width="6" height="12" fill="{WHITE}"/>
        <rect x="36" y="26" width="6" height="12" fill="{WHITE}"/>
        <line x1="12" y1="22" x2="52" y2="22" stroke="{RED}" stroke-width="2"/>
        """),
        ("geo_39_tungabhadra_dam_hospet", "Tungabhadra Dam (Hospet)", "ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟು", ["tungabhadra", "dam", "hospet", "bellary"], f"""
        <rect x="12" y="26" width="40" height="24" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Watchtower on hill beside it -->
        <rect x="14" y="14" width="8" height="12" fill="{DARK}" stroke="{GOLD}" stroke-width="1"/>
        <polygon points="18,8 12,14 24,14" fill="{RED}"/>
        <line x1="26" y1="34" x2="48" y2="34" stroke="{SKY_BLUE}" stroke-width="3"/>
        """),
        ("geo_40_linganamakki_dam", "Linganamakki Dam (Sharavathi)", "ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು", ["linganamakki", "dam", "sharavathi"], f"""
        <polygon points="14,48 18,24 46,24 50,48" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <line x1="18" y1="24" x2="46" y2="24" stroke="{GOLD}" stroke-width="2"/>
        <ellipse cx="32" cy="48" rx="20" ry="4" fill="{SKY_BLUE}"/>
        """),
        ("geo_41_krsna_raja_fountain_brindavan", "Brindavan Musical Fountains", "ಬೃಂದಾವನ ಕಾರಂಜಿ", ["brindavan", "fountain", "garden"], f"""
        <!-- Jet fountain spraying symmetrically -->
        <ellipse cx="32" cy="48" rx="16" ry="5" fill="{ROYAL_BLUE}"/>
        <line x1="32" y1="48" x2="32" y2="16" stroke="{SKY_BLUE}" stroke-width="3" stroke-linecap="round"/>
        <path d="M 32 20 Q 22 22 16 34" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <path d="M 32 20 Q 42 22 48 34" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <path d="M 32 26 Q 24 28 20 40" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        <path d="M 32 26 Q 40 28 44 40" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("geo_42_kabini_dam_forest", "Kabini Dam & Forest Lake", "ಕಬಿನಿ ಜಲಾಶಯ", ["kabini", "lake", "forest"], f"""
        <path d="M 12 36 Q 32 24 52 36" stroke="{SKY_BLUE}" stroke-width="8" fill="none"/>
        <!-- Jungle green line behind lake -->
        <path d="M 12 28 Q 32 20 52 28" stroke="{GREEN}" stroke-width="4" fill="none"/>
        <circle cx="32" cy="14" r="5" fill="{YELLOW}"/>
        """),
        ("geo_43_bababudangiri_crescent", "Bababudangiri Inam Dattatreya", "ಬಾಬಾಬುಡನ್‌ಗಿರಿ", ["bababudangiri", "shrine", "chikmagalur"], f"""
        <polygon points="12,50 32,18 52,50" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Crescent moon & sacred dome -->
        <path d="M 32 14 C 30 11 34 11 32 8" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="24" r="3" fill="{WHITE}"/>
        """),
        ("geo_44_kodachadri_peak_mookambika", "Kodachadri Sarvajna Peetha", "ಕೊಡಚಾದ್ರಿ ಸರ್ವಜ್ಞ ಪೀಠ", ["kodachadri", "shankaracharya", "kollur"], f"""
        <polygon points="10,50 32,16 54,50" fill="{DARK_GOLD}" stroke="{DARK}" stroke-width="2"/>
        <!-- Sarvajna Peetha stone sanctum -->
        <rect x="29" y="12" width="6" height="5" fill="{SLATE}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="46" cy="18" r="5" fill="{RED}"/>
        """),
        ("geo_45_brahmagiri_hills", "Brahmagiri Wildlife Sanctuary", "ಬ್ರಹ್ಮಗಿರಿ ಬೆಟ್ಟ", ["brahmagiri", "hills", "westernghats"], f"""
        <polygon points="8,52 26,20 44,52" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <polygon points="24,52 42,16 58,52" fill="{LIGHT_GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="8" y1="52" x2="58" y2="52" stroke="{BROWN}" stroke-width="2"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in geo_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
