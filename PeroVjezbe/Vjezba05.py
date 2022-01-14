import numpy as np

def prviZadatak():
    print()
    print("Vježba 5: Zadatak 1:")
    print()

    a = (int)(input("Unesite djeljenik"))
    b = (int)(input("Unesite djelitelj (veći od 0)"))
    while b <= 0:
        b = (int)(input("Unesite djelitelj (veći od 0)"))
    obaviCjelobrojnoDijeljenje(a,b)

def drugiZadatak():
    print()
    print("Vježba 5: Zadatak 2:")
    print()

    print("1+2+3+4+5 = ")
    suma = sumsve([1, 2, 3, 4, 5])
    print(suma)

def treciZadatak():
    print()
    print("Vježba 5: Zadatak 3:")
    print()

    abc = "abc"
    br = [0, 1, 2]

    rezultat = zip(abc, br)
    print(list(rezultat))

def cetvrtiZadatak():
    print()
    print("Vježba 5: Zadatak 4")
    print()

    x = 0
    while x < 1:
        x = int(input("Unesi broj 'od'"))

    y = 0
    while y < 1:
        y = int(input("Unesi broj 'do'"))

    matrix = np.random.randint(10, size=(x, y))
    print(matrix)
    print(np.linalg.inv(matrix))


def obaviCjelobrojnoDijeljenje(x,y):
    rezultat = x / y
    ostatak = x % y
    par = (round(rezultat, 0), ostatak)
    print(par)

def sumsve(*args):
    suma = 0
    for i in args:
        suma = sum(i)
    return suma