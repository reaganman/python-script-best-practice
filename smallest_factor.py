#! /usr/bin/env python3

'A script for getting the smallest prime factor of an integer.'

import sys

def get_smallest_prime_factor(n):
    """
    Returns the smallest integer that is a factor of `n`.

    If `n` is a prime number `None` is returned.

    Parameters
    ----------
    n : int
        The integer to be factored.

    Returns
    -------
    int or None
        The smallest integer that is a factor of `n`
        or None if `n` is a prime.

    Examples
    --------
    >>> get_smallest_prime_factor(7)
    >>> get_smallest_prime_factor(8)
    2
    >>> get_smallest_prime_factor(9)
    3
    """
    smallest_prime_factor = None
    for i in range(2, n):
        if (n % i) == 0:
            smallest_prime_factor = i
    return smallest_prime_factor

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
    n = int(sys.argv[1])
    if n < 1:
        sys.exit(sys.argv[0] + ": Expecting a positive integer")
    print(get_smallest_prime_factor(n))
