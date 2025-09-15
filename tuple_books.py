myBooks = ('Purple Hibiscus', 
           'The girls with a booming voice', 
           'Americanah',
           'Becoming',
           'The day God saw me as black')
print('Some of my favourite books: ')

for book in myBooks:
    print(f' {book}')

for i in range(len(myBooks)):
    print(f"{i}: {myBooks[i]}")
