def gen(start):
    value = start
    while True:
        yield value
        value += 3


generator = gen(5)
generator2 = gen(10)

print(next(generator))
print(next(generator2))
print(next(generator))
print(next(generator))
print(next(generator2))