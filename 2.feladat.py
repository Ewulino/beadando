# egyik számrendszerből másik számrendszerbe váltás
n=input('adj meg egy számot: ')
b1=int(input('add meg a szám számrendszerét: '))
b2 = int(input('adj meg egy másik számrendszert,amibe konvertálni szeretnéd: '))

def tizesbe(n,b1):
    ossz=0
    n=n[::-1]    # szám megfordítása
    for i in range(0,len(n)):    # számjegyek bejárása
        ujsz=int(n[i])*(b1**i)    # számjegyek*hatványok és utána a szorzatok összeadása
        ossz+=ujsz
    return ossz
# print(tizesbe(sz,b1))
sz=tizesbe(n,b1)   #  sz egyenlővé tétele ossz-el fv meghívasa által
def convert(sz,b2):
        new=[]
        while sz!=0:   # míg az osztás nem lesz 0 (baloldal)
            maradek=sz%b2   # szám maradékos osztása számrendszerrel
            new.append(maradek)
            sz=sz//b2     # szám egész osztása számrendszerrel ,szám csökken és ezt addig mig nem 0
        for i in range(len(new)-1,-1,-1):   # listában lévő számjegyek visszafelé olvasása
            print(new[i],end='')
convert(sz,b2)
