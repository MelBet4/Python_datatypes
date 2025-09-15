#Create a tuple containing five of your favorite movies. 
#Use a `for` loop to print them with their **index numbers**

movies = ("Black Panther",
           "American Gangster",
           "Equalizer 1",
           "Entergalactic",
           "Equalizer 2"
)

#using for loop
for i in range(len(movies)):
    print(f"{i}: {movies[i]}")

#using enumerate
print("\n")
for index, movie in enumerate(movies):
    print(index,":", movie)

#fruits
fruits = input("\nEnter your favourite 5 fruits: ").split()
print("Your favourite fruits:")

for index, fruit in enumerate(fruits):
    print( index,":", fruit)