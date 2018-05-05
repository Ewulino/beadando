n=input('adj meg egy számot: ')
b1=int(input('adj meg a szám számrendszerét: '))
b2 = int(input('adj meg egy másik számrendszert,amibe konvertálni szeretnéd: '))
def tizesbe(n,b1):
    ossz=0
    n=n[::-1]
    for i in range(0,len(n)):
        ujsz=int(n[i])*(b1**i)
        ossz+=ujsz
    return ossz
print(tizesbe(sz,b1))
sz=tizesbe(n,b1)
def convert(sz,b2):
        new=[]
        while sz!=0:
            maradek=sz%b2
            new.append(maradek)
            sz=sz//b2
        for i in range(len(new)-1,-1,-1):
            print(new[i],end='')
convert(sz,b2)
