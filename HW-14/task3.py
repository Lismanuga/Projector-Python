class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5

    def display_speed(self):
        return self.speed


my_car = Car("Brand", "Model", 2023)

my_car.accelerate()
print(f"Current Speed: {my_car.display_speed()}")
my_car.brake()
print(f"Current Speed: {my_car.display_speed()}")
my_car.brake()
print(f"Current Speed: {my_car.display_speed()}")
