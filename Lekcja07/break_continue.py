d = 1
while d < 10:
    print(d)
    if d % 3 == 0:
        break
    d += 1

print("-----")

d = 1
while d < 10:
    d += 1
    if d % 3 == 0:
        continue
    print(d)

