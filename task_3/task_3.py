with open('workers.txt', 'r', encoding="utf-8") as f:
    lines, s = 0, 0
    for line in f:
        lines += 1
        s += float(line.split()[1])
        if float(line.split()[1]) < 20_000:
            print(f'{line.split()[0]} получает меньше 20_000 тыс.')
    s /= lines
    print(f'Средняя зарплата всех сотрудников: {s}')