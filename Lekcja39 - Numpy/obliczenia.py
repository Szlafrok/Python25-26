import numpy as np

def print_array(array): # array
    print(f"Tablica \n{array}")
    print(f"Pierwszy element tablicy: {arr[0]}")
    print(f"Drugi element pierwszego rzędu: {arr[0][1]}")
    print(f"Kształt tablicy: {array.shape}")

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print_array(arr)

def shapeshifter(array: np.ndarray):
    print("Kształt 9 x 1")
    print(array.reshape(9, 1))

    print("Kształt 1 x 9")
    print(array.reshape(1, 9))

    print(array)

    print("Kształt 3 x 3")
    print(array.reshape(3, 3))

    print("Dopasowanie do dziewiątki")
    print(array.reshape(-1, 9))

    print("Dopasowanie do dziewiątki po wierszach")
    print(array.reshape(9, -1))

    print("????")
    print(array.reshape(-1, -1))

shapeshifter(arr)