L = [int(x) for x in input("Enter multiple values\n").split(',')]
sum2=0;
sum1=""
flag=0
i5=L.index(5)
i8=L.index(8)
for i in range(len(L)):
         if i>=i5 and i<=i8:
                  sum1=sum1+str(L[i])
         else:
                  sum2=sum2+L[i]
print(int(sum1)+sum2)
         
        

