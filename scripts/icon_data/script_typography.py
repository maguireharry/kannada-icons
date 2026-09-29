"""
Category 1: Kannada Script, Letters & Typography (65 icons)
"""
from .common import RED, YELLOW, GOLD, DARK_GOLD, SLATE, wrap_svg

def create_script_icon(glyph, name, kn_name, icon_id, badge_style="squircle", sub_label=""):
    border_color = RED if badge_style == "red" else (GOLD if badge_style == "gold" else YELLOW)
    accent_fill = "rgba(200, 16, 46, 0.06)" if badge_style == "red" else "rgba(255, 209, 0, 0.08)"
    
    # 64x64 icon canvas with transparent background
    svg_body = f"""
    <!-- Kannada Script Icon: {name} -->
    <rect x="6" y="6" width="52" height="52" rx="14" fill="{accent_fill}" stroke="{border_color}" stroke-width="2"/>
    <circle cx="12" cy="12" r="1.5" fill="{GOLD}"/>
    <circle cx="52" cy="12" r="1.5" fill="{GOLD}"/>
    <circle cx="12" cy="52" r="1.5" fill="{GOLD}"/>
    <circle cx="52" cy="52" r="1.5" fill="{GOLD}"/>
    <path d="M 26 8 Q 32 4 38 8" stroke="{RED}" stroke-width="1.5" stroke-linecap="round" fill="none"/>
    <text x="32" y="37" font-family="'Noto Sans Kannada', 'Noto Serif Kannada', 'Tunga', 'Kedage', sans-serif" font-size="26" font-weight="bold" fill="{SLATE}" text-anchor="middle" dominant-baseline="middle">{glyph}</text>
    """
    if sub_label:
        svg_body += f"""<text x="32" y="53" font-family="sans-serif" font-size="6" font-weight="600" fill="#64748B" text-anchor="middle">{sub_label}</text>"""

    return {
        "id": icon_id,
        "name": name,
        "kannada_name": kn_name,
        "category": "script-typography",
        "tags": ["kannada", "script", "alphabet", "letter", "typography", glyph],
        "svg": wrap_svg(svg_body)
    }

