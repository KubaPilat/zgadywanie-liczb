import random
mylist = []
for i in range(0, 5):
    x = random.randint(1, 200)
    mylist.append(x)
    mylist.sort()
print(mylist)

A=mylist[0]
Z=mylist[4]

print("Najmniejsa wysolowana liczba to: ", A)
print("Największa wysolowana liczba to: ", Z)

#for i in range(3):
 #   print("Próba ", i + 1)
  #  odp = input("Jaką liczbę od 1 do 50 mam na myśli? ")
    # print("Podałeś liczbę: ", odp)

   # if liczba == int(odp):
    #    print("Zgadłeś! Dostajesz długopis!")
     #   break
    #elif i == 2:
     #   print("Miałem na myśli liczbę: ", liczba)
    #else:
     #   print("Nie zgadłeś. Spróbuj jeszcze raz.")
    #print()

"""
Na ocenę dobrą:-komputer losuje liczbęz zakresu 1-50-użytkownik próbuj odgadnąć tą liczbę
-jeżeli odgaduje, to komunikat BRAWO-w przeciwnym razie komunikat NIESTETY
Na ocenę bardzo dobrą:-komputer losuje liczbęz zakresu 1-50-użytkownik próbuj odgadnąć tą liczbę
-jeżeli odgaduje, to komunikat BRAWO-w przeciwnym razie komunikat NIESTETYoraz PRÓBUJ DO SKUTKU (program wraca do początku)
Na oceną celującą:-komputer losuje pięć liczb(zakres 1-200)
-wyznacza największą i najmniejsząz nich
-komputer wyświetla komunikat: NAJMNIEJSZA Z WYLOSOWANYCH LICZB TO...NAJWIĘKSZA Z WYLOSOWANYCH LICZB TO...
Do 18 grudnia
"""