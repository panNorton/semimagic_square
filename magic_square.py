import numpy as np
import random


def semimagic_square(n, s):
    if n <= s:
        square = create_square(n, s)
        return square
    else:
        print("When n > s, construction of a semimagic square is impossible.")


def create_square(n, s):
    """
    Creates semimagic square based on n (matrix size) and s - sum of elements 
    of rows and columns
    """
    nums = constrained_sum_sample(n, s, 'pos')
    square = fill_square_values(nums)
    if min(nums) > 2:
        diffs = constrained_sum_sample(n, 0, 'rand')
        square = diff_square(rearrange_rows(square), diffs, n)
    elif min(nums) == 2:
        diffs = constrained_sum_sample(n, 0, 'ones')
        square = diff_square(rearrange_rows(square), diffs, n)
    return square


def fill_square_values(nums):
    """
    Fills square values with numbers creating a latin square
    """
    n = len(nums)
    square = np.zeros((n, n), dtype=np.int)
    for i in range(0, n):
        for j in range(0, n):
            square[i, j] = nums[(i + j) % n]
    return square


def constrained_sum_sample(n, s, dtype):
    """
    Returns a sample of random numbers
    """
    if dtype == 'pos':
        nums = sorted(random.sample(range(1, s), n - 1))
        return [a - b for a, b in zip(nums + [s], [0] + nums)]
    elif dtype == 'rand':
        nums = random.sample(range(0, n), n - 1)
        return [a - b for a, b in zip(nums + [s], [0] + nums)]
    elif dtype == 'ones':
        nums = [random.randint(0, 1) for i in range(n - 1)]
        return [a - b for a, b in zip(nums + [s], [0] + nums)]


def rearrange_rows(square):
    """
    Changes the order of rows 1 -> n, 2 -> n-1, ...
    """
    perm = np.arange(len(square) - 1, -1, -1)
    i = np.argsort(perm)
    square = square[i, :]
    return square


def diff_square(square, diffs, n):
    """
    Adds random noise to the latin square
    """
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            square[i, j] = square[i, j] + diffs[(i + j) % n]
    return square


print(semimagic_square(5, 6))
print(semimagic_square(7, 134))
print(semimagic_square(100, 56789))
