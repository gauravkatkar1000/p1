'''a=6
b=9
cnt=0
while(1):
         print(a,b)
         if a==1 or b ==1:
                  cnt=cnt+max(a,b)
                  break
         a,b=max(a,b),min(a,b)
         a=a-b
         
         if a==b:
                  cnt=cnt+2
                  break
         cnt=cnt+1
print(cnt)



l1=int(input())
l2=int(input())
b1=int(input())
b2=int(input())
cnt=0
for i in range(l1,l2+1):
         for j in range(b1,b2+1):
                  a=i
                  b=j
                  while(1):
                           if a==1 or b ==1:
                                    cnt=cnt+max(a,b)
                                    break
                           a,b=max(a,b),min(a,b)
                           if a%b==0:
                                    cnt=cnt+a//b
                                    break
                           a=a-b
                           if a==b:
                                    cnt=cnt+2
                                    break
                           cnt=cnt+1
print(str(cnt),end="")'''





l1=int(input())
l2=int(input())
b1=int(input())
b2=int(input())
cnt=0
for i in range(l1,l2+1):
         for j in range(b1,b2+1):
                  a=max(i,j)
                  b=min(i,j)
                  while(a!=b):
                           cnt=cnt+1
                           x=i-j
                           y
                           
print(str(cnt),end="")
                  

