f = open("listfile.txt","r")

line=0
print("File Content : ")
for i in f.readlines():
    line=line+1
    print(i,end="")

print("\nTotal Lines :",line)
f.close()
