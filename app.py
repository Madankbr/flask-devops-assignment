from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask DevOps Assignment!"

@app.route('/api')
def api():
    return jsonify({
        "name": "Madankbr",
        "course": "DevOps Assignment",
        "status": "active"
    })

if __name__ == '__main__':
    app.run(debug=True)