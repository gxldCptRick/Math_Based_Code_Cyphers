import cyphers
import console_io as c_io
import os
import transposition

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def app():
    running = True
    menu_options = ["Encryptor, Decryptor", "Brute Force Finder"]
    while(running): 
        choice = c_io.menu_selection(menu_options, with_quit=True)
        if(choice > 0):
            if(choice is 1):
                running = encryptor_decryptor()
            elif(choice is 2):
                running = brute_force_finder()
        else: 
            running = False
def brute_force_finder():
    user_input = c_io.get_input("Enter message to brute force")    
    pass

def encryptor_decryptor():
    cypher_names = list(map(cyphers.get_name, cyphers.cyphers))
    running = True
    selection = c_io.menu_selection(cypher_names, True)
    if(selection > 0):
        selection -= 1
        action = c_io.menu_selection(cyphers.actions)
        action -= 1
        user_input = c_io.get_input("Enter a Message", False);
        was_valid_input = False
        while(not was_valid_input):
            try:
                cyphers.do_action_based_on_cypher(cyphers.cyphers[selection], cyphers.actions[action], message=user_input)
                was_valid_input = True
            except AssertionError as error:
                print(error)
            input("Press Enter To Continue")
            cls()
    else:
        running = False
    return running