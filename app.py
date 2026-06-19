from flask import Flask, jsonify, request, render_template

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

@app.route('/todo')
def todo():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)