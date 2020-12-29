l=[]
while(1):
         a=int(input())
         if(a<0):
                  break
         else:
                  l.append(a)
l.sort()
check=0
for i in range(len(l)):
         if(l[i]>100):
                  print(l[i-1])
                  check=1
                  break
if check==0:
         if l[len(l)-1]>100:
                  print(check)
         else:
                  print(l[len(l)-1])
