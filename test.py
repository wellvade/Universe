a = int(input('number one='))
b = int(input('number two='))
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
