from flask import Flask, redirect, session, render_template, request
app = Flask(__name__)
app.secret_key = 'Guessing game'
import random

@app.route('/')
def numbers_Game():

    if 'answer' not in session:
        session['answer']= round(random.random() *100)
    if 'attempts' not in session:
        session['attempts'] = 0
        session['remaining']= 5
    if 'x' not in session:
        session['x']=0
    if 'guess' in session:
        print(session['guess'])
    print(session['answer'])
    return render_template('numbers_game.html', x=session['x'], answer=session['answer'])

@app.route('/guessing', methods=['POST'])
def guessing():
    session['guess'] = int(request.form['guess'])
    session['x'] += 1
    session['attempts']+= 1
    session['remaining']-=1
    print(request.form['guess'])
    print(session['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, port=5001)