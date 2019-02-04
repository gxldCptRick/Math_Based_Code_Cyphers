import cypher_app.supported_cyphers.caesar as caesar
import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
name = "Vignere Cypher"


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
    if(not key.isalpha()):
        raise AssertionError('Key must be alphabetic.')
    for c in key:
        if(c.isalpha()):
            c = c.upper()
            value = ord(c) - ah.UPPER_OFFSET
            sequence.append(value)
    return sequence


def brute_force_hack(message):
    pass
