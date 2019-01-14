import math
import re
cleaner_regex = re.compile(r"([^A-Z,a-z])")

name = "Word Transposition Cypher"

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
    return sequence;

def decrypt(key, message):
    validate_inputs(key, message)
    key = cleaner_regex.sub("", key)
    message = cleaner_regex.sub("", message)
    pattern = generate_sequence(key)
    amount_of_columns = len(key)
    if(amount_of_columns is 0):
        raise AssertionError("the key must be only characters with at a length greater than 0")
    length_of_input = len(message)
    if(length_of_input is 0):
        raise AssertionError("the message must contain an actuall message.")
    amount_of_rows = math.ceil(length_of_input/amount_of_columns)
    total_area = (amount_of_columns * amount_of_rows)
    amount_of_empty_spaces = total_area - length_of_input
    amount_of_valid_spaces = amount_of_columns - amount_of_empty_spaces
    #create the array to store the strings
    ciphertext = [''] * amount_of_columns
    current_position = 0
    for position in pattern:
        if(position < amount_of_valid_spaces):
            ciphertext[position] = message[current_position: current_position + amount_of_rows]
            current_position += amount_of_rows
        else:
            ciphertext[position] = message[current_position: current_position + (amount_of_rows - 1)]
            current_position += (amount_of_rows - 1)
    fulltext = ''
    for row in range(amount_of_rows):
        for column in range(amount_of_columns):
            if(row < len(ciphertext[column])):
                fulltext += ciphertext[column][row]
    return fulltext;