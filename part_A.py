"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

from math import sqrt
import numpy as np

# Sequence of numbers
num_lst = [1, 2, 3, 4 , 5] 
 
# 1. Standard deviation using loops 

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x) #length of list

    # accumulate the sum of all numbers in the list
    total_sum = 0  
    total_square_sum = 0 

    # Loop through each number in the list
    for num in x: #iterate over each element in x (num_lst) and assign it to the variable num.
       total_sum += num #sum of the numbers
       total_square_sum += num**2 #sum of the squares of the numbers

    # Compute the mean
    mean = total_sum / N 

    # Compute the mean of squares
    mean_of_squares = total_square_sum / N

    # Compute the variance
    variance = mean_of_squares - mean**2

    # Return the standard deviation (square root of variance)
    return sqrt(variance)

# Call the function and print the standard deviation
std_dev = std_loops(num_lst)
print("Standard Deviation: ", std_dev)


# 2. Standard deviation using Pyton's built-in functions
def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x)

    # Compute the mean
    mean = sum(x) / N

    # Compute the mean of squares
    mean_of_squares = sum(map(lambda num: num**2, x)) / N #map() function applies the function to each element of the list, and lambda num: num**2 takes the argument (num) and returns its square(num**2)

    # Compute the variance
    variance = mean_of_squares - mean**2

    # Return the standard deviation (square root of variance)
    return sqrt(variance)

# Call the function and print the standard deviation 
std_dev = std_builtin(num_lst)
print("Standard Deviation: ", std_dev)


# 3. Standard deviation using NumPy
def std_numpy(x): 
    return np.std(x)

# Call the function and print the Standard Deviation
std_dev = std_numpy(num_lst)
print("Standard Deviation: ", std_dev)
