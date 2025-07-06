
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    product_id = request.get_json().get('product_id')
    return_id = products_dao.delete_product(product_id)
    return jsonify({'product_id': return_id})

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders()
    return jsonify(response)
