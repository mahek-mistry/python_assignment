file = open("list.txt","w")

list1=["mahek","dilipbhai","mistry"]

for i in list1:
    file.write(i + " ")

file.close()

f = open("list.txt","r")
print(f.read())
f.close()
