# coding:utf-8
'''
Some ways to index into Numpy arrays
'''

import numpy as np

# Slicing indexing
# Create the following rank 2 array with shape (3,4)
# [[1  2  3  4]
#  [5  6  7  8]
#  [9  10 11 12]]
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2,2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array
print a[0,1]  # Prints "2"
b[0, 0] = 55  # b[0, 0] is the same piece of data as a[0, 1]
print a[0, 1] # Prints "55"

a[0, 1] =2


# Integer array indexing
# The returned array will have shape(3,)
print a[[0, 1 , 2], [2, 3, 2]]   # Prints "[ 3 8 11]"

# The above example of integer array indexing is equivalent to this:
print np.array([a[0, 2], a[1, 3], a[2, 2]]) # Prints "[ 3 8 11]"

# When using integer array indexing, you can reuse the same
# element from the source array:
print a[[0, 0], [1, 1]]		# Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print np.array([a[0, 1], a[0,1]])  # Prints "[2 2]"

# Boolean array indexing
bool_idx = (a > 3)  # Find the elements of a that are bigger than 3;
					# this returns a numpy array of Boolean of the same
					# shape as a, where each slot of bool_idx tells
					# whether that element of a is > 2
print bool_idx      # Prints "[[False False False True]"
					#		   [ True  True  True True]
					#		   [ True  True  True True]]

# We use boolean array indexing to construct a rank 1 array
# consisiting of the elements of a corresponding to the True values
# of bool_idx
print a[bool_idx]	# Prints "[ 4 5 6 7 8 9 10 11 12]"

# We can do all of the above in a single concise statement:
print a[a > 3]		# Prints "[ 4 5 6 7 8 9 10 11 12]"