#!/usr/bin/env python3
"""acra-secretsscanner wordmark banner: the moss garden after rain from its edge,
a closed gate at the left with shoes beside it, the name in Assistant on a dark board at the gate."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(83)
HERE = __file__.rsplit('/', 1)[0]
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE + '/banner.png'
W, H = 1200, 420
GREENS = [(46, 96, 44), (62, 118, 52), (78, 138, 60), (34, 78, 38), (96, 156, 74), (54, 108, 58)]
img = Image.new('RGB', (W, H), (22, 48, 26))
d = ImageDraw.Draw(img, 'RGBA')
# far shade behind the fence
for y in range(0, 150):
    d.line([(0, y), (W, y)], fill=(int(20 + 14 * y / 150), int(46 + 16 * y / 150), int(24 + 10 * y / 150)))
# maple trunks rising out of frame, behind and within the field
trunks = [(150, 46), (420, 60), (700, 52), (950, 66), (1140, 44)]
for (tx, tw) in trunks:
    d.polygon([(tx - tw / 2, H), (tx - tw * 0.3, 0), (tx + tw * 0.3, 0), (tx + tw / 2, H)], fill=(54, 46, 36))
    d.polygon([(tx - tw / 2, H), (tx - tw * 0.08, 0), (tx + tw * 0.06, 0), (tx + tw * 0.12, H)], fill=(70, 60, 46))
# low bamboo fence at the far side, where looking stops
for fx in range(16, W, 24):
    d.line([(fx, 128), (fx, 176)], fill=(150, 132, 88), width=5)
d.line([(8, 140), (W - 8, 140)], fill=(124, 108, 70), width=3)
d.line([(8, 164), (W - 8, 164)], fill=(124, 108, 70), width=3)
img = img.filter(ImageFilter.GaussianBlur(1.1))
d = ImageDraw.Draw(img, 'RGBA')

def cushion(cx, cy, rw, rh, strokes, slen, bright=False):
    base = (58, 124, 56) if bright else random.choice(GREENS[:4])
    d.ellipse([cx - rw, cy - rh, cx + rw, cy + rh], fill=base)
    for _ in range(strokes):
        a = random.uniform(0, math.pi * 2); rr = math.sqrt(random.uniform(0, 1))
        x = cx + math.cos(a) * rr * rw * 0.94; y = cy + math.sin(a) * rr * rh * 0.9
        ang = random.uniform(0, math.pi * 2)
        g = random.choice(GREENS) if not bright else random.choice([(96, 156, 74), (110, 172, 84), (78, 138, 60)])
        d.line([(x, y), (x + math.cos(ang) * slen, y + math.sin(ang) * slen)], fill=g, width=2)
    for _ in range(int(rw * 0.35)):
        x = cx + random.uniform(-rw * 0.8, rw * 0.8); y = cy + random.uniform(-rh * 0.6, rh * 0.6)
        d.ellipse([x, y, x + 2.2, y + 1.5], fill=(226, 244, 205, random.randint(100, 200)))

# the moss field: lower two thirds, cushions of many textures running under the trunks
random.seed(19)
for row, (cy, rh, sl) in enumerate([(196, 20, 3.5), (228, 26, 4.5), (268, 32, 5.5), (316, 40, 6.5), (372, 50, 8)]):
    x = -10 + row * 14
    while x < W + 10:
        rw = random.uniform(50, 92)
        cushion(x + rw * 0.5, cy + random.uniform(-5, 5), rw * 0.62, rh * 0.6, int(rw * 2.8), sl)
        x += rw * random.uniform(0.84, 0.98)
# brightest cushion near the centre, where the canopy light lands
cushion(640, 300, 74, 30, 340, 6, bright=True)
# soft shadows thrown across the green by every trunk, laid over the field
for (tx, tw) in trunks:
    d.polygon([(tx + tw * 0.2, 190), (tx + tw * 0.85, 190), (tx + 250, H), (tx + 120, H)], fill=(14, 38, 18, 62))
# dappled coins and shafts through the canopy
for _ in range(60):
    x = random.uniform(60, W - 40); y = random.uniform(150, 400); r = random.uniform(4, 14)
    d.ellipse([x - r, y - r * 0.45, x + r, y + r * 0.45], fill=(218, 238, 165, random.randint(36, 90)))
# fallen leaves spotted sparsely in amber
def maple_leaf(cx, cy, s, ang_deg):
    shape = [(0, -1.0), (0.16, -0.52), (0.5, -0.78), (0.44, -0.34), (0.86, -0.4), (0.58, -0.06), (0.98, 0.08), (0.52, 0.24), (0.62, 0.62), (0.2, 0.42), (0.07, 0.86), (-0.07, 0.86), (-0.2, 0.42), (-0.62, 0.62), (-0.52, 0.24), (-0.98, 0.08), (-0.58, -0.06), (-0.86, -0.4), (-0.44, -0.34), (-0.5, -0.78), (-0.16, -0.52)]
    a = math.radians(ang_deg)
    pts = [(cx + (x * math.cos(a) - y * math.sin(a)) * s, cy + (x * math.sin(a) + y * math.cos(a)) * s) for (x, y) in shape]
    d.polygon(pts, fill=(198, 130, 40))
    if s > 16:
        for (vx, vy) in [(0, -0.9), (0.5, 0.1), (-0.5, 0.1)]:
            d.line([(cx, cy), (cx + vx * s, cy + vy * s)], fill=(168, 106, 34), width=1)
for (lx, ly, ls, la) in [(512, 244, 15, 30), (852, 286, 18, -20), (1050, 350, 21, 55), (356, 348, 17, 10), (760, 386, 15, -48), (196, 268, 13, 70)]:
    maple_leaf(lx, ly, ls, la)
# closed wooden gate at the left foreground, shoes set neatly beside it on a stone step
gx, gy, gw, gh = 26, 196, 150, 196
d.rectangle([gx + 6, gy + 10, gx + gw + 10, gy + gh + 8], fill=(30, 24, 18))  # gate shadow
for px in (gx, gx + gw - 12):
    d.rectangle([px, gy - 14, px + 12, gy + gh], fill=(66, 52, 38))
for i in range(5):
    x0 = gx + 10 + i * 27
    d.rectangle([x0, gy, x0 + 20, gy + gh - 30], fill=(96, 76, 54))
    d.line([(x0 + 3, gy + 8), (x0 + 3, gy + gh - 38)], fill=(80, 62, 44), width=2)
d.rectangle([gx + 4, gy + 34, gx + gw - 4, gy + 44], fill=(74, 58, 42))
d.rectangle([gx + 4, gy + 128, gx + gw - 4, gy + 138], fill=(74, 58, 42))
# stone step with a pair of shoes beside the gate
d.polygon([(gx + gw + 8, gy + gh - 26), (gx + gw + 92, gy + gh - 26), (gx + gw + 100, gy + gh - 4), (gx + gw, gy + gh - 4)], fill=(150, 146, 136))
for sx in (gx + gw + 20, gx + gw + 56):
    d.polygon([(sx, gy + gh - 40), (sx + 26, gy + gh - 40), (sx + 31, gy + gh - 27), (sx + 29, gy + gh - 19), (sx, gy + gh - 19)], fill=(50, 48, 54))
    d.line([(sx + 3, gy + gh - 35), (sx + 21, gy + gh - 35)], fill=(214, 210, 200), width=2)
    d.line([(sx + 1, gy + gh - 19), (sx + 29, gy + gh - 19)], fill=(30, 28, 32), width=3)
# small dark wooden label board at the gate, the name in Assistant in pale paint
bx, by, bw, bh = gx + 16, gy + 58, 196, 52
d.rectangle([bx, by, bx + bw, by + bh], fill=(44, 36, 28), outline=(24, 19, 15), width=2)
f = ImageFont.truetype(HERE + '/fonts/Assistant.ttf', 21)
try:
    f.set_variation_by_axes([600])
except Exception:
    pass
t = 'acra-secretsscanner'
bb = d.textbbox((0, 0), t, font=f)
d.text((bx + bw / 2 - (bb[2] - bb[0]) / 2 - bb[0], by + bh / 2 - (bb[3] - bb[1]) / 2 - bb[1]), t, font=f, fill=(238, 234, 216))
img = img.filter(ImageFilter.GaussianBlur(0.4))
img.save(OUT)
print('saved', OUT)
