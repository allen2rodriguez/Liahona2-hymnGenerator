from connect2server import hymndb

cursor = hymndb.cursor()

def get_history(number_shown: int):
    query = """
    SELECT * 
    FROM history 
    ORDER BY date DESC
    LIMIT %s
    """

    cursor.execute(query, (number_shown,))
    results = cursor.fetchall()
    
    return results

def make_changes(date: str, position: str, hymn_number: int):
    query = f"""
    UPDATE history
    SET {position} = %s
    WHERE date = %s
    """
    
    cursor.execute(query, (hymn_number, date))
    hymndb.commit()
    
    print("Changes made succesfully")
