f = open("./day1-input.txt", "r")
lines = f.readlines()
f.close()

lines = [x.strip().split() for x in lines]

col1, col2 = [], []
for line in lines:
    col1.append(int(line[0]))
    col2.append(int(line[1]))

final = zip(sorted(col1), sorted(col2))

final_ans = 0

for x, y in final:
    final_ans += x * y


print(final_ans)
