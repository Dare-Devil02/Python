n=int(input("Enter the no. till which you want the sum and avg: "))
i=0
s=0
while i<=n:
    s+=i
    i+=1
avg = s / n
print("The sum of first n natural number is: " ,s)
print("The avg of first n natural nio. is: ",avg )