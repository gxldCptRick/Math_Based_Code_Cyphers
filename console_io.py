def menu_selection(menu_options, with_quit=False):
    if(type(with_quit) is not bool):
        raise AssertionError("with_quit must be a boolean.")
    if(type(menu_options) is not list):
        raise AssertionError("menu_options must be of type array.")
    lower_bound = 1
    upper_bound = len(menu_options)
    menu_options = list(menu_options)
    if(with_quit):
        lower_bound = 0
        menu_options.insert(lower_bound, "Quit");
    for index, option in enumerate(menu_options):
        if(not with_quit):
            print(index + 1, ")", option)
        else:  
            print(index, ")", option)
    message = "Enter A Number Between " + str(lower_bound) +  '-'+ str(upper_bound)
    is_valid_input = False
    return get_int_input(message, lower_bound, upper_bound)
    
    
def get_int_input(message, min, max):
    if(min > max):
        raise AssertionError("min cannot be greater than the max.s")
    input_is_valid = False
    actual_int = None
    while(not input_is_valid):
        try:
            user_input = get_input(message+" ("+str(min)+"-"+str(max)+")").strip()
            actual_int = int(user_input)
            input_is_valid = actual_int >= min and actual_int <= max
        except RuntimeError:
            print("Please input an actual number")
    return actual_int


def prompt_for_bool(message, true_string, false_string):
    output = message + "(" + true_string + ","+ false_string+ ")" + ": "
    user_input = get_input(output)
    while(user_input.upper() not in true_string.upper() and user_input.upper() not in false_string.upper()):
        user_input = input(output)
    return user_input.upper() in true_string.upper()


def get_input(message, allow_empty=False):
    is_valid_input = False
    user_input = None
    while(not is_valid_input):
        user_input = input(message + ": ").strip()
        is_valid_input = allow_empty or (not allow_empty and user_input not in '')
    return user_input