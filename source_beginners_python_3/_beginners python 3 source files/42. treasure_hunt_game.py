#Python Treasure Hunt Game

import random, time


def display_game_intro():
    print('''
             ----> Welcome to the 'Python Treasure Hunt Game'
             ... the most amazing game ever made!

             After a long journey, you find yourself in front of two caves.
             One cave leads to a treasure, the other, a spike filled pit!
             Being brave, and a little greedy for treasure, you've
             decided to go for it!

        ''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave do you want to enter? (1 or 2)')
        cave = input()
    return cave


def enter_cave():
    pass
      

def main_loop():
    display_game_intro()
    whatdidenter = choose_cave()
    print("What cave did I choose: " + whatdidenter)


main_loop()
