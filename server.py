from flask import Flask, request, jsonify, render_template
import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

# ✅ HTML Pages
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def order_page():
    products = products_dao.get_all_products()
    return render_template('order.html', products=products)

@app.route('/admin')
def admin_page():
    products = products_dao.get_all_products()
    return render_template('index.html', products=products)

# ✅ API Endpoints
@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms()
    return jsonify(response)

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        response = products_dao.get_all_products()
        return jsonify(response)
    except Exception as e:
        print("Error in /getProducts:", str(e))
        return jsonify({'error': 'Failed to fetch products'}), 500

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = request.get_json()
    product_id = products_dao.insert_new_product(request_payload)
    return jsonify({'product_id': product_id})

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_id = request.get_json().get('product_id')
    return_id = products_dao.delete_product(product_id)
    return jsonify({'product_id': return_id})

# ⚠️ Dummy routes for Orders
@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    # Return empty list
    return jsonify([])

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    # Pretend we saved it
    print("Received order payload (ignored):", request.get_json())
    return jsonify({'order_id': 1})

# ✅ Run
if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000, debug=True)
