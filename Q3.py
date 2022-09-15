num = int(input(" Please Enter any Maximum Number : "))
 
for number in range(1, num + 1):
    if(number % 2 != 0):
        print("{0}".format(number))

 
num = int(input(" Please Enter the Maximum Number : "))
 
for number in range(1, num+1):
    if(number % 2 == 0):
        print("{0}".format(number))