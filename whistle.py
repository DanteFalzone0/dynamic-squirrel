#!/usr/bin/env python

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

# This is the Whistle dictionary.

import os
import sys


def play(freq, time):
    os.system('play -n synth %s sin %s' % (time / 1000, freq))


def hither():
    play(550, 200)
    play(900, 350)
    play(750, 500)
    prompt()


def where_you():
    play(750, 190)
    play(600, 150)
    play(1100, 100)
    prompt()


def am_here():
    play(800, 400)
    play(650, 600)
    prompt()


def leave():
    play(750, 150)
    play(580, 90)
    play(580, 90)
    play(665, 150)
    play(580, 150)
    prompt()


def prompt():
    print("From the options below, press the number for the dictionary entry and press ENTER.")
    print('1 - "come here"')
    print('2 - "where are you?"')
    print('3 - "I\'m here"')
    print('4 - "it\'s time to leave"')
    print('5 - exit')
    choice = input("Selection: ")
    if choice == "1":
        hither()
    if choice == "2":
        where_you()
    if choice == "3":
        am_here()
    if choice == "4":
        leave()
    if choice == "5":
        print("Exiting.")
        sys.exit()
    else:
        print("Error - please try again.")
        prompt()


prompt()
