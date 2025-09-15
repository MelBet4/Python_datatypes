#Ask the user to enter a list of words. Use list comprehension
#to create a list of words that are **longer than 4 characters**.
words = input("Enter list of words: ").split()

more_than_4 = [word for word in words if len(word) > 4]
print(f"Words with more than 4 characters : {more_than_4}")

#Create a list of numbers from 1–20 using list comprehension. 
#Then use another list comprehension to keep only the 
#*multiples of 3**.
numbers = [num for num in range(1, 21)]
print(numbers)

multiples_3 = [num for num in numbers if num % 3 == 0]
print(f"Multiples of three: {multiples_3}")

#Ask the user for a sentence. Use list comprehension to 
#create a list of all the **words that start with a vowel**.
sentence = input("Write a sentence and space accordingly: ")
words = sentence.split()

initial_vowel = [word for word in words if word[0].lower() in 'aeiou']
print(f"Words that start with a vowel: {initial_vowel}")
