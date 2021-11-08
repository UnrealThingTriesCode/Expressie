__author__ = ['Sunka Labree']
__date__ = ['2021.10.14 -> 2021.10.27']
# imports sys.argv
import sys

# Creates a dictionary
dicti = {'a': 'alpha   |  *-', 'b': 'bravo   |  -***', 'c': 'charlie |  -*-*',
         'd': 'delta   |  -**', 'e': 'echo    |  *', 'f': 'foxtrot |  **-*',
         'g': 'golf    |  --*', 'h': 'hotel   |  ****', 'i': 'india   |  **',
         'j': 'juliet  |  *---', 'k': 'kilo    |  -*-', 'l': 'lima    |  *-**',
         'm': 'mike    |  --', 'n': 'november| -*', 'o': 'oscar   |  ---',
         'p': 'papa    |  *--*', 'q': 'quebec  |  --*-', 'r': 'romeo   |  *-*',
         's': 'sierra  |  ***', 't': 'tango   |  -', 'u': 'uniform |  **-',
         'v': 'victor  |  ***-', 'w': 'whiskey |  *--', 'x': 'x-ray   |  -**-',
         'y': 'yankee  |  -*--', 'z': 'zulu.   |  --**'}

# Checks if user has input words
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = input('Enter one or more letters to translate: ')
# Translates given letters to NATO
for letter in user_input:
    translation = dicti.get(letter)
    print(letter, translation, sep='\t')
    

