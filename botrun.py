import threading
from flask import Flask
from maze import Paths
import json
from flask import request

with open('token.json') as config_file:
    config = json.load(config_file)

# Extract the token from the configuration
token = config['token']

app = Flask(__name__)
bot = Paths()

@app.route('/')
def index():
    return 'Welcome to my bot!'

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = bot.generate_response(user_input)
    return bot_response

def run_flask():
    app.run(debug=True)

def run_bot():
    bot.run(token)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_bot)

    flask_thread.start()
    bot_thread.start()