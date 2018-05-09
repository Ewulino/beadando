# első 100 fibonacchi szám listája
def fibo():
    ls = [0, 1]   # fibonacchi számok 0. eleme, 1.eleme
    while len(ls)!=100:
        a=ls[-1]+ls[-2]     # megelőző 2 szám összegéből jön létre
        ls.append(a)
    return ls
print(fibo())
