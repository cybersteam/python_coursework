# Object Oriented Python - Video #47

class Car():
    ''' A simple class that describes a car '''

    def __init__(self, model, cost):
        self.model = model
        self.cost = cost 

    def start(self):
        ''' starts the car '''
        print(self.model.title() + " is now starting.")
        #print("Car is now starting.")

'''
myCar = Car("audi", "$98k")
myCar.start()

print("\nCreating new car ... \n")

my2ndCar = Car("ford", "$28k")
my2ndCar.start()

'''
myCar = Car("audi", "$98k")
myCar.start()
