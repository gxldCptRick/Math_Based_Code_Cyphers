import supported_cyphers.helpers.alphabet_helpers as ah
import supported_cyphers.helpers.detect_english as engrish
name = "Multiplication Cypher"
key_range = {
    "min": 1,
    "max": 25
}

def is_valid_key(key):
    if(type(key) is str):
        if(key.isnumeric()):
            key = int(key)
        else:
            return False
    if(type(key) is not int):
        return False
    return key % 13 is not 0 and key % 2 is not 0


def encrypt(key, message):
    if(not is_valid_key(key)):
        raise AssertionError("The Given key was not valid")
    if(type(key) is str and key.isnumeric()):
        key = int(key)
    encrypted_message = ""
    for character in message:
        if(character.isalpha()):
            if(character.isupper()):
               encrypted_message += transform_character(character, ah.UPPER_OFFSET, key)
            else:
                encrypted_message += transform_character(character, ah.LOWER_OFFSET, key)
        else:
            encrypted_message += character
    return encrypted_message


def decrypt(key, message):
    if(not is_valid_key(key)):
        raise AssertionError("The Given key was not valid")
    if(type(key) is str and key.isnumeric()):
        key = int(key)
    inverse_key = calculate_inverse(key)
    return encrypt(inverse_key, message)


def calculate_inverse(key):
    for possible_inverse in range(1, ah.AMOUNT_OF_LETTERS + 1):
        if((possible_inverse * key) % ah.AMOUNT_OF_LETTERS == 1):
            return possible_inverse
    raise AssertionError("There was no inverse key found for the given key %s" % key)


def transform_character(character, offset, key):
    og_position = ord(character) - offset
    adjust_position = og_position * key
    adjust_position %= ah.AMOUNT_OF_LETTERS
    return chr(adjust_position + offset)


def generate_alphabet(key):
    alphabets = []
    alphabets.append(list(ah.ALPHABET))
    alphabets.append(generate_alphabet_for_key(key))
    inverse_key = calculate_inverse(key)
    alphabets.append(generate_alphabet_for_key(inverse_key))
    return alphabets


def generate_alphabet_for_key(key):
    if(type(key) is str and key.isnumeric()):
        key = int(key)
    elif(type(key) is not int):
        raise AssertionError("key must either be a number or a string representing a number.")
    if(key % ah.AMOUNT_OF_LETTERS == 0):
        print('Warning You Will not be able to decrypt the message')
    alphabet = [] 
    for character in range(ah.AMOUNT_OF_LETTERS):
        adjustedCharacter = character * key
        adjustedCharacter %= ah.AMOUNT_OF_LETTERS
        alphabet.append(chr(adjustedCharacter + ah.UPPER_OFFSET))
    return alphabet


def generate_key_pairs():
    keys = []
    for i in range(1, ah.AMOUNT_OF_LETTERS):
        try:
            pairs = []
            pairs.append(i)
            pairs.append(calculate_inverse(i))
            keys.append(pairs)
        except AssertionError:
            pass
    pass
    return keys


def brute_force_crack(message):
    results = []
    for num in range(ah.AMOUNT_OF_LETTERS):
        if(is_valid_key(num)):
            decrypted_message = decrypt(num, message)
            if(engrish.is_english(decrypted_message)):
                results.append("key: {0}, message: {1}" % (num, decrypted_message))
    return results


if __name__ == "__main__":
    pass