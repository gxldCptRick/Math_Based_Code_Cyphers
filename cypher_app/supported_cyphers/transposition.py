import math
import re
import cypher_app.supported_cyphers.helpers.detect_english as engrish

cleaner_regex = re.compile(r"([^A-Za-z0-9])")
name = 'Transposition cypher'
key_type = "number"
description = """The Transposition Cypher Requires a word/phrase and a number to get a key. 
It will then create a chart using the word/phrase and using the number to create the number of columns
after producing the chart with the appropriate columns each letter in the word ignoring spaces goes into each column then row.
After the word is entirely in the chart grab each letter and add the letters together by row then column."""
example = """
* are spaces

Options given - Alex The Goat and 5
|===========|
||A|L|E|X|T||
||H|E|G|O|A||
||T|*|*|*|*||
|===========|

Encrypted Word would be
AHTLE EG XO AT

Decryption for AHTLE EG XO AT
|=====|
|A|H|T|
|L|E|*|
|E|G|*|
|X|O|*|
|T|A|*|
|=====|

Decrypted Word Would be
ALEXTHEGOAT ****
"""


def validateInput(key, message):
    if(type(message) is not str):
        raise AssertionError("message is not of type str.")
    if(type(key) is not str and type(key) is not int):
        raise AssertionError(
            "key must be either a str representing an int or int.")


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
    numOfShadedBoxes = (num_of_columns * num_of_rows) - len(message)
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


def brute_force_crack(message):
    transposition_range = len(message)
    lower_range = 2
    results = []
    for key in range(lower_range, transposition_range):
        decrypted_message = decrypt(key, message)
        if (engrish.is_english(decrypted_message)):
            results.append("key: {0}, message: {1}".format(
                str(key), decrypted_message))
    return results
