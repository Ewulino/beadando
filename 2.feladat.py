
n=input('adj meg egy számot: ')
b1=int(input('adj meg a szám számrendszerét: '))
def tizesbe(n,b1):
    ossz=0
    n=n[::-1]
    for i in range(0,len(n)):
        ujsz=int(n[i])*(b1**i)
        ossz+=ujsz
    return ossz
print(tizesbe(n,b1))
