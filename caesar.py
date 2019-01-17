name = 'Caesars Cypher'
UPPER_OFFSET = 65
LOWER_OFFSET = 97
AMOUNT_OF_LETTERS = 26

def validate_inputs(key, message):
    if(message is None):
        raise AssertionError("message cannot be None.")
    if(type(message) is not str):
        raise AssertionError("message must be of type str.")
    if(key is None):
        raise AssertionError("key cannot be None")
    if(type(key) is not int and type(key) is not str):
        raise AssertionError("key must be an int or a str")
    if(not key.isnumeric()):
        raise AssertionError("key must be numeric")

def encrypt(key, message):
    validate_inputs(key, message)
    if(type(key) is str):
        key = int(key)
    translated = ''
    for c in message:
        if(c.isalnum()):
            Offset = UPPER_OFFSET if c.isupper() else LOWER_OFFSET
            adjustedValue = ord(c) - Offset
            caesar_value = adjustedValue + key
            account_for_wrap = caesar_value % AMOUNT_OF_LETTERS
            remap_to_character = account_for_wrap + Offset
            character = chr(remap_to_character)
            translated += character
        else:
            translated += c
    return translated

def decrypt(key, message):
    validate_inputs(key, message)
    if(type(key) is str):
        key = int(key)
    translated = ''
    for c in message:
        if(c.isalnum()):
            Offset = UPPER_OFFSET if c.isupper() else LOWER_OFFSET
            adjustedValue = ord(c) - Offset
            caesar_value = adjustedValue - key
            account_for_wrap = caesar_value % AMOUNT_OF_LETTERS
            remap_to_character = account_for_wrap + Offset
            character = chr(remap_to_character)
            translated += character
        else:
            translated += c
    return translated
    