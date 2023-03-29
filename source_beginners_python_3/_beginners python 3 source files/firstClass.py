print("Our first look at Python classes.")

# creating an empty class. The 'pass' keyword allows you to create empty classes.
class Things:
    pass

#creating a class with empty functions/methods
# functions in classes are called: methods
# creating empty methods as a way to quickly plan out your code
class MoreThings():
    def fall(self):
        pass
    def moreFalling(self):
        pass


class AnObject():
    def class_function(self):
        print("This is a class function")
        
# class methods require the self parameter. No 'self' raises an error
    def anotherFunction():
        print("Calling the second method of the class")


        
# Use IDLE to jump to line number displayed in error message: edit -> go to line (Alt+G) Windows only 
cup = AnObject()
cup.class_function()
#cup.anotherFunction()


