import random
import string

program = ['\n', '# Here is your randomly generated Python program. It has been written to the file `randprog.py`.']

# path = 0

def choice_chooser():
    choice = random.randint(0, 2)

    if choice == 0:
        make_print_function()

    if choice == 1:
        declare_global()

"""
                              { Decision tree for the random program writer }

                                            choice_chooser
                                                  |
                                    ______________|_________________
                                   |                                |
                            random print func              random global declaration
                                   |                                |
            ____________ __________|                                |______________________
           |            |          |                                |                      |
         string      integer     variable                         string                 integer
"""
variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
integer_variables = []
string_variables = []
used_variables = []

def make_print_function():
    print_choice = random.randint(0, 2)

    print_string = '\'\\n\''

    if print_choice == 0:
        print_string = 'str(' + str(random.randint(-127, 127)) + ')'

    if print_choice == 1:
        str_length = random.randint(1, 64)
        rando = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(0, str_length)])
        print_string = "'" + rando + "'"

    program.append('print(' + print_string + ')')

    if print_choice == 2:
        variable_type = random.randint(0, 1)
        if variable_type == 0: # Print a string variable.
            if string_variables:
                variable_index = random.randint(0, (len(string_variables) - 1))
                program.append('print(' + string_variables[variable_index] + ')')
            else:
                program.append('print(\'\\n\')')
        if variable_type == 1: # Print an integer variable.
            if integer_variables:
                variable_index = random.randint(0, (len(integer_variables) - 1))
                program.append('print(str(' + integer_variables[variable_index] + '))')
            else:
                program.append('print(\'\\n\')')



def declare_global(): # No one said that this program writes *good* programs, just that it only writes *compilable* programs.
    variable_name = variables[random.randint(0, 25)]
    if variable_name in used_variables:
        pass
    else:
        variables.append(variable_name)
        type = random.randint(0, 1)
        if type == 0: # Declare an integer variable
            specific_variable = variables[random.randint(0, ((len(variables)) - 1))]
            integer_variables.append(specific_variable)
            program.append(specific_variable + " = " + str(random.randint(-127, 127)))
        if type == 1: # Declare a string variable
            specific_variable = variables[random.randint(0, ((len(variables)) - 1))]
            string_variables.append(specific_variable)
            program.append(specific_variable + " = '" + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(0, 16)]) + "'")
    used_variables.append(variable_name)


vez = random.randint(1, 16)

for x in range (0, vez):
    choice_chooser()

file = open('randprog.py', 'w+')
for x in program:
    file.write(x + '\n')
file.close()
