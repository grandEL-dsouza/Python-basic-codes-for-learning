#probelm statement check if a vowel is present in a user entered string

a=input("enter the string")
b=0
for i in range (0, len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        b=b+1
        print ("vowel is present")
        i=i+1
if b==0:
    print("the string has no vowels")
