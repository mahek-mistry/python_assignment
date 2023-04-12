from collections import Counter

l = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}]

result = Counter()

for i in l:
    result[i['item']] += i['amount']

print(result)

'''
res = {}
for i in l:
    for a,b in i.items():
        res[a] = res.get(a,[]) 
        res[b] = res.get(b,[])
    
print(res)
'''
