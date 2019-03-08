import cypher_app.supported_cyphers.caesar as caesar
import cypher_app.supported_cyphers.mulitplicative_cypher as mulitplicative_cypher
import cypher_app.supported_cyphers.helpers.alphabet_helpers as ah
import cypher_app.supported_cyphers.helpers.detect_english as engrish

name = "Alphine Cypher"
key_range = {
    "min": 26,
    "max": 676
}
key_type = "number"
description = """The alphine cypher is a cool little cypher that allows you to combine both a caesars cypher and a multiplicative cypher.
the idea is simple we use a mulitplicative key to change the letter. then you shift it with a caesars shift. and bam you have a stronger encryption
"""

example = """
multiplicative key of: 17
caesar key of: 3
so the alphine key will become
mulitplicative * 26 + caesar = alphine
17 * 26 + 3 = 445
message: stuff

so you do a multiplicative shift with your key
17
stuff -> ulchh
then we apply a caesar shift with the key again
3
ulchh -> xofkk
and so that becomes the encrypted text.
to revert all we need to do is find the mod inverse of 17 
and work with the caesar key again.
3
xofkk -> ulchh
then apply the multiplicative encryption again with the mod inverse of 17 in mod 26 i.e the number such that 7 * number would be congruant to 1 in mod 26
mod inverse of 17 in mod 26
ulchh -> stuff 
and blammo you found the message.

by the way you need to give this program the alphine key and not the seperate keys for the caesar and multiplicative
so what happens is it takes in that number lets say 445 
then what it does is first and foremost mod by 26 and see what the remainder is
in this case 445 % 26 will be 3
and then the program takes the same alphine key and divides by 26 to get the mulitplicative key
ie 445 / 26 = 17 with integer math.
"""


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
