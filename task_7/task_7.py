import json

with open('firms.txt', 'r', encoding="utf-8") as f:
    analytics = {}
    count, s = 0, 0
    for line in f:
        if line != '\n':
            line = line.split()

            count += 1
            profit = int(line[2]) - int(line[3])
            s += profit

            if profit > 0:
                analytics[line[0]] = profit

analytics = [analytics, {"average_profit": s / count}]

with open("my_file.json", "w") as f:
    json.dump(analytics, f)

print('Готово')
