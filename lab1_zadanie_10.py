# Pobranie trzech liczb od użytkownika
x = float(input("Podaj pierwszą liczbę (x): "))
y = float(input("Podaj drugą liczbę (y): "))
z = float(input("Podaj trzecią liczbę (z): "))

# Inicjalizacja zmiennych dla posortowanych liczb
maly = 0
sredni = 0
duzy = 0

# Sprawdzanie warunków
if x <= y and x <= z:
    maly = x
    if y <= z:
        sredni = y
        duzy = z
    else:
        sredni = z
        duzy = y
elif y <= x and y <= z:
    maly = y
    if x <= z:
        sredni = x
        duzy = z
    else:
        sredni = z
        duzy = x
else:  # z <= x and z <= y
    maly = z
    if x <= y:
        sredni = x
        duzy = y
    else:
        sredni = y
        duzy = x

# Wyświetlenie posortowanych liczb
print("Liczby w kolejności od najmniejszej do największej:")
print(maly, sredni, duzy)
