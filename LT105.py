class Vehicle:
    licensecode = ""
    serialcode = ""
    def turnOnAirConditioner(self):
        print("Turn on:Air")

class car(Vehicle):
    def sayhello(self):
        print("hello world:car")
class Pickup(Vehicle):
    def sayhello(self):
        print("hello world:Pickup")
class Van(Vehicle):
    def sayhello(self):
        print("hello world:Van")
class EstateCar(Vehicle):
    def sayhello(self):
        print("hello world:EstateCar")
car1=car()
car1.sayhello()

Pickup1=Pickup()
Pickup1.sayhello()

Van1=Van()
Van1.sayhello()

EstateCar1=EstateCar()
EstateCar1.sayhello()