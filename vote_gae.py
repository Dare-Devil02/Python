age=int(input("Enter the age: "))
if age>=18:
    print("You are eligible to vote")
else:
    yrs=18-age
    print("you have to wait",yrs , "years to cast your vote")
