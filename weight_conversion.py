# 體重轉換器

weight = float(input('plesae enter your weight'))
unit = input('what is the unit? (kg/lb)').upper()  #用upper變成大寫


#print(weight)
#print(unit)

# 1kg = 2.2 lb

if unit == 'KG':
    print(f'your weight is {weight} {unit}')
    weight *= 2.2
    print(f'your weight is {round(weight,2)} LB')
elif unit == 'LB':
    print(f'your weight is {weight} {unit}')
    weight /= 2.2
    print(f'your weight is {round(weight,2)} KG')
else:
    print('error')