from random import randrange

def prviZadatak():
    print()
    print("Vježba 10: Zadatak 1:")
    print()
    torba1 = Torba()
    torba2 = Torba()
    torba1.putIn(["1",2,3.4])
    torba2.putIn(torba1)
    print(torba1.__str__())
    print(torba2.__str__())


def drugiZadatak():
    print()
    print("Vježba 10: Zadatak 2:")
    print()

    mojDek = Dek()
    karta = mojDek.povuciKartu()
    print(karta)


class Torba:
  def __init__(self):
    self.sadrzaj = []
  def putIn(self,nekiSadržaj):
    self.sadrzaj.append(nekiSadržaj)
  def __str__(self):
    return self.sadrzaj

class Karta(object):
  def __init__(self):
    self.kr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    self.karte = {
        "pik": [self.kr],
        "herc": [self.kr],
        "karo": [self.kr],
        "tref": [self.kr]
    }

  def __str__(self):
      print(self.karte["pik"])
  def getLen(self):
      duljina = 4
      for i in self.karte.keys():
          for j in self.karte[i]:
              duljina += len(j)
      return duljina


class Dek(Karta):
    def __init__(self):
        self.dek = Karta()

    def povuciKartu(self):
        if(self.dek.getLen() == 0):
            print("Nema više karti")
        else:
            while(True):
                boja = randrange(0, 3)
                vrijednost = randrange(1, 12)
                if self.postojiLiKarta(boja, vrijednost):
                    return self.izaberiKartu(boja, vrijednost)
        pass
    def dodajKartu(self, kr):
        self.dek.karte[kr[1]][0].append(kr[0])
        self.dek.karte[kr[1]][0].sort()
        pass


    def postojiLiKarta(self, bj, br):
        x = list(self.dek.karte)[bj]
        a = self.dek.karte[x][0]
        if br in a:
            return True
        else:
            return False


    def izaberiKartu(self, boja, br):
        x = list(self.dek.karte)[boja]
        self.dek.karte[x][0].remove(br)
        return [x, br]
