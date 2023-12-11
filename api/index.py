from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Set your API key here
api_key = 'your-api-key'
client = OpenAI(api_key=api_key)

def get_response(message):
    return message
    # chat_completion = client.chat.completions.create(
    #     messages=[{"role": "user", "content": message}],
    #     model="gpt-4-1106-preview",
    # )
    # return chat_completion.choices[0].message.content

@app.route('/chat', methods=['GET'])
def chat():
    message = request.args.get('message')  # Get message from query string
    if message:
        response = get_response(message)
        return jsonify({"response": response})
    else:
        return jsonify({"error": "No message provided"}), 400

