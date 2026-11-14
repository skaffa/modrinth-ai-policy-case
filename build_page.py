"""Builds modrinth_exposer/publish/index.html from the verified project data below.

Every project row was checked live against api.modrinth.com/v2/projects on 2026-11-14 (status approved).
Quotes are the authors' own disclosure text, copied from the previous page and the evidence CSVs.
"""
import html
import sys

OUT = sys.argv[1]
CDN = "https://cdn.modrinth.com/data/"

# (id, slug, title, created, first_published, downloads, cohort, quote, icon path)
CODE = [
    ("j8VEYlIP", "lets-chess", "[咱们下棋吧！] Let's Chess!", "2026-09-05", "2026-10-02", 194, "grace",
     "Most of the code and functions of the game are generated and implemented with the assistance of AI.",
     "j8VEYlIP/f78aa6463b6369acda30949bc50b150ca498cab8_96.webp"),
    ("4M2o6zbf", "ransom", "Ransom(A90)", "2026-09-13", "2026-10-20", 605, "grace",
     "I used AI to assist with writing the mod’s Java code because I am not familiar with Java programming.",
     "4M2o6zbf/1ba3fe520c76ffec18d728a35818fbab83c44638_96.webp"),
    ("GaDa1lfJ", "infenity", "InFEnity", "2026-09-14", "2026-10-22", 232, "grace",
     "All the code is AI Generated.", "GaDa1lfJ/0c569dc17f0cca401ce2ce3d43bb93903f922b28_96.webp"),
    ("su2xWAa2", "pvptiers", "PVP Tiers", "2026-10-24", "2026-10-25", 327, "post",
     "Most of the code is AI-generated since I suck at it but that’s it",
     "su2xWAa2/056bd0a81f3ba76e40f8cf8883f42b5915dae7d5.png"),
    ("MrC0PXcn", "backrooms-chi_catt", "Backrooms", "2026-10-28", "2026-10-31", 285, "post",
     "Most of the code, the placeholder textures and sounds, and this page’s text were written with an AI assistant (Claude) under the author’s direction and review.",
     "MrC0PXcn/eb80a5fa3e4a9c9b9974f9c82dfbb1b0c4261741_96.webp"),
    ("4Re7aXso", "vulkairis", "VulkaIris (VIS)", "2026-05-31", "2026-11-05", 262, "pre",
     "Heavily assisted with AI for most of the code.", "4Re7aXso/9c4d17de55efbba4212d6fa8239cc69db6dc25e7_96.webp"),
    ("31A1SZXb", "fluidic", "Fluidic", "2026-10-24", "2026-11-07", 17, "post",
     "created as a stress test of Claude Code and as such is primarily AI coded.",
     "31A1SZXb/2186f29ba4216632b7938764dc05bc9bccbd9173_96.webp"),
    ("16YW9qCT", "bj-mapedit", "BJ-MapEdit", "2026-08-19", "2026-11-08", 36, "grace",
     "largely AI-assisted (LLM coding agents), under human direction, review and in-game testing.",
     "16YW9qCT/68506f4d88125a8c8f2804cb9606caf32af4b3cd_96.webp"),
    ("1EG1sra5", "water-everywhere", "Water Everywhere", "2026-08-20", "2026-11-09", 8, "grace",
     "Code and translations", "1EG1sra5/03c05c9f661f63934d524947375ac35c726f7e4f_96.webp"),
]
IMAGES = [
    ("nVj3rQLV", "uhc-prime", "UHC Prime", "2026-10-08", "2026-10-11", 240, "post",
     "the scripts that draw the icon and banners were written with the help of AI (Claude)",
     "nVj3rQLV/c1f836b76d5390b65135e03fa9d1c0b55ed9eb19_96.webp"),
    ("3W5LayVz", "nexora_players", "Nexora Players", "2026-08-29", "2026-11-08", 10, "grace",
     "image generation python code is ai assisted", "3W5LayVz/923bd897a0ee89078d7ecc16a01a7007a8b6271b_96.webp"),
    ("3qNitUjN", "stackable-shulkerbox", "stackable shulkerbox", "2026-10-14", "2026-10-18", 352, "post",
     "only for the brainstorming and the icon logo", "3qNitUjN/2e9c1569f91745d629b3b6c46894a71723faf5e4_96.webp"),
    ("5AOgM5wm", "gui-crafter", "GUI Crafter", "2026-08-05", "2026-10-08", 94, "pre",
     "The background art was primarily AI-generated", "5AOgM5wm/933c83ee568651a66a410c84e956816bcdb3bdfb_96.webp"),
    ("YTuuFsYM", "lively_bends", "Lively Bends", "2026-09-15", "2026-10-26", 683, "grace",
     "AI was used to assist with code development, project descriptions, and promotional artwork.",
     "YTuuFsYM/86afe03a5d8eeb76ed6dd62facfddc80350efd31_96.webp"),
]
# in-mod art (textures), not page images: relevant to the content ground, found in gate.db, live-checked 2026-11-14
TEXTURES = [
    ("Ta6w7RkG", "mystical-agriculture-plus", "Mystical Agriculture Plus", "2026-09-15", "2026-10-23", 393, "grace",
     "The code, textures (pixel art drawn by scripts, some recoloured from Mystical Agriculture's) and language files were made with an AI coding assistant. All the ideas are mine, not the AI's: every feature, mechanic and balance choice comes from me. I also test every feature in-game myself: I find the bugs, report them and check the fixes before each release.",
     "Ta6w7RkG/fd07829faac4957d21da716e665b2ac3601ad32a_96.webp"),
    ("EjWZNjOK", "imeinputbackport", "IMEInputBackport", "2026-08-19", "2026-10-21", 92, "grace",
     "Example assets used Claude to generate a script to generate the textures.",
     "EjWZNjOK/125ca9df1d7c928697a37acd8fbc7cc492ed5c23.webp"),
    ("b9sxAR2W", "cloudstorage", "Cloud Storage", "2026-08-09", "2026-11-04", 382, "grace",
     "I have let AI design the textures for blocks and items as I am not that good at designing. I did intervene for small changes in Photoshop.",
     "b9sxAR2W/fc983545ada0b7a1bef4ac69251d2ebad88603fd_96.webp"),
]
COHORT = {
    "post": ("created after deadline", "pill-red"),
    "grace": ("created during grace", "pill-orange"),
    "pre": ("created before policy", "pill-gray"),
}


