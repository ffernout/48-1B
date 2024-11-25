import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
        return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')

def insert_products(connection, products):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = connection.cursor
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCTS function')

def update_quantity(connection, products):
    try:
        sql = '''UPDATE products SET quantity=? WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY function')

def update_price(connection, products):
    try:
        sql = '''UPDATE products SET price=? WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE function')

def delete_by_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_BY_ID function')

def select_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL function')

def select_by_prise_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products
        WHERE price <=? AND quantity >=?'''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_PRISE_QUANTITY function')

def select_by_name(connection, limit):
    try:
        sql = '''SELECT * FROM products
        WHERE product_title LIKE '%cabbage%'
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_NAME function')


sql_to_create_products_table = '''
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
     product_title VARCHAR (200) NOT NULL, 
     price FLOAT(10, 2) NOT NULL DEFAULT 0.0
     quantity INTEGER NOT NULL DEFAULT 0
     )
'''

my_connection = create_connection('hw.db')
if my_connection:
    print('Connected successfully!')
    create_table(my_connection, sql_to_create_products_table)
    # insert_products(my_connection, ('Milk', 100.50, 6))
    # insert_products(my_connection, ('Classic cabbage', 90.50, 10))
    # insert_products(my_connection, ('Red cabbage', 130.50, 8))
    # insert_products(my_connection, ('Savoy cabbage', 150.50, 6))
    # insert_products(my_connection, ('Cocoa', 80.10, 15))
    # insert_products(my_connection, ('potato', 30.50, 20))
    # insert_products(my_connection, ('Cucumbers', 50.50, 20))
    # insert_products(my_connection, ('Tomatoes', 60.70, 20))
    # insert_products(my_connection, ('', 100.50, 6))
    # insert_products(my_connection, ('Cat food', 80.00, 15))
    # insert_products(my_connection, ('Dog food', 80.00, 15))
    # insert_products(my_connection, ('Buns', 99.99, 10))
    # insert_products(my_connection, ('Meat', 160.50, 5))
    # insert_products(my_connection, ('Onion', 20.50, 15))
    # insert_products(my_connection, ('Sugar', 70.50, 10))
    # update_price(my_connection, (200, 15))
    # update_quantity(my_connection, (15, 5))
    # delete_by_id(my_connection, 1)
    select_all(my_connection)
    select_by_prise_quantity(my_connection, (100, 3))
    select_by_name(my_connection)
