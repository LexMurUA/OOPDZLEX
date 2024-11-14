
class Car:
    def __init__(self, model: str, year: int, color: str, weight: float, speed: int, price: int, quantity_of_wheels: int, engine: str):
        self.model = model
        self.year = year
        self.color = color
        self.__weight = weight
        self._speed = speed
        self.__price = price
        self.__quantity_of_wheels = quantity_of_wheels
        self.__engine = engine
    
    # ========Getters and Setters========
    def set__price(self, price):
        if price is None or price <= 0:
            print(f'Price must be a positive number, not {price}')
        else:
            self.__price = price
    
    def get__price(self):
        return self.__price
    
    def set__weight(self, weight):
        if weight is None or weight <= 0:
            print(f'Weight must be a positive number, not {weight}')
        else:
            self.__weight = weight
    
    def get__weight(self):
        return self.__weight

    def set__speed(self, speed):
        if speed is None or speed <= 0:
            print(f'Speed must be a positive number, not {speed}')
        else:
            self._speed = speed
    
    def get__speed(self):
        return self._speed

    def set__quantity_of_wheels(self, quantity_of_wheels):
        if quantity_of_wheels is None or quantity_of_wheels < 4:
            print(f'Quantity of wheels must be at least 4, not {quantity_of_wheels}')
        else:
            self.__quantity_of_wheels = quantity_of_wheels

    def get__quantity_of_wheels(self):
        return self.__quantity_of_wheels

    def set__engine(self, engine):
        if engine is None or engine.lower() not in ['diesel', 'gasoline']:
            print(f'Engine must be either Diesel or Gasoline, not {engine}')
        else:
            self.__engine = engine
    
    @property
    def engine(self):
        return self.__engine

    # ========Methods=========
    def get_info(self):
        print(f'Car Model: {self.model}, Year: {self.year}, Color: {self.color}')

    def __take_special_info(self):
        return (f'Weight: {self.get__weight()}, Speed: {self.get__speed()}, '
                f'Price: {self.get__price()}, Quantity of wheels: {self.get__quantity_of_wheels()}, '
                f'Engine: {self.engine}')
    
    def _start(self):
        print(f'The {self.model} engine begins to work, powered by the {self.engine} engine with {self.get__quantity_of_wheels()} wheels.')

    def _move(self):
        print(f'The {self.model} is moving at {self.get__speed()} km/h.')

    def _stop(self):
        print(f'The {self.model} engine stops.')

# ======Test=====


car = Car(model="Tesla Model X", year=2022, color="Blue", weight=2400, speed=160, price=95000, quantity_of_wheels=4, engine="Gasoline")

print("Initial price:", car.get__price())
car.set__price(100000)
print("Updated price:", car.get__price())
car.set__price(-5000)  

print("\nInitial weight:", car.get__weight())
car.set__weight(2500)
print("Updated weight:", car.get__weight())

print("\nInitial speed:", car.get__speed())
car.set__speed(180)
print("Updated speed:", car.get__speed())
car.set__speed(-10)  


print("\nInitial quantity of wheels:", car.get__quantity_of_wheels())
car.set__quantity_of_wheels(6)
print("Updated quantity of wheels:", car.get__quantity_of_wheels())
car.set__quantity_of_wheels(2)  


print("\nInitial engine type:", car.engine)
car.set__engine("Diesel")
print("Updated engine type:", car.engine)
car.set__engine("Electric") 


print("\nCar actions:")
car._start()
car._move()
car._stop()

print("\nDetailed car information:")
print(car._Car__take_special_info())



    
