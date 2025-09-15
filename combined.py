#Ask the user for student names and scores, store them in a
#dictionary.
#Create a list of students who scored above the average 
#using **list comprehension**.
#Print the set of all scores (to remove duplicates).

#Ask user for number of students
n = int(input("Enter the number of students: "))

students = {} 

for i in range(n):
    name = input(f"Input name of student {i + 1}: ")
    score = int(input(f"Enter score of {name}: "))
    students[name] = score

#calculate average
average = sum(students.values()) / len(students)

#above average
above_average = [name for name, score in students.items() if score > average]

#print set of all scores(removes duplicate)
unique_scores = set(students.values())

print("\nStudents and their scores: ", students)
print(f"Average score: {average}")
print(f"Students above average: {above_average}")
print(f"Unique scores: {unique_scores}")
