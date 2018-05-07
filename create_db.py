import sqlite3
from sqlite3 import Error

create_cars_table_statement = """ CREATE TABLE IF NOT EXISTS cars (
                                    id integer PRIMARY KEY,
                                    vin text, 
                                    mileage int,
                                    city text,
                                    state text,
                                    make text,
                                    model text,
                                    year int,
                                    price int
                                    
                                ); """
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
        
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    conn = create_connection("C:\\sqlite\db\pythonsqlite.db")
    create_table(conn, create_cars_table_statement)
    
main()
    
    
    
    
    
    
    
    