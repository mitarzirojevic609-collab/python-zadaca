
#zadatal 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#zadatak 2
    def predstavi_se(self):
        print(f"Ja sam {self.name} i idem u {self.age} godinu")

Ana = Student("Ana", 2)
Ana.predstavi_se()

#zadatak 3
Marko = Student("Marko", 3)
Marko.predstavi_se()

#zadatak 4
class Knjiga:
    def __init__(self, naslov, autor):
        self.naslov = naslov
        self.autor = autor

#zadatak 5
    def opis(self):
        return f"{self.naslov} - {self.autor}"

#zadatak 6
knjige = [
    Knjiga("Na Drini ćuprija", "Ivo Andrić"),
    Knjiga("Jazavac pred sudom", "Petar Kočić"),
    Knjiga("Prokleta avlija", "Ivo Andrić")
]
def ispis_svih_naslova(lista):
    for knjige in lista:
        print(knjige.naslov)
ispis_svih_naslova(knjige)

#zadatak 7
class Automobil:
    def __init__(self, marka, model, godina):
        self.marka = marka
        self.model = model
        self.godina = godina

#zadatak 8
    def stanje(self):
        return f"{self.marka} {self.model} {self.godina}"

#zadatak 9
def dodaj_automobil(lista, auto):
    lista.append(auto)

#zadatak 10
class Zaposleni:
    def __init__(self, ime, pozicija, plata):
        self.ime = ime
        self.pozicija = pozicija
        self.plata = plata
#zadatak 11
def povecaj_platu(self, iznos):
    self.plata += iznos
#zadatak 12
class Manager(Zaposleni):
    def __init__(self, ime, pozicija, plata, tim):
        super().__init__(ime, pozicija, plata)
        self.tim = tim

#zadatak 13
def dodaj_u_tim(self, ime):
    self.tim.append(ime)

#zadatak 14
class Krug:
    def __init__(self, poluprecnik):
        self.poluprecnik = poluprecnik

    def povrsina(self):
        return 3.14 * self.poluprecnik * self.poluprecnik

#zadatak 15
class Pravougaonik:
    def __init__(self, duzina, sirina):
        self.duzina = duzina
        self.sirina = sirina

#zadatak 16
class Oblik:
    def povrsina(self):
        return 0

class Krug(Oblik):
    def __init__(self, poluprecnik):
        self.poluprecnik = poluprecnik

    def povrsina(self):
        return 3.14 * self.poluprecnik * self.poluprecnik


class Pravougaonik(Oblik):
    def __init__(self, a, b):
        self.a = a
        self .b = b
    def povrsina(self):
        return self.a * self.b

#zadatak 17
class BankovniRacun:
    def __init__(self, ime_vlasnika, stanje):
        self.ime_vlasnika = ime_vlasnika
        self.stanje = stanje
#zadatak 18

    def uplata (self, iznos):
        self.stanje += iznos

    def isplata (self, iznos):
        self.stanje -= iznos

#zadatak 19
    def get_stanje(self):
        return self.__stanje

#zadatak 20
racuni = [
    BankovniRacun("Ana", 100),
    BankovniRacun("Marko", 200),
    BankovniRacun("Ivan", 300)
]

def ispis_svih_racuna(lista):
    for racun in lista:
        print(racun.ime_vlasnika, racun.stanje)
ispis_svih_racuna(racuni)







