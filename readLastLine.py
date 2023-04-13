n = int(input("Enter N for last n lines : "))
file = open("random.txt","r")

for i in (file.readlines() [-n:]):
    print(i,end="")
