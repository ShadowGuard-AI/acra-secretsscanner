#!/usr/bin/env python3
"""acra-secretsscanner intro banner: moss garden of Saiho-ji after rain, close moss, no lettering anywhere."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(43)
HERE = __file__.rsplit('/', 1)[0]
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/intro-banner.png'
W, H = 1200, 520
GREENS = [(46, 96, 44), (62, 118, 52), (78, 138, 60), (34, 78, 38), (96, 156, 74), (54, 108, 58)]
AMBER = (206, 138, 44)
img = Image.new('RGB', (W, H), (24, 52, 28))
d = ImageDraw.Draw(img, 'RGBA')
# background: trunks rising into a closed canopy, shade deepening between them
for tx in (90, 300, 520, 760, 990, 1140):
    wd = random.uniform(34, 58)
    d.polygon([(tx - wd / 2, 190), (tx - wd * 0.32, 0), (tx + wd * 0.32, 0), (tx + wd / 2, 190)], fill=(52, 44, 34))
    d.polygon([(tx - wd / 2, 190), (tx - wd * 0.1, 0), (tx + wd * 0.05, 0), (tx + wd * 0.1, 190)], fill=(66, 56, 44))
# canopy closing the top of the frame, light filtering green through leaves
for _ in range(420):
    x = random.uniform(-20, W + 20); y = random.uniform(-40, 128); r = random.uniform(10, 34)
    d.ellipse([x - r, y - r * 0.7, x + r, y + r * 0.7], fill=random.choice([(26, 66, 30, 150), (38, 88, 38, 150), (52, 108, 46, 140), (20, 54, 26, 160)]))
# shade gradient under the canopy so the top closes rather than opening to sky
for y in range(0, 150):
    d.line([(0, y), (W, y)], fill=(16, 40, 20, int(70 * (1 - y / 150))))
for _ in range(46):  # coins of filtered light
    x = random.uniform(0, W); y = random.uniform(0, 130); r = random.uniform(4, 13)
    d.ellipse([x - r, y - r * 0.5, x + r, y + r * 0.5], fill=(214, 236, 160, random.randint(50, 120)))
# hint of the bamboo fence far back
for fx in range(30, W, 26):
    d.line([(fx, 196), (fx, 246)], fill=(146, 128, 84), width=5)
d.line([(20, 208), (W - 20, 208)], fill=(120, 104, 66), width=3)
d.line([(20, 234), (W - 20, 234)], fill=(120, 104, 66), width=3)
img = img.filter(ImageFilter.GaussianBlur(2.3))
d = ImageDraw.Draw(img, 'RGBA')
# moss ground shadow under the midground field so gaps between cushions read as shade, not void
d.rectangle([0, 238, W, 420], fill=(26, 60, 30))

def cushion(cx, cy, rw, rh, base_green, stroke_n, stroke_len):
    d.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=base_green)
    for _ in range(stroke_n):
        a = random.uniform(0, math.pi * 2); rr = math.sqrt(random.uniform(0, 1))
        x = cx + math.cos(a) * rr * rw * 0.94; y = cy + math.sin(a) * rr * rh * 0.9
        g = random.choice(GREENS)
        ang = random.uniform(0, math.pi * 2)
        d.line([(x, y), (x + math.cos(ang) * stroke_len, y + math.sin(ang) * stroke_len)], fill=g, width=2)
        d.point((x, y), fill=random.choice([(120, 178, 96), (140, 196, 110)]))
    # water held between the leaves: small bright points from recent rain
    for _ in range(int(rw * 0.5)):
        x = cx + random.uniform(-rw * 0.85, rw * 0.85); y = cy + random.uniform(-rh * 0.7, rh * 0.7)
        d.ellipse([x, y, x + 2.4, y + 1.6], fill=(226, 244, 205, random.randint(120, 220)))

# gravel maintenance border running along the right side, empty
d.polygon([(1064, 250), (1200, 240), (1200, 520), (1096, 520)], fill=(186, 178, 156))
for _ in range(260):
    x = random.uniform(1076, 1196); y = random.uniform(252, 516)
    d.ellipse([x, y, x + random.uniform(2, 5), y + random.uniform(1.5, 3.5)], fill=random.choice([(168, 160, 138), (198, 190, 168), (150, 142, 120)]))
for gy in (300, 360, 420, 480):
    d.arc([1050, gy - 26, 1230, gy + 26], 190, 340, fill=(158, 150, 128), width=1)
# midground field: cushions changing texture in patches, unbroken, edges staggered
random.seed(97)
for row, (cy, rh) in enumerate([(268, 26), (306, 32), (352, 40)]):
    x = 16 + row * 30 + random.uniform(-8, 8)
    while x < 1020:
        rw = random.uniform(52, 100)
        cushion(x + rw * 0.5, cy + random.uniform(-7, 7), rw * 0.62, rh * 0.62, random.choice(GREENS[:4]), int(rw * 3.0), random.uniform(3.5, 7))
        x += rw * random.uniform(0.82, 0.97)
# fern at the base of one trunk in the near midground, fronds partly uncurled
fx, fy = 512, 398
for k in range(7):
    a = -math.pi * (0.14 + 0.12 * k)
    pts = [(fx + math.cos(a) * s * 96 - math.sin(s * 2.4 + k) * 6 * s, fy - abs(math.sin(a)) * s * 16 - s * s * 66) for s in [i / 10 for i in range(11)]]
    d.line(pts, fill=(84, 164, 76), width=3)
    for si in range(2, 11):
        px, py = pts[si]
        d.line([(px, py), (px - 9, py + 4)], fill=(104, 184, 94), width=2)
        d.line([(px, py), (px + 9, py + 4)], fill=(104, 184, 94), width=2)
d.arc([fx + 66, fy - 96, fx + 108, fy - 54], 180, 330, fill=(84, 164, 76), width=3)  # one frond still curled
# foreground: moss at close range, leaf strokes visible, filling the bottom of the frame
cushion(210, 486, 265, 92, (40, 88, 40), 1500, 9)
cushion(560, 506, 300, 96, (36, 82, 36), 1600, 9)
cushion(905, 492, 235, 86, (44, 94, 42), 1300, 9)

def maple_leaf(cx, cy, s, ang_deg):
    pts = []
    shape = [(0, -1.0), (0.16, -0.52), (0.5, -0.78), (0.44, -0.34), (0.86, -0.4), (0.58, -0.06), (0.98, 0.08), (0.52, 0.24), (0.62, 0.62), (0.2, 0.42), (0.07, 0.86), (-0.07, 0.86), (-0.2, 0.42), (-0.62, 0.62), (-0.52, 0.24), (-0.98, 0.08), (-0.58, -0.06), (-0.86, -0.4), (-0.44, -0.34), (-0.5, -0.78), (-0.16, -0.52)]
    a = math.radians(ang_deg)
    for (x, y) in shape:
        pts.append((cx + (x * math.cos(a) - y * math.sin(a)) * s, cy + (x * math.sin(a) + y * math.cos(a)) * s))
    d.polygon(pts, fill=AMBER)
    d.line([(cx, cy + s * 0.8), (cx + s * 0.14, cy + s * 1.24)], fill=(150, 96, 30), width=3)
    for (vx, vy) in [(0, -0.9), (0.5, 0.1), (-0.5, 0.1), (0.16, 0.5), (-0.16, 0.5)]:
        d.line([(cx, cy), (cx + vx * s, cy + vy * s)], fill=(176, 112, 36), width=2)

# one amber maple leaf settled on the nearest cushion
maple_leaf(252, 452, 44, 18)
img = img.filter(ImageFilter.GaussianBlur(0.45))
img.save(OUT)
print('saved', OUT)
