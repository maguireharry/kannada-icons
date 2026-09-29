"""
Category 9: Festivals, Cultural Traditions, Literature & State Identity (50 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "festivals-traditions-literature",
            "tags": ["festival", "culture", "literature", "heritage", "karnataka", "tradition"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Karnataka Flag Bicolor
    add("fest_01_karnataka_flag_bicolor", "Official Karnataka State Flag", "ಕರ್ನಾಟಕ ಧ್ವಜ (ಹಳದಿ-ಕೆಂಪು)", ["flag", "karnataka", "arasina", "kunkuma", "bicolor"], f"""
    <!-- Golden Yellow top band (Arasina / Peace / Harmony) -->
    <rect x="8" y="14" width="48" height="18" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <!-- Deep Red bottom band (Kunkuma / Bravery / Revolution) -->
    <rect x="8" y="32" width="48" height="18" fill="{RED}" stroke="{RED}" stroke-width="1"/>
    <!-- Flag border -->
    <rect x="8" y="14" width="48" height="36" stroke="{DARK}" stroke-width="2" fill="none"/>
    """)

    # 2. Karnataka Flag Billowing on Mast
    add("fest_02_karnataka_flag_waving", "Karnataka Flag Billowing on Mast", "ಹಾರಾಡುತ್ತಿರುವ ಕನ್ನಡ ಬಾವುಟ", ["flag", "mast", "waving", "rajyotsava"], f"""
    <!-- Flagpole mast -->
    <line x1="14" y1="8" x2="14" y2="56" stroke="{SLATE}" stroke-width="3" stroke-linecap="round"/>
    <circle cx="14" cy="8" r="2.5" fill="{GOLD}"/>
    <!-- Waving yellow-red banner -->
    <path d="M 14 12 Q 28 8 38 14 Q 48 20 54 14 L 54 28 Q 48 34 38 28 Q 28 22 14 26 Z" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1"/>
    <path d="M 14 26 Q 28 22 38 28 Q 48 34 54 28 L 54 42 Q 48 48 38 42 Q 28 36 14 40 Z" fill="{RED}" stroke="{DARK}" stroke-width="1"/>
    """)

    # 3. Kannada Rajyotsava Procession Chariot
    add("fest_03_rajyotsava_chariot", "Kannada Rajyotsava Procession", "ಕನ್ನಡ ರಾಜ್ಯೋತ್ಸವ ರಥ", ["rajyotsava", "nov1", "procession", "chariot"], f"""
    <rect x="14" y="24" width="36" height="20" rx="3" fill="{YELLOW}" stroke="{RED}" stroke-width="2"/>
    <!-- Bicolor flag flying on vehicle -->
    <rect x="20" y="14" width="12" height="5" fill="{YELLOW}"/>
    <rect x="20" y="19" width="12" height="5" fill="{RED}"/>
    <line x1="20" y1="12" x2="20" y2="24" stroke="{DARK}" stroke-width="1.5"/>
    <!-- Wheels -->
    <circle cx="22" cy="46" r="6" fill="{DARK}" stroke="{GOLD}" stroke-width="2"/>
    <circle cx="42" cy="46" r="6" fill="{DARK}" stroke="{GOLD}" stroke-width="2"/>
    """)

    # 4. Bhuvaneshwari Devi Bust
    add("fest_04_bhuvaneshwari_devi_bust", "Kannada Thayi Bhuvaneshwari", "ಕನ್ನಡ ತಾಯಿ ಭುವನೇಶ್ವರಿ", ["bhuvaneshwari", "motherkannada", "deity", "crown"], f"""
    <circle cx="32" cy="32" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Radiant Golden Crown (Kireeta) -->
    <polygon points="32,6 20,22 44,22" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <circle cx="32" cy="14" r="2.5" fill="{RED}"/>
    <!-- Bindi & nose stud -->
    <circle cx="32" cy="28" r="2" fill="{RED}"/>
    <circle cx="36" cy="34" r="1" fill="{WHITE}"/>
    <!-- Golden halo behind -->
    <circle cx="32" cy="26" r="22" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="3 2" fill="none"/>
    """)

    # 5. Mysore Dasara Jamboo Savari
    add("fest_05_mysore_dasara_jamboo_savari", "Dasara Golden Howdah (Jamboo Savari)", "ಮೈಸೂರು ದಸರಾ ಜಂಬೂ ಸವಾರಿ", ["jamboosavari", "dasara", "elephant", "howdah", "ambari"], f"""
    <!-- Royal Caparisoned Elephant profile -->
    <ellipse cx="28" cy="38" rx="16" ry="12" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
    <!-- Trunk up in salute -->
    <path d="M 12 36 Q 6 30 10 24" stroke="{SLATE}" stroke-width="3" stroke-linecap="round" fill="none"/>
    <!-- 750kg Golden Howdah (Chinnada Ambari) on back -->
    <rect x="22" y="16" width="16" height="12" rx="2" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <polygon points="30,10 24,16 36,16" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <circle cx="30" cy="8" r="2" fill="{YELLOW}"/>
    <!-- Legs -->
    <line x1="20" y1="48" x2="20" y2="56" stroke="{SLATE}" stroke-width="3"/>
    <line x1="34" y1="48" x2="34" y2="56" stroke="{SLATE}" stroke-width="3"/>
    """)

    # 6. Dasara Ratna Simhasana (Throne)
    add("fest_06_dasara_golden_throne", "Dasara Golden Throne (Ratna Simhasana)", "ದಸರಾ ರತ್ನ ಸಿಂಹಾಸನ", ["simhasana", "throne", "gold", "wodeyar"], f"""
    <!-- Grand golden throne backrest -->
    <path d="M 20 40 L 20 16 C 20 10 44 10 44 16 L 44 40 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <circle cx="32" cy="22" r="5" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <!-- Royal umbrella canopy atop -->
    <path d="M 16 10 C 16 4 48 4 48 10 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <line x1="32" y1="4" x2="32" y2="0" stroke="{GOLD}" stroke-width="2"/>
    <!-- Seat cushion & legs -->
    <rect x="16" y="40" width="32" height="8" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
    <line x1="18" y1="48" x2="16" y2="56" stroke="{GOLD}" stroke-width="3"/>
    <line x1="46" y1="48" x2="48" y2="56" stroke="{GOLD}" stroke-width="3"/>
    """)

    # 7. Mysore Palace Illuminated Night
    add("fest_07_dasara_illuminated_palace_night", "Mysore Palace 100,000 Lights", "ದಸರಾ ದೀಪಾಲಂಕೃತ ಮೈಸೂರು ಅರಮನೆ", ["palace", "illuminated", "lights", "night"], f"""
    <!-- Dark background with glowing palace dome wireframe -->
    <rect x="8" y="10" width="48" height="44" rx="3" fill="{DARK}"/>
    <!-- Central golden illuminated dome -->
    <path d="M 24 32 C 24 20 40 20 40 32" stroke="{YELLOW}" stroke-width="2" fill="none"/>
    <line x1="32" y1="20" x2="32" y2="14" stroke="{YELLOW}" stroke-width="2"/>
    <circle cx="32" cy="14" r="1.5" fill="{RED}"/>
    <!-- Arches glowing -->
    <path d="M 16 44 C 16 38 22 38 22 44 M 26 44 C 26 38 32 38 32 44 M 36 44 C 36 38 42 38 42 44 M 44 44 C 44 38 48 38 48 44" stroke="{YELLOW}" stroke-width="1.5" fill="none"/>
    <line x1="10" y1="44" x2="54" y2="44" stroke="{YELLOW}" stroke-width="2"/>
    """)

    # 8. Kambala Buffalo Race
    add("fest_08_kambala_buffalo_race_jockey", "Kambala Muddy Buffalo Race", "ಕಂಬಳ ಕೋಣಗಳ ಓಟ", ["kambala", "buffalo", "slush", "race", "tulu"], f"""
    <!-- Pair of roaring racing buffaloes side-by-side -->
    <ellipse cx="26" cy="32" rx="12" ry="9" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
    <ellipse cx="40" cy="30" rx="12" ry="9" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Backward sweeping horns -->
    <path d="M 20 25 C 16 20 22 16 26 18 M 34 23 C 30 18 36 14 40 16" stroke="{SLATE}" stroke-width="2.5" fill="none"/>
    <!-- Jockey holding rope behind -->
    <circle cx="48" cy="20" r="3" fill="{CREAM}"/>
    <!-- Splashing muddy water waves -->
    <path d="M 8 46 Q 20 40 32 46 Q 44 40 56 46" stroke="{SKY_BLUE}" stroke-width="3" fill="none"/>
    """)

    # 9. Kambala Jockey Whip (Kolu)
    add("fest_09_kambala_whip_kolu", "Kambala Jockey Whip (Kolu)", "ಕಂಬಳದ ಚಾವಟಿ / ಕೋಲು", ["kambala", "whip", "kolu", "cane"], f"""
    <line x1="16" y1="52" x2="40" y2="22" stroke="{BROWN}" stroke-width="3" stroke-linecap="round"/>
    <!-- Flexible braided whip thong coiled -->
    <path d="M 40 22 C 48 14 54 26 48 34 C 44 40 52 44 56 40" stroke="{RED}" stroke-width="2" fill="none"/>
    <circle cx="16" cy="52" r="2.5" fill="{GOLD}"/>
    """)

    # 10. Ugadi Bevu Bella Bowl
    add("fest_10_ugadi_bevu_bella_bowl", "Ugadi Bevu-Bella (Neem & Jaggery)", "ಯುಗಾದಿ ಬೇವು-ಬೆಲ್ಲ", ["ugadi", "bevu", "bella", "newyear", "life"], f"""
    <!-- Traditional bowl -->
    <path d="M 14 30 C 14 48 50 48 50 30 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
    <ellipse cx="32" cy="30" rx="18" ry="6" fill="{DARK_GOLD}"/>
    <!-- Sweet brown Jaggery cubes -->
    <rect x="22" y="24" width="6" height="6" fill="{BROWN}"/>
    <rect x="36" y="24" width="6" height="6" fill="{BROWN}"/>
    <!-- Bitter green Neem leaves -->
    <ellipse cx="30" cy="22" rx="4" ry="2" transform="rotate(-30 30 22)" fill="{GREEN}"/>
    <ellipse cx="34" cy="22" rx="4" ry="2" transform="rotate(30 34 22)" fill="{GREEN}"/>
    """)

    # 11-50 Festivals, Literature, Traditions batch
    fest_batch = [
        ("fest_11_ugadi_mango_leaf_torana", "Mango Leaf Torana (Door Hanging)", "ಮಾವಿನ ಎಲೆ ತೋರಣ", ["torana", "mango", "marigold", "doorway"], f"""
        <!-- Thread -->
        <line x1="8" y1="18" x2="56" y2="18" stroke="{RED}" stroke-width="2"/>
        <!-- Pointed green mango leaves -->
        <polygon points="16,18 20,38 12,38" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <polygon points="32,18 36,40 28,40" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <polygon points="48,18 52,38 44,38" fill="{GREEN}" stroke="{DARK}" stroke-width="1"/>
        <!-- Bright orange marigold flowers (Chendu Hoovu) -->
        <circle cx="24" cy="22" r="4" fill="{ORANGE}"/>
        <circle cx="40" cy="22" r="4" fill="{ORANGE}"/>
        """),
        ("fest_12_ugadi_panchanga_reading", "Ugadi Panchanga Calendar Scroll", "ಯುಗಾದಿ ಪಂಚಾಂಗ ಶ್ರವಣ", ["panchanga", "calendar", "almanac", "ugadi"], f"""
        <rect x="16" y="14" width="32" height="38" rx="2" fill="{CREAM}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Red sacred swastika / kalasha symbol on top -->
        <circle cx="32" cy="24" r="4" fill="{RED}"/>
        <!-- Sanskrit / Kannada text lines -->
        <line x1="22" y1="34" x2="42" y2="34" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="22" y1="40" x2="42" y2="40" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="22" y1="46" x2="36" y2="46" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("fest_13_karaga_shakthi_otsava", "Bangalore Karaga Shakthiotsava", "ಬೆಂಗಳೂರು ಕರಗ ಶಕ್ತಿ ಉತ್ಸವ", ["karaga", "shakthi", "jasmine", "vahnikula"], f"""
        <!-- Floral pyramid carried by priest -->
        <polygon points="32,8 18,36 46,36" fill="{GOLD}" stroke="{YELLOW}" stroke-width="2"/>
        <!-- Jasmine flower layers -->
        <line x1="22" y1="28" x2="42" y2="28" stroke="{WHITE}" stroke-width="3"/>
        <line x1="26" y1="20" x2="38" y2="20" stroke="{WHITE}" stroke-width="3"/>
        <!-- Face of bearer veiled in flowers -->
        <circle cx="32" cy="44" r="8" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="32" cy="42" r="2" fill="{RED}"/>
        """),
        ("fest_14_basava_jayanthi_bull", "Nandi / Basavanna Sacred Bull", "ಬಸವಣ್ಣ / ನಂದಿ", ["basavanna", "nandi", "bull", "lingayat"], f"""
        <!-- Seated sacred Nandi bull -->
        <ellipse cx="32" cy="38" rx="18" ry="12" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="44" cy="26" r="6" fill="{SLATE}"/>
        <path d="M 44 22 L 42 14 M 48 22 L 50 14" stroke="{DARK}" stroke-width="2.5"/>
        <!-- Prominent dorsal hump -->
        <circle cx="30" cy="26" r="5" fill="{SLATE}"/>
        <!-- Bell garland around neck -->
        <path d="M 38 28 Q 42 36 46 32" stroke="{GOLD}" stroke-width="2" fill="none"/>
        <circle cx="42" cy="34" r="1.5" fill="{RED}"/>
        """),
        ("fest_15_basavanna_kayakave_kailasa", "Kayakave Kailasa (Work is Worship)", "ಕಾಯಕವೇ ಕೈಲಾಸ", ["kayakavekailasa", "basavanna", "work", "philosophy"], f"""
        <!-- Anvil / Plough and rising sun -->
        <rect x="18" y="38" width="28" height="12" rx="2" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <!-- Radiant divine sun rising from work -->
        <circle cx="32" cy="22" r="8" fill="{YELLOW}" stroke="{GOLD}" stroke-width="1.5"/>
        <line x1="32" y1="8" x2="32" y2="12" stroke="{RED}" stroke-width="2"/>
        <line x1="20" y1="16" x2="24" y2="18" stroke="{RED}" stroke-width="2"/>
        <line x1="44" y1="16" x2="40" y2="18" stroke="{RED}" stroke-width="2"/>
        """),
        ("fest_16_ishtalinga_palm", "Ishtalinga Held in Palm", "ಕರಸ್ಥಲದ ಇಷ್ಟಲಿಂಗ", ["ishtalinga", "lingayat", "palm", "shiva"], f"""
        <!-- Open cupped palm -->
        <path d="M 16 46 Q 32 54 48 46 L 46 38 Q 32 44 18 38 Z" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Shiny black Ishtalinga resting in center of palm -->
        <ellipse cx="32" cy="34" rx="8" ry="6" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <circle cx="32" cy="31" r="5" fill="{DARK}"/>
        <!-- Vibhuti stripe on linga -->
        <line x1="28" y1="30" x2="36" y2="30" stroke="{WHITE}" stroke-width="1.5"/>
        """),
        ("fest_17_akramahadevi_vachana", "Akka Mahadevi (Chennamallikarjuna)", "ಅಕ್ಕ ಮಹಾದೇವಿ", ["akkamahadevi", "vachana", "sharanas", "chennamallikarjuna"], f"""
        <!-- Ascetic silhouette with long flowing hair enveloping her -->
        <circle cx="32" cy="18" r="5" fill="{CREAM}"/>
        <path d="M 22 24 C 16 34 16 52 24 54 C 32 56 40 56 44 48 C 48 38 46 26 40 24" fill="{DARK}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Lotus offering in hands -->
        <circle cx="32" cy="36" r="3" fill="{RED}"/>
        """),
        ("fest_18_allama_prabhu_shunya_simhasana", "Allama Prabhu Shunya Simhasana", "ಅಲ್ಲಮ ಪ್ರಭು ಶೂನ್ಯ ಸಿಂಹಾಸನ", ["allamaprabhu", "shunya", "wisdom", "throne"], f"""
        <!-- Sacred empty throne representing transcendental void -->
        <rect x="18" y="28" width="28" height="22" rx="2" fill="none" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="38" r="7" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="2 2" fill="none"/>
        <circle cx="32" cy="38" r="2" fill="{WHITE}"/>
        <!-- Arched halo above -->
        <path d="M 22 28 C 22 18 42 18 42 28" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("fest_19_anubhava_mantapa_pillar", "Anubhava Mantapa Pillar (Basavakalyan)", "ಅನುಭವ ಮಂಟಪ ಸ್ತಂಭ", ["anubhavamantapa", "pillar", "parliament", "sharanas"], f"""
        <!-- Ornate stone pillar of free spiritual democracy -->
        <rect x="26" y="14" width="12" height="36" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <polygon points="22,14 42,14 32,8" fill="{DARK_GOLD}"/>
        <rect x="22" y="50" width="20" height="6" fill="{DARK_GOLD}"/>
        <line x1="26" y1="26" x2="38" y2="26" stroke="{WHITE}" stroke-width="2"/>
        <line x1="26" y1="38" x2="38" y2="38" stroke="{WHITE}" stroke-width="2"/>
        """),
        ("fest_20_kuvempu_poet_profile", "Rashtrakavi Kuvempu (K. V. Puttappa)", "ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು", ["kuvempu", "rashtrakavi", "jnanpith", "kannada"], f"""
        <!-- Characteristic side profile with round spectacles and silver hair -->
        <circle cx="32" cy="30" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Glasses -->
        <circle cx="28" cy="28" r="4" stroke="{DARK}" stroke-width="2" fill="none"/>
        <circle cx="38" cy="28" r="4" stroke="{DARK}" stroke-width="2" fill="none"/>
        <line x1="32" y1="28" x2="34" y2="28" stroke="{DARK}" stroke-width="2"/>
        <!-- White flowing hair -->
        <path d="M 18 30 C 16 18 48 18 46 30" stroke="{SLATE}" stroke-width="3" fill="none"/>
        <!-- Kurta collar -->
        <path d="M 22 44 L 32 40 L 42 44" stroke="{WHITE}" stroke-width="2" fill="none"/>
        """),
        ("fest_21_kuvempu_kavishaila_rock_monument", "Kavishaila Rock Circle (Kuppalli)", "ಕವಿಶೈಲ (ಕುಪ್ಪಳ್ಳಿ)", ["kavishaila", "kuppalli", "monument", "rockcircle"], f"""
        <!-- Megalithic standing stones in circle -->
        <rect x="14" y="24" width="5" height="26" rx="1" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="24" y="18" width="5" height="32" rx="1" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="35" y="18" width="5" height="32" rx="1" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <rect x="45" y="24" width="5" height="26" rx="1" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="10" y1="50" x2="54" y2="50" stroke="{GREEN}" stroke-width="2"/>
        """),
        ("fest_22_da_ra_bendre_shravana_kavi", "Varakavi Da. Ra. Bendre", "ವರಕವಿ ದ.ರಾ. ಬೇಂದ್ರೆ", ["bendre", "varakavi", "jnanpith", "dharwad"], f"""
        <!-- Poet profile with spectacles and forehead tilaka -->
        <circle cx="32" cy="28" r="13" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="30" cy="28" r="3.5" stroke="{DARK}" stroke-width="2" fill="none"/>
        <circle cx="32" cy="20" r="1.5" fill="{RED}"/>
        <path d="M 20 42 Q 32 48 44 42" stroke="{WHITE}" stroke-width="3" fill="none"/>
        """),
        ("fest_23_k_shivarama_karantha_chomana_dudi", "Kota Shivarama Karantha (Yakshagana)", "ಕೋಟ ಶಿವರಾಮ ಕಾರಂತ", ["karantha", "chomanadudi", "yakshagana", "jnanpith"], f"""
        <circle cx="32" cy="24" r="11" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Chomana Dudi drum in hand -->
        <ellipse cx="32" cy="44" rx="14" ry="8" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <line x1="20" y1="44" x2="44" y2="44" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("fest_24_masti_venkatesha_iyengar", "Masti Venkatesha Iyengar", "ಮಾಸ್ತಿ ವೆಂಕಟೇಶ ಅಯ್ಯಂಗಾರ್", ["masti", "shortstory", "jnanpith"], f"""
        <circle cx="32" cy="26" r="12" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Traditional Iyengar Naamam on forehead -->
        <path d="M 30 18 L 30 24 M 34 18 L 34 24" stroke="{WHITE}" stroke-width="2"/>
        <line x1="32" y1="20" x2="32" y2="25" stroke="{RED}" stroke-width="1.5"/>
        <line x1="18" y1="46" x2="46" y2="46" stroke="{WHITE}" stroke-width="3"/>
        """),
        ("fest_25_v_k_gokak_samarasave_jeevana", "V. K. Gokak (Gokak Report)", "ವಿ. ಕೃ. ಗೋಕಾಕ್", ["gokak", "gokakchalavali", "jnanpith"], f"""
        <circle cx="32" cy="26" r="12" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Thick academic glasses and pen -->
        <rect x="25" y="24" width="6" height="5" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <rect x="33" y="24" width="6" height="5" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <line x1="32" y1="40" x2="46" y2="52" stroke="{GOLD}" stroke-width="2.5"/>
        """),
        ("fest_26_u_r_ananthamurthy_samskara", "U. R. Ananthamurthy (Samskara)", "ಯು. ಆರ್. ಅನಂತಮೂರ್ತಿ", ["ananthamurthy", "samskara", "jnanpith"], f"""
        <circle cx="32" cy="26" r="12" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="28" cy="25" r="3.5" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <circle cx="36" cy="25" r="3.5" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <!-- Open book / Samskara quill -->
        <path d="M 20 48 Q 32 44 44 48" stroke="{SLATE}" stroke-width="2" fill="none"/>
        """),
        ("fest_27_girish_karnad_hayavadana_mask", "Girish Karnad (Hayavadana / Tughlaq)", "ಗಿರೀಶ್ ಕಾರ್ನಾಡ್", ["karnad", "theatre", "hayavadana", "tughlaq"], f"""
        <!-- Split theatre comedy/tragedy & horse mask -->
        <circle cx="32" cy="30" r="14" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 32 16 L 32 44" stroke="{DARK}" stroke-width="2"/>
        <!-- Crowned theatre mask -->
        <polygon points="32,8 24,16 40,16" fill="{GOLD}"/>
        """),
        ("fest_28_chandrashekhara_kambara", "Chandrashekhara Kambara", "ಚಂದ್ರಶೇಖರ ಕಂಬಾರ", ["kambara", "jnanpith", "folklore", "helatennakere"], f"""
        <circle cx="32" cy="26" r="12" fill="{CREAM}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="28" cy="25" r="3" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <circle cx="36" cy="25" r="3" stroke="{DARK}" stroke-width="1.5" fill="none"/>
        <!-- Folk crown / turban -->
        <path d="M 20 20 C 20 12 44 12 44 20 Z" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        """),
        ("fest_29_jnanpith_award_statue", "8 Jnanpith Awards (Vagdevi Idol)", "೮ ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ (ವಾಗ್ದೇವಿ)", ["jnanpith", "eight", "vagdevi", "kannada", "literature"], f"""
        <!-- Bronze statue of Saraswati / Vagdevi holding palm leaf scroll -->
        <ellipse cx="32" cy="50" rx="14" ry="4" fill="{DARK_GOLD}"/>
        <path d="M 28 48 L 28 26 L 36 26 L 36 48" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="32" cy="18" r="5" fill="{GOLD}"/>
        <!-- Halo with digit 8 -->
        <circle cx="32" cy="18" r="10" stroke="{RED}" stroke-width="1.5" fill="none"/>
        <text x="32" y="38" font-size="10" font-weight="bold" fill="{RED}" text-anchor="middle">8</text>
        """),
        ("fest_30_pampa_adi_kavi", "Adikavi Pampa (Palm-Leaf Manuscript)", "ಆದಿಕವಿ ಪಂಪ", ["pampa", "adikavi", "talagari", "kannada"], f"""
        <circle cx="26" cy="22" r="5" fill="{CREAM}"/>
        <!-- Palm leaf scroll (Tale Gari) and iron stylus (Ganta) -->
        <rect x="14" y="34" width="36" height="8" rx="2" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="42" y1="20" x2="34" y2="34" stroke="{SLATE}" stroke-width="2.5" stroke-linecap="round"/>
        """),
        ("fest_31_ranna_gada_yuddha", "Kavi Ranna (Gadayuddha Mace)", "ಕವಿ ರನ್ನ (ಗದಾಯುದ್ಧ)", ["ranna", "gadayuddha", "mace", "bhima"], f"""
        <!-- Massive spiked golden battle mace (Gada) -->
        <line x1="20" y1="48" x2="38" y2="20" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <circle cx="42" cy="16" r="8" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="42" cy="16" r="3" fill="{RED}"/>
        <circle cx="18" cy="50" r="3" fill="{GOLD}"/>
        """),
        ("fest_32_kumaravyasa_gadugina_bharata", "Kumaravyasa (Gadag Narayana)", "ಕುಮಾರವ್ಯಾಸ (ಗದಗಿನ ಭಾರತ)", ["kumaravyasa", "gadag", "bharata", "vachana"], f"""
        <circle cx="28" cy="22" r="5" fill="{CREAM}"/>
        <!-- Temple pillar of Gadag Veera Narayana -->
        <rect x="42" y="14" width="8" height="36" fill="{SLATE}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Writing book -->
        <path d="M 16 38 L 26 34 L 36 38 L 26 42 Z" fill="{CREAM}" stroke="{BROWN}" stroke-width="1.5"/>
        """),
        ("fest_33_kavirajamarga_scroll", "Kavirajamarga (850 CE Text)", "ಕವಿರಾಜಮಾರ್ಗ (ಕ್ರಿ.ಶ. ೮೫೦)", ["kavirajamarga", "amoghavarsha", "scroll", "rashtrakuta"], f"""
        <!-- Unrolled royal parchment scroll -->
        <path d="M 14 18 C 14 12 22 12 22 18 L 22 46 C 22 52 14 52 14 46 Z" fill="{GOLD}"/>
        <rect x="18" y="16" width="30" height="32" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 48 18 C 48 12 56 12 56 18 L 56 46 C 56 52 48 52 48 46 Z" fill="{GOLD}"/>
        <!-- Ancient Kannada script lines -->
        <line x1="22" y1="24" x2="44" y2="24" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="22" y1="32" x2="44" y2="32" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="22" y1="40" x2="40" y2="40" stroke="{BROWN}" stroke-width="1.5"/>
        """),
        ("fest_34_halmidi_stone_inscription", "Halmidi Stone Inscription (450 CE)", "ಹಾಲ್ಮಿಡಿ ಶಾಸನ (ಕ್ರಿ.ಶ. ೪೫೦)", ["halmidi", "inscription", "oldest", "stone", "kadamba"], f"""
        <!-- Ancient arched stone slab with Kadamba Kannada engravings -->
        <path d="M 18 52 L 18 20 C 18 10 46 10 46 20 L 46 52 Z" fill="{SLATE}" stroke="{DARK}" stroke-width="2.5"/>
        <!-- Inscription lines -->
        <line x1="22" y1="24" x2="42" y2="24" stroke="{CREAM}" stroke-width="1.5"/>
        <line x1="22" y1="30" x2="42" y2="30" stroke="{CREAM}" stroke-width="1.5"/>
        <line x1="22" y1="36" x2="42" y2="36" stroke="{CREAM}" stroke-width="1.5"/>
        <line x1="22" y1="42" x2="38" y2="42" stroke="{CREAM}" stroke-width="1.5"/>
        """),
        ("fest_35_shravanabelagola_mahamastakabhisheka", "Mahamastakabhisheka Holy Anointment", "ಶ್ರವಣಬೆಳಗೊಳ ಮಹಾಮಸ್ತಕಾಭಿಷೇಕ", ["mahamastakabhisheka", "shravanabelagola", "gommateshwara", "anointment"], f"""
        <!-- Bahubali monolith head anointed with golden turmeric & milk streams -->
        <circle cx="32" cy="30" r="14" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <ellipse cx="32" cy="18" rx="8" ry="4" fill="{DARK}"/>
        <!-- Golden turmeric & milk streams pouring from above -->
        <line x1="26" y1="6" x2="26" y2="48" stroke="{YELLOW}" stroke-width="2"/>
        <line x1="32" y1="4" x2="32" y2="52" stroke="{WHITE}" stroke-width="3"/>
        <line x1="38" y1="6" x2="38" y2="48" stroke="{YELLOW}" stroke-width="2"/>
        <!-- Sacred kalash pots pouring at top -->
        <circle cx="24" cy="8" r="3" fill="{GOLD}"/>
        <circle cx="40" cy="8" r="3" fill="{GOLD}"/>
        """),
        ("fest_36_kalasa_with_coconut", "Sacred Kalasha & Coconut", "ಮಂಗಳ ಕಳಶ", ["kalasa", "pooja", "coconut", "mangoleaves"], f"""
        <!-- Brass pitcher pot -->
        <ellipse cx="32" cy="44" rx="14" ry="10" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Mango leaves radiating -->
        <polygon points="32,34 20,24 28,34" fill="{GREEN}"/>
        <polygon points="32,34 44,24 36,34" fill="{GREEN}"/>
        <polygon points="32,34 32,18 36,32" fill="{GREEN}"/>
        <!-- Brown husked coconut with holy tilaka -->
        <circle cx="32" cy="22" r="7" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="22" r="2" fill="{RED}"/>
        """),
        ("fest_37_arati_thali_brass", "Puja Arati Plate with Camphor Flame", "ಪೂಜಾ ಆರತಿ ತಟ್ಟೆ", ["arati", "thali", "camphor", "flame", "brass"], f"""
        <!-- Circular brass plate -->
        <ellipse cx="32" cy="42" rx="20" ry="8" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Burning Camphor (Karpura) flame in center -->
        <path d="M 32 16 C 26 24 28 34 32 36 C 36 34 38 24 32 16 Z" fill="{YELLOW}" stroke="{RED}" stroke-width="1.5"/>
        <circle cx="32" cy="28" r="2" fill="{RED}"/>
        <!-- Flowers & kumkuma around rim -->
        <circle cx="18" cy="42" r="2.5" fill="{RED}"/>
        <circle cx="46" cy="42" r="2.5" fill="{YELLOW}"/>
        """),
        ("fest_38_rangoli_muggu", "Traditional Dot Rangoli (Muggu)", "ಚಿತ್ತಾರದ ರಂಗೋಲಿ", ["rangoli", "kolam", "muggu", "festive"], f"""
        <!-- Symmetrical 8-point geometric white chalk rangoli -->
        <polygon points="32,12 40,24 52,32 40,40 32,52 24,40 12,32 24,24" stroke="{WHITE}" stroke-width="2" fill="none"/>
        <polygon points="32,20 38,28 44,32 38,36 32,44 26,36 20,32 26,28" fill="{RED}"/>
        <circle cx="32" cy="32" r="3" fill="{YELLOW}"/>
        """),
        ("fest_39_tambula_betel_leaves_supari", "Auspicious Tambula Offering", "ಶುಭ ತಾಂಬೂಲ", ["tambula", "betelleaf", "supari", "dakshina"], f"""
        <!-- 2 Fresh green betel leaves (Vilyada Yele) -->
        <path d="M 24 40 C 14 30 18 18 28 22 C 32 30 28 42 24 40 Z" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 40 40 C 50 30 46 18 36 22 C 32 30 36 42 40 40 Z" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Golden coconut & supari nut in middle -->
        <circle cx="32" cy="34" r="5" fill="{BROWN}"/>
        <circle cx="32" cy="42" r="3" fill="{GOLD}"/>
        """),
        ("fest_40_navaratri_gombe_habba_dolls", "Mysore Gombe Habba (Raja Rani Dolls)", "ಗೊಂಬೆ ಹಬ್ಬ (ರಾಜ-ರಾಣಿ)", ["gombehabba", "mysore", "dolls", "navaratri"], f"""
        <!-- Raja wooden doll -->
        <rect x="18" y="26" width="10" height="22" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="23" cy="20" r="4" fill="{CREAM}"/>
        <polygon points="23,12 19,16 27,16" fill="{GOLD}"/>
        <!-- Rani wooden doll -->
        <rect x="36" y="26" width="10" height="22" rx="2" fill="{YELLOW}" stroke="{RED}" stroke-width="1.5"/>
        <circle cx="41" cy="20" r="4" fill="{CREAM}"/>
        <circle cx="41" cy="14" r="3" fill="{RED}"/>
        """),
        ("fest_41_deepavali_matti_diya", "Deepavali Clay Diya (Agalu Deepa)", "ದೀಪಾವಳಿ ಮಣ್ಣಿನ ಹಣತೆ", ["diya", "deepavali", "clay", "lamp", "light"], f"""
        <!-- Terra cotta clay saucer -->
        <path d="M 16 38 C 16 48 48 48 48 38 Z" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="38" rx="16" ry="5" fill="{DARK_GOLD}"/>
        <!-- Bright glowing flame -->
        <path d="M 32 14 C 26 22 28 32 32 34 C 36 32 38 22 32 14 Z" fill="{YELLOW}" stroke="{RED}" stroke-width="1.5"/>
        <circle cx="32" cy="26" r="2.5" fill="{RED}"/>
        """),
        ("fest_42_sankranti_ellu_bella", "Sankranti Ellu-Bella Festive Mix", "ಸಂಕ್ರಾಂತಿ ಎಳ್ಳು-ಬೆಲ್ಲ", ["sankranti", "ellubella", "sesame", "harvest"], f"""
        <!-- Brass bowl holding sweet sesame-jaggery mixture -->
        <path d="M 14 30 C 14 48 50 48 50 30 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <ellipse cx="32" cy="30" rx="18" ry="6" fill="{DARK_GOLD}"/>
        <!-- White sesame seeds -->
        <circle cx="24" cy="29" r="1" fill="{WHITE}"/>
        <circle cx="28" cy="31" r="1" fill="{WHITE}"/>
        <circle cx="36" cy="30" r="1" fill="{WHITE}"/>
        <circle cx="40" cy="29" r="1" fill="{WHITE}"/>
        <!-- Brown jaggery cubes & roasted gram -->
        <rect x="30" y="26" width="3" height="3" fill="{BROWN}"/>
        <circle cx="34" cy="29" r="1.5" fill="{YELLOW}"/>
        """),
        ("fest_43_sankranti_decorated_cow", "Sankranti Kichhu Haisuvudu", "ಸಂಕ್ರಾಂತಿ ಕಿಚ್ಚು ಹಾಯಿಸುವುದು", ["sankranti", "cow", "horns", "kichhu"], f"""
        <!-- Painted cow horns with balloons/tassels -->
        <ellipse cx="32" cy="36" rx="14" ry="10" fill="{CREAM}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Horns painted red and yellow -->
        <path d="M 24 28 C 18 16 16 8 20 6" stroke="{RED}" stroke-width="3" fill="none"/>
        <path d="M 40 28 C 46 16 48 8 44 6" stroke="{YELLOW}" stroke-width="3" fill="none"/>
        <circle cx="20" cy="6" r="2.5" fill="{GOLD}"/>
        <circle cx="44" cy="6" r="2.5" fill="{GOLD}"/>
        <!-- Fire flames below -->
        <polygon points="26,54 30,46 34,54" fill="{ORANGE}"/>
        <polygon points="32,54 36,44 40,54" fill="{RED}"/>
        """),
        ("fest_44_ganesha_chaturthi_gowri_idol", "Clay Gowri & Ganesha Idols", "ಮಣ್ಣಿನ ಗೌರಿ ಗಣೇಶ", ["ganesha", "gowri", "chaturthi", "clay"], f"""
        <!-- Clay Ganesha with trunk and single tusk -->
        <circle cx="32" cy="28" r="12" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 32 28 C 32 38 38 40 38 34" stroke="{BROWN}" stroke-width="3.5" fill="none"/>
        <!-- Big ears -->
        <path d="M 20 24 C 14 24 16 32 20 32" stroke="{BROWN}" stroke-width="2"/>
        <path d="M 44 24 C 50 24 48 32 44 32" stroke="{BROWN}" stroke-width="2"/>
        <circle cx="32" cy="20" r="1.5" fill="{RED}"/>
        """),
        ("fest_45_nagapanchami_milk_offering", "Nagapanchami Anthill (Hutta)", "ನಾಗರಪಂಚಮಿ ಹುತ್ತ", ["nagapanchami", "hutta", "serpent", "anthill"], f"""
        <!-- Sacred anthill mounds -->
        <path d="M 14 52 C 14 24 30 20 32 16 C 34 20 50 24 50 52 Z" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Hole with milk bowl -->
        <ellipse cx="32" cy="44" rx="6" ry="3" fill="{DARK}"/>
        <ellipse cx="32" cy="48" rx="8" ry="3" fill="{WHITE}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Snake hood carving stone beside -->
        <path d="M 32 28 C 30 24 34 24 32 20" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("fest_46_varamahalakshmi_kalasa", "Varamahalakshmi Decorated Face", "ವರಮಹಾಲಕ್ಷ್ಮಿ ಪೂಜೆ", ["varamahalakshmi", "goddess", "silverface", "puja"], f"""
        <circle cx="32" cy="24" r="10" fill="{SILVER}" stroke="{DARK}" stroke-width="1.5"/>
        <circle cx="32" cy="20" r="2" fill="{RED}"/>
        <!-- Silk saree drape below -->
        <polygon points="32,32 16,52 48,52" fill="{RED}" stroke="{GOLD}" stroke-width="2"/>
        <line x1="16" y1="52" x2="48" y2="52" stroke="{GOLD}" stroke-width="3"/>
        <circle cx="32" cy="40" r="3" fill="{GOLD}"/>
        """),
        ("fest_47_ayudha_puja_vehicle_lemon", "Ayudha Puja Vehicle with Lemon", "ಆಯುಧ ಪೂಜೆ ನಿಂಬೆಹಣ್ಣು", ["ayudhapuja", "vehicle", "lemon", "protection"], f"""
        <!-- Vehicle wheel -->
        <circle cx="32" cy="30" r="18" fill="{SLATE}" stroke="{DARK}" stroke-width="3"/>
        <circle cx="32" cy="30" r="8" fill="{DARK}"/>
        <!-- Sandalwood & kumkuma marks on wheel -->
        <circle cx="32" cy="18" r="2" fill="{RED}"/>
        <circle cx="32" cy="42" r="2" fill="{RED}"/>
        <!-- Crushed yellow lemon beneath wheel -->
        <ellipse cx="32" cy="50" rx="6" ry="3" fill="{YELLOW}" stroke="{GREEN}" stroke-width="1"/>
        """),
        ("fest_48_banna_leaves_vijayadashami", "Banna (Shami) Gold Leaves", "ಬನ್ನಿ ಮರದ ಬಂಗಾರದ ಎಲೆ", ["banni", "shami", "gold", "vijayadashami"], f"""
        <!-- Sprig of delicate sacred Shami leaves gifted as gold -->
        <line x1="18" y1="46" x2="46" y2="18" stroke="{BROWN}" stroke-width="2.5"/>
        <ellipse cx="26" cy="26" rx="4" ry="2" transform="rotate(-40 26 26)" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <ellipse cx="38" cy="30" rx="4" ry="2" transform="rotate(40 38 30)" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <ellipse cx="36" cy="18" rx="4" ry="2" transform="rotate(-30 36 18)" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        <ellipse cx="46" cy="20" rx="4" ry="2" transform="rotate(30 46 20)" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1"/>
        """),
        ("fest_49_kannada_sahitya_sammelana_torch", "Sahitya Sammelana Torch (Jyothi)", "ಸಾಹಿತ್ಯ ಸಮ್ಮೇಳನದ ಜ್ಯೋತಿ", ["sammelana", "jyothi", "torch", "sahitya"], f"""
        <!-- Torch staff -->
        <line x1="32" y1="56" x2="32" y2="28" stroke="{GOLD}" stroke-width="4" stroke-linecap="round"/>
        <rect x="24" y="24" width="16" height="6" rx="2" fill="{RED}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Vibrant flame in Kannada yellow and red -->
        <path d="M 32 8 C 24 16 26 24 32 24 C 38 24 40 16 32 8 Z" fill="{YELLOW}" stroke="{RED}" stroke-width="2"/>
        <circle cx="32" cy="18" r="3" fill="{RED}"/>
        """),
        ("fest_50_kannada_shasana_lipi", "Halegannada Brahmi Script Glyph", "ಹಳಗನ್ನಡ ಬ್ರಾಹ್ಮೀ ಲಿಪಿ", ["halegannada", "brahmi", "ancient", "script"], f"""
        <!-- Ancient stone tablet with Kadamba script character -->
        <rect x="14" y="14" width="36" height="36" rx="4" fill="{SLATE}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="32" cy="28" r="8" stroke="{GOLD}" stroke-width="3" fill="none"/>
        <line x1="32" y1="20" x2="32" y2="44" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in fest_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
