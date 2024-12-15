'''
comprehension.py

● IMPORTANT
○ Your autotest cases will NOT work if you don’t load your sys.argv like
below. For this assignment, load in your sys.argv like so:
my_ints = sys.argv[1:]

This material is for enrolled students' academic use only and protected under U.S. Copyright Laws. This content must not be shared outside the confines
of this course, in line with Eastern University's academic integrity policies. Unauthorized reproduction, distribution, or transmission of this material,
including but not limited to posting on third-party platforms like GitHub, is strictly prohibited and may lead to disciplinary action. You may not alter or
remove any copyright or other notice from copies of any content taken from BrightSpace or Eastern University’s website.
© Copyright Notice 2024, Eastern University - All Rights Reserved

○ The above my_ints a list-type variable which contain numbers that are
string-typed (ex. ['1', '2', '3', '4', '5'])

● Create a program, comprehension.py. Your program should:
1. Convert these string-type integers into integer-type.
2. If the number within the list is divisible by 3, multiply it by 10, then replace
it.
● For example:
○ If your my_ints = ['1', '2', '3', '4', '5'], your output should be [1, 2, 30, 4, 5]
○ If your my_ints = ['3', '30', '1', '15', '10'], your output should be [30, 300, 1,
150, 10]
'''



import sys

def comprehension():
    # Load my_ints from sys.argv
    my_ints = sys.argv[1:]

    # Convert strings to integers and apply the transformation if divisible by 3
    result = []
    
    for i in my_ints:
        if int(i) % 3 == 0:
            result.append(int(i) * 10)
        else:
            result.append(int(i))

    # Print the transformed list
    print(result)

if __name__ == "__main__":
    comprehension()