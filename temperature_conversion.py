# 溫度轉換器


temp = float(input('please enter the temperature'))
unit = input('please the temperature unit (攝氏c , 華氏f) :')

if unit =='c':
    temp = round(9 * temp / 5 + 23)
    print(f'the current temperature is {temp} F')
elif unit == 'f':
    temp = round((temp - 32) *5 / 9)
    print(f'the current temperature is {temp} c')
else:
    print('error')

