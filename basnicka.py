print("Napiš program, který vypíše básničku ze souboru basnicka.txt, ale obrátí pořadí veršů ")
radky = []
with open("basnicka.txt", encoding='utf-8') as soubor:
    radky = soubor.readlines()
    radky.reverse()
    opak = list(radky)
for radek in opak:
    print(radek)

print("Napiš program, který obrátí pořadí slov v jednotlivých verších")
radky2 = []
dalsi = []
c = []
a = []
with open("basnicka.txt", encoding='utf-8') as soubor:
    radky2 = soubor.readlines()

for i in radky2:
    c = i.split()
    c.reverse()
    dalsi = " ".join(c)
    a.append(dalsi)

for radek in a:
    print(radek)

print("Obrať pořadí slok (ty by měly být oddělené jedním prázdným řádkem).")
i = 0
if i < 4:
    for i in range(1,4):

        radky = []
        with open("basnicka.txt", encoding='utf-8') as soubor:
            radky = soubor.readlines()
        vyber = []
        n = 16
        n2 = 23
        vyber = (radky[(n -(i-1)*8):(n2 -(i-1)*8)])
        for radek in vyber:
            print(radek)
        print("\n")
i += 1

print("Vypiš slova básně v náhodném pořadí.")
import random
radky2 = []
dalsi = []
c = []
a = []
d = []
with open("basnicka.txt", encoding='utf-8') as soubor:
    radky2 = soubor.readlines()
    random.shuffle(radky2)

for i in radky2:
    c = i.split()
    random.shuffle(c)
    dalsi = " ".join(c)
    a.append(dalsi)
random.shuffle(a)

for radek in a:
    print(radek)
