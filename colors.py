#Ask the user to enter five colors and store them in a tuple.
#Then ask the user for a number (index) and print the color
#at that index, or `"Invalid index"` if it doesn’t exist.

colors = tuple(input("Enter five colors(seperate by space): ").split())
index = int(input("Enter the index to access: "))

if 0 <= index <= (len(colors)):
    print(index, colors[index])
else:
    print("Invalid index")
