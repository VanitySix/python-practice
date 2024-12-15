import sys

# takes in a string then prints 
# the number of unique vowels in the string 
# (regarless of it being upper or lwoercase)


def countVowels(input):
    vowels = {'i','o','a','e','u'}

    unique_vowels = set()
    
    for char in input:
        if char in vowels:
            unique_vowels.add(char)

    print("Unique vowels: ",len(unique_vowels))


if __name__ == "__main__":
    user_input = sys.argv[1]
    countVowels(user_input)

'''
def count_vowels(input_string):
    # Define a set of vowels (both lowercase and uppercase)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Use a set to track unique vowels found in the input string
    unique_vowels = set()
    
    # Loop through the string, convert to lowercase, and check if it's a vowel
    for char in input_string.lower():
        if char in vowels:
            unique_vowels.add(char)  # Add to the set if it's a vowel
    
    # Print the number of unique vowels
    print(len(unique_vowels))

if __name__ == "__main__":
    user_input = sys.argv[1]
    count_vowels(user_input)'''