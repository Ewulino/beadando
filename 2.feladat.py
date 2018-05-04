
n=input('adj meg egy számot: ')
b1=int(input('add meg a szám számrendszerét: '))
b2 =int(input('adj meg egy másik számrendszert,amibe konvertálni szeretnéd: '))
def tizesbe(n,b1):
    ossz=0
    n=n[::-1]
    for i in range(0,len(n)):
        ujsz=int(n[i])*(b1**i)
        ossz+=ujsz
    return ossz
print(tizesbe(n,b1))
