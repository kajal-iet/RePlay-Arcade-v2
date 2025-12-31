from PIL import Image, ImageDraw, ImageFont
import io

UP_DOWN_CHAR         = chr(9474)
LEFT_RIGHT_CHAR      = chr(9472)
DOWN_RIGHT_CHAR      = chr(9484)
DOWN_LEFT_CHAR       = chr(9488)
UP_RIGHT_CHAR        = chr(9492)
UP_LEFT_CHAR         = chr(9496)
UP_DOWN_RIGHT_CHAR   = chr(9500)
UP_DOWN_LEFT_CHAR    = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR   = chr(9524)
CROSS_CHAR           = chr(9532)

CANVAS_WIDTH = 40
CANVAS_HEIGHT = 20

def classify(d):
    if not d: return ' '
    if d.issubset({'W','S'}): return UP_DOWN_CHAR
    if d.issubset({'A','D'}): return LEFT_RIGHT_CHAR
    if d == {'S','D'}: return DOWN_RIGHT_CHAR
    if d == {'A','S'}: return DOWN_LEFT_CHAR
    if d == {'W','D'}: return UP_RIGHT_CHAR
    if d == {'W','A'}: return UP_LEFT_CHAR
    if d == {'W','S','D'}: return UP_DOWN_RIGHT_CHAR
    if d == {'W','S','A'}: return UP_DOWN_LEFT_CHAR
    if d == {'A','S','D'}: return DOWN_LEFT_RIGHT_CHAR
    if d == {'W','A','D'}: return UP_LEFT_RIGHT_CHAR
    if d == {'W','A','S','D'}: return CROSS_CHAR
    return ' '

def build_canvas(moves):
    canvas = {}
    cx, cy = 0, 0

    for m in moves:
        canvas.setdefault((cx,cy), set())

        if m == 'W' and cy > 0:
            canvas[(cx,cy)].add('W'); cy -= 1
            canvas.setdefault((cx,cy), set()).add('S')

        elif m == 'S' and cy < CANVAS_HEIGHT-1:
            canvas[(cx,cy)].add('S'); cy += 1
            canvas.setdefault((cx,cy), set()).add('W')

        elif m == 'A' and cx > 0:
            canvas[(cx,cy)].add('A'); cx -= 1
            canvas.setdefault((cx,cy), set()).add('D')

        elif m == 'D' and cx < CANVAS_WIDTH-1:
            canvas[(cx,cy)].add('D'); cx += 1
            canvas.setdefault((cx,cy), set()).add('A')

    return canvas, cx, cy

def canvas_to_string(canvas, cx, cy):
    out = ""
    for y in range(CANVAS_HEIGHT):
        for x in range(CANVAS_WIDTH):
            if (x,y) == (cx,cy):
                out += "#"
            else:
                out += classify(canvas.get((x,y)))
        out += "\n"
    return out

def render_image(canvas):
    img = Image.new('RGB', (CANVAS_WIDTH*20, CANVAS_HEIGHT*20), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for (x,y), dirs in canvas.items():
        draw.text((x*20, y*20), classify(dirs), fill="black", font=font)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
