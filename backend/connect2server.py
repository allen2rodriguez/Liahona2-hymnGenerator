import mysql.connector
import json # for getting data to connect to the database

with open('serverInfo.json') as file:
    data = json.load(file)
server_data = data["server"]

hymndb = mysql.connector.connect(
    host=server_data['ip'], 
    user=server_data['user'], 
    password=server_data['password'], 
    database=server_data['database'],)
hymndb.autocommit = True

# cursor = hymndb.cursor(dictionary=True) Consider implementing this