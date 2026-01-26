s=[1,2,3,4,5,6,7]
i=0
j=len(s)-1
while i<j:
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    i+=1
    j-=1
print(s)