from abc import ABC, abstractmethod, abstractproperty


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @property
    @abstractproperty
    def brand(self):
        pass


class TVControl(RemoteControl):
    def turn_on(self):
        print("Turning on the TV...")
        print("Is on!")

    def turn_off(self):
        print("Turning off the TV...")
        print("Is Off!")

    @property
    def brand(self):
        return "Philco"


class AirConditioningControl(RemoteControl):
    def turn_on(self):
        print("Turning on the Air Conditioning...")
        print("Is on!")

    def turn_off(self):
        print("Turning off the air conditioning...")
        print("Is off!")

    @property
    def brand(self):
        return "LG"


control = TVControl()
control.turn_on()
control.turn_off()
print(control.brand)


control = AirConditioningControl()
control.turn_on()
control.turn_off()
print(control.brand)
