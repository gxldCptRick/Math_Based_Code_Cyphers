name = 'Reverse Cypher'
key_type = "none"
description = "The reverse cypher encrypts a message by printing the given word in reverse order."
example = """"Hello World" encrypts to "dlroW olleH"
dlroW olleH decrypts to Hello World
"""


def encrypt(message):
    if(message is None):
        raise AssertionError("message cannot be None.")
    elif(type(message) is not str):
        raise AssertionError("message must be of type str.")
    else:
        output = ''
        current_character = len(message) - 1
        while current_character >= 0:
            output += message[current_character]
            current_character -= 1
        return output


def decrypt(message):
    return encrypt(message)
