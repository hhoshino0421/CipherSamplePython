

# 転置式暗号 暗号化処理関数
def transposition_encrypt(message, key):

    # 暗号文の各文字列は格子の列を表す
    cipher_text = [''] * key

    message_len = len(message)

    # cipher_textの各列でループ処理する
    for column in range(key):
        current_index = column

        # current_indexがメッセージ長を超えるまでループ処理する
        while current_index < message_len:
            # リストcipher_textの現在位置に
            # messageのcurrent_indexの位置にある文字をセットする
            cipher_text[column] += message[current_index]

            # current_indexを次に進める
            current_index += key

    # 暗号文のリストを単一の文字列に変換する
    return "".join(cipher_text)

