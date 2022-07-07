with open('subjects.txt', 'r', encoding="utf-8") as f:
    analytics = {}
    for line in f:
        line = line.replace(' —', '').replace(':', '').replace('.', '')
        line = line.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '')
        line = line.split()
        analytics[line[0]] = sum(int(number) for number in line[1:len(line) + 1])

print(analytics)
