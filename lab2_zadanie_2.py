# Pobranie liczby wierszy od użytkownika
n = int(input("Podaj liczbę wierszy: "))

# a) Kwadrat gwiazdek n x n
print("\na) Kwadrat gwiazdek:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()  # Nowa linia po każdej iteracji wiersza

# b) Trójkąt gwiazdek rosnący
print("\nb) Trójkąt rosnący:")
for i in range(1, n + 1):
    print("*" * i)  # Wyświetl i gwiazdek w każdej iteracji

# c) Trójkąt gwiazdek malejący
print("\nc) Trójkąt malejący:")
for i in range(n, 0, -1):
    print("*" * i)  # Wyświetl i gwiazdek w każdej iteracji
