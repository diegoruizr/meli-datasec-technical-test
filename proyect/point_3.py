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
SELECT c.first_name, c.last_name, COUNT(e.dt) as failures
FROM customers c
JOIN campaigns ca ON c.id = ca.customer_id
JOIN events e ON ca.id = e.campaign_id
WHERE e.status = 'failure'
GROUP BY c.first_name, c.last_name
HAVING failures > 3
"""

cursor.execute(query)
results = cursor.fetchall()

# Imprimir los resultados
for row in results:
    first_name, last_name, failures = row
    print(f"customer: {first_name} {last_name}, failures: {failures}")

# Cerrar la conexión
cursor.close()
conn.close()