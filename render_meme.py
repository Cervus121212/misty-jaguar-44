#!/usr/bin/env python3
"""Render the GTA 6 meme for make.fun bounty gta6-meme-x-01.

Original artwork drawn with PIL (no AI image gen, no stock photos).
The make.fun ghost is the official press-kit mark (mark-1024.png), which the
bounty requires to appear in the picture.

Concept: Vice City sunset. After 13 years of waiting, the make.fun ghost
rides shotgun in a pink convertible toward the Leonida sun on launch day,
19 Nov 2026. Top text states the wait, footer states the payoff + make.fun.

Deterministic: fixed seed, no timestamps, no network.
Output: meme.png (1024x1024).
"""
import math
import random

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "meme.png"
ASSETS = "assets"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

random.seed(7)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def sky_gradient(draw):
    # deep purple -> magenta -> orange, top to horizon (y=740)
    stops = [(0.0, (24, 8, 58)), (0.35, (91, 26, 110)),
             (0.62, (198, 43, 122)), (0.85, (255, 94, 98)),
             (1.0, (255, 179, 71))]
    top, bottom = 0, 740
    for y in range(top, bottom):
        t = (y - top) / (bottom - top)
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                f = 0 if t1 == t0 else (t - t0) / (t1 - t0)
                draw.line([(0, y), (W, y)], fill=lerp(c0, c1, f))
                break


def draw_sun(draw):
    cx, cy, r = 300, 400, 160
    # vertical gradient disc: yellow core -> orange -> pink rim
    for i in range(r, 0, -1):
        t = i / r
        if t > 0.66:
            c = lerp((255, 214, 64), (255, 140, 66), (t - 0.66) / 0.34)
        else:
            c = lerp((255, 140, 66), (255, 80, 120), 1 - t / 0.66)
        draw.ellipse([cx - i, cy - i, cx + i, cy + i], fill=c)
    # synthwave slats across the lower half, clipped to the disc, growing
    # thicker downward
    y = cy + 18
    gap = 7
    thick = 4
    while y < cy + r:
        half = int(math.sqrt(max(0, r * r - (y - cy) ** 2)))
        draw.rectangle([cx - half, y, cx + half, y + thick],
                       fill=(255, 94, 98))
        y += gap + thick
        gap = max(4, gap - 1)
        thick += 3


def draw_stars(draw):
    for _ in range(90):
        x = random.randint(0, W - 1)
        y = random.randint(0, 300)
        s = random.choice([1, 1, 2])
        a = random.randint(120, 255)
        draw.ellipse([x, y, x + s, y + s], fill=(255, 255, 255, a))


