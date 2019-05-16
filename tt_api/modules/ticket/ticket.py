from mysql.connector import MySQLConnection, Error
from tt_api.modules import db_connect as db_connect

def getTicket(id=0):
    ticket = {}
    try:
        conn = db_connect.connect()
        if conn.is_connected():
            cursor = conn.cursor(dictionary=True)
            query = """SELECT * FROM dev_ticket WHERE id = %s"""
            data = (id, )
            cursor.execute(query,data)
            ticket = cursor.fetchone()
    
            cursor.close()
            conn.close()


    except Error as e:
        ticket = {'name': str(e)}
 
    finally:
        return ticket