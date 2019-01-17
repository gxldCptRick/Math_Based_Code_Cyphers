import reverse
import caesar
import bacons
import transposition
import word_trasnposition_cipher

import inspect
import console_io as c_io


cyphers = [reverse, caesar, bacons, transposition, word_trasnposition_cipher]
actions = ["Encrypt", "Decrypt"] 

cypher_names = {
    "reverse": 0,
    "caesar": 1,
    "bacon": 2,
    "num_transposition": 3,
    "word_transposition": 4
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
        print(encrypted_output)
    else:
        decrypted_output = None
        parameters = len(inspect.signature(selection.decrypt).parameters)
        if(parameters is 2):
            if(key is None):
                key = c_io.get_input("Enter a key")
            decrypted_output = selection.decrypt(key, message)
        else: 
            decrypted_output = selection.decrypt(message)
        print(decrypted_output)