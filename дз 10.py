# print('Вітаю, це конвертер системи числення з базою 17.')
# print('Символи та їх значення:')
sth = '0123456789ABCDEFGH'

for line in sth:
    print(f'{line} = {sth.find(line)}')
system = input('Введіть число використовуючи обрану систему числення: ')
systemp = system[::-1]
b = 17
n = system.find(line)

p = system.find(systemp)
print(n)
print(p)

    # print(line)
    # print(num)
    # n = sth.index('0123456789ABCDEFG')
    # nth = str(n)
    # n = "'0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'"
    # for num in n:
    # num = int(sth)
    #     print(f'{line} = {num}')

# text = 'abc'[::-1]
# print(text)
system = input('Введіть число використовуючи обрану систему числення: ')
systemp = system[::-1]
p = systemp
print(systemp)