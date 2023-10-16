import csv
import database as db

PW = "aka123"  # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "akaroot"
DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"  # considering you have installed MySQL server on your computer

RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
PRODUCTS = 'products'
ORDER = 'orders'

connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB
db.create_and_switch_database(connection, DB, DB)

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

#creating user table\
create_users_table = """"""
CREATE TABLE IF NOT EXISTS users (
    user_id varchar(10) PRIMARY KEY,
    user_name varchar(45) NOT NULL,
    user_email varchar(45) NOT NULL,
    user_password varchar(45) NOT NULL,
    user_address varchar(45) NULL,
    is_vendor tinyint(1) DEFAULT 0
)
""""""
create_product_table = ""
CREATE TABLE IF NOT EXISTS products (
    product_id varchar(45) NOT NULL PRIMARY KEY,
    product_name varchar(45) NOT NULL,
    product_description varchar(100) NOT NULL,
    product_price float(45) NOT NULL,
    emi_avaliable varchar(10) NOT NULL,
    vendor_id varchar(10) NOT NULL
    CONSTRAINT 'fk_vendor_id' FOREIGN KEY ('vendor_id') REFERENCES 'users' ('user_id')
)
""""""

create_orders_table = """"""
CREATE TABLE IF NOT EXISTS orders (
     order_id int NOT NULL PRIMARY KEY,
     total_value float(45) NOT NULL,
     order_quantity int NOT NULL,
     reward_point int NOT NULL,
     vendor_id varchar(10) NOT NULL,
     customer_id varchar(10) NOT NULL,
     CONSTRAINT 'vendor_id' FOREIGN KEY ('vendor_id') REFRENCES 'users' ('user_id')
     CONSTRAINT 'customer_id' FORIEGN KEY ('customer_id') REFRENCES 'users' ('user_id')
)
""""""
#creating customer leaderboard table 
create_customer_leaderboard = """
CREATE TABLE customer_leaderboard(
     customer_id varchar(10) NOT NULL PRIMARY KEY,
     total_value float(45) NOT NULL,
     customer_name varchar(50) NOT NULL,
     customer_email varchar(50) NOT NULL,
     CONSTRAINT 'fk_customer_id' FOREIGN KEY('customer_id') REFERENCES 'users' ('user_id'
     )
     """


print("--------------E-commerce data storage solution--------------")
print("\n")
print("-----------Solution - Problem 1.a------------")
connection = db.create_server_connection(LOCALHOST, ROOT,PW)
print("---------------Solution - Problem 1.a id complete.------------------")
print("\n")
print("-------------------Solution - problem 1.b ---------------")
print("intiating creation of tables: ")

db.create_table(connection, create_users_table)
print("Users table created")
db.create_table(connection, create_product_table)
print("Products table created")
db.create_table(connection, create_customer_leaderboard)
print("Customer leader board table created")
print("--------------Solution - Problem 1.b is complete.-----------")
print("\n")

print("-------------Solution - Problem 2.a -------------------")
print("initiating data insertion in user table.")

with open(RELATIVE_CONFIG_PATH + USER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
   sql=''''''
INSERT INTO users (user_id, user_name, user_email, user_password, user_address, is_vendor)
VALUES (%s, %s, %s, %s,%s, %s)
''''''
 val.pop(0)
db.insert_many_records(connection, sql, val)
print("data insertion in user table is complete.")

print("initiating data insertion in products table.")
with open(RELATIVE_CONFIG_PATH + PRODUCTS + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = ''''''
    INSERT INTO PRODUCTS (product_id, product_name, product_price, product_description, vendor_id, emi_avaliable)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''''''
    val.pop(0)
    db.insert_many_records(connection, sql, val)
print("Data insertion in products table is complete.")

print("initiating data insertion in Order table.")
with open(RELATIVE_CONFIG_PATH + ORDER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = '''''' 
    INSERT INTO orders (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''''''    
    val.pop(0)
    db.insert_many_records(connection, sql, val)

print("Data insertion in order table is complete.")
print("-----------Solution - Problem 2.a is complete.--------------")
   
