import json
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from collections import defaultdict

data_path = '/config/Desktop/images/kannada-icons/posters/posters.json'
sheets_dir = '/config/Desktop/images/kannada-icons/posters/sheets'
output_dir = '/config/Desktop/images/kannada-icons/posters/individual'
os.makedirs(output_dir, exist_ok=True)

with open(data_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

posters_list = data['posters']

configs = {
    "posters_sheet_01_golden_epics": {
        "xs": [(57, 275), (390, 608), (725, 943)],
        "ys": [(23, 326), (357, 660), (692, 995)]
    },
    "posters_sheet_02_arthouse_milestones": {
        "xs": [(160, 350), (403, 595), (646, 838)],
        "ys": [(95, 350), (380, 635), (668, 922)]
    },
    "posters_sheet_03_80s_action_thrillers": {
        "xs": [(110, 316), (395, 601), (682, 888)],
        "ys": [(48, 326), (360, 638), (674, 952)]
    },
    "posters_sheet_04_romance_musicals": {
        "xs": [(190, 365), (412, 587), (634, 809)],
        "ys": [(140, 375), (410, 645), (680, 915)]
    },
    "posters_sheet_05_cult_underworld": {
        "xs": [(208, 390), (408, 592), (608, 792)],
        "ys": [(140, 368), (396, 624), (654, 882)]
    },
    "posters_sheet_06_2000s_blockbusters": {
        "xs": [(150, 345), (400, 595), (653, 848)],
        "ys": [(96, 365), (395, 655), (685, 950)]
    },
    "posters_sheet_07_indie_revolution": {
        "xs": [(110, 308), (400, 598), (688, 886)],
        "ys": [(132, 396), (412, 676), (690, 954)]
    },
    "posters_sheet_08_pan_indian_epics": {
        "xs": [(140, 348), (396, 604), (652, 860)],
        "ys": [(54, 328), (364, 638), (672, 946)]
    },
    "posters_sheet_09_contemporary_emotions": {
        "xs": [(138, 348), (395, 605), (651, 861)],
        "ys": [(70, 340), (370, 640), (665, 935)]
    },
    "posters_sheet_10_mass_blockbusters": {
        "xs": [(185, 378), (404, 597), (621, 814)],
        "ys": [(148, 394), (426, 662), (694, 955)]
    },
    "posters_sheet_11_cult_comedies": {
        "xs": [(132, 360), (385, 613), (638, 866)],
        "ys": [(132, 355), (388, 615), (644, 872)]
    },
    "posters_sheet_12_historic_milestones": {
        "xs": [(100, 285), (408, 593), (714, 899)],
        "ys": [(116, 364), (402, 650), (684, 932)]
    }
}

font_kannada_bold = '/usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf'
font_latin_bold = '/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf'
font_latin_reg = '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'

def render_movie_poster(cropped_art, movie, target_size=(700, 1050)):
    poster_w, poster_h = target_size
    poster = Image.new('RGB', (poster_w, poster_h), color=(12, 14, 18))
    
    art_small = cropped_art.resize((50, 50)).filter(ImageFilter.GaussianBlur(18))
    art_bg = art_small.resize((poster_w, poster_h))
    poster = Image.blend(poster, art_bg, 0.22)
    
    margin_x = 28
    margin_top = 26
    art_box_w = poster_w - (margin_x * 2)
    art_box_h = int(art_box_w * 1.25)
    
    art_resized = cropped_art.resize((art_box_w, art_box_h), Image.Resampling.LANCZOS)
    poster.paste(art_resized, (margin_x, margin_top))
    
    draw = ImageDraw.Draw(poster)
    draw.rectangle([margin_x - 2, margin_top - 2, margin_x + art_box_w + 1, margin_top + art_box_h + 1], 
                   outline=(212, 175, 55), width=2)
    
    plaque_y = margin_top + art_box_h + 14
    
    kn_title = movie["title_kn"]
    kn_size = 48
    if len(kn_title) > 24:
        kn_size = 30
    elif len(kn_title) > 18:
        kn_size = 36
    elif len(kn_title) > 12:
        kn_size = 42
        
    kn_font = ImageFont.truetype(font_kannada_bold, kn_size)
    bbox = draw.textbbox((0, 0), kn_title, font=kn_font)
    tw = bbox[2] - bbox[0]
    tx = (poster_w - tw) // 2
    
    for dx in [-2, 0, 2]:
        for dy in [-2, 0, 2]:
            if dx or dy:
                draw.text((tx + dx, plaque_y + dy), kn_title, font=kn_font, fill=(0, 0, 0))
    draw.text((tx, plaque_y), kn_title, font=kn_font, fill=(255, 224, 105))
    
    en_size = 20
    en_title = f"{movie['title'].upper()} ({movie['year']})"
    if len(en_title) > 30:
        en_size = 16
    elif len(en_title) > 24:
        en_size = 18
    en_font = ImageFont.truetype(font_latin_bold, en_size)
    ebbox = draw.textbbox((0, 0), en_title, font=en_font)
    etw = ebbox[2] - ebbox[0]
    etx = (poster_w - etw) // 2
    draw.text((etx, plaque_y + 54), en_title, font=en_font, fill=(245, 245, 250))
    
    meta_text = f"STYLE: {movie['style'].upper()}  •  {movie['era'].upper()}"
    meta_font = ImageFont.truetype(font_latin_bold, 12)
    mbbox = draw.textbbox((0, 0), meta_text, font=meta_font)
    mtw = mbbox[2] - mbbox[0]
    mtx = (poster_w - mtw) // 2
    draw.text((mtx, plaque_y + 86), meta_text, font=meta_font, fill=(185, 195, 210))
    
    credit_text = f"Dir: {movie['director']}  |  Cast: {movie['cast']}"
    if len(credit_text) > 65:
        credit_text = credit_text[:62] + "..."
    c_font = ImageFont.truetype(font_latin_reg, 13)
    cbbox = draw.textbbox((0, 0), credit_text, font=c_font)
    ctw = cbbox[2] - cbbox[0]
    ctx = (poster_w - ctw) // 2
    draw.text((ctx, plaque_y + 112), credit_text, font=c_font, fill=(145, 155, 170))
    
    draw.rectangle([8, 8, poster_w - 9, poster_h - 9], outline=(212, 175, 55), width=1)
    draw.rectangle([12, 12, poster_w - 13, poster_h - 13], outline=(80, 65, 25), width=1)
    
    tag_font = ImageFont.truetype(font_latin_bold, 10)
    tag_text = "SANDALWOOD CLASSICS REIMAGINED"
    tbbox = draw.textbbox((0, 0), tag_text, font=tag_font)
    ttw = tbbox[2] - tbbox[0]
    draw.text(((poster_w - ttw) // 2, 13), tag_text, font=tag_font, fill=(190, 160, 80))
    
    return poster

if __name__ == '__main__':
    by_sheet = defaultdict(list)
    for p in posters_list:
        by_sheet[p['sheet']].append(p)

    success_count = 0
    for sheet_key, mlist in by_sheet.items():
        sheet_path = os.path.join(sheets_dir, f"{sheet_key}.png")
        if not os.path.exists(sheet_path):
            continue
        sheet_img = Image.open(sheet_path)
        grid = configs.get(sheet_key)
        if not grid:
            continue
        for i, movie in enumerate(mlist):
            row = i // 3
            col = i % 3
            x1, x2 = grid["xs"][col]
            y1, y2 = grid["ys"][row]
            cropped_art = sheet_img.crop((x1, y1, x2, y2))
            poster = render_movie_poster(cropped_art, movie)
            out_filename = f"{movie['id']}.png"
            out_filepath = os.path.join(output_dir, out_filename)
            poster.save(out_filepath, quality=95)
            movie['poster_image'] = f"posters/individual/{out_filename}"
            movie['sheet_image'] = f"posters/sheets/{sheet_key}.png"
            success_count += 1

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open('/config/Desktop/images/kannada-icons/posters/posters_data.js', 'w', encoding='utf-8') as f:
        f.write('window.POSTERS_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')
    print(f"Generated {success_count} posters.")
