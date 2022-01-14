import random


def prviZadatak():
    print()
    print("Vježba 2: Zadatak 1:")
    print()

    godina = (float)(input("unesi broj godina: "))
    liga=""
    if(godina > 80):
        print("Pre star za nogomet")
        return
    if godina < 0:
        print("Netočan unos godina")
        return
    if godina < 8:
        print("Pre mladi za upis")
        return
    if godina < 12:
        savez = input("Kojem nogometnom savetu pripadaš: ")
        savez= savez.lower()
        if savez.lower().__contains__("zagreb"):
            if godina<9:
                liga = "Zagići"
            elif godina<10:
                liga = "Limači"
            else:
                liga = "Mlađi pioniri"
        else:
            liga = "Početnici"
    elif godina <14:
        liga = "Pioniri"
    elif godina <16:
        liga = "Kadeti"
    elif godina <18:
        liga = "Juniori"
    else:
        liga = "Seniori"
    print(liga)


def treciZadatak(x):
    print()
    print("Vježba 2: Zadatak 3:")
    print()

    svi = [1]
    for i in range(1, x + 1):
        denums = __recDenum__(i)
        for i in svi:
            if denums.__contains__(i):
                denums.remove(i)
        svi = svi + denums
    sum = 1
    for i in svi:
        sum = sum * i

    print("Broj koji je djeljiv sa svim brojevima od 1 do {} je {}".format(x, sum))


def cetvrtiZadatak():
    print()
    print("Vježba 2: Zadatak 4:")
    print()

    najmanji = 1
    najveci = 200
    random.seed()
    brojKojiRacunaloGenerira = random.randint(najmanji, najveci)

    brojKojiKorisnikBira = input("Izaberi broj od 1 do 200: ")

    while brojKojiRacunaloGenerira != brojKojiKorisnikBira:
        if brojKojiRacunaloGenerira < brojKojiKorisnikBira:
            brojKojiKorisnikBira = input("Manje: ")
        else:
            brojKojiKorisnikBira = input("Više: ")
    print()
    print("Pogodak!")
    print()


def __recDenum__(x):
    if x == 1:
        return [1]
    for i in range(2,x+1):
        if x % i == 0:
            l = __recDenum__(x // i)
            return [i]+l


