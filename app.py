# app.py
from flask import Flask, render_template, jsonify, request
from tamagotchi import Tamagotchi

app = Flask(__name__)

# Initialize your Tamagotchi pet
pet = Tamagotchi(name="Fluffy")

@app.route('/')
def home():
    return render_template('index.html', pet=pet.get_status())

@app.route('/feed', methods=['POST'])
def feed():
    pet.feed()
    return jsonify(pet.get_status())

@app.route('/play', methods=['POST'])
def play():
    pet.play()
    return jsonify(pet.get_status())

if __name__ == '__main__':
    app.run(debug=True)
