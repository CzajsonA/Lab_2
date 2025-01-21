# Wczytanie danych wejściowych
n = int(input("Podaj liczbę n (ilość elementów ciągu): "))
a = float(input("Podaj pierwszy element ciągu (a): "))
r = float(input("Podaj różnicę ciągu (r): "))

# Obliczanie i wypisywanie elementów ciągu
for i in range(n):
    wzor = a + i * r  # Wzór na n-ty element ciągu
    print(wzor)
