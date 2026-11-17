
from faker import Faker
from tabulate import tabulate

# Эта библиотека нужна для генерации вымышленных данных
f = Faker("en_US")

computers = []

for i in range(10):
    model = f.word().capitalize()
    owner = f.first_name()
    email = f.email()
    price = f.random_int(min=300, max=2000)
    year = f.random_int(min=2018, max=2026)

    computers.append([model, owner, email, price, year])

print("Информация о компьютерах:")

print(tabulate(
    computers,
    headers=["Модель", "Владелец", "Email", "Цена (€)", "Год"],
    tablefmt="grid"
))
