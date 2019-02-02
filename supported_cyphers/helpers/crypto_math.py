# import math
import random
Low_Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
              449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
Default_Max_Trails = 5


def is_number_prime(test_case):
    is_prime = False
    if(test_case >= 2):
        is_prime = test_case in Low_Primes
        if(not is_prime):
            if(len(list(filter(lambda e: test_case % e == 0, Low_Primes))) is 0):
                is_prime = rabin_miller_test(test_case)
    return is_prime


def rabin_miller_test(test_case, amount_of_trials=Default_Max_Trails):
    is_prime = False
    s = test_case - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1
    for trails in range(amount_of_trials):
        a = random.randrange(2, test_case - 1)
        v = pow(a, s, test_case)
        if v is not 1:
            i = 0
            while v != (test_case - 1):
                if i is not (t - 1):
                    is_prime = True
                    i += 1
                    v = (v ** 2) % test_case
                else:
                    is_prime = False
                    break
        if not is_prime:
            break
    return is_prime


def generate_prime_number(size_in_bits):
    if(size_in_bits < 2):
        raise AssertionError(
            'There is no such prime number that can be represented with less than 2 bits')
    prime_is_found = False
    num = None
    while(not prime_is_found):
        num = random.randrange(2 ** (size_in_bits - 1), 2 ** (size_in_bits))
        prime_is_found = is_number_prime(num)
    return num
