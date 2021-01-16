from ReverseCipher import *
from CaesarCipher import *
from CaesarHacker import *
from TranspositionEncrypt import *
from TranspositionDecrypt import *
from Const import *


# メイン処理関数
def main():

    # 暗号化テキストの入力
    message = input("Enter message: ")
    # 暗号化モードの指定
    input_mode = input("mode: ")

    try:
        # 暗号化モードを数値変換
        mode = int(input_mode)

    except ValueError:
        print("mode is numeric.")
        return

    if mode == REVERSE_CIPHER:
        # 逆転値暗号処理
        translated = reverse_cipher(message)

    elif mode == CAESAR_CIPHER:
        # シーザー暗号処理

        # キー長の入力
        input_key = input("key: ")
        input_enc_dec_mode = input("Encrypt=1 or Decrypt=2 ?: ")

        try:
            # キー長を数値化
            key = int(input_key)

        except ValueError:
            print("key is numeric.")
            return

        try:
            # 暗号化/復号化モードを数値化
            enc_dec_mode = int(input_enc_dec_mode)

        except ValueError:
            print("enc_dec_mode is numeric.")
            return

        if enc_dec_mode == ENCRYPT or enc_dec_mode == DECRYPT:
            pass

        else:
            print("enc_dec_mode is 1 or 2.")
            return

        # シーザー暗号処理を実行
        translated = caesar_cipher(message, key, enc_dec_mode)

    elif mode == CAESAR_HACKER:
        # シーザー暗号 総当たり攻撃
        caesar_hacker(message)

        # 処理結果は上記関数内で出力しているのでこのまま処理を抜ける
        return

    elif mode == TRANSPOSITION_ENCRYPT:
        # 転置式暗号 暗号化
        # キー長の入力
        input_key = input("key: ")

        try:
            # キー長を数値化
            key = int(input_key)

        except ValueError:
            print("key is numeric.")
            return

        # 転置式暗号 暗号化処理
        translated = transposition_encrypt(message, key)

    elif mode == TRANSPOSITION_DECRYPT:
        # 転置式暗号 復号化処理
        # キー長の入力
        input_key = input("key: ")

        try:
            # キー長を数値化
            key = int(input_key)

        except ValueError:
            print("key is numeric.")
            return

        # 転置式暗号 復号化処理
        translated = transposition_decrypt(message, key)

    else:
        # 暗号化モード指定不備
        print("mode is ignore.")
        return

    # 処理結果文字列出力
    print(translated)


# プログラムのエントリポイント
if __name__ == "__main__":

    # メイン処理
    main()
