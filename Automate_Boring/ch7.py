# phone number recognition
def IsPhoneNumber(text):

    if len(text) != 12:
        return False
    for i in range(0, 3):
        # .isdecimal essentially tests to see if each character is a number...
        # text[i] is checking each character of the text entered (list)
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        # the range function is NOT inclusive! so 12 = n + 1. 
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(IsPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(IsPhoneNumber('Moshi moshi'))
