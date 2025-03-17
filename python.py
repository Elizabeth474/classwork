# question 1
# a = input("enter string ")
# print(len(a))

# question 2

# a = input("enter string ")
# print(len(a.replace(" ", "")))


# question 3

# for i in range(5):
    # word = input(f"Enter word {i+1}: ")
    # word_length = len(word.replace(' ', ''))
    # print(f"The length of word {i+1} without spaces is: {word_length}")

# question 4

# Define the translation mapping as a set of tuples
trans = {("k", "a"), ("j", "i"), ("p", "o"), ("t", "e"), ("f", "u")}

# Create a dictionary for easy lookup
trans_dict = {}
for a, b in trans:
    trans_dict[a] = b
    trans_dict[b] = a  # Make sure both directions are covered

# Function to swap letters based on the translation
def swap_letters(word):
    swapped_word = []
    for letter in word:
        if letter in trans_dict:
            swapped_word.append(trans_dict[letter])
        else:
            swapped_word.append(letter)  # Keep the letter unchanged if no swap is found
    return ''.join(swapped_word)

# Get the word input from the user
word = input("Enter a word: ").lower()

# Call the function to swap letters and print the result
result = swap_letters(word)
print(f'Applying "kajipotefu" on the word "{word}" we get: {result}')
