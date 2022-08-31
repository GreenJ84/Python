from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.like import Like
from flask import flash, session


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked_made = data['date_cooked_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        if 'first_name' in data:
            self.user_first = data['first_name']
        if 'last_name' in data:
            self.user_last = data['last_name']
        if 'like_count' in data:
            self.like_count = data['like_count']
        if 'user_liked' in data:
            self.user_liked = data['user_liked']



    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        if len(recipe['name']) <= 3:
            is_valid = False
            flash("Recipe name is not long enough!")
        if len(recipe['description']) <= 3:
            is_valid = False
            flash("Description is not long eough!")
        if len(recipe['instructions']) <= 3:
            is_valid = False
            flash("Instructions are not long enough!")
        return is_valid
#======================== GetAll Recipes for Display ==============

    @classmethod
    def get_all_recipes(cls):
        
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id;"
        results = connectToMySQL('recipes').query_db(query)

        recipes = []

        for item in results:

            like_count = 0
            x = {
                'recipe_id': item['id']
            }
            answer = Like.check_recipe_likes(x)
            for items in answer:
                like_count = like_count + 1
            item['like_count'] = like_count

            y = {
                'recipe_id': item['id'],
                'user_id': session['user_id']
            }
            if len(Like.check_likes(y)) >= 1:
                item['user_liked'] = 1


            recipes.append(cls(item))
            print(item)

        return recipes

#======================== GetAll Recipes for Display ==============

    @classmethod
    def get_recipe_byid(cls, data):
        
        query = "SELECT * FROM recipes JOIN users ON recipes.users_id = users.id WHERE recipes.id = %(recipe_id)s;"
        results = connectToMySQL('recipes').query_db(query, data)

        recipe = []
        

        for item in results:
            recipe.append(cls(item))
        print(recipe)
        
        return recipe[0]


#========================== Create a New Recipe =====================

    @classmethod
    def create_new_recipe(cls, data):

        query = "INSERT INTO recipes (name, description, instructions, date_cooked_made, under_30, created_at, Updated_at, users_id)VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked_made)s, %(under_30)s, NOW(), NOW(), %(users_id)s);"

        results = connectToMySQL('recipes').query_db(query, data)

        return results


#========================== Update Recipe ====================
    @classmethod
    def update_recipe(cls, data):

        query =  "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked_made = %(date_cooked_made)s, under_30 = %(under_30)s WHERE id = %(recipe_id)s"

        connectToMySQL('recipes').query_db(query, data)

        return



#========================== Delete Recipe =====================
    @classmethod
    def delete_recipe(cls, data):

        query= "DELETE FROM recipes WHERE id = %(recipe_id)s"

        connectToMySQL('recipes').query_db(query, data)

        return



