#[expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

#list comprehension
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(f"Using list comprehension: {doubles}")
print("Triples: ",triples)
print("Squares: ",squares)


#strings
fruits = ["apples", "oranges", "bananas", "mangos"]
fruits = [fruit.upper() for fruit in fruits]
fruit_char = [fruit[0] for fruit in fruits]

print(f"Fruits(uppercase): {fruits}")
print(fruit_char)


#using conditions
numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(f"Positive numbers: {positive_nums}")
print(f"Negative numbers: {negative_nums}")
print(f"Even numbers: {even_nums}")
print(f"Odd numbers: {odd_nums}")


#list of grades: passing > 60
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)