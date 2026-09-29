"""
Category 10: Modern Karnataka, Innovation, Bengaluru Lifestyle & Heritage Icons (45 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "modern-karnataka-lifestyle",
            "tags": ["modern", "bengaluru", "lifestyle", "innovation", "tech", "karnataka"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Namma Metro Train
    add("modern_01_namma_metro_train", "Namma Metro Train", "ನಮ್ಮ ಮೆಟ್ರೋ ರೈಲು", ["nammametro", "bengaluru", "metro", "transit", "train"], f"""
    <!-- Aerodynamic silver metro train front with purple / green stripe -->
    <path d="M 18 16 C 18 10 46 10 46 16 L 44 46 C 44 50 20 50 20 46 Z" fill="{SILVER}" stroke="{DARK}" stroke-width="2"/>
    <!-- Windshield -->
    <path d="M 22 16 L 42 16 L 40 28 L 24 28 Z" fill="{DARK}"/>
    <!-- Purple Line / Green Line stripe -->
    <rect x="20" y="32" width="24" height="4" fill="{PURPLE}"/>
    <!-- Twin headlights -->
    <circle cx="25" cy="40" r="2.5" fill="{YELLOW}"/>
    <circle cx="39" cy="40" r="2.5" fill="{YELLOW}"/>
    <!-- Elevated track line -->
    <line x1="10" y1="52" x2="54" y2="52" stroke="{SLATE}" stroke-width="3"/>
    """)

    # 2. BMTC Bus
    add("modern_02_bmtc_volvo_bus", "BMTC City Bus", "ಬಿ.ಎಂ.ಟಿ.ಸಿ ಬಸ್", ["bmtc", "bus", "transport", "bengaluru"], f"""
    <!-- Iconic green & white BMTC bus body -->
    <rect x="12" y="16" width="40" height="28" rx="4" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
    <rect x="12" y="26" width="40" height="8" fill="{WHITE}"/>
    <!-- Windows -->
    <rect x="16" y="19" width="8" height="6" rx="1" fill="{SKY_BLUE}"/>
    <rect x="28" y="19" width="8" height="6" rx="1" fill="{SKY_BLUE}"/>
    <rect x="40" y="19" width="8" height="6" rx="1" fill="{SKY_BLUE}"/>
    <!-- Wheels -->
    <circle cx="22" cy="44" r="5" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
    <circle cx="42" cy="44" r="5" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
    <circle cx="22" cy="44" r="2" fill="{WHITE}"/>
    <circle cx="42" cy="44" r="2" fill="{WHITE}"/>
    """)

    # 3. Bengaluru Auto Rickshaw
    add("modern_03_bangalore_auto_rickshaw", "Bangalore Auto Rickshaw", "ಬೆಂಗಳೂರು ಆಟೋ ರಿಕ್ಷಾ", ["autorickshaw", "auto", "bengaluru", "yellowgreen"], f"""
    <!-- Yellow top, green bottom body -->
    <path d="M 22 14 L 38 14 C 44 14 48 20 48 28 L 48 42 L 16 42 L 16 28 C 16 20 18 14 22 14 Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="2"/>
    <rect x="16" y="28" width="32" height="14" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Windshield -->
    <polygon points="20,18 44,18 42,27 22,27" fill="{SKY_BLUE}"/>
    <!-- Wheels -->
    <circle cx="32" cy="46" r="4" fill="{DARK}"/>
    <circle cx="18" cy="46" r="4" fill="{DARK}"/>
    <circle cx="46" cy="46" r="4" fill="{DARK}"/>
    <!-- Single center headlight -->
    <circle cx="32" cy="34" r="2.5" fill="{YELLOW}" stroke="{DARK}" stroke-width="1"/>
    """)

    # 4. Silicon Valley Microchip
    add("modern_04_silicon_valley_microchip", "Silicon Valley Microchip", "ಸಿಲಿಕಾನ್ ಸಿಟಿ ಮೈಕ್ರೋಚಿಪ್", ["siliconvalley", "microchip", "tech", "it", "semiconductor"], f"""
    <!-- Square chip body -->
    <rect x="20" y="20" width="24" height="24" rx="3" fill="{DARK}" stroke="{GOLD}" stroke-width="2"/>
    <!-- Kannada 'ಕ' engraved in glowing center -->
    <circle cx="32" cy="32" r="6" fill="{GOLD}"/>
    <circle cx="32" cy="32" r="2" fill="{DARK}"/>
    <!-- Circuit pins radiating -->
    <line x1="26" y1="12" x2="26" y2="20" stroke="{GOLD}" stroke-width="2"/>
    <line x1="32" y1="12" x2="32" y2="20" stroke="{GOLD}" stroke-width="2"/>
    <line x1="38" y1="12" x2="38" y2="20" stroke="{GOLD}" stroke-width="2"/>
    <line x1="26" y1="44" x2="26" y2="52" stroke="{GOLD}" stroke-width="2"/>
    <line x1="32" y1="44" x2="32" y2="52" stroke="{GOLD}" stroke-width="2"/>
    <line x1="38" y1="44" x2="38" y2="52" stroke="{GOLD}" stroke-width="2"/>
    <line x1="12" y1="26" x2="20" y2="26" stroke="{GOLD}" stroke-width="2"/>
    <line x1="12" y1="32" x2="20" y2="32" stroke="{GOLD}" stroke-width="2"/>
    <line x1="12" y1="38" x2="20" y2="38" stroke="{GOLD}" stroke-width="2"/>
    <line x1="44" y1="26" x2="52" y2="26" stroke="{GOLD}" stroke-width="2"/>
    <line x1="44" y1="32" x2="52" y2="32" stroke="{GOLD}" stroke-width="2"/>
    <line x1="44" y1="38" x2="52" y2="38" stroke="{GOLD}" stroke-width="2"/>
    """)

    # 5. ISRO Rocket
    add("modern_05_isro_rocket_pslv_gslv", "ISRO Satellite Launch Vehicle", "ಇಸ್ರೋ ರಾಕೆಟ್ (ಪಿ.ಎಸ್.ಎಲ್.ವಿ)", ["isro", "space", "rocket", "pslv", "bengaluru"], f"""
    <!-- Rocket fuselage -->
    <path d="M 32 8 C 30 14 26 22 26 44 L 38 44 C 38 22 34 14 32 8 Z" fill="{WHITE}" stroke="{DARK}" stroke-width="2"/>
    <!-- Tricolor tip & strap-on boosters -->
    <polygon points="32,8 29,18 35,18" fill="{ORANGE}"/>
    <!-- Boosters -->
    <rect x="22" y="32" width="4" height="12" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <rect x="38" y="32" width="4" height="12" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <!-- Exhaust plume flame -->
    <polygon points="30,44 32,56 34,44" fill="{YELLOW}"/>
    <polygon points="31,44 32,52 33,44" fill="{RED}"/>
    """)

    # 6. ISRO Satellite
    add("modern_06_isro_satellite_aryabhata", "ISRO Satellite (Aryabhata)", "ಇಸ್ರೋ ಉಪಗ್ರಹ", ["satellite", "isro", "space", "solar"], f"""
    <!-- Central cubical satellite bus -->
    <rect x="24" y="24" width="16" height="16" fill="{GOLD}" stroke="{DARK}" stroke-width="2"/>
    <!-- Blue solar panels spread left and right -->
    <rect x="8" y="27" width="14" height="10" fill="{ROYAL_BLUE}" stroke="{SLATE}" stroke-width="1.5"/>
    <line x1="15" y1="27" x2="15" y2="37" stroke="{SLATE}" stroke-width="1"/>
    <rect x="42" y="27" width="14" height="10" fill="{ROYAL_BLUE}" stroke="{SLATE}" stroke-width="1.5"/>
    <line x1="49" y1="27" x2="49" y2="37" stroke="{SLATE}" stroke-width="1"/>
    <!-- Communications dish on top -->
    <circle cx="32" cy="18" r="4" fill="{SILVER}" stroke="{DARK}" stroke-width="1.5"/>
    <line x1="32" y1="24" x2="32" y2="18" stroke="{DARK}" stroke-width="2"/>
    """)

    # 7. HAL Tejas Fighter Jet
    add("modern_07_hal_tejas_fighter_jet", "HAL Tejas Fighter Jet", "ಎಚ್.ಎ.ಎಲ್ ತೇಜಸ್ ಯುದ್ಧ ವಿಮಾನ", ["tejas", "hal", "fighterjet", "defense", "aviation"], f"""
    <!-- Delta wing silhouette -->
    <polygon points="32,8 14,46 32,40 50,46" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
    <!-- Cockpit canopy -->
    <ellipse cx="32" cy="22" rx="3" ry="7" fill="{SKY_BLUE}" stroke="{DARK}" stroke-width="1"/>
    <!-- Fin -->
    <line x1="32" y1="36" x2="32" y2="44" stroke="{DARK}" stroke-width="2.5"/>
    """)

    # 8. IISc Bangalore Clock Tower
    add("modern_08_iisc_bangalore_tower", "IISc Bangalore Heritage Tower", "ಐ.ಐ.ಎಸ್.ಸಿ ಹೆರಿಟೇಜ್ ಗೋಪುರ", ["iisc", "tata", "science", "tower", "clock"], f"""
    <!-- Classical granite tower of Faculty Hall -->
    <rect x="24" y="18" width="16" height="34" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
    <polygon points="22,18 42,18 32,8" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Clock face -->
    <circle cx="32" cy="26" r="4" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
    <line x1="32" y1="26" x2="32" y2="24" stroke="{DARK}" stroke-width="1"/>
    <line x1="32" y1="26" x2="34" y2="26" stroke="{DARK}" stroke-width="1"/>
    <!-- Arched entrance below -->
    <path d="M 28 52 L 28 44 C 28 40 36 40 36 44 L 36 52 Z" fill="{DARK}"/>
    """)

    # 9. Lalbagh Glasshouse
    add("modern_09_lalbagh_glasshouse", "Lalbagh Botanical Glasshouse", "ಲಾಲ್‌ಬಾಗ್ ಗ್ಲಾಸ್‌ಹೌಸ್", ["lalbagh", "glasshouse", "garden", "bengaluru"], f"""
    <!-- Symmetrical iron and glass conservatory roof -->
    <path d="M 12 44 L 16 28 C 16 18 48 18 48 28 L 52 44 Z" fill="rgba(2,132,199,0.15)" stroke="{DARK}" stroke-width="2"/>
    <!-- Center dome cupola -->
    <path d="M 26 22 C 26 14 38 14 38 22" stroke="{DARK}" stroke-width="2" fill="none"/>
    <line x1="32" y1="14" x2="32" y2="10" stroke="{DARK}" stroke-width="2"/>
    <circle cx="32" cy="9" r="1.5" fill="{GOLD}"/>
    <!-- Lattice grid lines -->
    <line x1="24" y1="26" x2="24" y2="44" stroke="{SLATE}" stroke-width="1"/>
    <line x1="32" y1="22" x2="32" y2="44" stroke="{SLATE}" stroke-width="1"/>
    <line x1="40" y1="26" x2="40" y2="44" stroke="{SLATE}" stroke-width="1"/>
    <line x1="10" y1="44" x2="54" y2="44" stroke="{DARK}" stroke-width="2"/>
    """)

    # 10. Mysore Sandal Soap Oval
    add("modern_10_mysore_sandal_soap_oval", "Mysore Sandal Soap (Sharaba Logo)", "ಮೈಸೂರು ಸ್ಯಾಂಡಲ್ ಸೋಪ್", ["mysoresandal", "soap", "sharabha", "fragrance"], f"""
    <!-- Classic oval sandalwood soap bar -->
    <ellipse cx="32" cy="32" rx="22" ry="15" fill="{CREAM}" stroke="{GOLD}" stroke-width="2.5"/>
    <ellipse cx="32" cy="32" rx="17" ry="11" stroke="{DARK_GOLD}" stroke-width="1.5" stroke-dasharray="2 1" fill="none"/>
    <!-- Embossed Sharabha royal beast emblem in center -->
    <circle cx="32" cy="32" r="5" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
    <circle cx="32" cy="32" r="2" fill="{RED}"/>
    """)

    # 11-45 Modern Karnataka, Innovation, Lifestyle batch
    modern_batch = [
        ("modern_11_mysore_sandal_soap_box", "Mysore Sandal Soap Box", "ಮೈಸೂರು ಸ್ಯಾಂಡಲ್ ಸೋಪಿನ ಬಾಕ್ಸ್", ["soapbox", "ksdl", "greenbox"], f"""
        <!-- Rectangular green box with golden crest -->
        <rect x="14" y="20" width="36" height="24" rx="3" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="32" r="6" fill="{GOLD}" stroke="{YELLOW}" stroke-width="1.5"/>
        <line x1="18" y1="24" x2="46" y2="24" stroke="{GOLD}" stroke-width="1"/>
        <line x1="18" y1="40" x2="46" y2="40" stroke="{GOLD}" stroke-width="1"/>
        """),
        ("modern_12_sir_m_visvesvaraya_glasses", "Bharat Ratna Sir M. Visvesvaraya", "ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ", ["sir_mv", "engineer", "bharatratna", "peta"], f"""
        <circle cx="32" cy="30" r="13" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Classic Mysore Peta turban -->
        <path d="M 18 24 C 18 10 46 10 46 24 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="20" y1="20" x2="44" y2="20" stroke="{RED}" stroke-width="2"/>
        <!-- Spectacles -->
        <circle cx="28" cy="28" r="3" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <circle cx="36" cy="28" r="3" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <line x1="31" y1="28" x2="33" y2="28" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 22 43 L 32 40 L 42 43" stroke="{DARK}" stroke-width="2" fill="none"/>
        """),
        ("modern_13_engineers_day_turban", "Engineers Day Compass & Peta", "ಎಂಜಿನಿಯರ್ಸ್ ದಿನಾಚರಣೆ", ["engineersday", "compass", "drafting", "visvesvaraya"], f"""
        <ellipse cx="32" cy="22" rx="14" ry="8" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <line x1="20" y1="22" x2="44" y2="22" stroke="{RED}" stroke-width="2"/>
        <!-- Drafting compass divider -->
        <line x1="32" y1="30" x2="22" y2="52" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <line x1="32" y1="30" x2="42" y2="52" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="32" cy="30" r="2.5" fill="{GOLD}"/>
        """),
        ("modern_14_ksrtc_airavat_club_class", "KSRTC Airavat Club Class Bus", "ಕೆ.ಎಸ್.ಆರ್.ಟಿ.ಸಿ ಐರಾವತ", ["ksrtc", "airavat", "elephant", "coach", "bus"], f"""
        <rect x="10" y="20" width="44" height="24" rx="4" fill="{WHITE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Airavat Elephant logo on bus side -->
        <circle cx="24" cy="32" r="5" fill="{SKY_BLUE}"/>
        <line x1="10" y1="38" x2="54" y2="38" stroke="{RED}" stroke-width="2"/>
        <circle cx="20" cy="44" r="4" fill="{DARK}"/>
        <circle cx="44" cy="44" r="4" fill="{DARK}"/>
        """),
        ("modern_15_kstdc_mayura_tourist_bus", "KSTDC Mayura Tourist Coach", "ಕೆ.ಎಸ್.ಟಿ.ಡಿ.ಸಿ ಮಯೂರ", ["kstdc", "mayura", "tourism", "peacock"], f"""
        <rect x="10" y="20" width="44" height="24" rx="4" fill="{YELLOW}" stroke="{DARK}" stroke-width="2"/>
        <!-- Peacock Mayura emblem on coach -->
        <circle cx="26" cy="32" r="4" fill="{GREEN}"/>
        <line x1="10" y1="28" x2="54" y2="28" stroke="{RED}" stroke-width="2"/>
        <circle cx="20" cy="44" r="4" fill="{DARK}"/>
        <circle cx="44" cy="44" r="4" fill="{DARK}"/>
        """),
        ("modern_16_nandini_milk_pouch", "Nandini Milk Pouch (KMF)", "ನಂದಿನಿ ಹಾಲಿನ ಪ್ಯಾಕೆಟ್", ["nandini", "kmf", "milk", "karnataka"], f"""
        <!-- Blue and white milk packet -->
        <rect x="18" y="16" width="28" height="34" rx="3" fill="{WHITE}" stroke="{ROYAL_BLUE}" stroke-width="2"/>
        <rect x="18" y="26" width="28" height="12" fill="{ROYAL_BLUE}"/>
        <!-- Nandini cow logo silhouette -->
        <ellipse cx="32" cy="32" rx="6" ry="4" fill="{WHITE}"/>
        <circle cx="36" cy="30" r="2" fill="{WHITE}"/>
        """),
        ("modern_17_nandini_ghee_jar", "Nandini Pure Cow Ghee Jar", "ನಂದಿನಿ ಹಸುವಿನ ತುಪ್ಪ", ["nandini", "ghee", "clarifiedbutter", "kmf"], f"""
        <rect x="22" y="24" width="20" height="26" rx="4" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Green lid cap -->
        <rect x="24" y="18" width="16" height="6" rx="2" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="36" r="4" fill="{YELLOW}"/>
        """),
        ("modern_18_dr_rajkumar_silhouette", "Nata Sarvabhouma Dr. Rajkumar", "ಡಾ. ರಾಜ್‌ಕುಮಾರ್", ["rajkumar", "annavru", "kannada", "cinema"], f"""
        <!-- Iconic silhouette with moustache and smile -->
        <circle cx="32" cy="28" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Hairstyle -->
        <path d="M 18 26 C 18 14 46 14 46 26" stroke="{DARK}" stroke-width="4" fill="none"/>
        <!-- Characteristic curved mustache -->
        <path d="M 24 34 Q 32 38 40 34" stroke="{DARK}" stroke-width="2.5" fill="none"/>
        <circle cx="32" cy="22" r="1.5" fill="{RED}"/>
        <circle cx="28" cy="28" r="1.5" fill="{DARK}"/>
        <circle cx="36" cy="28" r="1.5" fill="{DARK}"/>
        """),
        ("modern_19_dr_rajkumar_gandhada_gudi", "Gandhada Gudi Forest Ranger Hat", "ಗಂಧದ ಗುಡಿ ಹ್ಯಾಟ್", ["gandhadagudi", "ranger", "forest", "rajkumar"], f"""
        <!-- Wide-brimmed safari hat -->
        <ellipse cx="32" cy="36" rx="22" ry="6" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <path d="M 22 36 L 24 20 C 24 16 40 16 40 20 L 42 36 Z" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <line x1="23" y1="30" x2="41" y2="30" stroke="{RED}" stroke-width="2"/>
        """),
        ("modern_20_puneeth_rajkumar_appu", "Appu Power Star (Heart of Karnataka)", "ಅಪ್ಪು (ಪುನೀತ್ ರಾಜ್‌ಕುಮಾರ್)", ["puneeth", "appu", "powerstar", "tribute"], f"""
        <!-- Radiant heart with dancing silhouette -->
        <path d="M 32 18 C 26 10 14 12 14 24 C 14 36 32 48 32 48 C 32 48 50 36 50 24 C 50 12 38 10 32 18 Z" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="24" r="3" fill="{YELLOW}"/>
        <path d="M 32 27 L 32 36 M 28 32 L 36 32" stroke="{YELLOW}" stroke-width="1.5"/>
        """),
        ("modern_21_bengaluru_torana_welcome_arch", "Namma Bengaluru City Welcome Arch", "ನಮ್ಮ ಬೆಂಗಳೂರು ಸ್ವಾಗತ ಕಮಾನು", ["welcomearch", "bengaluru", "entrance"], f"""
        <!-- Grand stone archway -->
        <path d="M 12 52 L 12 28 C 12 16 52 16 52 28 L 52 52" stroke="{SLATE}" stroke-width="4" stroke-linecap="round" fill="none"/>
        <path d="M 18 52 L 18 30 C 18 20 46 20 46 30 L 46 52" stroke="{GOLD}" stroke-width="2" stroke-linecap="round" fill="none"/>
        <circle cx="32" cy="14" r="4" fill="{RED}"/>
        """),
        ("modern_22_electronic_city_flyover", "Electronic City Elevated Expressway", "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ ಮೇಲ್ಸೇತುವೆ", ["expressway", "flyover", "electroniccity", "tech"], f"""
        <!-- Elevated pillars and road ribbon -->
        <line x1="22" y1="36" x2="22" y2="54" stroke="{SLATE}" stroke-width="4"/>
        <line x1="42" y1="36" x2="42" y2="54" stroke="{SLATE}" stroke-width="4"/>
        <path d="M 8 36 Q 32 30 56 36" stroke="{DARK}" stroke-width="5" fill="none"/>
        <path d="M 8 36 Q 32 30 56 36" stroke="{YELLOW}" stroke-width="1.5" stroke-dasharray="3 2" fill="none"/>
        """),
        ("modern_23_itpl_tech_park_building", "ITPL Tech Park Glass Towers", "ಐ.ಟಿ.ಪಿ.ಎಲ್ ಟೆಕ್ ಪಾರ್ಕ್", ["itpl", "techpark", "whitefield", "software"], f"""
        <rect x="14" y="22" width="16" height="30" fill="{SKY_BLUE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="34" y="14" width="16" height="38" fill="{ROYAL_BLUE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Window grids -->
        <line x1="18" y1="22" x2="18" y2="52" stroke="{WHITE}" stroke-width="1"/>
        <line x1="26" y1="22" x2="26" y2="52" stroke="{WHITE}" stroke-width="1"/>
        <line x1="38" y1="14" x2="38" y2="52" stroke="{WHITE}" stroke-width="1"/>
        <line x1="46" y1="14" x2="46" y2="52" stroke="{WHITE}" stroke-width="1"/>
        """),
        ("modern_24_chinnaswamy_stadium_floodlights", "Chinnaswamy Cricket Stadium Lights", "ಚಿನ್ನಸ್ವಾಮಿ ಕ್ರೀಡಾಂಗಣ", ["chinnaswamy", "cricket", "stadium", "floodlight"], f"""
        <polygon points="12,52 18,22 22,22 28,52" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Floodlight cluster bank -->
        <rect x="14" y="16" width="22" height="10" rx="2" fill="{DARK}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="18" cy="21" r="2" fill="{YELLOW}"/>
        <circle cx="25" cy="21" r="2" fill="{YELLOW}"/>
        <circle cx="32" cy="21" r="2" fill="{YELLOW}"/>
        <!-- Cricket ball -->
        <circle cx="46" cy="40" r="5" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
        <line x1="43" y1="38" x2="49" y2="42" stroke="{WHITE}" stroke-width="1"/>
        """),
        ("modern_25_rcb_namma_bengaluru_lion", "Royal Challengers Bengaluru Lion", "ಆರ್.ಸಿ.ಬಿ ಲಯನ್ (ಈ ಸಲ ಕಪ್ ನಮ್ದೆ)", ["rcb", "ee_sala_cup_namde", "lion", "bengaluru"], f"""
        <!-- Roaring lion crest in gold & red -->
        <polygon points="32,8 14,20 18,48 32,56 46,48 50,20" fill="{RED}" stroke="{GOLD}" stroke-width="2.5"/>
        <circle cx="32" cy="28" r="8" fill="{GOLD}"/>
        <path d="M 28 34 Q 32 30 36 34" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <polygon points="32,16 28,24 36,24" fill="{GOLD}"/>
        """),
        ("modern_26_bengaluru_fc_west_block_blues", "Bengaluru FC West Block Blues", "ಬೆಂಗಳೂರು ಎಫ್.ಸಿ", ["bengaluru_fc", "football", "westblockblues"], f"""
        <polygon points="32,10 16,18 18,46 32,54 46,46 48,18" fill="{ROYAL_BLUE}" stroke="{WHITE}" stroke-width="2"/>
        <line x1="32" y1="10" x2="32" y2="54" stroke="{WHITE}" stroke-width="1.5"/>
        <!-- Football inside shield -->
        <circle cx="32" cy="32" r="6" fill="{WHITE}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("modern_27_darshini_coffee_token", "Darshini Brass Token", "ದರ್ಶಿನಿ ಹೋಟೆಲ್ ಟೋಕನ್", ["darshini", "token", "tiffin", "brass"], f"""
        <!-- Circular punched metal token -->
        <circle cx="32" cy="32" r="18" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="14" stroke="{DARK_GOLD}" stroke-width="1" stroke-dasharray="2 1" fill="none"/>
        <circle cx="32" cy="32" r="5" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <text x="32" y="35" font-size="8" font-weight="bold" fill="{RED}" text-anchor="middle">ಕ</text>
        """),
        ("modern_28_darshini_stainless_counter", "Darshini Standing Counter", "ದರ್ಶಿನಿ ಸ್ಟ್ಯಾಂಡಿಂಗ್ ಟೇಬಲ್", ["darshini", "table", "standing", "coffee"], f"""
        <!-- Round stainless steel high table with hot coffee cup -->
        <ellipse cx="32" cy="28" rx="20" ry="6" fill="{SILVER}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="32" y1="34" x2="32" y2="54" stroke="{SLATE}" stroke-width="4"/>
        <ellipse cx="32" cy="54" rx="12" ry="4" fill="{SLATE}"/>
        <rect x="28" y="20" width="8" height="8" rx="1" fill="{CREAM}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("modern_29_commercial_street_shopping", "Commercial Street Shopping Bag", "ಕಮರ್ಷಿಯಲ್ ಸ್ಟ್ರೀಟ್ ಶಾಪಿಂಗ್", ["commercialstreet", "shopping", "bengaluru"], f"""
        <rect x="18" y="24" width="28" height="28" rx="3" fill="{RED}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 26 24 C 26 16 38 16 38 24" stroke="{GOLD}" stroke-width="2.5" fill="none"/>
        <!-- Silk ribbons peeking out -->
        <circle cx="32" cy="38" r="4" fill="{YELLOW}"/>
        """),
        ("modern_30_brigade_road_neon_sign", "Brigade Road Neon Sign", "ಬ್ರಿಗೇಡ್ ರೋಡ್ ನಿಯಾನ್ ದೀಪ", ["brigaderoad", "neon", "mgroad", "nightlife"], f"""
        <rect x="12" y="22" width="40" height="20" rx="3" fill="{DARK}" stroke="{RED}" stroke-width="2"/>
        <path d="M 18 32 L 24 32 M 28 32 L 36 32 M 40 32 L 46 32" stroke="{SKY_BLUE}" stroke-width="2"/>
        <circle cx="32" cy="14" r="3" fill="{YELLOW}"/>
        """),
        ("modern_31_kanteerava_studio_camera", "Sandalwood Cinema Film Camera", "ಸ್ಯಾಂಡಲ್‌ವುಡ್ ಸಿನಿಮಾ ಕ್ಯಾಮೆರಾ", ["sandalwood", "kannadacinema", "camera", "film"], f"""
        <!-- Studio movie camera with film magazines -->
        <rect x="16" y="24" width="22" height="18" rx="3" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Double round film reels on top -->
        <circle cx="22" cy="18" r="6" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="18" r="6" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Lens cone projecting forward -->
        <polygon points="38,28 48,22 48,38 38,34" fill="{GOLD}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="27" y1="42" x2="20" y2="56" stroke="{DARK}" stroke-width="2.5"/>
        <line x1="27" y1="42" x2="34" y2="56" stroke="{DARK}" stroke-width="2.5"/>
        """),
        ("modern_32_sandalwood_film_reel", "Sandalwood Cinema Reel", "ಕನ್ನಡ ಚಿತ್ರರಂಗದ ಫಿಲ್ಮ್ ರೀಲ್", ["filmreel", "sandalwood", "cinema"], f"""
        <circle cx="32" cy="32" r="20" fill="{SLATE}" stroke="{DARK}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="6" fill="{DARK}"/>
        <!-- Film spool holes -->
        <circle cx="32" cy="18" r="3.5" fill="{CREAM}"/>
        <circle cx="32" cy="46" r="3.5" fill="{CREAM}"/>
        <circle cx="18" cy="32" r="3.5" fill="{CREAM}"/>
        <circle cx="46" cy="32" r="3.5" fill="{CREAM}"/>
        """),
        ("modern_33_kannada_keyboard_key", "Kannada Keyboard Key 'ಅ'", "ಕನ್ನಡ ಕೀಬೋರ್ಡ್ 'ಅ'", ["keyboard", "typing", "unicode", "script"], f"""
        <rect x="12" y="12" width="40" height="40" rx="6" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <rect x="15" y="15" width="34" height="34" rx="4" fill="{WHITE}"/>
        <!-- Kannada letter 'ಅ' -->
        <text x="32" y="39" font-family="'Noto Sans Kannada', 'Kannada Sangam MN', sans-serif" font-size="22" font-weight="bold" fill="{RED}" text-anchor="middle">ಅ</text>
        """),
        ("modern_34_kannada_wikipedia_w", "Kannada Wikipedia Globe", "ಕನ್ನಡ ವಿಕಿಪೀಡಿಯ", ["wikipedia", "encyclopedia", "knowledge"], f"""
        <circle cx="32" cy="32" r="18" fill="{WHITE}" stroke="{SLATE}" stroke-width="2"/>
        <path d="M 14 32 Q 32 24 50 32 M 14 32 Q 32 40 50 32" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        <line x1="32" y1="14" x2="32" y2="50" stroke="{SLATE}" stroke-width="1.5"/>
        <text x="32" y="37" font-size="14" font-weight="bold" fill="{RED}" text-anchor="middle">ವಿ</text>
        """),
        ("modern_35_kempegowda_airport_terminal", "Kempegowda Int'l Airport (KIA)", "ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ", ["airport", "kia", "terminal", "flight", "bengaluru"], f"""
        <!-- Swooping aerodynamic modern terminal roofline -->
        <path d="M 8 36 C 20 22 44 22 56 36 L 52 46 L 12 46 Z" fill="{SILVER}" stroke="{DARK}" stroke-width="2"/>
        <line x1="16" y1="46" x2="16" y2="34" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="28" y1="46" x2="28" y2="28" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="40" y1="46" x2="40" y2="30" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Airplane taking off overhead -->
        <path d="M 32 14 L 38 18 L 34 20 L 32 18 Z" fill="{ROYAL_BLUE}"/>
        """),
        ("modern_36_kempegowda_tower_watchtower", "Kempegowda Watchtower (Boundary)", "ಕೆಂಪೇಗೌಡರ ಕಾವಲು ಗೋಪುರ", ["kempegowda", "watchtower", "lalbagh", "boundary"], f"""
        <!-- Historic 4-pillar watchtower on rock -->
        <polygon points="12,50 16,34 48,34 52,50" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Canopy pavilion -->
        <rect x="20" y="24" width="24" height="10" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <polygon points="18,24 46,24 32,14" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="12" r="2" fill="{GOLD}"/>
        """),
        ("modern_37_kempegowda_sword", "Kempegowda Founder Sword", "ನಾಡಪ್ರಭು ಕೆಂಪೇಗೌಡರ ಖಡ್ಗ", ["kempegowda", "sword", "founder", "hero"], f"""
        <!-- Broad steel broadsword of Nadaprabhu Kempegowda -->
        <line x1="18" y1="48" x2="46" y2="16" stroke="{SILVER}" stroke-width="3.5" stroke-linecap="round"/>
        <circle cx="16" cy="50" r="3" fill="{GOLD}"/>
        <line x1="20" y1="42" x2="26" y2="48" stroke="{GOLD}" stroke-width="3"/>
        """),
        ("modern_38_mysore_dasara_light_decoration", "Dasara City Lighting Arches", "ದಸರಾ ವಿದ್ಯುತ್ ದೀಪಾಲಂಕಾರ", ["dasara", "illumination", "arch", "lights"], f"""
        <path d="M 12 50 C 12 20 52 20 52 50" stroke="{GOLD}" stroke-width="3" stroke-linecap="round" fill="none"/>
        <circle cx="16" cy="38" r="2" fill="{RED}"/>
        <circle cx="24" cy="24" r="2" fill="{YELLOW}"/>
        <circle cx="32" cy="20" r="2.5" fill="{WHITE}"/>
        <circle cx="40" cy="24" r="2" fill="{GREEN}"/>
        <circle cx="48" cy="38" r="2" fill="{SKY_BLUE}"/>
        """),
        ("modern_39_hubballi_railway_longest_platform", "Hubballi World's Longest Platform", "ಹುಬ್ಬಳ್ಳಿ ರೈಲ್ವೆ ನಿಲ್ದಾಣ", ["hubballi", "railway", "platform", "record"], f"""
        <!-- Endless straight perspective railway tracks -->
        <line x1="28" y1="20" x2="12" y2="52" stroke="{SLATE}" stroke-width="2.5"/>
        <line x1="36" y1="20" x2="52" y2="52" stroke="{SLATE}" stroke-width="2.5"/>
        <!-- Ties -->
        <line x1="24" y1="30" x2="40" y2="30" stroke="{BROWN}" stroke-width="2"/>
        <line x1="20" y1="38" x2="44" y2="38" stroke="{BROWN}" stroke-width="2"/>
        <line x1="16" y1="46" x2="48" y2="46" stroke="{BROWN}" stroke-width="2"/>
        <!-- Signal post -->
        <line x1="46" y1="36" x2="46" y2="16" stroke="{DARK}" stroke-width="2"/>
        <circle cx="46" cy="18" r="3" fill="{GREEN}"/>
        """),
        ("modern_40_mangalore_tile_terracotta", "Mangalore Terracotta Roofing Tile", "ಮಂಗಳೂರು ಹೆಂಚು", ["mangaloretile", "terracotta", "roofing", "heritage"], f"""
        <!-- Interlocking red clay roofing tile with diamond ridges -->
        <polygon points="16,14 48,14 44,50 12,50" fill="{ORANGE}" stroke="{BROWN}" stroke-width="2"/>
        <line x1="30" y1="14" x2="28" y2="50" stroke="{BROWN}" stroke-width="2"/>
        <polygon points="30,26 36,32 30,38 24,32" stroke="{BROWN}" stroke-width="1.5" fill="none"/>
        """),
        ("modern_41_coorg_homestay_cottage", "Coorg Homestay Plantation Cottage", "ಕೊಡಗಿನ ಹೋಮ್‌ಸ್ಟೇ", ["homestay", "coorg", "plantation", "cottage"], f"""
        <polygon points="32,16 12,32 52,32" fill="{RED}" stroke="{BROWN}" stroke-width="2"/>
        <rect x="18" y="32" width="28" height="20" fill="{CREAM}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="28" y="40" width="8" height="12" fill="{BROWN}"/>
        <rect x="38" y="36" width="6" height="6" fill="{SKY_BLUE}" stroke="{DARK}" stroke-width="1"/>
        """),
        ("modern_42_hampi_coracle_boat", "Hampi Coracle Basket Boat (Theppa)", "ಹಂಪಿಯ ಹರಿಗೋಲು (ತೆಪ್ಪ)", ["coracle", "theppa", "boat", "tungabhadra", "hampi"], f"""
        <!-- Round circular basket boat -->
        <ellipse cx="32" cy="34" rx="20" ry="14" fill="{BROWN}" stroke="{DARK}" stroke-width="2.5"/>
        <ellipse cx="32" cy="34" rx="16" ry="10" stroke="{DARK_GOLD}" stroke-width="1.5" stroke-dasharray="3 2" fill="none"/>
        <!-- Single wooden paddle oar -->
        <line x1="18" y1="18" x2="38" y2="44" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        <ellipse cx="18" cy="18" rx="4" ry="2" fill="{DARK_GOLD}"/>
        """),
        ("modern_43_coastal_fishing_boat", "Malpe Mechanized Fishing Trawler", "ಕರಾವಳಿಯ ಮೀನುಗಾರಿಕಾ ದೋಣಿ", ["fishingboat", "trawler", "malpe", "karavali"], f"""
        <!-- Boat hull in sea -->
        <path d="M 12 36 L 48 36 C 54 36 50 46 44 48 L 18 48 C 12 48 8 40 12 36 Z" fill="{ROYAL_BLUE}" stroke="{DARK}" stroke-width="2"/>
        <rect x="20" y="26" width="12" height="10" fill="{WHITE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Mast & flag -->
        <line x1="38" y1="16" x2="38" y2="36" stroke="{DARK}" stroke-width="2"/>
        <polygon points="38,16 44,19 38,22" fill="{RED}"/>
        <path d="M 8 48 Q 32 54 56 48" stroke="{SKY_BLUE}" stroke-width="2" fill="none"/>
        """),
        ("modern_44_karnataka_tourism_one_state_many_worlds", "One State Many Worlds Emblem", "ಒಂದು ರಾಜ್ಯ ಹಲವು ಜಗತ್ತು", ["tourism", "onestatemanyworlds", "karnatakatourism"], f"""
        <!-- Globe with Karnataka flag banner ribbon -->
        <circle cx="32" cy="32" r="18" fill="{SKY_BLUE}" stroke="{GOLD}" stroke-width="2"/>
        <path d="M 12 30 Q 32 20 52 30 L 52 36 Q 32 26 12 36 Z" fill="{YELLOW}"/>
        <path d="M 12 36 Q 32 26 52 36 L 52 42 Q 32 32 12 42 Z" fill="{RED}"/>
        """),
        ("modern_45_cubbon_park_bamboo", "Cubbon Park Green Canopy", "ಕಬ್ಬನ್ ಪಾರ್ಕ್", ["cubbonpark", "garden", "greenlung", "bengaluru"], f"""
        <circle cx="24" cy="28" r="12" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="40" cy="28" r="12" fill="{GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="20" r="10" fill="{LIGHT_GREEN}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Tree trunks -->
        <line x1="24" y1="40" x2="24" y2="52" stroke="{BROWN}" stroke-width="3"/>
        <line x1="40" y1="40" x2="40" y2="52" stroke="{BROWN}" stroke-width="3"/>
        <line x1="12" y1="52" x2="52" y2="52" stroke="{DARK}" stroke-width="2"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in modern_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
