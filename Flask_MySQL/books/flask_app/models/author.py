from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    


#==================== Get Authors from DB ============


    @classmethod
    def get_authors(cls):

        query = "SELECT * FROM authors;"

        results= connectToMySQL('books_schema').query_db(query)

        authors = []

        for author in results:
            authors.append(cls(author))

        return authors



#==================== Add Authors to DB ============

    @classmethod
    def add_author(cls, data):

        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        return connectToMySQL('books_schema').query_db(query, data)



#==================== Create Authors favorites DB ============

    @classmethod
    def create_author_fav(cls, data):

        query= "INSERT INTO favorites (authors_id, books_id) VALUES (%(authors_id)s, %(books_id)s);"

        return connectToMySQL('books_schema').query_db(query, data)


#==================== Get Book Fav  authors ============

    @classmethod
    def book_favorites(cls, data):

        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.authors_id = authors.id LEFT JOIN books ON books.id = favorites.books_id WHERE `books`.`id` = %(book_id)s;"

        results = connectToMySQL('books_schema').query_db(query, data)

        favorites = []

        for authors in results:
            favorites.append(cls(authors))

        return favorites



