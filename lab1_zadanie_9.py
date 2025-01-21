age_input = input("Podaj swój wiek: ")

# Sprawdzenie, czy podano poprawne dane
if age_input.isdigit():
    wiek = int(age_input)

    # Sprawdzenie wieku
    if wiek < 4:
        print("Wstęp jest bezpłatny.")
    else:
        # Pobranie informacji, czy użytkownik jest studentem
        student = input("Czy jesteś studentem? (tak/nie): ").strip().lower()

        if wiek >= 4 and wiek < 18:
            print("Cena biletu: 10 zł.")
        elif student == "tak":
            print("Cena biletu: 15 zł (zniżka 25%).")
        else:
            print("Cena biletu: 20 zł.")
else:
    print("Wprowadziłeś niepoprawne dane. Podaj liczbę całkowitą dla wieku.")