import os
from configparser import ConfigParser
 
 
def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    # check if the path is to a valid file
    if not os.path.isfile(config_path):
        raise Exception('Config.ini file not found')
    
    parser.read(config_path)
 
    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return db

##def read_db_config():
##    db = {}
##    db['host'] = 'localhost'
##    db['database'] = 'toh-db'
##    db['user'] = 'root'
##    db['password'] = 'Mcbrother1292'
##    return db
##
##def test():
##    return 'hello from parser'
