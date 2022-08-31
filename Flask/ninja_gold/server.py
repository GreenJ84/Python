from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'ninja_gold'

@app.route('/')
def ninjaGold():
    if 'gold' not in session:
        session['gold']=0
    if 'activities' not in session:
        session['activities'] = []
    return render_template('ninja_gold.html')

@app.route('/process_money/farm')
def farm_money():
    import random
    import datetime
    now = datetime.datetime.now()
    farm_gamble = round(random.randint(10, 20))
    session['gold'] = session['gold'] + farm_gamble
    session['activities'].append(f'Earned {farm_gamble} golds from the Farm!    ({now})')
    return redirect('/')

@app.route('/process_money/cave')
def cave_money():
    import random
    import datetime
    now = datetime.datetime.now()
    cave_gamble = round(random.randint(5, 20))
    session['gold'] = session['gold'] + cave_gamble
    session['activities'].append(f'Earned {cave_gamble} golds from the Farm!    ({now})')
    return redirect('/')

@app.route('/process_money/house')
def house_money():
    import random
    import datetime
    now = datetime.datetime.now()
    house_gamble = round(random.randint(2, 5))
    session['gold'] = session['gold'] + house_gamble
    session['activities'].append(f'Earned {house_gamble} golds from the Farm!    ({now})')
    return redirect('/')

@app.route('/process_money/casino')
def casino_money():
    import random
    import datetime
    now = datetime.datetime.now()
    win_loss= [1, -1]
    casino_gamble = round(random.randint(5, 20)*random.choice(win_loss))
    session['gold'] = session['gold'] + casino_gamble
    if casino_gamble > 0:
        session['activities'].append(f'Entered a casino and won {casino_gamble} golds!    ({now})')
    else:
        session['activities'].append(f'Entered a Casino and lost {casino_gamble} golds!    ({now})')
    return redirect('/')

@app.route('/cash_out')
def cash_out():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=5001)