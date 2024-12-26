# Observer interface
class Observer:
    def update(self, temperature, humidity, pressure):
        pass

# Subject interface
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

# Concrete Subject
class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notifyObservers()

# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current conditions: {temperature}°C, {humidity}% humidity")

class StatisticsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Statistics updated with temperature: {temperature}°C")

# Example usage
weather_data = WeatherData()
current_display = CurrentConditionsDisplay()
stats_display = StatisticsDisplay()

weather_data.attach(current_display)
weather_data.attach(stats_display)

weather_data.setMeasurements(25, 65, 1013)
weather_data.setMeasurements(30, 70, 1012)
