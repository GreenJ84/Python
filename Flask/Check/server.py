
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board(y=8, x=8, color1='red', color2='black'):
    print(x)
    print(y)
    print(color1)
    print(color2)

    return render_template('checkerboard.html', y=y, x=x, color1=color1,color2=color2)

@app.route('/<int:y>')
def board_row(y, x=8, color1='red', color2='black'):
    print(x)
    print(y)
    print(color1)
    print(color2)

    return render_template('checkerboard.html', y=y, x=x, color1=color1,color2=color2)


@app.route('/<int:y>/<int:x>')
def column(y, x, color1='red', color2='black'):
    print(x)
    print(y)
    print(color1)
    print(color2)
    return render_template('checkerboard.html', y=y, x=x, color1=color1,color2=color2)


@app.route('/<int:y>/<int:x>/<color1>')
def color1(y, x, color1, color2='black'):
    print(x)
    print(y)
    print(color1)
    print(color2)

    return render_template('checkerboard.html', y=y, x=x, color1=color1, color2=color2)


@app.route('/<int:y>/<int:x>/<color1>/<color2>')
def change_whole(y, x, color1, color2):
    print(x)
    print(y)
    print(color1)
    print(color2)
    return render_template('checkerboard.html', y=y, x=x, color1=color1, color2=color2)



if (__name__) == '__main__':
    app.run(debug=True, port=5001)