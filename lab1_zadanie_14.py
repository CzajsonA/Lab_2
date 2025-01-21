# Pobierz nazwę pliku od użytkownika
filename = input("Podaj nazwę pliku: ")

# Sprawdzenie rozszerzenia pliku za pomocą if/else
if filename.endswith(".xlsx") or filename.endswith(".xls"):
    print("Podany plik jest arkuszem Excel.")
else:
    print("Podany plik nie jest arkuszem Excel.")

# Metoda `endswith()` w Pythonie pozwala sprawdzić, czy dany ciąg znaków (string)
# kończy się określonym wzorcem lub wzorcami (np. ".xlsx", ".xls").
# Metoda zwraca wartość True, jeśli ciąg kończy się podanym wzorcem, i False w przeciwnym przypadku.
# Można przekazać jeden wzorzec jako ciąg znaków lub wiele wzorców w krotce (tuple).
# Przykład:
# - "plik.xlsx".endswith(".xlsx") -> True
# - "plik.txt".endswith(".xlsx") -> False
# Metoda jest przydatna przy pracy z nazwami plików i sprawdzaniu ich typów.
