n,k,mp=input().split()
n,k,mp=int(n),int(k),int(mp)
pz=list(float(x) for x in input().split())
pp=list(float(x) for x in input().split())
l=[]
for i in range(len(pp)):
         a=[]
         a.append(pp[i])
         a.append(pz[i])
         l.append(a)
z=[]
for i in range(k):
         z=z+l
z.sort(reverse=True)

cost=0
paisa=0
while(cost<mp):
         k=z.pop(0)
         if(cost+k[0]<mp):
                  cost = cost+k[1]
                  paisa=paisa+k[0]*k[1]/100
print(int(paisa))
         
