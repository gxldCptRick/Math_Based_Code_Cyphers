import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah

name = "Caesar Word"
key_type = "text"
description = "A Key and a Message would be given. The message letters are then shifted by the letter corresponding with the key"
example = """
Given Key: Goat
Given Message: Animal


6 14  0 19  6  14
G  o  a  t  G  o
0 13  8 14  0  10
A  n  i  m  a  l

(0+6)(Mod 26)
(13+14)(Mod 26)
(8+0)(Mod 26)
(14+19)(Mod 26)
(0+6)(Mod 26)
(10+14)(Mod 26)

Encrypted Word
Gbihgy

Decrypt
Key: Goat
6 14  0 19  6 14
G  o  a  t  G  o
6  1  8  7  6  24
g  b  i  h  g  y


26 + (g-6)(mod 26)
26 + (b-14)(mod 26)
26 + (i-0)(mod 26)
26 + (h-19)(mod 26)
26 + (g-6)(mod 26)
26 + (y-14)(mod 26)

decrypted word: 
Animal
"""


def encrypt(key, message):
    alphabits = generate_alphabet(key)
    decrypted_message = ''
    for c in message:
        if c.isalpha():
            decrypted_message += alphabits[ah.ALPHABET.index(c.upper())]
        else:
            decrypted_message += c
    return decrypted_message


def decrypt(key, message):
    alphabits = generate_alphabet(key)
    print(alphabits)
    decrypted_message = ''
    for c in message:
        if c.isalpha():
            decrypted_message += ah.ALPHABET[alphabits.index(c.upper())]
        else:
            decrypted_message += c
    return decrypted_message


def generate_alphabet(key):
    key = key.upper()
    alphabet = []
    for c in key:
        if(c.isalpha()):
            if(c not in alphabet):
                alphabet.append(c)
    for c in ah.ALPHABET:
        if(c not in alphabet):
            alphabet.append(c)
    return alphabet
