class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def enqueue(self, item) -> None:
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        print("Próba zdjęcia z pustej kolejki!")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
queue = Queue()
queue.enqueue(2) # [2]
queue.enqueue(3) # [2, 3]
queue.enqueue(1) # [2, 3, 1]

print(queue.dequeue()) # Zdejmuję 2, zostaje [3, 1]
print(queue.dequeue()) # Zdejmuję 3, zostaje [1]
print(queue.is_empty()) # False
print(queue.peek()) # Podejrzenie: 1, w kolejce jest: [1]
print(queue.dequeue()) # Zdejmuję: 1, []
print(queue.is_empty()) # True

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
        
# UTWORZENIE STOSU
# dodaj 5
# dodaj 4
# WYPISZ ZDJĘTĄ WARTOŚĆ
# dodaj 3
# dodaj 2
# WYPISZ ZDJĘTĄ WARTOŚĆ
# WYPISZ ZDJĘTĄ WARTOŚĆ
# WYPISZ ZDJĘTĄ WARTOŚĆ

stack = Stack() # []
stack.push(5) # [5]
stack.push(4) # [5, 4]
print(stack.pop()) # [5] -> 4
stack.push(3) # [5, 3]
stack.push(2) # [5, 3, 2]
print(stack.pop()) # [5, 3] -> 2
print(stack.pop()) # [5] -> 3
print(stack.pop()) # [] -> 5
print(stack.stack)