rus_numbers = {
                1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
                6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'десять'
               }

with open('rus_n.txt', 'a', encoding="utf-8") as f:
    n = open('numbers.txt', 'r', encoding='utf-8')

    for line in n:
        print(f"{rus_numbers[int(line.split(' — ')[1])]} — {line.split(' — ')[1]}", file=f, end='')

    n.close()

print('готово')
