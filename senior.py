"""
Copyright (C) 2019 Dante Falzone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random as r  # Probably won't touch this again, it turns into spaghetti very easily

gpa = [3]
health = [15]
money = [100]
guilt = [2]
depression = [2]
stress = [1]
time = [4, 00]

if time[1] >= 60:
    time[1] = 00 + (time[1] - 60)
    time[0] = time[0] + 1


foodnum = r.randint(0, 2)
if foodnum == 0:
    food = "oatmeal"
if foodnum == 1:
    food = "eggs"
if foodnum == 2:
    food = "potatoes"

print("Your name is Dante James Falzone. The year is 2019, the place is Omaha, Nebraska. Your goal"
      " is to keep your GPA, health, and money up, and your guilt, depression, and stress down.")


def print_stats():
    print("-" * 32)
    print("GPA: " + str(float(gpa[0])))
    print("Health: " + str(health[0]))
    print("Money: $" + str(float(money[0])))
    print("Guilt: " + str(guilt[0]))
    print("Depression: " + str(depression[0]))
    print("Stress: " + str(stress[0]))
    print("Time: " + str(time[0]) + ":" + str(time[1]))


def begin():  # Start your day
    print_stats()
    print("It's your first day of school. Your alarm clock goes off at 4:00 AM. You're very tired, and dehydrated.")
    print("Tired though you are, you really want to get a glass of water.")
    print("Type the number corresponding to what you want to do and press ENTER.")
    print("0 - get a glass of water")
    print("1 - go back to sleep until 5:00")
    choice = input()
    if choice == "0":
        contingency0()
    if choice == "1":
        contingency1()
    if choice != "1" and choice != "0":
        print("Error - unable to parse input")
        begin()
        
        
def contingency1():
    print_stats()  # Choose what to do at 5:00 AM if you didn't get any water
    health[0] = 15
    guilt[0] = 3
    depression[0] = 3
    stress[0] = 3
    time[0] = 5
    print("At 5:00, your alarm goes off once more. You find yourself very thirsty, and very bleary-eyed. You really"
          " don't feel like doing anything today.")
    print("After getting a glass of water, you find that you couldn't go back to sleep if you wanted to.")
    print("There's a single warm serving of " + food +
          " on the stove. Downstairs is your computer, and you remember a cool dream you had about coding that makes"
          " you want to write some code. Your dog, Orson, appears before you, wagging his tail and looking eager for"
          " whatever you decide to do. It occurs to you that there was an important assignment due today, but you don't"
          " remember what it was, and you don't particularly care.")
    print("Type the number corresponding to what you want to do and press ENTER.")
    print("0 - get a cup of coffee")
    print("1 - have some " + food)
    print("2 - have some raisin bran")
    print("3 - write some code on the computer")
    print("4 - walk Orson")
    print("5 - play with Orson")
    print("6 - give Orson a treat")
    print("7 - try to remember what today's Important Assignment was")
    choice = input()
    if choice == "0":
        contingency10()
    if choice == "1":
        contingency11()
    if choice == "2":
        contingency12()
    if choice == "3":
        contingency13()
    if choice == "4":
        contingency14()
    if choice == "5":
        contingency15()
    if choice == "6":
        contingency16()
    if choice == "7":
        contingency17()


def contingency10():
    print_stats()


def contingency11():
    print_stats()


def contingency12():
    print_stats()


def contingency13():
    print_stats()


def contingency14():
    print_stats()


def contingency15():
    print_stats()


def contingency16():
    print("Orson wags his tail and wolfs down the treat in less than fifteen seconds. You tell him what a good boi he"
          " is.")
    contingency1()


def contingency17():
    print_stats()
    chance = r.randint(0, 1)
    if chance == 0:
        print("After some thinking and digging through your stuff, you remember what the assignment was."
              " Pondering the enormity of the task that you have utterly failed"
              " to put forth even the minimum effort on with no excuse, you mind races with stressful thoughts and you"
              " must find something else to do to calm yourself down.")
        print("Type the number corresponding to what you want to do and press ENTER.")
        print("0 - hit something")
        print("1 - rationalize")
        print("2 - read something")
        choice = input()
        print(choice + "I haven't programmed that path yet")  # TODO: code contingencies 1/7/{0-2}
    if chance == 1:
        qualifiernum = r.randint(0, 2)
        if qualifiernum == 0:
            qualifier = "summative"
        if qualifiernum == 1:
            qualifier = "double-weighted summative"
        if qualifiernum == 2:
            qualifier = "quadruple-weighted summative"
        print("After much thinking and searching through your stuff, you still have no clue what the assignment was, "
              "though your brain helpfully reminds you that it was a " + qualifier + " grade. Considering your newfound"
              " chances of getting an IB diploma and keeping your GPA high enough to not lose the Regents scholarship,"
              " your mind races with stressful thoughts and you must find something to calm yourself down.")
        print("Type the number corresponding to what you want to do and press ENTER.")
        print("0 - hit something")
        print("1 - rationalize")
        print("2 - read something")
        choice = input()
        print(choice + "I haven't programmed that path yet")  # TODO: code contingencies 1/7/{0-2}


def contingency0():  # If, upon your first alarm, you get a glass of water
    print_stats()
    print("You no longer feel dehydrated. Your parents are both up, the lights are on, and they're making noise"
          " as a result of their morning exercise routine. Do you want to stay up or try to go back to sleep?")
    print("Type the number corresponding to what you want to do and press ENTER.")
    print("0 - stay up")
    print("1 - go back to sleep until 5:00")
    choice = input()
    if choice == "0":
        contingency00()
    if choice == "1":
        contingency01()
    if choice != "1" and choice != "0":
        print("Error - unable to parse input")
        contingency0()


def contingency00():  # Choose what to do at 4:00 AM
    print_stats()
    print("You smell coffee. Your parents are exercising in the living room. There's several servings of " + food +
          " on the stove. Downstairs is your computer, and you remember a cool dream you had about coding that makes"
          " you want to write some code. Your dog, Orson, appears before you, wagging his tail and looking eager for"
          " whatever you decide to do. It occurs to you that there was an important assignment due today, but you don't"
          " remember what it was, and you don't particularly care.")
    print("Type the number corresponding to what you want to do and press ENTER.")
    print("0 - get a cup of coffee")
    print("1 - have some " + food)
    print("2 - have some raisin bran")
    print("3 - write some code on the computer")
    print("4 - walk Orson")
    print("5 - play with Orson")
    print("6 - give Orson a treat")
    print("7 - try to remember what today's Important Assignment was")
    choice = input()
    if choice == "0":
        contingency000()
    if choice == "1":
        contingency001()
    if choice == "2":
        contingency002()
    if choice == "3":
        contingency003()
    if choice == "4":
        contingency004()
    if choice == "5":
        contingency005()
    if choice == "6":
        contingency006()
    if choice == "7":
        contingency007()


def contingency000():
    print_stats()


def contingency001():
    print_stats()


def contingency002():
    print_stats()


def contingency003():
    print_stats()


def contingency004():
    print_stats()


def contingency005():
    print_stats()


def contingency006():
    print("Orson wags his tail and wolfs down the treat in less than fifteen seconds. You tell him what a good boi he"
          " is.")
    contingency00()


def contingency007():
    print_stats()
    chance = r.randint(0, 1)
    if chance == 0:
        print("After some thinking and digging through your stuff, you remember what the assignment was."
              " Pondering the enormity of the task that you have utterly failed"
              " to put forth even the minimum effort on with no excuse, you mind races with stressful thoughts and you"
              " must find something else to do to calm yourself down.")
        print("Type the number corresponding to what you want to do and press ENTER.")
        print("0 - hit something")
        print("1 - rationalize")
        print("2 - read something")
        choice = input()
        print(choice + "I haven't programmed that path yet")  # TODO: code contingencies 0/0/7/{0-2}
    if chance == 1:
        qualifiernum = r.randint(0, 2)
        if qualifiernum == 0:
            qualifier = "summative"
        if qualifiernum == 1:
            qualifier = "double-weighted summative"
        if qualifiernum == 2:
            qualifier = "quadruple-weighted summative"
        print("After much thinking and searching through your stuff, you still have no clue what the assignment was, "
              "though your brain helpfully reminds you that it was a " + qualifier + " grade. Considering your newfound"
              " chances of getting an IB diploma and keeping your GPA high enough to not lose the Regents scholarship,"
              " your mind races with stressful thoughts and you must find something to calm yourself down.")
        print("Type the number corresponding to what you want to do and press ENTER.")
        print("0 - hit something")
        print("1 - rationalize")
        print("2 - read something")
        choice = input()
        print(choice + "I haven't programmed that path yet")  # TODO: code contingencies 0/0/7/{0-2}


def contingency01():
    print_stats()
    print("Your alarm goes off at 5:00 AM, but you're still tired. Do you stay up, or go back to bed until 5:30?")
    print("Type the number corresponding to what you want to do and press ENTER.")
    print("0 - stay up")
    print("1 - go back to sleep until 5:30")
    choice = input()
    if choice == "0":
        contingency010()
    if choice == "1":
        contingency011()
    if choice != "1" and choice != "0":
        print("Error - unable to parse input")
        contingency01()


def contingency010():
    print_stats()


def contingency011():
    print_stats()


begin()
