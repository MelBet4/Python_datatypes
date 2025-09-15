#reverse list

#ask user for input
numbers = input("Enter 5 integers: ").split()

#1. Using reverse method
numbers.reverse()
print(f"Numbers using reverse method {numbers}")

#2. Slicing method
sliced = numbers[:: -1] 
print(f"Numbers using slicing method {sliced}")

#3. without slicing or reverse() method
reversed_list = []

i = len(numbers) - 1
while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1

print(f"Reversed list: {reversed_list}")