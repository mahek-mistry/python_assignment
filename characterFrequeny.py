n=input("enter the string:")
s={}    #dictionary called
for i in n:
    if i in s:
        s[i]+=1   #letters counted
    else:
        s[i]=1
print(s)
