import pymysql
import json
from tools import Tools

# create tools
tools = Tools()

path_to_config = "./config"
path_to_sql = "./TinyHippo.sql"

# load config of database
config = tools.get_config(path_to_config)

# connect to dataset
db = pymysql.connect(host=config['localhost']['host'],
                     user=config['localhost']['user'],
                     password=config['localhost']['password'],
                     charset=config['localhost']['charset'])
# create a cursor
cursor = db.cursor()

# create dataset and tables
with open(path_to_sql) as f:
    sql_list = f.read().split(';')[:-1]
    for sql in sql_list:
        cursor.execute(sql + ';')
db.commit()

# close the connection
db.close()
