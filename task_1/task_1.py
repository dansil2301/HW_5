with open('data.txt', 'a', encoding="utf-8") as f:
    add = input('Введите строку: ')
    while add != '':
        print(add, file=f)
        add = input('Введите строку: ')
