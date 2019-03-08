import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah

name = "Caesar Word"
key_type = "text"
description = """The caesar word cypher might actually be a misnomer because it isn't really the same as a caesar cypher. in fact, i would argue it would have nothign to do with it.
it involves using a word and taking out the alphabetical order of the letters from that and leaving the other letters of the alphabet that are unused the same."""
example = """
lets say our key is: Goat
so we would make a new Alphabet starting with the Characters in sequence 
G O A T 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
then we check off which ones we took on the actually alphabet line
G O A T
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
x           x               x         x
and we fill in the blanks with the rest of the remaining alphabet in alphabetical order like this.

G O A T B C D E F H I J K L M N P Q R S U V W X Y Z
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
and now you have the the alpahbet to use to change your message

So lets say your message is: alex this is cool.
we look at the regular alphabet for a then we know that should become the letter above it i.e. G
so 
G
and then keep going with it
GJBX SEFR FR AMMN
and to decrypt you recreate the alphabet again
and work in reverse i.e. read the top to find  the letter on the bottom that matches
so we notice our G becomes an A.
and just repeat through the cyphered text
ALEX THIS IS COOL
then blammo that would be the decrypted text.
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
