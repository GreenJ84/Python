from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# ================= Add Ninja Page ====================

@app.route('/new_ninja')
def add_ninja_display():

    dojos = Dojo.get_dojos()

    return render_template('new_ninja.html', all_dojos=dojos)


# ================= GET ALL DOJOS====================
@app.route('/new_ninja/create', methods=['POST'])
def create_new_ninja():

    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    print(data)
    dojo_updated = request.form['dojo_id']
    Ninja.add_ninja(data)

    dojo_name = Dojo.get_dojo_name(data)

    return redirect(f'/dojo/{dojo_updated}/{dojo_name}')