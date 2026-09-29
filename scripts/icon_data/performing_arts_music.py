"""
Category 4: Traditional Performing Arts, Dance & Music (50 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "performing-arts-music",
            "tags": ["arts", "dance", "music", "folklore", "yakshagana", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Yakshagana Tenkutittu Kireeta
    add("arts_01_yakshagana_tenkutittu_kireeta", "Yakshagana Tenkutittu Kireeta", "ಯಕ್ಷಗಾನ ತೆಂಕುತಿಟ್ಟು ಕಿರೀಟ", ["yakshagana", "tenkutittu", "kireeta", "crown"], f"""
    <!-- Ornate tiered golden crown with red and green mirrors -->
    <polygon points="32,8 14,46 50,46" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <polygon points="32,16 20,40 44,40" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Headband base -->
    <rect x="12" y="46" width="40" height="8" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="20" cy="50" r="2" fill="{YELLOW}"/>
    <circle cx="32" cy="50" r="2" fill="{YELLOW}"/>
    <circle cx="44" cy="50" r="2" fill="{YELLOW}"/>
    <!-- Top finial kalasa -->
    <circle cx="32" cy="6" r="2.5" fill="{RED}"/>
    """)

    # 2. Yakshagana Badagutittu Kireeta
    add("arts_02_yakshagana_badagutittu_kireeta", "Yakshagana Badagutittu Kireeta", "ಯಕ್ಷಗಾನ ಬಡಗುತಿಟ್ಟು ಕಿರೀಟ", ["yakshagana", "badagutittu", "turban", "crown"], f"""
    <!-- Large disc/turban shaped Badagu crown with red-gold radiant border -->
    <ellipse cx="32" cy="30" rx="22" ry="16" fill="{YELLOW}" stroke="{GOLD}" stroke-width="2.5"/>
    <circle cx="32" cy="30" r="10" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="32" cy="30" r="4" fill="{YELLOW}"/>
    <!-- Crown headband -->
    <rect x="18" y="44" width="28" height="8" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <line x1="32" y1="14" x2="32" y2="6" stroke="{GOLD}" stroke-width="2.5"/>
    <circle cx="32" cy="5" r="2" fill="{RED}"/>
    """)

    # 3. Yakshagana Raja Vesha
    add("arts_03_yakshagana_raja_vesha", "Yakshagana Raja Vesha Makeup", "ಯಕ್ಷಗಾನ ರಾಜ ವೇಷ", ["raja", "vesha", "makeup", "character"], f"""
    <circle cx="32" cy="34" r="16" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Tilaka on forehead -->
    <path d="M 32 22 L 32 30 M 28 26 L 36 26" stroke="{RED}" stroke-width="2"/>
    <!-- Painted curved eyes & mustache -->
    <path d="M 22 32 Q 26 28 30 32 M 34 32 Q 38 28 42 32" stroke="{DARK}" stroke-width="2" fill="none"/>
    <path d="M 22 40 Q 32 46 42 40" stroke="{DARK}" stroke-width="2.5" fill="none"/>
    <!-- Miniature crown atop -->
    <polygon points="32,8 22,20 42,20" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
    """)

    # 4. Yakshagana Bannada Vesha (Demon)
    add("arts_04_yakshagana_bannada_vesha", "Yakshagana Bannada Vesha (Demon)", "ಯಕ್ಷಗಾನ ಬಣ್ಣದ ವೇಷ (ರಾಕ್ಷಸ)", ["demon", "rakshasa", "fierce", "bannada"], f"""
    <!-- Red and black fierce demon face with white chutti knobs -->
    <circle cx="32" cy="34" r="18" fill="{RED}" stroke="{DARK}" stroke-width="2.5"/>
    <!-- White pith knobs (Chutti) on nose and forehead -->
    <circle cx="32" cy="30" r="3" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <circle cx="32" cy="22" r="2.5" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <circle cx="24" cy="38" r="2.5" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <circle cx="40" cy="38" r="2.5" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <!-- Fierce eyes and fangs -->
    <ellipse cx="24" cy="28" rx="3" ry="2" fill="{YELLOW}"/>
    <ellipse cx="40" cy="28" rx="3" ry="2" fill="{YELLOW}"/>
    <path d="M 24 44 L 27 40 L 37 40 L 40 44" stroke="{WHITE}" stroke-width="2.5" fill="none"/>
    """)

    # 5. Yakshagana Krishna Morpankhi
    add("arts_05_yakshagana_krishna_morpankhi", "Yakshagana Krishna Headdress", "ಯಕ್ಷಗಾನ ಕೃಷ್ಣನ ಕಿರೀಟ ಮತ್ತು ನವಿಲುಗರಿ", ["krishna", "peacock", "morpankhi"], f"""
    <circle cx="32" cy="38" r="12" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Headband -->
    <rect x="22" y="30" width="20" height="6" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
    <!-- Majestic Peacock Feather on crown -->
    <path d="M 32 30 C 26 18 30 8 32 6 C 34 8 38 18 32 30 Z" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <ellipse cx="32" cy="14" rx="3" ry="5" fill="{SKY_BLUE}"/>
    <circle cx="32" cy="14" r="1.5" fill="{GOLD}"/>
    """)

    # 6. Yakshagana Stree Vesha
    add("arts_06_yakshagana_stree_vesha", "Yakshagana Stree Vesha (Female Character)", "ಯಕ್ಷಗಾನ ಸ್ತ್ರೀ ವೇಷ", ["stree", "female", "jewelry"], f"""
    <circle cx="32" cy="34" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Bindi and hair braid -->
    <circle cx="32" cy="26" r="2" fill="{RED}"/>
    <path d="M 22 28 C 22 18 42 18 42 28" stroke="{DARK}" stroke-width="3" fill="none"/>
    <!-- Ornate forehead jhumki -->
    <circle cx="32" cy="22" r="2" fill="{GOLD}"/>
    <circle cx="16" cy="36" r="3" fill="{GOLD}"/>
    <circle cx="48" cy="36" r="3" fill="{GOLD}"/>
    """)

    # 7. Yakshagana Chande Drum
    add("arts_07_yakshagana_chande", "Yakshagana Chande Drum", "ಯಕ್ಷಗಾನ ಚಂಡೆ", ["chande", "drum", "percussion"], f"""
    <!-- Vertical high-pitch cylinder drum -->
    <rect x="22" y="16" width="20" height="34" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    <ellipse cx="32" cy="16" rx="10" ry="3" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
    <ellipse cx="32" cy="50" rx="10" ry="3" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Tight zigzag cords -->
    <path d="M 22 16 L 32 33 L 22 50 M 42 16 L 32 33 L 42 50" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
    <!-- Drumsticks (Kolu) -->
    <line x1="12" y1="12" x2="26" y2="18" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    <line x1="52" y1="12" x2="38" y2="18" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    """)

    # 8. Yakshagana Maddale Drum
    add("arts_08_yakshagana_maddale", "Yakshagana Maddale Drum", "ಯಕ್ಷಗಾನ ಮದ್ದಳೆ", ["maddale", "drum", "percussion"], f"""
    <!-- Horizontal barrel drum -->
    <ellipse cx="32" cy="34" rx="20" ry="12" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    <ellipse cx="12" cy="34" rx="3" ry="9" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
    <ellipse cx="52" cy="34" rx="3" ry="9" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Black ink spot (Karani) on right head -->
    <circle cx="52" cy="34" r="4" fill="{DARK}"/>
    <line x1="15" y1="26" x2="49" y2="26" stroke="{GOLD}" stroke-width="1.5"/>
    <line x1="15" y1="42" x2="49" y2="42" stroke="{GOLD}" stroke-width="1.5"/>
    """)

    # 9. Yakshagana Tala Cymbals
    add("arts_09_yakshagana_tala", "Yakshagana Tala Cymbals", "ಯಕ್ಷಗಾನ ತಾಳ", ["tala", "cymbals", "bronze"], f"""
    <!-- Pair of thick bronze cymbals linked with red cord -->
    <circle cx="24" cy="32" r="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <circle cx="40" cy="32" r="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <circle cx="24" cy="32" r="3" fill="{RED}"/>
    <circle cx="40" cy="32" r="3" fill="{RED}"/>
    <!-- Connecting cord -->
    <path d="M 24 32 Q 32 18 40 32" stroke="{RED}" stroke-width="2" fill="none"/>
    """)

    # 10. Yakshagana Dancing Bells (Gejje)
    add("arts_10_yakshagana_gejje", "Dancing Ankle Bells (Gejje)", "ನಾಟ್ಯದ ಗೆಜ್ಜೆ", ["gejje", "anklet", "bells"], f"""
    <!-- Leather strap with rows of brass bells -->
    <rect x="14" y="24" width="36" height="16" rx="3" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
    <!-- Bells -->
    <circle cx="20" cy="29" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="28" cy="29" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="36" cy="29" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="44" cy="29" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="20" cy="35" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="28" cy="35" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="36" cy="35" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="44" cy="35" r="2.5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <!-- Tie cords -->
    <line x1="8" y1="32" x2="14" y2="32" stroke="{BROWN}" stroke-width="2"/>
    <line x1="50" y1="32" x2="56" y2="32" stroke="{BROWN}" stroke-width="2"/>
    """)

    # 11-50 Performing Arts & Music (Dollu, Veeragase, Kamsale, Bhoota Kola, Carnatic, Instruments)
    arts_batch = [
        ("arts_11_dollu_drum", "Dollu Folk Drum", "ಡೊಳ್ಳು", ["dollu", "drum", "folk"], f"""
        <ellipse cx="32" cy="34" rx="22" ry="14" fill="{BROWN}" stroke="{DARK}" stroke-width="2.5"/>
        <ellipse cx="10" cy="34" rx="3" ry="12" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="54" cy="34" rx="3" ry="12" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <!-- Red cloth sling strap -->
        <path d="M 16 26 Q 32 10 48 26" stroke="{RED}" stroke-width="3" fill="none"/>
        <line x1="16" y1="34" x2="48" y2="34" stroke="{GOLD}" stroke-width="2"/>
        """),
        ("arts_12_dollu_kunitha_dancer", "Dollu Kunitha Dancer", "ಡೊಳ್ಳು ಕುಣಿತ ಕಲಾವಿದ", ["dollu", "dancer", "kunitha"], f"""
        <circle cx="32" cy="14" r="4" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <path d="M 26 12 Q 32 8 38 12" stroke="{RED}" stroke-width="2"/>
        <!-- Drum tied across hips -->
        <rect x="22" y="28" width="20" height="10" rx="3" fill="{BROWN}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Energetic leaping legs -->
        <path d="M 24 38 L 18 52 M 40 38 L 46 50" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Arms striking drum -->
        <path d="M 22 22 L 24 30 M 42 22 L 40 30" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
        """),
        ("arts_13_veeragase_sword_dancer", "Veeragase Warrior Dancer", "ವೀರಗಾಸೆ ನರ್ತಕ", ["veeragase", "dancer", "sword"], f"""
        <circle cx="32" cy="14" r="4" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <polygon points="32,6 26,12 38,12" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Body with red costume -->
        <path d="M 32 18 L 32 36 L 22 52 M 32 36 L 42 52" stroke="{RED}" stroke-width="3" stroke-linecap="round"/>
        <!-- Wooden sword in right hand -->
        <line x1="42" y1="20" x2="52" y2="12" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="22" y1="24" x2="14" y2="28" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arts_14_veeragase_rudraksha_vibhuti", "Veeragase Vibhuti & Rudraksha", "ವೀರಗಾಸೆ ವಿಭೂತಿ ಮತ್ತು ರುದ್ರಾಕ್ಷಿ", ["vibhuti", "rudraksha", "shiva"], f"""
        <!-- 3 Horizontal Vibhuti lines -->
        <line x1="16" y1="24" x2="48" y2="24" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>
        <line x1="16" y1="32" x2="48" y2="32" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>
        <line x1="16" y1="40" x2="48" y2="40" stroke="{WHITE}" stroke-width="4" stroke-linecap="round"/>
        <!-- Red Kumkuma dot in center -->
        <circle cx="32" cy="32" r="3" fill="{RED}"/>
        <!-- Rudraksha beads hanging garland -->
        <path d="M 18 46 Q 32 58 46 46" stroke="{BROWN}" stroke-width="3" fill="none" stroke-dasharray="3 3"/>
        """),
        ("arts_15_veeragase_kireeta", "Veeragase Serpent Crown", "ವೀರಗಾಸೆ ಕಿರೀಟ", ["veeragase", "crown", "serpent"], f"""
        <polygon points="32,10 18,36 46,36" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Serpent hood on top -->
        <path d="M 32 10 C 28 6 36 6 32 2" stroke="{RED}" stroke-width="2" fill="none"/>
        <rect x="16" y="36" width="32" height="6" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="24" r="3" fill="{RED}"/>
        """),
        ("arts_16_kamsale_cymbals", "Kamsale Bronze Cymbals", "ಕಂಸಾಳೆ", ["kamsale", "cymbals", "male_madeshwara"], f"""
        <!-- Deep cup-shaped bronze cymbal with handle and flat plate -->
        <circle cx="24" cy="32" r="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <path d="M 36 24 C 44 24 46 40 38 40 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="24" cy="32" r="3" fill="{RED}"/>
        <!-- Clashing motion sparks -->
        <line x1="32" y1="22" x2="32" y2="16" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="30" y1="44" x2="28" y2="48" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("arts_17_kamsale_dance_posture", "Kamsale Dance Posture", "ಕಂಸಾಳೆ ನೃತ್ಯ ಭಂಗಿ", ["kamsale", "posture", "rhythm"], f"""
        <circle cx="32" cy="14" r="4" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Body leaning in rhythm -->
        <path d="M 32 18 L 30 36 L 20 52 M 30 36 L 40 50" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Arms arched overhead clashing cymbals -->
        <path d="M 30 22 C 22 14 26 6 32 8 C 38 6 42 14 34 22" stroke="{GOLD}" stroke-width="2.5" fill="none"/>
        <circle cx="32" cy="7" r="2.5" fill="{RED}"/>
        """),
        ("arts_18_bhoota_kola_mask", "Bhoota Kola Kantara Divine Mask", "ಭೂತ ಕೋಲ ಕಾಂತಾರ ದೈವ ಮುಖವಾಡ", ["bhootakola", "kantara", "daiva", "panjurli"], f"""
        <!-- Divine spirit face with huge circular halo and tusks -->
        <circle cx="32" cy="32" r="22" stroke="{GOLD}" stroke-width="2" stroke-dasharray="2 2" fill="none"/>
        <circle cx="32" cy="32" r="16" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Divine third eye & tilaka -->
        <ellipse cx="32" cy="24" rx="2" ry="4" fill="{YELLOW}"/>
        <circle cx="26" cy="32" r="2" fill="{WHITE}"/>
        <circle cx="38" cy="32" r="2" fill="{WHITE}"/>
        <!-- Boar/Spirit tusks curving up -->
        <path d="M 22 40 C 20 34 24 30 25 36 M 42 40 C 44 34 40 30 39 36" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <!-- Red tongue / divine smile -->
        <path d="M 28 42 Q 32 46 36 42" stroke="{YELLOW}" stroke-width="2" fill="none"/>
        """),
        ("arts_19_bhoota_kola_pingara", "Areca Palm Flower (Pingara)", "ಹಿಂಗಾರ / ಪಿಂಗಾರ", ["pingara", "areca", "flower", "daivaradhane"], f"""
        <!-- Bunch of fragrant cream-white areca palm blossoms -->
        <path d="M 32 56 L 32 30" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <!-- Spikes of florets -->
        <path d="M 32 30 C 20 22 22 10 28 8 M 32 30 C 32 18 32 8 32 6 M 32 30 C 44 22 42 10 36 8" stroke="{CREAM}" stroke-width="3" stroke-linecap="round" fill="none"/>
        <circle cx="28" cy="8" r="2" fill="{YELLOW}"/>
        <circle cx="32" cy="6" r="2" fill="{YELLOW}"/>
        <circle cx="36" cy="8" r="2" fill="{YELLOW}"/>
        """),
        ("arts_20_bhoota_kola_flame_torch", "Sacred Flame Torch (Deevarige)", "ದೀವರsample / ಪಂಜು", ["torch", "flame", "panju", "fire"], f"""
        <line x1="32" y1="58" x2="32" y2="28" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>
        <!-- Torch head -->
        <rect x="26" y="24" width="12" height="8" rx="2" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Flaming Fire -->
        <path d="M 32 6 C 24 14 26 22 32 24 C 38 22 40 14 32 6 Z" fill="{YELLOW}" stroke="{RED}" stroke-width="2"/>
        <path d="M 32 12 C 28 16 28 20 32 22 C 36 20 36 16 32 12 Z" fill="{RED}"/>
        """),
        ("arts_21_bhoota_kola_siri_skirt", "Tender Palm Skirt (Siri)", "ಸಿರಿ ತೆಂಗಿನ ಗರಿಯ ಉಡುಪು", ["siri", "coconut", "costume"], f"""
        <!-- Waistband -->
        <rect x="18" y="22" width="28" height="6" rx="2" fill="{GOLD}" stroke="{GREEN}" stroke-width="1.5"/>
        <!-- Pleated tender coconut fronds hanging down -->
        <line x1="20" y1="28" x2="16" y2="54" stroke="{LIGHT_GREEN}" stroke-width="2"/>
        <line x1="24" y1="28" x2="22" y2="54" stroke="{GREEN}" stroke-width="2"/>
        <line x1="28" y1="28" x2="28" y2="54" stroke="{LIGHT_GREEN}" stroke-width="2"/>
        <line x1="32" y1="28" x2="32" y2="54" stroke="{GREEN}" stroke-width="2"/>
        <line x1="36" y1="28" x2="36" y2="54" stroke="{LIGHT_GREEN}" stroke-width="2"/>
        <line x1="40" y1="28" x2="42" y2="54" stroke="{GREEN}" stroke-width="2"/>
        <line x1="44" y1="28" x2="48" y2="54" stroke="{LIGHT_GREEN}" stroke-width="2"/>
        """),
        ("arts_22_pooja_kunitha_pot_tower", "Pooja Kunitha Floral Tower", "ಪೂಜಾ ಕುಣಿತ ಕಳಶ ಗೋಪುರ", ["pooja", "kunitha", "tower", "folk"], f"""
        <circle cx="32" cy="50" r="4" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Tall bamboo frame balanced on head -->
        <rect x="26" y="10" width="12" height="36" fill="{GOLD}" stroke="{RED}" stroke-width="2"/>
        <polygon points="32,4 24,10 40,10" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="3" r="1.5" fill="{YELLOW}"/>
        <!-- Floral tiers -->
        <line x1="22" y1="18" x2="42" y2="18" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="22" y1="26" x2="42" y2="26" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="22" y1="34" x2="42" y2="34" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("arts_23_goravara_kunitha_cap", "Goravara Bearskin Cap (Karadi Topi)", "ಗೊರವರ ಕರಡಿ ಚರ್ಮದ ಟೋಪಿ", ["goravara", "bearskin", "topi", "cap"], f"""
        <!-- Fluffy black cap -->
        <path d="M 18 42 C 14 22 50 22 46 42 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Vibhuti band across cap -->
        <line x1="20" y1="36" x2="44" y2="36" stroke="{WHITE}" stroke-width="2"/>
        <!-- Damaru & flute tied to it -->
        <circle cx="32" cy="42" r="3" fill="{RED}"/>
        """),
        ("arts_24_goravara_damaruga", "Goravara Damaruga Drum", "ಡಮರುಗ", ["damaruga", "drum", "shiva"], f"""
        <!-- Hourglass drum -->
        <polygon points="20,16 44,16 32,32" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <polygon points="20,48 44,48 32,32" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="32" cy="32" r="2" fill="{GOLD}"/>
        <!-- Knotted striker beads -->
        <path d="M 32 32 Q 22 30 18 36" stroke="{RED}" stroke-width="1.5" fill="none"/>
        <circle cx="17" cy="37" r="2" fill="{GOLD}"/>
        <path d="M 32 32 Q 42 34 46 28" stroke="{RED}" stroke-width="1.5" fill="none"/>
        <circle cx="47" cy="27" r="2" fill="{GOLD}"/>
        """),
        ("arts_25_goravara_pillangovi", "Sacred Bamboo Flute (Pillangovi)", "ಪಿಳ್ಳಂಗೋವಿ", ["flute", "pillangovi", "bamboo"], f"""
        <line x1="10" y1="32" x2="54" y2="32" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>
        <!-- 6 Finger holes -->
        <circle cx="22" cy="32" r="1.5" fill="{YELLOW}"/>
        <circle cx="27" cy="32" r="1.5" fill="{YELLOW}"/>
        <circle cx="32" cy="32" r="1.5" fill="{YELLOW}"/>
        <circle cx="37" cy="32" r="1.5" fill="{YELLOW}"/>
        <circle cx="42" cy="32" r="1.5" fill="{YELLOW}"/>
        <circle cx="47" cy="32" r="1.5" fill="{YELLOW}"/>
        <!-- Mouth hole -->
        <circle cx="15" cy="32" r="2" fill="{DARK}"/>
        """),
        ("arts_26_somana_kunitha_red_mask", "Somana Kunitha Red Mask", "ಸೋಮನ ಕುಣಿತ ಕೆಂಪು ಮುಖವಾಡ", ["somana", "mask", "red", "folk"], f"""
        <path d="M 16 16 C 16 8 48 8 48 16 L 46 44 C 46 54 18 54 18 44 Z" fill="{RED}" stroke="{DARK}" stroke-width="2.5"/>
        <circle cx="26" cy="28" r="3" fill="{YELLOW}"/>
        <circle cx="38" cy="28" r="3" fill="{YELLOW}"/>
        <path d="M 26 40 Q 32 46 38 40" stroke="{DARK}" stroke-width="2.5" fill="none"/>
        <!-- Feather crown fan above -->
        <path d="M 20 16 C 24 6 40 6 44 16" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("arts_27_somana_kunitha_yellow_mask", "Somana Kunitha Yellow Mask", "ಸೋಮನ ಕುಣಿತ ಹಳದಿ ಮುಖವಾಡ", ["somana", "yellow", "mask", "serene"], f"""
        <path d="M 16 16 C 16 8 48 8 48 16 L 46 44 C 46 54 18 54 18 44 Z" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="2.5"/>
        <circle cx="26" cy="28" r="3" fill="{RED}"/>
        <circle cx="38" cy="28" r="3" fill="{RED}"/>
        <path d="M 28 38 Q 32 42 36 38" stroke="{RED}" stroke-width="2" fill="none"/>
        """),
        ("arts_28_karaga_floral_cone", "Bangalore Karaga Floral Pot", "ಬೆಂಗಳೂರು ಕರಗ ಕಳಶ", ["karaga", "bangalore", "jasmine", "shakthi"], f"""
        <!-- Floral pyramid cone carried on head -->
        <polygon points="32,6 18,38 46,38" fill="{YELLOW}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="4" r="2" fill="{RED}"/>
        <!-- Jasmine flower garland loops -->
        <path d="M 22 28 Q 32 34 42 28" stroke="{WHITE}" stroke-width="3" fill="none"/>
        <path d="M 26 20 Q 32 24 38 20" stroke="{WHITE}" stroke-width="3" fill="none"/>
        <!-- Water pot (Kumbha) base -->
        <ellipse cx="32" cy="44" rx="10" ry="6" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="20" y1="52" x2="44" y2="52" stroke="{RED}" stroke-width="2.5"/>
        """),
        ("arts_29_karaga_veerakumara_sword", "Karaga Veerakumara Sword", "ಕರಗ ವೀರಕುಮಾರ ಕತ್ತಿ", ["veerakumara", "sword", "karaga"], f"""
        <line x1="16" y1="48" x2="48" y2="16" stroke="{SILVER}" stroke-width="3" stroke-linecap="round"/>
        <circle cx="14" cy="50" r="3" fill="{GOLD}"/>
        <!-- Floral garland around hilt -->
        <circle cx="20" cy="44" r="2.5" fill="{RED}"/>
        <circle cx="24" cy="40" r="2.5" fill="{YELLOW}"/>
        """),
        ("arts_30_mysore_veena", "Mysore Saraswati Veena", "ಮೈಸೂರು ವೀಣೆ", ["veena", "saraswati", "carnatic", "strings"], f"""
        <!-- Main resonator body -->
        <circle cx="44" cy="38" r="12" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Fretboard neck -->
        <line x1="44" y1="38" x2="16" y2="18" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>
        <!-- Frets -->
        <line x1="34" y1="27" x2="36" y2="31" stroke="{GOLD}" stroke-width="2"/>
        <line x1="28" y1="23" x2="30" y2="27" stroke="{GOLD}" stroke-width="2"/>
        <line x1="22" y1="19" x2="24" y2="23" stroke="{GOLD}" stroke-width="2"/>
        <!-- Secondary gourd resonator -->
        <circle cx="18" cy="26" r="6" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <!-- Yali Dragon Head terminal -->
        <path d="M 14 18 C 10 16 10 12 14 10" stroke="{GOLD}" stroke-width="2.5" fill="none"/>
        """),
        ("arts_31_veena_yali_head", "Veena Yali Dragon Terminal", "ವೀಣೆಯ ಯಾಳಿ ಮುಖ", ["yali", "veena", "sculpture"], f"""
        <path d="M 20 44 C 14 36 16 20 28 16 C 36 12 44 18 42 28 C 40 36 32 40 32 46" stroke="{GOLD}" stroke-width="3" fill="none"/>
        <circle cx="34" cy="22" r="2.5" fill="{RED}"/>
        <path d="M 38 26 L 46 24 L 40 30" stroke="{RED}" stroke-width="2" fill="none"/>
        """),
        ("arts_32_carnatic_tambura", "Carnatic Tambura (Drone)", "ತಂಬೂರಿ", ["tambura", "tanpura", "drone"], f"""
        <circle cx="32" cy="46" r="12" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Long neck -->
        <line x1="32" y1="34" x2="32" y2="8" stroke="{BROWN}" stroke-width="3"/>
        <!-- Pegs -->
        <circle cx="28" cy="12" r="2" fill="{GOLD}"/>
        <circle cx="36" cy="12" r="2" fill="{GOLD}"/>
        <circle cx="28" cy="16" r="2" fill="{GOLD}"/>
        <circle cx="36" cy="16" r="2" fill="{GOLD}"/>
        <line x1="31" y1="8" x2="31" y2="46" stroke="{GOLD}" stroke-width="1"/>
        <line x1="33" y1="8" x2="33" y2="46" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("arts_33_carnatic_mridangam", "Carnatic Mridangam Drum", "ಮೃದಂಗ", ["mridangam", "carnatic", "percussion"], f"""
        <ellipse cx="32" cy="32" rx="20" ry="11" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="12" cy="32" rx="3" ry="9" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <ellipse cx="52" cy="32" rx="3" ry="9" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="52" cy="32" r="4" fill="{DARK}"/>
        <line x1="15" y1="25" x2="49" y2="25" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="15" y1="39" x2="49" y2="39" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("arts_34_carnatic_ghatam", "Clay Ghatam Pot", "ಘಟ", ["ghatam", "pot", "clay"], f"""
        <circle cx="32" cy="36" r="16" fill="{ORANGE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Rim at top -->
        <ellipse cx="32" cy="20" rx="8" ry="3" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="34" r="3" fill="rgba(0,0,0,0.1)"/>
        """),
        ("arts_35_carnatic_kanjira", "Kanjira Tambourine", "ಕಂಜೀರ", ["kanjira", "tambourine", "frame"], f"""
        <circle cx="32" cy="32" r="18" fill="{CREAM}" stroke="{BROWN}" stroke-width="3"/>
        <!-- Brass jingle coins inserted in wooden rim -->
        <ellipse cx="46" cy="24" rx="2" ry="4" fill="{GOLD}"/>
        <ellipse cx="46" cy="40" rx="2" ry="4" fill="{GOLD}"/>
        """),
        ("arts_36_carnatic_morsing", "Morsing (Jaw Harp)", "ಮೋರ್ಸಿಂಗ್", ["morsing", "jawharp", "metal"], f"""
        <!-- Horseshoe shaped metal ring with vibrating tongue -->
        <circle cx="26" cy="32" r="12" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
        <line x1="38" y1="26" x2="52" y2="26" stroke="{SLATE}" stroke-width="2"/>
        <line x1="38" y1="38" x2="52" y2="38" stroke="{SLATE}" stroke-width="2"/>
        <line x1="20" y1="32" x2="56" y2="32" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="56" cy="32" r="2" fill="{RED}"/>
        """),
        ("arts_37_chipla_cymbals", "Chipla Cymbals (Purandara Dasa)", "ಚಿಪ್ಲ", ["chipla", "purandaradasa", "cymbals"], f"""
        <!-- Pair of wooden castanets with brass ring bells -->
        <rect x="18" y="22" width="28" height="8" rx="2" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="24" cy="26" r="2" fill="{GOLD}"/>
        <circle cx="40" cy="26" r="2" fill="{GOLD}"/>
        <rect x="18" y="34" width="28" height="8" rx="2" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="24" cy="38" r="2" fill="{GOLD}"/>
        <circle cx="40" cy="38" r="2" fill="{GOLD}"/>
        """),
        ("arts_38_purandara_dasa_silhouette", "Purandara Dasa with Tambura", "ಪುರಂದರದಾಸರು", ["purandara", "dasa", "carnatic"], f"""
        <circle cx="28" cy="18" r="4" fill="{GOLD}"/>
        <!-- Seated saint holding tambura -->
        <path d="M 28 22 L 26 36 L 18 50 L 38 50 L 34 36 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Tambura held vertically -->
        <line x1="38" y1="12" x2="38" y2="48" stroke="{BROWN}" stroke-width="2.5"/>
        <circle cx="38" cy="48" r="5" fill="{GOLD}"/>
        """),
        ("arts_39_kanaka_dasa_dhyana", "Kanaka Dasa in Dhyana", "ಕನಕದಾಸರು", ["kanakadasa", "dhyana", "saint"], f"""
        <circle cx="32" cy="16" r="5" fill="{GOLD}"/>
        <!-- Turban -->
        <ellipse cx="32" cy="14" rx="6" ry="3" fill="{RED}"/>
        <!-- Seated in deep prayer -->
        <path d="M 24 30 L 16 48 L 48 48 L 40 30 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <path d="M 28 34 L 32 38 L 36 34" stroke="{SLATE}" stroke-width="2" fill="none"/>
        """),
        ("arts_40_vachana_singer_ektara", "Vachana Singer with Ektara", "ವಚನ ಗಾಯಕ ಏಕತಾರಿ", ["vachana", "ektara", "sharanas"], f"""
        <circle cx="28" cy="16" r="4" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="42" y1="10" x2="42" y2="52" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <circle cx="42" cy="46" r="7" fill="{GOLD}"/>
        <line x1="28" y1="20" x2="28" y2="48" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arts_41_nagaswaram", "Temple Nadaswaram Pipe", "ನಾದಸ್ವರ", ["nagaswara", "nadaswaram", "temple"], f"""
        <polygon points="32,8 28,46 36,46" fill="{DARK}" stroke="{BROWN}" stroke-width="1.5"/>
        <!-- Flared brass bell at bottom -->
        <path d="M 26 46 L 22 56 L 42 56 L 38 46 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Reed at top -->
        <line x1="32" y1="8" x2="32" y2="4" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="20" r="1" fill="{CREAM}"/>
        <circle cx="32" cy="26" r="1" fill="{CREAM}"/>
        <circle cx="32" cy="32" r="1" fill="{CREAM}"/>
        <circle cx="32" cy="38" r="1" fill="{CREAM}"/>
        """),
        ("arts_42_thavil_drum", "Temple Thavil Drum", "ತವಿಲ್", ["thavil", "drum", "temple"], f"""
        <ellipse cx="32" cy="32" rx="16" ry="13" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="16" cy="32" rx="2" ry="11" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <ellipse cx="48" cy="32" rx="2" ry="11" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Thick leather band strap -->
        <line x1="18" y1="22" x2="46" y2="22" stroke="{GOLD}" stroke-width="2"/>
        <line x1="18" y1="42" x2="46" y2="42" stroke="{GOLD}" stroke-width="2"/>
        """),
        ("arts_43_kahale_kombu_curved_horn", "Temple S-Horn (Kombu Kahale)", "ಕೊಂಬು ಕಹಳೆ", ["kombu", "kahale", "brass"], f"""
        <path d="M 16 52 C 26 44 26 28 38 24 C 46 20 48 12 50 8" stroke="{GOLD}" stroke-width="4" fill="none" stroke-linecap="round"/>
        <circle cx="50" cy="8" r="3" fill="{YELLOW}"/>
        <circle cx="16" cy="52" r="2" fill="{RED}"/>
        """),
        ("arts_44_tamate_folk_drum", "Tamate Folk Frame Drum", "ತಮಟೆ", ["tamate", "drum", "folk"], f"""
        <circle cx="32" cy="32" r="20" fill="{CREAM}" stroke="{BROWN}" stroke-width="3"/>
        <circle cx="32" cy="32" r="16" stroke="{SLATE}" stroke-width="1" stroke-dasharray="2 2" fill="none"/>
        <!-- Curved stick striker -->
        <path d="M 12 18 Q 24 22 28 30" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
        """),
        ("arts_45_jaggalage_wheel_drum", "Jaggalage Giant Wheel Drum", "ಜಗ್ಗಲಿಗೆ", ["jaggalage", "drum", "wheel", "dharwad"], f"""
        <!-- Massive cart wheel with buffalo hide -->
        <circle cx="32" cy="32" r="22" stroke="{BROWN}" stroke-width="3.5" fill="{CREAM}"/>
        <circle cx="32" cy="32" r="6" fill="{DARK}"/>
        <line x1="32" y1="10" x2="32" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <line x1="10" y1="32" x2="54" y2="32" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("arts_46_halakki_gourd_instrument", "Halakki Tribal Gourd Instrument", "ಹಾಲಕ್ಕಿ ಒಕ್ಕಲಿಗರ ವಾದ್ಯ", ["halakki", "tribal", "gourd", "instrument"], f"""
        <circle cx="32" cy="40" r="14" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <path d="M 32 26 L 32 10" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <circle cx="32" cy="8" r="2.5" fill="{RED}"/>
        <circle cx="32" cy="40" r="4" fill="{DARK}"/>
        """),
        ("arts_47_suggi_kunitha_headgear", "Suggi Kunitha Peacock Headgear", "ಸುಗ್ಗಿ ಕುಣಿತ ನವಿಲುಗರಿ ಶಿರಸ್ತ್ರಾಣ", ["suggi", "kunitha", "peacock", "harvest"], f"""
        <!-- Semicircular fan of vibrant peacock feathers -->
        <path d="M 14 36 C 14 16 50 16 50 36 Z" fill="rgba(21,128,61,0.2)" stroke="{GREEN}" stroke-width="2"/>
        <circle cx="22" cy="24" r="2.5" fill="{SKY_BLUE}"/>
        <circle cx="32" cy="20" r="2.5" fill="{SKY_BLUE}"/>
        <circle cx="42" cy="24" r="2.5" fill="{SKY_BLUE}"/>
        <!-- Base headband -->
        <rect x="18" y="36" width="28" height="8" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("arts_48_patada_kunitha_flag", "Patada Kunitha Silk Banner Pole", "ಪಟದ ಕುಣಿತ ಧ್ವಜ", ["patada", "kunitha", "flag", "bamboo"], f"""
        <line x1="20" y1="58" x2="20" y2="8" stroke="{BROWN}" stroke-width="3"/>
        <!-- Billowing yellow and red silk streamer banner -->
        <path d="M 20 10 Q 36 6 52 14 Q 36 22 20 20 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <path d="M 20 20 Q 36 16 52 24 Q 36 32 20 30 Z" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("arts_49_kodava_bolak_aat_sword", "Kodava Bolak-Aat Dance Swords", "ಕೊಡವ ಬೊಳಕ್-ಆಟ್ ಕತ್ತಿಗಳು", ["kodava", "bolakaat", "sword", "dance"], f"""
        <!-- Pair of crossed Kodava swords -->
        <line x1="16" y1="16" x2="48" y2="48" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="48" y1="16" x2="16" y2="48" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="16" cy="16" r="2.5" fill="{GOLD}"/>
        <circle cx="48" cy="16" r="2.5" fill="{GOLD}"/>
        <circle cx="32" cy="32" r="3" fill="{RED}"/>
        """),
        ("arts_50_kodava_valaga_ensemble", "Kodava Valaga Trumpet", "ಕೊಡವ ವಾಲಗ", ["kodava", "valaga", "pipe", "coorg"], f"""
        <polygon points="18,18 42,42 46,38 22,14" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Flared brass mouth -->
        <ellipse cx="44" cy="40" rx="6" ry="3" transform="rotate(45 44 40)" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="16" cy="16" r="2" fill="{RED}"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in arts_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
