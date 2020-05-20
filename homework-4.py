class Car:
    def __init__(self, color, name):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False
        self.direction = None

    def show_speed(self):
        print(self.speed)

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("OverSpeed!")
        super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("OverSpeed!")
        super().show_speed()

class PoliceCar(Car):
    def __init__(self, *args, **kwargs):
        super(PoliceCar, self).__init__(*args, **kwargs)
        self.is_police = True

class SportCar(Car):
    pass

print("Car")
car = Car('Red', "Cool")
car.go(10)
car.show_speed()
car.stop()
car.show_speed()
car.turn("Bridge")
print(car.direction)
print("Is police", car.is_police)

print("TownCar")
car = TownCar('Red', "Cool")
car.go(100)
car.show_speed()
car.stop()
car.show_speed()
car.turn("Bridge")
print(car.direction)
print("Is police", car.is_police)

print("WorkCar")
car = WorkCar('Red', "Cool")
car.go(100)
car.show_speed()
car.stop()
car.show_speed()
car.turn("Bridge")
print(car.direction)
print("Is police", car.is_police)

print("PoliceCar")
car = PoliceCar('Red', "Cool")
car.go(100)
car.show_speed()
car.stop()
car.show_speed()
car.turn("Bridge")
print(car.direction)
print("Is police", car.is_police)

print("SportCar")
car = SportCar('Red', "Cool")
car.go(100)
car.show_speed()
car.stop()
car.show_speed()
car.turn("Bridge")
print(car.direction)
print("Is police", car.is_police)
