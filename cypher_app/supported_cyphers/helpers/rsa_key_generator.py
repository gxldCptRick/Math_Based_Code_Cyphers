import cypher_app.supported_cyphers.helpers.crypto_math as crypto_math
import sys
import os


def generate_key(size_in_bits):
    p = crypto_math.generate_prime_number(size_in_bits)
    q = crypto_math.generate_prime_number(size_in_bits)
    n = p * q
    found_relatively_prime_number = False
    upper_bound = 2 ** size_in_bits
    lower_bound = 2 ** (size_in_bits - 1)
    mod_base = (p - 1) * (q - 1)
    e = None
    while not found_relatively_prime_number:
        e = crypto_math.random.randrange(lower_bound, upper_bound)
        remainder_of_e = crypto_math.greatest_common_divisor(e, mod_base)
        found_relatively_prime_number = remainder_of_e == 1
    d = crypto_math.calculate_mod_inverse(e, mod_base)
    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)


def generate_key_dictionary(key_size_in_bits):
    public, private = generate_key(key_size_in_bits)
    return {
        "public": public,
        "private": private
    }


def write_key_to_file(file_object, key_size, key):
    n, d_or_e = key
    file_object.write('%s,%s,%s' % key_size, n, d_or_e)


def generate_key_files(file_name, key_size_in_bits):
    public_file_name = "%s_pub_key.rsa" % file_name
    private_file_name = "%s_priv_key.rsa" % file_name
    warn_if_override(public_file_name)
    warn_if_override(private_file_name)
    public_key, private_key = generate_key(key_size_in_bits)
    with open(public_file_name, 'w') as public_file:
        write_key_to_file(public_file, key_size_in_bits, public_key)
    with open(private_file_name, 'w') as private_file:
        write_key_to_file(private_file, key_size_in_bits, private_key)


def warn_if_override(file_path):
    if(os.path.exists(file_path)):
        print('File Name: %s will be overriden' % file_path)
