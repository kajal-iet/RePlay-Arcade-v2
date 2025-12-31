import random
import datetime

LEFT, RIGHT = 'left', 'right'
BEADY, WIDE, HAPPY, ALOOF = 'beady', 'wide', 'happy', 'aloof'
CHUBBY, VERY_CHUBBY = 'chubby', 'very chubby'
OPEN, CLOSED = 'open', 'closed'
OUT, DOWN, UP = 'out', 'down', 'up'

def get_seasonal_hat(seasonal):
    if not seasonal:
        return ""
    m = datetime.datetime.now().month
    return "^🎅" if m == 12 else "^🎃" if m == 10 else "^🎓" if m in [5,6] else ""

class Duckling:
    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])
        self.eyes = BEADY if self.body == CHUBBY else random.choice([BEADY, WIDE, HAPPY, ALOOF])

    def head(self, hat):
        if self.direction == LEFT:
            face = '>' if self.mouth == OPEN else '='
            eye = {'beady':'"', 'wide':"''", 'happy':'^^', 'aloof':'``'}[self.eyes]
            return f"{hat}{face}{eye})"
        else:
            face = '<' if self.mouth == OPEN else '='
            eye = {'beady':'"', 'wide':"''", 'happy':'^^', 'aloof':'``'}[self.eyes]
            return f"{hat}({eye}{face}"

    def body_str(self):
        wing = {'out':'>','up':'^','down':'v'}[self.wing]
        return f"( {wing} )"

    def feet(self):
        return " ^^ "

def generate_ducks(count, seasonal):
    hat = get_seasonal_hat(seasonal)
    ducks = []
    for _ in range(count):
        d = Duckling()
        ducks.append({
            "head": d.head(hat),
            "body": d.body_str(),
            "feet": d.feet()
        })
    return ducks
