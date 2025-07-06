from sql_connection import get_sql_connection

def get_all_products():
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = """
        SELECT products.product_id, products.name, products.uom_id, 
               products.price_per_unit, uom.uom_name 
        FROM products 
        INNER JOIN uom ON products.uom_id = uom.uom_id 
        ORDER BY products.product_id ASC
    """
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    cursor.close()
    connection.close()
    return response


def insert_new_product(product):
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    data = (product["product_name"], product["uom_id"], product["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()
    new_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return new_id


def delete_product(product_id):
    connection = get_sql_connection()
    cursor = connection.cursor()
    query = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return product_id
