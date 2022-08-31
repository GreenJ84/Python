from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key='dojo counter'


@app.route('/')
def counter():
    if 'visit' not in session:
        session['visit']= 1
    else:
        session['visit'] += 1
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1 
    return render_template('counter.html')

@app.route('/add_to_counter')
def add_counter():
    session['counter'] = session['counter'] + 1
    return redirect('/')

@app.route('/customAdd', methods=['POST'])
def customAdd():
    session['counter'] = session['counter'] + (int(request.form['customNum'])-1)
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)