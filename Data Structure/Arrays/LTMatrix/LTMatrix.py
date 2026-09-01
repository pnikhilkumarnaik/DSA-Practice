class LowerTriangularMatrix:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n * (n + 1) // 2)

    def set(self, i, j, value):
        if i >= j:
            index = i * (i + 1) // 2 + j
            self.arr[index] = value
        elif value != 0:
            print("Cannot store a non-zero value above the main diagonal.")

    def get(self, i, j):
        if i >= j:
            index = i * (i + 1) // 2 + j
            return self.arr[index]
        return 0

    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.get(i, j), end=" ")
            print()
lt = LowerTriangularMatrix(3)

lt.set(0, 0, 1)
lt.set(1, 0, 2)
lt.set(1, 1, 3)
lt.set(2, 0, 4)
lt.set(2, 1, 5)
lt.set(2, 2, 6)
lt.display()
print("Value at index i, j:")
print(lt.get(2,2))
print("Array: ", lt.arr)

""" OUTPUT:

1 0 0 
2 3 0 
4 5 6 
Value at index i, j:
6
Array:  [1, 2, 3, 4, 5, 6]

"""

