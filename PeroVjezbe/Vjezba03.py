import TimeModule as tm

def prviZadatak():
    print()
    print("Vježba 3: Zadatak 1:")
    print()
    pcString = input("unesite 'pace' ako zelite podatke o paceu umjesto o brzini")
    pc = False
    if pcString == "pace":
        pc = True
    km = input("unesite prijedjeni put u metrima")
    min = input("unesite potrebno vrijeme u minutama")
    data=pace(pc,km,min)
    if pc:
        print("Pace: ".format(data))
    else:
        print("Brzina: ".format(data))


def drugiZadatak():
    print()
    print("Vježba 3: Zadatak 2:")
    print()

    h=-1
    m=-1
    while(h<0 or h>24):
        h=input("Unesite broj sati od 0 do 24")
    while (m < 0 or h > 60):
        m = input("Unesite broj minuta od 0 do 60")
    print(tm.dobaDana(h))


def pace(pace, udaljenostM, trajanjeM=60):
    if(pace):
        return (trajanjeM/60) / (udaljenostM/1000)
    else:
        return  (udaljenostM/1000) / (trajanjeM/60)

