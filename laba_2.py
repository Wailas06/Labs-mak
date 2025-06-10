from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        print(f"{self.__class__.__name__} is starting to move...")

class Car(Transport):
    def __init__(self, driver_name, destination):
        self.driver_name = driver_name
        self.destination = destination

    def move(self):
        super().move()
        return f"Car driven by {self.driver_name} is heading to {self.destination}"

class Bicycle(Transport):
    def __init__(self, rider_name, destination):
        self.rider_name = rider_name
        self.destination = destination

    def move(self):
        super().move()
        return f"Bicycle ridden by {self.rider_name} is going to {self.destination}"

class ElectricScooter(Transport):
    def __init__(self, user_name, destination):
        self.user_name = user_name
        self.destination = destination

    def move(self):
        super().move()
        return f"Electric scooter used by {self.user_name} is heading to {self.destination}"

class TripLogger:
    def log_trip(self, transport: Transport):
        print(transport.move())

def start_trip():
    car = Car("Alice", "Office")
    bike = Bicycle("Bob", "Park")
    scooter = ElectricScooter("Charlie", "Library")

    logger = TripLogger()
    for vehicle in [car, bike, scooter]:
        logger.log_trip(vehicle)

if __name__ == "__main__":
    start_trip()
