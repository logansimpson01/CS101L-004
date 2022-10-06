choice = input('Would you like to encode (1) or decode (2) or quit (Q)?').upper()
    if choice != '1' and choice != '2' and choice != 'Q':
        print('invalid option')
        continue
    if choice == 1:

    if choice == 2:

    if choice == Q:
        quit()

text = input('Enter (brief) text to encrypt:').lower()

shift_letters = int(input('Enter the number to shift letters by: ')
            


def encrypt(text,s):
    result = ""
   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
      return result

def decrypt (text,s) :
    result = ""
    
    
    
