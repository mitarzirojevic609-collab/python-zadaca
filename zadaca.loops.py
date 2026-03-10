#zadatak 1
import math

from domaci import iteam
from zadaca_TE import lista_recenica

mix_tipe = ["test", 29,20,5, 3,4,5.3,"milan"]
int_count = 0
str_count = 0
float_count = 0
for item in mix_tipe:
    if isinstance(item, int):
        int_count += 1
    elif isinstance(item, str):
        str_count += 1
    elif isinstance(item, float):
        float_count += 1
print(f"integera ima {int_count}")
print(f"stringa ima {str_count}")
print(f"floata ima {float_count}")
#zadatak 2
brojevi = [-5,-4,2,1,-7,9,10,-12,14]
positive_sum = 0
for item in brojevi:
    if item > 0:
        positive_sum += item
print(positive_sum)
#zadatak3
for item in brojevi:
    if item <0:
        print(f"prvi negativan broj je {item}")
        break
#zadatak 4
list_of_string =["reciklaza", "stanovnistvno", "mogucnosti", "radioaktivnost"]
najduza_rijec = list_of_string[0]
for rijec in list_of_string:
    if len(rijec) > len(najduza_rijec):
        najduza_rijec = rijec
print(f"najduza rijec u listi je {najduza_rijec}")
#zadatak 5
ocene = [1, 2, 3, 4, 5]
pozitivne_ocene = []
for svaka_ocena in ocene:
    if svaka_ocena >= 2:
        pozitivne_ocene.append(svaka_ocena)
print(pozitivne_ocene)
#zadatak 6
ocene = [1, 2, 3, 4, 5]
number_of_odd = 0
number_of_even = 0
for num in ocene:
    if num % 2 == 0:
        number_of_even += 1
    else: number_of_odd += 1
print(f"broj parnih brojevi: {number_of_even} a broj neparvnih brojeva je {number_of_odd}")
#zadatak 7
temperatura = (20,15,25,27,22,13,11)
prosecna_temperatura = sum(temperatura) / len(temperatura)
print(prosecna_temperatura)
if prosecna_temperatura <= 15:
    print("hladno")
elif prosecna_temperatura >= 15 and prosecna_temperatura <= 25:
    print("prijatno")
elif prosecna_temperatura >= 25:
    print("vruce")
#zadatak8
imena = ["Stefan", "Srdjan", "Milan", "Milos", "Matija"]
for name in imena:
    if len(name ) >5:
        print(name)
#zadatak 9
i = ["test", 29,20,5, 3,4,5.3,"milan"]
for tekst in i:
    if isinstance(tekst, str):
        print(tekst)
#zadatak 10
brojevi = [-5,-4,2,1,-7,9,10,-12,14,0]
lowest = brojevi[0]
highest = brojevi[0]
for broj in brojevi:
    if broj > highest:
        highest = broj
    if broj < lowest:
        lowest = broj
print(f"najmanji broj u listi je {lowest} a najveci broj u listi je {highest}")
#zadatak 11
brojevi = [-5,-4,2,1,-7,0,1,2,14]
for lista in brojevi:
    if lista == 0:
        print("pronadjen broj 0")
        break
    else:
        print(lista)
#zadatak 12
brojevi = [25,30,40,60,50]
zbir = 0
for broj in brojevi:
    zbir += broj
    if zbir > 100:
        break
    print(zbir)
#zadatak 13
lista_recenica = ["ovo je recenica", "ovo je recenica sa dvadeset karaktera", "ovo nije"]
broj_recenica = 0
for ukupno in lista_recenica:
    if len(ukupno) > 10:
        broj_recenica += 1
print(f"ukupno imamo: {broj_recenica} recenice sa deset karaktera")
#zadatak 14
brojevi = [-5,-4,2,1,-7,9,10,-12,14,0]
nova_kvad_list = []
for nume in brojevi:
    kvadrat = nume * nume
    nova_kvad_list.append(kvadrat)
print(nova_kvad_list)
#zadatak 15
mix_tipe = ["test", 29,20,5, 3,4,5.3,"milan"]
for index, elem in enumerate(mix_tipe):
    print(index, elem)
#zadatak 16
zbir = 0
while True:
 user = int (input("unesite broj"))
 if user <0:
     break
zbir += user
print(zbir)
#zadatak 17
brojevi = [-5,-4,2,1,-7,9,10,-12,14,0]
find_number = 7
if find_number in brojevi:
    print(f"{find_number}broj u listi je pronadjen")
else:
    print(f"{find_number}broj u listi ne postoji")
#zadatak 18
brojevi = [-5,-4,2,1,-7, 2, 12, 10,9,10,-12,14,0]
s=set()
dup = []
for n in brojevi:
    if n in s:
        dup.append(n)
    else:
        s.add(n)
print(dup)
#zadatak 19
cena = [500,600,700,800,900,1000]
nove_cene = []
for c in cena:
    nova_cena = c * 1.10
    nove_cene.append(nova_cena)
print(nove_cene)
#zadatak 20
igraci = [
    ("mitar", 20),
    ("matija", 30),
    ("stefan", 18),
    ("srdjan", 10),
    ("veselin", 15)
]
zbir_poena = 0
for ime, poeni in igraci:
    zbir_poena += poeni
prosek = zbir_poena / len(igraci)
print("Prosek poena je:", prosek)
print("Igraci iznad proseka:")
for ime, poeni in igraci:
    if poeni > prosek:
        print(ime)



