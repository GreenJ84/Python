from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'dojo survey'

@app.route('/')
def form():

    return render_template('dojo_survey.html')

@app.route('/process', methods=['POST'])
def process():
    session['user_name'] = request.form['user_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    
    return render_template('results.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)