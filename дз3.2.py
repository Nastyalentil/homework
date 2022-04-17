print('Вітаю!')
number1 = input('Введіть перше число: ')
number2 = input('Введіть друге число: ')
if  number1 > number2:
    print(number1, '>', number2)
elif number1 < number2:
    print(number1, '<', number2)
else:
    print(number1, '=', number2)