# This code was written in March 2019. I have archived it here because
# I'm going to delete the repository in which it previously resided.

"""
    Copyright (C) 2019  Dante James Falzone
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
# The GNU TI Basic Compiler by DJF,
# implemented in Python by Dante James Falzone.
# I have no input on the text editor wars; personally, I use either
# gedit, vim, or nano, and I have never used emacs (as of 2019-03-25),
# but I don't give a hoot what text editors other people use.
# Seriously, why the hell do other people care about a silly thing
# like that?

import sys
import os
import re
import random

files = sys.argv[1]

source = []
headers = ["// This code is not meant to be read by humans.",
           "#include <stdio.h>"]
temp_code = []
out_code = []

if files[-4:] != ".tib":
    print('\033[1;31mFilename Error: Not a `.tib` file\033[0m')
    sys.exit()


else:
    string = open(files).read()
    source_code_lines = string.split(':')
    for x in source_code_lines:
        if x != "\n":
            if x != '':
                source.append(":" + x)


def is_string_var(text):
    if text == "Str0" or text == "Str1" or text == "Str2" or text == "Str3":
        return True
    elif text == "Str4" or text == "Str5" or text == "Str6" or text == "Str7":
        return True
    elif text == "Str8" or text == "Str9":
        return True
    else:
        return False
    # These are the only valid variables of type string in TI Basic (at least,
    # on my TI-84 Plus).


def interpret(code):
    clrhome = re.search(':ClrHome', code)
    disp1q  = re.search(':Disp "(.+)', code) # Match Disp for one quote
    disp2q  = re.search(':Disp "(.+)"', code) # Match Disp for two quotes
    disp0q  = re.search(':Disp (.+)', code) # Match Disp for no quotes
    inputs  = re.search(r':Input \"(.*?)\",(.+)', code)
    inputc  = re.search(':Input (.+)', code)
    pausec  = re.search(':Pause(\s?)', code)
    pauses  = re.search(':Pause (.+)', code)
    progcal = re.search(':prgm(.+)', code)

    if clrhome:
        var0 = "var" + str(random.randint(0, 1000000000000))
        var1 = "var" + str(random.randint(0, 1000000000000))
        temp_code.append(
         'int '+var0+';\n'
        +'for ('+var0+' = 0; '+var0+' < 150; '+var0+'++) {'
        +'\nprintf("\\n");\n'
        +'}\n'
        +'int '+var1+';\n'
        +'for ('+var1+' = 0; '+var1+' < 150; '+var1+'++) {'
        +'\nprintf("\\x1b[A");\n'
        +'}') # Sorry for this bit, I know it looks horrid

    elif disp1q and not disp2q: # because regex would get confused otherwise
        temp_code.append('printf("'+disp1q.group(1)+'\\n");\n')

    elif disp2q:
        temp_code.append('printf("'+disp2q.group(1)+'\\n");\n')

    elif disp0q:
        if is_string_var(disp0q.group(1)):
            temp_code.append('printf("%s\\n", '+disp0q.group(1)+');\n')
        else:
            caps = re.search('[A-Z]', disp0q.group(1))
            unacceptable = re.search('[A-Z](.+?)', disp0q.group(1))
            if caps and not unacceptable:
                temp_code.append('printf("%d\\n",'+disp0q.group(1)+');\n')
            else:
                print('\033[1;31mSyntax Error: Invalid variable name '
                +'on line '+str(source.index(code)+1)+ '\033[0m')
                sys.exit()


    elif inputs: # Wrote this block last night
        if is_string_var(inputs.group(2)):
            temp_code.append(
             'char '+inputs.group(2)+'[16];\n'
            +'printf("'+inputs.group(1)+'");\n'
            +'fgets('+inputs.group(2)+', 16, stdin);\n')
        else:
            caps = re.search('[A-Z]', inputs.group(2))
            unacceptable = re.search('[A-Z](.+)', inputs.group(2))
            if caps and not unacceptable:
                temp_code.append(
                 'int '+inputs.group(2)+';\n'
                +'printf("'+inputs.group(1)+'");\n'
                +'scanf("%d", &'+inputs.group(2)+');\n')
                # The screen on the TI-84 Plus is only 16 chars wide
            else:
                print('\033[1;31mSyntax Error: Invalid variable name '
                +'on line '+str(source.index(code)+1)+ '\033[0m')
                sys.exit()

    elif inputc:
        if is_string_var(inputc.group(1)):
            temp_code.append(
             'char '+inputc.group(1)+'[16];\n'
            +'printf("?");\n'
            +'fgets('+inputc.group(1)+', 16, stdin);\n')
        else:
            caps = re.search('[A-Z]', inputc.group(1))
            unacceptable = re.search('[A-Z](.+)', inputc.group(1))
            if caps and not unacceptable:
                temp_code.append(
                 'int '+inputc.group(1)+';\n'
                +'printf("?");\n'
                +'scanf("%d", &'+inputc.group(1)+');\n')
                # The screen on the TI-84 Plus is only 16 chars wide
            else:
                print('\033[1;31mSyntax Error: Invalid variable name '
                # Admittedly not what the TI-84 Plus does in response to such
                # an occurence; it just says `ERR:SYNTAX`, followed by the
                # options `1:Quit` or `2:Goto`. These features will hopefully
                # be implemented in a future version of the compiler.
                +'on line '+str(source.index(code)+1)+ '\033[0m')
                sys.exit()
    elif pausec:
        var0 = "var" + str(random.randint(0, 1000000000000))
        temp_code.append(
         'char '+var0+';\n'
        +'scanf("%c", &'+var0+');\n'
        +'getchar();\n')
    elif pauses:
        caps = re.search('[A-Z]', pauses.group(1))
        unacceptable = re.search('[A-Z](.+)', pauses.group(1))
        string = pauses.group(1)
        if string[0] == '"': # because terminating quotes are optional
            if string[-1] != '"':
                var0 = "var" + str(random.randint(0, 1000000000000))
                temp_code.append(
                 'printf('+string+'");\n'
                +'char '+var0+';\n'
                +'scanf("%c", &'+var0+');\n'
                +'getchar();\n')
            else:
                var0 = "var" + str(random.randint(0, 1000000000000))
                temp_code.append(
                 'printf('+string+');\n'
                +'char '+var0+';\n'
                +'scanf("%c", &'+var0+');\n'
                +'getchar();\n')
        elif caps and not unacceptable:
            temp_code.append(
             'printf("%d", '+string+');\n'
            +'char '+var0+';\n'
            +'scanf("%c", &'+var0+');\n'
            +'getchar();\n')
        elif is_string_var(string):
            temp_code.append(
             'printf("%s", '+string+');\n'
            +'char '+var0+';\n'
            +'scanf("%c", &'+var0+');\n'
            +'getchar();\n')
    elif progcal:
        temp_code.append('//todo: implement this\n')


for i in range (0, len(source)):
    interpret(source[i])

for x in headers:
    out_code.append(x)

out_code.append("int main(void) {")
for x in temp_code:
    out_code.append(x)
out_code.append("return 0;}")

out = open("out.c", "w+")
for x in out_code:
    out.write(x + "\n")
out.close()

pgrm = files.replace(".tib", "")
os.system("gcc out.c -o prgm"+pgrm+
          " && ./prgm"+pgrm+" && rm out.c")
