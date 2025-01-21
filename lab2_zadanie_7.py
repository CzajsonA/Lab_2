# a) Wczytanie imienia i wyświetlenie "Witaj" oraz wczytanego imienia
imie = input("Podaj swoje imię: ")
print("Witaj", imie)

# b) Wczytanie wieku i wyświetlenie tekstu "Twój wiek to: " oraz wczytanego wieku
wiek = int(input("Podaj swój wiek: "))
print("Twój wiek to:", wiek)

# c) Wczytanie imienia i nazwiska oraz wyświetlenie inicjałów
nazwisko = input("Podaj swoje nazwisko: ")
inicjaly = imie[0].upper() + '.' + nazwisko[0].upper() + '.'
print("Twoje inicjały to:", inicjaly)

# d) Wczytanie łańcucha i wyświetlenie go pięć razy
lancuch = input("Podaj łańcuch: ")
print(lancuch * 5)

# e) Wczytanie dwóch łańcuchów, a w trzecim zapamiętanie połączonych tych dwóch łańcuchów
lancuch1 = input("Podaj pierwszy łańcuch: ")
lancuch2 = input("Podaj drugi łańcuch: ")
lancuch3 = lancuch1 + lancuch2
print("Połączony łańcuch to:", lancuch3)

# f) Wczytanie dwóch łańcuchów, a w trzecim zapamiętanie pierwszej połowy pierwszego łańcucha i drugiej połowy drugiego łańcucha
polowa1 = lancuch1[:len(lancuch1)//2]  # Pierwsza połowa pierwszego łańcucha
polowa2 = lancuch2[len(lancuch2)//2:]  # Druga połowa drugiego łańcucha
lancuch4 = polowa1 + polowa2
print("Połączona pierwsza połowa pierwszego i druga połowa drugiego łańcucha:", lancuch4)
