# SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def translate(message: str, key: int, mode: str) -> str:
#     message = message.upper()
#     result = ""

#     for char in message:
#         if char in SYMBOLS:
#             index = SYMBOLS.index(char)

#             if mode == "encrypt":
#                 index += key
#             else:  # decrypt
#                 index -= key

#             index %= len(SYMBOLS)
#             result += SYMBOLS[index]
#         else:
#             result += char

#     return result


# def hack(message: str):
#     results = []
#     for k in range(26):
#         decrypted = translate(message, k, "decrypt")
#         results.append({
#             "key": k,
#             "text": decrypted
#         })
#     return results
