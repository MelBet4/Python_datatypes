#Store a list of words entered by the user.
#Use list comprehension to create:
#A new list of words that start with a vowel.
#A new list of words that are longer than 4 characters.
#Print both results.

#ask user for input
userList = input("Enter words separated by space: ").split()

#list comprehension
#1. For words with vowels as their initial character

#words_inital_vowel = [word for word in userList if word[0].lower() == ("a" or "e" or "i" or "o" or "u")]
#print(f"These words start with a vovel {words_inital_vowel}")
#above code doesn't work - it only looks for the word stating with a

words_inital_vowel = [word for word in userList if word[0].lower() in 'aeiou']
print(f"The words have vowels as their initial letters: {words_inital_vowel}")

#2. List of words with characters longer than 4
longer_length = [word for word in userList if len(word) > 4]
print(f"Words with more than 4 characters: {longer_length}")