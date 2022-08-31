from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash, session



class Like:
    def __init__(self, data):
        if 'id' in data:
            self.id = data['id']
        if 'user_id' in data:
            self.user_id = data['user_id']
        if 'recipe_id' in data:
            self.recipe_id = data['recipe_id']
        if 'created_at' in data:
            self.created_at = data['created_at']
        if 'updated_at' in data:
            self.updated_at = data['updated_at']


#========================== Create Like =====================
    @classmethod
    def create_like(cls, data):

        query = "INSERT INTO likes (user_id, recipe_id, created_at, updated_at) VALUES (%(user_id)s, %(recipe_id)s, NOW(), NOW());"

        connectToMySQL('recipes').query_db(query, data)

        return

#========================== Delete Like =====================
    @classmethod
    def delete_like(cls, data):

        query = "DELETE FROM likes WHERE user_id = %(user_id)s && recipe_id = %(recipe_id)s;"

        connectToMySQL('recipes').query_db(query, data)

        return

#========================== Check Like =====================
    @classmethod
    def check_likes(cls, data):

        query = "SELECT * FROM likes WHERE user_id = %(user_id)s && recipe_id = %(recipe_id)s;"
        print(query)

        results = connectToMySQL('recipes').query_db(query, data)

        return results

#========================== Check User Likes =====================
    @classmethod
    def check_recipe_likes(cls, data):

        query = "SELECT user_id FROM likes WHERE recipe_id = %(recipe_id)s;"

        result = connectToMySQL('recipes').query_db(query, data)

        results=[]
        for item in result:
            results.append(cls(item))

        
        return results