from connect2server import hymndb
from datetime import datetime, timedelta

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
    cursor.execute(query, tuple)
    hymndb.commit()

    # Try catch whenever it attempts a duplicate entry for the same date
    # "You've already done this weeks hymns, go to the history to see them"
