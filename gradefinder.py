maths=int(input("Enter the marks obtained in maths: "))
english=int(input("Enter the marks obtained in english: "))
Sst=int(input("Enter the marks obtained in S.St: "))
hindi=int(input("Enter the marks obtained in hindi: "))
science=int(input("Enter the marks obtained in science: "))
avg=(maths+english+Sst+hindi+science)/5
if avg>90:
    print("Grade A")
elif 90>avg>80:
    print("Grade B")
elif 80>avg>60:
    print("Grade C")
else:
    print("grade C")