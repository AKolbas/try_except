


first_enter = input('Введите числа и знак в формате: + 2 5 \n')


#print(type(first_enter))
try:
    c = first_enter[0]
    a = int(first_enter.split ()[1])
    b = int(first_enter.split ()[2])
except IndexError:
    print('Введены не все аргументы!')

try:
    assert c in ['+', '-', '/', '*'], 'Неверный знак!'
    assert a >= 0 and  b >= 0, 'одно из значений меньше 0'

    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = round((a / b), 2)
    print(result)
except ZeroDivisionError:
    print('Деление на 0')
except ValueError:
    print('Операции над строками недопустимы!')
except NameError:
    print('Проверьте правильность ввода!')




