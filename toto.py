import random

liczba = random.randint(1, 10)
# print("Wylosowana liczba:", liczba)

odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
# print("Podałeś liczbę: ", odp)

if liczba == int(odp):
    print("Zgadłeś! Dostajesz długopis!")
else:
    print("Nie zgadłeś. Spróbuj jeszcze raz.")