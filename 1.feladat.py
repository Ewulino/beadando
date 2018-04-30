def fibo():
    ls = [0, 1]
    while len(ls)!=100:
        a=ls[-1]+ls[-2]
        ls.append(a)
    return ls
print(fibo())