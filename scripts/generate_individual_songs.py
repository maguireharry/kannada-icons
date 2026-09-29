import json
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_KN_BOLD = "/usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf"
FONT_KN_REG = "/usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf"
FONT_EN_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_EN_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

SHEET_CONFIGS = {
    "songs_sheet_01_bhavageethe": (70, 100, 310, 294, 262, 254),
    "songs_sheet_02_kannada_pride": (80, 82, 298, 292, 264, 258),
    "songs_sheet_03_golden_romance": (52, 124, 308, 274, 270, 240),
    "songs_sheet_04_rajkumar_philosophical": (48, 76, 308, 296, 270, 260),
    "songs_sheet_05_ilaiyaraaja_melodies": (70, 110, 298, 288, 264, 254),
    "songs_sheet_06_hamsalekha_magic": (82, 114, 286, 286, 260, 252),
    "songs_sheet_07_monsoon_rain": (34, 96, 318, 300, 284, 264),
    "songs_sheet_08_spiritual_bhakti": (60, 94, 300, 298, 268, 262),
    "songs_sheet_09_folk_janapada": (126, 144, 260, 262, 232, 220),
    "songs_sheet_10_upendra_cult": (30, 72, 320, 304, 286, 268),
    "songs_sheet_11_2000s_youth": (28, 82, 322, 304, 286, 268),
    "songs_sheet_12_pan_indian_epics": (142, 176, 246, 254, 224, 218),
    "songs_sheet_13_contemporary_ballads": (30, 64, 320, 306, 286, 264),
    "songs_sheet_14_classical_ragas": (52, 72, 308, 302, 276, 264),
    "songs_sheet_15_retro_grooves": (40, 74, 314, 302, 282, 266),
    "songs_sheet_16_sugama_sangeetha": (44, 84, 312, 302, 278, 264),
    "songs_sheet_17_indie_waves": (28, 110, 322, 296, 284, 252),
}

