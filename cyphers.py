import supported_cyphers.reverse as reverse
import supported_cyphers.caesar as caesar
import supported_cyphers.bacons as bacons
import supported_cyphers.word_trasnposition_cipher as word_trasnposition_cipher
import supported_cyphers.transposition as transposition
import supported_cyphers.mulitplicative_cypher as mulitplicative_cypher
import supported_cyphers.alphine_cypher as alphine_cypher
import supported_cyphers.polyalphabetic_cypher as vig
import inspect
import console_io as c_io


cyphers = [reverse, caesar, bacons, transposition,
           word_trasnposition_cipher, mulitplicative_cypher, alphine_cypher, vig]
actions = ["Encrypt", "Decrypt"]
alphabet_generators = [caesar, mulitplicative_cypher, alphine_cypher]
brute_force_cyphers = [transposition, caesar,
                       mulitplicative_cypher, alphine_cypher]

brute_force_names = {
    "num_transposition": 0,
    "word_transposition": 1,
    "caesar": 2,
    "multiply": 3,
    "alphine": 4
}


alpha_generators_names = {
    "caesar": 0,
    "multiply": 1,
    "alphine": 2
}

cypher_names = {
    "reverse": 0,
    "caesar": 1,
    "bacon": 2,
    "num_transposition": 3,
    "word_transposition": 4,
    "multiply": 5,
    "alphine": 6
}


def get_name(obj):
    return obj.name


def do_action_based_on_cypher(selection, action, message=None, key=None):
    if(action in actions[0]):
        parameters = len(inspect.signature(selection.encrypt).parameters)
        encrypted_output = None
        if(parameters is 2):
            if(key is None):
                key = c_io.get_input("Enter a key")
            encrypted_output = selection.encrypt(key, message)
        else:
            encrypted_output = selection.encrypt(message)
        return encrypted_output
    else:
        decrypted_output = None
        parameters = len(inspect.signature(selection.decrypt).parameters)
        if(parameters is 2):
            if(key is None):
                key = c_io.get_input("Enter a key")
            decrypted_output = selection.decrypt(key, message)
        else:
            decrypted_output = selection.decrypt(message)
        return decrypted_output
