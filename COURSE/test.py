# if you want to use a global variable inside a function then you need to declare it inside the function:
# mostly you would want your function to be independant of the main program (so you can use it for other things)

def display_person_info(name, age):
    print()
    print ("your name is " + name + " you are " + str(age) + " old")
    print ("you will soon be " + str(age+1) + " old")

    if age == 17:
        print("You are almost an adult! Yay")
    elif age < 18 and age > 10:
        print("you are a teenager")
    elif age == 18:
        print("You are an adult now, Congrats!")
    elif age > 80:
        print("You are a senior.")
    elif age < 10:
        print("You are a kid.")
    elif age >= 18:
        print("you are an adult")
    else:
        print("you are a minor")


def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("what is your name?")
    return name_answer


def ask_for_the_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " what is your age?")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: Age must be a number")
    return age_int


'''
#constant/convention
NB_PERSONS = 3

for i in range(0, NB_PERSONS):
	name = "foo" + str(i+1)
	age = ask_for_the_age(name)
	display_person_info(name, age)
'''


#ask for the name
name1 = ask_for_the_name()
name2 = ask_for_the_name()

#ask for the age
age1 = ask_for_the_age(name1)
age2 = ask_for_the_age(name2)


display_person_info(name1, age1)
display_person_info(name2, age2)