def render_song_poster(song, cell_img, out_path):
    W, H = 700, 1050
    poster = Image.new("RGB", (W, H), (12, 15, 20))
    
    # 1. Ambient background blur from artwork
    small_bg = cell_img.resize((W, H), Image.Resampling.LANCZOS)
    small_bg = small_bg.filter(ImageFilter.GaussianBlur(radius=45))
    dark_overlay = Image.new("RGB", (W, H), (8, 10, 14))
    blended_bg = Image.blend(small_bg, dark_overlay, alpha=0.82)
    poster.paste(blended_bg, (0, 0))
    draw = ImageDraw.Draw(poster)
    
    # 2. Outer luxury double gold border
    draw.rectangle([20, 20, W-20, H-20], outline="#D4AF37", width=2)
    draw.rectangle([26, 26, W-26, H-26], outline="#5A4718", width=1)
    
    # Corner flourishes
    corner_len = 16
    for (cx, cy) in [(20, 20), (W-20, 20), (20, H-20), (W-20, H-20)]:
        dx = corner_len if cx == 20 else -corner_len
        dy = corner_len if cy == 20 else -corner_len
        draw.line([(cx, cy), (cx + dx, cy)], fill="#FFDF64", width=3)
        draw.line([(cx, cy), (cx, cy + dy)], fill="#FFDF64", width=3)
        draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill="#FFDF64")

    # 3. Top Header & Art Style Movement Badge (English font)
    font_badge = ImageFont.truetype(FONT_EN_BOLD, 12)
    badge_text = f"✦ {song['style_movement'].upper()} ✦"
    if len(badge_text) > 48:
        badge_text = f"✦ {song['theme'].upper()} ✦"
    
    bb = draw.textbbox((0, 0), badge_text, font=font_badge)
    bw, bh = bb[2] - bb[0], bb[3] - bb[1]
    bx = (W - bw) // 2
    by = 40
    
    draw.rounded_rectangle([bx - 14, by - 5, bx + bw + 14, by + bh + 7], radius=12, fill="#181f28", outline="#8C7326", width=1)
    draw.text((bx, by), badge_text, font=font_badge, fill="#E6C875")
    
    # Sub-badge: Theme & Year
    font_sub = ImageFont.truetype(FONT_EN_REG, 13)
    sub_text = f"{song['theme']}  •  {song['year']}"
    sbb = draw.textbbox((0, 0), sub_text, font=font_sub)
    draw.text(((W - (sbb[2] - sbb[0])) // 2, 72), sub_text, font=font_sub, fill="#A4B3C6")

    # 4. Framed Center Artwork
    art_size = 560
    art_x = (W - art_size) // 2
    art_y = 108
    resized_art = cell_img.resize((art_size, art_size), Image.Resampling.LANCZOS)
    
    draw.rectangle([art_x - 4, art_y - 4, art_x + art_size + 4, art_y + art_size + 4], fill="#080a0e")
    poster.paste(resized_art, (art_x, art_y))
    draw = ImageDraw.Draw(poster)
    draw.rectangle([art_x - 1, art_y - 1, art_x + art_size + 1, art_y + art_size + 1], outline="#D4AF37", width=2)
    draw.rectangle([art_x - 5, art_y - 5, art_x + art_size + 5, art_y + art_size + 5], outline="#3D3213", width=1)
    
    # 5. Typography Block
    curr_y = art_y + art_size + 24
    
    # Primary Title: Native Kannada Script (Always present & prominent)
    title_kn = song["title_kn"]
    kn_size = 46
    if len(title_kn) > 20:
        kn_size = 38
    if len(title_kn) > 28:
        kn_size = 32
    if len(title_kn) > 36:
        kn_size = 28
        
    font_kn = ImageFont.truetype(FONT_KN_BOLD, kn_size)
    kbb = draw.textbbox((0, 0), title_kn, font=font_kn)
    kw = kbb[2] - kbb[0]
    kx = (W - kw) // 2
    
    # Golden drop shadow
    draw.text((kx + 2, curr_y + 2), title_kn, font=font_kn, fill="#150E02")
    draw.text((kx + 1, curr_y + 1), title_kn, font=font_kn, fill="#523908")
    draw.text((kx, curr_y), title_kn, font=font_kn, fill="#FFDF64")
    
    curr_y += (kbb[3] - kbb[1]) + 10
    
    # Secondary Title: English Title
    title_en = song['title']
    font_en = ImageFont.truetype(FONT_EN_BOLD, 21)
    ebb = draw.textbbox((0, 0), title_en, font=font_en)
    draw.text(((W - (ebb[2] - ebb[0])) // 2, curr_y), title_en, font=font_en, fill="#FFFFFF")
    
    curr_y += (ebb[3] - ebb[1]) + 12
    
    # Decorative divider
    div_w = 260
    draw.line([(W - div_w)//2, curr_y, (W + div_w)//2, curr_y], fill="#8C7326", width=1)
    draw.ellipse([(W//2)-3, curr_y-3, (W//2)+3, curr_y+3], fill="#FFDF64")
    curr_y += 12
    
    # Album / Movie row:
    alb_kn = song.get('album_or_movie_kn', '')
    alb_en = song.get('album_or_movie', '')
    
    if alb_kn:
        font_alb_kn = ImageFont.truetype(FONT_KN_BOLD, 17)
        akbb = draw.textbbox((0, 0), alb_kn, font=font_alb_kn)
        draw.text(((W - (akbb[2] - akbb[0])) // 2, curr_y), alb_kn, font=font_alb_kn, fill="#E6C875")
        curr_y += (akbb[3] - akbb[1]) + 4

    font_alb_en = ImageFont.truetype(FONT_EN_REG, 14)
    aebb = draw.textbbox((0, 0), alb_en, font=font_alb_en)
    draw.text(((W - (aebb[2] - aebb[0])) // 2, curr_y), alb_en, font=font_alb_en, fill="#C0CCD8")
    curr_y += (aebb[3] - aebb[1]) + 12
    
    # Credits (Singer, Music, Lyrics in clean Latin sans)
    font_cred = ImageFont.truetype(FONT_EN_REG, 13)
    cred_line1 = f"Singer: {song['singer']}   •   Music: {song['composer']}"
    c1bb = draw.textbbox((0, 0), cred_line1, font=font_cred)
    draw.text(((W - (c1bb[2] - c1bb[0])) // 2, curr_y), cred_line1, font=font_cred, fill="#B0C2D6")
    
    curr_y += (c1bb[3] - c1bb[1]) + 5
    cred_line2 = f"Lyrics: {song['lyricist']}   •   Art Style: {song['style']}"
    if len(cred_line2) > 65:
        cred_line2 = f"Lyrics: {song['lyricist']}"
    c2bb = draw.textbbox((0, 0), cred_line2, font=font_cred)
    draw.text(((W - (c2bb[2] - c2bb[0])) // 2, curr_y), cred_line2, font=font_cred, fill="#8599AF")

    # Bottom footer tag
    font_foot = ImageFont.truetype(FONT_EN_REG, 10)
    foot_text = "KANNADA CLASSIC SONGS ARCHIVE • NANO BANANA ART SERIES"
    fbb = draw.textbbox((0, 0), foot_text, font=font_foot)
    draw.text(((W - (fbb[2] - fbb[0])) // 2, H - 38), foot_text, font=font_foot, fill="#5B6877")
    
    poster.save(out_path, quality=95)

def main():
    songs_file = "/config/Desktop/images/kannada-icons/songs/songs.json"
    sheets_dir = "/config/Desktop/images/kannada-icons/songs/sheets"
    out_dir = "/config/Desktop/images/kannada-icons/songs/individual"
    os.makedirs(out_dir, exist_ok=True)
    
    with open(songs_file, "r") as f:
        data = json.load(f)
    
    songs = data["songs"]
    print(f"Total songs to process: {len(songs)}")
    
    sheet_cache = {}
    
    count = 0
    for song in songs:
        sheet_key = os.path.basename(song["sheet_image"]).replace(".png", "")
        if sheet_key not in sheet_cache:
            sheet_path = os.path.join(sheets_dir, f"{sheet_key}.png")
            if not os.path.exists(sheet_path):
                print(f"ERROR: Sheet not found: {sheet_path}")
                continue
            sheet_cache[sheet_key] = Image.open(sheet_path)
            
        sheet_img = sheet_cache[sheet_key]
        cfg = SHEET_CONFIGS[sheet_key]
        x0, y0, sx, sy, pw, ph = cfg
        
        idx = (int(song["id"].split("_")[1]) - 1) % 9 # 0 to 8
        r = idx // 3
        c = idx % 3
        
        cell_x = x0 + c * sx
        cell_y = y0 + r * sy
        cell_img = sheet_img.crop((cell_x, cell_y, cell_x + pw, cell_y + ph))
        
        out_file = os.path.join(out_dir, f"{song['id']}.png")
        render_song_poster(song, cell_img, out_file)
        count += 1
        if count % 20 == 0 or count == len(songs):
            print(f"[{count}/{len(songs)}] Generated {out_file}")
            
    print(f"Successfully generated all {count} individual song posters!")

if __name__ == "__main__":
    main()
