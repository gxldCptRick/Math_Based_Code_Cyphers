import math
import re
cleaner_regex = re.compile(r"([^A-Za-z0-9])")
name = 'Transposition cypher'

def validateInput(key, message):
    if(type(message) is not str):
        raise AssertionError("message is not of type str.")
    if(type(key) is not str and type(key) is not int):
        raise AssertionError("key must be either a str representing an int or int.")

def encrypt(key, message):
    validateInput(key, message)
    message = cleaner_regex.sub("", message)
    if(type(key) is str): 
        key = cleaner_regex.sub("", key)
        key = int(key)
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def decrypt(key, message):
    validateInput(key, message)
    message = cleaner_regex.sub("", message)
    if(type(key) is str):
        key = cleaner_regex.sub("", key)
        key = int(key)
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    numOfShadedBoxes = (num_of_columns * num_of_rows) - len(message);
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for character in message:
        plaintext[col] += character
        col += 1
        if(col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)
