import cypher_app.supported_cyphers.reverse as reverse
import cypher_app.supported_cyphers.caesar as caesar
# import cypher_app.supported_cyphers.bacons as bacons
import cypher_app.supported_cyphers.word_trasnposition_cipher as word_trasnposition_cipher
import cypher_app.supported_cyphers.transposition as transposition
import cypher_app.supported_cyphers.mulitplicative_cypher as mulitplicative_cypher
import cypher_app.supported_cyphers.alphine_cypher as alphine_cypher
import cypher_app.supported_cyphers.polyalphabetic_cypher as vig
import cypher_app.supported_cyphers.rsa_cypher as rsa
import inspect
import cypher_app.command_line.console_io as c_io
import cypher_app.supported_cyphers.caesar_word_cypher as caesar_word
import cypher_app.command_line.tools as tools

cyphers = [reverse, caesar, transposition,
           word_trasnposition_cipher, mulitplicative_cypher, alphine_cypher, vig, caesar_word]
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
    output = None
    attr = "encrypt" if action == actions[0] else "decrypt"
    if (tools.file_regex.match(message) is None):
        do_action(selection, message, attr, key)
    else:
        with open(message, 'r') as file:
            content = file.read().split('\n')
            part = []
            for c in content:
                part.append(do_action(selection, c, attr, key))
        output = '\n'.join(part)
    return output


def do_action(cypher, message, attr, key=None):
    method = getattr(cypher, attr)
    parameters = len(inspect.signature(method).parameters)
    output = None
    if(parameters is 2):
        if(key is None):
            key = c_io.get_input("Enter a key")
        output = method(key, message)
    else:
        output = method(message)
    return output
