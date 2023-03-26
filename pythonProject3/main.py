#Zadanie 1
a = input()
a = a.split(",")
amax = a[0]
amin = a[0]

for i in range(0, len(a), 1):
    if a[i] < amin:
        amin = a[i]

    if a[i] > amax:
        amax = a[i]

print(amin)
print(amax)

# Zadanie 2
import random

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań",
              "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]

plan_wycieczki = []

for i in range(0, 10):
    wybrane = random.choice(moja_lista)
    plan_wycieczki.append(wybrane)
    print(i + 1, ". ", wybrane)
    moja_lista.remove(wybrane)

# Zadanie 3
import getpass
import random

print("Gra Papier, Kamień, Nożyce")
print("Wybierz ilość rund: ")
ilosc_rund = input()
print("Wybierz tryb gry:  (komputer / 2 graczy")
tryb = input()

wynikgracz1 = 0
wynikgracz2 = 0
nazwa1 = ""
nazwa2 = "Komputer"
pgk = ["p", "k", "n"]

if tryb == 'komputer':
    print("Wybierz swoja nazwe")
    nazwa1 = input()

    for i in range(0, int(ilosc_rund)):
        print("Wybierz Papier - p, Kamien - k, Nozyce - n")
        choiceg = getpass.getpass("wybór: ")

        choicek = random.choice(pgk)

        if (choiceg == 'k' and choicek == 'k') or (choiceg == 'p' and choicek == 'p') or (
                choiceg == 'n' and choicek == 'n'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor komputera: ", choicek)
            print("Remis, nikt nie dostaje punktu")
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty komputera: ", wynikgracz2)

        if (choiceg == 'k' and choicek == 'n') or (choiceg == 'n' and choicek == 'p') or (
                choiceg == 'p' and choicek == 'k'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor komputera: ", choicek)
            print(nazwa1, " wygrywa z komputerem, dostaje 1 pkt")
            wynikgracz1 += 1
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty komputera: ", wynikgracz2)

        if (choiceg == 'n' and choicek == 'k') or (choiceg == 'p' and choicek == 'n') or (
                choiceg == 'k' and choicek == 'p'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor komputera: ", choicek)
            print("Komputer wygrywa z ", nazwa1)
            wynikgracz2 += 1
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty komputera: ", wynikgracz2)

    print("Ilosc punktow ", nazwa1, "to: ", wynikgracz1)
    print("Ilosc punktow komputera to: ", wynikgracz2)

    if wynikgracz1 > wynikgracz2:
        print("Wygral ", nazwa1, "!")
    elif wynikgracz2 > wynikgracz1:
        print("Wygral komputer!")
    else:
        print("Remis!")
else:
    print("Wybierz nazwe gracza 1")
    nazwa1 = input()
    print("Wybierz nazwe gracza 2")
    nazwa2 = input()

    for i in range(0, int(ilosc_rund)):
        print("Wybiera ", nazwa1)
        print("Wybierz Papier - p, Kamien - k, Nozyce - n")
        choiceg = getpass.getpass("wybór: ")

        print("Wybiera ", nazwa2)
        print("Wybierz Papier - p, Kamien - k, Nozyce - n")
        choicek = getpass.getpass("wybór: ")

        if (choiceg == 'k' and choicek == 'k') or (choiceg == 'p' and choicek == 'p') or (
                choiceg == 'n' and choicek == 'n'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor ", nazwa2, choicek)
            print("Remis, nikt nie dostaje punktu")
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty ", nazwa2, ": ", wynikgracz2)

        if (choiceg == 'k' and choicek == 'n') or (choiceg == 'n' and choicek == 'p') or (
                choiceg == 'p' and choicek == 'k'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor ", nazwa2, choicek)
            print(nazwa1, " wygrywa z ", nazwa2, " i dostaje 1 pkt")
            wynikgracz1 += 1
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty ", nazwa2, ": ", wynikgracz2)

        if (choiceg == 'n' and choicek == 'k') or (choiceg == 'p' and choicek == 'n') or (
                choiceg == 'k' and choicek == 'p'):
            print("Wybor ", nazwa1, ": ", choiceg, " Wybor ", nazwa2, choicek)
            print(nazwa2, " wygrywa z ", nazwa1, " i dostaje 1 pkt")
            wynikgracz2 += 1
            print("Punkty ", nazwa1, ": ", wynikgracz1, " Punkty ", nazwa2, ": ", wynikgracz2)

    print("Ilosc punktow ", nazwa1, "to: ", wynikgracz1)
    print("Ilosc punktow ", nazwa2, "to: ", wynikgracz2)

    if wynikgracz1 > wynikgracz2:
        print("Wygral ", nazwa1, "!")
    elif wynikgracz2 > wynikgracz1:
        print("Wygral ", nazwa2, "!")
    else:
        print("Remis!")
