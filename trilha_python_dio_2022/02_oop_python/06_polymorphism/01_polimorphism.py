class Bird:
    def to_fly(self):
        print("Flying...")

#Pardal
class Sparrow(Bird):
    def to_fly(self):
        print("Sparrow can fly!")

#Avestruz
class Ostrich(Bird):
    def to_fly(self):
        print("Ostrich cannot fly!")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Airplane(Bird):
    def to_fly(self):
        print("Plane is taking off...")


def flight_plan(obj):
    obj.to_fly()


flight_plan(Sparrow())
flight_plan(Ostrich())
flight_plan(Airplane())
