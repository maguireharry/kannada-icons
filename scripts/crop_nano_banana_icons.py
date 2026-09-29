import os
import glob
from PIL import Image
import numpy as np
from scipy import ndimage

SHEET_ICONS = {
    "karnataka_icon_pack_sheet": [
        "mysore_palace", "yakshagana_mask", "hampi_stone_chariot",
        "carnatic_veena", "mysore_pak", "royal_bengal_tiger",
        "karnataka_flag", "filter_coffee_tumbler", "visvesvaraya_glasses"
    ],
    "bengaluru_tech_pack_sheet": [
        "namma_metro", "isro_rocket_launch", "bmtc_electric_bus",
        "bangalore_auto_rickshaw", "lalbagh_glasshouse", "iisc_tower",
        "karnataka_silicon_chip", "mysore_sandal_soap", "chinnaswamy_stadium"
    ],
    "wildlife_nature_pack_sheet": [
        "asian_elephant", "royal_bengal_tiger_head", "neelakantha_indian_roller",
        "blackbuck_antelope", "malabar_giant_squirrel", "great_indian_hornbill",
        "sacred_lotus", "sandalwood_branch_log", "coorg_coffee_berries"
    ],
    "crafts_textiles_pack_sheet": [
        "mysore_silk_saree", "channapatna_wooden_horse", "bidriware_silver_vase",
        "sandalwood_carved_elephant", "ilkal_saree", "kasuti_embroidery_mandala",
        "kempu_temple_jhumka", "kinhal_painted_parrot", "lambani_mirrorwork"
    ],
    "folk_festivals_pack_sheet": [
        "dollu_kunitha_drum", "veeragase_warrior", "kambala_racing_buffalo",
        "ugadi_bevu_bella", "mysore_dasara_ambari", "bangalore_karaga",
        "bhoota_kola_mask", "carnatic_mridangam", "dasara_gombe_habba"
    ],
    "cuisine_flavors_pack_sheet": [
        "davangere_benne_dosa", "dharwad_peda", "thatte_idli",
        "bisi_bele_bath", "ragi_mudde", "jolada_rotti",
        "maddur_vada", "mangalore_buns", "girmit_snack"
    ],
    "dynasties_emblems_pack_sheet": [
        "kadamba_lion", "chalukya_varaha", "hoysala_sala_tiger",
        "rashtrakuta_garuda", "wodeyar_coat_of_arms", "vijayanagara_gold_varaha",
        "tipu_sultan_tiger", "keladi_nayaka_seal", "mysore_peta_turban"
    ],
    "monuments_temples_pack_sheet": [
        "belur_chennakeshava_temple", "halebidu_hoysaleshwara_temple", "badami_cave_temple",
        "gol_gumbaz", "shravanabelagola_bahubali", "murudeshwar_shiva",
        "aihole_durga_temple", "pattadakal_virupaksha_temple", "bangalore_vidhana_soudha"
    ],
    "geography_nature_pack_sheet": [
        "jog_falls", "shivanasamudra_falls", "gokarna_om_beach",
        "st_marys_island", "kaup_beach_lighthouse", "yana_caves",
        "kudremukh_peak", "mullayanagiri_peak", "mekedatu_gorge"
    ],
    "literature_culture_pack_sheet": [
        "basavanna_kayakave_kailasa", "vachana_palm_leaf_manuscript", "ishtalinga_pendant",
        "kuvempu_kavishaila", "saraswati_vagdevi_statue", "halmidi_stone_inscription",
        "pooja_kalasha", "brass_arati_deepa", "rangoli_mandala"
    ],
    "agricultural_spices_pack_sheet": [
        "byadagi_red_chili", "nanjangud_rasabale_banana", "udupi_mattu_gulla",
        "green_cardamom_pods", "malnad_black_pepper", "mysore_betel_leaf",
        "badami_mango", "areca_nut_adike", "sihi_elaneeru_coconut"
    ],
    "musical_instruments_pack_sheet": [
        "carnatic_veena", "yakshagana_chande", "mridangam_drum",
        "maddale_percussion", "kamsale_brass_cymbals", "tambura_lute",
        "ghatam_clay_pot", "shanku_sacred_conch", "nadaswaram_pipe"
    ],
    "forts_palaces_pack_sheet": [
        "chitradurga_stone_fort", "bidar_fort_gate", "tipu_summer_palace",
        "kittur_chennamma_fort", "lalitha_mahal_palace", "bellary_rock_fort",
        "srirangapatna_water_gate", "mirjan_laterite_fort", "madikeri_coorg_fort"
    ],
    "tribal_folk_pack_sheet": [
        "togalu_gombeyaata_hanuman", "somana_kunitha_mask", "goravara_kunitha_bear",
        "pooja_kunitha_tower", "lambani_tribal_woman", "halakki_vokkaliga_elder",
        "jenu_kuruba_honey_basket", "koraga_tribal_drums", "wild_honeycomb"
    ],
    "coastal_maritime_pack_sheet": [
        "malpe_pattanod_boat", "bangude_mackerel_fish", "mangalore_roof_tile",
        "cashew_apple_nut", "neer_dosa_fish_curry", "karavali_backwater_canoe",
        "coir_fishing_net", "blue_flag_beach", "gokarna_koti_tirtha_pond"
    ],
    "birds_sanctuaries_pack_sheet": [
        "great_indian_bustard", "painted_stork", "malabar_pied_hornbill",
        "asian_paradise_flycatcher", "brahminy_kite", "spot_billed_pelican",
        "bar_headed_goose", "emerald_dove", "white_bellied_blue_flycatcher"
    ],
    "sweets_confectionery_pack_sheet": [
        "belagavi_kunda", "gokak_karadantu", "karjikai",
        "obbattu_holige", "chiroti_badam_milk", "kashi_halwa",
        "halbai_fudge", "shavige_payasa", "pheni_sweet"
    ],
    "savouries_snacks_pack_sheet": [
        "nippattu_cracker", "kodubale_rings", "chakkuli_murukku",
        "goli_baje_fritters", "congress_kadlekai", "maddur_vada_snack",
        "mandakki_oggarane", "avarekalu_mixture", "kerala_karnataka_banana_chips"
    ],
    "malnad_coastal_food_pack_sheet": [
        "kori_rotti_chicken_curry", "patrode_colocasia_roll", "akki_rotti_banana_leaf",
        "kane_ladyfish_fry", "marwai_clams_sukka", "kadubu_jackfruit_leaf",
        "halasina_hannu_jackfruit", "kokum_punarpuli_drink", "jackfruit_happala_papad"
    ],
    "bengaluru_landmarks_pack_sheet": [
        "bangalore_palace_tudor", "cubbon_park_library", "ulsoor_lake_boating",
        "vidyarthi_bhavan_dosa", "bangalore_auto_meter", "ngma_mansion",
        "st_marys_basilica", "russell_market_clock_tower", "commercial_street_shopping"
    ],
    "weapons_armor_pack_sheet": [
        "mysore_talwar_sword", "onake_obavva_pestle", "kadamba_gold_shield",
        "vijayanagara_katar_dagger", "tipu_tiger_pistol", "mysore_royal_gada",
        "kodava_peeche_kathi", "kodava_odi_kathi", "archery_bow_arrow"
    ],
    "coorg_kodagu_pack_sheet": [
        "kodava_kupya_chele", "coorg_pandi_curry", "coorg_mandarin_orange",
        "talacauvery_spring_pot", "kadambuttu_rice_balls", "kokkethathi_cobra_pendant",
        "bamboo_shoot_kanile_curry", "kodava_brass_sheath", "brahmagiri_coffee_blossom"
    ],
    "carnatic_music_pack_sheet": [
        "purandara_dasa_tambura", "kanakana_kindi_window", "carnatic_violin",
        "venu_bamboo_flute", "mridangam_tuning_stone", "electronic_shruti_box",
        "chipla_hand_clappers", "palm_leaf_music_notes", "bronze_nataraja"
    ],
    "sandalwood_cinema_pack_sheet": [
        "dr_rajkumar_portrait", "vintage_35mm_film_reel", "gandhada_gudi_badge",
        "mayura_golden_crown", "auto_raja_driver_cap", "babruvahana_sword_shield",
        "kgf_gold_bar_hammer", "kantara_divine_mask", "state_film_award_trophy"
    ],
    "traditional_jewellery_pack_sheet": [
        "lakshmi_kasu_malai", "kadaga_lion_bangle", "vanki_ruby_armlet",
        "south_indian_mookuthi", "chandra_surya_hair_jewels", "emerald_pearl_haara",
        "daabu_gold_waist_belt", "silver_kaalungura_rings", "brass_gejje_ankle_bells"
    ],
    "kannada_swaras_pack_sheet": [
        "kannada_letter_a", "kannada_letter_aa", "kannada_letter_i",
        "kannada_letter_ee", "kannada_letter_u", "kannada_letter_oo",
        "kannada_letter_ru", "kannada_letter_e", "kannada_letter_ae"
    ],
    "kannada_letters_part2_pack_sheet": [
        "kannada_letter_ai", "kannada_letter_o", "kannada_letter_oh",
        "kannada_letter_au", "kannada_letter_am", "kannada_letter_aha",
        "kannada_letter_ka", "kannada_letter_kha", "kannada_letter_ga"
    ],
    "kannada_numerals_pack_sheet": [
        "kannada_numeral_1", "kannada_numeral_2", "kannada_numeral_3",
        "kannada_numeral_4", "kannada_numeral_5", "kannada_numeral_6",
        "kannada_numeral_7", "kannada_numeral_8", "kannada_numeral_9"
    ],
    "sacred_festivals_pack_sheet": [
        "gowri_ganesha_idol", "varamahalakshmi_kalasha", "nagara_panchami_cobra",
        "deepavali_deepa_sparkler", "makar_sankranti_ellu_bella", "hampi_utsav_chariot",
        "ayudha_pooja_tools", "maha_shivaratri_lingam", "vaikunta_ekadashi_gateway"
    ],
    "village_farming_pack_sheet": [
        "bullock_cart", "wooden_plough_negilu", "scarecrow_paddy_field",
        "stone_well_pulley", "beesuva_kallu_grinder", "kanaja_grain_silo",
        "mora_winnowing_tray", "brass_milk_can", "karnataka_farmer"
    ],
    "traditional_games_pack_sheet": [
        "chowka_bara_game", "pagade_board_game", "buguri_spinning_top",
        "gilli_danda_wooden", "chenne_mane_mancala", "aadu_huli_aata",
        "goti_glass_marbles", "channapatna_rattle_toy", "lagori_seven_stones"
    ],
    "rivers_reservoirs_pack_sheet": [
        "kaveri_talacauvery_spring", "krishna_river_rocks", "tungabhadra_coracle_boat",
        "sharavathi_river_cascade", "krs_dam_brindavan_gardens", "almatti_dam_gates",
        "netravathi_river_estuary", "tungabhadra_dam_masonry", "malaprabha_river_ghats"
    ],
    "karnataka_legends_pack_sheet": [
        "sir_mv_visvesvaraya", "rashtrakavi_kuvempu", "kittur_rani_chennamma",
        "krantiveera_sangolli_rayanna", "akka_mahadevi_vachanakarthi", "bhakta_kanakadasa",
        "dr_shivaram_karanth", "field_marshal_cariappa", "shakuntala_devi_mathematician"
    ],
    "handloom_sarees_pack_sheet": [
        "mysore_silk_zari_saree", "ilkal_topi_teni_saree", "molakalmuru_temple_saree",
        "guledgudda_khana_fabric", "udupi_cotton_handloom_saree", "patteda_anchu_saree",
        "navalgund_jamkhana_durrie", "wooden_flying_shuttle", "traditional_charkha_wheel"
    ],
    "sacred_chariots_pack_sheet": [
        "mysore_dasara_ambari_howdah", "udupi_brahmaratha_chariot", "temple_chariot_wooden_wheel",
        "melukote_vairamudi_crown", "kukke_subramanya_silver_chariot", "golden_temple_pallaki",
        "temple_umbrella_muthukuda", "chamundeshwari_golden_idol", "coconut_breaking_ritual"
    ]
}

