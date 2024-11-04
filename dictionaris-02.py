# Завдання: 
# Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). 
# Додайте до словника нову улюблену книгу та виведіть оновлений словник.

books = {
    "Atlas Shrugged by Ayn Rand": 1957, 
    "The Great Gatsby by F. Scott Fitzgerald": 1925,
    "The Call of the Wild by Jack London": 1903,
    "Nineteen Eighty-Four by George Orwell": 1949
}

books.update({"The Count of Monte Cristo by Alexandre Dumas": 1844})

print(books)