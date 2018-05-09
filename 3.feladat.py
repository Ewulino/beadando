#  1-9 ig +,- vagy semmit a számjegyek közé téve az összeg 100

def csatolas(fej,elem):   # fej beszurása minden elem elé
    result=[]
    if len(elem)==0:
        return fej
    for t in elem:
        result.append([fej]+t)  #  ha t benne van elemben akkor fejet hozzáfűzi t-hez(+)
    return result
# print(csatolas(1,[[2,3],[4,5]])) pl: [[1,2,3],[1,4,5]]
# print(csatolas(1,[]))

def randomvalues(ertek):  # random értékek +,- előjellel
    if len(ertek)==0:
        return [[]]
    else:
        resz = randomvalues(ertek[1:])
        #  ertek[0] egyenlő a fejjel és ehhez csatolja hozzá az ertek 1.indexétől a többit(resz), majd ugyanezt megismétli - előjellel és visszaadja az összes lehetséges esetet
        return csatolas(ertek[0], resz) + csatolas(-ertek[0], resz)
# print(randomvalues(range(1,4))) pl:[[1, 2, 3], [1, 2, -3], [1, -2, 3], [1, -2, -3], [-1, 2, 3], [-1, 2, -3], [-1, -2, 3], [-1, -2, -3]]
# print(randomvalues([1])) pl:[[1],[-1]]

def get_ones_zeros(size): # 0,1-ből álló értékeket állít elő
    if size==0:
        return [[]]
    else:
        resz = get_ones_zeros(size - 1) # csökkentjük size -1-el mert 0.elem adott
        # 0-hoz hozzá csatolja a maradek helyet és kitölti majd ezt megteszi 1-el is és visszaadja az összes lehetséges esetet
        return csatolas(0, resz) + csatolas(1, resz)
# print(get_ones_zeros(1)) pl: [[0],[1]]
# print(get_ones_zeros(3)) pl: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

def nothing(ertek,one_zero):  # összevonja a számokat és 2vagy többszámjegyűt hoz létre 1-9iig
    idx_i = 0 # ertek indexei
    idx_j = 0  # one_zero indexei
    size = len(ertek)
    result = []
    kezdoertek = ertek[0]
    while idx_i < size:   # ameddig ertek indexe kisebb mint az ertek hossza
        if idx_i + 1 >= size:
            result.append(kezdoertek)
            break
        new_value = ertek[idx_i + 1]
        if one_zero[idx_j] == 0:   #  one_zero indexén lévő szám egyenlő nullával
            result.append(kezdoertek)
            kezdoertek= new_value
        else:
            kezdoertek= kezdoertek * 10 + new_value  # ertek[0]*10 és hozzáadja az ertek[1] elemét azaz a következőt
        idx_i += 1
        idx_j += 1
    return result
# print(nothing([1,2,3,4,5,6,7,8,9],[1,0,0,0,0,0,0,0,0])) pl: [12, 3, 4, 5, 6, 7, 8, 9]
# print(nothing([1,2,3,4,5,6,7,8,9],[0,1,1,0,0,1,0,1,0]))  pl:[1, 234, 5, 67, 89]

def get_numbers(stop=9):   # számok halmazát hozza létre
    ertek= range(1, stop + 1)   # 1-9 ig a számok
    one_zeros = get_ones_zeros(stop)  # 0,1-ből álló érétkekek hoz létre 9-es lista mérettel
    result = []
    for one_zero in one_zeros:
        szamhz = nothing(ertek, one_zero)  # szamhz-ban lesz 2jegyű szám is
        result.append(tuple(szamhz))  # eredmeny tuple() alakitása , mert lista nem lehet eleme a halmaznak
    return set(result)  # hz kell, ellenben 2x irja ki a legvégén az eredményt
# print(get_numbers(3)) pl:{(12, 3), (123,), (1, 23), (1, 2, 3)}
# print(get_numbers(9))

def vegso(stop=9,osszeg=100):  # 1-9 lévő számok összes lehetséges kombinációjábol visszaadja  amikor az összeg 100
    numbers = get_numbers(stop)
    for number in numbers:
        variacio = map(lambda y: [number[0]] + y, randomvalues(number[1:]))   # y = számhz 0.eleme (,) +,- értékek generálása és számhz1.elemétől
        for v in variacio:
            SumValue= sum(v)    # ha benne van , összegezzük és ha 100 akkor kiiratjuk
            if osszeg == SumValue:
                print(v,'=',osszeg)
vegso()
