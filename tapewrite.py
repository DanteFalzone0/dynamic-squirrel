import os
import sys
import time


def write(freq, millisecs):
    os.system('play -n synth %s sin %s' % (millisecs / 1000, freq))


def write_file():
    print("Input the string you wish to write to the tape.")
    letters = input()
    chars = list(letters)
    for x in chars:
        freq_translate(x)
        print("---")
    time = (10 * 90 * len(letters))
    for x in chars:
        print(x)
    print('Total playing time: ' + str(time) + ' milliseconds')


def freq_translate(char):
    if char in [' ']:
        playT(0, 0, 1, 0, 0, 0, 0, 0, 'space')
    if char in ['!']:
        playT(0, 0, 1, 0, 0, 0, 0, 1, 'exclamation mark')
    if char in ['"']:
        playT(0, 0, 1, 0, 0, 0, 1, 0, 'double quote')
    if char in ['#']:
        playT(0, 0, 1, 0, 0, 0, 1, 1, 'hashtag')
    if char in ['$']:
        playT(0, 0, 1, 0, 0, 1, 0, 0, 'dollar sign')
    if char in ['.']:
        playT(0, 0, 1, 0, 1, 1, 1, 0, 'period')
    if char in [',']:
        playT(0, 0, 1, 0, 1, 1, 0, 0, 'comma')
    if char in ['A']:
        playT(0, 1, 0, 0, 0, 0, 0, 1, 'A')
    if char in ['B']:
        playT(0, 1, 0, 0, 0, 0, 1, 0, 'B')
    if char in ['C']:
        playT(0, 1, 0, 0, 0, 0, 1, 1, 'C')
    if char in ['D']:
        playT(0, 1, 0, 0, 0, 1, 0, 0, 'D')
    if char in ['E']:
        playT(0, 1, 0, 0, 0, 1, 0, 1, 'E')
    if char in ['F']:
        playT(0, 1, 0, 0, 0, 1, 1, 0, 'F')
    if char in ['G']:
        playT(0, 1, 0, 0, 0, 1, 1, 1, 'G')
    if char in ['H']:
        playT(0, 1, 0, 0, 1, 0, 0, 0, 'H')
    if char in ['I']:
        playT(0, 1, 0, 0, 1, 0, 0, 1, 'I')
    if char in ['J']:
        playT(0, 1, 0, 0, 1, 0, 1, 0, 'J')
    if char in ['K']:
        playT(0, 1, 0, 0, 1, 0, 1, 1, 'K')
    if char in ['L']:
        playT(0, 1, 0, 0, 1, 1, 0, 0, 'L')
    if char in ['M']:
        playT(0, 1, 0, 0, 1, 1, 0, 1, 'M')
    if char in ['N']:
        playT(0, 1, 0, 0, 1, 1, 1, 0, 'N')
    if char in ['O']:
        playT(0, 1, 0, 0, 1, 1, 1, 1, 'O')
    if char in ['P']:
        playT(0, 1, 0, 1, 0, 0, 0, 0, 'P')
    if char in ['Q']:
        playT(0, 1, 0, 1, 0, 0, 0, 1, 'Q')
    if char in ['R']:
        playT(0, 1, 0, 1, 0, 0, 1, 0, 'R')
    if char in ['S']:
        playT(0, 1, 0, 1, 0, 0, 1, 1, 'S')
    if char in ['T']:
        playT(0, 1, 0, 1, 0, 1, 0, 0, 'T')
    if char in ['U']:
        playT(0, 1, 0, 1, 0, 1, 0, 1, 'U')
    if char in ['V']:
        playT(0, 1, 0, 1, 0, 1, 1, 0, 'V')
    if char in ['W']:
        playT(0, 1, 0, 1, 0, 1, 1, 1, 'W')
    if char in ['X']:
        playT(0, 1, 0, 1, 1, 0, 0, 0, 'X')
    if char in ['Y']:
        playT(0, 1, 0, 1, 1, 0, 0, 1, 'Y')
    if char in ['Z']:
        playT(0, 1, 0, 1, 1, 0, 1, 0, 'Z')
    else:
        """
        playT(0, 0, 1, 0, 0, 0, 0, 0, ' ')  # space
        playT(0, 1, 0, 0, 0, 1, 0, 1, 'E')  # E
        playT(0, 1, 0, 1, 0, 0, 1, 0, 'R')  # R
        playT(0, 1, 0, 1, 0, 0, 1, 0, 'R')  # R
        playT(0, 1, 0, 0, 1, 1, 1, 1, 'O')  # O
        playT(0, 1, 0, 1, 0, 0, 1, 0, 'R')  # R
        """
        # print('Error - invalid character found, write aborted')


def one():
    write(2000, 100)


def zero():
    print("---")
    time.sleep(0.1)


def playT(a, b, c, d, e, f, g, h, name):
    if a == 1:
        one()
        print(name)
    if a == 0:
        zero()
        print(name)
    if b == 1:
        one()
        print(name)
    if b == 0:
        zero()
        print(name)
    if c == 1:
        one()
        print(name)
    if c == 0:
        zero()
        print(name)
    if d == 1:
        one()
        print(name)
    if d == 0:
        zero()
        print(name)
    if e == 1:
        one()
        print(name)
    if e == 0:
        zero()
        print(name)
    if f == 1:
        one()
        print(name)
    if f == 0:
        zero()
        print(name)
    if g == 1:
        one()
        print(name)
    if g == 0:
        zero()
        print(name)
    if h == 1:
        one()
        print(name)
    if h == 0:
        zero()
        print(name)
        print("---")


write_file()
