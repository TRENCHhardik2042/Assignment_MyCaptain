#making of a calculator with other operators
print("Give the two values for calculation")

a = int(input())
b = int(input())

## value is being taken and stored
while True:

    print ("\n1. ADD \n2. SUBTRACT \n3. MULTIPLICATION\n4. DIVISION \n5. QUIT\n------------ PICK THE NUMBER AND EXECUTE THE OPERATION ACCORDINGLY -----------------")

    x= float(input())
## decision of addition or subtraction


## Running the if else condition for addition or subtraction
    if x == 1 : 
        result = a + b
        print (result)
    elif x == 2 :
        result = a - b
        print (result)
    elif x == 3:
        result = a * b 
        print (result)
    elif x == 4 :
        result = a / b 
        print (result)
    elif x == 5 :
        break

