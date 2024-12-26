from abc import ABC, abstractmethod

# Abstract Vehicle class
class Vehicle(ABC):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Abstract VehicleFactory class
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

# Concrete implementation of VehicleFactory for Cars
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car(name="DefaultCarName")

# Concrete implementation of Vehicle
class Car(Vehicle):
    def __init__(self, name=None):
        super().__init__(name or "UnnamedCar")  # Handle missing names gracefully

    def start(self):
        print(f"{self.name} is starting.")

    def stop(self):
        print(f"{self.name} is stopping.")

# Example usage
if __name__ == "__main__":
    factory = CarFactory()
    car = factory.create_vehicle()
    car.start()
    car.stop()

    # Creating another car with a custom name
    another_car = Car(name="MyCustomCar")
    another_car.start()
    another_car.stop()