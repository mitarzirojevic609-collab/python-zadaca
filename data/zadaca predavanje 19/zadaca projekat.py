from faker import Faker
import random
from db import connection
from datetime import datetime


faker = Faker()

genres = ["Mystery", "Adventure", "Fantasy"]
adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]
author_name = faker.name()


def generate_random_dob():
    return faker.date_between(start_date=datetime(1950, 1, 1) ,
                         end_date= datetime(2000, 1, 1))

def generate_random_genre():
    return random.choice(genres)

def random_author():
    return faker.name()

def generate_book_title(book_genre, book_author):
    return  f"{random.choice(adjectives)} {random.choice(nouns)}: A {genre} story by {author_name}"



def insert_user(con, name, date_of_birth):
    cursor = con.cursor()
    cursor.execute ("INSERT INTO users (name, dob) VALUES (%s, %s)", (name, date_of_birth))
    con.commit()
    cursor.close()

def insert_book(con, name, book_gener, book_author):
    cursor = con.cursor()
    cursor.execute ("INSERT INTO books (name, category, author) VALUES (%s, %s, %s)", (name, book_gener, book_author))
    con.commit()
    cursor.close()

dob = generate_random_dob()
genre = generate_random_genre()
author = random_author()
book_title = generate_book_title(genre, author)
insert_user(connection, author, dob)
insert_book(connection, book_title, genre, author)

print(dob, genre, author, book_title)