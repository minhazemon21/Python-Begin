class vehicle:
    def general_usage(self):
        print("generaluse: transpormation")

class car(vehicle):
    def __init__(self):
        print("I'm  Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")
class MotorCycle(vehicle):
    def __init__(self):
        print("I'm  Motor Cycle")
        self.wheels = 2
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip, racing")

c =car()
c.general_usage()
c.specific_usage()
m = MotorCycle()
m.general_usage()
m.specific_usage()
print(isinstance(c,car))
print(issubclass(car,MotorCycle))