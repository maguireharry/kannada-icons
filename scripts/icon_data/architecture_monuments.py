"""
Category 3: Architecture, Temples & Monuments (60 icons)
"""
from .common import RED, YELLOW, GOLD, DARK_GOLD, SLATE, DARK, BROWN, SILVER, CREAM, GREEN, SKY_BLUE, wrap_svg

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "architecture-monuments",
            "tags": ["architecture", "monument", "temple", "heritage", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Hampi Stone Chariot
    add("arch_01_hampi_stone_chariot", "Hampi Stone Chariot", "ಹಂಪಿ ಕಲ್ಲಿನ ರಥ", ["hampi", "chariot", "unesco", "vijayanagara"], f"""
    <!-- Chariot Body -->
    <rect x="18" y="24" width="28" height="16" fill="rgba(148,163,184,0.2)" stroke="{SLATE}" stroke-width="2"/>
    <!-- Vimana / Shikhara top -->
    <path d="M 22 24 L 32 10 L 42 24 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="32" cy="8" r="2" fill="{RED}"/>
    <!-- Stone Carved Wheels -->
    <circle cx="20" cy="46" r="8" stroke="{SLATE}" stroke-width="2.5" fill="{CREAM}"/>
    <circle cx="44" cy="46" r="8" stroke="{SLATE}" stroke-width="2.5" fill="{CREAM}"/>
    <circle cx="20" cy="46" r="2" fill="{RED}"/>
    <circle cx="44" cy="46" r="2" fill="{RED}"/>
    <line x1="20" y1="38" x2="20" y2="54" stroke="{SLATE}" stroke-width="1"/>
    <line x1="12" y1="46" x2="28" y2="46" stroke="{SLATE}" stroke-width="1"/>
    <line x1="44" y1="38" x2="44" y2="54" stroke="{SLATE}" stroke-width="1"/>
    <line x1="36" y1="46" x2="52" y2="46" stroke="{SLATE}" stroke-width="1"/>
    <!-- Elephant Guard at front -->
    <path d="M 46 40 C 50 38 56 42 54 48" stroke="{SLATE}" stroke-width="2" fill="none"/>
    <line x1="10" y1="54" x2="54" y2="54" stroke="{SLATE}" stroke-width="2"/>
    """)

    # 2. Virupaksha Gopuram
    add("arch_02_virupaksha_temple_gopuram", "Virupaksha Temple Gopuram", "ವಿರೂಪಾಕ್ಷ ದೇವಾಲಯ ಗೋಪುರ", ["virupaksha", "gopuram", "hampi"], f"""
    <!-- Tiered Pyramidal Gopuram -->
    <polygon points="32,8 20,44 44,44" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2"/>
    <!-- Tiers -->
    <line x1="29" y1="16" x2="35" y2="16" stroke="{SLATE}" stroke-width="1.5"/>
    <line x1="26" y1="24" x2="38" y2="24" stroke="{SLATE}" stroke-width="1.5"/>
    <line x1="23" y1="34" x2="41" y2="34" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Kalasas on ridge -->
    <circle cx="28" cy="7" r="1.5" fill="{GOLD}"/>
    <circle cx="32" cy="6" r="2" fill="{RED}"/>
    <circle cx="36" cy="7" r="1.5" fill="{GOLD}"/>
    <!-- Base Gateway (Arch) -->
    <rect x="16" y="44" width="32" height="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <path d="M 26 58 L 26 48 C 26 44 38 44 38 48 L 38 58 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
    """)

    # 3. Mysore Palace Facade
    add("arch_03_mysore_palace_facade", "Mysore Palace Facade", "ಮೈಸೂರು ಅರಮನೆ ಮುಂಭಾಗ", ["mysore", "palace", "ambavilas"], f"""
    <!-- Central Arches and Dome -->
    <rect x="10" y="34" width="44" height="22" fill="rgba(212,175,55,0.15)" stroke="{SLATE}" stroke-width="2"/>
    <!-- 3 Arches -->
    <path d="M 14 56 L 14 44 C 14 38 22 38 22 44 L 22 56" stroke="{RED}" stroke-width="1.5" fill="none"/>
    <path d="M 26 56 L 26 42 C 26 36 38 36 38 42 L 38 56" stroke="{RED}" stroke-width="2" fill="none"/>
    <path d="M 42 56 L 42 44 C 42 38 50 38 50 44 L 50 56" stroke="{RED}" stroke-width="1.5" fill="none"/>
    <!-- Central Grand Dome -->
    <path d="M 24 34 C 24 20 40 20 40 34 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <line x1="32" y1="20" x2="32" y2="12" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="32" cy="11" r="2" fill="{RED}"/>
    <!-- Corner Turrets -->
    <rect x="10" y="24" width="6" height="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
    <rect x="48" y="24" width="6" height="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
    """)

    # 4. Mysore Palace Golden Dome
    add("arch_04_mysore_palace_dome", "Mysore Palace Golden Dome", "ಮೈಸೂರು ಅರಮನೆಯ ಬಂಗಾರದ ಗುಮ್ಮಟ", ["dome", "gold", "palace"], f"""
    <!-- Ornate Gilded Dome -->
    <path d="M 16 42 C 16 18 48 18 48 42 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2.5"/>
    <!-- Ribs of dome -->
    <path d="M 22 42 C 22 26 32 20 32 20 C 32 20 42 26 42 42" stroke="{YELLOW}" stroke-width="1.5" fill="none"/>
    <!-- Golden Kalasa Finial -->
    <line x1="32" y1="20" x2="32" y2="8" stroke="{GOLD}" stroke-width="3"/>
    <circle cx="32" cy="7" r="3" fill="{RED}"/>
    <!-- Drum Base -->
    <rect x="14" y="42" width="36" height="8" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <line x1="10" y1="50" x2="54" y2="50" stroke="{SLATE}" stroke-width="2"/>
    """)

    # 5. Belur Chennakeshava Stellate Plan
    add("arch_05_belur_chennakeshava_star", "Belur Temple Stellate Platform", "ಬೇಲೂರು ಚನ್ನಕೇಶವ ನಕ್ಷತ್ರಾಕಾರದ ಜಗತಿ", ["belur", "star", "hoysala"], f"""
    <!-- 16-pointed star polygon / platform -->
    <path d="M 32 8 L 38 18 L 48 14 L 46 25 L 56 28 L 50 37 L 56 46 L 45 47 L 43 58 L 32 52 L 21 58 L 19 47 L 8 46 L 14 37 L 8 28 L 18 25 L 16 14 L 26 18 Z" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="32" cy="33" r="10" stroke="{SLATE}" stroke-width="2" fill="{CREAM}"/>
    <circle cx="32" cy="33" r="3" fill="{RED}"/>
    """)

    # 6. Belur Madanika Bracket Figure
    add("arch_06_belur_shilabhalika", "Belur Madanika Bracket Figure", "ಬೇಲೂರು ಶಿಲಾಬಾಲಿಕೆ", ["madanika", "sculpture", "dance", "hoysala"], f"""
    <!-- Graceful sculpted dancer silhouette in bracket angle -->
    <circle cx="28" cy="14" r="4" fill="{GOLD}"/>
    <path d="M 28 18 C 34 26 24 34 32 44 L 26 56 M 32 44 L 38 54" stroke="{SLATE}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <!-- Graceful arched arms holding mirror -->
    <path d="M 26 24 C 18 20 18 14 22 14" stroke="{RED}" stroke-width="2" fill="none"/>
    <circle cx="20" cy="14" r="3" stroke="{GOLD}" stroke-width="1.5" fill="{CREAM}"/>
    <!-- Pillar Bracket angle -->
    <path d="M 12 10 L 12 56 L 48 56" stroke="{SLATE}" stroke-width="2"/>
    <line x1="12" y1="10" x2="48" y2="46" stroke="{GOLD}" stroke-width="1" stroke-dasharray="2 2"/>
    """)

    # 7. Halebidu Hoysaleshwara Frieze
    add("arch_07_halebidu_hoysaleshwara", "Halebidu Temple Frieze", "ಹಳೇಬೀಡು ಹೊಯ್ಸಳೇಶ್ವರ ಶಿಲಾ ಕೆತ್ತನೆ", ["halebidu", "frieze", "elephants"], f"""
    <rect x="10" y="16" width="44" height="36" fill="rgba(100,116,139,0.15)" stroke="{SLATE}" stroke-width="2"/>
    <!-- Tier lines -->
    <line x1="10" y1="28" x2="54" y2="28" stroke="{GOLD}" stroke-width="2"/>
    <line x1="10" y1="40" x2="54" y2="40" stroke="{GOLD}" stroke-width="2"/>
    <!-- Top tier: Swan/Hamsa motifs -->
    <circle cx="20" cy="22" r="3" fill="{YELLOW}"/>
    <circle cx="32" cy="22" r="3" fill="{YELLOW}"/>
    <circle cx="44" cy="22" r="3" fill="{YELLOW}"/>
    <!-- Middle tier: Lions -->
    <rect x="18" y="32" width="6" height="5" fill="{RED}"/>
    <rect x="30" y="32" width="6" height="5" fill="{RED}"/>
    <rect x="42" y="32" width="6" height="5" fill="{RED}"/>
    <!-- Bottom tier: Elephants -->
    <ellipse cx="20" cy="46" rx="4" ry="3" fill="{SLATE}"/>
    <ellipse cx="32" cy="46" rx="4" ry="3" fill="{SLATE}"/>
    <ellipse cx="44" cy="46" rx="4" ry="3" fill="{SLATE}"/>
    """)

    # 8. Badami Cave Rock-Cut Column
    add("arch_08_badami_cave_temple", "Badami Cave Rock-Cut Column", "ಬಾದಾಮಿ ಗುಹಾ ದೇವಾಲಯ ಕಂಬ", ["badami", "cave", "chalukya"], f"""
    <!-- Heavy rock lintel and base -->
    <rect x="12" y="12" width="40" height="8" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    <rect x="12" y="48" width="40" height="8" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    <!-- Heavy Fluted Pillar Shaft -->
    <rect x="24" y="20" width="16" height="28" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <line x1="28" y1="20" x2="28" y2="48" stroke="{SLATE}" stroke-width="1.5"/>
    <line x1="36" y1="20" x2="36" y2="48" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Cushion capital (Amalaka) -->
    <ellipse cx="32" cy="22" rx="10" ry="3" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    """)

    # 9. Badami Nataraja 18-armed
    add("arch_09_badami_nataraja", "Badami Nataraja Cave 1", "ಬಾದಾಮಿ ನಟರಾಜ ಶಿಲ್ಪ", ["nataraja", "shiva", "dance", "badami"], f"""
    <circle cx="32" cy="18" r="4" fill="{GOLD}"/>
    <!-- Body in dance posture -->
    <path d="M 32 22 L 32 38 L 24 50 M 32 38 L 40 44 L 38 52" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    <!-- Multiple dancing arms radiating -->
    <path d="M 32 24 C 20 20 14 14 12 18" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 32 26 C 18 26 12 28 10 32" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 32 28 C 20 34 14 40 12 44" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 32 24 C 44 20 50 14 52 18" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 32 26 C 46 26 52 28 54 32" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    <path d="M 32 28 C 44 34 50 40 52 44" stroke="{RED}" stroke-width="1.5" stroke-linecap="round"/>
    """)

    # 10. Pattadakal Virupaksha Shikhara
    add("arch_10_pattadakal_virupaksha", "Pattadakal Temple Shikhara", "ಪಟ್ಟದಕಲ್ಲು ದೇವಾಲಯ ಶಿಖರ", ["pattadakal", "shikhara", "unesco"], f"""
    <!-- Dravidian vimana tiers -->
    <polygon points="32,10 16,46 48,46" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2"/>
    <rect x="22" y="20" width="20" height="5" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
    <rect x="19" y="30" width="26" height="5" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
    <rect x="16" y="40" width="32" height="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Amalaka & Kalasa -->
    <ellipse cx="32" cy="10" rx="5" ry="2.5" fill="{GOLD}"/>
    <circle cx="32" cy="7" r="2" fill="{RED}"/>
    <line x1="12" y1="52" x2="52" y2="52" stroke="{SLATE}" stroke-width="2.5"/>
    """)

    # 11. Aihole Durga Temple Apsidal Plan
    add("arch_11_aihole_durga_temple", "Aihole Durga Temple (Gajaprishtha)", "ಐಹೊಳೆ ದುರ್ಗಾ ದೇವಾಲಯ ಗಜಪೃಷ್ಠ", ["aihole", "durga", "apsidal"], f"""
    <!-- Apsidal curve at left, porch at right -->
    <path d="M 24 18 C 12 18 12 46 24 46 L 50 46 L 50 18 Z" fill="rgba(212,175,55,0.15)" stroke="{SLATE}" stroke-width="2.5"/>
    <!-- Colonnade pillared ambulatory -->
    <circle cx="20" cy="24" r="2" fill="{GOLD}"/>
    <circle cx="16" cy="32" r="2" fill="{GOLD}"/>
    <circle cx="20" cy="40" r="2" fill="{GOLD}"/>
    <circle cx="28" cy="24" r="2" fill="{GOLD}"/>
    <circle cx="28" cy="40" r="2" fill="{GOLD}"/>
    <circle cx="38" cy="24" r="2" fill="{GOLD}"/>
    <circle cx="38" cy="40" r="2" fill="{GOLD}"/>
    <circle cx="46" cy="24" r="2" fill="{GOLD}"/>
    <circle cx="46" cy="40" r="2" fill="{GOLD}"/>
    <!-- Inner Sanctum -->
    <rect x="26" y="28" width="12" height="8" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="1"/>
    """)

    # 12. Aihole Lad Khan Temple
    add("arch_12_aihole_lad_khan", "Aihole Lad Khan Temple", "ಐಹೊಳೆ ಲಾಡ್ ಖಾನ್ ದೇವಾಲಯ", ["aihole", "ladkhan", "chalukya"], f"""
    <!-- Sloping stone roof slabs -->
    <polygon points="32,16 12,32 52,32" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <polygon points="32,10 24,16 40,16" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="32" cy="8" r="2" fill="{RED}"/>
    <!-- Pillared Mandapa below -->
    <rect x="14" y="32" width="36" height="22" fill="rgba(148,163,184,0.1)" stroke="{SLATE}" stroke-width="2"/>
    <line x1="22" y1="32" x2="22" y2="54" stroke="{SLATE}" stroke-width="2"/>
    <line x1="32" y1="32" x2="32" y2="54" stroke="{SLATE}" stroke-width="2"/>
    <line x1="42" y1="32" x2="42" y2="54" stroke="{SLATE}" stroke-width="2"/>
    """)

    # 13. Gol Gumbaz Whispering Gallery Dome
    add("arch_13_gol_gumbaz_dome", "Gol Gumbaz Whispering Dome", "ಗೋಲ್ ಗುಂಬಜ್ ಗುಮ್ಮಟ", ["golgumbaz", "bijapur", "dome"], f"""
    <!-- Enormous Circular Hemisphere Dome -->
    <path d="M 12 36 C 12 14 52 14 52 36 Z" fill="rgba(148,163,184,0.2)" stroke="{SLATE}" stroke-width="2.5"/>
    <!-- Lotus petal rim at dome base -->
    <path d="M 10 36 C 14 34 18 36 22 36 C 26 34 30 36 34 36 C 38 34 42 36 46 36 C 50 34 54 36 54 36" stroke="{GOLD}" stroke-width="2" fill="none"/>
    <!-- Cubical Base -->
    <rect x="12" y="36" width="40" height="20" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Central Arch -->
    <path d="M 24 56 L 24 44 C 24 40 40 40 40 44 L 40 56 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Finial Crescent -->
    <circle cx="32" cy="12" r="2.5" fill="{GOLD}"/>
    """)

    # 14. Gol Gumbaz Minaret Tower
    add("arch_14_gol_gumbaz_minaret", "Gol Gumbaz Octagonal Minaret", "ಗೋಲ್ ಗುಂಬಜ್ ಅಷ್ಟಕೋನ ಮಿನಾರ", ["minaret", "bijapur", "tower"], f"""
    <!-- 7-Storey slender tower with domed cupola -->
    <rect x="24" y="16" width="16" height="40" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Balcony layers -->
    <line x1="22" y1="22" x2="42" y2="22" stroke="{GOLD}" stroke-width="2"/>
    <line x1="22" y1="28" x2="42" y2="28" stroke="{GOLD}" stroke-width="2"/>
    <line x1="22" y1="34" x2="42" y2="34" stroke="{GOLD}" stroke-width="2"/>
    <line x1="22" y1="40" x2="42" y2="40" stroke="{GOLD}" stroke-width="2"/>
    <line x1="22" y1="46" x2="42" y2="46" stroke="{GOLD}" stroke-width="2"/>
    <!-- Top Onion Cupola Dome -->
    <path d="M 24 16 C 24 10 32 8 32 8 C 32 8 40 10 40 16 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <circle cx="32" cy="6" r="1.5" fill="{RED}"/>
    """)

    # 15. Ibrahim Rauza
    add("arch_15_ibrahim_rauza", "Ibrahim Rauza Bijapur", "ಇಬ್ರಾಹಿಂ ರೋಜಾ ಬಿಜಾಪುರ", ["ibrahimrauza", "bijapur", "tajofsouth"], f"""
    <!-- Delicate minarets and central dome -->
    <rect x="18" y="32" width="28" height="22" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Bulbous dome -->
    <path d="M 24 32 C 24 22 32 18 32 18 C 32 18 40 22 40 32 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <circle cx="32" cy="16" r="2" fill="{RED}"/>
    <!-- Four slender corner minarets -->
    <line x1="14" y1="54" x2="14" y2="16" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    <line x1="50" y1="54" x2="50" y2="16" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    <circle cx="14" cy="14" r="2" fill="{GOLD}"/>
    <circle cx="50" cy="14" r="2" fill="{GOLD}"/>
    """)

    # 16. Gommateshwara Bahubali Monolith
    add("arch_16_gommateshwara_bahubali", "Gommateshwara Bahubali Monolith", "ಗೊಮ್ಮಟೇಶ್ವರ ಬಾಹುಬಲಿ ಏಕಶಿಲಾ ಮೂರ್ತಿ", ["bahubali", "shravanabelagola", "monolith", "jain"], f"""
    <!-- Kayotsarga standing posture -->
    <circle cx="32" cy="12" r="5" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Long earlobes & serene curly hair -->
    <path d="M 27 12 L 26 16 M 37 12 L 38 16" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Torso and arms down to knees -->
    <path d="M 28 17 L 26 38 L 26 44 M 36 17 L 38 38 L 38 44" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
    <path d="M 28 24 L 28 42 L 30 56 M 36 24 L 36 42 L 34 56" stroke="{SLATE}" stroke-width="2" stroke-linecap="round"/>
    <!-- Creepers (Madhavi latha) twining on legs -->
    <path d="M 24 48 Q 28 50 25 54 M 39 48 Q 36 50 39 54" stroke="{GREEN}" stroke-width="1.5" fill="none"/>
    <!-- Anthill and lotus pedestal at feet -->
    <ellipse cx="32" cy="58" rx="14" ry="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    """)

    # 17-60 Architecture Monuments
    monuments_batch = [
        ("arch_17_bidar_fort_gate", "Bidar Fort Arched Gateway", "ಬೀದರ್ ಕೋಟೆ ಬೃಹತ್ ದ್ವಾರ", ["bidar", "fort", "gateway"], f"""
        <path d="M 12 56 L 12 28 C 12 18 20 14 32 14 C 44 14 52 18 52 28 L 52 56" stroke="{SLATE}" stroke-width="2.5" fill="rgba(100,116,139,0.2)"/>
        <!-- Pointed Arch Gate -->
        <path d="M 22 56 L 22 36 C 22 26 32 24 32 24 C 32 24 42 26 42 36 L 42 56 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <line x1="8" y1="56" x2="56" y2="56" stroke="{SLATE}" stroke-width="2.5"/>
        """),
        ("arch_18_mahmud_gawan_madrasa", "Mahmud Gawan Madrasa Minaret", "ಮಹಮೂದ್ ಗವಾನ್ ಮದರಸಾ", ["bidar", "madrasa", "minaret"], f"""
        <rect x="24" y="16" width="16" height="40" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Glazed Persian ceramic pattern lines -->
        <line x1="24" y1="24" x2="40" y2="24" stroke="{SKY_BLUE}" stroke-width="2"/>
        <line x1="24" y1="32" x2="40" y2="32" stroke="{GREEN}" stroke-width="2"/>
        <line x1="24" y1="40" x2="40" y2="40" stroke="{GOLD}" stroke-width="2"/>
        <line x1="24" y1="48" x2="40" y2="48" stroke="{SKY_BLUE}" stroke-width="2"/>
        <path d="M 24 16 C 24 10 32 8 32 8 C 32 8 40 10 40 16 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """),
        ("arch_19_chitradurga_kallina_kote", "Chitradurga Kallina Kote (7 Rings)", "ಚಿತ್ರದುರ್ಗ ಕಲ್ಲಿನ ಕೋಟೆ (ಏಳು ಸುತ್ತಿನ ಕೋಟೆ)", ["chitradurga", "fortress", "bastion"], f"""
        <!-- Concentric stone battlement rings -->
        <path d="M 10 52 C 10 32 20 20 32 20 C 44 20 54 32 54 52" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
        <path d="M 16 52 C 16 36 22 28 32 28 C 42 28 48 36 48 52" stroke="{BROWN}" stroke-width="2" fill="none"/>
        <path d="M 22 52 C 22 42 26 36 32 36 C 38 36 42 42 42 52" stroke="{SLATE}" stroke-width="2" fill="none"/>
        <!-- Watchtower on rock -->
        <rect x="28" y="12" width="8" height="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="10" r="1.5" fill="{RED}"/>
        """),
        ("arch_20_onake_obavva_kindi", "Onake Obavva Kindi & Pestle", "ಒನಕೆ ಓಬವ್ವನ ಕಿಂಡಿ", ["obavva", "chitradurga", "onake", "bravery"], f"""
        <!-- Fort Boulder Crevice -->
        <path d="M 12 12 L 26 12 L 26 52 L 12 52 Z" fill="{SLATE}"/>
        <path d="M 38 12 L 52 12 L 52 52 L 38 52 Z" fill="{SLATE}"/>
        <!-- The narrow Kindi opening in center -->
        <!-- Onake (Heavy Wooden Pestle) held diagonally -->
        <line x1="18" y1="46" x2="44" y2="18" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>
        <!-- Iron ring tip on pestle -->
        <circle cx="43" cy="19" r="3" fill="{SILVER}" stroke="{DARK}" stroke-width="1"/>
        <circle cx="19" cy="45" r="3" fill="{SILVER}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("arch_21_vidhana_soudha_facade", "Vidhana Soudha Central Facade", "ವಿಧಾನ ಸೌಧ ಮುಂಭಾಗ", ["vidhana", "soudha", "bangalore"], f"""
        <!-- Massive Dravidian style legislative palace -->
        <rect x="10" y="32" width="44" height="24" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Pillars -->
        <line x1="16" y1="36" x2="16" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="22" y1="36" x2="22" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="28" y1="36" x2="28" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="36" y1="36" x2="36" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="42" y1="36" x2="42" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="48" y1="36" x2="48" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Pediment Arch with inscription -->
        <polygon points="32,24 14,32 50,32" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Central Majestic Dome -->
        <path d="M 24 24 C 24 14 40 14 40 24 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="14" x2="32" y2="8" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="7" r="2" fill="{RED}"/>
        """),
        ("arch_22_vidhana_soudha_dome", "Vidhana Soudha Lion Capital Dome", "ವಿಧಾನ ಸೌಧ ಸಿಂಹ ಲಾಂಛನ ಗುಮ್ಮಟ", ["dome", "ashoka", "lions", "vidhana"], f"""
        <path d="M 16 38 C 16 18 48 18 48 38 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <line x1="32" y1="18" x2="32" y2="10" stroke="{GOLD}" stroke-width="2"/>
        <!-- 4-Lion Ashoka Capital silhouette atop -->
        <circle cx="32" cy="8" r="2.5" fill="{GOLD}"/>
        <rect x="28" y="9" width="8" height="3" fill="{RED}"/>
        <rect x="12" y="38" width="40" height="12" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """),
        ("arch_23_bangalore_palace", "Bangalore Palace Tudor Turret", "ಬೆಂಗಳೂರು ಅರಮನೆ ಗೋಪುರ", ["bangalore", "palace", "tudor"], f"""
        <!-- Fortified stone castle turret with battlements -->
        <rect x="20" y="20" width="24" height="34" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Crenellations atop -->
        <rect x="18" y="14" width="6" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="29" y="14" width="6" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="40" y="14" width="6" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Tudor windows -->
        <rect x="28" y="26" width="8" height="10" rx="4" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="28" y="42" width="8" height="10" rx="4" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("arch_24_murudeshwar_shiva", "Murudeshwar Shiva Statue", "ಮುರುಡೇಶ್ವರ ಬೃಹತ್ ಶಿವನ ಮೂರ್ತಿ", ["murudeshwar", "shiva", "coastal"], f"""
        <!-- Gigantic seated Shiva silhouette -->
        <circle cx="32" cy="16" r="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 32 10 L 32 6 M 30 8 L 34 8" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Trishula in right hand -->
        <line x1="46" y1="14" x2="46" y2="52" stroke="{GOLD}" stroke-width="2"/>
        <path d="M 42 16 Q 46 12 50 16 M 46 12 L 46 16" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <!-- Seated cross-legged posture -->
        <path d="M 24 30 L 20 46 L 44 46 L 40 30" stroke="{SLATE}" stroke-width="2" fill="rgba(212,175,55,0.1)"/>
        <!-- Damaru -->
        <polygon points="44,28 48,28 46,32 48,36 44,36" fill="{RED}"/>
        """),
        ("arch_25_murudeshwar_gopuram", "Murudeshwar Raja Gopuram (20 storeys)", "ಮುರುಡೇಶ್ವರ ರಾಜಗೋಪುರ", ["murudeshwar", "gopuram", "tower"], f"""
        <polygon points="32,6 16,50 48,50" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Multi-tier windows -->
        <line x1="28" y1="14" x2="36" y2="14" stroke="{GOLD}" stroke-width="2"/>
        <line x1="25" y1="22" x2="39" y2="22" stroke="{GOLD}" stroke-width="2"/>
        <line x1="22" y1="30" x2="42" y2="30" stroke="{GOLD}" stroke-width="2"/>
        <line x1="19" y1="38" x2="45" y2="38" stroke="{GOLD}" stroke-width="2"/>
        <line x1="16" y1="46" x2="48" y2="46" stroke="{GOLD}" stroke-width="2"/>
        <rect x="28" y="50" width="8" height="8" fill="{DARK}"/>
        """),
        ("arch_26_udupi_krishna_mutt", "Udupi Sri Krishna Mutt", "ಉಡುಪಿ ಶ್ರೀ ಕೃಷ್ಣ ಮಠ", ["udupi", "krishna", "mutt", "madhwacharya"], f"""
        <rect x="14" y="28" width="36" height="26" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Sloping terracotta Mangalore-tiled roof -->
        <polygon points="32,12 8,28 56,28" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="10" r="2" fill="{GOLD}"/>
        <!-- Sacred Tulasi & lamp post -->
        <rect x="28" y="40" width="8" height="14" fill="{BROWN}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="32" cy="34" r="2" fill="{YELLOW}"/>
        """),
        ("arch_27_kanakana_kindi", "Kanakana Kindi (9-Window Grill)", "ಕನಕನ ಕಿಂಡಿ (ಒಂಬತ್ತು ರಂಧ್ರಗಳ ಕಿಂಡಿ)", ["kanaka", "kindi", "udupi", "silver"], f"""
        <!-- 9-hole Silver Window -->
        <rect x="14" y="14" width="36" height="36" rx="4" fill="rgba(148,163,184,0.2)" stroke="{SILVER}" stroke-width="3"/>
        <!-- 3x3 Grid of sacred holes -->
        <circle cx="21" cy="21" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="32" cy="21" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="43" cy="21" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="21" cy="32" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="32" cy="32" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="43" cy="32" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="21" cy="43" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="32" cy="43" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        <circle cx="43" cy="43" r="3" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("arch_28_dharmasthala_manjunatha", "Dharmasthala Manjunatha Temple", "ಧರ್ಮಸ್ಥಳ ಮಂಜುನಾಥ ಸ್ವಾಮಿ ದೇವಾಲಯ", ["dharmasthala", "manjunatha", "shrine"], f"""
        <polygon points="32,10 12,32 52,32" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="8" r="2.5" fill="{GOLD}"/>
        <rect x="16" y="32" width="32" height="22" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 28 54 L 28 42 C 28 38 36 38 36 42 L 36 54 Z" fill="{DARK}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="22" cy="40" r="1.5" fill="{RED}"/>
        <circle cx="42" cy="40" r="1.5" fill="{RED}"/>
        """),
        ("arch_29_melukote_cheluvanarayana", "Melukote Cheluvanarayana Hill Temple", "ಮೇಲುಕೋಟೆ ಚೆಲುವನಾರಾಯಣ ದೇವಾಲಯ", ["melukote", "hill", "vairamudi"], f"""
        <!-- Hill contours below -->
        <path d="M 8 56 Q 32 46 56 56" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
        <path d="M 14 50 Q 32 42 50 50" stroke="{SLATE}" stroke-width="2" fill="none"/>
        <!-- Temple atop -->
        <rect x="22" y="26" width="20" height="18" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <polygon points="32,12 20,26 44,26" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        <!-- Steps leading up -->
        <line x1="28" y1="46" x2="36" y2="46" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="26" y1="50" x2="38" y2="50" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("arch_30_melukote_raya_gopura", "Melukote Raya Gopura Monolith Pillars", "ಮೇಲುಕೋಟೆ ರಾಯಗೋಪುರ", ["raya", "gopura", "melukote", "pillars"], f"""
        <!-- Massive unfinished 4 pillars standing proud against the sky -->
        <rect x="14" y="16" width="6" height="38" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <rect x="44" y="16" width="6" height="38" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <rect x="24" y="22" width="5" height="32" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <rect x="35" y="22" width="5" height="32" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Stone beam across top -->
        <line x1="10" y1="16" x2="54" y2="16" stroke="{SLATE}" stroke-width="3"/>
        <circle cx="17" cy="12" r="2" fill="{GOLD}"/>
        <circle cx="47" cy="12" r="2" fill="{GOLD}"/>
        """),
        ("arch_31_sringeri_vidyashankara", "Sringeri Vidyashankara Temple", "ಶೃಂಗೇರಿ ವಿದ್ಯಾಶಂಕರ ದೇವಾಲಯ", ["sringeri", "sharada", "zodiac", "pillars"], f"""
        <path d="M 12 48 C 12 30 20 22 32 12 C 44 22 52 30 52 48 Z" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="32" cy="10" r="2.5" fill="{RED}"/>
        <!-- 12 Zodiac Rashi pillars represented -->
        <line x1="18" y1="48" x2="18" y2="34" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="24" y1="48" x2="24" y2="28" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="32" y1="48" x2="32" y2="24" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="40" y1="48" x2="40" y2="28" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="46" y1="48" x2="46" y2="34" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="8" y1="52" x2="56" y2="52" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_32_horanadu_annapoorneshwari", "Horanadu Annapoorneshwari Temple", "ಹೊರನಾಡು ಅನ್ನಪೂರ್ಣೇಶ್ವರಿ ದೇವಾಲಯ", ["horanadu", "annapoorneshwari", "gold"], f"""
        <polygon points="32,8 14,28 50,28" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="6" r="2" fill="{RED}"/>
        <rect x="16" y="28" width="32" height="26" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Golden spoon & bowl (Annapoorneshwari blessing) -->
        <circle cx="32" cy="40" r="5" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="35" x2="42" y2="28" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>
        """),
        ("arch_33_kukke_subramanya", "Kukke Subramanya Temple", "ಕುಕ್ಕೆ ಸುಬ್ರಹ್ಮಣ್ಯ ದೇವಾಲಯ", ["kukke", "subramanya", "naga"], f"""
        <polygon points="32,10 14,30 50,30" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <rect x="18" y="30" width="28" height="24" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Serpent / Naga emblem on doorway -->
        <path d="M 32 46 C 30 42 34 38 32 34 C 34 32 36 34 36 36" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="8" r="2" fill="{GOLD}"/>
        """),
        ("arch_34_chamundeshwari_temple", "Chamundeshwari Temple Gopuram", "ಚಾಮುಂಡೇಶ್ವರಿ ದೇವಾಲಯ ಗೋಪುರ", ["chamundi", "mysore", "gopuram"], f"""
        <polygon points="32,8 18,44 46,44" fill="rgba(200,16,46,0.2)" stroke="{RED}" stroke-width="2"/>
        <rect x="16" y="44" width="32" height="12" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 28 56 L 28 48 C 28 44 36 44 36 48 L 36 56 Z" fill="{DARK}"/>
        <circle cx="32" cy="6" r="2" fill="{GOLD}"/>
        """),
        ("arch_35_chamundi_nandi", "Chamundi Hill Monolithic Nandi", "ಚಾಮುಂಡಿ ಬೆಟ್ಟದ ಬೃಹತ್ ನಂದಿ", ["nandi", "bull", "monolith", "chamundi"], f"""
        <!-- Recumbent majestic monolithic bull -->
        <ellipse cx="32" cy="38" rx="18" ry="12" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Head & Horns -->
        <circle cx="44" cy="26" r="8" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 44 20 L 46 12 M 40 20 L 38 12" stroke="{GOLD}" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Bell garland (Gante sara) around neck -->
        <path d="M 36 28 C 36 34 42 36 44 32" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="40" cy="34" r="2" fill="{RED}"/>
        <!-- Hump -->
        <ellipse cx="26" cy="26" rx="6" ry="5" fill="{SLATE}"/>
        <line x1="12" y1="52" x2="52" y2="52" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_36_somanathapura_keshava", "Somanathapura Keshava Trikuta Shikhara", "ಸೋಮನಾಥಪುರ ಕೇಶವ ದೇವಾಲಯ", ["somanathapura", "trikuta", "hoysala"], f"""
        <!-- Triple Shikharas -->
        <polygon points="18,16 10,40 26,40" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.5"/>
        <polygon points="32,10 22,40 42,40" fill="{CREAM}" stroke="{GOLD}" stroke-width="2"/>
        <polygon points="46,16 38,40 54,40" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="18" cy="14" r="1.5" fill="{RED}"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        <circle cx="46" cy="14" r="1.5" fill="{RED}"/>
        <rect x="10" y="40" width="44" height="14" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        """),
        ("arch_37_belavadi_veera_narayana", "Belavadi Veera Narayana Temple", "ಬೆಳವಾಡಿ ವೀರನಾರಾಯಣ ದೇವಾಲಯ", ["belavadi", "trikuta", "shikhara"], f"""
        <polygon points="32,12 18,36 46,36" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        <rect x="14" y="36" width="36" height="18" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <line x1="20" y1="36" x2="20" y2="54" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="32" y1="36" x2="32" y2="54" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="44" y1="36" x2="44" y2="54" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("arch_38_lakkundi_kasi_vishveshwara", "Lakkundi Kalyani Stepwell", "ಲಕ್ಕುಂಡಿ ಕಲ್ಯಾಣಿ ಮೆಟ್ಟಿಲು ಬಾವಿ", ["lakkundi", "stepwell", "kalyani"], f"""
        <!-- Stepped square well -->
        <rect x="12" y="12" width="40" height="40" stroke="{SLATE}" stroke-width="2" fill="none"/>
        <rect x="18" y="18" width="28" height="28" stroke="{SLATE}" stroke-width="2" fill="none"/>
        <rect x="24" y="24" width="16" height="16" stroke="{SLATE}" stroke-width="2" fill="{SKY_BLUE}"/>
        <!-- Corner steps -->
        <line x1="12" y1="12" x2="24" y2="24" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="52" y1="12" x2="40" y2="24" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="12" y1="52" x2="24" y2="40" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="52" y1="52" x2="40" y2="40" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("arch_39_itagi_mahadeva", "Itagi Mahadeva Temple (Devalaya Chakravarthi)", "ಇಟಗಿ ಮಹಾದೇವ ದೇವಾಲಯ", ["itagi", "chalukya", "kalyani"], f"""
        <polygon points="32,10 16,42 48,42" fill="rgba(212,175,55,0.2)" stroke="{GOLD}" stroke-width="2"/>
        <rect x="12" y="42" width="40" height="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        <line x1="22" y1="42" x2="22" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        <line x1="42" y1="42" x2="42" y2="56" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("arch_40_banavasi_madhukeshwara", "Banavasi Madhukeshwara Temple", "ಬನವಾಸಿ ಮಧುಕೇಶ್ವರ ದೇವಾಲಯ", ["banavasi", "kadamba", "heritage"], f"""
        <polygon points="32,12 16,34 48,34" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <rect x="14" y="34" width="36" height="20" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 28 54 L 28 42 C 28 38 36 38 36 42 L 36 54" stroke="{DARK}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        """),
        ("arch_41_mirjan_fort", "Mirjan Fort Laterite Bastion", "ಮಿರ್ಜಾನ್ ಕೋಟೆ", ["mirjan", "fort", "laterite", "kumta"], f"""
        <rect x="16" y="24" width="32" height="30" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Curved circular bastions -->
        <circle cx="16" cy="38" r="8" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="48" cy="38" r="8" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Rampart loopholes -->
        <rect x="22" y="18" width="4" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="30" y="18" width="4" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="38" y="18" width="4" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("arch_42_namdroling_golden_temple", "Bylakuppe Namdroling Golden Pagoda", "ಬೈಲುಕುಪ್ಪೆ ಸುವರ್ಣ ದೇವಾಲಯ ಪಗೋಡ", ["namdroling", "bylakuppe", "tibetan", "pagoda"], f"""
        <!-- Multitier pagoda roof with upturned eaves -->
        <path d="M 20 22 Q 32 16 44 22 L 40 26 L 24 26 Z" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
        <path d="M 16 34 Q 32 26 48 34 L 44 38 L 20 38 Z" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
        <path d="M 12 46 Q 32 36 52 46 L 48 50 L 16 50 Z" fill="{GOLD}" stroke="{RED}" stroke-width="1.5"/>
        <!-- Golden Spire finial -->
        <line x1="32" y1="16" x2="32" y2="8" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="32" cy="7" r="2" fill="{RED}"/>
        """),
        ("arch_43_madikeri_fort", "Madikeri Fort & Palace", "ಮಡಿಕೇರಿ ಕೋಟೆ", ["madikeri", "coorg", "fort"], f"""
        <!-- Fort wall with life-size stone elephant silhouette -->
        <path d="M 10 52 L 10 32 L 20 32 L 20 36 L 44 36 L 44 32 L 54 32 L 54 52 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Elephant statue inside -->
        <circle cx="32" cy="42" r="5" fill="{SLATE}"/>
        <path d="M 32 40 L 38 46" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_44_hampi_lotus_mahal", "Hampi Lotus Mahal", "ಹಂಪಿ ಕಮಲ ಮಹಲ್", ["lotusmahal", "hampi", "vijayanagara"], f"""
        <!-- Multi-foliated Islamic/Hindu Cusped Arches -->
        <rect x="16" y="32" width="32" height="22" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 22 54 L 22 42 C 22 36 28 36 32 38 C 36 36 42 36 42 42 L 42 54" stroke="{RED}" stroke-width="2" fill="none"/>
        <!-- Lotus Petal Pyramidal Roof -->
        <polygon points="32,10 14,32 50,32" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        """),
        ("arch_45_hampi_elephant_stables", "Hampi Elephant Stables (Gaja Shaale)", "ಹಂಪಿ ಆನೆ ಲಾಯ (ಗಜ ಶಾಲೆ)", ["elephants", "stables", "hampi"], f"""
        <!-- Row of domed chambers -->
        <rect x="10" y="34" width="44" height="20" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- 3 Domes -->
        <path d="M 12 34 C 12 24 24 24 24 34 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 26 34 C 26 22 38 22 38 34 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 40 34 C 40 24 52 24 52 34 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- 3 Arched Entrances -->
        <path d="M 14 54 L 14 42 C 14 38 22 38 22 42 L 22 54" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 28 54 L 28 40 C 28 36 36 36 36 40 L 36 54" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 42 54 L 42 42 C 42 38 50 38 50 42 L 50 54" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("arch_46_hampi_queens_bath", "Hampi Queen's Bath (Snanagruha)", "ಹಂಪಿ ರಾಣಿಯ ಸ್ನಾನಗೃಹ", ["queensbath", "hampi", "pool"], f"""
        <rect x="12" y="14" width="40" height="38" rx="2" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Stepped water basin in center -->
        <rect x="22" y="24" width="20" height="18" fill="{SKY_BLUE}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Balconies / Jharokhas -->
        <path d="M 16 30 Q 18 33 20 30" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <path d="M 44 30 Q 46 33 48 30" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("arch_47_hampi_mahanavami_dibba", "Mahanavami Dibba Stepped Platform", "ಮಹಾನವಮಿ ದಿಬ್ಬ", ["mahanavami", "dibba", "dasara", "platform"], f"""
        <!-- 3 Stepped stone tiers -->
        <rect x="10" y="44" width="44" height="10" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="16" y="32" width="32" height="12" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="22" y="20" width="20" height="12" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Royal Throne dais atop -->
        <rect x="28" y="16" width="8" height="4" fill="{GOLD}" stroke="{RED}" stroke-width="1"/>
        <!-- Central staircase -->
        <line x1="32" y1="20" x2="32" y2="54" stroke="{YELLOW}" stroke-width="2"/>
        """),
        ("arch_48_hampi_sasivekalu_ganesha", "Sasivekalu Ganesha Monolith", "ಸಾಸಿವೆಕಾಳು ಗಣೇಶ", ["sasivekalu", "ganesha", "hampi"], f"""
        <!-- Giant Ganesha carved from single boulder -->
        <circle cx="32" cy="24" r="10" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="42" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Trunk curving left -->
        <path d="M 32 26 C 30 34 22 34 22 30" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
        <!-- Snake belt tied around belly -->
        <path d="M 20 42 C 26 46 38 46 44 42" stroke="{GREEN}" stroke-width="2" fill="none"/>
        """),
        ("arch_49_hampi_kadalekalu_ganesha", "Kadalekalu Ganesha Temple", "ಕಡಲೆಕಾಳು ಗಣೇಶ", ["kadalekalu", "ganesha", "monolith"], f"""
        <!-- Huge seated Ganesha behind tall pillars -->
        <circle cx="32" cy="30" r="12" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Tall slender front pillars -->
        <line x1="16" y1="14" x2="16" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="48" y1="14" x2="48" y2="54" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="12" y1="14" x2="52" y2="14" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_50_hampi_ugra_narasimha", "Hampi Ugra Narasimha Monolith", "ಹಂಪಿ ಉಗ್ರ ನರಸಿಂಹ ಏಕಶಿಲೆ", ["narasimha", "ugra", "hampi", "monolith"], f"""
        <!-- 6.7m monolithic Narasimha with Sheshanaga hood -->
        <circle cx="32" cy="28" r="8" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- 7-headed Snake Hood above -->
        <path d="M 18 20 C 22 10 42 10 46 20" stroke="{GOLD}" stroke-width="4" fill="none"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        <!-- Wide protruding eyes & lion mouth -->
        <circle cx="28" cy="26" r="2" fill="{RED}"/>
        <circle cx="36" cy="26" r="2" fill="{RED}"/>
        <path d="M 28 32 Q 32 36 36 32" stroke="{DARK}" stroke-width="2" fill="none"/>
        <!-- Yoga-patta strap around knees -->
        <path d="M 18 48 C 24 44 40 44 46 48" stroke="{SLATE}" stroke-width="3" fill="none"/>
        """),
        ("arch_51_talakad_keerthinarayana", "Talakad Buried Temple", "ತಲಕಾಡು ಮರಳಿನ ದೇವಾಲಯ", ["talakad", "sand", "temple"], f"""
        <!-- Sand dunes engulfing stone temple shikhara -->
        <polygon points="32,12 20,36 44,36" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        <!-- Dunes of golden sand -->
        <path d="M 6 54 C 18 42 34 50 58 42 L 58 58 L 6 58 Z" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        """),
        ("arch_52_srirangapatna_gumbaz", "Srirangapatna Gumbaz Mausoleum", "ಶ್ರೀರಂಗಪಟ್ಟಣ ಗುಂಬಜ್", ["gumbaz", "tipu", "srirangapatna"], f"""
        <!-- Black basalt pillared verandah with ivory dome -->
        <path d="M 20 28 C 20 14 44 14 44 28 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="12" r="2" fill="{GOLD}"/>
        <rect x="14" y="28" width="36" height="26" fill="rgba(15,23,42,0.1)" stroke="{SLATE}" stroke-width="2"/>
        <!-- Black pillars -->
        <line x1="20" y1="28" x2="20" y2="54" stroke="{DARK}" stroke-width="2"/>
        <line x1="28" y1="28" x2="28" y2="54" stroke="{DARK}" stroke-width="2"/>
        <line x1="36" y1="28" x2="36" y2="54" stroke="{DARK}" stroke-width="2"/>
        <line x1="44" y1="28" x2="44" y2="54" stroke="{DARK}" stroke-width="2"/>
        """),
        ("arch_53_dariya_daulat_bagh", "Dariya Daulat Bagh Teakwood Palace", "ದರಿಯಾ ದೌಲತ್ ಬಾಗ್", ["dariyadaulat", "summerpalace", "teak"], f"""
        <!-- Ornate wooden cusped arches on wide veranda -->
        <rect x="12" y="30" width="40" height="24" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <polygon points="32,14 8,30 56,30" fill="{RED}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <path d="M 18 54 L 18 40 Q 24 36 28 40 L 28 54" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
        <path d="M 36 54 L 36 40 Q 40 36 46 40 L 46 54" stroke="{GOLD}" stroke-width="1.5" fill="none"/>
        """),
        ("arch_54_savandurga_fort_ruins", "Savandurga Monolith Fort Ruins", "ಸಾವನದುರ್ಗ ಕೋಟೆ", ["savandurga", "monolith", "hillfort"], f"""
        <!-- Massive curved rock dome with fort wall atop -->
        <path d="M 8 56 C 14 26 50 26 56 56 Z" fill="rgba(100,116,139,0.3)" stroke="{SLATE}" stroke-width="2.5"/>
        <!-- Stone battlements on crest -->
        <rect x="26" y="22" width="12" height="6" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="32" y1="22" x2="32" y2="16" stroke="{RED}" stroke-width="2"/>
        """),
        ("arch_55_nandi_hills_yoga_nandeeshwara", "Nandi Hills Temple & Cliff", "ನಂದಿ ಬೆಟ್ಟ ದೇವಾಲಯ ಮತ್ತು ಪ್ರಪಾತ", ["nandihills", "temple", "tipusdrop"], f"""
        <!-- Hill cliff profile -->
        <path d="M 8 56 L 8 36 L 40 36 L 56 56 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Small temple on plateau -->
        <polygon points="24,24 16,36 32,36" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="24" cy="22" r="1.5" fill="{RED}"/>
        """),
        ("arch_56_basavakalyan_fort", "Basavakalyan Fort Gateway", "ಬಸವಕಲ್ಯಾಣ ಕೋಟೆ ದ್ವಾರ", ["basavakalyan", "fort", "sharanas"], f"""
        <path d="M 14 54 L 14 26 C 14 16 50 16 50 26 L 50 54" stroke="{SLATE}" stroke-width="2.5" fill="rgba(148,163,184,0.15)"/>
        <path d="M 24 54 L 24 36 C 24 28 40 28 40 36 L 40 54" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_57_kudalasangama_mantapa", "Kudalasangama Aikya Mantapa", "ಕೂಡಲಸಂಗಮ ಐಕ್ಯ ಮಂಟಪ", ["kudalasangama", "basavanna", "aikya", "mantapa"], f"""
        <!-- Cylindrical submerged stupa/mantapa surrounded by water -->
        <rect x="20" y="24" width="24" height="24" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 20 24 C 20 14 44 14 44 24 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="12" r="2" fill="{RED}"/>
        <!-- Water waves of Krishna and Malaprabha confluence -->
        <path d="M 8 52 Q 20 48 32 52 Q 44 56 56 52" stroke="{SKY_BLUE}" stroke-width="2.5" fill="none"/>
        <path d="M 10 56 Q 22 52 34 56 Q 46 60 58 56" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("arch_58_keladi_rameshwara_temple", "Keladi Rameshwara Wooden Hall", "ಕೆಳದಿ ರಾಮೇಶ್ವರ ದೇವಾಲಯ", ["keladi", "wooden", "ceiling", "nayaka"], f"""
        <polygon points="32,12 12,32 52,32" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <rect x="16" y="32" width="32" height="22" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Ornate wood pillar carvings -->
        <line x1="22" y1="32" x2="22" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <line x1="42" y1="32" x2="42" y2="54" stroke="{BROWN}" stroke-width="2"/>
        <circle cx="32" cy="10" r="2" fill="{GOLD}"/>
        """),
        ("arch_59_ikkeri_aghoreshwara", "Ikkeri Aghoreshwara Granite Temple", "ಇಕ್ಕೇರಿ ಅಘೋರೇಶ್ವರ ದೇವಾಲಯ", ["ikkeri", "granite", "aghoreshwara"], f"""
        <polygon points="32,10 16,36 48,36" fill="rgba(100,116,139,0.2)" stroke="{SLATE}" stroke-width="2"/>
        <rect x="14" y="36" width="36" height="18" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="8" r="2" fill="{RED}"/>
        <line x1="10" y1="54" x2="54" y2="54" stroke="{SLATE}" stroke-width="2"/>
        """),
        ("arch_60_kolaramma_temple", "Kolaramma Temple & Kalyani", "ಕೋಲಾರಮ್ಮ ದೇವಾಲಯ ಮತ್ತು ಕಲ್ಯಾಣಿ", ["kolaramma", "kolar", "temple"], f"""
        <polygon points="32,12 18,34 46,34" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <rect x="18" y="34" width="28" height="20" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 28 54 L 28 44 C 28 40 36 40 36 44 L 36 54" stroke="{RED}" stroke-width="1.5" fill="none"/>
        <circle cx="32" cy="10" r="2" fill="{RED}"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in monuments_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
