"""
Pixel-space GitHub profile generator.
Edit the CONFIG block, run `python3 generate_assets.py`, commit README.md + assets/.
Needs: Pillow (only for hero.gif).
"""
import math
import datetime
import os
import random
from PIL import Image

# ------------------------------------------------------------------ CONFIG
USERNAME = "Alfaeran"
LINKEDIN = "alfaeran"                   # linkedin.com/in/<this>; "" drops the badge
EMAIL = "maaurigar@gmail.com"           # "" drops the badge
NAME = "ALFAERAN"                       # big pixel title in hero.gif (letters/digits only)
HERO_SUB = "SYNTHETIC DATA // NLP"      # small line under the title

ABOUT_LINES = [                         # typing animation, A-Z 0-9 . , : - / > only
    "> HELLO WORLD, I AM ALFA",
    "> I BUILD SYNTHETIC DATASETS FOR AI",
    "> FOCUS: INDONESIAN E-COMMERCE NLP",
    "> STATUS: STUDENT / BUILDER / LEARNING",
]

STACK = {                               # SEED LIST - edit to match what you really use
    "DATA AND AI": ["PYTHON", "PANDAS", "NLP", "SYNTHETIC DATA", "TEXT CLASSIFICATION", "DATA LABELING"],
    "BACKEND AND WEB": ["PHP", "SQL", "JAVASCRIPT", "TYPESCRIPT", "REACT", "GO"],
    "TOOLS": ["GIT", "GITHUB", "BASH", "NOTION", "GOOGLE SHEETS", "LOOKER STUDIO", "CLAUDE"],
}

YEAR = str(datetime.date.today().year)  # present year, so the timeline never goes stale

TIMELINE = [                            # (label, [lines]) - alternates above/below the line
    (YEAR, ["SYNTHETIC INDONESIAN", "REVIEW DATASETS"]),
    (YEAR, ["PRICELIST SCANNER", "AND ANALYSIS"]),
    (YEAR, ["ARA 8.0 MARKETING", "SYSTEM"]),
    ("NEXT", ["YOUR NEXT", "BIG REPO"]),
]

REPOS = ["Pricelist-image-scanner-automation-analysis", "Project_Iseng", "FP_INSIS", "BarangTemu-Lost-Found--Project"]   # pinned-repo cards in README
# --------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
os.makedirs(ASSETS, exist_ok=True)
random.seed(8)

FONT = {
    "A": "01110,10001,10001,11111,10001,10001,10001",
    "B": "11110,10001,10001,11110,10001,10001,11110",
    "C": "01110,10001,10000,10000,10000,10001,01110",
    "D": "11110,10001,10001,10001,10001,10001,11110",
    "E": "11111,10000,10000,11110,10000,10000,11111",
    "F": "11111,10000,10000,11110,10000,10000,10000",
    "G": "01110,10001,10000,10111,10001,10001,01111",
    "H": "10001,10001,10001,11111,10001,10001,10001",
    "I": "01110,00100,00100,00100,00100,00100,01110",
    "J": "00111,00010,00010,00010,00010,10010,01100",
    "K": "10001,10010,10100,11000,10100,10010,10001",
    "L": "10000,10000,10000,10000,10000,10000,11111",
    "M": "10001,11011,10101,10101,10001,10001,10001",
    "N": "10001,11001,10101,10011,10001,10001,10001",
    "O": "01110,10001,10001,10001,10001,10001,01110",
    "P": "11110,10001,10001,11110,10000,10000,10000",
    "Q": "01110,10001,10001,10001,10101,10010,01101",
    "R": "11110,10001,10001,11110,10100,10010,10001",
    "S": "01111,10000,10000,01110,00001,00001,11110",
    "T": "11111,00100,00100,00100,00100,00100,00100",
    "U": "10001,10001,10001,10001,10001,10001,01110",
    "V": "10001,10001,10001,10001,10001,01010,00100",
    "W": "10001,10001,10001,10101,10101,10101,01010",
    "X": "10001,10001,01010,00100,01010,10001,10001",
    "Y": "10001,10001,01010,00100,00100,00100,00100",
    "Z": "11111,00001,00010,00100,01000,10000,11111",
    "0": "01110,10001,10011,10101,11001,10001,01110",
    "1": "00100,01100,00100,00100,00100,00100,01110",
    "2": "01110,10001,00001,00010,00100,01000,11111",
    "3": "11110,00001,00001,01110,00001,00001,11110",
    "4": "00010,00110,01010,10010,11111,00010,00010",
    "5": "11111,10000,11110,00001,00001,10001,01110",
    "6": "00110,01000,10000,11110,10001,10001,01110",
    "7": "11111,00001,00010,00100,01000,01000,01000",
    "8": "01110,10001,10001,01110,10001,10001,01110",
    "9": "01110,10001,10001,01111,00001,00010,01100",
    ".": "00000,00000,00000,00000,00000,01100,01100",
    ",": "00000,00000,00000,00000,01100,00100,01000",
    ":": "00000,01100,01100,00000,01100,01100,00000",
    "-": "00000,00000,00000,11111,00000,00000,00000",
    "/": "00001,00010,00010,00100,01000,01000,10000",
    ">": "10000,01000,00100,00010,00100,01000,10000",
}

