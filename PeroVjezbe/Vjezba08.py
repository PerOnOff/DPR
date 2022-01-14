import datetime

def prviZadatak():
    print()
    print("Vježba 8: Zadatak 1:")
    print()

def program():
    userCommand = input("printaj / dodaj / briši / izađi")
    if userCommand == "printaj":
        printajStudenta()
        program()
    elif userCommand == "dodaj":
        dodajStudenta()
        program()
    elif userCommand == "briši":
        brisiStudenta()
        program()
    elif userCommand == "izađi":
        print("Izlaz")

def dodajStudenta():
    ime = input("Ime i prezime: ")
    oib = input("Oib: ")
    adresa = input("Adresa: ")
    datumRaw = input("Datum rodenja (YYYY-MM-DD): ")
    year, month, day = map(int, datumRaw.split('-'))
    datum = datetime.date(year, month, day)
    prosjek = input("Unesite prosjek ocjena \n")
    bazaStudenata[ime] = { "oib" : oib, "adresa": adresa, "datumRodenja": datum, "prosjek": prosjek }

    print("Baza ažurirana\n")
    print()
    print(bazaStudenata)
    print()

bazaStudenata = {
    "Perica Jurić":
    {
        "oib": "88174171678",
        "adresa": "Jablanička Ulica",
        "datumRodenja": datetime.datetime(1992, 1, 18),
        "prosjek": 3.33
    }
}

def printajStudenta():
    naziv = input("Unesite ime i prezime studenta: ")
    podatci = bazaStudenata.get(naziv)
    print(podatci)

def brisiStudenta():
    ime = input("Ime i prezime studenta za brisanje \n")
    del bazaStudenata[ime]
    print("Baza ažurirana\n")
    print()
    print(bazaStudenata)
    print()