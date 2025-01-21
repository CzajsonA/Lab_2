# Pobranie współczynników od użytkownika
a = float(input("Podaj współczynnik a (a ≠ 0): "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

# Sprawdzenie, czy a jest różne od zera (bo inaczej równanie nie jest kwadratowe)
if a == 0:
    print("Współczynnik 'a' nie może być zerowy, bratku.")
else:
    # Obliczenie delty
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        # Dwa pierwiastki rzeczywiste
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("Równanie ma dwa pierwiastki rzeczywiste:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        # Jeden pierwiastek podwójny
        x = -b / (2 * a)
        print("Równanie ma jeden pierwiastek podwójny:")
        print("x =", x)
    else:
        # Brak pierwiastków rzeczywistych
        print("Równanie nie ma pierwiastków rzeczywistych.")
