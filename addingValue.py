

dic1 = {"A":10,"B":150,"C":1000,"A":40}
dic2 = {"A":10,"B":150,"C":1000}

for i in dic1:
    for j in dic2:
        dic1[i]=dic1[i]+dic2[i]
        break
print(dic1)
