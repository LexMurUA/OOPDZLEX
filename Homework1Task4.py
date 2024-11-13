# Завдання 4
# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список 
# автомобілів, доступних для продажу, і функцію продажу заданого автомобіля.

class Cars:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car model: {self.model}"

class Cardealer:
    def __init__(self):
        self.list_of_cars_for_sale = []

    def add_car(self, car):
        self.list_of_cars_for_sale.append(car)
        print(f"Car {car} has been added to the inventory.")

    def sell_car(self, car):
        if car in self.list_of_cars_for_sale:
            self.list_of_cars_for_sale.remove(car)
            print(f"Car {car} has been sold.")
        else:
            print(f"Car {car} is not available for sale.")

# Створення екземпляра автомобіля
car1 = Cars("Tesla Model S")

# Створення екземпляра автосалону
car_dealer = Cardealer()

# Додавання автомобіля до списку автомобілів на продаж
car_dealer.add_car(car1)

# Виведення інформації про автомобіль
print(car1)

# Продаж автомобіля
car_dealer.sell_car(car1)
