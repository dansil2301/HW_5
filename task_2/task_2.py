file = open('Example.txt', 'r', encoding='utf-8')
lines, words = 0, 0
for line in file:
    words += len(line.split())
    lines += 1
print(f'слов: {words}, строк: {lines}')
file.close()