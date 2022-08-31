from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.user import User

# ================= GET ALL ====================

@app.route('/')
def index():
    users = User.get_all()

    return render_template('index.html', all_users = users)

# ================== CREATE ======================

@app.route('/create')
def user_form():

    return render_template('create_user.html')

# ========== PROCESS CREATE =========

@app.route('/create_user', methods = ['POST'])
def create_user():

    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'email': request.form['email']
    }

    new_user_id = User.new_user(data)

    return redirect(f'/user/{new_user_id}')

# =============== SHOW BY ID ===============

@app.route('/user/<int:user_id>')
def diplay_user(user_id):
    
    data = {
        "id": user_id
    }
    
    user = User.get_user(data)

    return render_template('user_profile.html', user_info = user)

# ============== EDIT =====================

@app.route('/user/<int:user_id>/edit')
def edit_user(user_id):

    data = {
        "id": user_id
    }

    user = User.get_user(data)
    

    return render_template('user_edit.html', user_info=user)

# ========== PROCESS UPDATE =========

@app.route('/user/<user_id>/update', methods=['POST'])
def user_update(user_id):

    data = {
        'id': user_id,
        'fname' : request.form['fname'],
        'lname' : request.form['lname'],
        'email' :request.form['email']
    }
    user_id = user_id
    User.update_user(data)

    return redirect(f'/user/{user_id}')

# ================= DELETE ==================

@app.route('/user/<int:user_id>/delete')
def delete(user_id):

    data = {
        "id": user_id
    }

    User.delete_user(data)

    return redirect('/')