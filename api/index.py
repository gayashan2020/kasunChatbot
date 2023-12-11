# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from openai import OpenAI

# app = Flask(__name__)
# CORS(app)

# # Set your API key here
# api_key = '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'
# client = OpenAI(api_key=api_key)

# def get_response(message):
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "user", "content": message}],
#         model="gpt-4-1106-preview",
#     )
#     return chat_completion.choices[0].message.content

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.json
#     message = data['message']
#     response = get_response(message)
#     return jsonify({"response": response})


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
