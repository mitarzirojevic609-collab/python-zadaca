import random

from datetime import datetime
from faker import Faker

faker = Faker()



genres = ["Mystery", "Adventure", "Fantasy"]
adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]



def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1) ,
                         end_date= datetime(2000, 1, 1))

def generate_random_genre():
    return random.choice(genres)

def generate_random_author():
    return faker.name()

def generate_book_title(book_genre, book_author):
    return  f"{random.choice(adjectives)} {random.choice(nouns)}: A {book_genre} story by {book_author}"

def insert_book(con, name, book_gener, book_author):
    cursor = con.cursor()
    cursor.execute ("INSERT INTO books (name, category, author) VALUES (%s, %s, %s)", (name, book_gener, book_author))
    con.commit()
    cursor.close()

def get_all_books(con):
    cursor = con.cursor()
    cursor.execute ("SELECT * FROM books")
    con.commit()
    result = cursor.fetchall()
    cursor.close()
    return result

def get_book_by_id(con, book_id):
    cursor = con.cursor()
    cursor.execute ("SELECT * FROM books where id = %s", book_id,)
    con.commit()
    result = cursor.fetchone()
    cursor.close()
    return result

def delete_book_by_id(con, book_id):
    cursor = con.cursor()
    cursor.execute("DELETE FROM books where id = %s", book_id)
    con.commit()
    cursor.close()
