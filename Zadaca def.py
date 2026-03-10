books = []

def add_book(book_name, book_author):
    books.append({"name": book_name, "author": book_author})

def find_book_by_name(name):
    for book in books:
        if book["name"] == name:
            return book

add_book("Harry Potter 1", "J K ROWLING")
add_book("Harry Potter 3", "J K ROWLING")

hp1 = find_book_by_name("Harry Potter 6")
if hp1 is not None:
    print("Nema date knjige")
    print(hp1)

def delete_book_by_name(name):



   found_book = find_book_by_name(name)
   if found_book is None:
        print("Knjiga koju trazite ne postoji")
   else:
        books.remove(found_book)
        print("Obrisana je knjiga")

delete_book_by_name("Harry Potter 3")
print(books)





