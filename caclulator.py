# 計算機程式

operator = input("請輸入運算如號(加法:+ , 減法:- , 乘法:* , 除法:／）：")
num1 = float(input('please enter the first number'))
num2 = float(input('please enter the second number'))

if operator == '+':
    result = num1+num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '-':
    result = num1-num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator == '*':
    result = num1*num2
    print(f"{num1} {operator} {num2} = {result}")
elif operator =='/':
    result = num1/num2
    print(f"{num1} {operator} {num2} = {result}")
else:
    print('error')
