name = input("Введіть ваше імя: ")
print("Вітаю", name + "!")
choose = input('Оберіть вид операції: ')
number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))

if choose == "*":
    a = number1 * number2
    print(a)
elif choose == "+":
    b = number1 + number2
    print(b)
elif choose == '-':
    c = number1 - number2
    print(c)
elif choose == '/':
    d = number1 / number2
    print(d)
else:
    print("Помилка!")
