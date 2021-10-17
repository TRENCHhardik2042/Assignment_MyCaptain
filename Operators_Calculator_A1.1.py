# Making of calculatior basic one



print("Give the two values for calculation")

a = int(input())
b = int(input())
## value is being taken and stored

print ("1. ADD \n2. SUBTRACT \n------------ PICK THE NUMBER AND EXECUTE THE OPERATION ACCORDINGLY -----------------")

x= int(input())
## decision of addition or subtraction


## Running the if else condition for addition or subtraction
if x == 1 : 
    result = a + b
    print (result)
else:
    result = a - b
    print (result)