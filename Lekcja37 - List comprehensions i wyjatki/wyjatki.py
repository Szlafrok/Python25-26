try:
    print(f"Policzyłem sobie ile to jest {5/0}")
except:
    print("Głupoty gościu gadasz")

lista = [1, 2, 3]
try:

    # zgłasza wyjątek
    raise IOError("domino się wysypało")

    # print(1/0)
    lista[5] = 10
except IndexError as description:
    print(description)
except ZeroDivisionError:
    print("lipa kolego dzielisz przez zero")
except Exception as e:
    print(str(e) + "!!!")