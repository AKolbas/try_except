
first_enter = input('Введите два положительных числа и знак в формате: + 2 5 через пробел \n')
assert len(list(first_enter.split())) == 3, 'Вы ввели неправильное количество аргументов'

symbol = first_enter[0]
assert symbol in ['+', '-', '/', '*'], 'Неверный знак!'

try:
    num_1 = int(first_enter.split()[1])
    num_2 = int(first_enter.split()[2])
    assert num_1 >= 0 and num_2 >=0, 'Одно из значений отрицательное'
except ValueError:
    print('Вы ввели не число!')

#assert num_1 >= 0 and  num_2 >= 0, 'одно из значений меньше 0'

try:
    if symbol == '+':
        result = num_1 + num_2
    elif symbol == '-':
        result = num_1 - num_2
    elif symbol == '*':
        result = num_1 * num_2
    elif symbol == '/':
        result = round((num_1 / num_2), 2)
    print(result)
except ZeroDivisionError:
    print('Деление на 0')
except NameError:
    print('Проверьте правильность ввода!')




