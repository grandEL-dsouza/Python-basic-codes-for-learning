#try:
P = float(input("Enter the Amount of Loan you want(Principal Amount)"))
R = float(input("Enter the rate of interest Per Annum"))
RP = R/100 #Converting into Percentage
Y = float(input("Enter the Number of years or Tenure"))
N = Y*12 # Converting Years to Months
#EMI = (P*R/12)*[(1+R/12)**N]/[{(1+R/12)**N}-1]  this the formula for EMI
# We would have to break down the formula into smaller componenets because Python throws errors like this --> ""TypeError: can't multiply sequence by non-int of type 'float'
A= P*RP
B= A/12
C= R/12
D= 1+C
E= D**N
G=E-1
H=E/G
EMI=B*H
#EMI = round(EMI) # you can use Round function to Round of the value or convert to int
print(EMI,"This is the EMI per month for the Tensure")
#except:
#    print("Input entered is invalid")
