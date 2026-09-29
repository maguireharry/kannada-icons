"""
Category 6: Wildlife, Flora, Fauna & Forest Heritage of Karnataka (50 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "wildlife-flora-fauna",
            "tags": ["wildlife", "flora", "fauna", "nature", "forest", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Asian Elephant Head (State Animal)
    add("nature_01_asian_elephant_state_animal", "Karnataka State Animal - Asian Elephant", "ರಾಜ್ಯ ಪ್ರಾಣಿ - ಆನೆ", ["elephant", "stateanimal", "bandipur", "tusker"], f"""
    <!-- Majestic elephant head with large flapping ears and curved tusk -->
    <path d="M 22 20 C 14 20 12 32 18 38 C 22 42 26 36 28 32 L 28 46 C 28 54 36 54 36 46 L 36 30 C 42 30 52 24 50 16 C 46 12 36 14 30 18 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
    <!-- Large ear -->
    <path d="M 22 22 C 14 24 14 34 22 36" stroke="{DARK}" stroke-width="1.5" fill="none"/>
    <circle cx="34" cy="22" r="2" fill="{WHITE}"/>
    <circle cx="34" cy="22" r="1" fill="{DARK}"/>
    <!-- Ivory Tusk -->
    <path d="M 32 36 C 36 38 42 36 44 30" stroke="{CREAM}" stroke-width="3" stroke-linecap="round" fill="none"/>
    """)

    # 2. Elephant Herd Silhouette
    add("nature_02_elephant_herd_bandipur", "Elephant Herd in Forest", "ಕಾಡಾನೆಗಳ ಹಿಂಡು", ["elephant", "herd", "safari"], f"""
    <!-- Parent Elephant -->
    <ellipse cx="24" cy="34" rx="14" ry="10" fill="{SLATE}"/>
    <path d="M 12 32 L 8 46" stroke="{SLATE}" stroke-width="3" stroke-linecap="round"/>
    <rect x="18" y="40" width="4" height="12" fill="{SLATE}"/>
    <rect x="28" y="40" width="4" height="12" fill="{SLATE}"/>
    <!-- Baby Calf following -->
    <ellipse cx="44" cy="40" rx="8" ry="6" fill="{SLATE}"/>
    <rect x="40" y="44" width="3" height="8" fill="{SLATE}"/>
    <rect x="48" y="44" width="3" height="8" fill="{SLATE}"/>
    <path d="M 50 38 L 54 44" stroke="{SLATE}" stroke-width="2"/>
    <line x1="6" y1="52" x2="58" y2="52" stroke="{GREEN}" stroke-width="2"/>
    """)

    # 3. Indian Roller (State Bird - Neelakantha)
    add("nature_03_indian_roller_neelakantha", "State Bird - Indian Roller (Neelakantha)", "ರಾಜ್ಯ ಪಕ್ಷಿ - ನೀಲಕಂಠ", ["bird", "statebird", "roller", "neelakantha"], f"""
    <!-- Vibrant blue and turquoise Indian Roller perched -->
    <path d="M 30 16 C 36 16 42 22 40 32 L 36 48 L 30 48 L 26 34 C 24 24 24 16 30 16 Z" fill="{SKY_BLUE}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Deep blue wing patch -->
    <path d="M 28 26 C 34 26 36 36 34 44 C 30 40 26 34 28 26 Z" fill="{ROYAL_BLUE}"/>
    <!-- Beak and eye -->
    <polygon points="40,20 48,22 40,24" fill="{DARK}"/>
    <circle cx="36" cy="20" r="1.5" fill="{WHITE}"/>
    <!-- Branch perch -->
    <line x1="16" y1="46" x2="48" y2="46" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
    """)

    # 4. Neelakantha in Flight
    add("nature_04_neelakantha_in_flight", "Indian Roller in Flight", "ಹಾರುತ್ತಿರುವ ನೀಲಕಂಠ", ["flight", "wings", "neelakantha"], f"""
    <!-- Brilliant wings open showing turquoise and violet bands -->
    <path d="M 32 30 L 10 16 C 14 28 22 34 32 38 L 54 16 C 50 28 42 34 32 38 Z" fill="{SKY_BLUE}" stroke="{ROYAL_BLUE}" stroke-width="2"/>
    <line x1="16" y1="20" x2="28" y2="34" stroke="{ROYAL_BLUE}" stroke-width="3"/>
    <line x1="48" y1="20" x2="36" y2="34" stroke="{ROYAL_BLUE}" stroke-width="3"/>
    <!-- Tail -->
    <polygon points="30,38 34,38 36,54 28,54" fill="{ROYAL_BLUE}"/>
    """)

    # 5. Sacred Lotus (State Flower - Kamala)
    add("nature_05_sacred_lotus_state_flower", "State Flower - Sacred Lotus (Kamala)", "ರಾಜ್ಯ ಪುಷ್ಪ - ಕಮಲ", ["lotus", "stateflower", "kamala", "pink"], f"""
    <!-- Center petal -->
    <path d="M 32 14 C 26 24 26 38 32 44 C 38 38 38 24 32 14 Z" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Left petal -->
    <path d="M 32 44 C 22 42 14 32 18 24 C 24 24 28 34 32 44 Z" fill="rgba(200,16,46,0.7)" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Right petal -->
    <path d="M 32 44 C 42 42 50 32 46 24 C 40 24 36 34 32 44 Z" fill="rgba(200,16,46,0.7)" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Water ripples base -->
    <path d="M 18 52 Q 32 56 46 52" stroke="{SKY_BLUE}" stroke-width="2.5" fill="none"/>
    """)

    # 6. Lotus Bud
    add("nature_06_lotus_bud", "Lotus Flower Bud", "ಕಮಲದ ಮೊಗ್ಗು", ["lotus", "bud", "bloom"], f"""
    <path d="M 32 12 C 22 24 22 38 32 42 C 42 38 42 24 32 12 Z" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <!-- Sepals -->
    <path d="M 32 42 C 24 38 22 42 24 46 C 28 46 30 44 32 42 Z" fill="{GREEN}"/>
    <path d="M 32 42 C 40 38 42 42 40 46 C 36 46 34 44 32 42 Z" fill="{GREEN}"/>
    <line x1="32" y1="42" x2="32" y2="56" stroke="{GREEN}" stroke-width="3"/>
    """)

    # 7. Sandalwood Tree (State Tree - Gandhada Mara)
    add("nature_07_sandalwood_tree_state_tree", "State Tree - Sandalwood (Gandhada Mara)", "ರಾಜ್ಯ ವೃಕ್ಷ - ಶ್ರೀಗಂಧದ ಮರ", ["sandalwood", "statetree", "gandhadagudi"], f"""
    <!-- Strong trunk -->
    <path d="M 30 56 L 30 34 L 24 28 M 34 56 L 34 34 L 40 26" stroke="{BROWN}" stroke-width="3" stroke-linecap="round" fill="none"/>
    <!-- Lush canopy -->
    <circle cx="24" cy="22" r="10" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="40" cy="20" r="10" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="32" cy="14" r="11" fill="{LIGHT_GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="32" cy="18" r="2" fill="{RED}"/>
    """)

    # 8. Sandalwood Log
    add("nature_08_sandalwood_log", "Aromatic Sandalwood Log", "ಶ್ರೀಗಂಧದ ಕೊರಡು", ["sandalwood", "log", "fragrance"], f"""
    <!-- Log cut in 3D perspective showing dark bark and golden heartwood -->
    <ellipse cx="24" cy="32" rx="10" ry="16" fill="{GOLD}" stroke="{BROWN}" stroke-width="2.5"/>
    <ellipse cx="24" cy="32" rx="6" ry="10" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
    <!-- Tree rings -->
    <circle cx="24" cy="32" r="2" fill="{BROWN}"/>
    <!-- Log side cylinder -->
    <path d="M 24 16 L 46 22 C 54 26 54 38 46 42 L 24 48 Z" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    """)

    # 9. Sandalwood Rubbing Stone (Sane Kallu)
    add("nature_09_sandalwood_paste_stone", "Sandalwood Paste Stone (Sane Kallu)", "ಗಂಧ ತೇಯುವ ಸಾಣೆಕಲ್ಲು", ["sanekallu", "paste", "fragrance", "puja"], f"""
    <!-- Circular stone grinding slab -->
    <ellipse cx="32" cy="40" rx="20" ry="10" fill="{SLATE}" stroke="{DARK}" stroke-width="2.5"/>
    <!-- Golden paste circular ring on stone -->
    <ellipse cx="32" cy="40" rx="12" ry="6" fill="{GOLD}" stroke="{YELLOW}" stroke-width="1.5"/>
    <!-- Sandalwood piece held above it -->
    <polygon points="30,12 36,12 38,36 28,36" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
    """)

    # 10. Bengal Tiger Face
    add("nature_10_bengal_tiger_nagarahole", "Nagarahole Bengal Tiger", "ಬಂಗಾಳ ಹುಲಿ ಮುಖ", ["tiger", "nagarahole", "stripes", "wildlife"], f"""
    <!-- Tiger face contour -->
    <circle cx="32" cy="32" r="18" fill="{ORANGE}" stroke="{DARK}" stroke-width="2"/>
    <!-- Ears -->
    <circle cx="18" cy="18" r="5" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="46" cy="18" r="5" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="18" cy="18" r="2" fill="{DARK}"/>
    <circle cx="46" cy="18" r="2" fill="{DARK}"/>
    <!-- Eyes -->
    <ellipse cx="25" cy="30" rx="2.5" ry="2" fill="{YELLOW}"/>
    <ellipse cx="39" cy="30" rx="2.5" ry="2" fill="{YELLOW}"/>
    <!-- Tiger stripes -->
    <path d="M 32 16 L 32 24 M 22 20 L 26 24 M 42 20 L 38 24 M 18 32 L 23 32 M 46 32 L 41 32" stroke="{DARK}" stroke-width="2"/>
    <!-- White muzzle and nose -->
    <ellipse cx="32" cy="40" rx="6" ry="4" fill="{WHITE}"/>
    <polygon points="30,37 34,37 32,40" fill="{RED}"/>
    """)

    # 11-50 Wildlife, Flora, Fauna batch
    nature_batch = [
        ("nature_11_tiger_walking", "Royal Bengal Tiger Prowling", "ಹುಲಿ ಗಾಂಭೀರ್ಯದ ಹೆಜ್ಜೆ", ["tiger", "prowl", "safari"], f"""
        <ellipse cx="32" cy="32" rx="18" ry="10" fill="{ORANGE}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="48" cy="26" r="6" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Legs -->
        <line x1="20" y1="38" x2="18" y2="52" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>
        <line x1="28" y1="38" x2="26" y2="52" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>
        <line x1="38" y1="38" x2="40" y2="52" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>
        <line x1="46" y1="38" x2="48" y2="52" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>
        <!-- Tail -->
        <path d="M 14 30 Q 8 20 12 14" stroke="{ORANGE}" stroke-width="2.5" fill="none"/>
        """),
        ("nature_12_blackbuck_ranibennur", "Ranibennur Blackbuck", "ರಾಣೆಬೆನ್ನೂರು ಕೃಷ್ಣಮೃಗ", ["blackbuck", "antelope", "ranibennur"], f"""
        <ellipse cx="28" cy="36" rx="14" ry="9" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="40" cy="24" r="5" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Long spiral corkscrew horns -->
        <path d="M 40 20 L 44 8 M 38 20 L 38 6" stroke="{DARK}" stroke-width="2" stroke-linecap="round"/>
        <!-- White underbelly -->
        <path d="M 18 40 Q 28 44 38 40" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <line x1="22" y1="42" x2="20" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <line x1="34" y1="42" x2="36" y2="54" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("nature_13_lion_tailed_macaque", "Lion-Tailed Macaque", "ಸಿಂಹಬಾಲದ ಸಿಂಹಮುಖಿ ಕೋತಿ", ["macaque", "western_ghats", "primate"], f"""
        <!-- Dark monkey head surrounded by glorious silver mane -->
        <circle cx="32" cy="32" r="18" fill="{SILVER}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="32" cy="34" r="10" fill="{DARK}"/>
        <circle cx="28" cy="32" r="1.5" fill="{WHITE}"/>
        <circle cx="36" cy="32" r="1.5" fill="{WHITE}"/>
        <!-- Tufted tail tip -->
        <circle cx="12" cy="20" r="3" fill="{DARK}"/>
        """),
        ("nature_14_malabar_giant_squirrel", "Malabar Giant Squirrel (Shekaru)", "ಶೇಖರು (ಮಲಬಾರ್ ಅಳಿಲು)", ["squirrel", "shekaru", "canopy"], f"""
        <!-- Maroon, buff, and black giant squirrel with huge bushy tail -->
        <ellipse cx="26" cy="34" rx="12" ry="8" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="36" cy="28" r="5" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Massive curved fluffy tail -->
        <path d="M 16 36 C 8 36 6 16 16 12 C 22 10 24 18 20 28" fill="{DARK}" stroke="{BROWN}" stroke-width="2"/>
        <circle cx="38" cy="26" r="1" fill="{DARK}"/>
        """),
        ("nature_15_great_indian_hornbill", "Great Indian Hornbill", "ದಂಡೇಲಿ ಹೆಬ್ಬಕ (ಕಲ್ಮಂಗಟ್ಟೆ)", ["hornbill", "dandeli", "canopy", "bird"], f"""
        <!-- Curved huge beak with yellow casque on top -->
        <path d="M 24 30 C 24 20 32 16 40 18 L 54 28 L 38 34 Z" fill="{GOLD}" stroke="{DARK}" stroke-width="2"/>
        <!-- Black casque top -->
        <rect x="28" y="16" width="14" height="6" rx="2" fill="{RED}"/>
        <circle cx="34" cy="24" r="2" fill="{WHITE}"/>
        <circle cx="34" cy="24" r="1" fill="{DARK}"/>
        <path d="M 24 30 L 16 48 L 26 48 Z" fill="{DARK}"/>
        """),
        ("nature_16_sloth_bear_daroji", "Daroji Sloth Bear", "ದರೋಜಿ ಕರಡಿ", ["slothbear", "daroji", "bellary"], f"""
        <circle cx="32" cy="30" r="16" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="20" cy="18" r="4" fill="{DARK}"/>
        <circle cx="44" cy="18" r="4" fill="{DARK}"/>
        <!-- White V-shaped mark on chest -->
        <path d="M 26 38 L 32 46 L 38 38" stroke="{CREAM}" stroke-width="2.5" fill="none"/>
        <ellipse cx="32" cy="30" rx="5" ry="3" fill="{CREAM}"/>
        <circle cx="32" cy="29" r="1.5" fill="{DARK}"/>
        """),
        ("nature_17_king_cobra_agumbe", "Agumbe King Cobra (Kalinga Sarpa)", "ಕಾಳಿಂಗ ಸರ್ಪ (ಆಗುಂಬೆ)", ["kingcobra", "agumbe", "snake", "hood"], f"""
        <!-- Majestic flared hood with chevron marking -->
        <path d="M 32 14 C 20 20 18 36 26 44 L 26 56 M 32 14 C 44 20 46 36 38 44 L 38 56" stroke="{DARK}" stroke-width="2.5" fill="{GOLD}"/>
        <!-- Cobra head -->
        <ellipse cx="32" cy="20" rx="7" ry="9" fill="{DARK_GOLD}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="29" cy="18" r="1.5" fill="{RED}"/>
        <circle cx="35" cy="18" r="1.5" fill="{RED}"/>
        <!-- Monocle / Chevron on hood -->
        <path d="M 28 28 L 32 34 L 36 28" stroke="{DARK}" stroke-width="2" fill="none"/>
        """),
        ("nature_18_malabar_gliding_frog", "Malabar Gliding Frog", "ಹಾರುವ ಮಲಬಾರ್ ಕಪ್ಪೆ", ["frog", "agumbe", "gliding", "rainforest"], f"""
        <!-- Bright green frog body -->
        <ellipse cx="32" cy="32" rx="12" ry="10" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Bulbous eyes -->
        <circle cx="26" cy="24" r="4" fill="{YELLOW}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="38" cy="24" r="4" fill="{YELLOW}" stroke="{DARK}" stroke-width="1"/>
        <!-- Webbed reddish-orange feet -->
        <polygon points="18,28 10,24 14,34" fill="{ORANGE}"/>
        <polygon points="46,28 54,24 50,34" fill="{ORANGE}"/>
        <polygon points="20,40 12,46 18,48" fill="{ORANGE}"/>
        <polygon points="44,40 52,46 46,48" fill="{ORANGE}"/>
        """),
        ("nature_19_dhole_wild_dog", "Kabini Wild Dog (Dhole)", "ಕಾಡುನಾಯಿ (ಧೋಲೆ)", ["dhole", "wilddog", "kabini"], f"""
        <ellipse cx="30" cy="34" rx="14" ry="9" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="42" cy="24" r="5" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Pointed upright ears -->
        <polygon points="40,20 42,12 46,18" fill="{DARK}"/>
        <!-- Bushy black tail -->
        <path d="M 18 32 Q 10 32 8 42" stroke="{DARK}" stroke-width="3" fill="none"/>
        <line x1="24" y1="42" x2="22" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <line x1="36" y1="42" x2="38" y2="54" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("nature_20_indian_leopard_kabini", "Black Panther / Leopard (Saya)", "ಕಬಿನಿ ಕಪ್ಪು ಚಿರತೆ", ["panther", "leopard", "kabini", "saya"], f"""
        <circle cx="32" cy="30" r="16" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Glowing piercing yellow eyes -->
        <ellipse cx="25" cy="28" rx="3" ry="2" fill="{YELLOW}"/>
        <ellipse cx="39" cy="28" rx="3" ry="2" fill="{YELLOW}"/>
        <circle cx="25" cy="28" r="1" fill="{DARK}"/>
        <circle cx="39" cy="28" r="1" fill="{DARK}"/>
        <!-- Leopard spots faint outline -->
        <circle cx="20" cy="38" r="2" stroke="{SLATE}" fill="none"/>
        <circle cx="44" cy="38" r="2" stroke="{SLATE}" fill="none"/>
        """),
        ("nature_21_gaur_bison", "Indian Gaur (Western Ghats Bison)", "ಕಾಟಿ (ಕಾಡುಕೋಣ)", ["gaur", "bison", "kaati", "horns"], f"""
        <ellipse cx="30" cy="34" rx="16" ry="12" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Muscular dorsal ridge -->
        <path d="M 22 24 Q 30 18 38 24" stroke="{DARK}" stroke-width="4"/>
        <!-- Curved horns with yellow base and black tip -->
        <path d="M 42 24 C 48 18 52 14 50 8 M 42 24 C 44 14 40 8 36 8" stroke="{GOLD}" stroke-width="3" stroke-linecap="round" fill="none"/>
        <circle cx="44" cy="24" r="5" fill="{DARK}"/>
        <!-- White stockings on legs -->
        <line x1="22" y1="46" x2="22" y2="54" stroke="{WHITE}" stroke-width="3"/>
        <line x1="36" y1="46" x2="36" y2="54" stroke="{WHITE}" stroke-width="3"/>
        """),
        ("nature_22_spotted_deer_chital", "Spotted Deer (Chital)", "ಚುಕ್ಕೆ ಜಿಂಕೆ", ["deer", "chital", "bandipur"], f"""
        <ellipse cx="28" cy="36" rx="13" ry="8" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="38" cy="26" r="4.5" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- White spots -->
        <circle cx="24" cy="34" r="1" fill="{WHITE}"/>
        <circle cx="28" cy="36" r="1" fill="{WHITE}"/>
        <circle cx="32" cy="33" r="1" fill="{WHITE}"/>
        <!-- Branched antlers -->
        <path d="M 38 22 L 36 10 M 37 16 L 33 12 M 38 22 L 44 10" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="22" y1="42" x2="20" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <line x1="34" y1="42" x2="36" y2="54" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("nature_23_barking_deer_muntjac", "Barking Deer (Kadu Kuri)", "ಕಾಡು ಕುರಿ (ಮಂಟ್ಜಾಕ್)", ["muntjac", "deer", "barking"], f"""
        <ellipse cx="28" cy="36" rx="12" ry="7" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="38" cy="26" r="4" fill="{ORANGE}"/>
        <!-- Small unbranched antlers and canine tusks -->
        <line x1="38" y1="22" x2="39" y2="14" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="22" y1="42" x2="20" y2="52" stroke="{ORANGE}" stroke-width="2"/>
        <line x1="32" y1="42" x2="34" y2="52" stroke="{ORANGE}" stroke-width="2"/>
        """),
        ("nature_24_sambar_deer", "Western Ghats Sambar Deer", "ಕಡವೆ (ಸಾಂಬಾರ್ ಜಿಂಕೆ)", ["sambar", "kadave", "deer"], f"""
        <ellipse cx="28" cy="36" rx="15" ry="10" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="40" cy="24" r="5" fill="{SLATE}"/>
        <!-- Massive three-tined rugged antlers -->
        <path d="M 40 20 L 40 6 M 40 12 L 34 8 M 40 10 L 46 6" stroke="{DARK}" stroke-width="2"/>
        <line x1="22" y1="44" x2="20" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="36" y1="44" x2="38" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        """),
        ("nature_25_mugger_crocodile_ranganathittu", "Ranganathittu Mugger Crocodile", "ರಂಗನತಿಟ್ಟು ಮೊಸಳೆ", ["crocodile", "mugger", "cauvery", "ranganathittu"], f"""
        <!-- Armored snout and scutes lying on river rock -->
        <ellipse cx="32" cy="34" rx="22" ry="7" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Snout -->
        <polygon points="52,34 58,32 54,36" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="48" cy="31" r="1.5" fill="{YELLOW}"/>
        <!-- Back ridges (Scutes) -->
        <polygon points="20,27 24,24 28,27" fill="{DARK_GOLD}"/>
        <polygon points="28,27 32,24 36,27" fill="{DARK_GOLD}"/>
        <polygon points="36,27 40,24 44,27" fill="{DARK_GOLD}"/>
        <path d="M 12 44 Q 32 48 52 44" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("nature_26_painted_stork_kokkarebellur", "Painted Stork (Kokkare)", "ಬಣ್ಣದ ಕೊಕ್ಕರೆ", ["stork", "kokkarebellur", "bird"], f"""
        <circle cx="28" cy="24" r="5" fill="{WHITE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Yellow curved heavy beak -->
        <polygon points="32,24 48,28 32,27" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="1"/>
        <ellipse cx="24" cy="36" rx="10" ry="7" fill="{WHITE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Pink tip on wing -->
        <path d="M 16 34 L 10 40 L 16 42 Z" fill="{RED}"/>
        <!-- Long yellow stilt legs -->
        <line x1="22" y1="42" x2="20" y2="54" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="26" y1="42" x2="28" y2="54" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("nature_27_spot_billed_pelican", "Spot-Billed Pelican", "ಚಿಕ್ಕ ಕೊಕ್ಕಿನ ಹೆಜ್ಜಾರ್ಲೆ (ಪೆಲಿಕನ್)", ["pelican", "bird", "wetland"], f"""
        <circle cx="28" cy="22" r="5" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Large beak with pouch -->
        <path d="M 32 20 L 48 24 C 42 32 34 32 32 24 Z" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="40" cy="23" r="1" fill="{DARK}"/>
        <ellipse cx="22" cy="36" rx="12" ry="8" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("nature_28_river_otter_tungabhadra", "Tungabhadra Smooth-Coated Otter", "ತುಂಗಭದ್ರಾ ನೀರುನಾಯಿ", ["otter", "river", "tungabhadra"], f"""
        <!-- Sleek swimming otter -->
        <path d="M 14 36 C 18 28 36 26 44 32 C 48 35 50 33 52 30" stroke="{BROWN}" stroke-width="6" stroke-linecap="round" fill="none"/>
        <circle cx="48" cy="32" r="4" fill="{BROWN}"/>
        <circle cx="50" cy="31" r="1" fill="{WHITE}"/>
        <!-- Water waves -->
        <path d="M 10 44 Q 22 40 34 44 Q 46 48 58 44" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("nature_29_mahseer_fish_cauvery", "Cauvery Humpback Mahseer", "ಕಾವೇರಿ ಮಹಶೀರ್ ಮೀನು", ["mahseer", "fish", "cauvery", "angler"], f"""
        <!-- Big game fish with golden scales and dorsal hump -->
        <path d="M 14 32 C 22 22 36 20 48 30 C 36 40 22 40 14 32 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Dorsal hump and fin -->
        <polygon points="26,22 34,16 38,22" fill="{ORANGE}"/>
        <!-- Tail fin -->
        <polygon points="14,32 6,24 6,40" fill="{ORANGE}"/>
        <circle cx="44" cy="28" r="2" fill="{DARK}"/>
        """),
        ("nature_30_hampi_boulder_rock_agama", "Peninsular Rock Agama", "ಬಂಡೆ ಹಲ್ಲಿ (ಅಗಾಮಾ)", ["agama", "lizard", "hampi", "boulder"], f"""
        <!-- Colorful red/orange head and black body -->
        <ellipse cx="32" cy="30" rx="14" ry="6" transform="rotate(-20 32 30)" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="44" cy="24" r="5" fill="{RED}"/>
        <!-- Tail -->
        <path d="M 20 36 Q 10 44 6 52" stroke="{DARK}" stroke-width="2" fill="none"/>
        <!-- Boulder rock base -->
        <ellipse cx="32" cy="48" rx="22" ry="8" fill="{SLATE}"/>
        """),
        ("nature_31_bamboo_groves", "Western Ghats Bamboo Shoots", "ಸಹ್ಯಾದ್ರಿಯ ಬಿದಿರು", ["bamboo", "forest", "culms"], f"""
        <!-- Bamboo stalks with nodes -->
        <line x1="22" y1="56" x2="22" y2="12" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>
        <line x1="18" y1="26" x2="26" y2="26" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="18" y1="40" x2="26" y2="40" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="36" y1="56" x2="36" y2="16" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>
        <line x1="32" y1="30" x2="40" y2="30" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="32" y1="44" x2="40" y2="44" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Slender green leaves -->
        <path d="M 22 26 C 26 22 32 24 34 20" stroke="{LIGHT_GREEN}" stroke-width="2" fill="none"/>
        <path d="M 36 30 C 42 26 48 30 50 26" stroke="{LIGHT_GREEN}" stroke-width="2" fill="none"/>
        """),
        ("nature_32_neelakurinji_flower", "Neelakurinji (12-Year Bloom)", "ನೀಲಕುರಿಂಜಿ ಹೂವು", ["neelakurinji", "bloom", "western_ghats"], f"""
        <!-- Cluster of bell-shaped purplish-blue flowers -->
        <path d="M 32 48 L 32 28" stroke="{GREEN}" stroke-width="2.5"/>
        <circle cx="32" cy="24" r="6" fill="{PURPLE}" stroke="{SKY_BLUE}" stroke-width="1.5"/>
        <circle cx="24" cy="30" r="5" fill="{SKY_BLUE}" stroke="{PURPLE}" stroke-width="1.5"/>
        <circle cx="40" cy="30" r="5" fill="{SKY_BLUE}" stroke="{PURPLE}" stroke-width="1.5"/>
        <circle cx="32" cy="16" r="4" fill="{PURPLE}"/>
        """),
        ("nature_33_brahmakamala_flower", "Brahma Kamala Sacred Blossom", "ಬ್ರಹ್ಮ ಕಮಲ", ["brahmakamala", "sacred", "blossom"], f"""
        <!-- Radiant midnight star flower -->
        <circle cx="32" cy="32" r="6" fill="{GOLD}"/>
        <!-- Pointed starry white petals -->
        <polygon points="32,8 35,24 32,26 29,24" fill="{WHITE}" stroke="{GOLD}" stroke-width="1"/>
        <polygon points="32,56 35,40 32,38 29,40" fill="{WHITE}" stroke="{GOLD}" stroke-width="1"/>
        <polygon points="8,32 24,35 26,32 24,29" fill="{WHITE}" stroke="{GOLD}" stroke-width="1"/>
        <polygon points="56,32 40,35 38,32 40,29" fill="{WHITE}" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("nature_34_coffee_plant_berries", "Coffee Branch with Red Berries", "ಕಾಫಿ ಗಿಡದ ಹಣ್ಣುಗಳು", ["coffee", "berries", "chikmagalur", "coorg"], f"""
        <line x1="14" y1="46" x2="48" y2="16" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <!-- Shiny green leaves -->
        <ellipse cx="24" cy="26" rx="8" ry="4" transform="rotate(-30 24 26)" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <ellipse cx="38" cy="32" rx="8" ry="4" transform="rotate(-30 38 32)" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <!-- Ripe red coffee cherries cluster -->
        <circle cx="28" cy="32" r="3.5" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="34" cy="30" r="3.5" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="30" cy="26" r="3.5" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("nature_35_robusta_coffee_beans", "Roasted Coffee Beans", "ಹುರಿದ ಕಾಫಿ ಬೀಜಗಳು", ["coffee", "beans", "filtercoffee"], f"""
        <!-- Two roasted oval coffee beans with characteristic S-curve center crease -->
        <ellipse cx="26" cy="32" rx="9" ry="13" transform="rotate(-20 26 32)" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 23 21 Q 28 32 25 43" stroke="{DARK}" stroke-width="2" fill="none"/>
        <ellipse cx="40" cy="34" rx="8" ry="11" transform="rotate(35 40 34)" fill="{DARK_GOLD}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 36 25 Q 43 34 40 43" stroke="{DARK}" stroke-width="2" fill="none"/>
        """),
        ("nature_36_cardamom_pod", "Green Cardamom Pods (Yelakki)", "ಏಲಕ್ಕಿ ಕಾಯಿ", ["cardamom", "yelakki", "spice", "malnad"], f"""
        <!-- Ribbed green spindle pods -->
        <ellipse cx="28" cy="32" rx="8" ry="14" transform="rotate(-15 28 32)" fill="{LIGHT_GREEN}" stroke="{GREEN}" stroke-width="2"/>
        <line x1="28" y1="18" x2="28" y2="46" stroke="{GREEN}" stroke-width="1.5"/>
        <ellipse cx="40" cy="36" rx="6" ry="11" transform="rotate(25 40 36)" fill="{LIGHT_GREEN}" stroke="{GREEN}" stroke-width="2"/>
        <line x1="40" y1="25" x2="40" y2="47" stroke="{GREEN}" stroke-width="1.5"/>
        """),
        ("nature_37_black_pepper_vine", "Malnad Black Pepper Vine", "ಕರಿಮೆಣಸು (ಕಾಳುಮೆಣಸು)", ["pepper", "blackpepper", "spice", "vine"], f"""
        <!-- Hanging cluster of peppercorns -->
        <path d="M 32 10 Q 28 20 32 30" stroke="{BROWN}" stroke-width="2.5" fill="none"/>
        <!-- Peppercorn berries -->
        <circle cx="30" cy="20" r="2.5" fill="{DARK}"/>
        <circle cx="35" cy="22" r="2.5" fill="{DARK}"/>
        <circle cx="28" cy="26" r="2.5" fill="{DARK}"/>
        <circle cx="34" cy="28" r="2.5" fill="{DARK}"/>
        <circle cx="31" cy="34" r="2.5" fill="{DARK}"/>
        <circle cx="29" cy="40" r="2.5" fill="{DARK}"/>
        <circle cx="33" cy="44" r="2" fill="{DARK}"/>
        <!-- Green leaf -->
        <ellipse cx="44" cy="18" rx="7" ry="5" fill="{GREEN}"/>
        """),
        ("nature_38_areca_nut_tree", "Areca Nut Palm (Adike Mara)", "ಅಡಿಕೆ ಮರ", ["areca", "adike", "palm"], f"""
        <!-- Tall slender trunk with ring rings -->
        <line x1="32" y1="58" x2="32" y2="18" stroke="{BROWN}" stroke-width="3"/>
        <line x1="30" y1="30" x2="34" y2="30" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="30" y1="42" x2="34" y2="42" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Crown of feather palm fronds -->
        <path d="M 32 18 Q 16 12 12 24 M 32 18 Q 48 12 52 24 M 32 18 Q 32 6 32 4" stroke="{GREEN}" stroke-width="2.5" fill="none"/>
        <circle cx="32" cy="20" r="3" fill="{GOLD}"/>
        """),
        ("nature_39_areca_nut_bunch", "Ripe Betel Nut (Adike)", "ಹಣ್ಣಡಿಕೆ ಗೊಂಚಲು", ["adike", "betelnut", "harvest"], f"""
        <!-- Bright orange-yellow nuts -->
        <circle cx="26" cy="30" r="5" fill="{ORANGE}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="36" cy="28" r="5" fill="{ORANGE}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="38" r="5" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="22" cy="40" r="4.5" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="42" cy="38" r="4.5" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """),
        ("nature_40_tender_coconut_sihi_elaneeru", "Tender Coconut (Sihi Elaneeru)", "ಸಿಹಿ ಎಳನೀರು", ["elaneeru", "coconut", "karavali"], f"""
        <!-- Big green fresh coconut with cut top and straw -->
        <circle cx="32" cy="36" r="18" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <polygon points="26,18 38,18 32,24" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Red drinking straw -->
        <line x1="32" y1="22" x2="42" y2="8" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>
        """),
        ("nature_41_halasina_hannu_jackfruit", "Ripe Jackfruit (Halasina Hannu)", "ಹಲಸಿನ ಹಣ್ಣು", ["jackfruit", "halasu", "fruit"], f"""
        <!-- Large oblong fruit covered in spiky diamond texture -->
        <ellipse cx="32" cy="32" rx="16" ry="22" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Sweet yellow bulb (Tole) cut out -->
        <path d="M 32 24 C 28 28 28 36 32 40 C 36 36 36 28 32 24 Z" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="1.5"/>
        <circle cx="32" cy="32" r="2" fill="{BROWN}"/>
        """),
        ("nature_42_mysore_mallige_jasmine", "Mysore Mallige Jasmine Garland", "ಮೈಸೂರು ಮಲ್ಲಿಗೆ ಹೂವಿನ ದಂಡೆ", ["mallige", "jasmine", "mysore", "gi"], f"""
        <!-- String of fragrant white jasmine buds with green calyx -->
        <circle cx="20" cy="24" r="3.5" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <circle cx="28" cy="22" r="3.5" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <circle cx="36" cy="22" r="3.5" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <circle cx="44" cy="24" r="3.5" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <path d="M 14 36 Q 32 48 50 36" stroke="{GREEN}" stroke-width="3" fill="none"/>
        <circle cx="26" cy="40" r="3" fill="{WHITE}"/>
        <circle cx="32" cy="42" r="3" fill="{WHITE}"/>
        <circle cx="38" cy="40" r="3" fill="{WHITE}"/>
        """),
        ("nature_43_hadagali_mallige", "Hoovina Hadagali Jasmine", "ಹೂವಿನ ಹಡಗಲಿ ಮಲ್ಲಿಗೆ", ["hadagali", "jasmine", "fragrance"], f"""
        <!-- Single blooming delicate star jasmine flower -->
        <circle cx="32" cy="32" r="3" fill="{YELLOW}"/>
        <ellipse cx="32" cy="20" rx="3" ry="8" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <ellipse cx="32" cy="44" rx="3" ry="8" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <ellipse cx="20" cy="32" rx="8" ry="3" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        <ellipse cx="44" cy="32" rx="8" ry="3" fill="{WHITE}" stroke="{SLATE}" stroke-width="1"/>
        """),
        ("nature_44_udupi_mattu_gulla_brinjal", "Udupi Mattu Gulla Brinjal", "ಉಡುಪಿ ಮಟ್ಟು ಗುಳ್ಳ", ["mattugulla", "brinjal", "udupi", "gi"], f"""
        <!-- Round spherical green brinjal with light white streaks -->
        <circle cx="32" cy="36" r="16" fill="{LIGHT_GREEN}" stroke="{GREEN}" stroke-width="2"/>
        <line x1="26" y1="26" x2="26" y2="46" stroke="{WHITE}" stroke-width="1.5"/>
        <line x1="38" y1="26" x2="38" y2="46" stroke="{WHITE}" stroke-width="1.5"/>
        <!-- Spiny green calyx cap & stem -->
        <polygon points="24,24 32,20 40,24 36,28 28,28" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <line x1="32" y1="20" x2="32" y2="12" stroke="{GREEN}" stroke-width="3"/>
        """),
        ("nature_45_devarakadu_sacred_groves", "Devarakadu Sacred Banyan Grove", "ದೇವರಕಾಡು ಆಲದ ಮರ", ["devarakadu", "sacredgrove", "banyan", "coorg"], f"""
        <!-- Massive tree with spreading prop roots -->
        <path d="M 28 54 L 30 36 M 36 54 L 34 36 M 20 54 L 24 38 M 44 54 L 40 38" stroke="{BROWN}" stroke-width="2.5"/>
        <circle cx="32" cy="24" r="16" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Sacred trishula / shrine stone at tree base -->
        <line x1="32" y1="52" x2="32" y2="44" stroke="{RED}" stroke-width="2"/>
        """),
        ("nature_46_teak_wood_leaf", "Dandeli Teak Leaf & Timber", "ದಂಡೇಲಿ ತೇಗದ ಮರ", ["teak", "timber", "dandeli"], f"""
        <!-- Large broad teak leaf with distinct veins -->
        <path d="M 32 12 C 16 18 16 40 32 50 C 48 40 48 18 32 12 Z" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <line x1="32" y1="12" x2="32" y2="56" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="32" y1="24" x2="22" y2="28" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="32" x2="42" y2="36" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """),
        ("nature_47_amrut_mahal_bull", "Amrut Mahal Draught Bull", "ಅಮೃತ ಮಹಲ್ ತಳಿ ಹೋರಿ", ["amrutmahal", "bull", "cattle", "heritage"], f"""
        <circle cx="36" cy="26" r="6" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <ellipse cx="26" cy="36" rx="14" ry="10" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Characteristic long sharp backwards-pointing horns -->
        <path d="M 38 22 C 38 12 30 6 24 4" stroke="{DARK}" stroke-width="2.5" fill="none"/>
        <!-- Prominent hump -->
        <circle cx="28" cy="26" r="4" fill="{SLATE}"/>
        <line x1="20" y1="44" x2="18" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="32" y1="44" x2="34" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        """),
        ("nature_48_hallikar_cattle", "Hallikar Majestic Bull", "ಹಳ್ಳಿಕಾರ್ ಹೋರಿ", ["hallikar", "bull", "native", "karnataka"], f"""
        <ellipse cx="26" cy="36" rx="14" ry="10" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="38" cy="24" r="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Towering swept-back horns -->
        <path d="M 38 20 C 38 8 26 4 20 6" stroke="{SLATE}" stroke-width="3" fill="none"/>
        <circle cx="30" cy="24" r="4" fill="{CREAM}"/>
        <line x1="20" y1="44" x2="18" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="34" y1="44" x2="36" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        """),
        ("nature_49_mudhol_hound", "Mudhol Hound Indigenous Dog", "ಮುಧೋಳ ನಾಯಿ", ["mudhol", "hound", "dog", "indigenous"], f"""
        <!-- Slender aerodynamic sighthound silhouette -->
        <ellipse cx="26" cy="34" rx="13" ry="8" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Narrow sleek head & long muzzle -->
        <path d="M 36 28 L 48 24 L 40 20 Z" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="40" cy="22" r="1" fill="{DARK}"/>
        <!-- Long slender legs -->
        <line x1="18" y1="40" x2="16" y2="54" stroke="{DARK}" stroke-width="2"/>
        <line x1="32" y1="40" x2="34" y2="54" stroke="{DARK}" stroke-width="2"/>
        <!-- Curled whiplash tail -->
        <path d="M 14 32 Q 8 38 10 46" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        """),
        ("nature_50_southern_birdwing_butterfly", "State Butterfly - Southern Birdwing", "ರಾಜ್ಯ ಚಿಟ್ಟೆ - ಸಹ್ಯಾದ್ರಿ ಬರ್ಡ್‌ವಿಂಗ್", ["butterfly", "birdwing", "statebutterfly"], f"""
        <!-- Large black forewings and brilliant golden-yellow hindwings -->
        <path d="M 32 30 L 10 14 C 12 28 20 34 30 36 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
        <path d="M 32 30 L 54 14 C 52 28 44 34 34 36 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Golden-yellow hindwings -->
        <ellipse cx="24" cy="40" rx="7" ry="10" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <ellipse cx="40" cy="40" rx="7" ry="10" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Slender thorax -->
        <line x1="32" y1="20" x2="32" y2="44" stroke="{DARK}" stroke-width="2.5"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in nature_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
