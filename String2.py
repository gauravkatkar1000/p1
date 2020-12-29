str="hii how are you why are you work on you hii are hoi are"
words=[]
str1=""
for i in str:
    if(i!=" "):
        str1=str1+i
    else:
        words.append(str1)
        str1=""
#words=str.split(" ")
cnt=[]
ix=0
for i in words:
    c=0
    for j in words:
        if(i==j):
            c=c+1
    cnt.insert(ix,c)
    ix=ix+1
for i in range(1,len(words)):
    #print(words[i] +str(cnt[i]))
    print(f'{words[i]}\t{cnt[i]}')
print("******************")
#sorting
for i in range(0,len(words)):
    for j in range(i,len(words)):
        if(cnt[i]>cnt[j]):
            temp=cnt[i]
            cnt[i]=cnt[j]
            cnt[j]=temp
            temp=words[i]
            words[i]=words[j]
            words[j]=temp
for i in range(0,len(words)):
    if words[i]==words[i-1]:
        print(f'{words[i]}\t{cnt[i]}')
  
