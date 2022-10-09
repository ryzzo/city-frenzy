"""Program used to fetch data from the sqlite database - capital.db"""
import sqlite3
import random

def fetchRow(id):
    try:
        connection = sqlite3.connect('capital.db')
        cursor = connection.cursor()

        query = """SELECT * FROM country_city WHERE id = ?"""
        cursor.execute(query, (id,))
        
        data = cursor.fetchone()

        cursor.close()

    except sqlite3.Error as error:
        print("Error: ", error)
    
    finally:
        if connection:
            connection.close()
    
    return data

# TRY TO INCLUDE COUNTRIES THAT HAVE ALREADY BEEN CHOSEN
def getCapital():
    """Retrieve random capital"""
    id = random.randint(0, 238)
    data = fetchRow(id)
    return data
