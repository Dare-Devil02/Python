a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
D=(b*b)-(4*a*c)
deno=2*a
if D>0:
    print("Real Roots")
    root1=(-b+D**0.5)/deno
    root2 =(-b+D ** 0.5)/deno
    print("ROOT1: ",root1, "ROOT2: ",root2)
elif D==0:
    print("EQUAL ROOTS")
    roots= -b/deno
    print("Roots are:",roots)
else:
    print("Imaginary roots")