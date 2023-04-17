f=open("python.txt","r")
wd=0

for i in f.read().split():
    wd=wd+1
    print(i,end=" ")

print("\ntotal words:",wd)
f.close()
