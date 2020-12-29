def rotate(strg):
    return strg[1:] + strg[:1]


n =input()
str1=input()
str2=input()
n=int(n)
n1=len(str1)
for i in range(n*n):
    if(len(str1)==0):
        break
    elif str1[0]==str2[0]:
        str2=str2[1:]
        str1=str1[1:]
        n=n-1
    else:
        str2=rotate(str2)

print(n)
