# a = input("enter string ")
# print(len(a))

# a = input("enter string ")
# print(len(a.replace(" ", "")))


# 


# Loop to get 5 strings from the user
# Loop to ask the user to enter 5 words and print their lengths without spaces
for i in range(5):
    word = input(f"Enter word {i+1}: ")
    # Remove spaces from the word and calculate the length
    word_length = len(word.replace(' ', ''))
    print(f"The length of word {i+1} without spaces is: {word_length}")
