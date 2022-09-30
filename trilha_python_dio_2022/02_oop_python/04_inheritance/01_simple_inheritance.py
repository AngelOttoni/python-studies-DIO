class Vehicle:
    def __init__(self, color, license_plate, number_wheels):
        self.color = color
        self.license_plate = license_plate 
        self.number_wheels = number_wheels

    def start_engine(self):
        print("Starting the engine")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])}"


class Motorcycle(Vehicle):
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, color, license_plate, number_wheels, loaded):
        super().__init__(color, license_plate, number_wheels)
        self.loaded = loaded

    def is_loaded(self):
        print(f"{'Yes' if self.loaded else 'No'} I'm loaded")


motorcycle = Motorcycle("black", "abc-1234", 2)
motorcycle.start_engine()

car = Car("white", "xde-0098", 4)
car.start_engine()

truck = Truck("purple", "gfd-8712", 8, True)
truck.start_engine()
print("")

print(f"Morocycle description: Color - {motorcycle.color}, License Plate - {motorcycle.license_plate}, Number of wheels - {motorcycle.number_wheels}.")
print("")

print(f"Car description: Color - {car.color}, License Plate - {car.license_plate}, Number of wheels - {car.number_wheels}.")
print("")

print(f"Truck description: Color - {truck.color}, License Plate - {truck.license_plate}, Number of wheels - {truck.number_wheels}, Loaded - {truck.loaded}.")
