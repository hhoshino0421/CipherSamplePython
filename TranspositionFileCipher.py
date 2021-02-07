import time
import os
from Const import *
from TranspositionEncrypt import *
from TranspositionDecrypt import *


# 引数チェック処理
def param_check(plane_file_name, output_file_name, enc_dec_mode, key_len):

    if not plane_file_name:
        # 入力ファイル名なし
        return False, 0, 0, "plane_file_name is null."

    if not output_file_name:
        # 出力ファイル名なし
        return False, 0, 0, "output_file_name is null."

    if not os.path.exists(plane_file_name):
        # 入力ファイルが存在しない
        return False, 0, 0, "output_file_name is not exist."

    if os.path.exists(output_file_name):
        # 出力ファイルが既に存在している
        # ユーザに処理続行を確認
        print("Output file exist. Continue? YES=1,NO=2")
        ret = input('> ')

        if not ret or ret == "2":
            # 未入力 or 2
            # 強制終了
            return False, 0, 0, "User cancel.(Norman end)"

        if ret == "1":
            # 処理続行
            pass

        else:
            # 入力エラー
            # 強制終了
            return False, 0, 0, "User cancel.(Input command error)"

    if not enc_dec_mode:
        # モード未指定
        return False, 0, 0, "mode is empty."

    try:
        # モード指定を数値化
        enc_mode_int = int(enc_dec_mode)

    except ValueError:

        return False, 0, 0, "mode error.mode is numeric and 1 or 2."

    if enc_mode_int == ENCRYPT or enc_mode_int == DECRYPT:
        # モード入力OK
        pass

    else:
        # モード未指定
        return False, 0, 0, "mode error.mode is 1 or 2."

    if not key_len:
        # キー長未入力
        return False, 0, 0, "key_len is empty."

    try:
        # キー帳を数値化
        key_len_int = int(key_len)

    except ValueError:

        return False, 0, 0, "key_len is must numeric."

    # チェック処理正常終了
    return True, enc_mode_int, key_len_int, ""


# 暗号化処理関数
def encrypt_data(input_data_text, key_len_int):

    try:
        # 暗号化処理実行
        output_data = transposition_encrypt(input_data_text, key_len_int)

    except Exception:

        return False, "Encrypt in has error."

    return True, output_data


# 復号化処理関数
def decrypt_data(input_data_text, key_len_int):

    try:
        # 復号化処理実行
        output_data = transposition_decrypt(input_data_text, key_len_int)

    except Exception:

        return False, "Encrypt in has error."

    return True, output_data


# エントリポイント関数
# ファイル暗号化関数(転置式暗号処理)
def file_encrypt(plane_file_name, output_file_name, enc_dec_mode, key_len):

    # 入力パラメータチェック処理
    result, enc_dec_mode_int, key_len_int, error_message \
        = param_check(plane_file_name, output_file_name, enc_dec_mode, key_len)

    if not result:
        # パラメータエラー or ユーザによる処理キャンセル
        # 異常終了
        return False, error_message

    # 入力ファイルオープン処理
    with open(plane_file_name) as input_file_obj:

        # 入力ファイルデータ読込処理
        input_data_text = input_file_obj.read()

        # 出力ファイルオープン処理
        with open(output_file_name, 'w') as output_file_obj:

            # 暗号化/復号化処理時間計測
            start_time = time.time()

            if enc_dec_mode_int == ENCRYPT:
                # 暗号化処理
                result, output_data = encrypt_data(input_data_text, key_len_int)

            elif enc_dec_mode_int == DECRYPT:
                # 復号化処理
                result, output_data = decrypt_data(input_data_text, key_len_int)

            else:
                # ロジックエラー
                return False, "Logic error."

            if not result:
                # 暗号化/復号化処理 異常終了
                return False, "encrypt/decrypt error."

            # 暗号化/復号化処理時間計算処理
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            # 処理結果出力処理
            output_file_obj.write(output_data)

    print("Enc/Dec process time: %f", total_time)

    # 正常終了
    return True, ""

