#!/usr/bin/env python3
"""acra-secretsscanner logo: one moss cushion from above, a raked gravel ring, one amber maple leaf,
name in Assistant quiet capitals on a paper white specimen strip."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont
random.seed(61)
HERE = __file__.rsplit('/', 1)[0]
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/logo.png'
W, H = 900, 600
PAPER = (250, 248, 240); DGREEN = (30, 66, 34)
img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img, 'RGBA')
cx, cy, R = 450, 238, 168
# raked pale gravel ring: fine concentric arcs, broken at the lower right where sprigs trail across
for rr in range(R + 16, R + 58, 7):
    start = random.uniform(0, 40)
    d.arc([cx - rr, cy - rr, cx + rr, cy + rr], start, 302, fill=(168, 160, 140), width=2)
    d.arc([cx - rr, cy - rr, cx + rr, cy + rr], 330, 360 + start * 0.4, fill=(168, 160, 140), width=2)
# gravel bed speckle inside and outside the ring
for _ in range(500):
    a = random.uniform(0, math.pi * 2); rr = R + random.uniform(4, 66)
    x, y = cx + math.cos(a) * rr, cy + math.sin(a) * rr
    d.ellipse([x, y, x + 2.6, y + 1.8], fill=random.choice([(190, 182, 160), (205, 198, 178), (172, 164, 142)]))
# the cushion: a low dome of hundreds of tiny overlapping leaf strokes, darkest at the centre.
# Its edge is ragged: the radius wobbles by angle, and strokes follow that wobble.
wob = [1 + 0.045 * math.sin(a * 3.1 + 1.2) + 0.03 * math.sin(a * 7.7) + random.uniform(-0.012, 0.012) for a in [i * math.pi / 180 for i in range(360)]]
def edge_r(a):
    return wob[int(math.degrees(a) % 360)]
d.ellipse([cx - R, cy - R * 0.92, cx + R, cy + R * 0.92], fill=(38, 84, 40))
for i in range(2400):
    a = random.uniform(0, math.pi * 2); rr = math.sqrt(random.uniform(0, 1)) * edge_r(a)
    x = cx + math.cos(a) * rr * R * 0.97; y = cy + math.sin(a) * rr * R * 0.89
    depth = 1 - rr  # 1 at the centre
    g = random.choice([(28 + int(30 * (1 - depth)), 70 + int(52 * (1 - depth)), 32 + int(26 * (1 - depth))),
                       (44, 102, 46), (58, 122, 54), (70, 138, 60)])
    ang = random.uniform(0, math.pi * 2); ln = random.uniform(3.5, 6.5)
    d.line([(x, y), (x + math.cos(ang) * ln, y + math.sin(ang) * ln)], fill=g, width=2)
    if random.random() < 0.3:
        d.point((x, y), fill=(126, 184, 100))
# ragged natural edge: single sprigs trailing onto the gravel, crossing the ring at the lower right
for k in range(9):
    a = math.radians(random.uniform(18, 74))
    sx, sy = cx + math.cos(a) * R * 0.9, cy + math.sin(a) * R * 0.84
    pts = [(sx + math.cos(a) * s * 58 + random.uniform(-3, 3), sy + math.sin(a) * s * 58 + random.uniform(-3, 3)) for s in [i / 6 for i in range(7)]]
    d.line(pts, fill=(52, 112, 50), width=3)
    for (px, py) in pts[1:]:
        d.line([(px, py), (px + random.uniform(-6, 6), py + random.uniform(-6, 6))], fill=(70, 138, 60), width=2)
for k in range(5):  # a few sprigs at other edges, shorter
    a = math.radians(random.uniform(120, 330))
    sx, sy = cx + math.cos(a) * R * 0.94, cy + math.sin(a) * R * 0.88
    d.line([(sx, sy), (sx + math.cos(a) * 20, sy + math.sin(a) * 20)], fill=(52, 112, 50), width=3)

def maple_leaf(cx2, cy2, s, ang_deg):
    shape = [(0, -1.0), (0.16, -0.52), (0.5, -0.78), (0.44, -0.34), (0.86, -0.4), (0.58, -0.06), (0.98, 0.08), (0.52, 0.24), (0.62, 0.62), (0.2, 0.42), (0.07, 0.86), (-0.07, 0.86), (-0.2, 0.42), (-0.62, 0.62), (-0.52, 0.24), (-0.98, 0.08), (-0.58, -0.06), (-0.86, -0.4), (-0.44, -0.34), (-0.5, -0.78), (-0.16, -0.52)]
    a = math.radians(ang_deg)
    pts = [(cx2 + (x * math.cos(a) - y * math.sin(a)) * s, cy2 + (x * math.sin(a) + y * math.cos(a)) * s) for (x, y) in shape]
    d.polygon(pts, fill=(206, 138, 44))
    d.line([(cx2, cy2 + s * 0.8), (cx2 + s * 0.12, cy2 + s * 1.2)], fill=(150, 96, 30), width=3)
    for (vx, vy) in [(0, -0.9), (0.5, 0.1), (-0.5, 0.1)]:
        d.line([(cx2, cy2), (cx2 + vx * s, cy2 + vy * s)], fill=(176, 112, 36), width=2)

# one fallen maple leaf on the dome, off centre, the only warm colour
maple_leaf(cx - 52, cy - 30, 40, -14)
# specimen strip: paper white with a hairline rule, name in Assistant quiet capitals
sy = 486
d.line([(110, sy - 16), (W - 110, sy - 16)], fill=(120, 130, 118), width=1)
f = ImageFont.truetype(HERE + '/fonts/Assistant.ttf', 37)
try:
    f.set_variation_by_axes([600])
except Exception:
    pass
t2 = 'acra-secretsscanner'
bb = d.textbbox((0, 0), t2, font=f)
d.text(((W - (bb[2] - bb[0])) / 2 - bb[0], sy), t2, font=f, fill=DGREEN)
d.line([(110, sy + 58), (W - 110, sy + 58)], fill=(120, 130, 118), width=1)
img.save(OUT)
img.resize((72, 48)).save(HERE + '/scratch/logo64-ship.png')
print('saved', OUT)
