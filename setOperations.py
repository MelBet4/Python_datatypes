#Write a program that accepts user input to create two sets of integers.
#Then create:
#A set of elements common to both sets (intersection).
#A set of elements that are in the first set but not the second (difference).
#A set of all elements from both sets (union).

set1 = set(input("Enter integers for first set: ").split())
set2 = set(input("Enter integers for second set: ").split())

#intersection
common = set1 & set2
print(f"The common integers in set1 and set2: {common}")

#difference (-): element in first set but not the second (set1 - set2)
diff1 = set1.difference(set2)
print(f"{diff1}: in set1 but not in set2")

diff2 = set2 - set1
print(f"{diff2}: i set2 but not in set1")

#union(|): combine all elements from both sets (removes duplicates)
union_result = set1.union(set2) #OR: set1 | set2
print(f"Union: {union_result}")
