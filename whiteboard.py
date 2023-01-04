# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Examples:						
# Input: ‘Joel’
# Output: ‘Jl’
# Input: ‘Shoha’
# Output: ‘Shh’

#create a function
#loop through input to figure out if vowels are present
#return our output by appending it to our empty list

def vowels(st):

# input = ['Joel', 'shoha']
    empty = [] 
    #or ""

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for char in st:
        if char.lower() not in vowels:
            empty.append(char)
            #or empty +=
    print("".join(empty))

vowels ('Joel')
vowels ('Shoha')
