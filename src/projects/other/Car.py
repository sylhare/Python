class Car:
    """ Car """

    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        """ say state """
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        """ accelerate """
        self.speed += 5

    def brake(self):
        """" brake """
        self.speed -= 5

    def step(self):
        """ step """
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        """ average speed """
        return self.odometer / self.time


def drive():
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()


if __name__ == '__main__':
    drive()
