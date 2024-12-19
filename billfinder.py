#if at first 100 unit no bill 100 to 200 5 rs per unit 200 to 300 8 ruppee
unit=int(input("Enter the unit yoh have used: "))
if unit<100:
    print("No bill")
elif 100<unit<200:
    bill = (unit - 100)*5
    print("Your bill is:",bill)
elif 200<unit<300:
    bill = 500 + (unit - 200)*8
    print("Your bill is,.2f:",bill )