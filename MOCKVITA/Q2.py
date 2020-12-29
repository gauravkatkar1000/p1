n=int(input())
st1=input().split(" ")
st2=[]
a=0
count=0

for i in range(len(st1)):
    st1[i] = ((((int(max(st1[i])) * 11) + (int(min(st1[i])) * 7)) % 100) // 10)
for i in range(len(st1)):
    count=0
    start=i%2
    if st1[i] not in st2:
        for j in range(start,n,2):
            if st1[i]==st1[j]:
                count=count+1
        
        if count>1:
            if st1[i] not in st2:
                if count==2:
                    a=a+1
                if count>2:
                    a=a+2
            st2.append(st1[i])
           

print(a,end="")
