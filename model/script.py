from model.db import connection
from model.book import *
from model.user import insert_user

choices = None

while choices is None or choices == '':
    choices = input("What do you want to do?\n 1.Create random book \n 2. Show books \n 3. Show book by ID \n4. Delete a book ")
    choices = int(choices)

    if choices == 1:

        genre = generate_random_genre()
        author = generate_random_author()
        title = generate_book_title(genre, author)
        dob = generate_random_dob()

        user = insert_user(connection, author, dob)
        insert_book(connection, title, genre, user)
        print(f"created a new book call {title }")




    elif choices == 2:
        books = get_all_books(connection)
        print(books)

    elif choices == 3:
        book_id = None
        while book_id == None:
            book_id = input("Enter the book ID")

            book = get_book_by_id(connection, book_id)

            if book:
                print(f"This book name is {book['name']}")
            else:
                print("This book does not exist, try again")
                book_id = None

    elif choices == 4:
        book_id = None
        while book_id == None:
            book_id = input("Enter the book ID")

            delete_book_by_id(connection, book_id)


    else:
        choices = None



