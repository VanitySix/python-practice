'''
inrange.py

● Create a program inrange.py that has a function that takes one integer argument.
The function will print a list of all values between 3000 and 5000 that is divisible
by:
1. the integer argument
2. the integer argument + 7
3. the integer argument ^ 2
● For example, if the integer argument is 6, it should print:
[3276, 3744, 4212, 4680]
'''

import sys

def divisible(n):
    result = []
    for i in range(3000,5001):
        if i % n == 0 or i % (n + 7) == 0 or i % (n ** 2) == 0:
            result.append(i)
            

    print(result)


if __name__ == "__main__":
    divisible(6)