from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Example route
@app.route('/')
def home():
    return "Welcome to the Flask API Service"

# Route to fetch and transform data
@app.route('/get-data', methods=['GET'])
def get_data():
    # Example external API URL
    external_api_url = "https://api.example.com/data"

    # Call the external API
    response = requests.get(external_api_url)
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

    data = response.json()

    # Transform the data (example transformation)
    transformed_data = transform_data(data)

    return jsonify(transformed_data)

def transform_data(data):
    # Perform some transformation on the data
    # For example, let's extract some fields and rename them
    transformed = {
        "new_field_1": data.get("old_field_1"),
        "new_field_2": data.get("old_field_2"),
        # Add more transformations as needed
    }
    return transformed

if __name__ == '__main__':
    app.run(debug=True)

# transform data

    
