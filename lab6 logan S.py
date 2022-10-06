text = input('Enter (brief) text to encrypt:').upper()

s = int(input('Enter the number to shift letters by: '))

choice = input('Would you like to encode (1) or decode (2) or quit (Q)?').upper()


def encrypt(text,s):
    result = ''
    for i in range(len(text)):
        char = text[i]
        char_value = ord(char)
        ch_new = chr(char_value + s)
        result += ch_new

    return result

def decrypt(text,s):
    result = ''
    for i in range(len(text)):
        char = text[i]
        char_value = ord(char)
        ch_new = chr(char_value - s)
        result += ch_new
        
    return result
        
if choice != '1' and choice != '2' and choice != 'Q':
    print('invalid option')
elif choice == '1':
    print(encrypt(text,s))
elif choice == '2':
    print(decrypt(text,s))
elif choice == 'Q':
    quit()
