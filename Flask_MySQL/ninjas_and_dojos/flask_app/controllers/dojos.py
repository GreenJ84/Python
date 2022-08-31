from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


# ================= GET ALL DOJOS====================

@app.route('/')
def index():

    dojos = Dojo.get_dojos()

    return render_template('dojos.html', all_dojos = dojos)


# ================= Create New DOJO==================== "Insert"

@app.route('/dojo/create_dojo', methods=['POST'])
def create_dojo():

    data = {
        'name': request.form['name']
    }
    this_dojo_name = request.form['name']

    created_under = Dojo.create_new_dojo(data)

    return redirect(f'/dojo/{created_under}/{this_dojo_name}')


# ================= SOLO DOJO PAGE  ==================== "Select specific dojo"

@app.route('/dojo/<int:dojo_id>/<dojo_name>')
def dojo_display(dojo_id, dojo_name):
    
    data = {
        "dojo_id": dojo_id
    }
    
    ninjas = Ninja.get_dojo_ninjas(data)
    this_dojo_name = dojo_name
    
    return render_template('display_dojo.html', dojo_ninjas = ninjas, dojo_name = this_dojo_name)

