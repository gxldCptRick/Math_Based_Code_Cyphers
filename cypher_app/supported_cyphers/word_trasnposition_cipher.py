import math
import re
import itertools
cleaner_regex = re.compile(r"([^A-Z,a-z])")

name = "Word Transposition Cypher"
key_type = "text"
description = """The Word Transposition Cypher is similar to the transposition cypher except with a couple of key details.
it uses the length of the key given in terms of how many characters it has as. it then build the grid as you would with a transposition.
the main difference comes with the way we write down the columns. we take it in the alphabetical order of the letters.
in order to decrypt it we need to do it in the write the message back in that same alphabetical order.
"""

example = """
Given Message: Buy Some Milk and Eggs
Given Keyword: Money
Column order:  24315
 m o n e y
===========
|b|u|y|s|o|
|m|e|m|i|l|
|k|a|n|d|e|
|g|g|s|x|x|
===========

e m n o y
this would be the order we remove them from the grid.
sid bmkg ymns ueag ole

that would be the message you send
sidx bmkg ymns ueag olek

they would then build a grid again with that same order as before
e m n o y
Column order : 24315
sid bmkg ymns ueag ole
rows = 20 / 5
  ===========
m |b|m|k|g|
o |u|e|a|g|
n |y|m|n|s|
e |s|i|d|x|
y |o|l|e|x|
  ===========
and the just read the columns down. from right to left.
buy some milk and eggs

Decrypted Word:
Buy some milk and eggs
"""


def validate_inputs(key, message):
    if(type(message) is not str):
        raise AssertionError("Message must be a str.")
    if(type(key) is not str):
        raise AssertionError("Key must be a str.")
    if(key.isnumeric()):
        raise AssertionError("Key must be alphabetical.")
    if(len(message) is 0):
        raise AssertionError("message must have some length.")


def encrypt(key, message):
    validate_inputs(key, message)
    message = cleaner_regex.sub("", message)
    key = cleaner_regex.sub("", key)
    key_length = len(key)
    ciphertext = [''] * key_length
    for col in range(key_length):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key_length
    sequence = generate_sequence(key)
    fulltext = ''
    for move in sequence:
        fulltext += ciphertext[move]
    return fulltext


def generate_sequence(string):
    string = string.upper()
    sorted_order = list(string)
    sorted_order.sort()
    sequence = []
    last_char = None
    last_index = None
    for order in sorted_order:
        if(order is last_char):
            last_index = string.index(order, last_index + 1)
        else:
            last_index = string.index(order)
            last_char = order
        sequence.append(last_index)
    return sequence


def decrypt(key, message):
    validate_inputs(key, message)
    key = cleaner_regex.sub("", key)
    message = cleaner_regex.sub("", message)
    pattern = generate_sequence(key)
    amount_of_columns = len(key)
    if(amount_of_columns is 0):
        raise AssertionError(
            "the key must be only characters with at a length greater than 0")
    length_of_input = len(message)
    if(length_of_input is 0):
        raise AssertionError("the message must contain an actuall message.")
    amount_of_rows = math.ceil(length_of_input/amount_of_columns)
    total_area = (amount_of_columns * amount_of_rows)
    amount_of_empty_spaces = total_area - length_of_input
    amount_of_valid_spaces = amount_of_columns - amount_of_empty_spaces
    # create the array to store the strings
    ciphertext = [''] * amount_of_columns
    current_position = 0
    for position in pattern:
        if(position < amount_of_valid_spaces):
            ciphertext[position] = message[current_position: current_position + amount_of_rows]
            current_position += amount_of_rows
        else:
            ciphertext[position] = message[current_position: current_position +
                                           (amount_of_rows - 1)]
            current_position += (amount_of_rows - 1)
    fulltext = ''
    for row in range(amount_of_rows):
        for column in range(amount_of_columns):
            if(row < len(ciphertext[column])):
                fulltext += ciphertext[column][row]
    return fulltext


def generate_patterns(length):
    return itertools.permutations(range(length), length)


def brute_force_guess(guess_length, message):
    message = cleaner_regex.sub("", message)
    amount_of_columns = guess_length
    amount_of_rows = math.ceil(len(message)/amount_of_columns)
    ciphertext = [''] * amount_of_columns
    possible_solutions = []
    for pattern in generate_patterns(amount_of_columns):
        current_position = 0
        for position in pattern:
            ciphertext[position] = message[current_position: current_position + amount_of_rows]
            current_position += amount_of_rows
        fulltext = ''
        for row in range(amount_of_rows):
            for column in range(amount_of_columns):
                if(row < len(ciphertext[column])):
                    fulltext += ciphertext[column][row]
        possible_solutions.append("%s: %s" % (pattern, fulltext))
    return possible_solutions
