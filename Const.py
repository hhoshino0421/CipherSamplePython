# シーザー暗号での変換可能な文字種定義
CAESAR_SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."

# 転置式暗号のテストで利用可能なメッセージ定義
TRANSPOSITION_TEST_MESSAGE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 暗号化モード指定
REVERSE_CIPHER = 1      # 逆転値暗号
CAESAR_CIPHER = 2       # シーザー暗号
CAESAR_HACKER = 3       # シーザー暗号 総当たり攻撃
TRANSPOSITION_ENCRYPT = 4       # 転置式暗号 暗号化
TRANSPOSITION_DECRYPT = 5       # 転置式暗号 復号化
TRANSPOSITION_FILE_ENC_DEC = 6  # 転置式暗号 ファイル処理

# 暗号化/復号化モード指定
ENCRYPT = 1             # 暗号化処理モード
DECRYPT = 2             # 復号化処理モード


