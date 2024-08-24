# app.py
from flask import Flask, jsonify

app = Flask(__name__)

# Contoh data produk
products = [
    {"id": 1, "name": "Laptop", "price": 800},
    {"id": 2, "name": "Smartphone", "price": 600},
    {"id": 3, "name": "Tablet", "price": 300}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
