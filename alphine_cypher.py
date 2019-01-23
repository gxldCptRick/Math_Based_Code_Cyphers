import caesar
import mulitplicative_cypher
import alphabet_helpers as ah

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
        raise AssertionError('The alphine Key must have a valid multiplicative key')
    return {
        "mult": mult_key,
        "caesar": caesar_key
        }

def generate_alphabet(key):
    keys = generate_keys(key)
    alphabets = mulitplicative_cypher.generate_alphabet(keys["mult"])
    for index in range(ah.AMOUNT_OF_LETTERS):
        alphabets[1][index] = caesar.encrypt(keys["caesar"], alphabets[1][index])
        alphabets[2][index] = caesar.encrypt(keys["caesar"], alphabets[2][index])
    return alphabets
