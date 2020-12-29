a=["$500","$21,000","1200"]
final=[]

for i in a:
    str=""
    for k in range(0,len(i)):
        if i[k]!='$' and i[k]!=',':
            str+=i[k]
#    print(str)
    final.append(str)
a=final.copy()
print(a)


            
        
        