STYLE = """<style>
.a,.b,.c{animation-timing-function:steps(4,end);animation-iteration-count:infinite}
.a{animation-name:tw;animation-duration:2.4s}
.b{animation-name:tw;animation-duration:3.6s}
.c{animation-name:tw2;animation-duration:5s}
@keyframes tw{0%,100%{opacity:.2}50%{opacity:1}}
@keyframes tw2{0%,100%{opacity:1}50%{opacity:.15}}
.bl{animation:blink 1s steps(1) infinite}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
.march{animation:march 1s steps(2) infinite}
@keyframes march{to{stroke-dashoffset:-16}}
.ty{opacity:0;animation:show .01s forwards}
@keyframes show{to{opacity:1}}
.chip{animation:pulse 4s steps(3) infinite}
@keyframes pulse{0%,100%{opacity:.5}50%{opacity:1}}
.shoot{opacity:0;animation:shoot 8s linear infinite}
@keyframes shoot{0%{transform:translate(0,0);opacity:0}2%{opacity:1}11%{transform:translate(240px,120px);opacity:0}100%{transform:translate(240px,120px);opacity:0}}
.fly{animation:fly 14s steps(70) infinite}
@keyframes fly{from{transform:translateX(-40px)}to{transform:translateX(940px)}}
.fl{animation:blink .3s steps(1) infinite}
.df{animation:df 1.2s steps(1) infinite}
@keyframes df{0%,49%{opacity:.08}50%,100%{opacity:.5}}
.bump{animation:bump 1.2s steps(2) infinite;transform-box:fill-box;transform-origin:center}
@keyframes bump{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}.ty{opacity:1}}
</style>"""


def text_w(text, s):
    return len(text) * 6 * s - s


def pixel_text(text, x, y, s, fill="#fff", per_char=None):
    out, cx = [], x
    for i, ch in enumerate(text):
        g = FONT.get(ch)
        if g:
            rects = []
            for r, row in enumerate(g.split(",")):
                c = 0
                while c < 5:
                    if row[c] == "1":
                        c2 = c
                        while c2 < 5 and row[c2] == "1":
                            c2 += 1
                        rects.append(f'<rect x="{cx + c * s}" y="{y + r * s}" width="{(c2 - c) * s}" height="{s}"/>')
                        c = c2
                    else:
                        c += 1
            attrs = per_char(i) if per_char else ""
            out.append(f'<g fill="{fill}" {attrs}>{"".join(rects)}</g>')
        cx += 6 * s
    return "".join(out)


def cross(x, y, k, p):
    r = [f'<rect x="{x}" y="{y}" width="{p}" height="{p}"/>']
    if k > 0:
        r += [
            f'<rect x="{x - k * p}" y="{y}" width="{k * p}" height="{p}"/>',
            f'<rect x="{x + p}" y="{y}" width="{k * p}" height="{p}"/>',
            f'<rect x="{x}" y="{y - k * p}" width="{p}" height="{k * p}"/>',
            f'<rect x="{x}" y="{y + p}" width="{p}" height="{k * p}"/>',
        ]
    return "".join(r)