def draw_skyline(draw):
    base = 740
    col = (22, 8, 38)
    x = 0
    heights = [120, 190, 90, 230, 150, 260, 110, 200, 140, 240, 100,
               180, 130, 210, 95, 170, 250, 120]
    i = 0
    while x < W:
        bw = random.randint(46, 84)
        bh = heights[i % len(heights)] + random.randint(-15, 15)
        draw.rectangle([x, base - bh, x + bw, base], fill=col)
        # antenna on the tallest
        if bh > 230:
            draw.line([(x + bw // 2, base - bh), (x + bw // 2, base - bh - 26)],
                      fill=col, width=4)
            draw.ellipse([x + bw // 2 - 3, base - bh - 32,
                          x + bw // 2 + 3, base - bh - 26], fill=(255, 80, 90))
        # lit windows
        for wy in range(base - bh + 12, base - 14, 22):
            for wx in range(x + 8, x + bw - 8, 18):
                if random.random() < 0.28:
                    draw.rectangle([wx, wy, wx + 6, wy + 8],
                                   fill=(255, 214, 120))
        x += bw + random.randint(2, 10)
        i += 1
    # neon sign on the skyline: skip (the ghost now rides in that space)


def draw_palm(draw, x, y, s, flip=False):
    col = (18, 7, 32)
    # trunk: curved thick line
    pts = []
    for t in range(0, 21):
        f = t / 20
        px = x + (26 * s * f * f) * (-1 if flip else 1)
        py = y - 210 * s * f
        pts.append((px, py))
    draw.line(pts, fill=col, width=int(14 * s), joint="curve")
    tx, ty = pts[-1]
    # fronds: quadratic arcs that rise then droop below the crown
    for ang in range(-165, -5, 20):
        a = math.radians(ang if not flip else 180 - ang)
        dx, dy = math.cos(a), math.sin(a)
        p0 = (tx, ty)
        p1 = (tx + dx * 55 * s, ty - 48 * s + dy * 10 * s)
        p2 = (tx + dx * 105 * s, ty + 58 * s + dy * 18 * s)
        curve = []
        for k in range(13):
            t = k / 12
            bx = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
            by = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
            curve.append((bx, by))
        draw.line(curve, fill=col, width=int(7 * s), joint="curve")
    # coconuts
    draw.ellipse([tx - 8 * s, ty - 2, tx + 2 * s, ty + 8 * s], fill=col)
    draw.ellipse([tx + 2 * s, ty, tx + 12 * s, ty + 10 * s], fill=col)


def draw_road(draw):
    draw.rectangle([0, 740, W, H], fill=(16, 7, 26))
    # road edge glow (sunset reflection)
    for i in range(6):
        draw.line([(0, 742 + i), (W, 742 + i)],
                  fill=(255, 120, 90 - i * 8))
    # centre dashes, perspective
    y = 800
    while y < H:
        w = 6 + (y - 800) // 26
        draw.rectangle([W // 2 - w, y, W // 2 + w, y + 14],
                       fill=(255, 214, 120))
        y += 74


def draw_car(draw):
    # pink convertible, side view facing right
    body = (255, 77, 141)
    dark = (214, 38, 102)
    x0, x1 = 150, 874
    y_body_top, y_body_bot = 838, 928
    # main body
    draw.rounded_rectangle([x0, y_body_top, x1, y_body_bot], radius=34,
                           fill=body)
    # hood slope (front, right)
    draw.polygon([(x1 - 190, y_body_top), (x1 - 30, y_body_top),
                  (x1, y_body_top + 46), (x1 - 190, y_body_top + 46)],
                 fill=body)
    # windshield
    draw.polygon([(x0 + 250, y_body_top), (x0 + 300, 788),
                  (x0 + 470, 788), (x0 + 500, y_body_top)], fill=(140, 220, 235))
    draw.line([(x0 + 250, y_body_top), (x0 + 300, 788)], fill=dark, width=6)
    draw.line([(x0 + 300, 788), (x0 + 470, 788)], fill=dark, width=6)
    draw.line([(x0 + 470, 788), (x0 + 500, y_body_top)], fill=dark, width=6)
    # door line + handle
    draw.line([(x0 + 330, y_body_top + 18), (x0 + 330, y_body_bot - 12)],
              fill=dark, width=4)
    draw.rounded_rectangle([x0 + 430, y_body_top + 34, x0 + 480, y_body_top + 44],
                           radius=5, fill=dark)
    # headlight + taillight
    draw.ellipse([x1 - 34, y_body_top + 26, x1 - 6, y_body_top + 52],
                 fill=(255, 240, 160))
    draw.rectangle([x0 + 4, y_body_top + 28, x0 + 16, y_body_top + 50],
                   fill=(255, 60, 60))
    # wheels
    for wx in (x0 + 130, x1 - 150):
        draw.ellipse([wx - 46, 896, wx + 46, 988], fill=(10, 5, 16))
        draw.ellipse([wx - 26, 916, wx + 26, 968], fill=(200, 200, 210))
        draw.ellipse([wx - 10, 932, wx + 10, 952], fill=(120, 120, 130))


def star_points(cx, cy, r_out, r_in, n=5):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / n - math.pi / 2
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_coin(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(226, 0, 122))
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255),
                 width=3)
    draw.polygon(star_points(cx, cy, r * 0.62, r * 0.26), fill=(255, 255, 255))


def outlined_text(draw, xy, text, font, fill=(255, 255, 255), stroke=5):
    draw.text(xy, text, font=font, fill=fill, stroke_width=stroke,
              stroke_fill=(0, 0, 0), anchor="ma")


def main():
    img = Image.new("RGB", (W, H), (24, 8, 58))
    draw = ImageDraw.Draw(img, "RGBA")

    sky_gradient(draw)
    draw_stars(draw)
    draw_sun(draw)
    draw_skyline(draw)
    draw_palm(draw, 30, 760, 1.15)
    draw_palm(draw, 1010, 770, 1.0, flip=True)
    draw_road(draw)

    # the make.fun ghost (official mark, disc removed so the ghost itself
    # rides in the scene): paste first, then the car body covers its lower
    # part so it reads as sitting in the convertible, holding its coin.
    ghost = Image.open(f"{ASSETS}/ghost-only.png").convert("RGBA")
    ghost = ghost.crop(ghost.getbbox())
    ghost = ghost.resize((330, int(330 * ghost.height / ghost.width)),
                         Image.LANCZOS)
    img.paste(ghost, (600, 560), ghost)
    draw = ImageDraw.Draw(img, "RGBA")

    draw_car(draw)

    # top text
    f_big = ImageFont.truetype(FONT_BOLD, 82)
    outlined_text(draw, (W // 2, 42), "13 YEARS WAITING", f_big)
    outlined_text(draw, (W // 2, 132), "FOR GTA 6", f_big)

    # footer bar: make.fun brand + payoff line
    draw.rectangle([0, 962, W, H], fill=(10, 5, 18))
    draw.line([(0, 962), (W, 962)], fill=(226, 0, 122), width=4)
    draw_coin(draw, 62, 993, 22)
    f_foot = ImageFont.truetype(FONT_BOLD, 42)
    draw.text((96, 970), "make.fun", font=f_foot, fill=(255, 255, 255))
    f_pay = ImageFont.truetype(FONT_BOLD, 36)
    draw.text((W - 24, 974), "FINALLY HERE — 19 NOV 2026", font=f_pay,
              fill=(255, 214, 120), anchor="ra")

    img.save(OUT, "PNG")
    print(f"saved {OUT} {img.size}")


if __name__ == "__main__":
    main()
