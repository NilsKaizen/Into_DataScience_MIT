# SCORE = (60 - (a+b+c+d+e))*F + a*ps1 + b*ps2 + c*ps3 + d*ps4 + e*ps5
import random

# class Variable(object):

#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

#     def getvalue(self):
#         return self.value

#     def getName(self):
#         retunr = self.name

#     def __str__(self):
#         return (self.name, self.value)


# Algoritm Used: BRUTE FORCE
# Number of operations: O(2**n - n + 1) with n = number of variables


def createVConst(i, j):
    """ Creates a list of 6 random values
    between i and j both included"""
    v_const = [random.randint(i, j) for x in range(6)]
    return v_const


def setConstants(v_const):
    """ Creates a dictionary of constants with 
    key = temp and value = v_const"""

    temp = ['F', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5']
    constants = {}

    if len(temp) == len(v_const):
        for i in range(len(v_const)):
            constants[temp[i]] = int(v_const[i])
        return constants
    else:
        return 0


def setVariables(v_var):
    """ Creates a dictionary of variables with 
    key = temp and value = v_var"""

    temp = ['a', 'b', 'c', 'd', 'e']
    var = {}

    if len(temp) == len(v_var):
        for i in range(len(v_var)):
            var[temp[i]] = int(v_var[i])
        return var
    else:
        return 0


def testCombination(c, v):
    """Having the constants and 
    the variables calculate the score"""

    print('With the constants: ')
    print(c)
    print('And the variables: ')
    print(v)

    score = (60 - (v['a']+v['b']+v['c']+v['d']+v['e']))*c['F'] + v['a']*c['ps1'] + \
        v['b']*c['ps2'] + v['c']*c['ps3'] + v['d']*c['ps4'] + v['e']*c['ps5']

    print('The score is: {}'.format(score))
    print('\n')
    print('\n')
    return (score, v)


# Create random constants
c = setConstants(createVConst(1, 100))

# Use your own constants
# c = setConstants([2,3,4,5,6,7])


def bestCombination(toConsider, avail, v={}):
    """ Brute Force Search for the Values that maximize the score 
    using a Tree decision"""

    # Checks wether the avail is negative
    if avail < 0:
        avail = 0

    # You arrived to the end of the branch, leaf and return the result
    if toConsider == []:
        result = testCombination(c, v)

    # Checks if you are still into the Constrain a+b+c+d+e >= 20
    elif len(toConsider)*10 < avail:
        result = (0, {})
    else:
        # Set the letter and the dictionary of variables
        temp = ['a', 'b', 'c', 'd', 'e']
        letter = temp[-len(toConsider)]
        vfor10 = v.copy()
        vfor10[letter] = 10

        # Inspect the LEFT branch
        score10, v10 = bestCombination(toConsider[1:], avail-10, vfor10)

        vfor0 = v.copy()
        vfor0[letter] = 0

        # Inspect the RIGHT branch
        score0, v0 = bestCombination(toConsider[1:], avail, vfor0)

        # Compare two branches and select the Winner
        if score10 > score0:
            print('Evaluating {} with {}'.format(score10, v10))
            print('And {} with {}'.format(score0, v0))
            print('\n')
            result = (score10, v10)
        else:
            result = (score0, v0)

    print('Wins {}'.format(result))
    print('\n')
    print('\n')
    return result


# The number of "1" are the 5 variables
print(bestCombination([1, 1, 1, 1, 1], 20))
