def prviZadatak():
    print()
    print("Vjezba 1: Zadatak 1:")
    print()
    print("The test scores program")
    print()
    print("Enter 3 test scores")
    print("=======================")

    # unesi 3 rezultata
    total_score = 0     #postavimo total score na 0 pa mu dodajemo score
    total_score += (int)(input("Enter test score: "))
    total_score += (int)(input("Enter test score: "))
    total_score += (int)(input("Enter test score: "))

    #logika
    avg_score = total_score/3

    #ispis
    print("==================================================")
    print("Total score: {0}, Avg score: {1}".format(total_score, avg_score))
    print()
    print("Bye")

def drugiZadatak():
    print()
    print("Vjezba 1: Zadatak 2:")
    print()
    #unesi podatke
    km_driven = (float)(input("Enter km driven: "))
    money_payed = (float)(input("Enter money payed: "))

    if km_driven==0:
        print("Broj predjenih kilometara nemoze bit 0")
        return
    #racunaj
    mpg = money_payed/km_driven
    mpg = float.__round__(mpg,2)
    print("Money per kilometar: {0}".format(mpg))
    print()
    print("Bye")

def treciZadatak():
    print()
    print("Vjezba 1: Zadatak 3:")
    print()
    #unesi podatke
    ime = input("Unesi ime: ")
    udaraca = (int)(input("Unesi broj udaraca: "))
    pogodaka = (int)(input("Unesi broj pogogdaka: "))

    if pogodaka>udaraca:
        print("broj pogodaka nemoze biti veci od broja udaraca")
        return
    print("Ime:{}".format(ime))
    print("Broj udaraca:{}".format(udaraca))
    print("Broj pogodaka:{}".format(pogodaka))
    print("Za sportaša {} prosjek pogodaka je {}%".format(ime,pogodaka/udaraca*100))
