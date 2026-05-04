class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(-1)
        # return self.pop() <-- to spowoduje nieskończone wywoływanie funkcji
        # przez samą siebie - tzw. nieskończona rekurencja.
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
zadanie = ""
historia = Stack()

while zadanie != "koniec":
    zadanie = input("Co robimy? ")
    if zadanie == "wroc":
        print("Odwiedzamy:" + historia.pop())
    else:
        print("Odwiedzamy: " + zadanie)
        historia.push(zadanie)