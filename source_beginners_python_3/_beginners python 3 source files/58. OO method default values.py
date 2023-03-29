# inheritance - default values in methods

class AutoMobile:
    '''->Automobile base / parent class'''     
    
    def start(self):
        print("Automobile is starting ... vroom, vroom!")

    def turn_off(self):
        '''-> shut off auto ...'''
        print("Click, pud, pud ... thud. Vehicle is off.")       


class Truck(AutoMobile):
    '''-> Truck - a type of automobile. '''

    def __init__(self, year=None):
        if year is None:
            self.year = 2018
        else:
            self.year = year

    def __str__(self):
        return "2019 Truck sold by StudioWeb."


    def truck_year(self):
         print("This truck was built in:" + str(self.year))


    def dumpload(self, value=None):

        if value is None:
            print("Truck has nothing to dump.")
        else:
            print("Truck is dumping " + str(value))     
            

my_truck = Truck("2021")
my_truck.truck_year()

my_truck.dumpload()
my_truck.dumpload(2000)

#create a new truck, but don't specify the year
another_truck = Truck()
another_truck.truck_year()

print(type(another_truck))





