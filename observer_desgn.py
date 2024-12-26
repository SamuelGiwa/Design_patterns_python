class Weatherdisplay:
    def __init__(self,Temp,hum,press):
        self.Temp = Temp
        self.hum = hum
        self.press = press
    def update(self, data):
        print(f"{self.name} received weather update: {data}")
        
class Weatherstation:
    
    def __init__(self):
        self.observer = []
    
    def register(self,observer):
        self.observer.append(observer)
    
    def unregister(self,observer):
        self.observer.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    

        