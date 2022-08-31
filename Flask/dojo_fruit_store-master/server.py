from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    fruits= int(request.form['raspberry']) +int(request.form['apple']) + int(request.form['strawberry'])
    fullName= request.form['first_name'] + request.form['last_name']
    print(request.form)
    print(f'Charging {fullName} for {fruits} fruits')
    return render_template("checkout.html",  raspberry= request.form['raspberry'], apple= request.form['apple'], strawberry=request.form['strawberry'], firstName=request.form['first_name'], lastName=request.form['last_name'], student_id=request.form['student_id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, port=5001)    