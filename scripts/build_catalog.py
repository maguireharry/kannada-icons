#!/usr/bin/env python3
"""
Builds the standalone, zero-dependency interactive web catalog index.html
"""
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, "icons.json")
HTML_PATH = os.path.join(BASE_DIR, "index.html")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Compact icons data for embedding
embedded_icons_json = json.dumps(data["icons"], ensure_ascii=False)
categories_json = json.dumps(data["categories"], ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="kn">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ಕನ್ನಡ ಐಕಾನ್‌ಗಳು — Kannada Icons Collection (515 Vectors)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@400;500;600;700&family=Noto+Sans+Kannada:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --red: #C8102E;
      --red-dark: #990011;
      --yellow: #F5B800;
      --yellow-light: #FEF08A;
      --gold: #D97706;
      --dark: #0F172A;
      --dark-card: #1E293B;
      --dark-border: #334155;
      --slate-text: #64748B;
      --light-bg: #F8FAFC;
      --light-card: #FFFFFF;
      --light-border: #E2E8F0;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-kannada: 'Noto Sans Kannada', var(--font-body);
      --font-heading: 'Cinzel', serif;
    }}

    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: var(--font-body);
      background: var(--light-bg);
      color: var(--dark);
      line-height: 1.5;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    /* Top Announcement Banner */
    .top-banner {{
      background: linear-gradient(90deg, #C8102E 0%, #D97706 50%, #F5B800 100%);
      color: #FFFFFF;
      text-align: center;
      padding: 8px 16px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    /* Header Section */
    header {{
      background: #FFFFFF;
      border-bottom: 1px solid var(--light-border);
      padding: 40px 24px 30px;
      text-align: center;
    }}
    .header-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #FEF2F2;
      color: var(--red);
      border: 1px solid #FECACA;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 16px;
    }}
    h1 {{
      font-family: var(--font-kannada);
      font-size: 2.8rem;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 8px;
      letter-spacing: -0.5px;
    }}
    .subtitle {{
      font-size: 1.15rem;
      color: var(--slate-text);
      max-width: 720px;
      margin: 0 auto 20px;
    }}
    .stats-row {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 24px;
    }}
    .stat-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #F1F5F9;
      padding: 6px 14px;
      border-radius: 8px;
      font-size: 0.88rem;
      font-weight: 600;
    }}
    .stat-pill strong {{
      color: var(--red);
    }}

    /* Sticky Control Toolbar */
    .toolbar {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--light-border);
      padding: 16px 24px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }}
    .toolbar-inner {{
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .search-row {{
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .search-input-wrap {{
      flex: 1;
      min-width: 280px;
      position: relative;
    }}
    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--slate-text);
      pointer-events: none;
    }}
    .search-input {{
      width: 100%;
      padding: 12px 16px 12px 42px;
      border-radius: 10px;
      border: 1.5px solid var(--light-border);
      font-size: 1rem;
      font-family: var(--font-kannada);
      outline: none;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--red);
      box-shadow: 0 0 0 3px rgba(200, 16, 46, 0.12);
    }}

    /* Control Buttons */
    .view-controls {{
      display: flex;
      gap: 10px;
      align-items: center;
      flex-wrap: wrap;
    }}
    .control-label {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--slate-text);
      text-transform: uppercase;
      margin-right: 4px;
    }}
    .btn-group {{
      display: inline-flex;
      background: #F1F5F9;
      padding: 3px;
      border-radius: 8px;
    }}
    .btn-toggle {{
      border: none;
      background: transparent;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      color: var(--slate-text);
      transition: all 0.15s;
    }}
    .btn-toggle.active {{
      background: #FFFFFF;
      color: var(--dark);
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    /* Category Filter Pills */
    .categories-wrap {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: thin;
    }}
    .cat-pill {{
      white-space: nowrap;
      border: 1px solid var(--light-border);
      background: #FFFFFF;
      color: var(--slate-text);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-family: var(--font-kannada);
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .cat-pill:hover {{
      border-color: var(--red);
      color: var(--red);
    }}
    .cat-pill.active {{
      background: var(--red);
      border-color: var(--red);
      color: #FFFFFF;
    }}
    .cat-count {{
      font-size: 0.75rem;
      opacity: 0.85;
      background: rgba(0, 0, 0, 0.08);
      padding: 1px 6px;
      border-radius: 9999px;
    }}
    .cat-pill.active .cat-count {{
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }}

    /* Main Grid */
    main {{
      max-width: 1400px;
      width: 100%;
      margin: 24px auto;
      padding: 0 24px;
      flex: 1;
    }}
    .grid-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      font-size: 0.92rem;
      color: var(--slate-text);
    }}
    .icons-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
      gap: 16px;
    }}

    /* Icon Card */
    .icon-card {{
      background: var(--light-card);
      border: 1px solid var(--light-border);
      border-radius: 12px;
      padding: 16px 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .icon-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
      border-color: var(--red);
    }}
    .icon-preview-box {{
      width: 80px;
      height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      margin-bottom: 12px;
      position: relative;
      transition: background 0.2s;
    }}
    /* Background variants */
    .bg-checker {{
      background-image: linear-gradient(45deg, #E2E8F0 25%, transparent 25%),
                        linear-gradient(-45deg, #E2E8F0 25%, transparent 25%),
                        linear-gradient(45deg, transparent 75%, #E2E8F0 75%),
                        linear-gradient(-45deg, transparent 75%, #E2E8F0 75%);
      background-size: 12px 12px;
      background-position: 0 0, 0 6px, 6px -6px, -6px 0px;
      background-color: #F8FAFC;
    }}
    .bg-light {{ background: #FFFFFF; border: 1px solid #E2E8F0; }}
    .bg-dark {{ background: #0F172A; border: 1px solid #334155; }}
    .bg-gold {{ background: #FFFBEB; border: 1px solid #FDE68A; }}

    .icon-preview-box svg {{
      width: 56px;
      height: 56px;
      display: block;
      transition: transform 0.2s;
    }}
    .icon-card:hover .icon-preview-box svg {{
      transform: scale(1.08);
    }}

    .icon-name-kn {{
      font-family: var(--font-kannada);
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--dark);
      margin-bottom: 3px;
      display: -webkit-box;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .icon-name-en {{
      font-size: 0.78rem;
      color: var(--slate-text);
      display: -webkit-box;
      -webkit-line-clamp: 1;
      -webkit-box-orient: vertical;
      overflow: hidden;
      margin-bottom: 8px;
    }}
    .icon-cat-tag {{
      font-size: 0.7rem;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 6px;
      background: #F1F5F9;
      color: #475569;
    }}

    /* Card Hover Action Overlay */
    .card-actions {{
      position: absolute;
      top: 8px;
      right: 8px;
      display: none;
      gap: 4px;
    }}
    .icon-card:hover .card-actions {{
      display: flex;
    }}
    .action-mini-btn {{
      background: #FFFFFF;
      border: 1px solid var(--light-border);
      border-radius: 6px;
      padding: 4px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 4px rgba(0,0,0,0.06);
      transition: all 0.15s;
    }}
    .action-mini-btn:hover {{
      background: var(--red);
      color: #FFFFFF;
      border-color: var(--red);
    }}
    .action-mini-btn svg {{
      width: 14px;
      height: 14px;
    }}

    /* Modal Styles */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.open {{
      display: flex;
    }}
    .modal-card {{
      background: #FFFFFF;
      border-radius: 16px;
      max-width: 640px;
      width: 100%;
      overflow: hidden;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
      animation: modalFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 24px;
      border-bottom: 1px solid var(--light-border);
    }}
    .modal-title {{
      font-size: 1.1rem;
      font-weight: 700;
    }}
    .modal-close {{
      background: none;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
      color: var(--slate-text);
    }}
    .modal-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      max-height: 80vh;
      overflow-y: auto;
    }}
    .modal-preview-hero {{
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 32px;
      border-radius: 12px;
      min-height: 200px;
    }}
    .modal-preview-hero svg {{
      width: 128px;
      height: 128px;
    }}
    .modal-meta {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .modal-meta h2 {{
      font-family: var(--font-kannada);
      font-size: 1.6rem;
      font-weight: 800;
      color: var(--dark);
    }}
    .modal-meta p {{
      color: var(--slate-text);
      font-size: 1rem;
    }}
    .modal-tag-cloud {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 6px;
    }}
    .modal-tag {{
      background: #F1F5F9;
      color: #475569;
      font-size: 0.78rem;
      padding: 3px 8px;
      border-radius: 6px;
    }}
    .modal-actions {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .btn-action {{
      flex: 1;
      min-width: 140px;
      padding: 12px 18px;
      border-radius: 10px;
      font-size: 0.92rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      border: none;
      transition: all 0.15s;
    }}
    .btn-primary {{
      background: var(--red);
      color: #FFFFFF;
    }}
    .btn-primary:hover {{
      background: var(--red-dark);
    }}
    .btn-secondary {{
      background: #F1F5F9;
      color: var(--dark);
    }}
    .btn-secondary:hover {{
      background: #E2E8F0;
    }}
    .code-preview-box {{
      position: relative;
    }}
    .code-snippet {{
      background: #0F172A;
      color: #E2E8F0;
      padding: 12px 16px;
      border-radius: 8px;
      font-family: monospace;
      font-size: 0.8rem;
      max-height: 120px;
      overflow-y: auto;
      white-space: pre-wrap;
      word-break: break-all;
    }}

    /* Toast */
    .toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #0F172A;
      color: #FFFFFF;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 0.9rem;
      font-weight: 600;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 200;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toast.show {{
      transform: translateX(-50%) translateY(0);
    }}

    /* Footer */
    footer {{
      background: #FFFFFF;
      border-top: 1px solid var(--light-border);
      padding: 32px 24px;
      text-align: center;
      font-size: 0.88rem;
      color: var(--slate-text);
      margin-top: auto;
    }}
    footer a {{
      color: var(--red);
      text-decoration: none;
      font-weight: 600;
    }}
    footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <!-- Top Announcement -->
  <div class="top-banner">
    ಕರ್ನಾಟಕದ ಹಿರಿಮೆ, ಸಂಸ್ಕೃತಿ ಮತ್ತು ಕಲೆ ಬಿಂಬಿಸುವ ೫೧೫ ಮುಕ್ತ ವಾಹಕ ಐಕಾನ್‌ಗಳು • 515 Open Source Vector Icons
  </div>

  <!-- Header -->
  <header>
    <div class="header-badge">🌟 515 Icons • 10 Categories • Open Source</div>
    <h1>ಕನ್ನಡ ಐಕಾನ್‌ಗಳು</h1>
    <p class="subtitle">A comprehensive, production-ready vector icon system celebrating the rich heritage, monuments, performing arts, folklore, wildlife, flavors, and modern innovation of Karnataka.</p>
    
    <div class="stats-row">
      <div class="stat-pill"><strong>515</strong> Icons</div>
      <div class="stat-pill"><strong>10</strong> Categories</div>
      <div class="stat-pill"><strong>SVG & PNG</strong> 512×512</div>
      <div class="stat-pill"><strong>Transparent</strong> Background</div>
      <div class="stat-pill"><strong>MIT</strong> License</div>
    </div>
  </header>

  <!-- Sticky Controls Toolbar -->
  <section class="toolbar">
    <div class="toolbar-inner">
      <div class="search-row">
        <div class="search-input-wrap">
          <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input type="text" id="searchInput" class="search-input" placeholder="Search icons in Kannada or English (e.g. ಹಂಪಿ, ಆನೆ, ಮೈಸೂರು ಪಾಕ್, yakshagana, flag)..." autofocus>
        </div>

        <div class="view-controls">
          <span class="control-label">Canvas:</span>
          <div class="btn-group">
            <button class="btn-toggle active" data-bg="bg-checker">Checker</button>
            <button class="btn-toggle" data-bg="bg-light">Light</button>
            <button class="btn-toggle" data-bg="bg-dark">Dark</button>
            <button class="btn-toggle" data-bg="bg-gold">Gold</button>
          </div>
        </div>
      </div>

      <!-- Categories Pills -->
      <div class="categories-wrap" id="categoryPills">
        <button class="cat-pill active" data-cat="all">
          ಎಲ್ಲಾ ಐಕಾನ್‌ಗಳು (All) <span class="cat-count">515</span>
        </button>
      </div>
    </div>
  </section>

  <!-- Main Grid -->
  <main>
    <div class="grid-header">
      <span id="resultsCount">Showing 515 icons</span>
      <span id="activeFilterBadge">Category: All</span>
    </div>

    <div class="icons-grid" id="iconsGrid">
      <!-- Icon Cards injected via JS -->
    </div>
  </main>

  <!-- Details Modal -->
  <div class="modal-backdrop" id="modalBackdrop">
    <div class="modal-card">
      <div class="modal-header">
        <span class="modal-title">Icon Details</span>
        <button class="modal-close" id="modalCloseBtn">&times;</button>
      </div>
      <div class="modal-body">
        <div class="modal-preview-hero bg-checker" id="modalHero">
          <div id="modalSvgWrap"></div>
        </div>
        <div class="modal-meta">
          <h2 id="modalNameKn"></h2>
          <p id="modalNameEn"></p>
          <div class="modal-tag-cloud" id="modalTags"></div>
        </div>
        <div class="modal-actions">
          <button class="btn-action btn-primary" id="copySvgBtn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            Copy SVG
          </button>
          <a class="btn-action btn-secondary" id="downloadSvgLink" download>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download SVG
          </a>
          <a class="btn-action btn-secondary" id="downloadPngLink" download>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            Download PNG (512px)
          </a>
        </div>
        <div class="code-preview-box">
          <pre class="code-snippet" id="modalCodeSnippet"></pre>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div class="toast" id="toastMessage">SVG copied to clipboard!</div>

  <!-- Footer -->
  <footer>
    <p><strong>ಕನ್ನಡ ಐಕಾನ್‌ಗಳು — Kannada Icons Collection</strong></p>
    <p>Crafted with pride for Karnataka graphic designers, web developers, content creators and mobile app architects.</p>
    <p style="margin-top: 8px;">Released under the <a href="LICENSE">MIT License</a> • <a href="https://github.com/maguireharry/kannada-icons" target="_blank">GitHub Repository</a></p>
  </footer>

  <!-- Embedded Data & Application Script -->
  <script>
    const ICONS_DATA = {embedded_icons_json};
    const CATEGORIES = {categories_json};

    let currentBgClass = "bg-checker";
    let activeCategory = "all";
    let activeSearchQuery = "";
    let activeModalIcon = null;

    // Elements
    const iconsGrid = document.getElementById("iconsGrid");
    const searchInput = document.getElementById("searchInput");
    const categoryPills = document.getElementById("categoryPills");
    const resultsCount = document.getElementById("resultsCount");
    const activeFilterBadge = document.getElementById("activeFilterBadge");
    const modalBackdrop = document.getElementById("modalBackdrop");
    const modalCloseBtn = document.getElementById("modalCloseBtn");
    const modalHero = document.getElementById("modalHero");
    const modalSvgWrap = document.getElementById("modalSvgWrap");
    const modalNameKn = document.getElementById("modalNameKn");
    const modalNameEn = document.getElementById("modalNameEn");
    const modalTags = document.getElementById("modalTags");
    const modalCodeSnippet = document.getElementById("modalCodeSnippet");
    const copySvgBtn = document.getElementById("copySvgBtn");
    const downloadSvgLink = document.getElementById("downloadSvgLink");
    const downloadPngLink = document.getElementById("downloadPngLink");
    const toastMessage = document.getElementById("toastMessage");

    // Init Category Pills
    CATEGORIES.forEach(cat => {{
      const btn = document.createElement("button");
      btn.className = "cat-pill";
      btn.dataset.cat = cat.slug;
      btn.innerHTML = `${{cat.kannada}} <span class="cat-count">${{cat.count}}</span>`;
      btn.addEventListener("click", () => {{
        document.querySelectorAll(".cat-pill").forEach(p => p.classList.remove("active"));
        btn.classList.add("active");
        activeCategory = cat.slug;
        activeFilterBadge.textContent = "Category: " + cat.title;
        render();
      }});
      categoryPills.appendChild(btn);
    }});

    // All Pill Click
    document.querySelector('.cat-pill[data-cat="all"]').addEventListener("click", function() {{
      document.querySelectorAll(".cat-pill").forEach(p => p.classList.remove("active"));
      this.classList.add("active");
      activeCategory = "all";
      activeFilterBadge.textContent = "Category: All";
      render();
    }});

    // Background Toggles
    document.querySelectorAll(".btn-toggle").forEach(btn => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll(".btn-toggle").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        const newBg = btn.dataset.bg;
        document.querySelectorAll(".icon-preview-box").forEach(el => {{
          el.classList.remove(currentBgClass);
          el.classList.add(newBg);
        }});
        modalHero.classList.remove(currentBgClass);
        modalHero.classList.add(newBg);
        currentBgClass = newBg;
      }});
    }});

    // Search Input
    searchInput.addEventListener("input", (e) => {{
      activeSearchQuery = e.target.value.trim().toLowerCase();
      render();
    }});

    // Show Toast
    function showToast(msg) {{
      toastMessage.textContent = msg;
      toastMessage.classList.add("show");
      setTimeout(() => toastMessage.classList.remove("show"), 2200);
    }}

    // Open Modal
    function openModal(icon) {{
      activeModalIcon = icon;
      modalSvgWrap.innerHTML = icon.svg;
      modalNameKn.textContent = icon.kannada_name;
      modalNameEn.textContent = icon.name + " (" + icon.id + ")";
      modalHero.className = "modal-preview-hero " + currentBgClass;
      
      // Tags
      modalTags.innerHTML = "";
      icon.tags.forEach(t => {{
        const span = document.createElement("span");
        span.className = "modal-tag";
        span.textContent = "#" + t;
        modalTags.appendChild(span);
      }});

      // Code snippet
      modalCodeSnippet.textContent = icon.svg;

      // Links
      const svgBlob = new Blob([icon.svg], {{ type: "image/svg+xml" }});
      downloadSvgLink.href = URL.createObjectURL(svgBlob);
      downloadSvgLink.download = icon.id + ".svg";

      downloadPngLink.href = icon.png_relative_path;
      downloadPngLink.download = icon.id + ".png";

      modalBackdrop.classList.add("open");
    }}

    // Close Modal
    modalCloseBtn.addEventListener("click", () => modalBackdrop.classList.remove("open"));
    modalBackdrop.addEventListener("click", (e) => {{
      if (e.target === modalBackdrop) modalBackdrop.classList.remove("open");
    }});
    document.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") modalBackdrop.classList.remove("open");
    }});

    // Copy SVG Button
    copySvgBtn.addEventListener("click", () => {{
      if (activeModalIcon) {{
        navigator.clipboard.writeText(activeModalIcon.svg).then(() => {{
          showToast("Copied SVG code to clipboard!");
        }});
      }}
    }});

    // Render Function
    function render() {{
      const query = activeSearchQuery;
      const filtered = ICONS_DATA.filter(item => {{
        // Filter by category
        if (activeCategory !== "all" && item.category_slug !== activeCategory) return false;
        
        // Filter by search query
        if (query) {{
          const matchId = item.id.toLowerCase().includes(query);
          const matchEn = item.name.toLowerCase().includes(query);
          const matchKn = item.kannada_name.toLowerCase().includes(query);
          const matchTag = item.tags.some(t => t.toLowerCase().includes(query));
          return matchId || matchEn || matchKn || matchTag;
        }}
        return true;
      }});

      resultsCount.textContent = `Showing ${{filtered.length}} of ${{ICONS_DATA.length}} icons`;
      iconsGrid.innerHTML = "";

      if (filtered.length === 0) {{
        iconsGrid.innerHTML = `
          <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: var(--slate-text);">
            <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 8px;">ಯಾವುದೇ ಐಕಾನ್ ಕಂಡುಬಂದಿಲ್ಲ (No icons found)</p>
            <p>Try searching with another keyword in Kannada or English.</p>
          </div>
        `;
        return;
      }}

      const fragment = document.createDocumentFragment();

      filtered.forEach(icon => {{
        const card = document.createElement("div");
        card.className = "icon-card";
        card.innerHTML = `
          <div class="card-actions">
            <button class="action-mini-btn copy-btn" title="Copy SVG">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            </button>
            <a class="action-mini-btn dl-btn" href="${{icon.svg_relative_path}}" download="${{icon.id}}.svg" title="Download SVG">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            </a>
          </div>
          <div class="icon-preview-box ${{currentBgClass}}">
            ${{icon.svg}}
          </div>
          <div class="icon-name-kn">${{icon.kannada_name}}</div>
          <div class="icon-name-en">${{icon.name}}</div>
          <span class="icon-cat-tag">${{icon.category_title.split(' ')[0]}}</span>
        `;

        // Card Click opens Modal
        card.addEventListener("click", (e) => {{
          if (e.target.closest(".action-mini-btn")) return;
          openModal(icon);
        }});

        // Copy button in card hover
        card.querySelector(".copy-btn").addEventListener("click", (e) => {{
          e.stopPropagation();
          navigator.clipboard.writeText(icon.svg).then(() => {{
            showToast("Copied " + icon.name + " SVG!");
          }});
        }});

        fragment.appendChild(card);
      }});

      iconsGrid.appendChild(fragment);
    }}

    // Initial render
    render();
  </script>
</body>
</html>
"""

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Interactive Web Catalog generated: {HTML_PATH} ({len(html_content)} bytes)")
