"""
Input data: an arbitrary, greater than zero quantity of arguments
Arguments may be a numbers or a strings, that may contain numbers and letters
without spaces

Output: a string, that consisiting of recieved values in reversible order,
recorded through a gap. The space in the end of string is absent.

"""


import sys
user_input = sys.argv[1:]

user_input = user_input[::-1]
user_input = " ".join(user_input)
print user_input




