import json
import os

all_sheets = [
    # Sheet 1: Bhavageethe & Poetic Anthems
    {
        "key": "songs_sheet_01_bhavageethe",
        "theme": "Bhavageethe & Poetic Anthems",
        "theme_kn": "ಭಾವಗೀತೆ ಮತ್ತು ಕಾವ್ಯ ಸಿರಿ",
        "style_movement": "Abstract Watercolor, Ink Calligraphy & Paper Cutout",
        "songs": [
            ("song_001_kaanada_kadalige", "Kaanada Kadalige", "ಕಾಣದ ಕಡಲಿಗೆ", "Bhavageethe (Album)", "ಭಾವಗೀತೆ", "C. Ashwath", "C. Ashwath", "G.S. Shivarudrappa", 1980, "Abstract Ocean Waves & Golden Sail"),
            ("song_002_kurigalu_saar_kurigalu", "Kurigalu Saar Kurigalu", "ಕುರಿಗಳು ಸಾರ್ ಕುರಿಗಳು", "Nityotsava (Album)", "ನಿತ್ಯೋತ್ಸವ", "Shimoga Subbanna", "Mysore Ananthaswamy", "K.S. Nissar Ahmed", 1978, "Surrealist Satirical Graphic Pop Art"),
            ("song_003_taravva_thangi_taravva", "Taravva Thangi Taravva", "ತಾರವ್ವ ತಂಗಿ ತಾರವ್ವ", "Janapada Bhavagita", "ಜನಪದ ಭಾವಗೀತೆ", "C. Ashwath", "C. Ashwath", "Traditional Folk", 1982, "Traditional Indian Folk Linocut"),
            ("song_004_elladaru_iru_enthadaru_iru", "Elladaru Iru Enthadaru Iru", "ಎಲ್ಲಾದರೂ ಇರು ಎಂತಾದರು ಇರು", "Kuvempu Kavya", "ಕುವೆಂಪು ಕಾವ್ಯ ಸಿರಿ", "PB Sreenivas & Chorus", "Mysore Ananthaswamy", "Rashtrakavi Kuvempu", 1975, "Minimalist Swiss Typography & Nature"),
            ("song_005_nee_heenga_nodabyada_nanna", "Nee Heenga Nodabyada Nanna", "ನೀ ಹೀಂಗ ನೋಡಬ್ಯಾಡ ನನ್ನ", "Bendre Bhavaganga", "ಬೇಂದ್ರೆ ಭಾವಗಂಗಾ", "Ratnamala Prakash", "C. Ashwath", "Da Ra Bendre", 1981, "Matisse Paper Cutout Silhouette"),
            ("song_006_jogada_siri_belakinalli", "Jogada Siri Belakinalli", "ಜೋಗದ ಸಿರಿ ಬೆಳಕಿನಲ್ಲಿ", "Nityotsava (Album)", "ನಿತ್ಯೋತ್ಸವ", "Mysore Ananthaswamy", "Mysore Ananthaswamy", "K.S. Nissar Ahmed", 1978, "Art Nouveau Flowing Streams & Cascades"),
            ("song_007_andu_kanda_aa_mukha", "Andu Kanda Aa Mukha", "ಅಂದು ಕಂಡ ಆ ಮುಖ", "Prema Sangama (Album)", "ಪ್ರೇಮ ಸಂಗಮ", "Ratnamala Prakash", "Mysore Ananthaswamy", "K.S. Narasimhaswamy", 1983, "Impressionist Dreamy Pastel Memory"),
            ("song_008_theranerida_ambaradolu", "Theranerida Ambaradolu", "ತೇರನೇರಿದ ಅಂಬರದೊಳು", "Kuvempu Bhavadarshana", "ಕುವೆಂಪು ಭಾವದರ್ಶನ", "Shimoga Subbanna", "C. Ashwath", "Rashtrakavi Kuvempu", 1980, "Cosmic Stained Glass Celestial Chariot"),
            ("song_009_benne_kadda_namma_krishna", "Benne Kadda Namma Krishna", "ಬೆಣ್ಣೆ ಕದ್ದ ನಮ್ಮ ಕೃಷ್ಣ", "Dasa Sahitya (Album)", "ದಾಸ ಸಾಹಿತ್ಯ", "Bhimsen Joshi", "Traditional Carnatic", "Purandara Dasa", 1972, "Mysore Traditional Miniature Painting")
        ]
    },
    # Sheet 2: Kannada Pride & Rajyotsava Anthems
    {
        "key": "songs_sheet_02_kannada_pride",
        "theme": "Kannada Pride & Rajyotsava Anthems",
        "theme_kn": "ಕನ್ನಡ ನಾಡು-ನುಡಿ ಗೀತೆಗಳು",
        "style_movement": "Soviet Constructivist, Bauhaus & Silkscreen Graphic",
        "songs": [
            ("song_010_huttidare_kannada_nadalli", "Huttidare Kannada Nadalli Huttabeku", "ಹುಟ್ಟಿದರೆ ಕನ್ನಡ ನಾಡಲ್ಲಿ ಹುಟ್ಟಬೇಕು", "Aakasmika (Movie)", "ಆಕಸ್ಮಿಕ", "Dr. Rajkumar", "Hamsalekha", "Hamsalekha", 1993, "Heroic Soviet Constructivist Vector Art"),
            ("song_011_baarisu_kannada_dindimava", "Baarisu Kannada Dindimava", "ಬಾರಿಸು ಕನ್ನಡ ಡಿಂಡಿಮವ", "Rashtrakavi Kavya", "ಕುವೆಂಪು ಕಾವ್ಯ ಸಿರಿ", "Shimoga Subbanna & Chorus", "C. Ashwath", "Rashtrakavi Kuvempu", 1977, "Bauhaus Rhythm & War Drum Waves"),
            ("song_012_jenina_holeyo_halina_maleyo", "Jenina Holeyo Halina Maleyo", "ಜೇನಿನ ಹೊಳೆಯೋ ಹಾಲಿನ ಮಳೆಯೋ", "Chalisuva Modagalu (Movie)", "ಚಲಿಸುವ ಮೋಡಗಳು", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1982, "1970s Psychedelic Pop Art Swirls"),
            ("song_013_kannada_nadina_jeevanadi", "Kannada Nadina Jeevanadi", "ಕನ್ನಡ ನಾಡಿನ ಜೀವನದಿ", "Jeevanadi (Movie)", "ಜೀವನದಿ", "SP Balasubrahmanyam", "Koti", "R.N. Jayagopal", 1996, "Art Deco Stepped River Flow"),
            ("song_014_hesarayithu_karnataka", "Hesarayithu Karnataka Usiragali Kannada", "ಹೆಸರಾಯಿತು ಕರ್ನಾಟಕ ಉಸಿರಾಗಲಿ ಕನ್ನಡ", "Rajyotsava Geethegalu", "ರಾಜ್ಯೋತ್ಸವ ಗೀತೆಗಳು", "PB Sreenivas", "M. Ranga Rao", "Huilgol Narayana Rao", 1973, "Retro 1970s Screenprint Commemorative"),
            ("song_015_munjane_eddu_yara_mukhava", "Munjane Eddu Yara Mukhava Nodide", "ಮುಂಜಾನೆ ಎದ್ದು ಯಾರ ಮುಖವ ನೋಡಿದೆ", "Bangaarada Manushya (Movie)", "ಬಂಗಾರದ ಮನುಷ್ಯ", "PB Sreenivas", "G.K. Venkatesh", "Hunsur Krishnamurthy", 1972, "Folk Kalamkari Woodblock Dawn"),
            ("song_016_hoovondu_balukithu", "Hoovondu Balukithu Hadondu Nakkithu", "ಹೂವೊಂದು ಬಳುಕಿತು ಹಾಡೊಂದು ನಕ್ಕಿತು", "Shubhamangala (Movie)", "ಶುಭಮಂಗಳ", "S. Janaki", "Vijaya Bhaskar", "Chi. Udayashankar", 1975, "Japanese Ukiyo-e Woodblock Floral"),
            ("song_017_navaduva_nudiye_kannada_nudi", "Navaduva Nudiye Kannada Nudi", "ನಾವಾಡುವ ನುಡಿಯೇ ಕನ್ನಡ ನುಡಿ", "Gandhada Gudi (Movie)", "ಗಂಧದ ಗುಡಿ", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1973, "Vintage Adventure Comic Graphic Art"),
            ("song_018_bharata_jananiya_tanujate", "Jaya Bharata Jananiya Tanujate", "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ", "Nada Geethe (Official Anthem)", "ನಾಡಗೀತೆ", "C. Ashwath Chorus", "C. Ashwath", "Rashtrakavi Kuvempu", 1985, "Stained Glass Sacred Heritage Art")
        ]
    },
    # Sheet 3: Golden Era Romance & Serenades
    {
        "key": "songs_sheet_03_golden_romance",
        "theme": "Golden Era Romance & Serenades",
        "theme_kn": "ಚಿನ್ನದ ಯುಗದ ಪ್ರೇಮ ಗೀತೆಗಳು",
        "style_movement": "Mid-Century Modern, French Lithograph & Noir Silhouette",
        "songs": [
            ("song_019_aaha_nanna_sangaathi", "Aaha Nanna Sangaathi", "ಆಹಾ ನನ್ನ ಸಂಗಾತಿ", "Bangarada Hoovu (Movie)", "ಬಂಗಾರದ ಹೂವು", "PB Sreenivas & P. Susheela", "Rajan-Nagendra", "Chi. Udayashankar", 1967, "1960s Mid-Century Travel Poster"),
            ("song_020_baala_nonada_raagave", "Baala Nonada Raagave", "ಬಾಲ ನೊಣದ ರಾಗವೇ", "Kasturi Nivasa (Movie)", "ಕಸ್ತೂರಿ ನಿವಾಸ", "PB Sreenivas", "G.K. Venkatesh", "Chi. Udayashankar", 1971, "Minimalist Linear Musical Abstract"),
            ("song_021_gaanave_jeeva_gaanave_dhyana", "Gaanave Jeeva Gaanave Dhyana", "ಗಾನವೇ ಜೀವ ಗಾನವೇ ಧ್ಯಾನ", "Amruthavahini (Movie)", "ಅಮೃತವಾಹಿನಿ", "PB Sreenivas", "M. Ranga Rao", "Vijayanarasimha", 1976, "Musical Cubist Abstract Expressionism"),
            ("song_022_baare_baare_chandada", "Baare Baare Chandada Cheluvina Taare", "ಬಾರೆ ಬಾರೆ ಚಂದದ ಚೆಲುವಿನ ತಾರೆ", "Nagarahavu (Movie)", "ನಾಗರಹಾವು", "PB Sreenivas", "Vijaya Bhaskar", "Chi. Udayashankar", 1972, "1970s Vintage Romance Comic Cover"),
            ("song_023_olave_jeevana_lekkachara", "Olave Jeevana Lekkachara", "ಒಲವೇ ಜೀವನ ಲೆಕ್ಕಾಚಾರ", "Eradu Kanasu (Movie)", "ಎರಡು ಕನಸು", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1974, "Geometric Dual-Reality Split Canvas"),
            ("song_024_kangalu_tumbiralu", "Kangalu Tumbiralu Kambani Eke", "ಕಂಗಳು ತುಂಬಿರಲು ಕಂಬನಿ ಏಕೆ", "Naa Ninna Mareyalare (Movie)", "ನಾ ನಿನ್ನ ಮರೆಯಲಾರೆ", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1976, "Monochrome Film Noir Linocut Silhouette"),
            ("song_025_nooru_nooru_kaala_baalu", "Nooru Nooru Kaala Baalu", "ನೂರು ನೂರು ಕಾಲ ಬಾಳು", "Bangarada Panjara (Movie)", "ಬಂಗಾರದ ಪಂಜರ", "PB Sreenivas", "G.K. Venkatesh", "Chi. Udayashankar", 1974, "Vintage Golden Cage Folk Metaphor"),
            ("song_026_aralide_nayana", "Aralide Nayana Maretide Mana", "ಅರಳಿದೆ ನಯನ ಮರೆತಿದೆ ಮನ", "Babruvahana (Movie)", "ಬಬ್ರುವಾಹನ", "S. Janaki", "T.G. Lingappa", "Chi. Udayashankar", 1977, "Royal Mysore Silk & Lotus Floral Art"),
            ("song_027_premada_kaanike_needuve", "Premada Kaanike Needuve Ninage", "ಪ್ರೇಮದ ಕಾಣಿಕೆ ನೀಡುವೆ ನಿನಗೆ", "Premada Kaanike (Movie)", "ಪ್ರೇಮದ ಕಾಣಿಕೆ", "PB Sreenivas", "Upendra Kumar", "Vijayanarasimha", 1976, "Vintage Heart Pop Art Silkscreen")
        ]
    },
    # Sheet 4: Dr. Rajkumar Philosophical Classics
    {
        "key": "songs_sheet_04_rajkumar_philosophical",
        "theme": "Dr. Rajkumar Philosophical Classics",
        "theme_kn": "ಡಾ. ರಾಜ್‌ಕುಮಾರ್ ತತ್ತ್ವ ಮತ್ತು ಜೀವನ ಗೀತೆಗಳು",
        "style_movement": "Surrealist Marionette, Epic Bas-Relief & Graphic Woodcut",
        "songs": [
            ("song_028_aadisi_nodu_beelisi_nodu", "Aadisi Nodu Beelisi Nodu", "ಆಡಿಸಿ ನೋಡು ಬೀಳಿಸಿ ನೋಡು", "Kasturi Nivasa (Movie)", "ಕಸ್ತೂರಿ ನಿವಾಸ", "PB Sreenivas", "G.K. Venkatesh", "Chi. Udayashankar", 1971, "Surrealist Puppet Strings & Marionette Art"),
            ("song_029_yaare_koogadali_oore_horadali", "Yaare Koogadali Oore Horadali", "ಯಾರೇ ಕೂಗಾಡಲಿ ಊರೇ ಹೋರಾಡಲಿ", "Sampathige Savaal (Movie)", "ಸಂಪತ್ತಿಗೆ ಸವಾಲ್", "Dr. Rajkumar", "G.K. Venkatesh", "Chi. Udayashankar", 1974, "Bold Brutalist Graphic Agitprop"),
            ("song_030_maanavanagu_maanavanagu", "Maanavanagu Maanavanagu", "ಮಾನವನಾಗು ಮಾನವನಾಗು", "Bangaarada Manushya (Movie)", "ಬಂಗಾರದ ಮನುಷ್ಯ", "Dr. Rajkumar", "G.K. Venkatesh", "Hunsur Krishnamurthy", 1972, "Earthy Graphic Woodcut & Golden Sunburst"),
            ("song_031_naa_ninage_jeeva_needide", "Naa Ninage Jeeva Needide", "ನಾ ನಿನಗೆ ಜೀವ ನೀಡಿದೆ", "Babruvahana (Movie)", "ಬಬ್ರುವಾಹನ", "Dr. Rajkumar", "T.G. Lingappa", "Chi. Udayashankar", 1977, "Ancient Warrior Stone Bas-Relief"),
            ("song_032_nagu_nagutha_nee_baalu", "Nagu Nagutha Nee Baalu", "ನಗು ನಗುತಾ ನೀ ಬಾಳು", "Bangaarada Hoovu (Movie)", "ಬಂಗಾರದ ಹೂವು", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1967, "Sunny Minimalist Pop Vector"),
            ("song_033_belli_moodithu_koli_koogithu", "Belli Moodithu Koli Koogithu", "ಬೆಳ್ಳಿ ಮೂಡಿತು ಕೋಳಿ ಕೂಗಿತು", "Janma Janmada Anubandha (Movie)", "ಜನ್ಮ ಜನ್ಮದ ಅನುಬಂಧ", "Dr. Rajkumar", "Ilaiyaraaja", "Chi. Udayashankar", 1980, "Rural Sunrise Folk Silhouette"),
            ("song_034_dharani_mandala_madhyadolage", "Dharani Mandala Madhyadolage", "ಧರಣಿ ಮಂಡಲ ಮಧ್ಯದೊಳಗೆ", "Punyakoti (Folk Classic)", "ಪುಣ್ಯಕೋಟಿ", "Dr. Rajkumar", "Traditional Folk", "Traditional Folk", 1977, "Traditional Indian Folk Patchwork & Cow Emblem"),
            ("song_035_aakashave_beelali_mele", "Aakashave Beelali Mele", "ಆಕಾಶವೇ ಬೀಳಲಿ ಮೇಲೆ", "Nyayave Devaru (Movie)", "ನ್ಯಾಯವೇ ದೇವರು", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1971, "Dramatic Thunderstorm Woodblock Poster"),
            ("song_036_ivalu_yaaru_balleyene", "Ivalu Yaaru Balleyene", "ಇವಳು ಯಾರು ಬಲ್ಲೆಯೇನೆ", "Mayura (Movie)", "ಮಯೂರ", "Dr. Rajkumar", "G.K. Venkatesh", "Chi. Udayashankar", 1975, "Kadamba Royal Palace Miniature Art")
        ]
    },
    # Sheet 5: Ilaiyaraaja 1980s Sandalwood Melodies
    {
        "key": "songs_sheet_05_ilaiyaraaja_melodies",
        "theme": "Ilaiyaraaja 1980s Sandalwood Melodies",
        "theme_kn": "ಇಳಯರಾಜಾ ಅವರ ಸುವರ್ಣ ಮಧುರ ಗೀತೆಗಳು",
        "style_movement": "80s Neon Synthwave, City Lights & Memphis Graphic",
        "songs": [
            ("song_037_naguva_nayana_madhura_mouna", "Naguva Nayana Madhura Mouna", "ನಗು ನಯನ ಮಧುರ ಮೌನ", "Pallavi Anu Pallavi (Movie)", "ಪಲ್ಲವಿ ಅನುಪಲ್ಲವಿ", "SP Balasubrahmanyam & S. Janaki", "Ilaiyaraaja", "R.N. Jayagopal", 1983, "80s Cyberpunk Neon Noir City Reflections"),
            ("song_038_jotheyali_jothe_jotheyali", "Jotheyali Jothe Jotheyali", "ಜೊತೆಯಲಿ ಜೊತೆ ಜೊತೆಯಲಿ", "Geetha (Movie)", "ಗೀತೆಯಲಿ", "SP Balasubrahmanyam & S. Janaki", "Ilaiyaraaja", "Chi. Udayashankar", 1981, "80s Cassette Memphis Color Geometric Art"),
            ("song_039_olavina_udugore_ellarigu", "Olavina Udugore Ellarigu", "ಒಲವಿನ ಉಡುಗೊರೆ ಎಲ್ಲರಿಗೂ", "Olavina Udugore (Movie)", "ಒಲವಿನ ಉಡುಗೊರೆ", "SP Balasubrahmanyam", "M. Ranga Rao", "R.N. Jayagopal", 1987, "Dreamy Pastel Anime Cloudscape"),
            ("song_040_thangaaliyanthe_bali_bandu", "Thangaaliyanthe Bali Bandu", "ತಂಗಾಳಿಯಂತೆ ಬಳಿ ಬಂದು", "Nammura Mandara Hoove (Movie)", "ನಮ್ಮೂರ ಮಂದಾರ ಹೂವೇ", "K.S. Chithra", "Ilaiyaraaja", "K. Kalyan", 1996, "Ghibli Wind & Wildflowers Watercolor"),
            ("song_041_nannaaseya_hoove", "Nannaaseya Hoove", "ನನ್ನಾಸೆಯ ಹೂವೇ", "Janumada Jodi (Movie)", "ಜನುಮದ ಜೋಡಿ", "Mano & Anuradha Sriram", "V. Manohar", "V. Manohar", 1996, "Vibrant Rural Kasuti Embroidery"),
            ("song_042_malligeye_malligeye", "Malligeye Malligeye", "ಮಲ್ಲಿಗೆಯೇ ಮಲ್ಲಿಗೆಯೇ", "Muthina Haara (Movie)", "ಮುತ್ತಿನ ಹಾರ", "K.S. Chithra", "Hamsalekha", "Hamsalekha", 1990, "Stained Glass Jasmine Garland Mosaic"),
            ("song_043_sundari_sundari_kanasina", "Sundari Sundari Kanasina Taare", "ಸುಂದರಿ ಸುಂದರಿ ಕನಸಿನ ತಾರೆ", "Nee Nanna Gellalare (Movie)", "ನೀ ನನ್ನ ಗೆಲ್ಲಲಾರೆ", "Dr. Rajkumar", "Ilaiyaraaja", "Chi. Udayashankar", 1981, "Retro 80s Disco Electric Vector"),
            ("song_044_ello_hodavu_haleya_nenapugalu", "Ello Hodavu Haleya Nenapugalu", "ಎಲ್ಲೋ ಹೋದವು ಹಳೆಯ ನೆನಪುಗಳು", "Janumada Jodi (Movie)", "ಜನುಮದ ಜೋಡಿ", "Dr. Rajkumar", "V. Manohar", "V. Manohar", 1996, "Melancholic Monochrome Ink Wash Landscape"),
            ("song_045_hrudaya_samudra_kalaki", "Hrudaya Samudra Kalaki", "ಹೃದಯ ಸಮುದ್ರ ಕಲಕಿ", "Ashwamedha (Movie)", "ಅಶ್ವಮೇಧ", "SP Balasubrahmanyam", "Sangeetha Raja", "Chi. Udayashankar", 1990, "Turbulent Indigo Ocean Wave Abstract")
        ]
    },
    # Sheet 6: Hamsalekha Golden Era Magic (90s)
    {
        "key": "songs_sheet_06_hamsalekha_magic",
        "theme": "Hamsalekha Golden Era Magic (90s)",
        "theme_kn": "ನಾದಬ್ರಹ್ಮ ಹಂಸಲೇಖ ಅವರ ಮಾಂತ್ರಿಕ ಗೀತೆಗಳು",
        "style_movement": "80s High-Fantasy, Cyber-Romantic & Pop Chromatics",
        "songs": [
            ("song_046_premalokada_paarijaathave", "Premalokada Paarijaathave", "ಪ್ರೇಮಲೋಕದ ಪಾರಿಜಾತವೇ", "Premaloka (Movie)", "ಪ್ರೇಮಲೋಕ", "SP Balasubrahmanyam", "Hamsalekha", "Hamsalekha", 1987, "80s High-Fantasy Rainbow Glamour Vector"),
            ("song_047_nodu_nanna_kannalli", "Nodu Nanna Kannalli", "ನೋಡು ನನ್ನ ಕಣ್ಣಲ್ಲಿ", "Premaloka (Movie)", "ಪ್ರೇಮಲೋಕ", "SP Balasubrahmanyam & S. Janaki", "Hamsalekha", "Hamsalekha", 1987, "Neon Cyber-Romantic Wireframe Hearts"),
            ("song_048_yelu_swaragala_sangamave", "Yelu Swaragala Sangamave", "ಏಳು ಸ್ವರಗಳ ಸಂಗಮವೇ", "Premaloka (Movie)", "ಪ್ರೇಮಲೋಕ", "SP Balasubrahmanyam", "Hamsalekha", "Hamsalekha", 1987, "Vibrant Psychedelic Rainbow Soundwaves"),
            ("song_049_bombe_heluthaithe_hrudaya", "Bombe Heluthaithe", "ಬೊಂಬೆ ಹೇಳುತೈತೆ", "Hrudaya Haadithu (Movie)", "ಹೃದಯ ಹಾಡಿತು", "SP Balasubrahmanyam", "Upendra Kumar", "Chi. Udayashankar", 1991, "Surreal Storybook Clockwork Dollhouse"),
            ("song_050_chanda_o_chanda_nee_elli_hode", "Chanda O Chanda Nee Elli Hode", "ಚಂದ ಓ ಚಂದ ನೀ ಎಲ್ಲಿ ಹೋದೆ", "Sparsha (Movie)", "ಸ್ಪರ್ಶ", "Hariharan", "Hamsalekha", "Hamsalekha", 2000, "Moonlit Stargazing Paper Cutout Silhouette"),
            ("song_051_sihi_gaali_beesitho", "Sihi Gaali Beesitho", "ಸಿಹಿ ಗಾಳಿ ಬೀಸಿತೋ", "Ranadheera (Movie)", "ರಣಧೀರ", "SP Balasubrahmanyam & S. Janaki", "Hamsalekha", "Hamsalekha", 1988, "Retro Pop Floral Kaleidoscope"),
            ("song_052_o_meghave_meghave", "O Meghave Meghave", "ಓ ಮೇಘವೇ ಮೇಘವೇ", "Ranadheera (Movie)", "ರಣಧೀರ", "SP Balasubrahmanyam", "Hamsalekha", "Hamsalekha", 1988, "Dramatic Thunderhead Cloudscape Woodblock"),
            ("song_053_radhe_ninage_naa_hoova_tande", "Radhe Ninage Naa Hoova Tande", "ರಾಧೆ ನಿನಗೆ ನಾ ಹೂವ ತಂದೆ", "Anjada Gandu (Movie)", "ಅಂಜದ ಗಂಡು", "SP Balasubrahmanyam", "Hamsalekha", "Hamsalekha", 1988, "Stylized Indian Folk Romance Graphic"),
            ("song_054_yaaro_yaaro_nannolage", "Yaaro Yaaro Nannolage", "ಯಾರೋ ಯಾರೋ ನನ್ನೊಳಗೆ", "Chaitrada Premanjali (Movie)", "ಚೈತ್ರದ ಪ್ರೇಮಾಂಜಲಿ", "SP Balasubrahmanyam", "Hamsalekha", "Hamsalekha", 1992, "Infinite Mirror Reflections Surrealism")
        ]
    },
    # Sheet 7: Romantic Rain & Monsoon Melodies
    {
        "key": "songs_sheet_07_monsoon_rain",
        "theme": "Romantic Rain & Monsoon Melodies",
        "theme_kn": "ಮುಂಗಾರು ಮಳೆ ಮತ್ತು ಮಳೆಯ ಮಧುರ ಗೀತೆಗಳು",
        "style_movement": "Impressionist Rainy Window, Studio Ghibli & Japanese Wave",
        "songs": [
            ("song_055_anisuthide_yaako_indu", "Anisuthide Yaako Indu", "ಅನಿಸುತಿದೆ ಯಾಕೋ ಇಂದು", "Mungaru Male (Movie)", "ಮುಂಗಾರು ಮಳೆ", "Sonu Nigam", "Mano Murthy", "Jayanth Kaikini", 2006, "Impressionist Rainy Window With Glowing Streetlights"),
            ("song_056_onde_ondu_aase", "Onde Ondu Aase", "ಒಂದೇ ಒಂದು ಆಸೆ", "Mungaru Male (Movie)", "ಮುಂಗಾರು ಮಳೆ", "Kunal Ganjawala", "Mano Murthy", "Kaviraj", 2006, "Ghibli Raindrop & Sprouting Seedling"),
            ("song_057_mungaru_maleye", "Mungaru Maleye", "ಮುಂಗಾರು ಮಳೆಯೇ", "Mungaru Male (Movie)", "ಮುಂಗಾರು ಮಳೆ", "Sonu Nigam", "Mano Murthy", "Hrudaya Shiva", 2006, "Dramatic Japanese Wave & Rain Woodblock"),
            ("song_058_baanina_haniye_dharegilidu", "Baanina Haniye Dharegilidu Baa", "ಬಾನಿನ ಹನಿಯೇ ಧರೆಗಿಳಿದು ಬಾ", "Beladingala Baale (Movie)", "ಬೆಳದಿಂಗಳ ಬಾಲೆ", "SP Balasubrahmanyam", "Gunasingh", "V. Manohar", 1995, "Minimalist Silver Starlight Silhouette"),
            ("song_059_beladingalaagi_baa", "Beladingalaagi Baa", "ಬೆಳದಿಂಗಳಾಗಿ ಬಾ", "Beladingala Baale (Movie)", "ಬೆಳದಿಂಗಳ ಬಾಲೆ", "S.P. Sailaja", "Gunasingh", "V. Manohar", 1995, "Luminous Paper Moon Cutout Over Sea"),
            ("song_060_tunturu_alli_neera_haadu", "Tunturu Alli Neera Haadu", "ತುಂತುರು ಅಲ್ಲಿ ನೀರ ಹಾಡು", "Amruthavarshini (Movie)", "ಅಮೃತವರ್ಷಿಣಿ", "K.S. Chithra", "Deva", "K. Kalyan", 1997, "Vibrant Watercolor Droplets Symphony"),
            ("song_061_ello_maleyagideyanthe", "Ello Maleyagideyanthe", "ಎಲ್ಲೋ ಮಳೆಯಾಗಿದೆಯಂತೆ", "Manasaare (Movie)", "ಮನಸಾರೆ", "Sonu Nigam", "Mano Murthy", "Jayanth Kaikini", 2009, "Pastel Gouache Flying Umbrellas Dreamscape"),
            ("song_062_ee_sanje_eke_aagide", "Ee Sanje Eke Aagide", "ಈ ಸಂಜೆ ಏಕೆ ಆಗಿದೆ", "Ugramm (Movie)", "ಉಗ್ರಂ", "Anuradha Bhat", "Ravi Basrur", "Chintan Vikas", 2014, "Twilight Dusky Neo-Noir Silhouette"),
            ("song_063_male_nintu_hoda_mele", "Male Nintu Hoda Mele", "ಮಳೆ ನಿಂತು ಹೋದ ಮೇಲೆ", "Milana (Movie)", "ಮಿಲನ", "Shreya Ghoshal", "Mano Murthy", "Jayanth Kaikini", 2007, "Fresh Dewdrop Macro Geometric Vector Art")
        ]
    },
    # Sheet 8: Spiritual, Bhakti, Haridasa & Vachanas
    {
        "key": "songs_sheet_08_spiritual_bhakti",
        "theme": "Spiritual, Bhakti, Haridasa & Vachanas",
        "theme_kn": "ಭಕ್ತಿ, ದಾಸ ಸಾಹಿತ್ಯ ಮತ್ತು ವಚನಗಳು",
        "style_movement": "Sacred Mandalic Gold Stencil & Medieval Linocut",
        "songs": [
            ("song_064_bhagyada_lakshmi_baramma", "Bhagyada Lakshmi Baramma", "ಭಾಗ್ಯದ ಲಕ್ಷ್ಮಿ ಬಾರಮ್ಮ", "Purandara Dasa Kritis", "ಪುರಂದರ ದಾಸ ಕೃತಿಗಳು", "Bhimsen Joshi", "Purandara Dasa", "Purandara Dasa", 1970, "Golden Temple Stencil & Lotus Mandala"),
            ("song_065_tallanisadiru_kandya", "Tallanisadiru Kandya Taalu Manave", "ತಲ್ಲಣಿಸದಿru ಕಂಡ್ಯ ತಾಳು ಮನವೇ", "Kanaka Dasa Kritis", "ಕನಕ ದಾಸ ಕೃತಿಗಳು", "PB Sreenivas", "Kanaka Dasa", "Kanaka Dasa", 1968, "Zen Minimalist Inscribed River Stones"),
            ("song_066_kaayo_shri_gananatha", "Kaayo Shri Gananatha", "ಕಾಯೋ ಶ್ರೀ ಗಣನಾಥ", "Bhakti Taranga", "ಭಕ್ತಿ ತರಂಗ", "Dr. Rajkumar", "Traditional", "Purandara Dasa", 1978, "Geometric Mandalic Ganesha Deity Vector"),
            ("song_067_jagadoddharana_adisidale", "Jagadoddharana Adisidale Yashoda", "ಜಗದೋದ್ಧಾರನಾ ಆಡಿಸಿದಳೆ ಯಶೋದಾ", "Dasa Namana", "ದಾಸ ನಮನ", "M.S. Subbulakshmi", "Purandara Dasa", "Purandara Dasa", 1975, "Mysore Traditional Iconographic Relief"),
            ("song_068_kayakave_kailasa", "Kayakave Kailasa", "ಕಾಯಕವೇ ಕೈಲಾಸ", "Shiva Sharana Vachanamruta", "ವಚನಾಮೃತ", "C. Ashwath", "C. Ashwath", "Jagajjyoti Basavanna", 1982, "Constructivist Hammer & Chisel Sacred Graphic"),
            ("song_069_arive_guru", "Arive Guru", "ಅರಿವೇ ಗುರು", "Allama Prabhu Vachana", "ಅಲ್ಲಮ ಪ್ರಭು ವಚನ", "C. Ashwath", "C. Ashwath", "Allama Prabhu", 1984, "Glowing Cosmic Eye of Wisdom Surrealism"),
            ("song_070_krishna_nee_begane_baro", "Krishna Nee Begane Baro", "ಕೃಷ್ಣಾ ನೀ ಬೇಗನೆ ಬಾರೋ", "Yamuna Kalyani Classical", "ಯಮುನಾ ಕಲ್ಯಾಣಿ", "M. Balamuralikrishna", "Vadiraja Tirtha", "Vadiraja Tirtha", 1973, "Riverbank Flute Silhouette Woodcut"),
            ("song_071_neenyako_ninna_hangyako", "Neenyako Ninna Hangyako", "ನೀನ್ಯಾಕೋ ನಿನ್ನ ಹಂಗ್ಯಾಕೋ", "Kanaka Dasa Pada", "ಕನಕ ದಾಸರ ಪದ", "Bhimsen Joshi", "Kanaka Dasa", "Kanaka Dasa", 1976, "Broken Chains Minimalist Linocut"),
            ("song_072_indenage_govinda", "Indenage Govinda", "ಇಂದೆನಗೆ ಗೋವಿಂದ", "Rayara Sannidhi", "ರಾಯರ ಸನ್ನಿಧಿ", "Dr. Rajkumar", "Vijaya Bhaskar", "Raghavendra Swami Pada", 1980, "Sacred Sacred Golden Ray Aura Mandala")
        ]
    },
    # Sheet 9: Folk, Janapada & Karavali Waves
    {
        "key": "songs_sheet_09_folk_janapada",
        "theme": "Folk, Janapada & Karavali Waves",
        "theme_kn": "ಕರ್ನಾಟಕ ಜನಪದ ಮತ್ತು ಕರಾವಳಿ ಗೀತೆಗಳು",
        "style_movement": "Tribal Gond, Madhubani & Terracotta Graphic",
        "songs": [
            ("song_073_mayadantha_male_bantanna", "Mayadantha Male Bantanna", "ಮಾಯಾದಂಥ ಮಳೆ ಬಂತಣ್ಣ", "Janapada Loka", "ಜನಪದ ಲೋಕ", "C. Ashwath", "Traditional Folk", "Traditional Folk", 1985, "Raw Tribal Gond Animal & Monsoon Clouds"),
            ("song_074_munjane_eddu_gidagala", "Munjane Eddu Gidagala Nodidare", "ಮುಂಜಾನೆ ಎದ್ದು ಗಿಡಗಳ ನೋಡಿದರೆ", "Folk Melodies", "ಜನಪದ ಸುಗ್ಗಿ", "B.R. Chaya", "Traditional Folk", "Traditional Folk", 1986, "Terracotta Rural Village Woodcut"),
            ("song_075_gidamoolike_ganda", "Gidamoolike Ganda", "ಗಿಡಮೂಲಿಕೆ ಗಂಡ", "Janapada Siri", "ಜನಪದ ಸಿರಿ", "Goriganahalli Madappa", "Traditional Folk", "Traditional Folk", 1983, "Colorful Madhubani Jungle Flora & Fauna"),
            ("song_076_kuri_kayo_kuruba", "Kuri Kayo Kuruba", "ಕುರಿ ಕಾಯೋ ಕುರುಬ", "Janapada Geetegalu", "ಜನಪದ ಗೀತೆಗಳು", "Appagere Thimmaraju", "Traditional Folk", "Traditional Folk", 1988, "Stylized Shepherd & Rolling Hills Linocut"),
            ("song_077_karavali_teerada_kogile", "Karavali Teerada Kogile", "ಕರಾವಳಿ ತೀರದ ಕೋಗಿಲೆ", "Karavali Geethegalu", "ಕರಾವಳಿ ಗೀತೆಗಳು", "Ramesh Chandra", "Coastal Folk", "Traditional Folk", 1992, "Coconut Palm Sunset Beach Silhouette"),
            ("song_078_doni_saagali_munde_hogali", "Doni Saagali Munde Hogali", "ದೋಣಿ ಸಾಗಲಿ ಮುಂದೆ ಹೋಗಲಿ", "K.S.Na Kavya", "ಕೆ.ಎಸ್.ನ ಕಾವ್ಯ", "C. Ashwath", "C. Ashwath", "K.S. Narasimhaswamy", 1980, "Paper Boat Origami Geometric Riverscape"),
            ("song_079_mysore_mallige_hadu", "Mysore Mallige", "ಮೈಸೂರು ಮಲ್ಲಿಗೆ", "Mysore Mallige (Album)", "ಮೈಸೂರು ಮಲ್ಲಿಗೆ", "Ratnamala Prakash", "C. Ashwath", "K.S. Narasimhaswamy", 1981, "Romantic Botanical Jasmine Lithograph"),
            ("song_080_arerere_bantu_nodu_kambala", "Arerere Bantu Nodu Kambala", "ಅರೆರೆರೆ ಬಂತು ನೋಡು ಕಂಬಳ", "Karavali Siri", "ಕರಾವಳಿ ಸಿರಿ", "Janapada Troupe", "Coastal Traditional", "Traditional Tulu/Kannada", 1989, "Mud-Splashed Dynamic Racing Buffalo Vector"),
            ("song_081_ello_jogappa_ninnaramane", "Ello Jogappa Ninnaramane", "ಎಲ್ಲೋ ಜೋಗಪ್ಪ ನಿನ್ನರಮನೆ", "Jogi (Movie)", "ಜೋಗಿ", "Prem & Gurukiran", "Gurukiran", "Prem", 2005, "Mystic Saffron Nomad & Tamburi Linocut")
        ]
    },
    # Sheet 10: Upendra & 90s Cult Eccentricities
    {
        "key": "songs_sheet_10_upendra_cult",
        "theme": "Upendra & 90s Cult Eccentricities",
        "theme_kn": "ಉಪೇಂದ್ರ ಮತ್ತು ೯೦ರ ದಶಕದ ಕಲ್ಟ್ ಗೀತೆಗಳು",
        "style_movement": "Pop Art Comic Strip, Glitch Collage & Neon Noir",
        "songs": [
            ("song_082_en_kathe_helali_nannola", "En Kathe Helali Nannola", "ಎನ್ ಕತೆ ಹೇಳಲಿ ನನ್ನೋಳ", "A (Movie)", "ಎ", "Upendra", "Gurukiran", "Upendra", 1998, "Glitch Art Psychological Collage"),
            ("song_083_maari_kannu_hori_kannu", "Maari Kannu Hori Kannu", "ಮಾರಿ ಕಣ್ಣು ಹೋರಿ ಕಣ್ಣು", "A (Movie)", "ಎ", "Sadhu Kokila & Upendra", "Gurukiran", "Upendra", 1998, "Surrealist Eyeball Pop Art Stare"),
            ("song_084_preethse_preethse", "Preethse Preethse", "ಪ್ರೀತ್ಸೆ ಪ್ರೀತ್ಸೆ", "Preethse (Movie)", "ಪ್ರೀತ್ಸೆ", "Hemanth Kumar", "Hamsalekha", "K. Kalyan", 2000, "Retro 90s Neon Glow Synth Silhouette"),
            ("song_085_uppittu_saaku_nange", "Uppittu Saaku Nange", "ಉಪ್ಪಿಟ್ಟು ಸಾಕು ನಂಗೆ", "Upendra (Movie)", "ಉಪೇಂದ್ರ", "Upendra", "Gurukiran", "Upendra", 1999, "Pop Art Comic Strip / Roy Lichtenstein"),
            ("song_086_tarle_nan_maga_title", "Tarle Nan Maga", "ತರಲೆ ನನ್ ಮಗ", "Tarle Nan Maga (Movie)", "ತರಲೆ ನನ್ ಮಗ", "Mano", "Hamsalekha", "Upendra", 1992, "Wacky Cartoon Caricature & Mischief"),
            ("song_087_jaya_jaya_jaya_hanumanta", "Jaya Jaya Jaya Hanumanta", "ಜಯ ಜಯ ಜಯ ಹನುಮಂತ", "Gauri Ganesha (Movie)", "ಗೌರಿ ಗಣೇಶ", "SP Balasubrahmanyam", "Rajan-Nagendra", "Chi. Udayashankar", 1991, "Retro Indian Comic Book Cover Art"),
            ("song_088_kothigalu_saar_kothigalu", "Kothigalu Saar Kothigalu", "ಕೊತಿಗಳು ಸಾರ್ ಕೊತಿಗಳು", "Kothigalu Saar Kothigalu (Movie)", "ಕೊತಿಗಳು ಸಾರ್ ಕೊತಿಗಳು", "Hemanth Kumar", "Hamsalekha", "Hamsalekha", 2001, "Three Wise Monkeys Stylized Pop Vector"),
            ("song_089_super_star_nannobbane", "Super Star Nannobbane", "ಸೂಪರ್ ಸ್ಟಾರ್ ನನ್ನೊಬ್ಬನೇ", "Upendra (Movie)", "ಉಪೇಂದ್ರ", "Upendra", "Gurukiran", "Upendra", 1999, "Flashy Metallic Y2K Graphic Vector"),
            ("song_090_love_madbardu_andbitta", "Love Madbardu Andbitta", "ಲವ್ ಮಾಡ್ಬಾರ್ದು ಅಂದ್ಬಿಟ್ಟ", "Om (Movie)", "ಓಂ", "Dr. Rajkumar", "Hamsalekha", "Hamsalekha", 1995, "Grunge Blackboard Chalk & Heart Graffiti")
        ]
    },
    # Sheet 11: 2000s Romance & Youth Anthems
    {
        "key": "songs_sheet_11_2000s_youth",
        "theme": "2000s Romance & Youth Anthems",
        "theme_kn": "೨೦೦೦ರ ದಶಕದ ಯುವ ಪ್ರೇಮ ತರಂಗಗಳು",
        "style_movement": "Y2K Vibrant Vector, Candy Colors & Pastel Dreamscape",
        "songs": [
            ("song_091_neenene_nanna_saviganasu", "Neenene Nanna Saviganasu", "ನೀನೇನೆ ನನ್ನ ಸವಿಗನಸು", "100% Love (Album)", "ನೂರು ಪ್ರತಿಶತ ಪ್ರೇಮ", "Sonu Nigam", "Gurukiran", "Kaviraj", 2005, "Candy Color Y2K Pop Swirls"),
            ("song_092_milana_milana_idu", "Milana Milana Idu Olavina Milana", "ಮಿಲನ ಮಿಲನ ಇದು ಒಲವಿನ ಮಿಲನ", "Milana (Movie)", "ಮಿಲನ", "Sonu Nigam", "Mano Murthy", "Jayanth Kaikini", 2007, "Sunrise Over Clouds Watercolor Vector"),
            ("song_093_kanninchinali_kanasugala", "Kanninchinali Kanasugala", "ಕಣ್ಣಿಂಚಿನಲ್ಲಿ ಕನಸುಗಳ", "Gaalipata (Movie)", "ಗಾಳಿಪಟ", "Sonu Nigam", "Mano Murthy", "Jayanth Kaikini", 2008, "Flying Paper Kites in Blue Sky Vector"),
            ("song_094_aaha_entha_savimaathu", "Aaha Entha Savimaathu", "ಆಹಾ ಎಂಥ ಸವಿಮಾತು", "Cheluvina Chittara (Movie)", "ಚೆಲುವಿನ ಚಿತ್ತಾರ", "Kunal Ganjawala", "Mano Murthy", "S. Narayan", 2007, "Pastel Storybook Melody Vignette"),
            ("song_095_madhura_ee_mouna", "Madhura Ee Mouna", "ಮಧುರ ಈ ಮೌನ", "Nenapirali (Movie)", "ನೆನಪಿರಲಿ", "Chetan Sosca", "Hamsalekha", "Hamsalekha", 2005, "Violet Twilight Gradient Minimalist Lines"),
            ("song_096_nagu_nagu_nagu", "Nagu Nagu Nagu", "ನಗು ನಗು ನಗು", "Appu (Movie)", "ಅಪ್ಪು", "Puneeth Rajkumar", "Gurukiran", "Upendra", 2002, "Electric Yellow Emoji Pop & Beats"),
            ("song_097_bombe_heluthaite_maththe", "Bombe Heluthaite", "ಬೊಂಬೆ ಹೇಳುತೈತೆ", "Raajakumara (Movie)", "ರಾಜಕುಮಾರ", "Vijay Prakash", "V. Harikrishna", "Santosh Ananddram", 2017, "Heritage Golden Pillar & Family Silhouette"),
            ("song_098_kudukara_sangha", "Kudukara Sangha", "ಕುಡುಕರ ಸಂಘ", "Duniya (Movie)", "ದುನಿಯಾ", "V. Manohar", "V. Sridhar", "Yogaraj Bhat", 2007, "Urban Slum Gritty Linocut Graphic"),
            ("song_099_o_gelathi_nannolave", "O Gelathi Nannolave", "ಓ ಗೆಳತಿ ನನ್ನೊಲವೇ", "Cheluvina Chittara (Movie)", "ಚೆಲುವಿನ ಚಿತ್ತಾರ", "Chetan Sosca", "Mano Murthy", "S. Narayan", 2007, "Rural Sunset Bicycle Silhouette")
        ]
    },
    # Sheet 12: Modern Pan-Indian Cinematic Powerhouses
    {
        "key": "songs_sheet_12_pan_indian_epics",
        "theme": "Modern Pan-Indian Cinematic Powerhouses",
        "theme_kn": "ಪ್ಯಾನ್-ಇಂಡಿಯನ್ ದೃಶ್ಯ ಮಹಾಕಾವ್ಯ ಗೀತೆಗಳು",
        "style_movement": "Bioluminescent Forest, Heavy Metal Gold Dust & Lightning Noir",
        "songs": [
            ("song_100_singara_siriye", "Singara Siriye", "ಸಿಂಗಾರ ಸಿರಿಯೇ", "Kantara (Movie)", "ಕಾಂತಾರ", "Vijay Prakash & Ananya Bhat", "B. Ajaneesh Loknath", "Pramod Maravanthe", 2022, "Sacred Bioluminescent Forest Folk Art"),
            ("song_101_varaha_roopam_daiva", "Varaha Roopam Daiva Varishtam", "ವರಾಹ ರೂಪಂ", "Kantara (Movie)", "ಕಾಂತಾರ", "Sai Vignesh", "B. Ajaneesh Loknath", "Shashiraj Kavoor", 2022, "Sacred Mystic Daiva Fiery Iconography"),
            ("song_102_salaam_rocky_bhai", "Salaam Rocky Bhai", "ಸಲಾಂ ರಾಕಿ ಭಾಯ್", "K.G.F: Chapter 1 (Movie)", "ಕೆ.ಜಿ.ಎಫ್ ೧", "Vijay Prakash & Chorus", "Ravi Basrur", "Kinnal Raj", 2018, "Heavy Metal Gold Ore Typography & Smoke"),
            ("song_103_dheera_dheera", "Dheera Dheera", "ಧೀರಾ ಧೀರಾ", "K.G.F: Chapter 1 (Movie)", "ಕೆ.ಜಿ.ಎಫ್ ೧", "Ananya Bhat", "Ravi Basrur", "Ravi Basrur", 2018, "Fiery Golden Dust Sunburst Vector"),
            ("song_104_toofan", "Toofan", "ತೂಫಾನ್", "K.G.F: Chapter 2 (Movie)", "ಕೆ.ಜಿ.ಎಫ್ ೨", "Brijesh Shandilya & Chorus", "Ravi Basrur", "Varadaraj Chikkaballapura", 2022, "High-Contrast Lightning & Heavy Anvil Noir"),
            ("song_105_mehabooba", "Mehabooba", "ಮೆಹಬೂಬಾ", "K.G.F: Chapter 2 (Movie)", "ಕೆ.ಜಿ.ಎಫ್ ೨", "Ananya Bhat", "Ravi Basrur", "Kinnal Raj", 2022, "Candlelit Smokey Art Deco Silhouette"),
            ("song_106_sahore_kannadiga", "Sahore Kannadiga", "ಸಾಹೋರೆ ಕನ್ನಡಿಗ", "Veera Kannadiga (Movie)", "ವೀರ ಕನ್ನಡಿಗ", "Udit Narayan", "Chakri", "Hamsalekha", 2004, "Ancient War Drum & Spear Vector"),
            ("song_107_sakhi_sakhi_o_nanna", "Sakhi Sakhi O Nanna Navile", "ಸಖಿ ಸಖಿ ಓ ನನ್ನ ನವಿಲೇ", "Pop Single", "ಕನ್ನಡ ಪಾಪ್", "Sanjith Hegde", "Charan Raj", "Nagarjun Sharma", 2021, "Psychedelic Peacock Feather Mandala"),
            ("song_108_bande_bitta_nodi_charlie", "Bande Bitta Nodi Charlie", "ಬಂದೇ ಬಿಟ್ಟ ನೋಡಿ ಚಾರ್ಲಿ", "777 Charlie (Movie)", "೭೭೭ ಚಾರ್ಲಿ", "Nobin Paul", "Nobin Paul", "Nagarjun Sharma", 2022, "Heartwarming Children's Book Storybook Illustration")
        ]
    },
    # Sheet 13: Soulful Contemporary Ballads & Folk Fusion
    {
        "key": "songs_sheet_13_contemporary_ballads",
        "theme": "Soulful Contemporary Ballads & Folk Fusion",
        "theme_kn": "ಸಮಕಾಲೀನ ಭಾವಸ್ಪರ್ಶಿ ಮತ್ತು ಫ್ಯೂಷನ್ ಗೀತೆಗಳು",
        "style_movement": "Ocean Wave Cutouts, Wandering Bard Woodcuts & 8-Bit Pixel",
        "songs": [
            ("song_109_sapta_saagaradaache_ello_title", "Sapta Saagaradaache Ello Title Track", "ಸಪ್ತ ಸಾಗರದಾಚೆ ಎಲ್ಲೋ", "Sapta Saagaradaache Ello (Movie)", "ಸಪ್ತ ಸಾಗರದಾಚೆ ಎಲ್ಲೋ", "Kapil Kapilan", "Charan Raj", "Dhananjay Ranjan", 2023, "Deep Ocean Cyan Wave Paper Cutout"),
            ("song_110_kanasina_kadalalli", "Kanasina Kadalalli", "ಕನಸಿನ ಕಡಲಲ್ಲಿ", "SSE Side B (Movie)", "ಸಪ್ತ ಸಾಗರದಾಚೆ ಎಲ್ಲೋ ಭಾಗ ಬಿ", "Sanjith Hegde", "Charan Raj", "Dhananjay Ranjan", 2023, "Labyrinth of Blue Moonlight Vector"),
            ("song_111_sanje_vele_surya_mulugo", "Sanje Vele Surya Mulugo", "ಸಂಜೆ ವೇಳೆ ಸೂರ್ಯ ಮುಳುಗೋ", "Raghu Dixit Project", "ರಘು ದೀಕ್ಷಿತ್ ಪ್ರಾಜೆಕ್ಟ್", "Raghu Dixit", "Raghu Dixit", "Traditional / Shishunala Sharifa", 2010, "Vibrant Fusion Folk Silhouette & Lungi Art"),
            ("song_112_lokada_kaalaji_madutheeni", "Lokada Kaalaji Madutheeni", "ಲೋಕದ ಕಾಳಜಿ", "Shishunala Sharifa Classics", "ಶಿಶುನಾಳ ಶರೀಫ ಗೀತೆಗಳು", "Raghu Dixit", "Raghu Dixit", "Santa Shishunala Sharifa", 2010, "Ektara Wandering Mystic Bard Linocut"),
            ("song_113_gudugudiya_sedi_nodu", "Gudugudiya Sedi Nodu", "ಗುಡುಗುಡಿಯ ಸೇದಿ ನೋಡು", "Santa Shishunala Sharifa (Movie)", "ಸಂತ ಶಿಶುನಾಳ ಶರೀಫ", "C. Ashwath", "C. Ashwath", "Santa Shishunala Sharifa", 1990, "Swirling Mystic Smoke & Hookah Abstract"),
            ("song_114_marali_manasaagide", "Marali Manasaagide", "ಮರಳಿ ಮನಸಾಗಿದೆ", "Gentleman (Movie)", "ಜೆಂಟಲ್‌ಮನ್", "Sanjith Hegde & C.R. Bobby", "B. Ajaneesh Loknath", "Nagarjun Sharma", 2020, "Floating Dream Bubble Pastel Shapes"),
            ("song_115_hangover_nan_talege", "Hangover Nan Talege", "ಹ್ಯಾಂಗ್ ಓವರ್", "Youth Single", "ಯೂತ್ ಸಿಂಗಲ್", "Chandan Shetty", "Chandan Shetty", "Chandan Shetty", 2018, "8-Bit Retro Arcade Pixel Graphic"),
            ("song_116_kavaludaari_teerada_payana", "Kavaludaari Teerada Payana", "ಕವಲುದಾರಿ ತೀರದ ಪಯಣ", "Kavaludaari (Movie)", "ಕವಲುದಾರಿ", "Siddhartha Belmannu", "Charan Raj", "Kiran Kaverappa", 2019, "1970s Highway Film Noir Graphic"),
            ("song_117_bell_bottom_gammattu", "Bell Bottom Gammattu", "ಬೆಲ್ ಬಾಟಮ್ ಗಮ್ಮತ್ತು", "Bell Bottom (Movie)", "ಬೆಲ್ ಬಾಟಮ್", "Raghu Dixit", "B. Ajaneesh Loknath", "Yogaraj Bhat", 2019, "1970s Polka Dot Disco Vector Pop")
        ]
    },
    # Sheet 14: Classical Carnatic & Raga Milestones
    {
        "key": "songs_sheet_14_classical_ragas",
        "theme": "Classical Carnatic & Raga Milestones",
        "theme_kn": "ಕರ್ನಾಟಕ ಶಾಸ್ತ್ರೀಯ ಮತ್ತು ರಾಗ ರತ್ನಗಳು",
        "style_movement": "Celestial Soundwaves, Tanjore Gold Inlay & Swara Geometry",
        "songs": [
            ("song_118_naadamaya_ee_lokavella", "Naadamaya Ee Lokavella", "ನಾದಮಯ ಈ ಲೋಕವೆಲ್ಲಾ", "Jeevana Chaitra (Movie)", "ಜೀವನ ಚೈತ್ರ", "Dr. Rajkumar", "Upendra Kumar", "Chi. Udayashankar", 1992, "Flowing Celestial Sound Waves & Golden Aura"),
            ("song_119_shankarabharanam_kannada_kritis", "Shankarabharanam Kannada Kritis", "ಶಂಕರಾಭರಣಂ ಕೃತಿಗಳು", "Classical Carnatic", "ಶಾಸ್ತ್ರೀಯ ಸಂಗೀತ", "M. Balamuralikrishna", "Carnatic Trinity", "Classical Kritis", 1979, "Nataraja Cosmic Dance Geometric Vector"),
            ("song_120_maamavathu_shri_saraswathi", "Maamavathu Shri Saraswathi", "ಮಾಮವತು ಶ್ರೀ ಸರಸ್ವತಿ", "Mysore Carnatic Heritage", "ಮೈಸೂರು ಶಾಸ್ತ್ರೀಯ ಪರಂಪರೆ", "M.S. Subbulakshmi", "Mysore Vasudevachar", "Mysore Vasudevachar", 1965, "Sacred Veena & Celestial White Swan"),
            ("song_121_thaaye_yashoda_kritis", "Thaaye Yashoda", "ತಾಯೇ ಯಶೋದಾ", "Carnatic Classics", "ಶಾಸ್ತ್ರೀಯ ಕೃತಿಗಳು", "Sudha Ragunathan", "Oothukkadu Venkata Kavi", "Traditional", 1985, "Tanjore Golden Foil Inlay Painting"),
            ("song_122_paavamana_jagada_praana", "Paavamana Jagada Praana", "ಪಾವಮಾನ ಜಗದ ಪ್ರಾಣ", "Madhwa Haridasa Kritis", "ಹರಿದಾಸ ಕೃತಿಗಳು", "Bhimsen Joshi", "Purandara Dasa", "Vijaya Dasa", 1974, "Celestial Wind & Lotus Mandala"),
            ("song_123_nalinakanthi_ragalapane", "Nalinakanthi Ragalapane", "ನಳಿನಕಾಂತಿ ರಾಗಾಲಾಪನೆ", "Raga Sudha", "ರಾಗ ಸುಧಾ", "K.J. Yesudas", "Classical", "Swara Heritage", 1980, "Geometric Swara Matrix Line Art"),
            ("song_124_venkatachala_nilayam", "Venkatachala Nilayam", "ವೆಂಕಟಾಚಲ ನಿಲಯಂ", "Purandara Kritis", "ಪುರಂದರ ಕೃತಿಗಳು", "Bhimsen Joshi", "Purandara Dasa", "Purandara Dasa", 1972, "Tirumala Seven Hills Stylized Woodblock"),
            ("song_125_pillangoviya_chelva_krishnana", "Pillangoviya Chelva Krishnana", "ಪಿಳ್ಳಂಗೋವಿಯ ಚೆಲ್ವ ಕೃಷ್ಣನ", "Dasa Namana", "ದಾಸ ನಮನ", "PB Sreenivas", "Purandara Dasa", "Purandara Dasa", 1970, "Flute Melody Spiral Line Art Graphic"),
            ("song_126_sharanu_sharanayya_benaka", "Sharanu Sharanayya Benaka", "ಶರಣು ಶರಣಯ್ಯ ಬೆನಕ", "Vinayaka Geethegalu", "ವಿನಾಯಕ ಗೀತೆಗಳು", "SP Balasubrahmanyam", "Kanaka Dasa", "Kanaka Dasa", 1980, "Minimalist Ganesha Sacred Geometry Vector")
        ]
    },
    # Sheet 15: Playful Duets, Grooves & Retro Beats
    {
        "key": "songs_sheet_15_retro_grooves",
        "theme": "Playful Duets, Grooves & Retro Beats",
        "theme_kn": "ಕುಣಿವ ತಾಳ, ಚುರುಕು ಯುಗಳ ಗೀತೆಗಳು",
        "style_movement": "Rangoli Patterns, 70s Disco Vectors & Pop Mascot Art",
        "songs": [
            ("song_127_ellamma_rangoli_cheluve", "Ellamma Rangoli Cheluve", "ಎಲ್ಲಮ್ಮ ರಂಗೋಲಿ", "Retro Classic Duet", "ರಂಗೋಲಿ ಗೀತೆಗಳು", "SP Balasubrahmanyam & S. Janaki", "G.K. Venkatesh", "Chi. Udayashankar", 1978, "Intricate White & Ochre Rangoli Geometry"),
            ("song_128_shankar_guru_disco", "Shankar Guru Disco Beat", "ಶಂಕರ್ ಗುರು ಡ್ಯಾನ್ಸ್", "Shankar Guru (Movie)", "ಶಂಕರ್ ಗುರು", "Dr. Rajkumar", "Upendra Kumar", "Chi. Udayashankar", 1978, "70s Psychedelic Mirror Ball & Bellbottoms"),
            ("song_129_amma_naan_ninna_kanda", "Amma Naan Ninna Kanda", "ಅಮ್ಮಾ ನಾನ್ ನಿನ್ನ ಕಂದ", "Tayiya Madilu (Movie)", "ತಾಯಿಯ ಮಡಿಲು", "PB Sreenivas", "G.K. Venkatesh", "Chi. Udayashankar", 1970, "Mother & Child Minimalist Tender Line Drawing"),
            ("song_130_silli_lalli_title_song", "Silli Lalli Title Song", "ಸಿಲ್ಲಿ ಲಲ್ಲಿ", "Television Classic", "ದೂರದರ್ಶನ ಕ್ಲಾಸಿಕ್", "Rajesh Krishnan", "V. Manohar", "Sihi Kahi Chandru", 2003, "Quirky Comic Strip Newspaper Humor"),
            ("song_131_appa_amma_preethi", "Appa Amma Preethi", "ಅಪ್ಪ ಅಮ್ಮ ಪ್ರೀತಿ", "Family Classic (Album)", "ಕುಟುಂಬ ಗೀತೆಗಳು", "S. Janaki", "Hamsalekha", "Hamsalekha", 1994, "Golden Tree of Life Folk Illustration"),
            ("song_132_ram_ram_raghupathi", "Ram Ram Raghupathi", "ರಾಮ್ ರಾಮ್ ರಘುಪತಿ", "Folk Devotional Fusion", "ಜನಪದ ಭಕ್ತಿ", "C. Ashwath", "C. Ashwath", "Traditional", 1987, "Saffron Woodcut Graphic Chariot"),
            ("song_133_bande_eddalu_kannada_naadu", "Bande Eddalu Kannada Naadu", "ಬಂಡೆ ಎದ್ದಳು ಕನ್ನಡ ನಾಡು", "Veera Parampare", "ವೀರ ಪರಂಪರೆ", "Dr. Rajkumar", "G.K. Venkatesh", "Hunsur Krishnamurthy", 1968, "Warrior Chariot Graphic Silhouette"),
            ("song_134_bombaat_kaara_bangalore", "Bombaat Kaara Bangalore", "ಬೊಂಬಾಟ್ ಕಾರ", "Bangalore Street Beats", "ಬೆಂಗಳೂರು ಗೀತೆಗಳು", "All.OK", "All.OK", "All.OK", 2017, "Spicy Retro Mascot Pop Art Graphic"),
            ("song_135_aakashadinda_dharegilida", "Aakashadinda Dharegilida Taare", "ಆಕಾಶದಿಂದ ಧರೆಗಿಳಿದ ತಾರೆ", "Chandanada Gombe (Movie)", "ಚಂದನದ ಗೊಂಬೆ", "PB Sreenivas", "Rajan-Nagendra", "Chi. Udayashankar", 1979, "Falling Shooting Star Abstract Surrealism")
        ]
    },
    # Sheet 16: Sugama Sangeetha & Literary Poetry
    {
        "key": "songs_sheet_16_sugama_sangeetha",
        "theme": "Sugama Sangeetha & Literary Poetry",
        "theme_kn": "ಸುಗಮ ಸಂಗೀತ ಮತ್ತು ಕನ್ನಡ ಕಾವ್ಯ ಸೌರಭ",
        "style_movement": "Calligraphic Watercolor, Stargazer Line Art & Woodblock",
        "songs": [
            ("song_136_baaro_sadhanakerige", "Baaro Sadhanakerige", "ಬಾರೋ ಸಾಧನಕೇರಿಗೆ", "Bendre Kavya (Album)", "ಬೇಂದ್ರೆ ಕಾವ್ಯ", "C. Ashwath", "C. Ashwath", "Da Ra Bendre", 1982, "Mystic Lake & Sacred Banyan Tree Watercolor"),
            ("song_137_kuniyonu_baara_kuniyonu_baa", "Kuniyonu Baara Kuniyonu Baa", "ಕುಣಿಯೋಣು ಬಾರಾ ಕುಣಿಯೋಣು ಬಾ", "Bendre Gitanjali", "ಬೇಂದ್ರೆ ಗೀತಾಂಜಲಿ", "Ratnamala Prakash", "Mysore Ananthaswamy", "Da Ra Bendre", 1980, "Joyful Dancing Silhouettes Under Twilight"),
            ("song_138_aanandamaya_ee_jagahrudaya", "Aanandamaya Ee Jagahrudaya", "ಆನಂದಮಯ ಈ ಜಗಹೃದಯ", "Kuvempu Gana Siri", "ಕುವೆಂಪು ಗಾನ ಸಿರಿ", "PB Sreenivas", "Mysore Ananthaswamy", "Rashtrakavi Kuvempu", 1976, "Cosmic Harmony Golden Spiral Vector"),
            ("song_139_hacchevu_kannadada_deepa", "Hacchevu Kannadada Deepa", "ಹಚ್ಚೇವು ಕನ್ನಡದ ದೀಪ", "Kannada Deepa", "ಕನ್ನಡದ ದೀಪ", "C. Ashwath & Chorus", "C. Ashwath", "D.S. Karki", 1980, "Flaming Sacred Diya Lamp Graphic Silhouette"),
            ("song_140_neredide_manadali_kavitheya", "Neredide Manadali Kavitheya Habba", "ನೆರೆದಿದೆ ಮನದಲಿ ಕವಿತೆಯ ಹಬ್ಬ", "Sugama Sangeetha Siri", "ಸುಗಮ ಸಂಗೀತ ಸಿರಿ", "Shimoga Subbanna", "C. Ashwath", "G.S. Shivarudrappa", 1984, "Poetry Scroll & Golden Feather Pen Vector"),
            ("song_141_naanu_badavi_aata_badava", "Naanu Badavi Aata Badava", "ನಾನು ಬಡವಿ ಆಟ ಬಡವ", "Bendre Smruti", "ಬೇಂದ್ರೆ ಸ್ಮೃತಿ", "C. Ashwath", "C. Ashwath", "Da Ra Bendre", 1983, "Humble Village Hut Monochrome Linocut"),
            ("song_142_endendigu_naavibbare", "Endendigu Naavibbare", "ಎಂದೆಂದಿಗೂ ನಾವಿಬ್ಬರೇ", "Bhavabindu (Album)", "ಭಾವಬಿಂದು", "P. Susheela", "Mysore Ananthaswamy", "K.S. Narasimhaswamy", 1979, "Entwined Lovebirds Woodcut Silhouette"),
            ("song_143_mugila_maarige_ragada_ratiyu", "Mugila Maarige Ragada Ratiyu", "ಮುಗಿಲ ಮಾರಿಗೆ ರಾಗದ ರತಿಯು", "Kuvempu Sangita", "ಕುವೆಂಪು ಸಂಗೀತ", "Shimoga Subbanna", "C. Ashwath", "Rashtrakavi Kuvempu", 1981, "Sunset Dusk Cloud Shapes Abstract"),
            ("song_144_moodala_kunigal_kere", "Moodala Kunigal Kere", "ಮೂಡಲ ಕುಣಿಗಲ್ ಕೆರೆ", "Janapada Classical", "ಕುಣಿಗಲ್ ಕೆರೆ", "Traditional / C. Ashwath", "C. Ashwath", "Traditional Folk", 1980, "Kunigal Lake & Flying Cranes Japanese Woodblock")
        ]
    },
    # Sheet 17: Indie Renaissance & Modern Waves (2010s–2024)
    {
        "key": "songs_sheet_17_indie_waves",
        "theme": "Indie Renaissance & Modern Waves (2010s–2024)",
        "theme_kn": "ಕನ್ನಡ ಇಂಡಿ ಕ್ರಾಂತಿ ಮತ್ತು ಹೊಸ ಅಲೆಯ ಗೀತೆಗಳು",
        "style_movement": "Rural Charcoal, Minimalist Vector & Doodle Illustration",
        "songs": [
            ("song_145_thithi_village_ballad", "Thithi Village Ballad", "ತಿತಿ ಹಾಡು", "Thithi (Movie)", "ತಿತಿ", "Cast of Thithi", "Traditional", "Ere Gowda", 2015, "Raw Hand-Drawn Rural Charcoal Graphic"),
            ("song_146_rama_rama_re_chakra", "Rama Rama Re Chariot Theme", "ರಾಮ ರಾಮ ರೇ ಚಕ್ರ", "Rama Rama Re... (Movie)", "ರಾಮ ರಾಮ ರೇ...", "Vasuki Vaibhav", "Nobin Paul", "D. Satyaprakash", 2016, "Desert Road & Wheel Minimalist Vector"),
            ("song_147_kada_gadingana_gadinalli", "Kada Gadingana Gadinalli", "ರಂಗಿತರಂಗ ಅಕಾಲಿಕ", "RangiTaranga (Movie)", "ರಂಗಿತರಂಗ", "Anup Bhandari", "Anup Bhandari", "Anup Bhandari", 2015, "Monsoon Rainforest Supernatural Fog Vector"),
            ("song_148_bel_belagge_kannu_bittare", "Bel Belagge Kannu Bittare", "ಬೆಳ್ ಬೆಳಗ್ಗೆ ಕಣ್ಣು ಬಿಟ್ಟರೆ", "Kirik Party (Movie)", "ಕಿರಿಕ್ ಪಾರ್ಟಿ", "Chintan Vikas", "B. Ajaneesh Loknath", "Anup Bhandari", 2016, "College Campus Doodle Illustration"),
            ("song_149_kattu_kathe_malpe", "Kattu Kathe Malpe", "ಕಟ್ಟು ಕಥೆ", "Ulidavaru Kandanthe (Movie)", "ಉಳಿದವರು ಕಂಡಂತೆ", "Vijay Prakash", "B. Ajaneesh Loknath", "Rakshit Shetty", 2014, "Malpe Fishing Boats & Arabian Sea Woodcut"),
            ("song_150_maleye_maleye_dia", "Maleye Maleye", "ಮಳೆಯೇ ಮಳೆಯೇ", "Dia (Movie)", "ದಿಯಾ", "Sanjith Hegde", "B. Ajaneesh Loknath", "Dhananjay Ranjan", 2020, "Minimalist Train Window Droplet Art"),
            ("song_151_daariya_konege_godhi_banna", "Daariya Konege", "ದಾರಿಯ ಕೊನೆಗೆ", "Godhi Banna Sadharana Mykattu (Movie)", "ಗೋಧಿ ಬಣ್ಣ ಸಾಧಾರಣ ಮೈಕಟ್ಟು", "Siddhartha Belmannu", "Charan Raj", "Jayanth Kaikini", 2016, "Winding Bengaluru Alleyway Linocut"),
            ("song_152_motte_heggade_ballad", "Motte Heggade Ballad", "ಮೋಟೆ ಹೆಗ್ಗಡೆ", "Ondu Motteya Kathe (Movie)", "ಒಂದು ಮೊಟ್ಟೆಯ ಕಥೆ", "Raj B. Shetty", "Midhun Mukundan", "Raj B. Shetty", 2017, "Quirky Bald Silhouette Comic Art"),
            ("song_153_jaya_bharata_symphony", "Jaya Bharata Jananiya Modern Symphony", "ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ ಸಿಂಫನಿ", "State Anthem Modern Orchestration", "ನಾಡಗೀತೆ ಸಿಂಫನಿ", "Karnataka State Choir", "Charan Raj", "Rashtrakavi Kuvempu", 2024, "Glowing Symphony Sound Waves & Karnataka Map")
        ]
    }
]

