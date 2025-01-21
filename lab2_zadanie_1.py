# a) 1, 2, 3, ..., 99, 100
print("a) Ciąg: 1, 2, 3, ..., 99, 100")
for i in range(1, 101):
    print(i, end=", ")
print("\n")  # Przejście do nowej linii

# b) 100, 99, ..., 2, 1, 0
print("b) Ciąg: 100, 99, ..., 2, 1, 0")
for i in range(100, -1, -1):
    print(i, end=", ")
print("\n")  # Przejście do nowej linii

# c) 7, 14, 21, ..., 70, 77
print("c) Ciąg: 7, 14, 21, ..., 70, 77")
for i in range(7, 78, 7):
    print(i, end=", ")
print("\n")  # Przejście do nowej linii

# d) 20, 18, ..., 2, 0
print("d) Ciąg: 20, 18, ..., 2, 0")
for i in range(20, -1, -2):
    print(i, end=", ")
print("\n")  # Przejście do nowej linii
