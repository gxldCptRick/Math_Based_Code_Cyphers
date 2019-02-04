from io import open
import cypher_app.supported_cyphers.reverse as reverse
import random
BaconDecoder = {
    "00000": 'A',
    "00001": 'B',
    "00010": 'C',
    "00011": 'D',
    "00100": 'E',
    "00101": 'F',
    "00110": 'G',
    "00111": 'H',
    "01000": '(I/J)',
    "01001": 'K',
    "01010": 'L',
    "01011": 'M',
    "01100": 'N',
    "01101": 'O',
    "01110": 'P',
    "01111": 'Q',
    "10000": 'R',
    "10001": 'S',
    "10010": 'T',
    "10011": '(U,V)',
    "10100": 'W',
    "10101": 'X',
    "10110": 'Y',
    "10111": 'Z'
}

BaconEncoder = {
    'A': "00000",
    'B': "00001",
    'C': "00010",
    'D': "00011",
    'E': "00100",
    'F': "00101",
    'G': "00110",
    'H': "00111",
    'I': "01000",
    'J': "01000",
    'K': "01001",
    'L': "01010",
    'M': "01011",
    'N': "01100",
    'O': "01101",
    'P': "01110",
    'Q': "01111",
    'R': "10000",
    'S': "10001",
    'T': "10010",
    'U': "10011",
    'V': "10011",
    'W': "10100",
    'X': "10101",
    'Y': "10110",
    'Z': "10111"
}

words = None
with open('words.txt') as file:
    words = file.read().split('\n')

name = 'Bacons Cypher'


def encrypt(message):
    binary = create_binary(message)
    sentence = create_sentence(len(binary))
    bacon_sentence = baconize_sentence(sentence, binary)
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


def create_sentence(size):
    sentence = ""
    while(size > 0):
        word = random.choice(words)
        if(size - len(word) >= 0):
            sentence += word + " "
            size -= len(word)
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
    reversedString = reverse.encrypt(binary)
    if(binary in BaconDecoder):
        return BaconDecoder[binary]
    elif(reversedString in BaconDecoder):
        return BaconDecoder[reversedString]
    else:
        return None


def decrypt(message):
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
