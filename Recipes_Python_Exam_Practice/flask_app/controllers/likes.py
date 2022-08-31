from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.like import Like
from flask_app.models.recipe import Recipe



#========================== Create a New recipe like =========================
@app.route('/like/<recipe_id>')
def like_recipe(recipe_id):

    data = {
        'user_id': session['user_id'],
        'recipe_id': recipe_id
    }
    like = Like.check_likes(data)

    if like:
        flash('Already like this recipe!')
        return redirect('/dashboard')
    else:
        Like.create_like(data)
        print('like created')

    return redirect(f'/recipe/view/{recipe_id}')


#========================== Delete a Like =========================
@app.route('/unlike/<recipe_id>')
def unlike_recipe(recipe_id):

    data = {
        'user_id': session['user_id'],
        'recipe_id': recipe_id
    }

    Like.delete_like(data)

    return redirect(f'/recipe/view/{recipe_id}')