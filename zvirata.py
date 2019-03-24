seznamZvirat = ["pes", "kočka", "králík", "had"]
dalsiSeznamZvirat = ["holub","tygr","kočka","had"]

def kratkeSlova(seznamZvirat):
    """
    Funkce vrací jména domácích zvířat (zadaných argumentem), která jsou kratší než 5 písmen
    """
    kratkeZvirata = []
    for zvire in seznamZvirat:
        if len(zvire) < 5:
            kratkeZvirata.append(zvire)
    return(kratkeZvirata)

print("Seznam krátkých zvířat je: ",kratkeSlova(seznamZvirat))

def zvirataK(seznamZvirat):
    """
    Funkce vrací jména domácích zvířat (zadaných argumentem), která začínají na k
    """
    zvirataZacinajiciK = []
    for zvire in seznamZvirat:
        if zvire.startswith("k"):
            zvirataZacinajiciK.append(zvire)
    return(zvirataZacinajiciK)

print("Seznam zvířat začínající na k je: ",zvirataK(seznamZvirat))

slovo = input("Jaké zvíře chceš otestovat na přítomnost v seznamu?")
def jeVseznamu(seznamZvirat,slovo):
    """
    Funkce, která dostane slovo a zjistí, jestli je v seznamu domácích zvířat
    """
    if slovo in seznamZvirat:
        return True
    else:
        return False
print("True/False přítomnosti zvířete v seznamu: ",jeVseznamu(seznamZvirat,slovo))

def dvaSeznamy(seznamZvirat,dalsiSeznamZvirat):
    """
    Funkce, která porovnává dva seznamy.
    """
    vObou = seznamZvirat+dalsiSeznamZvirat
    vPrvnim = []
    vDruhem = []
    for slovo in seznamZvirat:
        if slovo not in dalsiSeznamZvirat:
            vPrvnim.append(slovo)
    for slovo in dalsiSeznamZvirat:
        if slovo not in seznamZvirat:
            vDruhem.append(slovo)
    return("V obou:", vObou,"V prvním:",vPrvnim,"V druhém:",vDruhem)
print(dvaSeznamy(seznamZvirat,dalsiSeznamZvirat))

def serazeni(seznamZvirat):
    """
    Funkce, která seřadí zvířata.
    """
    seznamZvirat == seznamZvirat.sort()
    return(seznamZvirat)
print("Seřazená zvířata: ",serazeni(seznamZvirat))

seznamZvirat == seznamZvirat.append("andulka")
print("Zvířata s andulkou ",seznamZvirat)
druhaPismena = []
seznamDvojic = []
serazeno = []

for zvire in seznamZvirat:
    druhaPismena.append(zvire[1])

for pismeno, zvire in zip(druhaPismena,seznamZvirat):
    seznamDvojic.append((pismeno,zvire))
    seznamDvojic == seznamDvojic.sort()


for pismeno, zvire in seznamDvojic:
    serazeno.append(zvire)
print("Seřazené zvířata, kdy andulka nedráždí hada: ",serazeno)
