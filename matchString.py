def matchStr(list):      
    count = 0           # count the str to match criteria and store

    for i in list:      # check in list till end of the list
        if len(i)>=2 and i[0]==i[-1]:   
            count = count + 1           # if matched increment count variable 
            print("Length is more then 2 and first and Last Character are same : ",i)
    return count        # if not found str then return 

l1 = ["mahek", "manya","rajr","J","mm","jj"]  # List for check str

print(matchStr(l1))
