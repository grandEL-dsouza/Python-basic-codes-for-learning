try:
    unique_elements = [] # defined a blank array to be used later in code
    a = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    #a = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3] sample data set its for data sets like this we need another array
    #a = [2321,123,4,5,6,7,3,2,2,4,6,7,] #sample data set
    #a.sort() #you can use direct sort function provided by Python if this is not allowed in your test center then use the following bubble sort method
#bubble sort starts
    for i in range (len(a)):
        for j in range (len(a)-1):
            if a[j]>a[i]:
                c=a[j]
                a[j]=a[i]
                a[i]=c
#bubble sort ends 
#we now start appending unqiue elements into the array these will be in sorted order only  
    for i in range (len(a)):
            if a[i] not in unique_elements:
                unique_elements.append(a[i])
#print ("sorted", a)            # print if you want to validate
#print ("unique", unique_elements)  # print if you want to validate
#print ("lenght" , len(unique_elements))  # print if you want to validate
    print ("largest element is", unique_elements[(len(unique_elements)-1)])  
    print ("second largest element is", unique_elements[(len(unique_elements)-2)])  
except:
    print("invalid data only enter integers")
