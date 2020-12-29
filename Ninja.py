for z in range(int(input())):
         ans=""
         n=int(input())
         a=0
         l=[]
         add=[]
         for j in range(int(n)):
                  l.append(int(input()))
         add.append(l[0])
         for i in range(1,n+1):
                  for j in range(1,i+2):
                           if(i%j==0):
                                    a=a+add[j-1]
                                    break
                  print(a,end=" ")
                  add.append(a)
                  a=0
         print()
                  

