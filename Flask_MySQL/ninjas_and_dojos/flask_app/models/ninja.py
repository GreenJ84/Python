from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['fname']
        self.last_name = data['lname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']

    #===================== Adding a new ninja ===========================

    @classmethod
    def add_ninja(cls, data):

        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"

        dojo_updated = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        return dojo_updated



    #===================== Displaying ninjas in Dojo ===========================
    
    @classmethod
    def get_dojo_ninjas(cls, data):

        query = "SELECT `dojo_id`, `first_name`, `last_name`, `age` FROM `ninjas` JOIN `dojos` ON `dojos`.`id` = `ninjas`.`dojo_id` WHERE `dojos`.`id` = '%(dojo_id)s' GROUP BY `ninjas`.`id`;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        ninjas = []

        for ninja in results:
            ninjas.append(ninja)
        print(ninjas)

        return ninjas
