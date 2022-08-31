from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def hi(name):
    print(f'Hi {name}!')
    return f'Hi {name}!'


@app.route('/repeat/<int:num>/<word>')
def repeats(num, word):
    for x in range(num):
        result = f'{str(word)}! \n'
        results = result*num
        return results

# @app.route('/<sting:anything>')
# def blankResponse():
#     return "Sorry! No Response. Try Again."

if __name__=="__main__":
    app.run(debug=True, port=5001)