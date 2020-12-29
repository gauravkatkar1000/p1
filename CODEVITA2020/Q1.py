n=int(input())
l1=input()
l2=input()
l3=input()
i=0

while (i<len(l1)-1):
         flag=0
         if(l1[i]==l2[i]==l3[i]=="#"):
             print("#",end="")
             
         if(i+4<len(l1)):
                  if(l2[i]==l2[i+4]==l2[i+2]==l1[i+4]==l1[i]==l1[i+2]==l3[i]==l3[i+4]==l3[i+2]=="*"):
                           print("E",end="")
                           flag=1
                  elif(l1[i+2]==l2[i]==l2[i+2]==l2[i+4]==l3[i]==l3[i+4]=="*"):
                           flag=1
                           print("A",end="")
                  elif(l1[i]==l1[i+2]==l1[i+4]==l2[i+2]==l3[i]==l3[i+2]==l3[i+4]=="*"):
                           flag=1
                           print("I",end="")
                  elif(l1[i]==l1[i+2]==l1[i+4]==l2[i]==l2[i+4]==l3[i]==l3[i+2]==l3[i+4]=="*"):
                           flag=1
                           print("O",end="")
                  elif(l1[i]==l1[i+4]==l2[i]==l2[i+4]==l3[i]==l3[i+2]==l3[i+4]=="*"):
                           flag=1
                           print("U",end="")
                  
                  
                  
         i=i+6
         if flag==0:
                  i=i-4
