from connect2server import hymndb

cursor = hymndb.cursor()

def get_opening_hymn():
    query = """
    SELECT h.h_id, h.h_title
    FROM hymns h
    LEFT JOIN (
        SELECT opening
        FROM history
        ORDER BY date DESC
        LIMIT 40
    ) AS recent ON h.h_id = recent.opening
    WHERE h.position = 1 
    AND recent.opening IS NULL
    ORDER BY RAND()
    LIMIT 1;
    """

    cursor.execute(query)
    selection = cursor.fetchone()
    
    # Return a list: selection[0] = hymn number, selection[1] = hymn title
    return selection

def get_sacrament_hymn():
    query = """
    SELECT h.h_id, h.h_title
    FROM hymns h
    LEFT JOIN (
        SELECT sacraments
        FROM history
        ORDER BY date DESC
        LIMIT 20
    ) AS recent ON h.h_id = recent.sacraments
    WHERE h.position = 2 
    AND recent.sacraments IS NULL
    ORDER BY RAND()
    LIMIT 1;
    """

    cursor.execute(query)
    selection = cursor.fetchone()
    
    # Return a list: selection[0] = hymn number, selection[1] = hymn title
    return selection

def get_intermediate_hymn():
    query = """
    SELECT h.h_id, h.h_title
    FROM hymns h
    LEFT JOIN (
        SELECT intermediate
        FROM history
        ORDER BY date DESC
        LIMIT 40
    ) AS recent ON h.h_id = recent.intermediate
    WHERE h.position IS NULL 
    AND recent.intermediate IS NULL
    ORDER BY RAND()
    LIMIT 1;
    """
    
    cursor.execute(query)
    selection = cursor.fetchone()
    
    # Return a list: selection[0] = hymn number, selection[1] = hymn title
    return selection

def get_closing_hymn():
    query = """
    SELECT h.h_id, h.h_title
    FROM hymns h
    LEFT JOIN (
        SELECT intermediate
        FROM history
        ORDER BY date DESC
        LIMIT 40
    ) AS recent ON h.h_id = recent.intermediate
    WHERE h.position IS NULL OR h.position = 4
    AND recent.intermediate IS NULL
    ORDER BY RAND()
    LIMIT 1;
    """
    
    cursor.execute(query)
    selection = cursor.fetchone()
    
    # Return a list: selection[0] = hymn number, selection[1] = hymn title
    return selection