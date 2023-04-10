file = open("example.txt","a")

file.write("This is Appended Text\n")
file.write("my name is mahek.....\n")
file.close()

file=open("example.txt","r")
print(file.read())
file.close()
