try:
    a = int(input("Enter a number"))
    b=0
    if a==0 or a==1:
        print("Neither prime nor composite")
    elif a==2:
        print("2 is the one even prime number")
    else:
     for i in range (2, a//2):
        c=a%i
        if c==0:
            b=b+1
            print ("Number is not prime")
            break;
            i=i+1
    if b==0:
        print ("number is prime")
except:
    print("Non interger")