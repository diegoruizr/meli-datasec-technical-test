import mysql.connector

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'meli'
}

# Datos a migrar customers
customers_to_migrate = [
    {'id': 1, 'first_name': 'Whitney', 'last_name': 'Ferrero'},
    {'id': 2, 'first_name': 'Dickie', 'last_name': 'Romera'}
]

# Datos a migrar campaigns
campaigns_to_migrate = [
    {'id': 1, 'customer_id': 1, 'name': 'Upton Group'},
    {'id': 2, 'customer_id': 1, 'name': 'Roob, Hudson and Rippin'},
    {'id': 3, 'customer_id': 1, 'name': 'McCullough, Rempel and Larson'},
    {'id': 4, 'customer_id': 1, 'name': 'Lang and Sons'},
    {'id': 5, 'customer_id': 2, 'name': 'Ruecker, Hand and Haley'}
]

# Datos a migrar events
events_to_migrate = [
    {'dt': '2021-12-02 13:52:00', 'campaign_id': 1, 'status': 'failure'},
    {'dt': '2021-12-02 08:17:48', 'campaign_id': 2, 'status': 'failure'},
    {'dt': '2021-12-02 08:18:17', 'campaign_id': 2, 'status': 'failure'},
    {'dt': '2021-12-01 11:55:32', 'campaign_id': 3, 'status': 'failure'},
    {'dt': '2021-12-01 06:53:16', 'campaign_id': 4, 'status': 'failure'},
    {'dt': '2021-12-02 04:51:09', 'campaign_id': 4, 'status': 'failure'},
    {'dt': '2021-12-01 06:34:04', 'campaign_id': 5, 'status': 'failure'},
    {'dt': '2021-12-02 03:21:18', 'campaign_id': 5, 'status': 'failure'},
    {'dt': '2021-12-01 03:18:24', 'campaign_id': 5, 'status': 'failure'},
    {'dt': '2021-12-02 15:32:37', 'campaign_id': 1, 'status': 'success'},
    {'dt': '2021-12-01 04:23:20', 'campaign_id': 1, 'status': 'success'},
    {'dt': '2021-12-02 06:53:24', 'campaign_id': 1, 'status': 'success'},
    {'dt': '2021-12-02 08:01:02', 'campaign_id': 2, 'status': 'success'},
    {'dt': '2021-12-01 15:57:19', 'campaign_id': 2, 'status': 'success'},
    {'dt': '2021-12-02 16:14:34', 'campaign_id': 3, 'status': 'success'},
    {'dt': '2021-12-02 21:56:38', 'campaign_id': 3, 'status': 'success'},
    {'dt': '2021-12-01 05:54:43', 'campaign_id': 4, 'status': 'success'},
    {'dt': '2021-12-02 17:56:45', 'campaign_id': 4, 'status': 'success'},
    {'dt': '2021-12-02 11:56:50', 'campaign_id': 4, 'status': 'success'},
    {'dt': '2021-12-02 06:08:20', 'campaign_id': 5, 'status': 'success'}
]

# Conectar a la base de datos
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Crear la tabla si no existe
create_table_customers_query = """
CREATE TABLE IF NOT EXISTS customers (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Customer ID',
    first_name VARCHAR(64) COMMENT 'Customer first name',
    last_name VARCHAR(64) COMMENT 'Customer last name'
)
"""

create_table_campaigns_query = """
CREATE TABLE IF NOT EXISTS campaigns (
    id SMALLINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Campaign ID',
    customer_id VARCHAR(64) COMMENT 'Customer ID',
    name VARCHAR(64) COMMENT 'Campaign name'
)
"""

create_table_events_query = """
CREATE TABLE IF NOT EXISTS events (
    dt VARCHAR(19) COMMENT 'Event timestamp',
    campaign_id SMALLINT COMMENT 'Campaign ID',
    status VARCHAR(64) COMMENT 'Event status'
)
"""
cursor.execute(create_table_customers_query)
cursor.execute(create_table_campaigns_query)
cursor.execute(create_table_events_query)

# Insertar datos en la tabla customers
insert_customers_query = """
INSERT INTO customers (id, first_name, last_name)
VALUES (%s, %s, %s)
"""

# Insertar datos en la tabla campaigns
insert_campaigns_query = """
INSERT INTO campaigns (id, customer_id, name)
VALUES (%s, %s, %s)
"""

# Insertar datos en la tabla events
insert_events_query = """
INSERT INTO events (dt, campaign_id, status)
VALUES (%s, %s, %s)
"""

for customer in customers_to_migrate:
    cursor.execute(insert_customers_query, (customer['id'], customer['first_name'], customer['last_name']))

for campaign in campaigns_to_migrate:
    cursor.execute(insert_campaigns_query, (campaign['id'], campaign['customer_id'], campaign['name']))

for event in events_to_migrate:
    cursor.execute(insert_events_query, (event['dt'], event['campaign_id'], event['status']))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()

print("Migración completada con éxito.")