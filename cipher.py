# assignment: programming assignment 4
# author: Krishna Dua
# date: 11/26/2023
# file: cipher.py is a program that encodes or decodes the caeser cipher.
# input: Input is a txt file
# output: Output is the encoded or decoded files and strings.

def readfile():
    message = []
    while True:
        text_file = input("Please enter a file for reading:\n")
        try:
            read_file = open(text_file, 'r')
            message = read_file.readlines()
        except IOError:
            print("The selected file cannot be open for reading!")
            continue
        else:
            read_file.close()
            break
    return message

# write a list of strings (message) to a file
# the function should contain an input statement, open file statement,
# and try-except statement
def writefile(message):
    while True:
        newfile = input("Please enter a file for writing:\n")
        try:
            filecreate = open(newfile, 'w')
            filecreate.writelines(to_string(message))
        except IOError:
            print("The selected file cannot be open for writing!")
            continue
        else:
            filecreate.close()
            break
    # DO NOT RETURN ANYTHING!

# An optional helper function
# make a tuple of letters in the English alphabet
def make_alphabet():
   alphabet = ()
   for i in range(26):
       char = i + 65
       alphabet += (chr(char),)
   #print (alphabet)
   return alphabet

# encode plaintext letter by letter using a Caesar cipher 
# plaintext is a list of strings
# return a list of encoded strings
def encode(plaintext, shift = 3):
    ciphertext = []
    alphabet = make_alphabet()
    for line in plaintext:  # 'HELLO!'
        new_line = ""
        for char in line:    # 'H'
            if char in alphabet: # ('A', 'B', 'C', 'D', ...,'X', 'Y', 'Z')
                index = alphabet.index(char)
                newindex = (index + shift) % len(alphabet)
                newletter = alphabet[newindex]
                new_line += newletter
            else:
                new_line += char
        ciphertext.append(new_line)
    return ciphertext

# decode ciphertext letter by letter using a Caesar cipher
# ciphertext is a list of strings
# return a list of decoded strings
def decode(ciphertext, shift = -3):
    plaintext = encode(ciphertext, -3)
    return plaintext

# An optional helper function
# convert a list into a string
# for example, the list ["A", "B", "C"] is converted to the string "ABC" or
# the list ["H", "O", "W", " ", "A", "R", "E", " ", "Y", "O", "U", "?"] 
# is converted to the string "HOW ARE YOU?"
def to_string(text):
   return "".join(text)

# main program
if __name__ == '__main__':
    while True:
        print("Would you like to encode or decode the message?")
        choice = input("Type E to encode, D to decode, or Q to quit:\n")
        if choice == 'e' or choice == 'E':
            message = readfile()
            ciphertext = encode(message)
            writefile(ciphertext)
            print("Plaintext:\n"+to_string(message)+"\nCiphertext:\n"+to_string(ciphertext))
            continue

        elif choice == 'd' or choice == 'D':
            message = readfile()
            plaintext = decode(message)
            writefile(plaintext)
            print("Ciphertext:\n"+to_string(message)+"\nPlaintext:\n"+to_string(plaintext))
            continue

        elif choice == 'q' or choice == 'Q':
            print("Goodbye!")
            break
