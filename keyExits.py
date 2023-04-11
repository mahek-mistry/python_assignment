d1={"A":10,"B":20,"C":30,"D":40,"E":50}

print("disctionary:",d1)
n=input("enter key to check : ")

for i in d1:
    if i==n:
        print("key already exists")
else:
    print("key not found")
