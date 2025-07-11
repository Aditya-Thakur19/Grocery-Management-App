from sql_connection import get_sql_connection

def get_uoms():
    connection = get_sql_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM uom"
    cursor.execute(query)

    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })

    cursor.close()
    connection.close()
    return response