def e(s):
    return html.escape(s, quote=True)


LOGO = """<svg viewBox="0 0 32 32" width="{s}" height="{s}" aria-hidden="true"><rect width="32" height="32" rx="8" fill="var(--brand)"/><g fill="none" stroke="var(--brand-ink)" stroke-width="2.6" stroke-linecap="round"><path d="M9 13h14M9 19h14"/><path d="M20 8 12 24"/></g></svg>"""
ME = """<span class="me" aria-hidden="true">?</span>"""
MY_CODE = "[This project] was made together with Claude (Anthropic). Most of the code, the documentation and this page’s text were written by Claude under my direction, and I tested everything in game."
MY_ICON = "The pixel-art icon was drawn by a small script Claude wrote, not by an image generator."


def row(p):
    pid, slug, title, created, published, dl, cohort, quote, icon = p
    label, cls = COHORT[cohort]
    return f"""
      <a class="row" href="https://modrinth.com/mod/{e(slug)}" rel="noopener">
        <img src="{CDN}{e(icon)}" alt="" width="40" height="40" loading="lazy">
        <span class="row-main"><b>{e(title)}</b> <q>{e(quote)}</q></span>
        <span class="row-meta"><span class="pill pill-approved">approved {e(published)}</span><span class="pill {cls}" title="{e(label)}">created {e(created)}</span></span>
      </a>"""


