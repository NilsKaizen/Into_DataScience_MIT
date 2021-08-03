###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """
    # Sort eggs weights
    eggs = sorted(egg_weights, reverse=True)
    w = target_weight
    c_eggs = 0
    e_d = {}

    for egg in eggs:
        n_eggs = 0
        while True:
            if(n_eggs*egg <= w):
                n_eggs += 1
            else:
                n_eggs -= 1
                break

        w -= n_eggs*egg
        c_eggs += n_eggs
        e_d[egg] = n_eggs

        if w == 0:
            break
    print(e_d)
    return c_eggs
    pass


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 26
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 26")
    print("Expected ouput: 2 (25 + 1 = 26)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    n = 100
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 100")
    print("Expected ouput: 4 (4 * 25 = 100)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    n = 7
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 7")
    print("Expected ouput: 3 (1 * 5 + 2 * 1 = 100)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    n = 101
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 101")
    print("Expected ouput: 5 (4 * 25 + 1 * 1 = 100)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    egg_weights = (1, 5, 10, 20)
    n = 99
    print("Egg weights = ", egg_weights)
    print("n = ", n)
    print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n, {}))
    print()

    n = 100
    print("Egg weights = ", egg_weights)
    print("n = ", n)
    print("Expected ouput: 5 (5 * 20 = 100)")
    print("Actual output:", dp_make_weight(egg_weights, n, {}))
    print()
