#Accept two sets of integers from the user. Print their 
#**union, intersection, and difference**.
#Create a set of numbers from 1–10. Remove all even numbers from the set and print the result.
#Write a program that checks whether two sets entered by 
#the user are **disjoint** (no elements in common).

set1 = set(input("Enter integers for set1: ").split())
set2 = set(input("Enter integers for set2: ").split())

union = set1 & set2
print(f"Union: {union}")

intersection = set1 | set2
print(f"Intersection: {intersection}")

difference1 = set1 - set2
print(f"In set1 but not set2: {difference1}")
difference2 = set2 - set1
print(f"In set2 but not set1: {difference2}")

#disjoint - two sets have no elements in common
print(set1.isdisjoint(set2)) 
