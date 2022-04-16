#################################
#  PROJECT EULER - PROBLEM 012  #
#################################
import time


def get_prime_factors(n: int) -> list[int]:
    """ Returns the list of all prime factors of n.  Determines all necessary
    primes on the fly.  """
    factors = []
    prime_flags = [True] * (n + 1)
    prime_flags[0] = False
    prime_flags[1] = False
    for (p, is_prime) in enumerate(prime_flags):
        if n == 1:
            break
        if is_prime:
            for multiple in range(p * p, n + 1, p):
                prime_flags[multiple] = False
            while n % p == 0:
                factors.append(p)
                n = n // p
    return factors


def divisor_count(n: int) -> int:
    """ Counts the number of divisors of n. """
    list_of_factors = get_prime_factors(n)
    set_of_factors = set(list_of_factors)
    number_of_divisors = 1
    for p in set_of_factors:
        multiplicity_of_p = list_of_factors.count(p)
        number_of_divisors *= multiplicity_of_p + 1
    return number_of_divisors


start = time.time()

""" The triangular numbers are given by n * (n + 1) / 2 for n = 1, 2, ....
Equivalently, they are given by n * (n - 1) / 2 and n * (n + 1) / 2 for n = 2,
4, 6, .... Writing n = 2 * k in the last two formulae, we see that they can be
generated by k * (2 * k - 1) and k * (2 * k + 1) for k = 1, 2, ....

Moreover, the number of divisors of a product of two relatively prime numbers
(such as k and (2 * k +- 1)) is the product of the number of divisors of each
factor. These observations can be used to speed up the computation a bit.  """

N = 500

k = 1
divisors_complement = divisor_count(2 * k - 1)

while True:
    divisors_k = divisor_count(k)
    if divisors_k * divisors_complement > N:
        triangular_number = k * (2 * k - 1)
        break
    """ Notice that 2 * k + 1 = 2 * (k + 1) - 1. This means that, for fixed k,
    instead of computing the number of divisors of (2 * k - 1) and (2 * k + 1),
    we can avoid one computation by anticipating the increment of k to this
    moment, and then calculate the number of divisors of (2 * (k + 1) - 1),
    which will be required anyways when we loop with k + 1. """
    k += 1
    divisors_complement = divisor_count(2 * k - 1)
    if divisors_k * divisors_complement > N:
        triangular_number = (k - 1) * (2 * k - 1)
        # In terms of the 'old' k, this is k * (2 * k + 1).
        break

print(triangular_number)

end = time.time()
print(f"Program runtime: {end - start} seconds")
