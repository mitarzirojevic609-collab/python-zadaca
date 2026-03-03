studnets = {
    "u1": {
        "name": "Ana",
        "ocene": [5,4,5],
    "u2": {
        "name": "Marko",
        "ocene": [3,4,4],
    },

    "u3": {
        "name": "Ana",
        "ocene": [5, 4, 5]
    }
    }
}

def prosek_ocena(ucenici):

    rezultati = {}

    for student in ucenici:
        podaci = ucenici[student]
        ocene = podaci["ocene"]
        prosek = sum(ocene) / len(ocene)
        rezultati[podaci["name"]] = prosek

    return rezultati

print(prosek_ocena(studnets))

#zadatak 2
def veci_od_proseka(lista):
    prosecna_vrednost = sum(lista) / len(lista)
    rezultat = []

    for number in lista:
        if number > prosecna_vrednost:
            rezultat.append(number)

    return rezultat
print(veci_od_proseka([5, 8, 13, 17, 22]))

#zadatak 3
products = {
    "hleb": {
        "cena": 100,
        "kolicina":50

},
    "pivo": {
        "cena": 150,
        "kolicina":200

},
    "jagode": {
        "cena": 90,
        "kolicina":30
    },
}

def ukupna_vrednost(proizvodi):
    ukupno = 0

    for proizvod in proizvodi:
        cena = proizvodi[proizvod]["cena"]
        kolicina = proizvodi[proizvod]["kolicina"]
        ukupno = ukupno + cena * kolicina
    return ukupno
print(ukupna_vrednost(products))

#zadatak 4
def najkraca_rec(lista):
    najkraca = lista[0]

    for rec in lista:
        if len(rec) / len(najkraca):
            najkraca = rec
        return najkraca
reci = ["duhovnost", "religija", "porodica", "vjera"]
print(najkraca_rec(reci))

#zadatak 5
zaposleni = {
    "z1": {"ime": "Milos", "plata": 1000},
    "z2": {"ime": "Marko", "plata": 1200},
    "z3": {"ime": "Jovan", "plata": 1500}
}
def iznad_proseka(zaposleni):
    ukupno = 0

    # računanje proseka
    for zaposlen in zaposleni:
        ukupno += zaposleni[zaposlen]["plata"]

    prosek = ukupno / len(zaposleni)

    rezultat = []

    for zaposlen in zaposleni:
        if zaposleni[zaposlen]["plata"] > prosek:
            rezultat.append(zaposleni[zaposlen]["ime"])

        return rezultat
    print(iznad_proseka(zaposleni))

#zadatak 6
def broj_ledenih_dana(temperatura):
    ukupno_vrednost = 0
    for temp in temperatura:
        if temp < 0:
            ukupno_vrednost += 1
    return ukupno_vrednost
lista_temperatura = [5, 3, -2, 3, -1, -4]
print(broj_ledenih_dana(lista_temperatura))

#zadatak 7
gradovi ={
"Beograd": {"drzava": "Srbija", "stanovnici": 1400000},
"Pariz": {"drzava": "Francuska", "stanovnici": 2100000}
}
def gradovi_u_drzavi(gradovi, drzava):
    rezultat = []
    for grad in gradovi:
        if gradovi[grad]["drzava"] == drzava:
            rezultat.append(grad)
    return rezultat

print(gradovi_u_drzavi(gradovi, "Srbija"))

#zadatak 8
def parni(lista):
    parnil = []
    for element in lista:
        if element % 2 == 0:
            parnil.append(element)
    return parnil
list_nummber = [2,5,3,4,7,9,8,6,12]
print(parni(list_nummber))

#zadatak 9
predmeti = {
    "p1": {
        "name": "srpski jezik",
        "lista poena": [70, 40,30,20]
    },
    "p2": {
        "name": "matematika",
        "lista poena": [65, 70, 80, 55]
    },
    "p3": {
        "name": "fizika",
        "lista poena": [40, 35, 50, 60]
    },
    "p4": {
        "name": "hemija",
        "lista poena": [50, 45, 70]
    }
}
def dovoljno_za_prolaza(predmeti):
    rezultat = {}
    for predmet in predmeti:
        prosjek = sum(predmeti[predmet]["lista poena"]) / len(predmeti[predmet]["lista poena"])
        if prosjek >=50:
            rezultat[predmet] = True
        else:
            rezultat[predmet] = False
    return rezultat
print(dovoljno_za_prolaza(predmeti))

#zadatak 10
def pocinju_sa(lista, slovo):
    rezultat = []
    for name in lista:
        if name[0] == slovo:
            rezultat.append(name)
    return rezultat
lista_imena = ["stefan", "srdjan", "matija", "jakov", "simon"]
print(pocinju_sa(lista_imena, "s"))

#zadatak 11
sportisti = {
    "s1": {
        "name": "stefan",
        "broj medalja": 10
    },
    "s2": {
        "name": "milos",
        "broj medalja": 12
    },
    "s3": {
        "name": "milorad",
        "broj medalja": 15
    },
    "s4": {
        "name": "srdjan",
        "broj medalja": 22
    }
}
def vise_od_medalja(sportisti, broj_medalja):
    rezultat = []
    for sportista in sportisti:
        if sportisti[sportista]["broj medalja"]>broj_medalja:
            rezultat.append(sportisti[sportista]["name"])
    return rezultat
