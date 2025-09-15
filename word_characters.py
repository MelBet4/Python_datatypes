#Create a program that stores a list of words. 
#Then, use list comprehension to create a new list that 
#contains only the words that have an odd number of 
#characters.

#store a list of words
words = input("Enter words separated by space: ").split()

#use list comprehension to filter words with odd length
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)

even_length_words = [word for word in words if len(word) % 2 == 0]
print("Words with even number of characters: ", even_length_words)


fruits = ["apples", "mangos", "carrots", "bananas"]
odd_length = [fruit for fruit in fruits if len(fruit) % 2 != 0]
even_length = [fruit for fruit in fruits if len(fruit) % 2 == 0]

print("Words with odd number of characters: ", odd_length)
print("Words with even numbers of characters: ", even_length)