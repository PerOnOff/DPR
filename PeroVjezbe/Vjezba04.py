def prviZadatak():
    print()
    print("Vjezba 4: Zadatak 1:")
    print()
    fiba1113 = [1, 1, 1, 3, 5, 9, 17, 32, 58, 107, 197, 394, 698, 1289, 2381, 4368,
               8038, 14787, 27193, 50018,91998, 169209, 311225, 572432, 1052866]

    x = -1
    while x < 1 or x > 25:
        input("Unesite broj od 1 do 25: ")
    print ("Fibanacijev broj pod rednim brojem {} je {}".format(x,fiba1113[x - 1]))

def drugiZadatak():
    print()
    print("Vjezba 4: Zadatak 2:")
    print()

    prva = input("Unesite prvu riječ")
    druga = input("Unesite drugu riječ")

    if sorted(prva) == sorted(druga):
        print("Prva i druga riječ su Anagrami")
    else:
        print("Prva i druga riječ nisu Anagrami")


def treciZadatak():
    print()
    print("Vjezba 4: Zadatak 3:")
    print()
    listaSaDuplikatom = ["nikolina", "ninoslava", "ana", "perica", "marija", "ana"]
    listaBezDuplikata = ["nikolina", "ninoslava", "ana", "perica", "marija", "banana"]

    print("Lista sa duplikatom: ".format(listaSaDuplikatom))
    if __imaDupleVrijednosti__(listaSaDuplikatom):
        print("Provjera duplikata vraća True")
    else:
        print("Provjera duplikata vraća False")

    print()

    print("Lista bez duplikata: ".format(listaBezDuplikata))
    if __imaDupleVrijednosti__(listaBezDuplikata):
        print("Provjera duplikata vraća True")
    else:
        print("Provjera duplikata vraća False")

def cetvrtiZadatak():
    print()
    print("Vjezba 4: Zadatak 4:")
    print()
    listaSaDuplikatom = ["nikolina", "ninoslava", "ana", "perica", "marija", "ana"]
    print("Lista sa duplikatom prije izbacivanja: ".format(listaSaDuplikatom))
    listaSaDuplikatom = __ukloniDuplikate__(listaSaDuplikatom)
    print("Lista sa duplikatom poslije izbacivanja: ".format(listaSaDuplikatom))


def __imaDupleVrijednosti__(x):
    if len(x) == len(set(x)):
        return False
    else:
        return True

def __ukloniDuplikate__(x):
  return list(dict.fromkeys(x))