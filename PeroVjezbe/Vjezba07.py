import sys
import cmath
import datetime

def prviZadatak():
    print()
    print("Vježba 7: Zadatak 1:")
    print()

    a = (int)(input("Unesi broj a"))
    b = (int)(input("Unesi broj b"))
    c = (int)(input("Unesi broj c"))

    try:
        discrimination = (b ** 2) - (4 * a * c)
        if a == 0 and b == 0 and c == 0:
            raise allAreZero
        if a == 0:
            raise aIsZero
        if discrimination == 0:
            raise discriminationIsZero
    except aIsZero:
        print()
        sys.exit()
    except allAreZero:
        sys.exit()
    except discriminationIsZero:
        sys.exit()

    rjesenje1 = (-b - cmath.sqrt(discrimination)) / (2 * a)
    rjesenje2 = (-b + cmath.sqrt(discrimination)) / (2 * a)
    print(rjesenje1)
    print(rjesenje2)

def drugiZadatak():
    print()
    print("Vježba 7: Zadatak 2:")
    print()

    date = datetime(2022, 1, 5)
    time = input("unesite vijeme")
    ispravnostDatuma(date, time)


def treciZadatak():
    print()
    print("Vježba 7: Zadatak 3:")
    print()

    tekstUnazad = ""
    for line in reversed(list(open("mojfile.txt"))):
        if len(line) == 0:
            raise Exception("emptyFile")
        tekstUnazad += line.rstrip()

    with open("mojemptyfile.txt", "w") as f:
        f.write(tekstUnazad[::-1])


def ispravnostDatuma(date, time):
    if int(time) < 0:
        raise Exception("Negativno vrijeme")
    if date.weekday() == 5:
        raise Exception("Vikendom ne radimo, dođite prekosutra")
    elif(date.weekday() == 6):
        raise Exception("Vikendom ne radimo, dođite sutra")
    if int(time) > 17:
        print("Izvan radnog vremena")


class Error(Exception):
    print("dogodio se error")
    pass
class aIsZero(Error):
    print("a je nula")
    pass
class allAreZero(Error):
    print("svi unosi su 0")
    pass
class discriminationIsZero(Error):
    print("Diskriminanta je 0")
    pass
