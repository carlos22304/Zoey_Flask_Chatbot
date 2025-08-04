from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.get_json()
        message = data.get('message', '').lower()

        if 'history' in message:
            response = "Chattanooga has a rich Civil War history and was a key railroad hub."
        elif 'nature' in message:
            response = "Chattanooga is known for its mountains, riverfront, and outdoor activities."
        elif 'attractions' in message:
            response = "Top attractions include Lookout Mountain, Tennessee Aquarium, and Ruby Falls."
        else:
            response = "I'm not sure about that. Try asking about history, nature, or attractions."

        return jsonify({'response': response})

    return render_template('chat.html')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)




