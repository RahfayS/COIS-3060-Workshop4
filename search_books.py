print('Search Books')  
print('-' * 20)  
search\_term \= input('Enter search term: ')

print(f'\nSearching for "{search_term}"...')  
found \= False

with open('books.txt', 'r') as f:  
    for line in f:  
        if search\_term.lower() in line.lower():  
            print(line.strip())  
            found \= True

if not found:  
    print('No books found.')
