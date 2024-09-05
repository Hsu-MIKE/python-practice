# 字串方法
#'len()'   'find()'   'capitalize()'
# 'upper()'  'lower()'  'count()'   'replace()'

#help(str)  #可以找所有的字串方法

name ="code shiba 程式柴"


#幾個字元
length = len(name)
print('你的全名總共有' , length , "個字元")


#找到第一個空格
space_pos = name.find(' ')
print("the first space appear at 第 " , space_pos , "個字元")

name_captipalize = name.capitalize()  #讓字母的第一個字母變大寫
name_upper = name.upper()  #全部變大寫
name_lower = name.lower()  #全部變小寫


#count
phone_number = input('plz enter your phone number')
dash_count = phone_number.count('-')
print('there are ', dash_count , 'dash')



#replace
phone_number = input('plz enter your phone number')
phone_number = phone_number.replace('-' ,' ')
print(phone_number)

#程式練習
# 使用者名稱不能超過12個字元
# 使用者名稱不能包含空格
# 使用者名稱不能包含數字
# 如果都符合，顯示 '歡迎+使用者名稱'


user_name = input('plz enter your user name')
if len(user_name) > 12:
    print('your name cant be over 12 strings')
elif " " in user_name:                                   #可以用in去看有沒有條件
    print('you cant have any spaces in your name')
elif not user_name.isalpha():                              #isalpha()都是string，用not找出不是字以外的符號
    print('your name cant be involve in numbers')
else:
    print('welcome', user_name , '!')

