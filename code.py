#Encrypted Message Program


import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)

plain_text=input("enter the encrypted message:")
ciper_text=""

for letter in plain_text:
    index=chars.index(letter)
    ciper_text+=key[index]

print("Original message:",plain_text)
print("Encrypted message:",ciper_text)
