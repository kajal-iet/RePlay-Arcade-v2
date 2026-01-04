from PIL import Image, ImageDraw, ImageFont
import io

class CarpetGame:
    def __init__(self):
        self.pattern = "_ \\ \\ \\_/ __\n \\ \\ \\___/ _\n\\ \\ \\_____/"
        self.x = 6
        self.y = 4
        self.bg = "#000000"

GAME = CarpetGame()

def apply_changes(pattern, x, y, bg):
    GAME.pattern = pattern
    GAME.x = x
    GAME.y = y
    GAME.bg = bg

def build_carpet():
    base = GAME.pattern.splitlines()
    out = []
    for _ in range(GAME.y):
        for line in base:
            out.append(line * GAME.x)
    return "\n".join(out)

def generate_image():
    text = build_carpet()
    lines = text.splitlines()
    font_size = 16
    padding = 20

    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
    except:
        font = ImageFont.load_default()

    dummy = Image.new("RGB", (1,1))
    draw = ImageDraw.Draw(dummy)
    width = max(draw.textlength(l, font=font) for l in lines)
    line_h = font_size + 4

    img = Image.new("RGB",
        (int(width) + padding*2, line_h * len(lines) + padding*2),
        GAME.bg
    )

    draw = ImageDraw.Draw(img)
    y = padding
    for line in lines:
        draw.text((padding,y), line, fill="white", font=font)
        y += line_h

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.getvalue()
