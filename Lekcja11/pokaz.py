def trojkat(a, b, c):
    if a >= b and a >= c:
        if b + c > a:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")
    elif b >= a and b >= c:
        if a + c > b:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")
    else: # c jest największe
        if a + b > c:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")

trojkat(2, 3, 10)