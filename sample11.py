from datetime import datetime

# Wprowadź rok urodzenia jako liczbę całkowitą
rok_urodzenia = int(input("Podaj rok urodzenia: "))

# Pobierz aktualny rok
aktualny_rok = datetime.now().year

# Oblicz wiek
wiek = aktualny_rok - rok_urodzenia

# Sprawdź, czy osoba jest pełnoletnia
if wiek >= 18:
    print("Jesteś pełnoletni/a.")
else:
    print("Nie jesteś pełnoletni/a.")