import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah

name = "Caesar Word"


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
