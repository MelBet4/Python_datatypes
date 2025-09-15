#Create a tuple containing the names of five countries 
#you’d like to visit.
#Ask the user for a number (index).
#Print the country at that index if it exists, 
#otherwise print "Invalid index".
#Also, use a for loop to print all country names in 
#uppercase.

destinations = ("South Africa", "USA", "Rwanda", "Egypt", "Switzerland")

access_index = int(input("Enter index to access a destination: "))

if 0 <= access_index < len(destinations):
    print(f"Country at index {access_index} is {destinations[access_index]}")
else:
    print("Invalid index")

#list comprehension
upper_countries = [destination.upper() for destination in destinations]
print(f"Countries in capital: {upper_countries}")



#colors tuple
colors = ("red", "blue", "green", "yellow", "purple")

#ask for user for an index
index = int(input("Enter an index number: "))

#check if index is valid
if 0 <= index < len(colors):
    print(f"Color at index {index} is {colors[index]}")
else:
    print("Invalid index")

#change first letter to upper case
title = [color.title() for color in colors]
print(f"Title format: {title}")