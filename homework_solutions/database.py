import sqlite3

def connect_to_database():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    return connection, cursor

def execute_sql(commands: list[str]):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    for one_command in commands:
        cursor.execute(one_command)
    connection.commit()
    connection.close()


def init_database():
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE patients ('name' TEXT, 'doctor' TEXT)")
    cursor.execute("CREATE TABLE doctors ('name' TEXT, 'specialty' TEXT)")
    cursor.execute("CREATE TABLE medicine ('name' TEXT, 'items' INTEGER)")
    connection.commit()
    connection.close()

def add_medicine(name: str, items: int):
    connection = sqlite3.connect("hospital.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO medicine (name, items) VALUES('"+ name + "', "+str(items) + ")")
    connection.commit()
    connection.close()

# add_medicine("nurofen", 100)

def take_medicine(name: str, items_to_remove: int):
    connection, cursor = connect_to_database()
    cursor.execute("SELECT * FROM medicine WHERE name = '" + name + "'")
    medicine = cursor.fetchone()
    connection.close()
    current_items = medicine[1]
    print(medicine)
    current_items -= items_to_remove
    execute_sql(["UPDATE medicine set items=" + str(current_items)+ "WHERE name='" + name + "'"])


def get_all_medicine()-> list[str]:
    connection, cursor = connect_to_database()
    cursor.execute("SELECT name FROM medicine")
    medicines = cursor.fetchall()
    connection.close()
    print(medicines)
    return medicines
get_all_medicine()


# take_medicine("nurofen" , 100)


