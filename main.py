#początek losowanie liczb
import random
ListaWylosowanychLiczb = []#tworzenie pustej tablicy potem w linijce 6 dodajemy liczby do tej tablicy
for i in range(0, 5):#ile liczb ma sie wylosowac domyslnie 5
    x = random.randint(1, 200)#zakres liczb od 1 do 200
    ListaWylosowanychLiczb.append(x)#dodawania liczb "x" do tablicy
    ListaWylosowanychLiczb.sort()#sortowanie liczb po dodaniu
print(ListaWylosowanychLiczb)#dac to jako komentarz zeby user nie widzial jakie sa wylosowane liczby ale do ulatwienia dodalem zeby wiedziec jakie sa mozliwe odpowiedzi

A = ListaWylosowanychLiczb[0]#najmniejsza liczba
Z = ListaWylosowanychLiczb[4]#najwieksza liczba
G = ListaWylosowanychLiczb[2]#poprawna odpowiedz dla ułatwienia
#koniec losowanie

#początek zakresu
print("NAJMNIEJSZA Z WYLOSOWANYCH LICZB TO...", A)
print("NAJWIĘKSZA Z WYLOSOWANYCH LICZB TO...", Z)
#koniec zakresu

#początek petla do zgadywania
for i in ListaWylosowanychLiczb:#petla for dziala na tablicy 
    odp = int(input("Jaką liczbę od 1 do 200 mam na myśli? "))#podawanie odpowiedz przez user
    if odp == G:#warunek jak user zgadnie
        print("BRAWO")
        break
    else:#warunek jak user nie zgadnie
        print("NIESTETY")
        print("PRÓBUJ DO SKUTKU")
#koniec petla do zgadywania

"""
miejsce na ocenę:



"""