def starfield(w, h, n, avoid=None):
    out = []
    for _ in range(n):
        p = random.choice([2, 2, 2, 3, 4])
        k = random.choices([0, 1, 2, 3], [35, 35, 20, 10])[0]
        x, y = random.randrange(10, w - 10, 2), random.randrange(10, h - 10, 2)
        m = k * p + p
        if avoid and any(a - m <= x <= c + m and b - m <= y <= d + m for a, b, c, d in avoid):
            continue
        cls = random.choice("aabbc")
        delay = round(random.uniform(0, 5), 2)
        out.append(f'<g class="{cls}" fill="#fff" style="animation-delay:-{delay}s">{cross(x, y, k, p)}</g>')
    return "".join(out)


def shooting_star(x, y):
    parts = []
    for i in range(9):
        op = round(1 - i * 0.11, 2)
        parts.append(f'<rect x="{x - i * 4}" y="{y - i * 2}" width="2" height="2" fill="#fff" opacity="{op}"/>')
    return f'<g class="shoot" style="animation-delay:{random.randint(0, 5)}s">{"".join(parts)}</g>'


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'shape-rendering="crispEdges">{STYLE}<rect width="{w}" height="{h}" fill="#000"/>{body}</svg>')


def write(name, content):
    with open(os.path.join(ASSETS, name), "w") as f:
        f.write(content)


# ---------------------------------------------------------------- headings
def heading(slug, text):
    w, h, s = 900, 56, 4
    t = "> " + text
    tw = text_w(t, s)
    body = starfield(w, h, 30, avoid=[(0, 0, 24 + tw + 50, h)])
    body += pixel_text(t, 24, 10, s)
    body += f'<rect class="bl" x="{24 + tw + 10}" y="10" width="{3 * s}" height="{7 * s}" fill="#fff"/>'
    body += f'<line x1="0" y1="{h - 4}" x2="{w}" y2="{h - 4}" stroke="#fff" stroke-width="2" stroke-dasharray="8 8" class="march" opacity=".6"/>'
    write(f"heading-{slug}.svg", svg(w, h, body))


# ----------------------------------------------------------------- divider
def divider():
    w, h = 900, 40
    body = starfield(w, h, 34) + shooting_star(40, 6)
    write("divider.svg", svg(w, h, body))


# ------------------------------------------------------------------- about
def about():
    w, s, lh = 900, 3, 38
    h = 24 + lh * len(ABOUT_LINES) + 20
    avoid = [(0, 0, 24 + max(text_w(l, s) for l in ABOUT_LINES) + 50, h)]
    body = starfield(w, h, 60, avoid=avoid)
    t, y = 0.3, 22
    last_end = 24
    for line in ABOUT_LINES:
        base = t
        body += pixel_text(line, 24, y, s, per_char=lambda i, b=base: f'class="ty" style="animation-delay:{b + i * 0.07:.2f}s"')
        last_end = 24 + text_w(line, s)
        t += len(line) * 0.07 + 0.35
        y += lh
    cy = y - lh
    body += (f'<g class="ty" style="animation-delay:{t:.2f}s"><rect class="bl" x="{last_end + 8}" y="{cy}" '
             f'width="{3 * s}" height="{7 * s}" fill="#fff"/></g>')
    write("about.svg", svg(w, h, body))


