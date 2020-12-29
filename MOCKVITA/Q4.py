k=list(int(i) for i in input().split())
k.sort()
l1=[]
l2=[]
p1=max(k)
l1.append(p1)
k.remove(max(k))
p2=max(k)
l2.append(p2)

k.remove(max(k))

for i in range(len(k)-1,-1,-1):
         if p1+k[i]>p2+k[i]:
                  p2=p2+k[i]
                  l1.append(k[i])
         else:
                  p1=p1+k[i]
                  l2.append(k[i])
         
         
print(p1-p2)
