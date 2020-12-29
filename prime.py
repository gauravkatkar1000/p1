'''for i in range(2,101):
    n=0
    for j in range(2,i//2):
        if(i%j==0):
            n=1
            break
    if n==0:
        print(i)

'''
import sympy as s
a=int(input())
if s.isprime(a):
    print("YES")
