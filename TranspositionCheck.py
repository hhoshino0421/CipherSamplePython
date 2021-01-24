import time
import random
from Const import *
from TranspositionEncrypt import *
from TranspositionDecrypt import *


# 転置式暗号テスト処理関数
def transposition_test(test_count):

    # 現在日時から乱数のシードを設定(null指定時と動作は同じ)
    ut = time.time()
    random.seed(ut)

    # 統計情報
    match_count = 0
    mismatch_count = 0

    for i in range(test_count):

        # メッセージを取得
        # 4-40間の乱数を生成
        message = TRANSPOSITION_TEST_MESSAGE * random.randint(4, 40)

        # メッセージを操作するためにリストに変換する
        message_list = list(message)            # 文字列をリスト化する
        random.shuffle(message_list)            # リストの要素をランダムに並べ替える
        message_edit = ''.join(message_list)    # リストを文字列に戻す

        # テスト用のランダム文字列を表示
        print('Test #%s: "%s..."' % (i + 1, message_edit[:50]))

        for key in range(1, int(len(message_edit) / 2)):

            # 暗号化
            encrypted = transposition_encrypt(message_edit, key)

            # 復号化
            decrypted = transposition_decrypt(encrypted, key)

            if message_edit != decrypted:
                # 不一致

                print('Mismatch with key %s and message %s.' % (key, message_edit))

                print('Decrypted as :' + decrypted)

                mismatch_count += 1

            else:
                # 一致

                # for debug
                # print('Match with key %s and message %s.' % (key, message_edit))

                match_count += 1

    # 統計情報出力
    print('')
    print("match: %d, mismatch: %d" % (match_count, mismatch_count))

    if mismatch_count <= 0:
        # 全て一致
        print('Transposition cipher test passed.')
