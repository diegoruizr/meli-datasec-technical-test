# meli-datasec-technical-test

## Point One
Point one is located in the file point_1.py, in this section, the "Minesweeper Number of Neighbouring Mines" was implemented. To modify the input, the variable `input_minesweeper` should be adjusted, where mines are represented by `1` and empty spaces by `0`.

## Point Two
Point one is located in the file point_2.py, in this section, As a first step, install the Flask dependency `pip install Flask` and run the file to start the local API server, as a next step, there is only one route:

- ## **Input**

    http://127.0.0.1:5000/api/shows?page={page}&genre={genre}

    **For example**

    http://127.0.0.1:5000/api/shows?page=1&genre=Drama

- ## **Output**
    The name of the series will be displayed in the browser of preference

    `Breaking Bad`

## Point Three
Point one is located in the file point_2.py, in this section, a connection.py file was created to migrate the data to be migrated in the local database (`MySQL`), this file represents the data in JSON format, with the creation of the tables (`customers`, `campaigns` and `events`), and the insertion of each of the data.

The configuration data for the connection to the MySQL database requires installing the MySQL driver for Python `pip install mysql-connector-python`.

- ## **Input**

    `db_config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'meli'
    }`

- ## **Output**

    customer: Whitney Ferrero, failures: 6
