"""
Category 2: Historical Dynasties, Emblems & Royalty (50 icons)
"""
from .common import RED, YELLOW, GOLD, DARK_GOLD, SLATE, DARK, BROWN, SILVER, CREAM, wrap_svg

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "emblems-royalty",
            "tags": ["emblem", "royalty", "history", "karnataka", "dynasty"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Gandaberunda
    add("emblem_01_gandaberunda", "Gandaberunda State Emblem", "ಗಂಡಭೇರುಂಡ ರಾಜ್ಯ ಲಾಂಛನ", ["gandaberunda", "bird", "state", "crest"], f"""
    <!-- Gandaberunda Two-Headed Mythological Bird -->
    <path d="M 32 16 L 32 54 M 22 26 C 14 20 10 32 18 38 C 24 42 32 40 32 40 C 32 40 40 42 46 38 C 54 32 50 20 42 26" stroke="{GOLD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <!-- Left Head -->
    <path d="M 27 18 C 24 14 18 14 16 19 C 14 22 17 24 22 22" stroke="{RED}" stroke-width="2" fill="none"/>
    <circle cx="20" cy="18" r="1.5" fill="{RED}"/>
    <!-- Right Head -->
    <path d="M 37 18 C 40 14 46 14 48 19 C 50 22 47 24 42 22" stroke="{RED}" stroke-width="2" fill="none"/>
    <circle cx="44" cy="18" r="1.5" fill="{RED}"/>
    <!-- Crown Finial -->
    <path d="M 28 12 L 32 6 L 36 12 Z" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Wings & Feathers -->
    <path d="M 12 30 C 6 36 8 46 16 48 M 52 30 C 58 36 56 46 48 48" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
    <path d="M 24 44 L 20 56 M 40 44 L 44 56 M 32 42 L 32 58" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    """)

    # 2. Hoysala Sala Emblem
    add("emblem_02_hoysala_crest", "Hoysala Sala Striking Tiger", "ಹೊಯ್ಸಳ ಸಳ ಮತ್ತು ಹುಲಿ ಲಾಂಛನ", ["hoysala", "sala", "tiger", "sculpture"], f"""
    <!-- Hoysala Warrior Sala fighting tiger -->
    <circle cx="20" cy="18" r="4" fill="{GOLD}"/>
    <path d="M 20 22 L 22 34 L 16 48 M 22 34 L 28 46" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    <!-- Sword thrusting down -->
    <path d="M 16 26 L 34 32" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Rearing Tiger -->
    <path d="M 48 24 C 44 20 38 22 36 28 C 34 34 38 42 46 44 L 52 46 M 36 28 L 32 32 M 42 42 L 40 52 M 48 44 L 52 52" stroke="{GOLD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <circle cx="44" cy="24" r="1.5" fill="{RED}"/>
    """)

    # 3. Chalukya Varaha Boar
    add("emblem_03_chalukya_varaha", "Chalukya Royal Boar (Varaha)", "ಚಾಲುಕ್ಯ ವರಾಹ ಲಾಂಛನ", ["chalukya", "varaha", "boar", "crest"], f"""
    <!-- Royal Boar -->
    <path d="M 14 36 C 14 26 24 20 36 20 C 44 20 52 26 52 34 C 52 42 44 46 36 46 L 22 46 C 16 46 14 42 14 36 Z" stroke="{GOLD}" stroke-width="2.5" fill="rgba(212, 175, 55, 0.15)"/>
    <!-- Snout & Tusk -->
    <path d="M 14 34 L 8 36 L 12 30" stroke="{SLATE}" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Legs -->
    <path d="M 20 46 L 20 54 M 26 46 L 26 54 M 42 46 L 42 54 M 48 46 L 48 54" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    <!-- Royal Sun and Moon -->
    <circle cx="24" cy="14" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <path d="M 40 12 C 38 15 40 18 44 18 C 42 16 42 14 40 12 Z" fill="{GOLD}"/>
    """)

    # 4. Kadamba Royal Lion Crest
    add("emblem_04_kadamba_lion", "Kadamba Royal Lion Crest", "ಕದಂಬ ಸಿಂಹ ಲಾಂಛನ", ["kadamba", "lion", "banavasi"], f"""
    <path d="M 24 26 C 20 18 32 12 40 18 C 46 22 48 30 42 36 L 36 40 L 44 48 M 36 40 L 26 42 L 18 52" stroke="{GOLD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <!-- Mane -->
    <path d="M 28 16 C 24 16 22 22 26 24 M 36 14 C 36 10 42 12 40 16" stroke="{RED}" stroke-width="2" stroke-linecap="round"/>
    <circle cx="34" cy="22" r="2" fill="{RED}"/>
    <!-- Raised paw -->
    <path d="M 26 28 L 18 24 L 14 26" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    """)

    # 5. Ganga Dynasty Elephant Crest
    add("emblem_05_ganga_elephant", "Western Ganga Elephant Emblem", "ಪಶ್ಚಿಮ ಗಂಗರ ಆನೆ ಲಾಂಛನ", ["ganga", "elephant", "crest"], f"""
    <path d="M 18 36 C 18 26 26 20 38 20 C 48 20 54 26 54 36 C 54 44 48 48 40 48 L 26 48" stroke="{SLATE}" stroke-width="2.5" fill="rgba(148, 163, 184, 0.2)"/>
    <!-- Trunk -->
    <path d="M 18 32 C 14 32 10 36 12 44 C 13 48 16 48 18 44" stroke="{SLATE}" stroke-width="2" fill="none"/>
    <path d="M 18 40 L 24 40" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
    <circle cx="26" cy="28" r="1.5" fill="{DARK}"/>
    <!-- Legs -->
    <path d="M 28 48 L 28 56 M 46 48 L 46 56" stroke="{SLATE}" stroke-width="3" stroke-linecap="round"/>
    """)

    # 6. Vijayanagara Boar & Dagger
    add("emblem_06_vijayanagara_boar_dagger", "Vijayanagara Boar and Dagger", "ವಿಜಯನಗರ ವರಾಹ ಮತ್ತು ಖಡ್ಗ", ["vijayanagara", "hampi", "empire"], f"""
    <!-- Central Dagger -->
    <path d="M 32 10 L 32 50 M 26 20 L 38 20 M 30 50 L 34 50" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Boar on Left -->
    <path d="M 26 32 C 22 28 16 28 12 34 C 12 40 18 42 24 42" stroke="{GOLD}" stroke-width="2" fill="none"/>
    <!-- Sun and Moon -->
    <circle cx="16" cy="18" r="3" fill="{YELLOW}"/>
    <path d="M 48 16 C 46 19 48 22 52 21 C 50 19 50 17 48 16 Z" fill="{YELLOW}"/>
    """)

    # 7. Rashtrakuta Garuda Emblem
    add("emblem_07_rashtrakuta_garuda", "Rashtrakuta Garuda Emblem", "ರಾಷ್ಟ್ರಕೂಟ ಗರುಡ ಲಾಂಛನ", ["rashtrakuta", "garuda", "malkhed"], f"""
    <!-- Seated Garuda in Anjali Mudra -->
    <circle cx="32" cy="18" r="5" fill="{GOLD}"/>
    <!-- Beak -->
    <path d="M 32 19 L 28 22 L 32 23" fill="{RED}"/>
    <!-- Wings -->
    <path d="M 28 26 C 16 24 10 34 14 44 M 36 26 C 48 24 54 34 50 44" stroke="{GOLD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M 28 32 L 32 38 L 36 32" stroke="{SLATE}" stroke-width="2" fill="none"/>
    <path d="M 24 48 C 28 42 36 42 40 48" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    """)

    # 8. Mysore Wodeyar Crest
    add("emblem_08_mysore_wodeyar_coat_arms", "Mysore Royal Crest", "ಮೈಸೂರು ಒಡೆಯರ್ ರಾಜ ಲಾಂಛನ", ["mysore", "wodeyar", "crest", "royal"], f"""
    <circle cx="32" cy="34" r="16" stroke="{GOLD}" stroke-width="2" fill="rgba(212,175,55,0.1)"/>
    <!-- Crown atop -->
    <path d="M 24 16 L 32 10 L 40 16 L 36 20 L 28 20 Z" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Two miniature heads inside -->
    <circle cx="28" cy="32" r="2" fill="{RED}"/>
    <circle cx="36" cy="32" r="2" fill="{RED}"/>
    <path d="M 28 36 Q 32 40 36 36" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
    """)

    # 9. Golden Ambari (Howdah)
    add("emblem_09_golden_ambari", "Mysore Golden Howdah (Ambari)", "ಚಿನ್ನದ ಅಂಬಾರಿ", ["ambari", "dasara", "howdah", "gold"], f"""
    <!-- Ornate Golden Canopy Howdah -->
    <path d="M 16 36 L 20 22 L 44 22 L 48 36 Z" stroke="{GOLD}" stroke-width="2" fill="{YELLOW}"/>
    <path d="M 22 22 L 32 12 L 42 22" stroke="{DARK_GOLD}" stroke-width="2" fill="{GOLD}"/>
    <circle cx="32" cy="10" r="2" fill="{RED}"/>
    <!-- Base platform -->
    <rect x="14" y="36" width="36" height="8" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <circle cx="22" cy="40" r="1.5" fill="{YELLOW}"/>
    <circle cx="32" cy="40" r="1.5" fill="{YELLOW}"/>
    <circle cx="42" cy="40" r="1.5" fill="{YELLOW}"/>
    <path d="M 18 44 L 18 52 M 46 44 L 46 52" stroke="{SLATE}" stroke-width="2"/>
    """)

    # 10. Kanteerava Lion Throne
    add("emblem_10_kanteerava_simhasana", "Kanteerava Lion Throne", "ಕಂಠೀರವ ಸಿಂಹಾಸನ", ["throne", "simhasana", "lion"], f"""
    <!-- Backrest -->
    <path d="M 20 40 L 20 18 C 20 12 44 12 44 18 L 44 40 Z" fill="rgba(200,16,46,0.15)" stroke="{GOLD}" stroke-width="2"/>
    <!-- Finial Crown -->
    <path d="M 28 14 L 32 8 L 36 14 Z" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Seat -->
    <rect x="14" y="38" width="36" height="8" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Lion Legs -->
    <path d="M 16 46 L 14 56 M 48 46 L 50 56 M 26 46 L 26 56 M 38 46 L 38 56" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
    """)

    # 11. Mysore Peta (Turban)
    add("emblem_11_mysore_peta", "Mysore Peta Royal Turban", "ಮೈಸೂರು ಪೇಟ", ["peta", "turban", "mysore", "headgear"], f"""
    <!-- Swirling silk folds of Mysore Peta -->
    <ellipse cx="32" cy="34" rx="22" ry="14" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <path d="M 12 34 C 18 22 46 22 52 34" stroke="{RED}" stroke-width="2.5" fill="none"/>
    <path d="M 16 38 C 24 28 40 28 48 38" stroke="{RED}" stroke-width="2" fill="none"/>
    <!-- Turra / Kalasa jewel -->
    <path d="M 32 20 L 32 10 L 35 14" stroke="{RED}" stroke-width="2" fill="none"/>
    <circle cx="32" cy="22" r="3" fill="{YELLOW}" stroke="{RED}" stroke-width="1"/>
    <path d="M 44 38 L 54 48" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
    """)

    # 12. Royal Chhatra (Umbrella)
    add("emblem_12_royal_chhatra", "Royal Parasol (Chhatra)", "ರಾಜ ಛತ್ರ", ["chhatra", "umbrella", "parasol"], f"""
    <path d="M 12 28 C 12 14 52 14 52 28 Z" fill="rgba(255,209,0,0.3)" stroke="{GOLD}" stroke-width="2"/>
    <path d="M 32 14 L 32 8" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
    <circle cx="32" cy="7" r="2" fill="{RED}"/>
    <!-- Ribs -->
    <path d="M 22 28 C 24 20 28 16 32 14 C 36 16 40 20 42 28" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
    <!-- Tassels -->
    <circle cx="16" cy="31" r="1.5" fill="{RED}"/>
    <circle cx="26" cy="31" r="1.5" fill="{RED}"/>
    <circle cx="38" cy="31" r="1.5" fill="{RED}"/>
    <circle cx="48" cy="31" r="1.5" fill="{RED}"/>
    <!-- Staff -->
    <path d="M 32 28 L 32 58" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    """)

    # 13. Chamara Flywhisk
    add("emblem_13_chamara", "Royal Chamara Flywhisk", "ರಾಜ ಚಾಮರ", ["chamara", "flywhisk", "royal"], f"""
    <!-- Handle -->
    <path d="M 32 38 L 32 58" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="32" cy="58" r="2.5" fill="{RED}"/>
    <circle cx="32" cy="38" r="4" fill="{GOLD}"/>
    <!-- Whisks -->
    <path d="M 32 34 C 24 26 18 16 22 8 M 32 34 C 28 22 28 12 32 6 M 32 34 C 36 22 36 12 32 6 M 32 34 C 40 26 46 16 42 8" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    """)

    # 14. Royal Khadga / Sword
    add("emblem_14_khadga_royal_sword", "Royal Talwar / Khadga", "ರಾಜ ಖಡ್ಗ", ["sword", "talwar", "khadga", "weapon"], f"""
    <!-- Curved blade -->
    <path d="M 20 46 C 24 36 34 22 48 10 C 44 18 40 32 24 48 Z" fill="rgba(148,163,184,0.3)" stroke="{SLATE}" stroke-width="2"/>
    <!-- Hilt & Disc pommel -->
    <path d="M 20 46 L 14 52" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
    <path d="M 16 44 L 24 50" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
    <circle cx="12" cy="54" r="3" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
    """)

    # 15. Royal Scabbard
    add("emblem_15_scabbard", "Royal Scabbard (Ori)", "ಖಡ್ಗದ ಒರೆ", ["scabbard", "sheath", "gold"], f"""
    <path d="M 22 48 C 26 38 36 24 50 12 L 46 10 C 32 22 22 36 18 46 Z" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
    <path d="M 44 14 L 48 18 M 32 28 L 36 32 M 20 42 L 24 46" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="17" cy="49" r="3" fill="{GOLD}"/>
    """)

    # 16. Royal Dhal Shield
    add("emblem_16_royal_dhal_shield", "Royal Warrior Shield (Dhal)", "ರಾಜ ಗುರಾಣಿ", ["shield", "dhal", "armor"], f"""
    <circle cx="32" cy="32" r="22" fill="rgba(30,41,59,0.1)" stroke="{SLATE}" stroke-width="2.5"/>
    <circle cx="32" cy="32" r="16" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="2 2"/>
    <!-- 4 Bosses -->
    <circle cx="24" cy="24" r="3" fill="{GOLD}" stroke="{SLATE}" stroke-width="1"/>
    <circle cx="40" cy="24" r="3" fill="{GOLD}" stroke="{SLATE}" stroke-width="1"/>
    <circle cx="24" cy="40" r="3" fill="{GOLD}" stroke="{SLATE}" stroke-width="1"/>
    <circle cx="40" cy="40" r="3" fill="{GOLD}" stroke="{SLATE}" stroke-width="1"/>
    <circle cx="32" cy="32" r="2" fill="{RED}"/>
    """)

    # 17. Push Dagger (Katar)
    add("emblem_17_katar_push_dagger", "Vijayanagara Katar Dagger", "ಕಠಾರಿ", ["katar", "dagger", "blade"], f"""
    <!-- Triangular Blade -->
    <path d="M 32 10 L 24 34 L 40 34 Z" fill="rgba(148,163,184,0.3)" stroke="{SLATE}" stroke-width="2"/>
    <line x1="32" y1="12" x2="32" y2="34" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Hilt Side Bars -->
    <path d="M 22 34 L 22 54 M 42 34 L 42 54" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Double Crossbars -->
    <line x1="22" y1="42" x2="42" y2="42" stroke="{GOLD}" stroke-width="2"/>
    <line x1="22" y1="48" x2="42" y2="48" stroke="{GOLD}" stroke-width="2"/>
    """)

    # 18. Bichuwa Dagger
    add("emblem_18_bichuwa_dagger", "Bichuwa Scorpion Dagger", "ಬಿಚುವಾ ಬಾಕು", ["bichuwa", "dagger", "scorpion"], f"""
    <!-- Curved double-wave blade -->
    <path d="M 32 8 C 38 16 26 24 34 36 L 30 36 C 24 24 34 16 28 8 Z" fill="rgba(148,163,184,0.3)" stroke="{SLATE}" stroke-width="2"/>
    <!-- Loop Handle -->
    <path d="M 28 36 C 24 40 24 50 32 54 C 40 50 40 40 34 36" stroke="{GOLD}" stroke-width="2.5" fill="none"/>
    """)

    # 19. Dhanush & Bana
    add("emblem_19_dhanush_bana", "Royal Bow & Arrow", "ಧನುಷ್ ಮತ್ತು ಬಾಣ", ["bow", "arrow", "dhanush"], f"""
    <!-- Bow Arc -->
    <path d="M 18 12 C 34 20 34 44 18 52" stroke="{BROWN}" stroke-width="3" fill="none" stroke-linecap="round"/>
    <line x1="18" y1="12" x2="18" y2="52" stroke="{SLATE}" stroke-width="1" stroke-dasharray="2 1"/>
    <!-- Arrow -->
    <line x1="14" y1="32" x2="52" y2="32" stroke="{RED}" stroke-width="2" stroke-linecap="round"/>
    <path d="M 46 27 L 54 32 L 46 37 Z" fill="{RED}"/>
    <path d="M 14 29 L 10 32 L 14 35" stroke="{RED}" stroke-width="1.5"/>
    """)

    # 20. Royal Gada (Mace)
    add("emblem_20_gada_mace", "Royal Gada (Mace)", "ರಾಜ ಗದೆ", ["gada", "mace", "strength"], f"""
    <line x1="20" y1="52" x2="38" y2="28" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="18" cy="54" r="3" fill="{DARK_GOLD}"/>
    <!-- Fluted Head -->
    <circle cx="42" cy="22" r="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <path d="M 36 16 C 42 22 42 22 48 28" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="48" cy="14" r="2.5" fill="{RED}"/>
    """)

    # 21-50 Emblems & Royal Items (concise generator loop with unique visual features)
    other_emblems = [
        ("emblem_21_parashu_battleaxe", "Parashu Battle Axe", "ಪರಶು ಯುದ್ಧ ಕೊಡಲಿ", ["parashu", "axe"], f"""
        <line x1="24" y1="56" x2="24" y2="10" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <path d="M 24 16 C 36 12 44 20 44 28 C 44 36 36 44 24 40 Z" fill="rgba(148,163,184,0.3)" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("emblem_22_royal_spear", "Royal Spear / Barcha", "ರಾಜ ಭರ್ಚಿ", ["spear", "lance"], f"""
        <line x1="32" y1="60" x2="32" y2="22" stroke="{BROWN}" stroke-width="3"/>
        <path d="M 32 6 L 24 24 L 40 24 Z" fill="{SILVER}" stroke="{SLATE}" stroke-width="2"/>
        <line x1="32" y1="6" x2="32" y2="24" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="32" cy="26" r="3" fill="{GOLD}"/>
        """),
        ("emblem_23_tipu_tiger_finial", "Tipu Sultan Tiger Throne Finial", "ಟಿಪ್ಪು ಸಿಂಹಾಸನದ ಚಿನ್ನದ ಹುಲಿ", ["tipu", "tiger", "gold"], f"""
        <circle cx="32" cy="30" r="16" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="22" cy="18" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="42" cy="18" r="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Eyes & Snout -->
        <ellipse cx="26" cy="28" rx="2" ry="3" fill="{RED}"/>
        <ellipse cx="38" cy="28" rx="2" ry="3" fill="{RED}"/>
        <polygon points="30,34 34,34 32,38" fill="{DARK}"/>
        <path d="M 28 40 Q 32 44 36 40" stroke="{DARK}" stroke-width="2" fill="none"/>
        <line x1="32" y1="46" x2="32" y2="58" stroke="{GOLD}" stroke-width="4"/>
        """),
        ("emblem_24_tipu_babri_stripe", "Tipu Babri Tiger Stripe Motif", "ಟಿಪ್ಪು ಬಬ್ರಿ ಹುಲಿ ಪಟ್ಟೆ ಚಿಹ್ನೆ", ["babri", "stripe", "srirangapatna"], f"""
        <path d="M 12 20 C 22 14 26 26 36 20 C 44 14 50 24 52 18" stroke="{RED}" stroke-width="4" stroke-linecap="round" fill="none"/>
        <path d="M 12 34 C 22 28 26 40 36 34 C 44 28 50 38 52 32" stroke="{GOLD}" stroke-width="4" stroke-linecap="round" fill="none"/>
        <path d="M 12 48 C 22 42 26 54 36 48 C 44 42 50 52 52 46" stroke="{RED}" stroke-width="4" stroke-linecap="round" fill="none"/>
        """),
        ("emblem_25_mysore_war_rocket", "Mysore War Rocket", "ಮೈಸೂರು ಯುದ್ಧ ರಾಕೆಟ್", ["rocket", "warfare", "invention"], f"""
        <line x1="16" y1="56" x2="44" y2="16" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
        <!-- Iron rocket casing lashed to bamboo -->
        <rect x="30" y="16" width="16" height="8" transform="rotate(-55 38 20)" fill="{SLATE}" stroke="{GOLD}" stroke-width="1.5" rx="2"/>
        <path d="M 44 12 L 52 10 L 46 18 Z" fill="{RED}"/>
        <!-- Spark trails -->
        <path d="M 24 38 L 18 42 M 22 34 L 14 36" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("emblem_26_srirangapatna_cannon", "Srirangapatna Fortress Cannon", "ಶ್ರೀರಂಗಪಟ್ಟಣ ಕೋಟೆ ಫಿರಂಗಿ", ["cannon", "fortress", "artillery"], f"""
        <!-- Barrel -->
        <path d="M 14 32 L 48 24 L 46 16 L 12 24 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Wheel -->
        <circle cx="28" cy="40" r="12" stroke="{BROWN}" stroke-width="3" fill="none"/>
        <circle cx="28" cy="40" r="3" fill="{GOLD}"/>
        <line x1="28" y1="28" x2="28" y2="52" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="16" y1="40" x2="40" y2="40" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="14" y1="38" x2="8" y2="48" stroke="{BROWN}" stroke-width="3"/>
        """),
        ("emblem_27_cannon_balls", "Fortress Cannonballs Stack", "ಫಿರಂಗಿ ಗುಂಡುಗಳ ರಾಶಿ", ["cannonball", "ammunition"], f"""
        <!-- Base 3 balls -->
        <circle cx="20" cy="44" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="34" cy="44" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="48" cy="44" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Middle 2 balls -->
        <circle cx="27" cy="32" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="41" cy="32" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Top ball -->
        <circle cx="34" cy="20" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("emblem_28_chennamma_talwar", "Kittur Chennamma Talwar", "ಕಿತ್ತೂರು ಚೆನ್ನಮ್ಮ ಖಡ್ಗ", ["kittur", "chennamma", "bravery"], f"""
        <path d="M 16 52 C 22 40 32 24 50 12 C 44 22 36 38 22 54 Z" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="16" cy="54" r="3" fill="{GOLD}"/>
        <path d="M 38 8 L 52 10 L 50 24" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
        """),
        ("emblem_29_sangolli_rayanna_staff", "Sangolli Rayanna Bamboo Staff", "ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ ಬೆತ್ತ", ["rayanna", "staff", "rebellion"], f"""
        <line x1="20" y1="58" x2="44" y2="8" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>
        <line x1="25" y1="48" x2="29" y2="46" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="31" y1="36" x2="35" y2="34" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="37" y1="24" x2="41" y2="22" stroke="{YELLOW}" stroke-width="2"/>
        <!-- Knotted tip -->
        <circle cx="44" cy="8" r="3" fill="{BROWN}"/>
        """),
        ("emblem_30_royal_palanquin", "Royal Palanquin (Pallakki)", "ರಾಜ ಪಲ್ಲಕ್ಕಿ", ["palanquin", "pallakki"], f"""
        <!-- Pole -->
        <path d="M 6 30 Q 32 20 58 30" stroke="{GOLD}" stroke-width="3" fill="none" stroke-linecap="round"/>
        <!-- Box -->
        <rect x="20" y="26" width="24" height="18" rx="3" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <path d="M 26 32 L 38 32 M 32 26 L 32 44" stroke="{GOLD}" stroke-width="1"/>
        <path d="M 20 44 L 18 52 M 44 44 L 46 52" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("emblem_31_royal_ratha_chariot", "Temple Chariot (Ratha)", "ದೇವಾಲಯದ ರಥ", ["ratha", "chariot", "festival"], f"""
        <!-- Tower -->
        <polygon points="32,8 22,26 42,26" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <rect x="20" y="26" width="24" height="16" fill="{BROWN}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Wheels -->
        <circle cx="20" cy="48" r="6" stroke="{GOLD}" stroke-width="2" fill="{BROWN}"/>
        <circle cx="44" cy="48" r="6" stroke="{GOLD}" stroke-width="2" fill="{BROWN}"/>
        <circle cx="32" cy="7" r="2" fill="{RED}"/>
        """),
        ("emblem_32_raja_mudre_seal", "Royal Signet Seal (Raja Mudre)", "ರಾಜ ಮುದ್ರೆ", ["seal", "mudre", "stamp"], f"""
        <circle cx="32" cy="32" r="20" fill="rgba(200,16,46,0.15)" stroke="{RED}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="16" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Kannada letter 'ಶ್ರೀ' or emblem in center -->
        <text x="32" y="37" font-family="'Noto Sans Kannada', sans-serif" font-size="14" font-weight="bold" fill="{RED}" text-anchor="middle">ಶ್ರೀ</text>
        """),
        ("emblem_33_tamra_shasana", "Copper Plate Inscription (Tamra Shasana)", "ತಾಮ್ರ ಶಾಸನ", ["tamra", "copper", "inscription"], f"""
        <!-- Plates linked with ring -->
        <rect x="14" y="20" width="36" height="26" rx="2" fill="#B45309" stroke="#78350F" stroke-width="2"/>
        <line x1="20" y1="28" x2="44" y2="28" stroke="{YELLOW}" stroke-width="1.5"/>
        <line x1="20" y1="34" x2="44" y2="34" stroke="{YELLOW}" stroke-width="1.5"/>
        <line x1="20" y1="40" x2="38" y2="40" stroke="{YELLOW}" stroke-width="1.5"/>
        <!-- Ring at top -->
        <circle cx="32" cy="14" r="6" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        """),
        ("emblem_34_shila_shasana", "Stone Slab Inscription (Shila Shasana)", "ಶಿಲಾ ಶಾಸನ", ["shasana", "inscription", "stone"], f"""
        <path d="M 16 54 L 16 22 C 16 12 48 12 48 22 L 48 54 Z" fill="rgba(100,116,139,0.2)" stroke="{SLATE}" stroke-width="2.5"/>
        <circle cx="24" cy="20" r="2" fill="{YELLOW}"/>
        <path d="M 38 18 C 36 21 38 24 41 23 C 39 21 39 19 38 18 Z" fill="{YELLOW}"/>
        <!-- Inscription lines -->
        <line x1="22" y1="30" x2="42" y2="30" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="22" y1="36" x2="42" y2="36" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="22" y1="42" x2="42" y2="42" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="22" y1="48" x2="36" y2="48" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("emblem_35_veeragallu", "Hero Stone Memorial (Veeragallu)", "ವೀರಗಲ್ಲು", ["veeragallu", "hero", "memorial"], f"""
        <rect x="18" y="10" width="28" height="46" rx="3" fill="rgba(71,85,105,0.2)" stroke="{SLATE}" stroke-width="2.5"/>
        <!-- Tier dividers -->
        <line x1="18" y1="24" x2="46" y2="24" stroke="{SLATE}" stroke-width="2"/>
        <line x1="18" y1="38" x2="46" y2="38" stroke="{SLATE}" stroke-width="2"/>
        <!-- Hero fighting in lower tier -->
        <circle cx="28" cy="44" r="2" fill="{RED}"/>
        <line x1="28" y1="46" x2="28" y2="52" stroke="{RED}" stroke-width="1.5"/>
        <line x1="28" y1="48" x2="36" y2="46" stroke="{RED}" stroke-width="1.5"/>
        <!-- Hero reaching heaven in top tier -->
        <circle cx="32" cy="16" r="2" fill="{GOLD}"/>
        <line x1="30" y1="18" x2="34" y2="18" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("emblem_36_masti_kallu", "Masti Kallu (Sacred Hand Stone)", "ಮಾಸ್ತಿ ಕಲ್ಲು", ["masti", "stone", "heritage"], f"""
        <path d="M 18 54 L 18 20 C 18 12 46 12 46 20 L 46 54 Z" fill="rgba(148,163,184,0.2)" stroke="{SLATE}" stroke-width="2"/>
        <!-- Raised Right Hand (Abhaya) -->
        <path d="M 32 46 L 32 30 C 32 26 36 26 36 30 L 36 46" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <path d="M 36 30 C 36 26 40 26 40 30 L 40 46" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Sun and Moon at top -->
        <circle cx="26" cy="18" r="2" fill="{RED}"/>
        <circle cx="38" cy="18" r="2" fill="{YELLOW}"/>
        """),
        ("emblem_37_vijayanagara_varaha_coin", "Vijayanagara Gold Pagoda Coin", "ವಿಜಯನಗರ ವರಾಹ ಬಂಗಾರದ ನಾಣ್ಯ", ["coin", "varaha", "gold", "gadyana"], f"""
        <circle cx="32" cy="32" r="20" fill="{YELLOW}" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="16" stroke="{DARK_GOLD}" stroke-width="1" stroke-dasharray="2 2"/>
        <!-- Boar engraving -->
        <path d="M 22 34 C 22 28 28 26 34 26 C 38 26 42 28 42 34 L 38 34" stroke="{BROWN}" stroke-width="2" fill="none"/>
        <line x1="26" y1="34" x2="26" y2="40" stroke="{BROWN}" stroke-width="2"/>
        <line x1="36" y1="34" x2="36" y2="40" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("emblem_38_kanteerava_fanam", "Mysore Kanteerava Fanam Coin", "ಕಂಠೀರವ ಹಣ ನಾಣ್ಯ", ["fanam", "coin", "currency", "mysore"], f"""
        <circle cx="32" cy="32" r="18" fill="{CREAM}" stroke="{GOLD}" stroke-width="2.5"/>
        <!-- Narasimha / Lion motif on coin -->
        <circle cx="32" cy="26" r="4" fill="{GOLD}"/>
        <path d="M 26 32 C 28 36 36 36 38 32" stroke="{RED}" stroke-width="2" fill="none"/>
        <path d="M 32 34 L 32 44 M 28 44 L 36 44" stroke="{GOLD}" stroke-width="2"/>
        """),
        ("emblem_39_raja_danda_scepter", "Royal Scepter (Raja Danda)", "ರಾಜ ದಂಡ", ["scepter", "rajadanda", "authority"], f"""
        <line x1="32" y1="58" x2="32" y2="18" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <!-- Crown / Lotus finial on scepter -->
        <path d="M 24 18 C 24 10 40 10 40 18 Z" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="8" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="58" r="2.5" fill="{RED}"/>
        """),
        ("emblem_40_ratha_chakra", "Royal Chariot Wheel (Chakra)", "ರಥ ಚಕ್ರ", ["chakra", "wheel", "spoke"], f"""
        <circle cx="32" cy="32" r="22" stroke="{BROWN}" stroke-width="3" fill="none"/>
        <circle cx="32" cy="32" r="6" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <circle cx="32" cy="32" r="2" fill="{RED}"/>
        <!-- 8 Spokes -->
        <line x1="32" y1="10" x2="32" y2="26" stroke="{GOLD}" stroke-width="2"/>
        <line x1="32" y1="38" x2="32" y2="54" stroke="{GOLD}" stroke-width="2"/>
        <line x1="10" y1="32" x2="26" y2="32" stroke="{GOLD}" stroke-width="2"/>
        <line x1="38" y1="32" x2="54" y2="32" stroke="{GOLD}" stroke-width="2"/>
        <line x1="17" y1="17" x2="28" y2="28" stroke="{GOLD}" stroke-width="2"/>
        <line x1="36" y1="36" x2="47" y2="47" stroke="{GOLD}" stroke-width="2"/>
        <line x1="17" y1="47" x2="28" y2="36" stroke="{GOLD}" stroke-width="2"/>
        <line x1="36" y1="28" x2="47" y2="17" stroke="{GOLD}" stroke-width="2"/>
        """),
        ("emblem_41_kahale_horn", "Royal Trumpet (Kahale / Kombu)", "ಕಹಳೆ", ["kahale", "trumpet", "horn"], f"""
        <!-- Curved brass horn -->
        <path d="M 12 50 C 20 42 22 26 36 24 C 44 22 50 16 52 10" stroke="{GOLD}" stroke-width="3.5" fill="none" stroke-linecap="round"/>
        <!-- Horn mouth -->
        <ellipse cx="52" cy="10" rx="4" ry="2" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="12" cy="50" r="2.5" fill="{RED}"/>
        """),
        ("emblem_42_nagara_war_drum", "Royal War Drum (Nagara)", "ನಗಾರಿ", ["nagara", "drum", "war"], f"""
        <!-- Hemisphere drum bowl -->
        <path d="M 14 30 C 14 46 50 46 50 30 Z" fill="{BROWN}" stroke="{SLATE}" stroke-width="2.5"/>
        <ellipse cx="32" cy="30" rx="18" ry="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Drumsticks -->
        <line x1="22" y1="12" x2="30" y2="28" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="21" cy="10" r="2" fill="{RED}"/>
        <line x1="42" y1="12" x2="34" y2="28" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="43" cy="10" r="2" fill="{RED}"/>
        """),
        ("emblem_43_durbar_arch", "Royal Durbar Arch", "ದರ್ಬಾರ್ ಕಮಾನು", ["durbar", "arch", "palace"], f"""
        <path d="M 14 56 L 14 26 C 14 14 24 10 32 18 C 40 10 50 14 50 26 L 50 56" stroke="{GOLD}" stroke-width="2.5" fill="rgba(212,175,55,0.15)"/>
        <path d="M 10 56 L 54 56" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="32" cy="12" r="2.5" fill="{RED}"/>
        """),
        ("emblem_44_torana_gateway", "Ceremonial Torana Gateway", "ತೋರಣ ದ್ವಾರ", ["torana", "gateway", "welcome"], f"""
        <!-- 2 Pillars -->
        <rect x="12" y="18" width="6" height="38" fill="{BROWN}" stroke="{SLATE}" stroke-width="1.5"/>
        <rect x="46" y="18" width="6" height="38" fill="{BROWN}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Crossbeams with scrolls -->
        <rect x="8" y="12" width="48" height="6" rx="2" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 18 18 Q 32 26 46 18" stroke="{RED}" stroke-width="2" fill="none"/>
        <circle cx="24" cy="22" r="1.5" fill="{YELLOW}"/>
        <circle cx="32" cy="23" r="1.5" fill="{YELLOW}"/>
        <circle cx="40" cy="22" r="1.5" fill="{YELLOW}"/>
        """),
        ("emblem_45_ankusha_goad", "Elephant Ankusha Goad", "ಅಂಕುಶ", ["ankusha", "goad", "elephant"], f"""
        <line x1="32" y1="58" x2="32" y2="18" stroke="{SLATE}" stroke-width="3" stroke-linecap="round"/>
        <!-- Hook & Spearhead -->
        <path d="M 32 18 L 32 8 L 35 12" stroke="{GOLD}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M 32 20 C 40 20 44 26 40 30 C 38 32 34 30 34 26" stroke="{GOLD}" stroke-width="2.5" fill="none"/>
        """),
        ("emblem_46_pakhar_armor", "Elephant Head Armor (Pakhar)", "ಆನೆಯ ಶಿರಸ್ತ್ರಾಣ", ["pakhar", "armor", "elephant"], f"""
        <path d="M 20 18 L 44 18 L 48 38 L 32 50 L 16 38 Z" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="26" cy="28" r="3" fill="{RED}"/>
        <circle cx="38" cy="28" r="3" fill="{RED}"/>
        <circle cx="32" cy="40" r="2.5" fill="{YELLOW}"/>
        """),
        ("emblem_47_royal_steed_saddle", "Royal Horse Saddle", "ರಾಜ ಕುದುರೆ ಜೀನು", ["saddle", "horse", "steed"], f"""
        <path d="M 14 32 C 18 24 46 24 50 32 C 48 42 42 46 32 46 C 22 46 16 42 14 32 Z" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <path d="M 28 46 L 28 54 M 36 46 L 36 54" stroke="{BROWN}" stroke-width="2"/>
        <!-- Stirrup -->
        <circle cx="28" cy="56" r="2" fill="none" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="36" cy="56" r="2" fill="none" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("emblem_48_palace_guard_crest", "Mysore Palace Guard Badge", "ಅರಮನೆ ಕಾವಲು ಲಾಂಛನ", ["guard", "crest", "mysore"], f"""
        <polygon points="32,8 52,18 52,38 32,56 12,38 12,18" fill="rgba(200,16,46,0.15)" stroke="{RED}" stroke-width="2"/>
        <circle cx="32" cy="30" r="8" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <path d="M 32 24 L 32 36 M 26 30 L 38 30" stroke="{RED}" stroke-width="2"/>
        """),
        ("emblem_49_keladi_nayaka_crest", "Keladi Nayaka Battle Crest", "ಕೆಳದಿ ನಾಯಕರ ಯುದ್ಧ ಲಾಂಛನ", ["keladi", "nayaka", "crest"], f"""
        <!-- Double Swords crossed behind shield -->
        <line x1="14" y1="14" x2="50" y2="50" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
        <line x1="50" y1="14" x2="14" y2="50" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
        <circle cx="32" cy="32" r="14" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="32" r="4" fill="{RED}"/>
        """),
        ("emblem_50_chitradurga_nayaka_crest", "Chitradurga Nayaka Crest", "ಚಿತ್ರದುರ್ಗ ನಾಯಕರ ಕೋಟೆ ಲಾಂಛನ", ["chitradurga", "nayaka", "fortress"], f"""
        <!-- Fortress bastions with battleaxe -->
        <path d="M 12 50 L 12 30 L 18 30 L 18 34 L 26 34 L 26 30 L 38 30 L 38 34 L 46 34 L 46 30 L 52 30 L 52 50 Z" fill="rgba(100,116,139,0.2)" stroke="{SLATE}" stroke-width="2"/>
        <!-- Battleaxe upright in center -->
        <line x1="32" y1="12" x2="32" y2="46" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <path d="M 32 16 C 40 12 44 22 32 26 Z" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in other_emblems:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
