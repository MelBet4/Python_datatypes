set1 = set(map(int, input("Enter integers for the first set: ").split()))
set2 = set(map(int, input("Enter integers for the second set: ").split()))

#find common elements(intersection)
common = set1 & set2

print(f"Common element(s): {common}")

grp1 = set(map(int, input("Enter first group integers (separate by space): ").split()))
grp2 = set(map(int, input("Enter second group integers:  ").split()))

common = grp1 & grp2
print(f"Common element(s) in group 1 and 2: {common}")

#same marks
Noel = set(map(int, input("Enter your marks in five subjects: ").split()))
Melanie = set(map(int, input("Enter your scores in five subjects: ").split()))

commonScore = Noel & Melanie
print(f"Common score(s) between the two students: {commonScore}")
totalNoel = sum(Noel)
averageNoel = totalNoel/5
print(f"Noel's score: {totalNoel}, {averageNoel}")
totalMelanie = sum(Melanie)
averageMelanie = totalMelanie/5
print(f"Melanie's score: {totalMelanie}, {averageMelanie}")

