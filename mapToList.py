key=[1,2,3,4,5]
val=["mahek","manya","jay","hetakshi","harsh"]

dic={}

for i in key:
    for j in val:
        dic[i]=j
        val.remove(j)
        break
print(dic)
