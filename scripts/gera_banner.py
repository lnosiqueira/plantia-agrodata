# scripts/gera_banner.py
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 300
TITLE = "PlantIA Agrodata — FIAP"
SUB   = "Sistema Inteligente de Gestão de Colheita de Cana-de-Açúcar"

def pick_font(size):
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/seguiemj.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size=size)
    return ImageFont.load_default()

def gradient_bg():
    img = Image.new("RGB", (W, H), "#2e7d32")
    draw = ImageDraw.Draw(img)
    top = (23, 94, 30)
    bot = (67, 160, 71)
    for y in range(H):
        t = y / H
        rr = int(top[0] + (bot[0]-top[0]) * t)
        gg = int(top[1] + (bot[1]-top[1]) * t)
        bb = int(top[2] + (bot[2]-top[2]) * t)
        draw.line([(0, y), (W, y)], fill=(rr, gg, bb))
    return img

def main():
    img = gradient_bg()
    draw = ImageDraw.Draw(img)

    title_font = pick_font(64)
    sub_font   = pick_font(28)

    tw, th = draw.textbbox((0, 0), TITLE, font=title_font)[2:]
    sw, sh = draw.textbbox((0, 0), SUB, font=sub_font)[2:]

    title_pos = ((W - tw)//2, H//2 - th - 10)
    sub_pos   = ((W - sw)//2, H//2 + 10)

    shadow = (0, 0, 0)
    for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
        draw.text((title_pos[0]+dx, title_pos[1]+dy), TITLE, font=title_font, fill=shadow)
        draw.text((sub_pos[0]+dx, sub_pos[1]+dy), SUB, font=sub_font, fill=shadow)

    draw.text(title_pos, TITLE, font=title_font, fill="white")
    draw.text(sub_pos, SUB, font=sub_font, fill="white")

    out_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "img"))
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "banner_plantia.png")
    img.save(out_path, format="PNG")
    print("✅ Banner salvo em:", out_path)

if __name__ == "__main__":
    main()
