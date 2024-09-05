# if else elif 控制流程

#boolean 布林值

for_sale = False
if for_sale:
    print('the product is for sale')
else:
    print('it is noe for sale')

age = int(input("please enter your age"))
if age >= 18:
    print('you are able to register')
else:
    print('your not able to register')

#elif => else if
age = int(input("please enter your age"))
if age >= 100:
    print('you are too old to register')
elif age>= 18:
    print('you are able to register')
elif age <= 0:
    print('you are too young to register')
else:
    print('you are not able to register')


