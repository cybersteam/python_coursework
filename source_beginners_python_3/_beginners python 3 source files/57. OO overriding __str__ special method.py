# inheritance

# Python conventions:
# 1. Class names should normally use the CapWords convention.
# 2. Function names should be lowercase, with words separated by underscores as necessary to improve readability.
# 3. Always use self for the first argument to instance methods.
# 4. Mutliline comments should use the # symbol for each line. Don't use docstring - I cheated before! 

# creating an object from a class, nerds call it creating an instance.

class AutoMobile:
    '''->Automobile base / parent class'''     

    model_year = "2019"
    
    def start(self):
        print("Automobile is starting ... vroom, vroom!")

    def turn_off(self):
        '''-> shut off auto ...'''
        print("Click, pud, pud ... thud. Vehicle is off.")
        

class Truck(AutoMobile):
    '''-> Truck - a type of automobile. '''

    def __str__(self):
        return "2019 Truck sold by StudioWeb."

    def dumpload(self):
        print("Truck is dumping load")

    # overriding method
    def start(self):
        print("Truck is starting ... puda, puda, vroom!")

    #def turn_off(self):
        #'''-> shut off truck ...'''
        #print("Click, puda, puda ... thud. Truck is off.")

my_truck = Truck()

print(my_truck)




