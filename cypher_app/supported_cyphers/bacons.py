import cypher_app.supported_cyphers.reverse as reverse
import random
import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
BaconDecoder = {}
BaconEncoder = {}
key_type = "none"
description = """To encrypt the message must be given 
and the message will have each letter turned into its binary value
Decrypt will have the binary number turned into a message.
"""

example = """
Encrypt
Hello
Encrypted Key:
00111 00100 01010 01010 01101

Decrypt
00111 00100 01010 01010 01101
Decrypted Key:
 H      E     L     L     O
"""
counter = 0
for a in ah.ALPHABET:
    binary_string = "{0:05b}".format(counter)
    if(binary_string in BaconDecoder.keys()):
        BaconDecoder[binary_string] = "(%s,%s)" % (
            BaconDecoder[binary_string], a)
    else:
        BaconDecoder[binary_string] = a
    BaconEncoder[a] = binary_string
    counter += 1
    if(a == 'I' or a == 'U'):
        counter -= 1

name = 'Bacons Cypher'


def encrypt(key, message):
    binary = create_binary(message)
    sentence = create_sentence(len(binary), key)
    bacon_sentence = baconize_sentence(sentence, binary).strip()
    return bacon_sentence


def baconize_sentence(sentence, binary):
    current_index = 0
    baconized_sentence = ''
    for character in sentence:
        if(character.isalpha()):
            if(binary[current_index] in '0'):
                baconized_sentence += character.lower()
            else:
                baconized_sentence += character.upper()
            current_index += 1
        else:
            baconized_sentence += character
    return baconized_sentence


def create_sentence(size, key):
    sentence = ""
    num = 0
    while(size > 0):
        current_char = key[num % len(key)]
        if current_char.isalpha():
            size -= 1
        if(num % len(key) == 0):
            sentence += " "
        sentence += current_char
        num += 1
    return sentence


def create_binary(message):
    binary = ''
    for character in message:
        if(character.isalpha()):
            binary += BaconEncoder[character.upper()]
    return binary


def process_binary(binary):
    if(type(binary) is not str):
        raise AssertionError("binary must be a type str.")
    if(binary in BaconDecoder):
        return BaconDecoder[binary]
    else:
        return '*'


def decrypt(message, key=None):
    if(type(message) == str):
        binaryStrings = []
        binaryString = ""
        for character in message:
            if(character.isalpha()):
                if(character.islower()):
                    binaryString += "0"
                else:
                    binaryString += "1"
                if(len(binaryString) is 5):
                    binaryStrings.append(binaryString)
                    binaryString = ""
        if(binaryString not in binaryStrings and len(binaryString) is 5):
            binaryStrings.append(binaryString)
        output = ""
        for binaryString in binaryStrings:
            print(binaryString)
            output += process_binary(binaryString)
        return output
    else:
        raise AssertionError("message must be of type str")
