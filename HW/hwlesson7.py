import sqlite3

connection = sqlite3.connect('store.db')
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    price INTEGER,
    quantity INTEGER
)
""")

def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
)

    print("product created successfully")
connection.commit()
# create_product("Chocolate", 50, 100  )
# create_product("Coke", 99, 200 )
# create_product("Chips", 250, 100  )
# create_product("Bread", 99, 100  )
def read_product():
    cursor.execute(
        "SELECT * FROM products")
    products = cursor.fetchall()
    for i in products:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]}")
read_product()

connection.commit()
def update_product(id,price):
   cursor.execute(
        "UPDATE poducts SET price=? WHERE id=?",
        (id, price)
)

print("product updated successfully")

def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id=?",
        (id,)
    )
    connection.commit()
    print("product deleted successfully")



