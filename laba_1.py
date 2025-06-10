class Vehicle:
    def __init__(self, model, fuel_type):
        self.__model = model
        self.__fuel_type = fuel_type

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement start_engine method")

    def info(self):
        return f"This is a {self.__class__.__name__} model {self.__model}."

    def refuel(self):
        return f"The {self.__class__.__name__} model {self.__model} uses {self.__fuel_type} as fuel."

    def get_model(self):
        return self.__model

    def get_fuel_type(self):
        return self.__fuel_type

    def set_model(self, new_model):
        self.__model = new_model

    def set_fuel_type(self, new_fuel_type):
        self.__fuel_type = new_fuel_type


class Car(Vehicle):
    def start_engine(self):
        return "Car engine started: Врууум!"


class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started: Брррррм!"


class Airplane(Vehicle):
    def start_engine(self):
        return "Airplane engine started: Вжуууууух!"

vehicles = [
    Car("Audi Rs6-etron", "electricity"),
    Motorcycle("Harley Davidson", "gasoline"),
    Airplane("An-225", "jet fuel")
]

for vehicle in vehicles:
    print(vehicle.info())
    print(vehicle.start_engine())
    print(vehicle.refuel())
    print()

print("Changing car model to BMW M5 Competition...")
vehicles[0].set_model("BMW M5 Competition")
print(vehicles[0].info())

print()
print("Changing motorcycle's fuel type to ethanol...")
vehicles[1].set_fuel_type("ethanol")
print(vehicles[1].refuel())
