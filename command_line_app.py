import cyphers
import console_io as c_io
import os
import transposition
import detect_english

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def app():
    running = True
    menu_options = ["Encryptor, Decryptor", "Brute Force Key Finder", "Alphabet Generator", "Alphine Key Helper"]
    while(running): 
        choice = c_io.menu_selection(menu_options, with_quit=True)
        if(choice > 0):
            if(choice is 1):
                running = encryptor_decryptor()
            elif(choice is 2):
                running = brute_force_finder()
            elif(choice is 3):
                running = generate_alphabet()
            elif(choice is 4):
                running = key_generator()
        else: 
            running = False
            cls()
            print("Goodbye....")
            

def brute_force_finder():
    applicable_cyphers = cyphers.brute_force_cyphers
    opts = list(map(cyphers.get_name, applicable_cyphers))
    selection = c_io.menu_selection(opts, True)
    if(selection > 0):
        selection -= 1
        message = c_io.get_input("Please Enter Message To Decrypt")
        possible_choices = applicable_cyphers[selection].brute_force_crack(message)
        for possible_choice in possible_choices:
            print(possible_choice)
        pause()
    else:
        cls()
    
    
    return True

def encryptor_decryptor():
    cypher_names = list(map(cyphers.get_name, cyphers.cyphers))
    running = True
    selection = c_io.menu_selection(cypher_names, True)
    if(selection > 0):
        selection -= 1
        action = c_io.menu_selection(cyphers.actions) - 1
        user_input = c_io.get_input("Enter a Message", False);
        was_valid_input = False
        while(not was_valid_input):
            try:
                message = cyphers.do_action_based_on_cypher(cyphers.cyphers[selection], cyphers.actions[action], message=user_input)
                print(message)
                was_valid_input = True
            except AssertionError as error:
                print(error)
        pause()
    else:
        cls()
    return running

def generate_alphabet():
    running = True
    generators = list(map(cyphers.get_name, cyphers.alphabet_generators))
    selection = c_io.menu_selection(generators, True)
    key_is_valid = False
    while(not key_is_valid and selection is not 0):
        try:
            cypher = cyphers.alphabet_generators[selection]
            min = cypher.key_range["min"]
            max = cypher.key_range["max"]
            if max is None:
                pass
            key = c_io.get_int_input("Enter A Key", min, max)
            alphabets = cypher.generate_alphabet(key)
            key_is_valid = True
            for alphabet in alphabets:
                print(alphabet)
            pause()
        except AssertionError as e:
            print("The Key entered is not valid for the given cypher please try again.")
    cls()
    return running

def pause():
    input("Press Enter To Continue...")
    cls()

def key_generator():
    running = True
    options = ["Generate Alphine" , "Break Down Alphine"]
    selection = c_io.menu_selection(options, True)
    if selection is 1:
        mult_key = c_io.get_int_input("Enter Multiplicative Key", 1, 25)
        while(mult_key % 2 == 0 or mult_key % 13 == 0):
            print("That is not a valid Multiplicative Key.")
            mult_key = c_io.get_int_input("Enter Multiplicative Key", 1, 25)
        caesar_key = c_io.get_int_input("Enter Caesar Key", 1, 25)
        print("Alphine Key:", mult_key * 26 +  caesar_key)
        pause()
    elif selection is 2:
        cypher = cyphers.cyphers[cyphers.cypher_names["alphine"]]
        alphine_key = c_io.get_int_input("Enter Alphine Key", cypher.key_range["min"], cypher.key_range["max"])
        print(cypher.generate_keys(alphine_key))
        pause()
    elif selection is 0:
        cls()
    return running