def vs(icon_src, name, status_cls, status, quote):
    img = f'<img src="{icon_src}" alt="">' if icon_src else ME
    return f"""<div class="vs-col"><header>{img}<b>{e(name)}</b><span class="pill {status_cls}">{e(status)}</span></header><p>“{e(quote)}”</p></div>"""


code_rows = "".join(row(p) for p in CODE)
image_rows = "".join(row(p) for p in IMAGES)
texture_rows = "".join(row(p) for p in TEXTURES)
back = CODE[4]
uhc, nexora = IMAGES[0], IMAGES[1]
map_ = TEXTURES[0]

PAGE = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Modrinth AI Policy: Uneven Enforcement</title>
<meta name="description" content="A submission refused under Modrinth's AI policy, set against 17 projects disclosing the same or more that were approved after the grace period. Independent; not affiliated with Modrinth.">
<link rel="icon" href="data:image/svg+xml,{LOGO.format(s=32).replace('var(--brand)', '%231bd96a').replace('var(--brand-ink)', '%23000').replace('"', "'").replace('<', '%3C').replace('>', '%3E')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
/* Colour tokens modelled on Modrinth's dark and light themes. */
:root {{
  --bg: #16181c; --raised: #26292f; --raised-2: #2e3138; --button: #33363d; --divider: #33363d;
  --base: #b0bac5; --contrast: #ecf9fb; --secondary: #96a2b0;
  --brand: #1bd96a; --brand-bg: rgba(27, 217, 106, .12); --brand-ink: #000;
  --red: #ff496e; --red-bg: rgba(255, 73, 110, .13); --orange: #ffa347; --orange-bg: rgba(255, 163, 71, .13);
  --gray-bg: rgba(150, 162, 176, .14);
  --shadow: 0 2px 4px rgba(0, 0, 0, .25), 0 6px 16px rgba(0, 0, 0, .18);
  --r-lg: 1rem; --r-md: .75rem; --r-sm: .5rem;
}}
@media (prefers-color-scheme: light) {{
  :root {{
    --bg: #e5e7eb; --raised: #ffffff; --raised-2: #f5f6f7; --button: #eceef1; --divider: #e2e5e9;
    --base: #2c2e31; --contrast: #1a202c; --secondary: #5e6774;
    --brand: #00af5c; --brand-bg: rgba(0, 175, 92, .12); --brand-ink: #fff;
    --red: #cb2245; --red-bg: rgba(203, 34, 69, .1); --orange: #c25e00; --orange-bg: rgba(194, 94, 0, .1);
    --gray-bg: rgba(94, 103, 116, .1);
    --shadow: 0 1px 2px rgba(0, 0, 0, .06), 0 4px 12px rgba(0, 0, 0, .06);
  }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--base);
  font: 400 15px/1.55 Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; -webkit-text-size-adjust: 100%; }}