# ------------------------------------------------------------------- stack
def stack():
    s, pad, ch, gap, maxw, x0 = 2, 16, 40, 12, 876, 24
    y, content, avoid = 20, [], []
    for cat, items in STACK.items():
        label = "// " + cat
        content.append(pixel_text(label, x0, y, s))
        avoid.append((x0, y, x0 + text_w(label, s), y + 14))
        y += 14 + 14
        x = x0
        for item in items:
            w = text_w(item, s) + 2 * pad
            if x + w > x0 + maxw:
                x, y = x0, y + ch + gap
            d = round(random.uniform(0, 4), 2)
            content.append(f'<g class="chip" style="animation-delay:-{d}s"><rect x="{x + 1}" y="{y + 1}" width="{w - 2}" height="{ch - 2}" fill="none" stroke="#fff" stroke-width="2"/></g>')
            content.append(pixel_text(item, x + pad, y + (ch - 14) // 2, s))
            content.append(f'<g class="{random.choice("abc")}" fill="#fff" style="animation-delay:-{d}s">{cross(x + w - 12, y + 8, 1, 2)}</g>')
            avoid.append((x, y, x + w, y + ch))
            x += w + gap
        y += ch + 28
    h = y
    write("stack.svg", svg(900, h, starfield(900, h, 70, avoid=avoid) + "".join(content)))


# ---------------------------------------------------------------- timeline
ROCKET = ["...WWW....", ".FWWWWWW..", "FFWWCWWWWW", ".FWWWWWW..", "...WWW...."]
ROCKET_COL = {"W": "#fff", "C": "#5ef2ff", "F": "#ffaa28"}


def rocket_svg(x, y, s):
    body, flame = [], []
    for r, row in enumerate(ROCKET):
        for c, ch in enumerate(row):
            if ch == ".":
                continue
            rect = f'<rect x="{x + c * s}" y="{y + r * s}" width="{s}" height="{s}" fill="{ROCKET_COL[ch]}"/>'
            (flame if ch == "F" else body).append(rect)
    return f'<g class="fly">{"".join(body)}<g class="fl">{"".join(flame)}</g></g>'


def dancefloor(w, y, rows=2, cw=30, rh=14):
    """Checkerboard floor whose tiles flash in a travelling wave."""
    tiles = []
    for r in range(rows):
        for c in range(w // cw):
            delay = round(((c + r * 2) % 6) * 0.2, 1)
            tiles.append(f'<rect class="df" x="{c * cw}" y="{y + r * rh}" width="{cw - 2}" '
                         f'height="{rh - 2}" fill="#fff" style="animation-delay:-{delay}s"/>')
    return "".join(tiles)


def timeline():
    w, h, ly = 900, 290, 148
    xs = [150, 360, 570, 780]
    body_stars_avoid = [(0, ly - 6, w, ly + 6)]
    items = []
    for i, (label, lines) in enumerate(TIMELINE):
        x = xs[i]
        up = i % 2 == 0
        block_h = 21 + 10 + len(lines) * 20
        top = ly - 34 - block_h if up else ly + 34
        lw = max([text_w(label, 3)] + [text_w(l, 2) for l in lines])
        body_stars_avoid.append((x - lw // 2, top, x + lw // 2, top + block_h))
        items.append(f'<g class="bump" style="animation-delay:-{i * 0.3:.1f}s">'
                     f'{pixel_text(label, x - text_w(label, 3) // 2, top, 3)}</g>')
        for j, l in enumerate(lines):
            items.append(pixel_text(l, x - text_w(l, 2) // 2, top + 31 + j * 20, 2, fill="#bdbdbd"))
        # stem + node
        sy1, sy2 = (top + block_h + 6, ly - 10) if up else (ly + 10, top - 6)
        items.append(f'<line x1="{x}" y1="{sy1}" x2="{x}" y2="{sy2}" stroke="#fff" stroke-width="2" stroke-dasharray="4 4" opacity=".5"/>')
        items.append(f'<g class="{"ab"[i % 2]}" fill="#fff" style="animation-delay:-{i * 0.7}s">{cross(x - 2, ly - 2, 4, 4)}</g>')
    line = f'<line x1="0" y1="{ly + 1}" x2="{w}" y2="{ly + 1}" stroke="#fff" stroke-width="2" stroke-dasharray="8 8" class="march" opacity=".5"/>'
    body = (starfield(w, h, 60, avoid=body_stars_avoid) + dancefloor(w, h - 32) + line
            + "".join(items) + rocket_svg(0, ly - 24, 3) + shooting_star(20, 8))
    write("timeline.svg", svg(w, h, body))


# --------------------------------------------------------------------- GIF
def hero_gif():
    W, H, S, N = 225, 75, 4, 48
    grays = [i * 17 for i in range(16)]
    acc = [(94, 242, 255), (255, 77, 77), (255, 170, 40), (255, 230, 90)]
    pal = []
    for g in grays:
        pal += [g, g, g]
    for c in acc:
        pal += list(c)
    pal += [0] * (768 - len(pal))
    palimg = Image.new("P", (1, 1))
    palimg.putpalette(pal)

    def gray(v):
        v = max(0, min(255, int(v)))
        g = round(v / 17) * 17
        return (g, g, g)

    def put(im, x, y, c):
        if 0 <= x < W and 0 <= y < H:
            im.putpixel((x, y), c)

    def draw_text(im, text, x, y, s, c):
        cx = x
        for ch in text:
            g = FONT.get(ch)
            if g:
                for r, row in enumerate(g.split(",")):
                    for cc, bit in enumerate(row):
                        if bit == "1":
                            for dx in range(s):
                                for dy in range(s):
                                    put(im, cx + cc * s + dx, y + r * s + dy, c)
            cx += 6 * s

    rnd = random.Random(8)
    stars = []
    while len(stars) < 95:
        x, y = rnd.randrange(3, W - 3), rnd.randrange(3, H - 3)
        if 6 <= x <= 160 and 12 <= y <= 60:      # keep title area clean
            continue
        if x > 160 and 14 <= y <= 62:            # keep planet area clean
            continue
        k = rnd.choices([0, 1, 2, 3], [45, 30, 17, 8])[0]
        stars.append((x, y, k, rnd.random(), rnd.choice([1, 1, 2])))

    pcx, pcy, R = 192, 40, 16
    frames = []
    for f in range(N):
        im = Image.new("RGB", (W, H), (0, 0, 0))

        # twinkling cross stars
        for x, y, k, ph, m in stars:
            v = 0.2 + 0.8 * (0.5 + 0.5 * math.sin(2 * math.pi * (m * f / N + ph)))
            c, ca = gray(v * 255), gray(v * 150)
            put(im, x, y, c)
            for d in range(1, k + 1):
                for ax, ay in ((d, 0), (-d, 0), (0, d), (0, -d)):
                    put(im, x + ax, y + ay, ca)

        # shooting star
        if 8 <= f < 22:
            i = f - 8
            hx, hy = 30 + i * 6, 2 + int(i * 1.2)
            for t in range(9):
                put(im, hx - t * 3, hy - int(t * 0.7), gray(255 * (1 - t * 0.11)))

        # ring (back half hidden behind the planet), planet, ring front, moon
        def ring_hit(dx, dy):
            dyt = dy + 0.2 * dx
            eo = (dx / 28) ** 2 + (dyt / 7) ** 2
            ei = (dx / 21) ** 2 + (dyt / 5) ** 2
            return eo <= 1 and ei >= 1, dyt

        bayer = [[0.0, 0.5], [0.75, 0.25]]
        lv = [40, 100, 165, 235]
        for y in range(pcy - R, pcy + R + 1):
            for x in range(pcx - R, pcx + R + 1):
                dx, dy = x - pcx, y - pcy
                d2 = dx * dx + dy * dy
                if d2 > R * R:
                    continue
                nz = math.sqrt(max(0, 1 - d2 / (R * R)))
                dot = max(0, -0.5 * dx / R - 0.6 * dy / R + 0.6 * nz)
                lvl = dot * 3.2 + bayer[y % 2][x % 2] * 0.9 - 0.2
                lvl = int(max(0, min(3, lvl)))
                if (((x - f) // 6) + y // 4) % 4 == 0:
                    lvl = min(3, lvl + 1)
                put(im, x, y, gray(lv[lvl]))
        for y in range(pcy - 14, pcy + 15):
            for x in range(pcx - 30, pcx + 31):
                dx, dy = x - pcx, y - pcy
                hit, dyt = ring_hit(dx, dy)
                if not hit:
                    continue
                if dyt < 0 and dx * dx + dy * dy <= R * R:
                    continue
                put(im, x, y, gray(210 if dyt >= 0 else 110))
        ang = 2 * math.pi * f / N
        mx, my = pcx + int(30 * math.cos(ang)), pcy + int(11 * math.sin(ang)) - int(0.2 * 30 * math.cos(ang))
        behind = math.sin(ang) < 0
        for yy in range(-2, 3):
            for xx in range(-2, 3):
                if xx * xx + yy * yy <= 5:
                    px, py = mx + xx, my + yy
                    if behind and (px - pcx) ** 2 + (py - pcy) ** 2 <= R * R:
                        continue
                    put(im, px, py, gray(235 if xx + yy < 1 else 150))

        # title + subtitle
        draw_text(im, NAME, 13, 21, 3, gray(60))
        draw_text(im, NAME, 12, 20, 3, (255, 255, 255))
        draw_text(im, HERO_SUB, 13, 48, 1, gray(190))
        if (f // 6) % 2 == 0:
            cx = 13 + text_w(HERO_SUB, 1) + 3
            for yy in range(7):
                for xx in range(4):
                    put(im, cx + xx, 48 + yy, (255, 255, 255))

        # rocket
        rx = int(-14 + f * (W + 28) / N)
        ry = 8 + int(round(1.5 * math.sin(2 * math.pi * 2 * f / N)))
        cols = {"W": (255, 255, 255), "C": acc[0], "R": acc[1], "F": acc[2] if f % 2 == 0 else acc[3]}
        for r, row in enumerate(ROCKET):
            for c, ch in enumerate(row):
                if ch != ".":
                    put(im, rx + c, ry + r, cols[ch])

        big = im.resize((W * S, H * S), Image.NEAREST).quantize(palette=palimg, dither=0)
        frames.append(big)

    frames[0].save(os.path.join(ASSETS, "hero.gif"), save_all=True, append_images=frames[1:],
                   duration=80, loop=0, optimize=False, disposal=1)


# ------------------------------------------------------------------ README
def readme():
    u = USERNAME
    card = "theme=dark&bg_color=000000&border_color=ffffff&title_color=ffffff&icon_color=ffffff&text_color=bdbdbd"
    pins = ""
    for i in range(0, len(REPOS), 2):
        pins += "<tr>\n"
        for r in REPOS[i:i + 2]:
            pins += (f'<td><a href="https://github.com/{u}/{r}"><img src="https://github-readme-stats.vercel.app/api/pin/'
                     f'?username={u}&repo={r}&{card}" width="420"/></a></td>\n')
        pins += "</tr>\n"
    badge = "style=flat-square&logoColor=white&labelColor=000000&color=ffffff"
    links = [f'<a href="https://github.com/{u}"><img src="https://img.shields.io/badge/GITHUB-000000?{badge}&logo=github"/></a>']
    if LINKEDIN:
        links.append(f'<a href="https://linkedin.com/in/{LINKEDIN}"><img src="https://img.shields.io/badge/LINKEDIN-000000?{badge}&logo=linkedin"/></a>')
    if EMAIL:
        links.append(f'<a href="mailto:{EMAIL}"><img src="https://img.shields.io/badge/EMAIL-000000?{badge}&logo=gmail"/></a>')
    contact = "\n".join(links)
    md = f"""<div align="center">

<img src="assets/hero.gif" width="100%" alt="pixel space banner"/>

<img src="assets/about.svg" width="100%" alt="about me"/>

</div>

<img src="assets/heading-projects.svg" width="100%" alt="projects"/>

<table align="center">
{pins}</table>

<img src="assets/heading-stack.svg" width="100%" alt="tech stack"/>

<img src="assets/stack.svg" width="100%" alt="tech stack"/>

<img src="assets/heading-history.svg" width="100%" alt="history"/>

<img src="assets/timeline.svg" width="100%" alt="timeline"/>

<img src="assets/heading-stats.svg" width="100%" alt="stats"/>

<p align="center">
<img src="https://github-readme-stats.vercel.app/api?username={u}&show_icons=true&hide_border=false&{card}" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username={u}&layout=compact&hide_border=false&{card}" height="165"/>
</p>

<img src="assets/heading-contact.svg" width="100%" alt="contact"/>

<p align="center">
{contact}
</p>

<img src="assets/divider.svg" width="100%" alt=""/>
"""
    with open(os.path.join(HERE, "README.md"), "w") as f:
        f.write(md)


if __name__ == "__main__":
    for slug, text in [("projects", "PROJECTS"), ("stack", "TECH STACK"), ("history", "HISTORY"),
                       ("stats", "STATS"), ("contact", "CONTACT")]:
        heading(slug, text)
    divider()
    about()
    stack()
    timeline()
    hero_gif()
    readme()
    print("done")
