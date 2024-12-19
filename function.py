def pos_neg(a,b):
    
    if a<0 and b<0 and parameter=="true":
        print("true")
    elif a>0 and b<0 and parameter=="false":
        print("true")
    elif a<0 and b>0 and parameter=="false":
        print("true")
    else:
        print("false")
    return a,b
parameter=input("enter true or false:")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
pos_neg(a,b)