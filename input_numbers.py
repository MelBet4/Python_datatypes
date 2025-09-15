#example 1
numbers = input("Enter integers separated by spaces: ").split()

#convert into a list of integers
int_list = [int(num) for num in numbers]

#compute sum
total = sum(int_list)

#display the result
print(f"The sum of the integers is: {total}")

#example 2
nums = input('Enter integer and separate by space: ').split()
int_list = [int(digit) for digit in nums]
totalnum = sum(int_list)
print(f"Sum of the numbers: {totalnum}")

#example 3
students = input('Numbers for 3 classes: ').split()
int_number = [int(count) for count in students]
totalStudents = sum(int_number)
print(f"Total number of students: {totalStudents}")

cars = input("Number of cars: ").split()
carCount = [int(toll) for toll in cars]
totalCars = sum(carCount)
print(f'Total number of cars: {totalCars}')

#using map function
#example 1
nums = list(map(int, input("Enter numbers: ").split()))
print(sum(nums))

#example 2
cars = list(map(int, input('Enter car count: ').split()))
total_cars = sum(cars)
print(f'Total count of cars in different parks: {total_cars}')

