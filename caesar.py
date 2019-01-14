name = 'Caesars Cypher'

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
    upper = message.upper()
    translated = ''
    for c in upper:
        if(c.isalnum()):
            adjustedValue = ord(c) - 65
            caesar_value = adjustedValue + key
            account_for_wrap = caesar_value % 26
            remap_to_character = account_for_wrap + 65
            character = chr(remap_to_character)
            translated += character
        else:
            translated += c
    return translated

def decrypt(key, message):
    validate_inputs(key, message)
    if(type(key) is str):
        key = int(key)
    upper = message.upper()
    translated = ''
    for c in upper:
        if(c.isalnum()):
            adjustedValue = ord(c) - 65
            caesar_value = adjustedValue - key
            account_for_wrap = caesar_value % 26
            remap_to_character = account_for_wrap + 65
            character = chr(remap_to_character)
            translated += character
        else:
            translated += c
    return translated
    