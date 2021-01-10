from CaesarCipher import *
from Const import *


# シーザー暗号を総当たり攻撃で解読する関数
def caesar_hacker(message):

    for i in range(len(CAESAR_SYMBOLS)):

        # シーザー暗号関数を復号化モードでキーを変更しながら実行
        translated = caesar_cipher(message, i, DECRYPT)

        # 総当たり攻撃結果を出力
        print("key[" + str(i) + "]: " + translated)
