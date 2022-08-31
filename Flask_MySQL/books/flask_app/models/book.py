from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updates_at = data['updated_at']

#==================== Get Books all books ============

    @classmethod
    def get_books(cls):

        query = "SELECT * FROM books;"

        results = connectToMySQL('books_schema').query_db(query)

        books=[]

        for book in results:
            books.append(cls(book))

        return books

#==================== Add book to db ============
    @classmethod
    def add_book(cls, data):

        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"

        return connectToMySQL('books_schema').query_db(query, data)

#==================== Create Books favorites DB ============

    @classmethod
    def create_book_fav(cls, data):

        query = "INSERT INTO favorites (authors_id, books_id) VALUES (%(authors_id)s, %(books_id)s);"

        return connectToMySQL('books_schema').query_db(query, data)



#==================== Get Author Fav  books ============

    @classmethod
    def author_favorites(cls, data):

        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.books_id = books.id LEFT JOIN authors ON authors.id = favorites.authors_id WHERE `authors`.`id` = %(author_id)s;"

        results = connectToMySQL('books_schema').query_db(query, data)

        favorites=[]
        
        for books in results:
            favorites.append(cls(books))

        return favorites
