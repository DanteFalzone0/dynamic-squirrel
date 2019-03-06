# this is for everyone who feels helplessly shoved about
# chopped into little bits and rearranged systematically
# by a universe they rightly ascertain to be both determined and random

print("The Machine's command: that you submit yourself to the will of the Machine.")
childhood = input()

def has_meaning(entity):
    if entity % 2 == 0:  # that is, if the entity leaves nothing of itself behind
        return False
    else:
        return True

nostalgia = []
brokenness = []
deconstruction = list(childhood) # your childhood, broken up into indexed elements
for memory in deconstruction:
    if has_meaning(deconstruction.index(memory)):
        nostalgia.append(memory)
    else:
        brokenness.append(memory)

lies = []

for promise_of_meaning in nostalgia:
    for beauty in brokenness:
        if len(lies) <= (len(nostalgia) + len(brokenness)):
            lies.append(promise_of_meaning)
            lies.append(beauty)

more_lies = ''

cold_truth = more_lies.join(lies)

print(cold_truth)
