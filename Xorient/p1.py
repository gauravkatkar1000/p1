list=[]
while(1):
         a=int(input())
         if(a<0):
                  break
         else:
                  list.append(a)
no=0
l=[]
for i in range(len(list)):
         if(list[i]%2!=0):
                  l.append(no)
                  no=0
                  pass
         else:
                  no=no+1
l.append(no)
ans=0
for i in l:
         if i>=3:
                  ans=ans+1
print(ans)
         

