import mysql.connector
from mysql.connector import errorcode # Handles errors when connecting to the database

import json # for getting data to connect to the database

# TODO: Implement a try/except block to handle errors when connecting to the database

with open('serverInfo.json') as file:
    data = json.load(file)

server_data = data["server"]

hymndb = mysql.connector.connect(
    host=server_data['ip'], 
    user=server_data['user'], 
    password=server_data['password'], 
    database=server_data['database'],) 


# hymndb.autocommit = True
cursor = hymndb.cursor

# cursor = hymndb.cursor(buffered=True) # buffered=True allows for multiple queries to be executed at once