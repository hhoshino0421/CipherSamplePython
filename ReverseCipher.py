
# 逆転値暗号処理
def reverse_cipher(message):

    translated = ""

    i = len(message) - 1

    while i >= 0:
        translated = translated + message[i]
        i = i - 1

    return translated
