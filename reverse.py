def rev_string(str1):

    if len(str1) % 5 == 0:
        return print(" ".join(reversed(str1)))
    else:
        print("Invalid length ..!")

s = input("Enter a String : ")
rev_string(s)