a {{ color: var(--brand); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
strong, b {{ color: var(--contrast); font-weight: 650; }}
code {{ font: .84em ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background: var(--button); padding: .08em .35em; border-radius: .35rem; color: var(--contrast); }}
h1, h2, h3 {{ color: var(--contrast); line-height: 1.25; }}
q {{ quotes: "“" "”"; }}

.topbar {{ background: var(--raised); border-bottom: 1px solid var(--divider); }}
.topbar-inner {{ max-width: 1180px; margin: 0 auto; padding: .6rem 1rem; display: flex; gap: .7rem; align-items: center; flex-wrap: wrap; }}
.wordmark {{ display: flex; align-items: center; gap: .55rem; font-weight: 800; color: var(--contrast); }}
.topbar nav {{ display: flex; gap: .15rem; flex-wrap: wrap; margin-left: auto; }}
.topbar nav a {{ color: var(--base); font-weight: 600; font-size: .85rem; padding: .3rem .65rem; border-radius: 99px; }}
.topbar nav a:hover {{ background: var(--button); color: var(--contrast); text-decoration: none; }}
.notice {{ max-width: 1180px; margin: 0 auto; padding: .45rem 1rem; font-size: .78rem; color: var(--secondary); }}

.wrap {{ max-width: 1180px; margin: 0 auto; padding: .25rem 1rem 3rem; display: grid; grid-template-columns: minmax(0, 1fr) 290px; gap: 1rem; align-items: start; }}
.main {{ display: flex; flex-direction: column; gap: 1rem; min-width: 0; }}
.side {{ display: flex; flex-direction: column; gap: 1rem; position: sticky; top: 1rem; }}
.card {{ background: var(--raised); border-radius: var(--r-lg); padding: 1.05rem 1.2rem; box-shadow: var(--shadow); }}
.card h2 {{ font-size: 1.12rem; margin: 0 0 .5rem; }}
.card h3 {{ font-size: .95rem; margin: 1rem 0 .45rem; }}
.card p {{ margin: .45rem 0; }}
.tag {{ font-size: .72rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--secondary); margin-right: .4rem; }}

.hero h1 {{ font-size: 1.6rem; margin: 0 0 .5rem; letter-spacing: -.02em; }}
.hero p {{ color: var(--contrast); }}
.hero {{ border-left: 4px solid var(--brand); }}
.pills {{ display: flex; flex-wrap: wrap; gap: .35rem; }}
.pill {{ display: inline-flex; align-items: center; gap: .3rem; font-size: .74rem; font-weight: 650; padding: .14rem .55rem; border-radius: 99px; white-space: nowrap; }}
.pill-red {{ background: var(--red-bg); color: var(--red); }}
.pill-orange {{ background: var(--orange-bg); color: var(--orange); }}
.pill-gray {{ background: var(--gray-bg); color: var(--secondary); }}
.pill-approved {{ background: var(--brand-bg); color: var(--brand); }}
.pill-approved::before, .pill-rejected::before {{ content: ""; width: .42rem; height: .42rem; border-radius: 50%; background: currentColor; }}
.pill-rejected {{ background: var(--red-bg); color: var(--red); }}

blockquote {{ margin: .6rem 0; padding: .6rem .85rem; background: var(--raised-2); border-radius: var(--r-md); border-left: 3px solid var(--divider); color: var(--contrast); font-size: .92rem; }}
blockquote p {{ margin: .2rem 0; }}
blockquote.mod {{ border-left-color: var(--red); }}
.note {{ color: var(--secondary); font-size: .84rem; }}

.vs {{ display: grid; grid-template-columns: 1fr 1fr; gap: .7rem; margin: .6rem 0; }}
.vs-col {{ background: var(--raised-2); border-radius: var(--r-md); padding: .7rem .85rem; }}
.vs-col header {{ display: flex; align-items: center; gap: .5rem; flex-wrap: wrap; margin-bottom: .35rem; }}
.vs-col header img, .me {{ width: 28px; height: 28px; border-radius: var(--r-sm); background: var(--button); flex: none; }}
.me {{ display: inline-flex; align-items: center; justify-content: center; font-weight: 800; color: var(--secondary); }}
.vs-col p {{ margin: 0; font-size: .9rem; color: var(--contrast); }}
.mine {{ margin: .6rem 0; }}
.mine .vs-col {{ border-left: 3px solid var(--red); }}
.match {{ margin: .35rem .2rem 0; font-size: .8rem; color: var(--secondary); }}

.rows {{ display: flex; flex-direction: column; gap: .35rem; margin: .5rem 0; }}
.row {{ display: grid; grid-template-columns: 40px minmax(0, 1fr) auto; gap: .75rem; align-items: center; background: var(--raised-2);
  border-radius: var(--r-md); padding: .5rem .7rem; color: var(--base); }}
.row:hover {{ text-decoration: none; background: var(--button); }}
.row img {{ width: 40px; height: 40px; border-radius: var(--r-sm); background: var(--button); object-fit: cover; }}
.row-main {{ font-size: .9rem; min-width: 0; }}
.row-main q {{ font-style: italic; }}
.row-meta {{ display: flex; flex-direction: column; align-items: flex-end; gap: .2rem; }}

.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: .55rem; margin: .5rem 0; }}
.stat {{ background: var(--raised-2); border-radius: var(--r-md); padding: .6rem .75rem; }}
.stat b {{ display: block; font-size: 1.35rem; line-height: 1.1; font-weight: 800; font-variant-numeric: tabular-nums; }}
.stat span {{ font-size: .76rem; color: var(--secondary); }}
.stat.hl b {{ color: var(--brand); }}

