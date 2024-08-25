from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        user_id = "Abhay_21BSA10126"
        email = "abhay.devaki2021@vitbhopal.ac.in"
        roll_number = "21BSA10126"
        print(data)

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
        }
        custom_response = json.dumps(response, ensure_ascii=False, separators=(",", ": "))
        # custom_response = custom_response.replace('"', '“').replace(':', '”:').replace(',', ',”').replace('{', '{\n').replace('}', '\n}').replace('[', '[“').replace(']', '”]')
        print(custom_response)
        return Response(custom_response, mimetype='application/json')
        # return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
