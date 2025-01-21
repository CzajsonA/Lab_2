# Kalkulator: Pobierz dwie liczby i operację matematyczną od użytkownika
print("Prosty kalkulator")
print("Wybierz działanie:")
print("1. Dodawanie (+)")
print("2. Odejmowanie (-)")
print("3. Mnożenie (*)")
print("4. Dzielenie (/)")

# Pobranie danych od użytkownika
num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))
oper = input("Wybierz operację (+, -, *, /): ")

# Realizacja operacji matematycznej za pomocą if/elif/else
if oper == "+":
    wynik = num1 + num2
    print(f"Wynik dodawania: {num1} + {num2} = {wynik}")
elif oper == "-":
    wynik = num1 - num2
    print(f"Wynik odejmowania: {num1} - {num2} = {wynik}")
elif oper == "*":
    wynik = num1 * num2
    print(f"Wynik mnożenia: {num1} * {num2} = {wynik}")
elif oper == "/":
    if num2 != 0:
        wynik = num1 / num2
        print(f"Wynik dzielenia: {num1} / {num2} = {wynik}")
    else:
        print("Błąd: Nie można dzielić przez zero!")
else:
    print("Błąd: Wybrano nieprawidłową operację.")

# ---
# Komentarz dotyczący `if-elif-else` vs `switch`:
# W językach takich jak C, C++ lub Java, istnieje konstrukcja `switch-case`,
# która pozwala na bardziej zwięzły zapis wielokrotnych warunków w zależności od wartości zmiennej.
# W Pythonie nie ma natywnej instrukcji `switch-case`, ale można uzyskać podobny efekt
# za pomocą ciągu `if-elif-else` lub, w bardziej zaawansowanych implementacjach,
# poprzez mapowanie funkcji w słowniku (dictionary mapping).
# Switch-case w językach takich jak C działa szybciej dla wielu warunków,
# ale `if-elif-else` w Pythonie spełnia podobną rolę z nieco większą czytelnością.
