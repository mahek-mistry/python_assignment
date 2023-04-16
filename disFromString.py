s = input("Enter String : ")
dic = {}

for i in s:                         #for loop till str end
    if i in dic:                    #check if char availabel in dictionary or not
        dic[i] = dic[i]+1       # if available increment value
    else:   
        dic[i]=1                    # if not then assign value = 1
    
print(dic)
