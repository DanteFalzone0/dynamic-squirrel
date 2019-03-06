import os

def play(freq, time):
    os.system('play -n synth %s sin %s' % (time / 1000, freq))

play(800, 200)

