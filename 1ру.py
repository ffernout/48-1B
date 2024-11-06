# OOП 1: Основы ООП, Создание первых классов,
#Атрибуты и Методы классов, Принцип ООП - Наследование.

class Transport:
    def __init__(self, the_model, the_year, the_color, penalties=0):
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties

    def change_color(self, new_color):
        print(f"color changed from {self.color} to {new_color}")
        self.color = new_color


class plane(Transport):
    def __init__(self, the_model, the_year, the_color, penalties):
        super().__init__(self, the_model, the_year, the_color, penalties)

class Car:
    #конструктор           параметры
    def __init__(self, the_model, the_year, the_color, penalties= 0):
        #атребуты
        self.model = the_model
        self.year = the_year
        self.color = the_color
        self.penalties = penalties

    #метод
    def drive(self, city):
        print(f"Car {self.model} is driving to {city}")

    def signal(self, num_of_times, sound):
        while num_of_times >0:
            print(f'Car {self.model} is signalling: {sound}')
            num_of_times -= 1

    def change_color(self, new_color):
        self.color = new_color

class Truck(Car):
    def __init__(self, the_model, the_year, the_color, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties=0, load_capacity=0)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, product_type):
        if weight > self.load_capacity:
            print(f"вы не можете погрузить больше чем {self.load_capacity} kg.")
        else:
            print(f" вы погрузили {product_type} ({weight} kg.)")


number = 5
my_car = Car("BMW X6", "2023", "Black")
print(my_car)
print(f"model: {my_car.model} year: {my_car.year} color: {my_car.color}" f"Penalties: {my_car.penalties}")

best_car = Car (the_year= 2000, the_color="red", the_model="bmw 5y")

best_car = Car(the_model="honda fit", the_year=2020, the_color="blue", penalties=56)
best_car.penalties = 23
print(f"model: {best_car.model} year: {best_car.year} color: {best_car.color}" f"Penalties: {best_car.penalties}")

best_car = Car(penalties=6, the_model="bmw b4", the_year=2017, the_color="blue")
best_car.color = "Red"
print(f"model: {best_car.model} year: {best_car.year} New color: {best_car.color}")

my_car.drive('Osh')
best_car.drive('Kant')
best_car.drive('Tokmok')
best_car.signal(2,'beeeeep')

my_plane = plane("boeing 747", 2019, 'red')
print(f'model: {my_plane.model} year: {my_plane.year} color: {my_plane.color}')

truck = Truck("volvo 300", 2000, "blue", 30000)
print(f"model: {truck.model}, year: {truck.year}, color: {truck.color}, load_capacity {truck.load_cargo} ")
truck.load_cargo(35000, product_type="apples")
truck.load_cargo(25000,"oranges")
truck.drive("batken")