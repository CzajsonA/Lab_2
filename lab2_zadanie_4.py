# Wczytanie liczby n
n = int(input("Podaj liczbę n: "))

# Inicjalizacja zmiennej do przechowywania wyniku
silnia = 1

# Obliczanie silni
for i in range(1, n + 1):
    silnia *= i  # Mnożenie przez kolejne liczby od 1 do n

# Wypisanie wyniku
print(f"Silnia liczby {n} wynosi: {silnia}")
