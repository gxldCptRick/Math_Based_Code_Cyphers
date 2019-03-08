import cypher_app.command_line.console_io as c_io


def brute_force_message(message):
    character_count = count_characters(message)
    frequencies = generate_character_frequencies(character_count, len(message))
    # best guess at substitution
    # substitute the string


def count_characters(message):
    character_count = {}
    for c in message:
        c = c.upper()
        if(c.isalpha()):
            if(c in character_count.keys()):
                character_count[c] += 1
            else:
                character_count[c] = 1
    return character_count


def generate_character_frequencies(character_counts, message_length):
    pass


if __name__ == '__main__':
    message = c_io.get_input("Enter A Message to analyize")
    print(count_characters(message))
