from connect2server import hymndb
from datetime import datetime, timedelta
from mysql.connector import IntegrityError # Handles errors when connecting to the database

cursor = hymndb.cursor()

def find_next_sunday():
    today = datetime.now()
    days_ahead = 6 - today.weekday()
    sunday = today + timedelta(days=days_ahead)
    sunday = sunday.strftime("%Y-%m-%d")
    return sunday

def insert_hymns(opening, sacraments, intermediate, closing):
    date = find_next_sunday()
    tuple = (date, opening, sacraments, intermediate, closing)
    query = """
    INSERT INTO history (date, opening, sacraments, intermediate, closing)
    VALUES (%s,%s, %s, %s, %s);
    """
    try: 
        cursor.execute(query, tuple)
    except IntegrityError as e:
        if e.errno == 1062:
            raise SystemExit("\nYou've already done this week's hymns, go to the history to see them")