print(vise_od_medalja(sportisti, 14))

#zadatak 12
mesovita_lista = [1, "Python", 3.5, "Kod", 7]
brojaci = {
    "int":0,
    "float":0,
    "str":0,
}
def broj_tipova(lista):
    for element in mesovita_lista:
        if isinstance(element, int):
           brojaci["int"] += 1
        elif isinstance(element, float):
            brojaci["float"] += 1
        elif isinstance(element, str):
           brojaci["str"] += 1
    return brojaci
print(broj_tipova(mesovita_lista))

#zadatak 13
filmovi = {
    "f1": {
        "name": "orlovi rano lete",
        "godina izlaska": 1984,
        "ocena" : 7
    },
    "f2": {
        "name": "kad porastem bicu kengur",
        "godina izlaska": 2002,
        "ocena" : 6
    },
    "f3": {
        "name": "lepa sela lepo gore",
        "godina izlaska": 1999,
        "ocena" : 9
    },
    "f4": {
        "name": "mrtav hladan",
        "godina izlaska": 2004,
        "ocena" : 8
    }
}
def visoka_ocena_filmovi(filmovi):
    rezultat = []
    for element in filmovi:
        if filmovi[element]["ocena"]>8:
            rezultat.append(filmovi[element]["name"])
    return rezultat
print(visoka_ocena_filmovi(filmovi))

#zadatak 14
lista_cijena = [200, 300, 400, 500, 1000]
def popust(lista, prag, procenat):
    nova_lista = []
    for price in lista:
        if price > prag:
            nova_cena = price -(price * procenat / 100)
            nova_lista.append(nova_cena)
        else:
            nova_lista.append(price)
    return nova_lista
print(popust(lista_cijena, 300, 10))

#zadatak 15
ucenici = {
    "u1": {
        "name": "marko",
        "godina": 16
    },
    "u2": {
        "name": "stefan",
        "godina": 27
    },
    "u3": {
        "name": "srdjan",
        "godina": 16
    },
    "u4": {
        "name": "milos",
        "godina": 23
    }
}
def punoljetni(ucenici):
    rezultat = []
    for imena in ucenici:
        if ucenici[imena]["godina"]>18:
            rezultat.append(ucenici[imena]["name"])
    return rezultat
print(punoljetni(ucenici))

#zadatak 16
def zbir_do_liste(lista, granice):
    zbir = 0
    for num in lista:
        zbir += num
        if zbir > granice:
            break
    return zbir
list_num = [5,7,4,2]
print(zbir_do_liste(list_num, 22))

#zadatak 17
restorani = {
    "r1": {
        "name": "kamin",
        "ocene": [5,4,3,4]
    },
    "r2": {
        "name": "kula",
        "ocene": [2,3,2,5,]
    },
    "r3": {
        "name": "orac",
        "ocene": [1,3,2,3]
    },
    "r4": {
        "name": "perla",
        "ocene": [4,4,5,5]
    }
}
def prosek_restorana(restorani):
    rezultat ={}
    for num in restorani:
         podaci = restorani[num]
         ocene = podaci["ocene"]
         prosek = sum(ocene) / len(ocene)
         rezultat[podaci["name"]] = prosek
    return rezultat
print(prosek_restorana(restorani))

#zadatak 18
list_recen = ["duga recenica", "kratka recenica", "i ovo je recenica"]
def duge_recenice(lista, n):
    rezultat = []
    for rec in lista:
        if len(rec) > n:
            rezultat.append(rec)
    return rezultat
print(duge_recenice(list_recen, 14))

#zadatak 19
kursevi = {
    "k1": {
        "naziv": "Python Osnove",
        "polaznici": ["Marko", "Ana", "Jovan"]
    },
    "k2": {
        "naziv": "Web Development",
        "polaznici": ["Milos", "Sara"]
    },
    "k3": {
        "naziv": "Data Science",
        "polaznici": ["Ivana", "Nikola", "Petar", "Luka"]
    },
    "k4": {
        "naziv": "Cyber Security",
        "polaznici": ["Teodora", "Stefan"]
    }
}
def popunjenost(kursevi, prag):
    rezultat = []
    for kurs in kursevi:
        broj_polaznika = len(kursevi[kurs]["polaznici"])
        if broj_polaznika > prag:
            rezultat.append(kurs)
    return rezultat
print(popunjenost(kursevi, 2))

#zadatak 20
ucenici = [
    {
        "ime": "Marko",
        "godine": 23,
        "ocene": [5, 4, 3, 5]
    },
    {
        "ime": "Ana",
        "godine": 16,
        "ocene": [4, 4, 5, 5]
    },
    {
        "ime": "Jovan",
        "godine": 22,
        "ocene": [3, 2, 4, 3]
    },
    {
        "ime": "Sara",
        "godine": 17,
        "ocene": [5, 5, 5, 4]
    }
]
def prosek_punoletnih(lista_ucenika):
    rezultat = {}
    for ucenik in lista_ucenika:
        if ucenik["godine"]>=18:
            prosek = sum(ucenik["ocene"]) / len(ucenik["ocene"])
            rezultat[ucenik["ime"]] = prosek
    return rezultat
print(prosek_punoletnih(ucenici))






