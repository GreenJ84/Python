from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book



#==================== Render Author main ============

@app.route('/')
def authors_main_display():

    authors = Author.get_authors()

    return render_template('author_main.html', all_authors = authors)


#==================== Create A new Author ============

@app.route('/author/create', methods=['POST'])
def create_author():
    
    data ={
        "name": request.form['name']
    }
    Author.add_author(data)

    return redirect (f'/')



#==================== Render Author Sub page ============

@app.route('/author/<author_id>/<name>')
def display_author_page(author_id, name):

    data = {
        'author_id': author_id
    }
    
    author_info = Book.author_favorites(data)
    books = Book.get_books()

    return render_template('author_sub.html', fav_books = author_info, author_name = name, all_books = books,author_id=author_id)



#==================== Add Author Favorites ============

@app.route('/author/add_favorite', methods=['POST'])
def add_author_favorite():

    data = {
        'authors_id': request.form['authors_id'],
        'books_id': request.form['books_id']
    }

    author_id = request.form['authors_id']
    author_name = request.form['author_name']

    Author.create_author_fav(data)

    return redirect(f'/author/{author_id}/{author_name}')