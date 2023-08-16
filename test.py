class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def get_speed(self):
        return self.speed

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        if self.speed - speed_decrease >= 0:
            self.speed -= speed_decrease

def play_game():
    car = Car("Toyota", "Camry", 2022, 0)
    print("You are driving a", car.year, car.make, car.model)
    while True:
        print("Current speed:", car.get_speed(), "mph")
        action = input("What would you like to do? (accelerate, brake, quit): ")
        if action == "accelerate":
            speed_increase = int(input("By how many mph would you like to accelerate? "))
            car.accelerate(speed_increase)
        elif action == "brake":
            speed_decrease = int(input("By how many mph would you like to brake? "))
            car.brake(speed_decrease)
        elif action == "quit":
            print("Thanks for playing!")
            break

play_game()