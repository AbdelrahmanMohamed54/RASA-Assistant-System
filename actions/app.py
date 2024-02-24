from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
   return "Welcome to the Mezo Application Assistant System"


@app.route('/test_action', methods=['GET'])
def test_action():
    return jsonify({"message": "This is a test response from Flask API"})


@app.route('/get_program_info', methods=['GET'])
def get_program_info():
    # Load data from the JSON file
    with open('new.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
