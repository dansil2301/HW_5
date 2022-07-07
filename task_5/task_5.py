from random import randrange

with open('num.txt', 'w', encoding="utf-8") as f:
    for i in range(randrange(1, 100)):
        f.write(f'{randrange(0, 1001)} ')

with open('num.txt', 'r', encoding="utf-8") as f:
    print(f'Сумма случайных чисел: {sum(int(number) for number in f.read().split())}')