def crop_icons():
    output_dir = "/config/Desktop/images/kannada-icons/nano-banana-icons/individual"
    os.makedirs(output_dir, exist_ok=True)
    sheets = sorted(glob.glob("/config/Desktop/images/kannada-icons/nano-banana-icons/*_sheet*.png"))
    
    total_cropped = 0
    for sheet_path in sheets:
        base = os.path.basename(sheet_path)
        key = None
        for k in SHEET_ICONS:
            if k in base:
                key = k
                break
        
        if not key:
            print(f"Skipping unknown sheet: {base}")
            continue
            
        names = SHEET_ICONS[key]
        img = Image.open(sheet_path)
        gray = img.convert('L')
        arr = np.array(gray)
        mask = arr < 240
        labeled, num_features = ndimage.label(mask)
        objects = ndimage.find_objects(labeled)
        
        icons = []
        for sl in objects:
            h = sl[0].stop - sl[0].start
            w = sl[1].stop - sl[1].start
            if 90 < h < 380 and 90 < w < 380:
                icons.append((sl[1].start, sl[0].start, w, h))
                
        icons = sorted(icons, key=lambda b: (b[1] // 150, b[0]))
        
        filtered_icons = []
        for b in icons:
            if not any(abs(b[0] - fb[0]) < 50 and abs(b[1] - fb[1]) < 50 for fb in filtered_icons):
                filtered_icons.append(b)
                
        if len(filtered_icons) != 9:
            xs = [50, 375, 700]
            ys = [80, 400, 715]
            size = 270
            filtered_icons = []
            for y in ys:
                for x in xs:
                    filtered_icons.append((x, y, size, size))
                    
        for idx, box in enumerate(filtered_icons[:9]):
            icon_name = names[idx] if idx < len(names) else f"{key}_icon_{idx+1}"
            x, y, w, h = box
            pad = 6
            x0 = max(0, x - pad)
            y0 = max(0, y - pad)
            x1 = min(img.width, x + w + pad)
            y1 = min(img.height, y + h + pad)
            
            crop = img.crop((x0, y0, x1, y1))
            crop = crop.resize((512, 512), Image.Resampling.LANCZOS)
            out_path = os.path.join(output_dir, f"{icon_name}.png")
            crop.save(out_path, format="PNG")
            total_cropped += 1
            
    print(f"\nSuccessfully cropped {total_cropped} individual 512x512 icons into {output_dir}!")

if __name__ == "__main__":
    crop_icons()
