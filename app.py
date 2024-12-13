from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__,static_folder='static', template_folder='templates')

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
machine_color = random.choice(colors)
attempts = 0
max_attempts = 5
games_won = 0
games_lost = 0
player_name = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global player_name, attempts, machine_color
    player_name = request.form['player_name']
    attempts = 0
    machine_color = random.choice(colors)
    return redirect(url_for('game'))

@app.route('/game')
def game():
    return render_template('game.html', attempts=attempts, max_attempts=max_attempts)

@app.route('/guess', methods=['POST'])
def guess():
    global attempts, games_won, games_lost, machine_color
    user_color = request.form['color'].lower()
    attempts += 1
    if user_color not in colors:
        return render_template('game.html', attempts=attempts, max_attempts=max_attempts, message="Invalid color. Please try again.")
    
    if user_color == machine_color:
        games_won += 1
        message = f"You won the game! Number of attempts: {attempts}. Total number of attempts: {max_attempts}."
        return render_template('options.html', message=message)
    elif attempts >= max_attempts:
        games_lost += 1
        return redirect(url_for('options'))
    else:
        attempts_left = max_attempts - attempts
        return render_template('game.html', attempts=attempts, max_attempts=max_attempts, message=f"Your guess was wrong. Please try again. Number of attempts left: {attempts_left}.")

@app.route('/options')
def options():
    return render_template('options.html')

@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html', games_won=games_won, games_lost=games_lost, player_name=player_name)

if __name__ == '__main__':
    app.run(debug=True)
