# 字串索引

credit_number = '1234-5678-5432'

first_char = credit_number[0]               #取得第一個字元(是從0位是第1個)
print('the first char is ', first_char)

first_char = credit_number[1]               #取得第2個字元
print('the first char is ', first_char)


first_four = credit_number[0:6]               #取得從第0位開始的6個字元
print('the first four chars are ', first_four)

last_one = credit_number[-1]               #取得最後一個字元
print('the last char is ', last_one)


print(len(credit_number))
last_four = credit_number[-13:3]           #長度14但是起始位是從0開始所以最後一位是13
print('the last four chars are', last_four)         