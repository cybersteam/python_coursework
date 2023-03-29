import mod_1, mod_2, time

print("three mods have been imported")
#calls a function from a module
mod_1.a_function()

#calls a function from another module
mod_2.a_nother_function()
time.sleep(1)

#using a class from a module
my_dog = mod_1.Dog()
my_dog.bark()
my_dog.dog_spawn_window()
print("this should have worked!")
