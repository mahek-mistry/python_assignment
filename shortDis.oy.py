import operator
dic = {
            "X" : 10,
            "Y" : 30,
            "Z" : 50
            }

print(dic)

dic_sort = dict(sorted(dic.items(),key=operator.itemgetter(1)))
print("Dictionary in ascending order :-",dic_sort)

dic_sort2 = dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order :-",dic_sort2)
