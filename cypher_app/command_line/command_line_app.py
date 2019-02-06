import cypher_app.cyphers as cyphers
import cypher_app.command_line.console_io as c_io
import os
import cypher_app.supported_cyphers.rsa_cypher as rsa
import cypher_app.supported_cyphers.helpers.rsa_key_generator as rsa_gen
import cypher_app.command_line.tools as tools


def file_filter(e):
    return tools.file_regex.match(e)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def app():
    running = True
    menu_options = ["Encryptor, Decryptor", "Brute Force Key Finder",
                    "Alphabet Generator", "Alphine Key Helper", "Decrypt, Encrypt Files", "Work With RSA"]
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
            elif(choice is 5):
                running = do_file_encryption()
            else:
                running = rsa_encrypter()
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
        possible_choices = applicable_cyphers[selection].brute_force_crack(
            message)
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
        user_input = c_io.get_input("Enter a Message", False)
        was_valid_input = False
        while(not was_valid_input):
            try:
                message = cyphers.do_action_based_on_cypher(
                    cyphers.cyphers[selection], cyphers.actions[action], message=user_input)
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
            selection -= 1
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
    options = ["Generate Alphine", "Break Down Alphine"]
    selection = c_io.menu_selection(options, True)
    if selection is 1:
        mult_key = c_io.get_int_input("Enter Multiplicative Key", 1, 25)
        while(mult_key % 2 == 0 or mult_key % 13 == 0):
            print("That is not a valid Multiplicative Key.")
            mult_key = c_io.get_int_input("Enter Multiplicative Key", 1, 25)
        caesar_key = c_io.get_int_input("Enter Caesar Key", 1, 25)
        print("Alphine Key:", mult_key * 26 + caesar_key)
        pause()
    elif selection is 2:
        cypher = cyphers.cyphers[cyphers.cypher_names["alphine"]]
        alphine_key = c_io.get_int_input(
            "Enter Alphine Key", cypher.key_range["min"], cypher.key_range["max"])
        print(cypher.generate_keys(alphine_key))
        pause()
    elif selection is 0:
        cls()
    return running


def rsa_encrypter():
    cls()
    running = False
    options = ["Decrypt/Encrypt with RSA", "Generate RSA keys",
               "Bulk Encryption With Unique Keys"]
    option = c_io.menu_selection(options, True)
    if(option != 0):
        running = True
        if(option == 1):
            options = ["Encrypt Message to file", "Decrypt File to message"]
            option = c_io.menu_selection(options)
            if(option == 1):
                encrypt_with_rsa()
            else:
                decrypt_with_rsa()
        elif(option == 2):
            generate_keys()
        else:
            do_bulk_rsa()
    pause()
    return running


def encrypt_with_rsa():
    pub_keys = tools.get_all_public_keys()
    if(len(pub_keys) > 0):
        print("Select the public key to encrypt with.")
        choice = c_io.menu_selection(pub_keys) - 1
        message_to_encrypt = c_io.get_input("Enter any message to encrypt")
        encrypted_message = rsa.encrypt(pub_keys[choice], message_to_encrypt)
        path_to_save_to = c_io.get_input(
            "Enter the File name to save the encrypted message", filter=file_filter)
        with open(path_to_save_to, 'w') as message_file:
            message_file.write(encrypted_message)
    else:
        print("No Public keys found")


def decrypt_with_rsa():
    priv_keys = tools.get_all_private_keys()
    if(len(priv_keys) > 0):
        choice = c_io.menu_selection(priv_keys) - 1
        path_to_message = c_io.get_input(
            "Enter the file path to the message", filter=file_filter)
        decrypted_message = rsa.decrypt(priv_keys[choice], path_to_message)
        print(decrypted_message)
    else:
        print("No private keys found")


def generate_keys():
    file_name = c_io.get_input("Enter File Name For Keys")
    key_size_in_bits = c_io.get_int_input(
        "Enter a Key Size[in bits]", 2, 10000)
    rsa_gen.generate_key_files(file_name, key_size_in_bits)


def resolve_file_name(file_name):
    if(not file_filter(file_name)):
        file_name = "%s.txt" % file_name
    return file_name


def do_bulk_rsa():
    message_file = c_io.get_input(
        "Enter file with messages", filter=file_filter)
    text = tools.read_in_file(message_file)
    files = tools.get_all_public_keys()
    if(len(files) > 0):
        for block in text:
            print("Text to encrypt")
            print(block)
            print("Select a key to encrypt message above\n")
            choice = c_io.menu_selection(files)
            save_name = c_io.get_input("What should i name the file?")
            save_name = resolve_file_name(save_name)
            encrypted_message = rsa.encrypt(files[choice - 1], block)
            with open(save_name, 'w') as file:
                file.write(encrypted_message)
    else:
        print("You must have some public keys in the current directory")


def check_if_file_exists(file_name):
    file_name = resolve_file_name(file_name)
    return os.path.exists(file_name)


def do_file_encryption():
    cypher_names = list(map(cyphers.get_name, cyphers.cyphers))
    running = True
    selection = c_io.menu_selection(cypher_names, True)
    if(selection > 0):
        selection -= 1
        action = c_io.menu_selection(cyphers.actions) - 1
        message_file = c_io.get_input(
            "Enter a Message File", filter=check_if_file_exists)
        message_file = resolve_file_name(message_file)
        message = cyphers.do_action_based_on_cypher(
            cyphers.cyphers[selection], cyphers.actions[action], message_file)
        with open("%s_%s" % (cyphers.actions[action], message_file), 'w') as file:
            file.write(message)
        pause()
    cls()
    return running