def get_icons():
    icons = []
    
    # 1. Swaragalu (Vowels)
    swaras = [
        ("ಅ", "Kannada Letter A", "ಕನ್ನಡ ಸ್ವರ 'ಅ'", "script_01_swara_a", "a"),
        ("ಆ", "Kannada Letter AA", "ಕನ್ನಡ ಸ್ವರ 'ಆ'", "script_02_swara_aa", "aa"),
        ("ಇ", "Kannada Letter I", "ಕನ್ನಡ ಸ್ವರ 'ಇ'", "script_03_swara_i", "i"),
        ("ಈ", "Kannada Letter EE", "ಕನ್ನಡ ಸ್ವರ 'ಈ'", "script_04_swara_ee", "ee"),
        ("ಉ", "Kannada Letter U", "ಕನ್ನಡ ಸ್ವರ 'ಉ'", "script_05_swara_u", "u"),
        ("ಊ", "Kannada Letter OO", "ಕನ್ನಡ ಸ್ವರ 'ಊ'", "script_06_swara_oo", "oo"),
        ("ಋ", "Kannada Letter RU", "ಕನ್ನಡ ಸ್ವರ 'ಋ'", "script_07_swara_ru", "ru"),
        ("ಎ", "Kannada Letter E", "ಕನ್ನಡ ಸ್ವರ 'ಎ'", "script_08_swara_e", "e"),
        ("ಏ", "Kannada Letter E_LONG", "ಕನ್ನಡ ಸ್ವರ 'ಏ'", "script_09_swara_e_long", "ē"),
        ("ಐ", "Kannada Letter AI", "ಕನ್ನಡ ಸ್ವರ 'ಐ'", "script_10_swara_ai", "ai"),
        ("ಒ", "Kannada Letter O", "ಕನ್ನಡ ಸ್ವರ 'ಒ'", "script_11_swara_o", "o"),
        ("ಓ", "Kannada Letter O_LONG", "ಕನ್ನಡ ಸ್ವರ 'ಓ'", "script_12_swara_o_long", "ō"),
        ("ಔ", "Kannada Letter AU", "ಕನ್ನಡ ಸ್ವರ 'ಔ'", "script_13_swara_au", "au"),
        ("ಅಂ", "Kannada Letter AM (Anusvara)", "ಕನ್ನಡ ಸ್ವರ 'ಅಂ' (ಅನುಸ್ವಾರ)", "script_14_swara_am", "am"),
        ("ಅಃ", "Kannada Letter AHA (Visarga)", "ಕನ್ನಡ ಸ್ವರ 'ಅಃ' (ವಿಸರ್ಗ)", "script_15_swara_aha", "aha"),
    ]
    for glyph, name, kn_name, icon_id, sub in swaras:
        icons.append(create_script_icon(glyph, name, kn_name, icon_id, "gold", sub))

    # 2. Vyanjanagalu (Consonants)
    vyanjanas = [
        ("ಕ", "Kannada Consonant Ka", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಕ'", "script_16_ka", "ka"),
        ("ಖ", "Kannada Consonant Kha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಖ'", "script_17_kha", "kha"),
        ("ಗ", "Kannada Consonant Ga", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಗ'", "script_18_ga", "ga"),
        ("ಘ", "Kannada Consonant Gha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಘ'", "script_19_gha", "gha"),
        ("ಙ", "Kannada Consonant Nga", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಙ'", "script_20_nga", "nga"),
        
        ("ಚ", "Kannada Consonant Cha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಚ'", "script_21_cha", "cha"),
        ("ಛ", "Kannada Consonant Chha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಛ'", "script_22_chha", "chha"),
        ("ಜ", "Kannada Consonant Ja", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಜ'", "script_23_ja", "ja"),
        ("ಝ", "Kannada Consonant Jha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಝ'", "script_24_jha", "jha"),
        ("ಞ", "Kannada Consonant Nya", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಞ'", "script_25_nya", "nya"),
        
        ("ಟ", "Kannada Consonant Ta (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಟ'", "script_26_ta", "ṭa"),
        ("ಠ", "Kannada Consonant Tha (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಠ'", "script_27_tha", "ṭha"),
        ("ಡ", "Kannada Consonant Da (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಡ'", "script_28_da", "ḍa"),
        ("ಢ", "Kannada Consonant Dha (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಢ'", "script_29_dha", "ḍha"),
        ("ಣ", "Kannada Consonant Na (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಣ'", "script_30_na_retro", "ṇa"),
        
        ("ತ", "Kannada Consonant Ta (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ತ'", "script_31_ta_dental", "ta"),
        ("ಥ", "Kannada Consonant Tha (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಥ'", "script_32_tha_dental", "tha"),
        ("ದ", "Kannada Consonant Da (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ದ'", "script_33_da_dental", "da"),
        ("ಧ", "Kannada Consonant Dha (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಧ'", "script_34_dha_dental", "dha"),
        ("ನ", "Kannada Consonant Na (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ನ'", "script_35_na_dental", "na"),
        
        ("ಪ", "Kannada Consonant Pa", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಪ'", "script_36_pa", "pa"),
        ("ಫ", "Kannada Consonant Pha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಫ'", "script_37_pha", "pha"),
        ("ಬ", "Kannada Consonant Ba", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಬ'", "script_38_ba", "ba"),
        ("ಭ", "Kannada Consonant Bha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಭ'", "script_39_bha", "bha"),
        ("ಮ", "Kannada Consonant Ma", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಮ'", "script_40_ma", "ma"),
        
        ("ಯ", "Kannada Consonant Ya", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಯ'", "script_41_ya", "ya"),
        ("ರ", "Kannada Consonant Ra", "ಕನ್ನಡ ವ್ಯಂಜನ 'ರ'", "script_42_ra", "ra"),
        ("ಲ", "Kannada Consonant La", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಲ'", "script_43_la", "la"),
        ("ವ", "Kannada Consonant Va", "ಕನ್ನಡ ವ್ಯಂಜನ 'ವ'", "script_44_va", "va"),
        ("ಶ", "Kannada Consonant Sha (Palatal)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಶ'", "script_45_sha", "śa"),
        ("ಷ", "Kannada Consonant Sha (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಷ'", "script_46_sha_retro", "ṣa"),
        ("ಸ", "Kannada Consonant Sa (Dental)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಸ'", "script_47_sa", "sa"),
        ("ಹ", "Kannada Consonant Ha", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಹ'", "script_48_ha", "ha"),
        ("ಳ", "Kannada Consonant Lla (Retroflex)", "ಕನ್ನಡ ವ್ಯಂಜನ 'ಳ'", "script_49_lla", "ḷa"),
    ]
    for glyph, name, kn_name, icon_id, sub in vyanjanas:
        icons.append(create_script_icon(glyph, name, kn_name, icon_id, "red", sub))

    # 3. Kannada Numerals (0 to 9)
    numerals = [
        ("೦", "Kannada Numeral 0 (Sonney)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೦ (ಸೊನ್ನೆ)", "script_50_num_0", "0"),
        ("೧", "Kannada Numeral 1 (Ondu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೧ (ಒಂದು)", "script_51_num_1", "1"),
        ("೨", "Kannada Numeral 2 (Eradu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೨ (ಎರಡು)", "script_52_num_2", "2"),
        ("೩", "Kannada Numeral 3 (Mooru)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೩ (ಮೂರು)", "script_53_num_3", "3"),
        ("೪", "Kannada Numeral 4 (Naalku)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೪ (ನಾಲ್ಕು)", "script_54_num_4", "4"),
        ("೫", "Kannada Numeral 5 (Aidu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೫ (ಐದು)", "script_55_num_5", "5"),
        ("೬", "Kannada Numeral 6 (Aaru)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೬ (ಆರು)", "script_56_num_6", "6"),
        ("೭", "Kannada Numeral 7 (Yelu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೭ (ಏಳು)", "script_57_num_7", "7"),
        ("೮", "Kannada Numeral 8 (Entu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೮ (ಎಂಟು)", "script_58_num_8", "8"),
        ("೯", "Kannada Numeral 9 (Ombattu)", "ಕನ್ನಡ ಸಂಖ್ಯೆ ೯ (ಒಂಬತ್ತು)", "script_59_num_9", "9"),
    ]
    for glyph, name, kn_name, icon_id, sub in numerals:
        icons.append(create_script_icon(glyph, name, kn_name, icon_id, "gold", sub))

    # 4. Sacred & Typographical Glyphs
    symbols = [
        ("ಓಂ", "Kannada Sacred Om", "ಕನ್ನಡ ಪವಿತ್ರ ಪ್ರಣವ 'ಓಂ'", "script_60_om", "Om"),
        ("ಶ್ರೀ", "Kannada Auspicious Shree", "ಕನ್ನಡ ಮಂಗಳಕರ 'ಶ್ರೀ'", "script_61_shree", "Shree"),
        ("್", "Kannada Virama / Halant", "ಕನ್ನಡ ಹಲ್ / ವಿರಾಮ ಚಿಹ್ನೆ", "script_62_virama", "Halant"),
        ("ಂ", "Kannada Anusvara Bindu", "ಕನ್ನಡ ಅನುಸ್ವಾರ ಬಿಂದು", "script_63_anusvara", "Bindu"),
        ("ಃ", "Kannada Visarga", "ಕನ್ನಡ ವಿಸರ್ಗ ಚಿಹ್ನೆ", "script_64_visarga", "Visarga"),
        ("ಁ", "Kannada Ardhachandra", "ಕನ್ನಡ ಅರ್ಧಚಂದ್ರ", "script_65_ardhachandra", "Chandra"),
    ]
    for glyph, name, kn_name, icon_id, sub in symbols:
        icons.append(create_script_icon(glyph, name, kn_name, icon_id, "red", sub))

    return icons
