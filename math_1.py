# python 中的數學

# 加減乘除

#apple = 3
#apple = apple + 1
#apple -=1

#apple = apple*2

#apple*=2

#apple /= 3  #用除法後會自動轉換成浮點數float
#print(apple)


# 指數(二次方、三次方)

#apple = 3

#apple  = apple**3

# 也可以寫成 apple**=3
#print(apple)


#模數 MOD  (餘數)

# 10 mod 3 = 3...1
print(10%3)
#11 mod 3 = 3....2
print(11 % 3)
#12 mod 3 = 4...0
print(12 % 3)


# 次方 pow
print(pow(3,2))

#max,min
x = 1
y = 2
z= 3
print(max(x,y,z))
print(min(x,y,z))


#四捨五入 round

a = 3.14
print(round(a))

b = 3.5
print(round(b))

#絕對值

a = -4
print("絕對值:", abs(a))

#四捨五入、無條件進位、無條件捨去
x = 9.5
import math      #要記得引述math模組才可以使用以下語法
print(math.ceil(x))  #ceil無條件進位
print(math.floor(x))   #floor無條件捨去

#圓周率

print(math.pi)

#計算周常
radius = float(input("please enter the radius"))
c = 2* math.pi * radius
print(f'圓的周長為:{round(c,2)}')  #圓周率太長，用round取到小數點後兩位就好

#圓的面積
radius = float(input("please enter the radius"))
d = math.pi *(radius**2)
print(f'圓的面積為:{round(d)}')   #如果直接用round就會是整數


