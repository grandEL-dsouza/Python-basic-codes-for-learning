try:
    a = float(input("Enter the first number"))
    b = float(input("Enter the second number"))
    c = a+b
    print(c,"This is the result of addition" )
    d = a-b
    print(d, "This is the result of subtraction" )
    e = a*b
    print(e ,"This is the result of multiplication" )
    f = a/b
    print(f, "This is the result of division (first number divided with the second)" )
    g = a//b
    h = a%b
    print(h, "This is the result of mod (remainder after divison)" )
    i = a**b
    print(i, "This is the result of the first number raised to the power of the second number" )
except:
    print("Non interger")
