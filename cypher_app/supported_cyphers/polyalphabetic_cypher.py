import cypher_app.supported_cyphers.caesar as caesar
import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
name = "Vigen\u00E9re Cypher"
key_type = "text"

description = "The Vigen\u00E9re Cypher is a polyalphabetic cypher based on the use of mulitple Caesar Cyphers to encrypt."
example = """
First you choose the message you wish to encrypt and then a key word or phrase if you want
    text: This is something important
    key: sure

then you place the key under the text to start the encryption 
    encrypt: This is something important
             sure su resuresur suresures

we use the ordinal value of the key for example and shift each letter by that amount to encrypt the phrase.
     t  h  i s
     s  u  r e
    18 20 17 4

    so then t would be l, h would be b, i would be z, and s would be w and so forth for a fully encoded phrase of
    Encrypted: lbzw am jseyklahx mejfvluex

"""


def encrypt(key, message):
    pointer = 0
    sequence = generate_key_sequence(key)
    length = len(sequence)
    encrypted_message = ''
    for c in message:
        if(c.isalpha()):
            encrypted_message += caesar.encrypt(sequence[pointer], c)
            pointer += 1
            pointer %= length
        else:
            encrypted_message += c
    return encrypted_message


def decrypt(key, message):
    pointer = 0
    sequence = generate_key_sequence(key)
    length = len(sequence)
    decrypted_message = ''
    for c in message:
        if(c.isalpha()):
            decrypted_message += caesar.decrypt(sequence[pointer], c)
            pointer += 1
            pointer %= length
        else:
            decrypted_message += c
    return decrypted_message


def generate_key_sequence(key):
    sequence = []
    for c in key:
        if(c.isalpha()):
            c = c.upper()
            value = ord(c) - ah.UPPER_OFFSET
            sequence.append(value)
    return sequence


def brute_force_hack(message):
    pass
