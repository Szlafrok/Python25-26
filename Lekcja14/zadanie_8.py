def ambrozy(pierogi):
    sumy = []
    for pierog in pierogi:
        sumy.append(0)
        while pierog > 0:
            sumy[-1] += pierog % 10
            pierog //= 10

    print(sumy)
    for s in sumy:
        if sumy.count(s) == 1:
            return pierogi[sumy.index(s)]


print(ambrozy([123, 99, 321, 213]))