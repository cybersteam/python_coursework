import random

def ask_number(nb_min, nb_max):
    #what is the magic number (between 1 and 10)
    user_num_int = 0

    while user_num_int == 0:
        user_num = input(f"what is the magic number??(between {nb_min} and {nb_max}) ")
        try:
            user_num_int = int(user_num)
        except:
            print('invaklid')

        else:
            if user_num_int < nb_min or user_num_int > nb_max:
                print(f'must be in range between {nb_min} and {nb_max}')
                user_num_int = 0
    return user_num_int


MIN_NUM = 1
MAX_NUM = 10
MAGIC_NUMBER = random.randint(MIN_NUM, MAX_NUM)
NB_LIVES = 5

lives = NB_LIVES
number = 0
while not number == MAGIC_NUMBER and lives > 0:
    print(f'you have {lives} lives')
    number = ask_number(MIN_NUM, MAX_NUM)

    if number < MAGIC_NUMBER:
        print("no it's bigger than that, try again!")
        lives -= 1
    elif number > MAGIC_NUMBER:
        print("no it's smaller than that.. try again!")
        lives -= 1
    else:
        print(f"yes, {MAGIC_NUMBER} is correct!")

if lives == 0:
    print('you lost!')
    print(f'the magic number was {MAGIC_NUMBER}!')
