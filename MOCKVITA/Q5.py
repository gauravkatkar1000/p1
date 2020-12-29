def replace(l1,al):
         l2=[0 for x in range(len(l1))]
         for i in range(len(l1)):
                  l2.insert(l1[i]-1,al[i])
                  l2.remove(0)
         return (l2)
         
                  

l1=[3,6,5,4,1,2]
ab=6
al=[chr(x) for x in range(ord('a'),ord('a')+ab)]
z=replace(l1,al)
cnt=0
while(z!=al):
         cnt=cnt+1
         z=replace(l1,z)
print(cnt+1)
         

                  









       
