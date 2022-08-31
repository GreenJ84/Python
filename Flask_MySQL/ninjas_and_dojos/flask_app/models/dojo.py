from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']


#================================ Display Dojos =======================



    @classmethod
    def get_dojos(cls):

        query = "Select * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))

        return dojos
        
        
        
#================================ Retrieve Dojo Name =======================



    @classmethod
    def get_dojo_name(cls, data):

        query = "Select `name` FROM dojos WHERE `id` = %(dojo_id)s;"
        print(query)


        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        result2 = results[0]
        dojo_name = result2['name']

        return dojo_name



#================================ Create new dojo =======================


    @classmethod
    def create_new_dojo(cls, data):

        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"

        dojo_applied = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)


        return dojo_applied



#================================  =======================
