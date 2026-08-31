def tresc(funkcja):
    def wrapper():
        print("PRZED")
        funkcja()
        print("PO")
    return wrapper


@tresc
def hej():
    print("Hej :)")

@tresc
def klej():
    print("Kup se klej")

hej()
klej()