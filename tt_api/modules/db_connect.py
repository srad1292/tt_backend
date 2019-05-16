from mysql.connector import MySQLConnection, Error
from .db_config_parser import read_db_config

 
 
def connect():
    """ Connect to MySQL database """
 
    db_config = read_db_config()
 
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)
 
        if conn.is_connected():
            print('connection established.')
            return conn
        else:
            print('connection failed.')
            
    except Error as error:
        print(error)
 
    finally:
        #conn.close()
        print('Connection closed.')
 
 