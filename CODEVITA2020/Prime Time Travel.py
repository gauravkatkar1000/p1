def isPrime(i):
         pn=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]
         if i in pn:
                  return True
         else:
                  return False
d,p=input().split()
d,p=int(d),int(p)
d1=d//p
cnt=0
for i in range(1,d1+1):
         flag=0
         for j in range(i,d+1,d1):
                  if isPrime(j):
                           continue
                  else:
                           flag=1
                           break
         if flag==0:
                  cnt=cnt+1
                  
print(cnt,end="")
