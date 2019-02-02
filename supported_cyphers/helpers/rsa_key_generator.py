import supported_cyphers.helpers.crypto_math as crypto_math
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


def genereate_key_files(file_name, key_size_in_bits):
    pass