.side .card {{ padding: .95rem 1.05rem; }}
.side h3 {{ font-size: .9rem; margin: 0 0 .55rem; }}
.facts {{ margin: 0; display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: .3rem .7rem; font-size: .84rem; }}
.facts dt {{ color: var(--secondary); }}
.facts dd {{ margin: 0; color: var(--contrast); text-align: right; white-space: nowrap; font-variant-numeric: tabular-nums; }}
.staff {{ font-size: .82rem; }}
.staff p {{ margin: .3rem 0; }}
ol.asks {{ margin: .3rem 0; padding-left: 1.2rem; }}
ol.asks li {{ margin: .3rem 0; }}
ul.links {{ margin: .3rem 0; padding-left: 1.1rem; font-size: .9rem; }}
footer.card {{ font-size: .82rem; color: var(--secondary); }}
footer.card p {{ margin: .35rem 0; }}

@media (max-width: 960px) {{
  .wrap {{ grid-template-columns: minmax(0, 1fr); }}
  .side {{ position: static; }}
}}
@media (max-width: 640px) {{
  .vs {{ grid-template-columns: 1fr; }}
  .hero h1 {{ font-size: 1.3rem; }}
  .row {{ grid-template-columns: 32px minmax(0, 1fr); }}
  .row img {{ width: 32px; height: 32px; }}
  .row-meta {{ grid-column: 2; flex-direction: row; align-items: flex-start; flex-wrap: wrap; }}
  .topbar nav {{ margin-left: 0; }}
}}
@media print {{
  .topbar nav {{ display: none; }}
  .wrap {{ grid-template-columns: 1fr; }}
  .card {{ box-shadow: none; border: 1px solid #ccc; }}
}}
</style>
</head>
<body>

<header class="topbar">
  <div class="topbar-inner">
    <span class="wordmark">{LOGO.format(s=26)} AI policy, applied twice</span>
    <nav aria-label="Sections">
      <a href="#refusal">Refusal</a><a href="#code">Code</a><a href="#icon">Icon</a><a href="#numbers">Numbers</a><a href="#ask">Ask</a><a href="#method">Method</a>
    </nav>
  </div>
</header>
<p class="notice">Independent write-up by one Modrinth creator. Not affiliated with or endorsed by Modrinth.</p>

<div class="wrap">
<main class="main">

  <section class="card hero">
    <h1>Modrinth’s AI policy is not applied evenly.</h1>
    <p>My submission disclosed its AI use in detail and was refused on <strong>both</strong> grounds: content (§6.2b) and icon (§6.2a).
    Projects disclosing the same, or more, were approved <strong>after the grace period ended</strong> on 27 September 2026.</p>
    <div class="pills">
      <span class="pill pill-rejected">refused 2026-11-09 after 38.4 h</span>
      <span class="pill pill-red">§6.2b: no evidence cited</span>
      <span class="pill pill-red">§6.2a: icon</span>
      <span class="pill pill-approved">17 comparable projects approved after the deadline</span>
    </div>
  </section>

  <section class="card" id="refusal">
    <h2>1. The refusal</h2>
    <p>My disclosure:</p>
    <blockquote><p>“{e(MY_CODE)} {e(MY_ICON)}”</p></blockquote>
    <p>Submitted 2026-11-08 06:01 UTC, rejected 2026-11-09 20:25 UTC with two issues:</p>
    <blockquote class="mod"><p><b>§6.2b</b> “…this project is not suitable to be published publicly on Modrinth. If you believe this is incorrect, please provide
    significant evidence that your project consists of primarily non-AI-generated content. Otherwise, we ask that you <strong>do not resubmit</strong>.”</p>
    <p><b>§6.2a</b> “…images created or significantly altered with AI are not permitted… Please remove the following AI images: Project icon.”</p></blockquote>
    <p>The §6.2a message names and links the image it objects to. The §6.2b message <strong>cites no evidence</strong>: no file, passage or excerpt
    (both issues carry an empty <code>locations</code> field). Because §6.2b also asks me not to
    resubmit, replacing the icon cannot bring the project back. The project page’s own “Changes requested” banner says the opposite, with a warning attached:
    <q>Please address all moderation concerns, including any issues listed in messages below, before resubmitting this project.
    Repeatedly submitting your project without addressing all moderation concerns first may result in account suspension.</q></p>
    <p class="note">Issue text quoted from the moderation record as captured 2026-11-10 03:47 UTC; banner text as shown on the project page on 2026-11-14.
    “§6.2a” and “§6.2b” are the labels used in the moderation messages; the rules page itself has one §6.2. Note that §6.1 <em>requires</em> disclosure when
    “a substantial portion of the project's code is a product of AI output”, so substantial AI code is allowed; only content “primarily or entirely” from AI is not.
    Rule text: <a href="http://web.archive.org/web/20261102101459/https://modrinth.com/legal/rules" rel="noopener">Content Rules §6, archived 2 Nov 2026</a>
    (unchanged since added; <a href="http://web.archive.org/web/20260802000307/https://modrinth.com/legal/rules" rel="noopener">absent on 2 Aug</a>).
    Grace period: <a href="https://modrinth.com/news/article/ai-policy-and-disclosures/" rel="noopener">policy announcement</a>.</p>
  </section>

  <section class="card" id="code">
    <h2><span class="tag">§6.2b</span>2. Code: the same disclosure, approved</h2>
    <div class="mine">{vs(None, "My submission", "pill-rejected", "refused 2026-11-09", MY_CODE + " " + MY_ICON)}</div>
    <div class="vs">
      <div>{vs(CDN + back[8], "Backrooms", "pill-approved", "approved 2026-10-31", back[7])}
      <p class="match">Same: Claude, most of the code, page text, assets, human direction and review.</p></div>
      <div>{vs(CDN + map_[8], "Mystical Agriculture Plus", "pill-approved", "approved 2026-10-23", map_[7])}
      <p class="match">Same: AI-written code, pixel art drawn by AI-written scripts, author’s design and in-game testing.</p></div>
    </div>
    <h3>Code written with AI, in the authors’ own words, approved after the deadline</h3>
    <div class="rows">{code_rows}
    </div>
    <h3>In-mod art from AI or AI-written scripts</h3>
    <p class="note">Textures inside the mod, so not §6.2a page images, but part of the content §6.2b judges.</p>
    <div class="rows">{texture_rows}
    </div>
  </section>

  <section class="card" id="icon">
    <h2><span class="tag">§6.2a</span>3. Icon: the same method, approved</h2>
    <div class="vs">
      {vs(CDN + uhc[8], "UHC Prime", "pill-approved", "approved 2026-10-11", uhc[7])}
      {vs(None, "My submission", "pill-rejected", "icon refused 2026-11-09", "… " + MY_ICON)}
    </div>
    <p>Nexora Players (<q>{e(nexora[7])}</q>, about its icon) was approved on <strong>8 November, the day before</strong>.
    If an image drawn by an AI-written script is an AI image, these are too; if not, mine was refused in error.</p>
    <h3>Icon and artwork disclosures approved after the deadline</h3>
    <div class="rows">{image_rows}
    </div>
  </section>

  <section class="card" id="numbers">
    <h2>4. The numbers</h2>
    <div class="stats">
      <div class="stat"><b>924</b><span>AI-disclosing projects approved after the deadline</span></div>
      <div class="stat hl"><b>921</b><span>of them still public (3 archived)</span></div>
      <div class="stat hl"><b>10</b><span>say AI wrote, or was used for, most or all of their code: all public</span></div>
      <div class="stat"><b>47.1%</b><span>of AI disclosures have no explanation</span></div>
      <div class="stat"><b>38.4 h</b><span>my review; median 179.1 h; 740 approved faster</span></div>
    </div>
    <p class="note">From a collected set of 4,861 public Modrinth projects with content disclosures (4,831 of them disclosing AI), as of 2026-11-10.
    “After the deadline” means approved on or after 28 September 2026. The 10 were found by reading every candidate statement by hand.
    Only public projects are visible, so this shows no rejection rate; it shows that projects disclosing what I disclosed are public.</p>
  </section>

  <section class="card" id="ask">
    <h2>5. What I ask</h2>
    <p>Not that any project above is removed. I would not report them.</p>
    <ol class="asks">
      <li><strong>State the §6.2b threshold.</strong> If “most of the code by AI” fails it, Backrooms, PVP Tiers, Fluidic and others fail too. If human direction, review and testing pass it, my disclosure described exactly that.</li>
      <li><strong>State the §6.2a threshold</strong> for images drawn by AI-written scripts.</li>
      <li><strong>Cite evidence</strong> in §6.2b findings, as §6.2a findings already do.</li>
      <li><strong>Apply the same reading to everyone.</strong> I will rebuild to whatever the standard is.</li>
    </ol>
  </section>

  <section class="card" id="method">
    <h2>6. Method and limits</h2>
    <p>Disclosures (flags and notes) for a collected set of 4,861 public projects, with <code>published</code> (created) and <code>approved</code>
    (went public) from the public API, as of 2026-11-10. Collected and classified with help from AI tools; every project cited here was re-checked by hand
    against the live API on 2026-11-14: <code>approved</code>, dates as shown, quote present word for word. Only projects approved after 27 September 2026 are cited. No moderator is named, and none should be sought;
    I claim inconsistency, not bad faith.</p>
    <ul class="links">
      <li><a href="evidence/corpus_ledger.csv">corpus_ledger.csv</a>: all 4,831 AI-disclosing projects</li>
      <li><a href="evidence/post_grace_ai_authored_core.csv">post_grace_ai_authored_core.csv</a> and <a href="evidence/post_grace_substantial_ai.csv">post_grace_substantial_ai.csv</a>: the post-deadline cases</li>
      <li><a href="evidence/page_image_ai_claims.csv">page_image_ai_claims.csv</a> and <a href="evidence/corpus_stats.json">corpus_stats.json</a></li>
    </ul>
  </section>

  <footer class="card">
    <p><strong>Corrections:</strong> projects change. If an item is outdated or misrepresented, open an issue on this repository and I will correct it with a changelog note.
    Text CC BY 4.0. Data from Modrinth’s public API v2/v3 and the Internet Archive.</p>
  </footer>
</main>

<aside class="side">
  <section class="card">
    <h3>At a glance</h3>
    <dl class="facts">
      <dt>Refused</dt><dd>2026-11-09</dd>
      <dt>Review time</dt><dd>38.4 h</dd>
      <dt>Grounds</dt><dd>§6.2b + §6.2a</dd>
      <dt>Evidence cited</dt><dd>none</dd>
      <dt>Grace ended</dt><dd>2026-09-27</dd>
      <dt>Approved after it</dt><dd>924</dd>
      <dt>“AI wrote most code”</dt><dd>10, all public</dd>
      <dt>Same icon method</dt><dd>approved</dd>
    </dl>
  </section>
  <section class="card staff">
    <h3>For Modrinth staff</h3>
    <p>The refused submission is project <code>nBg1qbWp</code> (rejected 2026-11-09, issues <code>rules-ai-generated</code> and <code>rules-ai-images</code>).</p>
  </section>
</aside>
</div>

</body>
</html>
"""

with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(PAGE)
print("wrote", OUT)
