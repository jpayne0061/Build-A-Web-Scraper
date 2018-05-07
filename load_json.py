import json
from create_db import create_connection

def insert_car(conn, car_dict):
    vin = car_dict["vin"]
    mileage = car_dict["mileage"]
    city = car_dict["city"]
    state = car_dict["state"]
    make = car_dict["make"]
    model = car_dict["model"]
    year = car_dict["year"]
    price = car_dict["price"]
    
    car_tuple = (vin, mileage, city, state, make, model, year, price)
    
    insert_statement = ''' insert into cars(vin, mileage, city, state, make, model, year, price )
                                     values(?,?,?,?,?,?,?,?)''' 
    cur = conn.cursor()
    cur.execute(insert_statement, car_tuple)
    return cur.lastrowid


with open('data.json','r') as f:
    conn = create_connection("C:\\sqlite\db\pythonsqlite.db")
    
    with conn:
        for json_line in f:
            car_dictionary = json.loads(json_line)
            insert_car(conn, car_dictionary)



