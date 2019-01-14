import reverse
import caesar
import bacons
import transposition
import word_trasnposition_cipher

import inspect
import console_io as c_io


cyphers = [reverse, caesar, bacons, transposition, word_trasnposition_cipher]
actions = ["Encrypt", "Decrypt"] 
def get_name(obj):
    return obj.name

def validate_inputs(selection, action):
    if(selection is None):
        raise AssertionError("selection cannot be set to None.")
    if(action is None):
        raise AssertionError("action cannot be None.")
    if(type(selection) is not int):
        raise AssertionError("selection must be an integer.")
    if(type(action) is not int):
        raise AssertionError("action must be an integer.")
    if(action > 2 or action < 1):
        raise AssertionError("action must be between 1 and 2.")
    if(selection > len(cyphers) or selection < 0):
        raise AssertionError("selection must be between 0 and the length of the cyphers array")

def do_action_based_on_cypher(selection, action, message=None, key=None):
    validate_inputs(selection, action)
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