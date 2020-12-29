a=[2,3,1]
b=[1,2,3]
c=b.copy()
k=0
for i in a:
    e=0
    for j in range(0,len(b)):
        if(i==b[j]):
            e=1
            b[j]=-1
            break
    if(e==0):
        print("not equal")
        k=1;
        break
if(k==0):
    print("equal")
print(a)
print(b)
print(c)

                      
	
