a=[]
ix=0
k=0
for i in range(2,100):
    k=0
    for j in range(2 ,i//2):
        if i%j==0:
            k=1
            break
    if(k==0):
        a.insert(ix,i)
        ix=ix+1
print(a)
