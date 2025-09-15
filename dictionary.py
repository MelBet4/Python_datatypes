#Write a program that stores a dictionary with keys: 
#`"name"`, `"age"`, and `"city"`. Ask the user to input 
#the values, then print the dictionary.
#Extend challenge #7: Ask the user if they want to 
#**update** one of the values. If yes, let them choose 
#which key to update and enter a new value.

person = {}

person["Name"] = input("Enter your name: ").title()
person["Age"] = input("Enter your age: ")
person["City"] = input("Enter the city you live in: ").title()
print(f"Person details: {person}")

#update
choice = input("\nDo you want to make an update(yes/no): ")

if choice == "yes":
    personField = input("\nWhich field do you want to update: (Name, Age, City): ").title()
    if personField in person:
        update = input(f"Enter the value for {choice}: ")
        person[personField] = update
    else:
        print("Invalid field")

print(f"\nUpdated person's details: {person}")


#Create a dictionary where the keys are **numbers 1–5** 
#and the values are their **squares**. 
#Print the dictionary.
squares = {}

for i in range(1, 6):
    squares[i] = i ** 2

print(f"Squares dictionary: {squares}")

#simpler method
squares = {i: i ** 2 for i in range(1, 6)}
print(f"Squares: {squares}")