# Окно логина, ну, например:
name = input('Enter your name')
print ('Hello', name)

# Числовое произведение
a = int(input('take a number'))
print (a * 10)

# Перемножение переменных a и b
a = int(input('A is'))
b = int(input('B is'))
print (a * b)


a = int(input('Day minutes'))
b = int(input('Night hours'))
print (a + b * 60)

'''
Катя узнала, что ей для сна надо XX минут. В отличие от Коли, Катя ложится спать после полуночи в HH часов и MM минут.
Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через XX минут после того, как она ляжет спать.
'''
x = int(input('Общий сон'))
h = int(input('Час пробуждения'))
m = int(input('Минуты пробуждения'))
hours = (x + m) // 60 + h
minutes = (x + h * 60 + m) % 60
print (hours)
print (minutes)


a = int(input('Число'))
print (a > 0)

a = int(input('Число'))
print (10 <= a < 100)


a = int(input('a'))
b = int(input('b'))
if b != 0:
    print (a / b)
else:
    print ('Деление Невозможно')
    b = int(input('Введите ненулевое значение'))
    if b == 0:
        print ('You cant do this!')
    else:
        print(a / b)
"""
Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки, но пересыпать тоже вредно и не стоит спать более BB часов.
Сейчас Аня спит HH часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
Если Аня спит менее AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.
Общее рекомендуемое время сна, часов
"""
a = int(input('take a'))
# Не стоит спать более чам, часов
b = int(input('take b'))
# Спит в данный момент, часов
n = int(input('take n'))
if b >= n >= a:
    print ('Это нормально')
elif a < n:
    print ('Пересып')
elif a > n:
    print ('Недосып')



if ((n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0)):
    print ('Вискоксный')
else:
    print ('Обычный')

# напишите программу, вычисляющую площадь треугольника по переданным длинам трёх его сторон по формуле Герона:
# где p=a+b+c2p=a+b+c2 – полупериметр треугольника.
a = int(input(''))
b = int(input(''))
c = int(input(''))
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)

#Калькулятор
a = float(input('number one='))
b = float(input('number two='))
c = str(input('operation'))
if c == '+':
    print (a + b)
elif c == '-':
    print (a - b)
elif c == '*':
    print (a * b)
elif c == 'pow':
    print (a ** b)
elif c == '/':
    print ('Деление на ноль!' if b == 0 else a / b)
elif c == 'div':
    print ('Деление на ноль!' if b == 0 else a // b)
elif c == 'mod':
    print ('Деление на ноль!' if b == 0 else a % b)
