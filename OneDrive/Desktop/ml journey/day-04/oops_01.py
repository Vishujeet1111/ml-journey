class Car:
    def __init__(self,userbrand,usercar):
        self.brand = userbrand
        self.car = usercar

    def full_name(self):
        return f"{self.brand} {self.car} {self.battery_size}"


class ElectricCar(Car):
    def __init__(self,userbrand,usercar,battery_size):
        super().__init__(userbrand,usercar)
        self.battery_size = battery_size

my_new_car = ElectricCar("tata","BEV","85kWh")
print(my_new_car.full_name())

# my_car = Car("toyota","fortuner")
# print(my_car.brand)
# print(my_car.car)
# print(my_car.full_name())