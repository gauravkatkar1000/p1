def isPrime(i):
         pn=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
         if i in pn:
                  return True
         else:
                  return False
n = int(input())
l=[]
for i in range(2,n+2):
         l.append(i)
z=[]
k=0

a=[]
for i in range(len(l)):
         for j in range(i,len(l)):
                  if isPrime(l[i]):
                           if (l[j]%l[i]==0):
                                    a.append(l[j])
         if len(a)>0:
                  z.append(a)
         a=[]
last=len(z)
print(z)
for i in range(len(z)):
         a=z[i]
         for j in range(len(a)):
                  b=a[j]
                  for k in range(i+1,len(z)):
                           c=z[k]
                           if b in c and 9999 not in c:
                                    last=last-1
                                    z[k].append(9999)
                                    break
print(last)
                                    
                  
         
         
         
