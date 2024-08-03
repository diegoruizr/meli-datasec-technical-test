import mysql.connector


db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'meli'
}

# Conectar a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Consulta para obtener los clientes con más de 3 eventos de falla
query = """
SELECT CONCAT(c.first_name,' ',c.last_name) as customer, COUNT(e.dt) as failures
FROM customers c
JOIN campaigns ca ON c.id = ca.customer_id
JOIN events e ON ca.id = e.campaign_id
WHERE e.status = 'failure'
GROUP BY c.first_name, c.last_name
HAVING failures > 3
"""

cursor.execute(query)
results = cursor.fetchall()

# Obtener los nombres de las columnas
column_names = [desc[0] for desc in cursor.description]

# Convertir los resultados a una lista de diccionarios
results_dict = [dict(zip(column_names, row)) for row in results]

print(results_dict)


# Cerrar la conexión
cursor.close()
conn.close()