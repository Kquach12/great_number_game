from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'blah blah'

@app.route('/')
def guess():
    if 'number' not in session:
        session['number'] = random.randrange(1,100)
        session['attempts'] = 0

    return render_template('index.html')

@app.route('/check', methods=["POST"])
def check():
    if not request.form['guess_value']:
        return redirect('/')
    session['guess_value'] = int(request.form['guess_value'])
    session['attempts'] += 1

    return redirect ('/')


@app.route('/reset')
def reset():
    session.pop('attempts')
    session.pop('guess_value')
    session.pop('number')
    return redirect('/')

@app.route('/joinleaderboard', methods = ["POST"])
def joinleaderboard():
    if 'leaderboard' not in session:
        session['leaderboard'] = []
    session['name'] = request.form['name']
    session['leaderboard'].append({'name': session['name'], 'attempts': session['attempts']})
    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

if __name__ == "__main__":
    app.run(debug = True)