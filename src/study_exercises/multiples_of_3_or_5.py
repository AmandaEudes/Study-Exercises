# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1.000.

# https://projecteuler.net/problem=1


def multiples_of_3_or_5(value: int) -> int:
    """Calculate the sum of all the multiples of 3 or 5 below a natural number.

    Args:
        value (int): natural number

    Returns:
        int: the sum
    """
    total = 0
    if value >= 3:
        for i in range(1, value):
            if i % 3 == 0 or i % 5 == 0:
                total += i
    return total
