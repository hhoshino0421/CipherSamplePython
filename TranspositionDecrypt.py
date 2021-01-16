import math


# 転置式暗号 復号化処理関数
def transposition_decrypt(message, key):

    num_of_columns = int(math.ceil(len(message) / float(key)))
    num_of_rows = key
    num_of_shaded_boxs = (num_of_columns * num_of_rows) - len(message)

    plain_text = [''] * num_of_columns

    column = 0
    row = 0

    for symbol in message:

        plain_text[column] += symbol
        column += 1

        if (column == num_of_columns) or \
                (column == num_of_rows - 1
                 and row >= num_of_rows - num_of_shaded_boxs):
            column = 0
            row += 1

    return "".join(plain_text)
