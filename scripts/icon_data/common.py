"""
Common utilities, color constants, and SVG builders for Kannada Icons.
"""

# Authentic Karnataka & Cultural Palette
RED = "#C8102E"          # Karnataka Flag Red
YELLOW = "#FFD100"       # Karnataka Flag Yellow
GOLD = "#D4AF37"         # Mysore Royal Gold
DARK_GOLD = "#B8860B"    # Antique Gold
SLATE = "#1E293B"        # Charcoal Slate for crisp line work
DARK = "#0F172A"         # Deep Midnight
GREEN = "#15803D"        # Western Ghats Emerald
LIGHT_GREEN = "#22C55E"  # Fresh Bamboo Green
BROWN = "#78350F"        # Sandalwood / Coffee Brown
LIGHT_BROWN = "#B45309"  # Teakwood Ochre
ORANGE = "#EA580C"       # Saffron / Terracotta
ROYAL_BLUE = "#1D4ED8"   # Krishna / Netravathi Blue
SKY_BLUE = "#0284C7"     # Karavali Sky Blue
PURPLE = "#6B21A8"       # Royal Mysore Silk Purple
SILVER = "#94A3B8"       # Bidriware Silver
WHITE = "#FFFFFF"        # Highlight White
CREAM = "#FEF9C3"        # Sandalwood Cream

COMMON_DEFS = """
    <linearGradient id="flagGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#FFD100"/>
      <stop offset="50%" stop-color="#FFD100"/>
      <stop offset="50%" stop-color="#C8102E"/>
      <stop offset="100%" stop-color="#C8102E"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FDE047"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#996515"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#EF4444"/>
      <stop offset="100%" stop-color="#991B1B"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#34D399"/>
      <stop offset="100%" stop-color="#065F46"/>
    </linearGradient>
    <linearGradient id="coffeeGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#92400E"/>
      <stop offset="100%" stop-color="#451A03"/>
    </linearGradient>
"""

def wrap_svg(inner_content, extra_defs=""):
    defs = f"<defs>{COMMON_DEFS}\n{extra_defs}</defs>" if (COMMON_DEFS or extra_defs) else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
{defs}
{inner_content.strip()}
</svg>"""

# Convenient aliases
BLUE = ROYAL_BLUE
LIGHT_BLUE = SKY_BLUE
GOLD_DARK = DARK_GOLD
