import re
"""
In the first line, print True if has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False. 
"""

if __name__ == '__main__':
    s = input()
    lowercase, uppercase, alphanumeric, digits, characters = [False] *5
    if re.search(r'[a-z]+', s):
        lowercase, characters = True, True
    if re.search(r'[1-9]+', s):
        digits = True
    if re.search(r'[A-Z]+', s):
        uppercase = True
        if not characters:
            characters = True
    if characters or digits:
        alphanumeric = True

    print(f'{alphanumeric}\n{characters}\n{digits}\n{lowercase}\n{uppercase}\n')
