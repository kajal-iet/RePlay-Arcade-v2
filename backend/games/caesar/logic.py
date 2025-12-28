SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_translate(message: str, key: int, mode: str) -> str:
    message = message.upper()
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                num += key
            else:
                num -= key

            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]
        else:
            translated += symbol

    return translated
