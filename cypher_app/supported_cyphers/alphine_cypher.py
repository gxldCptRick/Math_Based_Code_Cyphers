import cypher_app.supported_cyphers.caesar as caesar
import cypher_app.supported_cyphers.mulitplicative_cypher as mulitplicative_cypher
import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
import cypher_app.supported_cyphers.helpers.detect_english as engrish

name = "Alphine Cypher"
key_range = {
    "min": 26,
    "max": 676
}


def validate_key(key):
    pass


def encrypt(key, message):
    if type(key) is str:
        key = int(key)
    keys = generate_keys(key)
    print(keys)
    mult_encrypt = mulitplicative_cypher.encrypt(keys["mult"], message)
    return caesar.encrypt(keys["caesar"], mult_encrypt)


def decrypt(key, message):
    if type(key) is str:
        key = int(key)
    keys = generate_keys(key)
    mult_encrypt = caesar.decrypt(keys["caesar"], message)
    return mulitplicative_cypher.decrypt(keys["mult"], mult_encrypt)


def generate_keys(key):
    caesar_key = (key % ah.AMOUNT_OF_LETTERS)
    mult_key = int((key - caesar_key) / ah.AMOUNT_OF_LETTERS)
    if(mult_key % 2 is 0 or mult_key % 13 is 0):
        raise AssertionError(
            'The alphine Key must have a valid multiplicative key')
    return {
        "mult": mult_key,
        "caesar": caesar_key
    }


def generate_alphine_key(caesar_key, multi_key):
    if(not caesar.is_valid_key(caesar_key)):
        raise AssertionError("The caesar_key was not valid {0}" % caesar_key)
    if(not mulitplicative_cypher.is_valid_key(multi_key)):
        raise AssertionError("The given multiplicative key {0}" % multi_key)
    return multi_key * ah.AMOUNT_OF_LETTERS + caesar_key


def generate_alphabet(key):
    keys = generate_keys(key)
    alphabets = [list(ah.ALPHABET)]
    encrypted_alphabet = caesar.encrypt(
        keys["caesar"], mulitplicative_cypher.encrypt(keys["mult"], ah.ALPHABET))
    alphabets.append(list(encrypted_alphabet))
    decrypted_alphabet = mulitplicative_cypher.decrypt(
        keys["mult"], caesar.decrypt(keys["caesar"], ah.ALPHABET))
    alphabets.append(list(decrypted_alphabet))
    return alphabets


def brute_force_crack(message):
    results = []
    for caesar_key in range(ah.AMOUNT_OF_LETTERS):
        for multi_key in range(ah.AMOUNT_OF_LETTERS):
            if(caesar.is_valid_key(caesar_key) and mulitplicative_cypher.is_valid_key(multi_key)):
                alphine_key = generate_alphine_key(caesar_key, multi_key)
                decrypted_message = decrypt(alphine_key, message)
                if(engrish.is_english(decrypted_message)):
                    results.append("key: {0}, message: {1}".format(
                        str(alphine_key), decrypted_message))
    return results
