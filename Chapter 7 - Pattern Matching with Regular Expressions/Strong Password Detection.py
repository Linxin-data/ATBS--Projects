#   A strong password has the following:
#   8+ characters
#   Both uppercase and lowercase characters
#   1+ digit

import pyperclip, re

def isUpperCase(password):
    if re.search('[A-Z]', password):
        return True
    return False

def isLowerCase(password):
    if re.search('[a-z]', password):
        return True
    return False

def digitCheck(password):
    if re.search('[0-9]', password):
        return True
    return Fals


def isStrongPassword():
    password = input('Please enter password:')
    passwordCheck = dict()
    passwordCheck['check8+Characters'] = (len(password) >= 8)
    passwordCheck['checkUpperCase'] = isUpperCase(password)
    passwordCheck['checkLowerCase'] = isLowerCase(password)
    passwordCheck['checkDigit'] = digitCheck(password)

    if False in passwordCheck.values():
        print('Weak password. Please re-enter')
    else:
        print('Strong password')

isStrongPassword()


# #   Different attempt. Shorter
# import re
#
# passwordRegex = ('[A-Z]', '[a-z]', '[0-9]')
#
# def isStrongPassword():
#     password = input('Please enter password:')
#     if len(password) >= 8 and all(re.search(r, password) for r in passwordRegex):
#         print('Strong Password')
#     else:
#         print('Weak Password. Please re-enter')
#
# isStrongPassword()
