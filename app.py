from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
todo_collection = db["todo_items"]

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

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "Item added successfully",
        "itemName": item_name,
        "itemDescription": item_description
    }), 201

if __name__ == '__main__':
    app.run(debug=True)