m,n=input().split()
m,n=int(m),int(n)
l=[]
st=""
for i in range(m):
    l.append(input())
for i in range(n):
    for j in l:
        st=st+j[i]
flag=0
ans=""
st1=""
i=0
while(i<len(st)):
    while (st[i].isalnum()):
        ans=ans+st[i]
        i=i+1
        if (i>=len(st)):
            break
    if (i>=len(st)):
            break
    while (not(st[i].isalnum())):
        st1=st1+st[i]
        i=i+1
        if (i>=len(st)):
            break
        
    if(i>=len(st)-1):
    
        ans=ans+st1
    else:
        ans=ans+" "
    
        st1=""
print(ans)

    
    
    


   
