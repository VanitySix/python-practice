import sys
'''
commonset.py

● IMPORTANT
a. Your autotest cases will NOT work if you don’t load your sys.argv like
below. For this assignment, load in your variables like this:
set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']
b. The above set_a is a list-type variable which contains words.
c. Your order may be different for the examples below because sets are
unordered.

● Create a program, commonset.py. Your program should:
a. Find the common words between set_a and set_b.
b. Print the output in a set format.
● Example 1 - If the set_a is ['apple', 'banana', 'pear', 'grape'], the program should
print:
{'banana', 'apple'}
● Example 2 - If the set_a is ['mango', 'mango', 'mango', 'pear', 'grape'], the
program should print: {'mango'}
'''
def common_words():
    # Get the words from command-line arguments
    set_a = sys.argv[1:]  # This will capture all command-line arguments except the script name
    set_b = ['apple', 'banana', 'mango', 'orange']

    # Convert both lists to sets to find common elements
    # Sets all have unique values, while arrays are only ordered and are not inherently unique
    # set(set_a)
    # set(set_b)
    # common_set = set_a & set_b

    # common_set = set(set_a) & set(set_b) # Set intersection
    common_set = set(set_a) - set(set_b)

    
    print(common_set)

if __name__ == "__main__":
    common_words()
