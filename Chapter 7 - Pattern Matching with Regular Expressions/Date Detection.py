#   Detect dates in the DD/MM/YYYY format.

import pyperclip, re

dateRegex = re.compile(r'''(
    ([0-3][0-9])
    (\s|-|\.|/)?
    ([0-9]{2})
    (\s|-|\.|/)?
    ([1-2][0-9]{3})
    )''', re.VERBOSE)

def isLeapYear(year):
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 != 0):
        return True
    else:
        return False

def isValidDate(day, month, year):
    if int(month) == 2 and isLeapYear(year):
        return int(day) <= 29
    elif int(month) == 2 and not isLeapYear(year):
        return int(day) <= 28
    elif int(month) in [4,6,9,11]:
        return int(day) <= 30
    else:
        return int(day) <= 31


text = str(pyperclip.paste())

matches = []

for groups in dateRegex.findall(text):
    day, month, year = groups[1], groups[3], groups[5]
    dates = '/'.join([groups[1], groups[3], groups[5]])
    #print(groups)
    if isValidDate(day, month, year):
        matches.append(dates)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found.')

