import sqlite3
#A4
connect = sqlite3.connect('user.db')
#рука с ручкой
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        name Varchar (50) NOT NULL,
        age INTENGER NOT NULL ,
        hobby Text 
    )
""")

connect.commit()
# Crud - Create Read Update Delete
def create_student(name, age, hobby):
    """здесь создаем студентов"""
    cursor.execute(
        "INSERT INTO student(name, age, hobby) VALUES (?, ?, ?)",
        (name, age, hobby)

    )
#     cursor.execute('INSERT INTO student(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
#     print('студент cоздан !!')
    connect.commit()
create_student('John Doe', 17, 'ski')

