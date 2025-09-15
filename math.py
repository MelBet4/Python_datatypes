#Write a program that accepts user input to create a list of integers.
#Then compute the average, maximum, and minimum of the integers.
#Finally, print the list in reverse order.

numbers = list(map(int, input("Enter numbers separed by space: ").split()))

#average
average = sum(numbers) / len(numbers)
print(f"The average of {numbers} is: {average}")
maximum = max(numbers)
print(f"The maximum integer: {maximum}")
minimum = min(numbers)
print(f"Minimum integer: {minimum}")
