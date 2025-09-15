#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.

#empty list
myList = []

#append [10, 20, 30, 40] to myList
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
print(myList)

#insert 15 at the second position
#myList[1] = 15
#print(myList)

#second list
list2 = [50, 60, 70]
myList.extend(list2)
print(myList) #output: [10, 15, 30, 40, 50, 60, 70]

#remove the last element from list
myList.remove(70)
print(myList) #output: [10, 15, 30, 40, 50, 60]

#rearrange in ascending order
asc = sorted(myList)
print("Ascending: ", asc) #output: [10, 15, 30, 40, 50, 60]

#descending order
desc = sorted(myList, reverse=True)
print("Descending: ", desc) #output: [60, 50, 40, 30, 15, 10]

numbers = [10, 20, 30, 40, 50]
print(numbers[0])   #returns the first item
print(numbers[1])   #returns the second item
print(numbers[-1])   #returns the last item
print(numbers[-2])   #returns the second last item

print(numbers.append(6)) #add 6 to the end
print(numbers.insert(0, 6)) #adds 6 at index position of 0
print(numbers.remove(6)) #removes the first occurrence of 6
print(numbers.pop()) #removes the last item
print("Index of 20: ",numbers.index(20)) #returns the index of the first occurence of 8
print("Ascending: ",numbers.sort()) #sorts in ascending order
print("Descending: ", numbers.reverse()) #sorts in descending order
print("Number's copy: ",numbers.copy) #return a copy of the list
print("Cleared list: ",numbers.clear) #removes all the items


