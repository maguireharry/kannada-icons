import json

with open('/config/Desktop/images/kannada-icons/songs/songs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sheets = data['sheets']
songs_by_sheet = {}
for s in data['songs']:
    songs_by_sheet.setdefault(s['sheet'], []).append(s)

prompts = {}
for sheet in sheets:
    key = sheet['key']
    theme = sheet['theme']
    style_m = sheet['style_movement']
    slist = songs_by_sheet[key]
    
    panel_descriptions = []
    for i, song in enumerate(slist, 1):
        panel_descriptions.append(f"Panel {i} ({song['title']}): {song['style']}")
    
    panels_str = "; ".join(panel_descriptions)
    
    prompt = (
        f"A master art exhibition sheet containing 9 distinct stylized graphic poster art panels arranged in an elegant 3x3 grid, "
        f"celebrating classic Kannada songs in '{theme}'. "
        f"ART STYLE: strictly non-realistic graphic illustration, {style_m}, fine art printmaking, flat vibrant colors, decorative linework, zero photorealism. "
        f"The 9 panels depict: {panels_str}. "
        f"Each of the 9 panels has clear borders, high artistic composition, retro screenprint and woodblock aesthetic, rich texture."
    )
    prompts[key] = prompt

with open('/config/Desktop/images/kannada-icons/songs/sheet_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(prompts, f, indent=2)

print("Generated 17 sheet prompts successfully!")
