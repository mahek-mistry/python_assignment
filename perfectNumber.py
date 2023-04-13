def checkNum(n):
    sum=0
    for i in range(1,n):        #loop till 1 to number
        if n % i == 0:              # check if divided by any number
            sum=sum+i           # if yes then store in sum variable
    return sum == n


n = int(input("Enter Number : "))
if checkNum(n) == True:
    print(n," is Perfect Number")
else:
    print(n," is not Perfect Number")
