from random import randrange
def pole(souradnice):
    """
    Vykreslí pole s "hadem" a ovocem.
    """
    for j in range(vyska):
        for i in range(sirka):
            if (i,j) in souradnice:
                print("X", end = " ")
            elif(i,j) in ovoce:
                print("?",end = " ")
            else:
                print(".", end = " ")
        print()

def posun(souradnice,smer,ovoce,vyska,sirka):
    """
    Zajišťuje pohyb hada.
    """
    while True:
        pocitadloOvoce = 0
        pridanaSouradnice = souradnice[-1]
        x, y = pridanaSouradnice
        if smer == 's':
            novaSourednice = x, y-1
        elif smer == 'j':
            novaSourednice = x, y+1
        elif smer == 'v':
            novaSourednice = x+1, y
        elif smer == 'z':
            novaSourednice = x-1, y
        else:
            False

        x,y = novaSourednice

        if novaSourednice in souradnice:
            print("Had se snaží pokousat")
            return False


        if x < 0 or x > sirka or y < 0 or y > vyska:
            print("Had se snaží utéct z pole")
            return False

        if novaSourednice in ovoce:  # had jí ovoce
            souradnice.append(novaSourednice)
            ovoce.remove(novaSourednice) #vymazání ovoce z pole
            return souradnice

        else:
            souradnice.pop(0)  # posun hada
            souradnice.append(novaSourednice)
            pocitadloOvoce += 1
            return souradnice


souradnice  = [(0, 0), (1, 0), (2, 0)]
ovoce = [(2,3)]
pocitadloOvoce = 0
vyska = 0
sirka = 0

while vyska < 4 and sirka < 4:
    sirka=int(input("Jak má být široké pole? Zadej minimálně 4."))
    vyska=int(input("Jak má být vysoké pole? Zadej minimálně 4."))
pole(souradnice)

while True:
    pocitadloOvoce += 1
    if len(ovoce) == 0 or pocitadloOvoce%30 == 0:   #vytvoření ovoce, když v poli žádné jiné není.
        noveOvoce = (randrange(0,sirka),(randrange(0,vyska)))
        ovoce.append(noveOvoce)

    smer = input("Kudy se má had vydat? Zvol s pro sever, j pro jih, v pro východ a z pro západ.")
    while True:
        if smer in ["s","j","v","z"]:
            break
        else:
            smer = input("Zadaljsi špatný směr. Zvol s pro sever, j pro jih, v pro východ a z pro západ. ")
            True


    print("Počet odehraných kol: ",pocitadloOvoce)



    pole(posun(souradnice,smer, ovoce,vyska,sirka))
