import io
import re
import os

file_regex = re.compile(
    r"(^[A-Za-z]{1}[:]\\[a-zA-Z\s]*[\\]{0}([\sA-Za-z\\]*|[]|[.]{1}[a-zA-z]+))")
Default_Block_Size = 128
Byte_Size = 256


def encrypt(path, message, block_size=Default_Block_Size):
    if(not os.path.isfile(path)):
        raise AssertionError(
            'The Key must be a file path to load the actual stuff from god....\ngod help us all....')
    key_size, n, e = read_key_file(path)
    encrypted_blocks = encrypt_message_to_blocks(message, (n, e), block_size)
    encrypted_message = ','.join(map(lambda e: str(e), encrypted_blocks))
    return "%s_%s_%s" % (len(message), block_size, encrypted_message)


def encrypt_message_to_blocks(message, key, block_size=Default_Block_Size):
    encrypted_blocks = []
    n, e = key
    for block in get_blocks_for_message(message, block_size):
        encrypted_blocks.append(pow(block, e, n))
    return encrypted_blocks


def get_blocks_for_message(message, block_size=Default_Block_Size):
    message_bytes = message.encode('ascii')
    blocks = []
    for block_start in range(0, len(message_bytes), block_size):
        block = 0
        block_end = min(block_start + block_size, len(message_bytes))
        for index in range(block_start, block_end):
            block += message_bytes[index] * (Byte_Size ** (index % block_size))
        blocks.append(block)
    return blocks


def decrypt(path, message_path, block_size=Default_Block_Size):
    if(not os.path.isfile(path)):
        raise AssertionError(
            'The Key must be a file path to load the actual stuff from god....\ngod help us all....')
    if(not os.path.isfile(message_path)):
        raise AssertionError('The Message must also be a path')
    key_size, n, d = read_key_file(path)
    message_length, block_size, message = read_message_file(message_path)
    if key_size < block_size:
        raise AssertionError('key_size was smaller than the block_size')
    message_blocks = map(lambda e: int(e), message.split(','))
    return decrypt_message_blocks(message_blocks, message_length, (n, d), block_size)


def decrypt_message_blocks(message_blocks, message_length, key, block_size=Default_Block_Size):
    n, d = key
    decrypted_block = map(lambda e: pow(e, d, n), message_blocks)
    return turn_block_into_text(decrypted_block, message_length, block_size)


def turn_block_into_text(blocks, message_length, block_size=Default_Block_Size):
    message = []
    for block in blocks:
        block_message = []
        for index in range(block_size - 1, -1, -1):
            if (len(message) + index < message_length):
                block_offset = Byte_Size ** index
                ascii_number = block // block_offset
                block %= block_offset
                block_message.insert(0, chr(ascii_number))
        message.extend(block_message)
    return ''.join(message)


def read_key_file(path):
    key_data = None
    with io.open(path) as file:
        key_data = file.read()
    key_length, n, d_or_e = key_data.split(',')
    return (int(key_length), int(n), int(d_or_e))


def read_message_file(path):
    message_data = None
    with io.open(path) as file:
        message_data = file.read()
    message_length, block_size, encrypted_message = message_data.split('_')
    return (int(message_length), int(block_size), encrypted_message)


if __name__ == "__main__":
    encrypt(input("input path to file"), None)
