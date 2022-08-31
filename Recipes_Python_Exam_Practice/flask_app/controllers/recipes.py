from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app.models.like import Like

#========================== Render Create Page =========================
@app.route('/recipe/create')
def recipe_create():
    if 'user_id' not in session:
        return redirect('/')


    return render_template('create_recipe.html', display_name = session['user_first_name'])



#========================== Create Recipe Page  POST! =========================
@app.route('/recipe/create/post', methods=['POST'])
def create_new_recipe():

    if not Recipe.validate_recipe(request.form):
        return redirect('/recipe/create')

    if request.form['under_30'] == 'true':
        under_30 = True
    elif request.form['under_30'] == 'false':
        under_30 = False
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked_made': request.form['date_cooked_made'],
        'under_30': under_30,
        'users_id': session['user_id']
    }
    Recipe.create_new_recipe(data)

    return redirect('/dashboard')



#========================== Render Edit Page =========================
@app.route('/recipe/view/<recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'recipe_id': recipe_id
    }
    recipe = Recipe.get_recipe_byid(data)


    return render_template('view_recipe.html', display_name = session['user_first_name'], recipe = recipe)


#========================== Render Edit Page =========================
@app.route('/recipe/edit/<recipe_id>')
def edit_recipe_display(recipe_id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        'recipe_id': recipe_id
    }
    recipe = Recipe.get_recipe_byid(data)


    return render_template('edit_recipe.html', display_name = session['user_first_name'], recipe = recipe)

#========================== Apply edit to database  POST! =========================
@app.route('/recipe/edit/<recipe_id>/post', methods=['POST'])
def edit_recipe(recipe_id):

    if not Recipe.validate_recipe(request.form):
        return redirect(f'/recipe/edit/{recipe_id}')

    if request.form['under_30'] == 'true':
        under_30 = True
    elif request.form['under_30'] == 'false':
        under_30 = False

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_cooked_made': request.form['date_cooked_made'],
        'under_30': under_30
    }

    Recipe.update_recipe(data)


    return redirect('/dashboard')


#========================== Render Delete method   POST! =========================
@app.route('/recipe/delete/<recipe_id>')
def delete_recipe(recipe_id):

    data = {
        'recipe_id': recipe_id
    }

    Recipe.delete_recipe(data)


    return redirect('/dashboard')