songs_list = []
for sheet in all_sheets:
    sheet_key = sheet["key"]
    for s_tuple in sheet["songs"]:
        sid, title, title_kn, album, album_kn, singer, composer, lyricist, year, style = s_tuple
        song_obj = {
            "id": sid,
            "sheet": sheet_key,
            "theme": sheet["theme"],
            "theme_kn": sheet["theme_kn"],
            "style_movement": sheet["style_movement"],
            "title": title,
            "title_kn": title_kn,
            "album_or_movie": album,
            "album_or_movie_kn": album_kn,
            "singer": singer,
            "composer": composer,
            "lyricist": lyricist,
            "year": year,
            "style": style,
            "poster_image": f"songs/individual/{sid}.png",
            "sheet_image": f"songs/sheets/{sheet_key}.png"
        }
        songs_list.append(song_obj)

full_data = {
    "total_songs": len(songs_list),
    "total_sheets": len(all_sheets),
    "sheets": [
        {
            "key": s["key"],
            "theme": s["theme"],
            "theme_kn": s["theme_kn"],
            "style_movement": s["style_movement"],
            "song_ids": [st[0] for st in s["songs"]]
        }
        for s in all_sheets
    ],
    "songs": songs_list
}

with open('/config/Desktop/images/kannada-icons/songs/songs.json', 'w', encoding='utf-8') as f:
    json.dump(full_data, f, indent=2, ensure_ascii=False)

with open('/config/Desktop/images/kannada-icons/songs/songs_data.js', 'w', encoding='utf-8') as f:
    f.write('window.SONGS_DATA = ' + json.dumps(full_data, ensure_ascii=False, indent=2) + ';\n')

print(f"Successfully generated database with {len(songs_list)} songs across {len(all_sheets)} sheets!")
