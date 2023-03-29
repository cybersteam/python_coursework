## future ideas:

### add comments to understand everything again fully
### fix for answers that are floats...!

## choose how many questions you want
## add timer so that fastest time has a score
## add the two scores together for a grand score --- only correct answers count
## add a leaderboard database with other players names

import random

MIN_NUMBER = 1
MAX_NUMBER = 18
NB_QUESTIONS = 4

print(f"There are {NB_QUESTIONS} questions, see how many you can get correct!")
print()

def ask_question():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    o = random.randint(0,3)
    
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    elif o == 2:
        operator_str = "/"
    elif o == 3:
        operator_str = "-"
    
    answer = input(f"What is {a} {operator_str} {b} = ")
    compute = a+b

    if o == 1:
        compute = a*b
    elif o == 2:
        compute = a/b
    elif o == 3:
        compute = a-b

    if int(answer) == compute:
        return True
    return False

nb_points = 0
for x in range(NB_QUESTIONS):
    print(f"Question {x+1}:")
    print()
    if ask_question():
        print(f"yes thats right")
        nb_points += 1
    else:
        print (f"no thats wrong")
    print()    

print(f"your score is {nb_points} out of {NB_QUESTIONS}")
average = int(NB_QUESTIONS/2)
if nb_points == NB_QUESTIONS:
    print(f"You got {nb_points} out of {NB_QUESTIONS}, Excellent! - You're a genius!! :)")
    print()
    print()
elif nb_points == 0:
    print(f"You need to improve your maths")
elif nb_points > average:
    print("Good!")
else:
    print("You can do better.")



