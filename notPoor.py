s = input("Enter String : ").lower()

#print("Original String is :",s)

a = s.find("not")

b = s.find("poor")

#print(a)
#print(b)

if b > a:
    print("Result : ",s.replace(s[a:(b+4)],"good"))
