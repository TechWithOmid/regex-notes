"""
Identifiers:
    \d any number
    \D anything but number
    \s space
    \S anything but space
    \w any character
    \W anything but charcaters
    .  any character, except for newline
    \b the white space around words
    \. a period (this is exeption)

Modifiers:
    {x-y} we're expecting x-y \d{1-3} 
    + Match 1 or more
    ? Match 0 or 1
    * Match 0 or more
    $ Match the end of a string
    ^ Matching the beginning of string
    | either or \d{1-3}|\w{6-10}
    [] range or 'variance'
    {x} expecting 'x' amount
    
White space characters:
    \n new line
    \s space 
    \t tab
    \e escape
    \f form feed
    \r return
"""
import re


exampleString = """
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his gradfather, Oscar, is 102.
"""

ages = re.findall(r'\d{1,3}', exampleString)
print(ages)

names = re.findall(r'[A-Z][a-z]*', exampleString)
print(names)
