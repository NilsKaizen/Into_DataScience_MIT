###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import pandas as pd

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    with open(filename) as f:
        data = f.read()
        
        # Create a list of cows
        cow_data = data.split('\n')
        
        # Create a dict of cow name and weight
        c_data_dict = {cow.split(',')[0] : int(cow.split(',')[1]) for cow in cow_data}
        f.close()
    return c_data_dict

# Problem 2


def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    
    c_sort = sorted(cows.items(), key= lambda item: item[1], reverse=True)
    
    # Trips and cows
    t_a_c = []
    
    # List of cows
    c_list = []
    
    # Limit
    l = limit
    
    # Reset and create new list
    def reset(): 
 
        l = limit
        t_a_c.append(c_list.copy())

        c_list.clear()
        
    def add_cow(l):

        temp = c_sort.copy()
        for cow in temp: 

            if int(cow[1]) <= l:
                
                c_list.append(c_sort.pop(c_sort.index(cow)))
                l -= int(cow[1])
                try:
                    # Check if the smallest cow can fit, otherwise break the loop
                    if int(c_sort[-1][1]) > l: break
                except: 
#                     print('no more cows')
                    pass
                    
        
    while len(c_sort) > 0:
        add_cow(l)
        reset()
   

    return t_a_c

# Problem 3


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Make a copy of the data
    cows_data = cows.copy()
    
    # Create an exeption to get out of all loops
    class GetOutOfLoop( Exception ):
        pass
    
    # All combinations of trips that are below or equal the limit
    trips_to_check = []
    
    def check_trips(trips):
        try: 
            for trip in trips:
                total = 0
                for cow in trip: 
                    total += int(cow[1])
                    # if one of the trips is over weight the trips won't be saved
                    if total > limit: 
                        raise GetOutOfLoop
        except GetOutOfLoop:
            return 0
        return 1
            
    i=0
    for trips in get_partitions(cows_data.items()):
        i +=1
        if check_trips(trips) == 1:
            trips_to_check.append(trips)
    print(i)
    return min(trips_to_check, key= len)

# Problem 4


def compare_cow_transport_algorithms(cows, limit=10):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    g_start = time.time()
    r_greedy = greedy_cow_transport(cows, limit)
    g_end = time.time()
    b_start = time.time()
    r_brute = brute_force_cow_transport(cows, limit)
    b_end = time.time()
    
    g_time = g_end - g_start
    b_time = b_end - b_start
    
    dict_results = {'Algorithm': ['Greedy', 'Brute Force'],
                      'Time': [g_time, b_time],
                      'Trips': [len(r_greedy), len(r_brute)],
                       'Result': [r_greedy, r_brute]}
    df = pd.DataFrame(dict_results, columns = ['Algorithm', 'Time', 'Trips', 'Result'])
    return df
    
#     print('Comparation of two algorithms: ')
#     print('Greedy got: ' + str(len(r_greedy)) + ' trips')
#     print(r_greedy)
#     print(' ')
#     print('Brute got: ' + str(len(r_brute)) + ' trips')
#     print(r_brute)

compare_cow_transport_algorithms(load_cows('ps1_cow_data.txt'), 10)