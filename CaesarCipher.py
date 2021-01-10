from Const import *


# シーザー暗号処理(暗号化/復号化処理)
def caesar_cipher(mesaage, key, enc_dec_mode):

    # シーザ暗号化処理可能な文字種の長さ取得
    symbols_len = len(CAESAR_SYMBOLS)

    translated = ""

    for symbol in mesaage:

        if symbol in CAESAR_SYMBOLS:
            # 変換可能な文字種に限定して変換処理を実行する

            symbol_index = CAESAR_SYMBOLS.find(symbol)

            if enc_dec_mode == ENCRYPT:
                # 暗号化処理モード
                translated_index = symbol_index + key

            elif enc_dec_mode == DECRYPT:
                # 復号化処理モード
                translated_index = symbol_index - key

            else:
                translated_index = symbol_index

            if translated_index >= symbols_len:
                translated_index = translated_index - symbols_len

            elif translated_index < 0:
                translated_index = translated_index + symbols_len

            translated = translated + CAESAR_SYMBOLS[translated_index]

        else:
            # 定義にない文字種はそのまま文字連結処理する
            translated = translated + symbol

    return translated
