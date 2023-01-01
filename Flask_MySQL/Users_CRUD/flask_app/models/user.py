from flask_app.config.mysqlconnection import connectToMySQL


def changeDate(date):
    return str(date.month)+"-"+str(date.day)+"-"+str(date.year)
class User:
    def __init__(self, data):
        x = changeDate(data['created_at'])
        y = changeDate(data ['updated_at'])
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = x
        self.updated_at = y

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users;"

        results = connectToMySQL('users_schema').query_db(query)

        users = []
        print(users)

        for user in results:
            users.append(cls(user))

        return users



    @classmethod
    def get_user(cls, data):

        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('users_schema').query_db(query, data)

        user = User(result[0])

        return user



    @classmethod
    def new_user(cls, data):
        
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES ( %(fname)s, %(lname)s, %(email)s, NOW(), NOW() );"

        return connectToMySQL('users_schema').query_db(query, data)



    @classmethod
    def update_user(cls, data):


        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id= %(id)s;"


        return connectToMySQL('users_schema').query_db(query, data)




    @classmethod
    def delete_user(cls, data):

        query = "DELETE FROM users WHERE id = %(id)s"

        return connectToMySQL('users_schema').query_db(query, data)