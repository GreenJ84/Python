from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

#==================== Render Books main ============
@app.route('/books')
def books_main_display():

    books = Book.get_books()
    print(books)
    return render_template('book_main.html', all_books=books )


#==================== Add New book  ==============


@app.route('/books/new_book',methods=['POST'])
def add_new_book():

    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_pages']
    }
    
    Book.add_book(data)

    return redirect('/books')



#==================== Render Books Sub page  ==============
@app.route('/books/<book_id>/<book_title>')
def books_sub_display(book_id, book_title):
    book_id = book_id

    data = {
        'book_id': book_id
    }

    book_info = Author.book_favorites(data)
    authors = Author.get_authors()

    return render_template('book_sub.html', book_title = book_title, book_id = book_id, all_authors = authors, book_favs = book_info)


#==================== Render Books Sub page  ==============
@app.route('/books/add_favorite', methods=['POST'])
def add_book_favorite():

    data = {
        'authors_id': request.form['author_id'],
        'books_id': request.form['book_id']
    }
    print(data)
    book_id = request.form['book_id']
    book_title = request.form['book_title']

    Book.create_book_fav(data)

    return redirect(f'/books/{book_id}/{book_title}')