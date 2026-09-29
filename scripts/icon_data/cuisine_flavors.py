"""
Category 8: Culinary Traditions, Dishes, Sweets & Flavors of Karnataka (50 icons)
"""
from .common import *

def get_icons():
    icons = []

    def add(icon_id, name, kn_name, tags, inner_svg):
        icons.append({
            "id": icon_id,
            "name": name,
            "kannada_name": kn_name,
            "category": "cuisine-flavors",
            "tags": ["food", "cuisine", "karnataka", "sweet", "breakfast", "flavor"] + tags,
            "svg": wrap_svg(inner_svg)
        })

    # 1. Mysore Pak Square
    add("food_01_mysore_pak_square", "Mysore Pak (Single Block)", "ಮೈಸೂರು ಪಾಕ್", ["mysorepak", "sweet", "ghee", "besan"], f"""
    <!-- 3D perspective of rich porous ghee sweet block -->
    <polygon points="20,24 44,24 50,34 26,34" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <polygon points="20,24 26,34 26,50 20,40" fill="{DARK_GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
    <polygon points="26,34 50,34 50,50 26,50" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Porous texture dots in center -->
    <circle cx="34" cy="40" r="1.5" fill="{BROWN}"/>
    <circle cx="42" cy="42" r="1.5" fill="{BROWN}"/>
    <circle cx="38" cy="46" r="1.5" fill="{BROWN}"/>
    """)

    # 2. Mysore Pak Stack
    add("food_02_mysore_pak_stack", "Stack of Mysore Pak Sweets", "ಮೈಸೂರು ಪಾಕ್ ತುಂಡುಗಳು", ["mysorepak", "stack", "sweet"], f"""
    <!-- Bottom block -->
    <rect x="16" y="38" width="32" height="12" rx="2" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Middle block -->
    <rect x="20" y="26" width="28" height="12" rx="2" fill="{YELLOW}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Top block -->
    <rect x="24" y="14" width="24" height="12" rx="2" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <line x1="16" y1="44" x2="48" y2="44" stroke="{BROWN}" stroke-width="1"/>
    """)

    # 3. Dharwad Peda Sugar Crust
    add("food_03_dharwad_peda_sugar_crust", "Dharwad Peda (Line Peda)", "ಧಾರವಾಡ ಪೇಡ", ["dharwadpeda", "peda", "mishra", "dharwad"], f"""
    <!-- Cylindrical dark brown mawa peda dusted in white sugar crystals -->
    <rect x="14" y="24" width="36" height="18" rx="7" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
    <!-- Sugar crystals dusting -->
    <circle cx="20" cy="30" r="1" fill="{WHITE}"/>
    <circle cx="28" cy="34" r="1" fill="{WHITE}"/>
    <circle cx="36" cy="28" r="1" fill="{WHITE}"/>
    <circle cx="44" cy="33" r="1" fill="{WHITE}"/>
    <circle cx="24" cy="36" r="1" fill="{WHITE}"/>
    <circle cx="40" cy="36" r="1" fill="{WHITE}"/>
    """)

    # 4. Dharwad Peda Pair
    add("food_04_dharwad_peda_pair", "Pair of Dharwad Pedas", "ಧಾರವಾಡ ಪೇಡ ಜೋಡಿ", ["dharwad", "peda", "sweet"], f"""
    <ellipse cx="26" cy="30" rx="14" ry="8" transform="rotate(-15 26 30)" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
    <ellipse cx="38" cy="36" rx="14" ry="8" transform="rotate(10 38 36)" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
    <circle cx="24" cy="30" r="1" fill="{WHITE}"/>
    <circle cx="40" cy="36" r="1" fill="{WHITE}"/>
    """)

    # 5. Davangere Benne Dosa
    add("food_05_benne_dosa_davangere", "Davangere Benne Dosa with Butter", "ದಾವಣಗೆರೆ ಬೆಣ್ಣೆ ದೋಸೆ", ["bennedosa", "davangere", "butter", "crispy"], f"""
    <!-- Golden brown circular dosa with porous texture -->
    <circle cx="32" cy="34" r="20" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
    <circle cx="32" cy="34" r="16" fill="{YELLOW}"/>
    <!-- Dollop of fresh white melting butter on top -->
    <ellipse cx="32" cy="30" rx="7" ry="5" fill="{WHITE}" stroke="{CREAM}" stroke-width="1.5"/>
    <!-- Melting butter trickle -->
    <path d="M 32 35 Q 34 40 33 44" stroke="{WHITE}" stroke-width="2" fill="none"/>
    """)

    # 6. Mysore Masala Dosa
    add("food_06_masala_dosa_triangle", "Mysore Masala Dosa (Triangle Fold)", "ಮೈಸೂರು ಮಸಾಲ ದೋಸೆ", ["masaladosa", "mysore", "crispy", "redchutney"], f"""
    <!-- Crispy golden folded triangular dosa -->
    <polygon points="32,12 10,48 54,48" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
    <!-- Red chutney visible inside fold -->
    <path d="M 24 38 L 32 24 L 40 38 Z" fill="{RED}" stroke="{ORANGE}" stroke-width="1"/>
    <!-- Potato palya yellow peeking -->
    <circle cx="32" cy="34" r="3" fill="{YELLOW}"/>
    """)

    # 7. Set Dosa Stack
    add("food_07_set_dosa_stack", "Set Dosa Stack (Spongy)", "ಸೆಟ್ ದೋಸೆ", ["setdosa", "sponge", "breakfast"], f"""
    <!-- 3 Spongy soft circular dosas overlapping -->
    <ellipse cx="32" cy="44" rx="20" ry="7" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <ellipse cx="32" cy="34" rx="20" ry="7" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <ellipse cx="32" cy="24" rx="20" ry="7" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
    <!-- Golden roast spots -->
    <circle cx="26" cy="24" r="1" fill="{GOLD}"/>
    <circle cx="34" cy="23" r="1.5" fill="{GOLD}"/>
    <circle cx="40" cy="25" r="1" fill="{GOLD}"/>
    """)

    # 8. Neer Dosa Roll
    add("food_08_neer_dosa_roll", "Mangalore Neer Dosa Rolls", "ಮಂಗಳೂರು ನೀರ್ ದೋಸೆ", ["neerdosa", "mangalore", "rice", "lacy"], f"""
    <!-- Lacy paper-thin soft white folded triangular crepes -->
    <polygon points="18,22 36,22 27,42" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
    <polygon points="28,26 46,26 37,46" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Lacy pore dots -->
    <circle cx="28" cy="28" r="0.8" fill="{SLATE}"/>
    <circle cx="34" cy="32" r="0.8" fill="{SLATE}"/>
    """)

    # 9. Thatte Idli (Bidadi)
    add("food_09_thatte_idli_bidadi", "Bidadi Thatte Idli (Plate Idli)", "ಬಿದದಿ ತಟ್ಟೆ ಇಡ್ಲಿ", ["thatteidli", "bidadi", "idli", "plate"], f"""
    <!-- Giant broad plate-shaped steamed idli -->
    <ellipse cx="32" cy="34" rx="22" ry="14" fill="{WHITE}" stroke="{SLATE}" stroke-width="2"/>
    <!-- Red button dollop of podi & ghee in the center -->
    <circle cx="32" cy="34" r="5" fill="{RED}" stroke="{GOLD}" stroke-width="1"/>
    <circle cx="32" cy="34" r="2" fill="{YELLOW}"/>
    """)

    # 10. Idli Vada Sambar Combo
    add("food_10_idli_vada_sambar_combo", "Idli Vada Sambar Combo", "ಇಡ್ಲಿ ವಡೆ ಸಾಂಬಾರ್", ["idli", "vada", "sambar", "combo"], f"""
    <!-- Steamed white idli -->
    <circle cx="22" cy="28" r="10" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
    <!-- Golden crispy medu vada with center hole -->
    <circle cx="40" cy="38" r="11" fill="{GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
    <circle cx="40" cy="38" r="3.5" fill="{DARK}"/>
    <!-- Hot bowl of Sambar -->
    <ellipse cx="24" cy="46" rx="10" ry="6" fill="{ORANGE}" stroke="{DARK}" stroke-width="1.5"/>
    """)

    # 11-50 Cuisine & Flavors batch
    food_batch = [
        ("food_11_medu_vada_crispy", "Crispy Medu Vada", "ಉದ್ದಿನ ವಡೆ", ["vada", "meduvada", "crispy"], f"""
        <circle cx="32" cy="32" r="18" fill="{GOLD}" stroke="{BROWN}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="6" fill="{DARK}"/>
        <!-- Peppercorns and curry leaves embedded -->
        <circle cx="26" cy="24" r="1.5" fill="{DARK}"/>
        <circle cx="40" cy="28" r="1.5" fill="{DARK}"/>
        <circle cx="30" cy="42" r="1.5" fill="{GREEN}"/>
        """),
        ("food_12_maddur_vada_onion", "Maddur Vada (Onion Crispy)", "ಮದ್ದೂರು ವಡೆ", ["maddurvada", "onion", "maddur", "snack"], f"""
        <!-- Flat uneven circular disc with charred onion bits -->
        <circle cx="32" cy="32" r="18" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <line x1="22" y1="28" x2="28" y2="28" stroke="{RED}" stroke-width="2"/>
        <line x1="36" y1="36" x2="42" y2="34" stroke="{RED}" stroke-width="2"/>
        <line x1="26" y1="38" x2="30" y2="42" stroke="{GREEN}" stroke-width="2"/>
        """),
        ("food_13_bisi_bele_bath_bowl", "Bisi Bele Bath with Boondi", "ಬಿಸಿಬೇಳೆ ಬಾತ್", ["bisibelebath", "spicy", "rice", "karnataka"], f"""
        <!-- Traditional bowl with aromatic spicy lentil rice -->
        <path d="M 12 30 C 12 48 52 48 52 30 Z" fill="{ORANGE}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="30" rx="20" ry="7" fill="{RED}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Boondi pearls & cashews floating on top -->
        <circle cx="26" cy="29" r="2" fill="{YELLOW}"/>
        <circle cx="32" cy="31" r="2" fill="{YELLOW}"/>
        <circle cx="38" cy="28" r="2" fill="{YELLOW}"/>
        <!-- Steam plumes rising -->
        <path d="M 24 22 Q 26 14 24 8" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        <path d="M 32 20 Q 34 12 32 6" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        <path d="M 40 22 Q 42 14 40 8" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        """),
        ("food_14_vangi_bath_eggplant_rice", "Vangi Bath (Brinjal Rice)", "ವಾಂಗಿ ಬಾತ್", ["vangibath", "eggplant", "brinjal", "spicedrice"], f"""
        <path d="M 14 32 C 14 48 50 48 50 32 Z" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="32" rx="18" ry="6" fill="{GOLD}"/>
        <!-- Purple brinjal slice on top -->
        <ellipse cx="32" cy="30" rx="7" ry="3" fill="{PURPLE}"/>
        <circle cx="24" cy="32" r="1.5" fill="{GREEN}"/>
        <circle cx="40" cy="32" r="1.5" fill="{GREEN}"/>
        """),
        ("food_15_chitranna_lemon_rice", "Nimbehannu Chitranna (Lemon Rice)", "ನಿಂಬೆಹಣ್ಣಿನ ಚಿತ್ರಾನ್ನ", ["chitranna", "lemonrice", "turmeric"], f"""
        <path d="M 14 32 C 14 48 50 48 50 32 Z" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <!-- Bright turmeric yellow rice -->
        <ellipse cx="32" cy="32" rx="18" ry="6" fill="{YELLOW}"/>
        <!-- Peanuts and mustard seeds -->
        <ellipse cx="26" cy="31" rx="2" ry="1.5" fill="{BROWN}"/>
        <ellipse cx="38" cy="33" rx="2" ry="1.5" fill="{BROWN}"/>
        <circle cx="32" cy="30" r="1" fill="{GREEN}"/>
        <!-- Lemon wedge on rim -->
        <path d="M 46 26 C 50 20 44 18 42 24 Z" fill="{YELLOW}" stroke="{GREEN}" stroke-width="1"/>
        """),
        ("food_16_puliyogare_temple_prasada", "Melukote Puliyogare (Tamarind Rice)", "ಮಂಡ್ಯ ಮೇಲುಕೋಟೆ ಪುಳಿಯೋಗರೆ", ["puliyogare", "melukote", "tamarind", "prasada"], f"""
        <path d="M 14 32 C 14 48 50 48 50 32 Z" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <!-- Dark spicy tamarind rice -->
        <ellipse cx="32" cy="32" rx="18" ry="6" fill="{BROWN}"/>
        <!-- Roasted peanuts and curry leaves -->
        <ellipse cx="28" cy="31" rx="2.5" ry="1.5" fill="{GOLD}"/>
        <ellipse cx="36" cy="33" rx="2.5" ry="1.5" fill="{GOLD}"/>
        <circle cx="32" cy="30" r="1" fill="{DARK}"/>
        """),
        ("food_17_curd_rice_mosaranna", "Mosaranna (Curd Rice)", "ಮೊಸರನ್ನ", ["mosaranna", "curdrice", "comfortfood"], f"""
        <path d="M 14 32 C 14 48 50 48 50 32 Z" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="32" rx="18" ry="6" fill="{WHITE}"/>
        <!-- Pomegranate ruby seeds on top -->
        <circle cx="28" cy="31" r="1.5" fill="{RED}"/>
        <circle cx="34" cy="30" r="1.5" fill="{RED}"/>
        <circle cx="37" cy="33" r="1.5" fill="{RED}"/>
        <!-- Mustard tempering -->
        <circle cx="30" cy="33" r="0.8" fill="{DARK}"/>
        """),
        ("food_18_ragi_mudde_steamed_ball", "Ragi Mudde (Millet Ball)", "ರಾಗಿ ಮುದ್ದೆ", ["ragimudde", "millet", "healthy", "karnataka"], f"""
        <!-- Glossy steamed deep purple-brown ragi ball -->
        <circle cx="32" cy="34" r="18" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Glossy highlight reflection -->
        <path d="M 24 24 Q 30 20 38 24" stroke="{CREAM}" stroke-width="2" stroke-linecap="round" fill="none"/>
        """),
        ("food_19_ragi_mudde_soppina_saaru", "Ragi Mudde with Bassaru / Saaru", "ರಾಗಿ ಮುದ್ದೆ ಮತ್ತು ಸೊಪ್ಪಿನ ಸಾರು", ["ragimudde", "bassaru", "village"], f"""
        <!-- Plate -->
        <ellipse cx="32" cy="46" rx="22" ry="7" fill="{SLATE}"/>
        <!-- Ragi Mudde on plate -->
        <circle cx="24" cy="34" r="12" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <!-- Bowl of green leaf saaru -->
        <ellipse cx="42" cy="34" rx="8" ry="5" fill="{GREEN}" stroke="{DARK}" stroke-width="1.5"/>
        """),
        ("food_20_jolada_rotti_north_karnataka", "Jolada Rotti (North Karnataka)", "ಉತ್ತರ ಕರ್ನಾಟಕದ ಜೋಳದ ರೊಟ್ಟಿ", ["joladarotti", "jowar", "northkarnataka"], f"""
        <!-- Large thin unleavened jowar flatbread with roasted speckles -->
        <ellipse cx="32" cy="34" rx="20" ry="14" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Roasted brown blisters -->
        <circle cx="24" cy="32" r="1.5" fill="{BROWN}"/>
        <circle cx="34" cy="28" r="2" fill="{BROWN}"/>
        <circle cx="40" cy="36" r="1.5" fill="{BROWN}"/>
        <circle cx="28" cy="40" r="1.5" fill="{BROWN}"/>
        """),
        ("food_21_badanekayi_yennegai", "Badanekayi Yennegai (Stuffed Brinjal)", "ಬದನೆಕಾಯಿ ಎಣ್ಣೆಗಾಯಿ", ["yennegai", "brinjal", "curry"], f"""
        <circle cx="32" cy="36" r="14" fill="{PURPLE}" stroke="{DARK}" stroke-width="2"/>
        <line x1="32" y1="22" x2="32" y2="50" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="18" y1="36" x2="46" y2="36" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Spicy gravy bath -->
        <ellipse cx="32" cy="48" rx="18" ry="5" fill="{RED}"/>
        """),
        ("food_22_shenga_chutney_pudi", "Shenga Chutney Pudi (Peanut Powder)", "ಶೇಂಗಾ ಚಟ್ನಿ ಪುಡಿ", ["shenga", "chutneypudi", "peanut"], f"""
        <!-- Conical mound of red-brown spiced peanut chutney powder -->
        <polygon points="32,18 16,48 48,48" fill="{RED}" stroke="{BROWN}" stroke-width="2"/>
        <circle cx="32" cy="28" r="1.5" fill="{GOLD}"/>
        <circle cx="26" cy="40" r="1.5" fill="{GOLD}"/>
        <circle cx="38" cy="40" r="1.5" fill="{GOLD}"/>
        <ellipse cx="32" cy="48" rx="16" ry="4" fill="{BROWN}"/>
        """),
        ("food_23_akki_rotti_griddled", "Akki Rotti with Dill & Chillies", "ಅಕ್ಕಿ ರೊಟ್ಟಿ", ["akkirotti", "ricebread", "dill", "breakfast"], f"""
        <circle cx="32" cy="32" r="19" fill="{CREAM}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Finger holes pressed in dough -->
        <circle cx="32" cy="32" r="2" fill="{BROWN}"/>
        <circle cx="24" cy="26" r="2" fill="{BROWN}"/>
        <circle cx="40" cy="26" r="2" fill="{BROWN}"/>
        <circle cx="26" cy="40" r="2" fill="{BROWN}"/>
        <circle cx="38" cy="40" r="2" fill="{BROWN}"/>
        <!-- Green chilli and dill flecks -->
        <circle cx="28" cy="32" r="1" fill="{GREEN}"/>
        <circle cx="36" cy="34" r="1" fill="{GREEN}"/>
        """),
        ("food_24_ragi_rotti", "Ragi Rotti Flatbread", "ರಾಗಿ ರೊಟ್ಟಿ", ["ragirotti", "milletbread", "onion"], f"""
        <circle cx="32" cy="32" r="19" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="32" cy="32" r="2" fill="{DARK}"/>
        <circle cx="24" cy="30" r="1.5" fill="{WHITE}"/>
        <circle cx="38" cy="36" r="1.5" fill="{WHITE}"/>
        <circle cx="30" cy="22" r="1.5" fill="{GREEN}"/>
        """),
        ("food_25_filter_coffee_davarah_tumbler", "Filter Coffee Davarah & Tumbler", "ಫಿಲ್ಟರ್ ಕಾಫಿ ಡಬರಾ-ಲೋಟ", ["filtercoffee", "davarah", "tumbler", "brass"], f"""
        <!-- Brass Davarah wide saucer -->
        <ellipse cx="32" cy="48" rx="20" ry="6" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Brass Tumbler cup -->
        <polygon points="22,46 24,18 40,18 42,46" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Frothy creamy coffee head pouring -->
        <ellipse cx="32" cy="18" rx="8" ry="3" fill="{CREAM}" stroke="{BROWN}" stroke-width="1.5"/>
        <circle cx="30" cy="18" r="1" fill="{BROWN}"/>
        <circle cx="34" cy="18" r="1" fill="{BROWN}"/>
        <!-- Steam plumes -->
        <path d="M 32 14 Q 34 8 32 4" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        """),
        ("food_26_filter_coffee_maker", "Brass Coffee Filter (Percolator)", "ಹಿತ್ತಾಳೆ ಕಾಫಿ ಫಿಲ್ಟರ್", ["coffeefilter", "brass", "chicory"], f"""
        <!-- Top cylinder -->
        <rect x="22" y="10" width="20" height="18" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <!-- Bottom receiving container -->
        <rect x="20" y="28" width="24" height="22" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <line x1="20" y1="28" x2="44" y2="28" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Lid knob -->
        <circle cx="32" cy="7" r="2" fill="{RED}"/>
        """),
        ("food_27_mangalore_buns_banana_puri", "Mangalore Buns (Sweet Banana)", "ಮಂಗಳೂರು ಬನ್ಸ್", ["mangalorebuns", "banana", "sweetpuri"], f"""
        <!-- Puffy golden fried round bun -->
        <circle cx="32" cy="34" r="18" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Fluffy swelling contour -->
        <path d="M 20 28 Q 32 20 44 28" stroke="{YELLOW}" stroke-width="3" fill="none"/>
        <ellipse cx="32" cy="34" rx="8" ry="4" fill="{YELLOW}"/>
        """),
        ("food_28_goli_baje_fritters", "Mangalore Goli Baje Fritters", "ಗೋಳಿ ಬಜೆ", ["golibaje", "fritters", "mangalore"], f"""
        <!-- 3 round golden fried fritters -->
        <circle cx="24" cy="36" r="9" fill="{GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <circle cx="40" cy="36" r="9" fill="{GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <circle cx="32" cy="24" r="9" fill="{GOLD}" stroke="{BROWN}" stroke-width="1.5"/>
        <circle cx="32" cy="24" r="1.5" fill="{GREEN}"/>
        """),
        ("food_29_kori_rotti_chicken", "Kori Rotti & Gassi", "ಕೋರಿ ರೊಟ್ಟಿ", ["korirotti", "tulu", "mangalore", "chicken"], f"""
        <!-- Crisp dry rice cracker sheets -->
        <polygon points="16,36 30,22 44,36 30,50" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        <!-- Spicy red gravy dripping -->
        <path d="M 22 28 Q 32 36 40 28" stroke="{RED}" stroke-width="3" fill="none"/>
        <circle cx="32" cy="36" r="3" fill="{RED}"/>
        """),
        ("food_30_kundapura_chicken_roast", "Kundapura Ghee Roast", "ಕುಂದಾಪುರ ಘೀ ರೋಸ್ಟ್", ["gheeroast", "kundapura", "byadgi"], f"""
        <path d="M 12 30 C 12 48 52 48 52 30 Z" fill="{DARK}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Fiery crimson red ghee roasted meat -->
        <circle cx="26" cy="34" r="6" fill="{RED}"/>
        <circle cx="38" cy="34" r="6" fill="{RED}"/>
        <circle cx="32" cy="28" r="5" fill="{RED}"/>
        <circle cx="32" cy="34" r="2" fill="{GOLD}"/>
        """),
        ("food_31_pandi_curry_coorg_claypot", "Coorg Pandi Curry in Claypot", "ಕೊಡಗಿನ ಪಾಂಡಿ ಕರಿ", ["pandicurry", "coorg", "kachampuli", "claypot"], f"""
        <!-- Earthen black clay pot -->
        <ellipse cx="32" cy="26" rx="14" ry="4" fill="{BROWN}" stroke="{DARK}" stroke-width="1.5"/>
        <path d="M 18 26 C 14 44 50 44 46 26 Z" fill="{DARK}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Deep rich dark curry -->
        <ellipse cx="32" cy="26" rx="12" ry="3" fill="{DARK}"/>
        <!-- Green chilli on rim -->
        <path d="M 28 22 Q 34 18 36 24" stroke="{GREEN}" stroke-width="2" fill="none"/>
        """),
        ("food_32_kadambuttu_rice_balls", "Coorg Kadambuttu (Rice Dumplings)", "ಕದಂಬುಟ್ಟು (ಉಂಡೆ)", ["kadambuttu", "coorg", "dumpling", "steamed"], f"""
        <!-- 3 round steamed white rice dumplings -->
        <circle cx="24" cy="36" r="9" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="40" cy="36" r="9" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        <circle cx="32" cy="24" r="9" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        """),
        ("food_33_noolputtu_string_hoppers", "Coorg Noolputtu (String Hoppers)", "ನೂಲ್ಪುಟ್ಟು", ["noolputtu", "idiyappam", "coorg"], f"""
        <!-- Swirling nest of steamed rice string noodles -->
        <circle cx="32" cy="34" r="18" fill="{WHITE}" stroke="{SLATE}" stroke-width="1.5"/>
        <path d="M 20 28 Q 32 40 44 28 M 22 36 Q 32 24 42 36 M 26 42 Q 32 30 38 42" stroke="{SLATE}" stroke-width="1.5" fill="none"/>
        """),
        ("food_34_bella_pyasa_payasa", "Gasagase Payasa Sweet Pudding", "ಗಸಗಸೆ ಪಾಯಸ", ["payasa", "gasagase", "kheer", "sweet"], f"""
        <!-- Silver bowl -->
        <path d="M 14 28 C 14 46 50 46 50 28 Z" fill="{SILVER}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="28" rx="18" ry="6" fill="{CREAM}"/>
        <!-- Cashews & golden raisins -->
        <ellipse cx="26" cy="28" rx="2.5" ry="1.5" fill="{GOLD}"/>
        <circle cx="36" cy="28" r="2" fill="{BROWN}"/>
        """),
        ("food_35_obbattu_holige", "Holige / Obbattu (Sweet Flatbread)", "ಹೋಳಿಗೆ (ಒಬ್ಬಟ್ಟು)", ["holige", "obbattu", "sweet", "festival"], f"""
        <!-- Thin golden flatbread brushed with ghee -->
        <ellipse cx="32" cy="34" rx="20" ry="14" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <circle cx="32" cy="34" r="4" fill="{YELLOW}"/>
        <line x1="22" y1="30" x2="28" y2="30" stroke="{BROWN}" stroke-width="1.5"/>
        <line x1="36" y1="38" x2="42" y2="38" stroke="{BROWN}" stroke-width="1.5"/>
        """),
        ("food_36_chiroti_with_badam_milk", "Crisp Puffed Chiroti Sweet", "ಚಿರೋಟಿ", ["chiroti", "badammilk", "wedding", "sweet"], f"""
        <!-- Layered concentric puffed pastry discs -->
        <circle cx="32" cy="34" r="18" fill="{CREAM}" stroke="{GOLD}" stroke-width="2"/>
        <circle cx="32" cy="34" r="12" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.5"/>
        <circle cx="32" cy="34" r="6" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Powdered sugar dust -->
        <circle cx="32" cy="34" r="1.5" fill="{WHITE}"/>
        """),
        ("food_37_karadantu_gokak", "Gokak Karadantu Sweet", "ಗೋಕಾಕ್ ಕರದಂಟು", ["karadantu", "gokak", "jaggery", "dryfruit"], f"""
        <!-- Chewy jaggery block embedded with almonds, cashews, and edible gum -->
        <rect x="16" y="20" width="32" height="24" rx="3" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <!-- Dry fruit pieces embedded -->
        <ellipse cx="24" cy="28" rx="3" ry="2" fill="{CREAM}"/>
        <ellipse cx="38" cy="26" rx="3" ry="2" fill="{CREAM}"/>
        <circle cx="32" cy="36" r="2.5" fill="{GOLD}"/>
        """),
        ("food_38_antinkunde_laddu", "Antina Unde (Dink Laddu)", "ಅಂಟಿನ ಉಂಡೆ", ["antinaunde", "laddu", "dryfruit", "energy"], f"""
        <!-- Round textured jaggery dry fruit ball -->
        <circle cx="32" cy="32" r="16" fill="{BROWN}" stroke="{DARK}" stroke-width="2"/>
        <circle cx="26" cy="26" r="2" fill="{CREAM}"/>
        <circle cx="36" cy="28" r="2" fill="{GOLD}"/>
        <circle cx="30" cy="38" r="2" fill="{CREAM}"/>
        """),
        ("food_39_kodubale_spiral_snack", "Crunchy Kodubale Ring", "ಕೋಡುಬಳೆ", ["kodubale", "crunchy", "snack"], f"""
        <!-- Ring / crescent shaped spicy snack with pointed tapered ends -->
        <path d="M 20 40 C 14 30 20 18 32 18 C 44 18 50 30 44 40 C 38 48 26 48 20 40 Z" fill="{RED}" stroke="{BROWN}" stroke-width="2.5"/>
        <circle cx="32" cy="32" r="5" fill="{DARK}"/>
        <circle cx="28" cy="24" r="1" fill="{CREAM}"/>
        <circle cx="36" cy="24" r="1" fill="{CREAM}"/>
        """),
        ("food_40_nippattu_crunchy_cracker", "Nippattu Rice Cracker", "ನಿಪ್ಪಟ್ಟು", ["nippattu", "cracker", "crunchy"], f"""
        <circle cx="32" cy="32" r="18" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <!-- Peanuts & curry leaves in cracker -->
        <ellipse cx="26" cy="28" rx="2.5" ry="1.5" fill="{BROWN}"/>
        <ellipse cx="38" cy="34" rx="2.5" ry="1.5" fill="{BROWN}"/>
        <circle cx="32" cy="38" r="1.5" fill="{GREEN}"/>
        """),
        ("food_41_chakkuli_spiral", "Chakkuli / Murukku Spiral", "ಚಕ್ಕುಲಿ", ["chakkuli", "murukku", "spiral", "crisp"], f"""
        <!-- Spiky spiral extruded coil -->
        <path d="M 32 32 C 34 30 36 34 32 36 C 26 38 24 28 32 24 C 42 20 44 38 32 42 C 18 46 16 20 32 14" stroke="{GOLD}" stroke-width="3" stroke-linecap="round" fill="none"/>
        """),
        ("food_42_churumuri_street_snack", "Bangalore Churumuri / Girmit", "ಬೆಂಗಳೂರು ಚುರುಮುರಿ", ["churumuri", "girmit", "streetfood", "snack"], f"""
        <!-- Newspaper cone holding spicy puffed rice -->
        <polygon points="32,54 18,22 46,22" fill="{CREAM}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="22" rx="14" ry="6" fill="{YELLOW}"/>
        <!-- Grated carrot & coriander garnish -->
        <circle cx="28" cy="22" r="1.5" fill="{ORANGE}"/>
        <circle cx="36" cy="22" r="1.5" fill="{GREEN}"/>
        """),
        ("food_43_mirchi_bhajji_menasinakayi", "Menasinakayi Bhajji (Mirchi Fritter)", "ಮೆಣಸಿನಕಾಯಿ ಬಜ್ಜಿ", ["mirchibhajji", "menasinakayi", "fritter"], f"""
        <!-- Long batter coated fried chili with green stem -->
        <path d="M 24 20 C 24 20 34 26 36 38 C 38 46 32 52 30 52 C 28 52 24 46 22 36 Z" fill="{GOLD}" stroke="{BROWN}" stroke-width="2"/>
        <line x1="24" y1="20" x2="22" y2="12" stroke="{GREEN}" stroke-width="2.5" stroke-linecap="round"/>
        """),
        ("food_44_kootu_stew", "Karnataka Vegetable Kootu", "ತರಕಾರಿ ಕೂಟು", ["kootu", "stew", "vegetable"], f"""
        <path d="M 14 30 C 14 48 50 48 50 30 Z" fill="{YELLOW}" stroke="{DARK}" stroke-width="2"/>
        <ellipse cx="32" cy="30" rx="18" ry="6" fill="{GOLD}"/>
        <circle cx="26" cy="30" r="2" fill="{GREEN}"/>
        <circle cx="34" cy="31" r="2" fill="{ORANGE}"/>
        <circle cx="40" cy="29" r="2" fill="{WHITE}"/>
        """),
        ("food_45_saaru_rasam_chombu", "Traditional Saaru in Brass Pot", "ಕಲಶದ ಸಾರು (ರಸಂ)", ["saaru", "rasam", "chombu", "brass"], f"""
        <!-- Traditional narrow neck brass water pitcher (Chombu) -->
        <ellipse cx="32" cy="20" rx="8" ry="3" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="1.5"/>
        <path d="M 24 20 L 22 28 C 16 34 16 48 32 48 C 48 48 48 34 42 28 L 40 20 Z" fill="{GOLD}" stroke="{DARK_GOLD}" stroke-width="2"/>
        <!-- Steam plumes of piping hot saaru -->
        <path d="M 30 16 Q 32 8 30 4" stroke="{RED}" stroke-width="1.5" fill="none"/>
        <path d="M 34 16 Q 36 8 34 4" stroke="{RED}" stroke-width="1.5" fill="none"/>
        """),
        ("food_46_happala_sandige", "Aralu Sandige & Happala", "ಹಪ್ಪಳ ಸಂಡಿಗೆ", ["happala", "sandige", "papad"], f"""
        <!-- Disc papad -->
        <circle cx="26" cy="34" r="12" fill="{CREAM}" stroke="{GOLD}" stroke-width="1.5"/>
        <!-- Sun-dried crunchy flower sandige -->
        <circle cx="42" cy="30" r="7" fill="{YELLOW}" stroke="{ORANGE}" stroke-width="1.5"/>
        <circle cx="42" cy="30" r="2" fill="{RED}"/>
        """),
        ("food_47_halasina_kadubu", "Halasina Kadubu in Teak Leaf", "ಹಲಸಿನ ಹಣ್ಣಿನ ಕಡಬು", ["halasinakadubu", "kadubu", "jackfruit", "steamed"], f"""
        <!-- Cylindrical leaf-wrapped parcel tied with fibre -->
        <rect x="22" y="16" width="20" height="32" rx="3" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <line x1="22" y1="26" x2="42" y2="26" stroke="{BROWN}" stroke-width="2"/>
        <line x1="22" y1="38" x2="42" y2="38" stroke="{BROWN}" stroke-width="2"/>
        """),
        ("food_48_patrode_colocasia_leaves", "Patrode Pinwheel Rolls", "ಪಾತ್ರೊಡೆ", ["patrode", "colocasia", "coastal", "malnad"], f"""
        <!-- Spiral sliced green pinwheel roll -->
        <ellipse cx="32" cy="32" rx="16" ry="16" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <path d="M 32 32 C 36 26 42 32 38 38 C 30 44 22 34 28 26 C 36 16 46 26 44 36" stroke="{GOLD}" stroke-width="2" fill="none"/>
        """),
        ("food_49_bale_yele_oota_banana_leaf", "Traditional Banana Leaf Feast", "ಬಾಳೆ ಎಲೆ ಊಟ", ["bananaleaf", "oota", "feast", "meals"], f"""
        <!-- Green banana leaf cut section -->
        <ellipse cx="32" cy="32" rx="22" ry="14" fill="{GREEN}" stroke="{DARK}" stroke-width="2"/>
        <line x1="10" y1="32" x2="54" y2="32" stroke="{LIGHT_GREEN}" stroke-width="2"/>
        <!-- Salt, pickle, sweet, rice heaps -->
        <circle cx="20" cy="26" r="2" fill="{WHITE}"/>
        <circle cx="26" cy="25" r="2" fill="{RED}"/>
        <circle cx="34" cy="26" r="3" fill="{YELLOW}"/>
        <circle cx="32" cy="38" r="5" fill="{WHITE}"/>
        """),
        ("food_50_tatte_idli_gun_powder", "Thatte Idli with Gunpowder & Ghee", "ತಟ್ಟೆ ಇಡ್ಲಿ ಚಟ್ನಿ ಪುಡಿ ತುಪ್ಪ", ["thatteidli", "gunpowder", "ghee"], f"""
        <ellipse cx="32" cy="34" rx="20" ry="12" fill="{WHITE}" stroke="{SLATE}" stroke-width="2"/>
        <!-- Generous spread of red chutney pudi -->
        <circle cx="32" cy="34" r="8" fill="{RED}"/>
        <!-- Pool of golden melted ghee -->
        <circle cx="32" cy="34" r="4" fill="{GOLD}"/>
        """)
    ]

    for icon_id, name, kn_name, tags, inner_svg in food_batch:
        add(icon_id, name, kn_name, tags, inner_svg)

    return icons
