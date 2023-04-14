tuple=(10,20,30,40,50)

print(tuple)
print(10 in tuple)
print(20 in tuple)
print(22 in tuple)

n=int(input("enter an element to check :"))

for i in tuple:
    if i==n:
        print(n,"is avalible in tuple")
        break
    else:
        print(n,"is not avalible in taple")
