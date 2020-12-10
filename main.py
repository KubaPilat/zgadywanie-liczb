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