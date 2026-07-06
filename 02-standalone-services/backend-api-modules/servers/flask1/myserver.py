from flask import Flask, jsonify, request

app = Flask(__name__)

# Empty list to manipulate
data_store = []

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store), 200

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if item:
        data_store.append(item)
        return jsonify({"message": "Item added", "data": item}), 201
    return jsonify({"error": "No item provided"}), 400

@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    if 0 <= index < len(data_store):
        new_value = request.json.get('item')
        data_store[index] = new_value
        return jsonify({"message": "Item updated", "data": new_value}), 200
    return jsonify({"error": "Index out of range"}), 404

@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    if 0 <= index < len(data_store):
        removed_item = data_store.pop(index)
        return jsonify({"message": "Item deleted", "data": removed_item}), 200
    return jsonify({"error": "Index out of range"}), 404

if __name__ == '__main__':
    app.run(debug=True)

# Export app and data store for external use and testing
__all__ = ['app', 'data_store']
