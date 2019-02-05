import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
import cypher_app.supported_cyphers.helpers.detect_english as engrish

name = 'Caesars Cypher'
key_range = {
    "min": 1,
    "max": 25
}
key_type = "number"

description = "TODO: ADD DESCRIPTION"
example = "TODO: ADD EXAMPLE"


def is_valid_key(key):
    return (type(key) is str and key.isnumeric() or type(key) is int)


def validate_inputs(key, message):
    if(message is None):
        raise AssertionError("message cannot be None.")
    if(type(message) is not str):
        raise AssertionError("message must be of type str.")
    if(not is_valid_key(key)):
        raise AssertionError("The given key is not valid %s" % key)


def encrypt(key, message):
    validate_inputs(key, message)
    if(type(key) is str):
        key = int(key)
    translated = ''
    for c in message:
        if(c.isalnum()):
            Offset = ah.UPPER_OFFSET if c.isupper() else ah.LOWER_OFFSET
            adjustedValue = ord(c) - Offset
            caesar_value = adjustedValue + key
            account_for_wrap = caesar_value % ah.AMOUNT_OF_LETTERS
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
            Offset = ah.UPPER_OFFSET if c.isupper() else ah.LOWER_OFFSET
            adjustedValue = ord(c) - Offset
            caesar_value = adjustedValue - key
            account_for_wrap = caesar_value % ah.AMOUNT_OF_LETTERS
            remap_to_character = account_for_wrap + Offset
            character = chr(remap_to_character)
            translated += character
        else:
            translated += c
    return translated


def generate_alphabet(key):
    alphabets = [list(ah.ALPHABET)]
    if(type(key) is str and key.isnumeric()):
        key = int(key)
    alphabet = []
    for character in range(ah.AMOUNT_OF_LETTERS):
        adjusted_character = character + key
        adjusted_character %= ah.AMOUNT_OF_LETTERS
        alphabet.append(chr(adjusted_character + ah.UPPER_OFFSET))
    alphabets.append(alphabet)
    return alphabets


def brute_force_crack(message):
    result = []
    for num in range(ah.AMOUNT_OF_LETTERS):
        if(is_valid_key(num)):
            decrypted_message = decrypt(num, message)
            if(engrish.is_english(decrypted_message)):
                result.append("key: {0}, message: {1}".format(
                    str(num), decrypted_message))
    return result


if __name__ == "__main__":
    pass
