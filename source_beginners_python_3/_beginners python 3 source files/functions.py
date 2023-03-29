# Comments are for leaving messages.
# Comments are ignored by Python.
# You could even leave code comments: def myFunction:

#price = 45.6
#print(price)

def functionOne():
    print("My name is jimmy!")

    
# understanding: input, int vs str and type conversion.
def functionTwo():
    value = input("Please give me a number: ")
    value2 = input("Please give me another number: ")
    calculated_value = str(int(value) * int(value2))
    print("The answer is: " + calculated_value)

functionTwo()
