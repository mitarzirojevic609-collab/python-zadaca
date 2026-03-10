# zadatak 1

lista = ["ovo je lista", 20, 20.5]
if isinstance(lista [0], str):
    print("prvi element je string")
#zadatak 2
if not lista:
    print("lista je prazna")
else:
    print(f"Lista ima {len(lista)} elemenata")
#zadatak3
if len(lista)>3:
    print("prvi element liste" [0])
    print("poslednji element liste" [-1])
else:
    print("lista je prekratka")
#zadatak 4
godina_starosti = [19,19, 23, 25, 30]
if any(godina <18 for godina in godina_starosti):
    print("nisu svi punoljetni")
else:
    print("svi su punoljetni")
#zadatak 5
cena_proizvoda = [500, 700, 800, 1200, 3000]
prosecna_cena = sum(cena_proizvoda) /len(cena_proizvoda)
print(prosecna_cena)
if prosecna_cena > 1000:
    print("skupo")
else:
    print("povoljno")
#zadatak 6
lista_stringova = ["Java", "C++", "Python"]
if "Python" in lista_stringova:
    print("u listi je Python")
else:
    print("")
#zadatak 7
brojevi = [3,4,2,1,]
pozitivni = 0
negativni = 0
for broj in brojevi:
    if broj > 0:
        pozitivni += 1
    elif broj < 0:
        negativni += 1
if pozitivni > negativni:
    print("vise pozitivnih")
#zadatak 8
reci = ["moc", "slava", "novac", "zdravlje", "sreca", "vjerovanje"]
najduza = max(reci, key=len)
if len(najduza)>8:
    print("najduza rec je veca od 8 slova")
#zadatak 9
ocene = [1,2,3,4,5]
if 1 in ocene:
    print("ima nedovolja ocena")
#zadatak 10
for element in ocene:
    if not isinstance(element, int):
        print("lista ne sadrzi samo brojeve")
        break
    else:
        print("zbir je", sum(ocene))
        break
#zadatak 11
for paran_broj in ocene:
    if paran_broj % 2 ==0:
        print("lista sadrzi paran broj")
        break
#zadatak 12
imena = ["Milos", "Stefan", "Srđan", "Milutin", "Ugljesa", "Vukasin"]
if len(imena)>5:
    print("velika lista imena")
#zadatak 13
    lista1 = [15, -2, 30, 1, 2,4,5,6,7,40.5]
    if min(lista1)<0:
        print("postoji negativni broj")
#zadatak 14
if len (lista1)==10:
    print("lista ima idealnu duzinu")
#zadatak 15
lista1[-1]
if isinstance(lista1[-1], float):
    print("decimalni broj")
#zadatak 16
lista_cena = [1000,200,3000,4000,6000]
najveca_cena = max(lista_cena)
if najveca_cena > 5000:
    nova_cena = najveca_cena * 0.9
    print("cena nakon popusta", nova_cena)
#zadatak 17
lista_recenica = ["ovo je recenica", "ovo je recenica sa dvadeset karaktera"]
for recenica in lista_recenica:
    if len(recenica)>20:
        print("duga recenica pronadjena")
#zadatak 18
lista = [1, "natpis", 3,4]
ima_string = False
ima_brojeve = False
for element in lista:
    if isinstance(element, str):
        ima_string = True
    elif isinstance(element, (int, float)):
        ima_brojeve = True
    else:
        print("mesoviti tip poadataka")
    #zadatak 19
    lista_brojeva = [50,60,70,80]
    prosjecna_vrjednost = sum(lista_brojeva)/len(lista_brojeva)
    if prosjecna_vrjednost > 50 and prosjecna_vrjednost < 100:
        print("prosek je u ocekivanom opsegu")
    #zadatak 20
    temperatura = [15, 20, 25, 30]
    najveca = max(temperatura)
    if najveca > 30:
        print("vruce")
    elif najveca > 15 and najveca <= 30:
        print("prijatno")
    else:
        print("hladno")
    break





