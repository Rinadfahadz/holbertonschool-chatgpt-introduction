#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Recursively computes the factorial of a non-negative integer n.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of n. By definition, factorial(0) returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from command line arguments
f = factorial(int(sys.argv[1]))

# Print the computed factorial
print(f)

