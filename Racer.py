# Name: Yusra Hassan
# Date: May 17, 2024
# Purpose: OOP and Data structure practice
# Description: A class of Racers, different instances
# Note: children must override's parent's abstract function or else they won't instantiate

from abc import ABC, abstractmethod # abc is a special class to let us have abstract classes in python

class Racer(ABC): # that's why we need to extend it here
    
    def __init__(self, name, speed, medals):
        self.name = name
        self.speed = speed
        self.medals = medals  

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Runner(Racer): # A small number here will definitely mean more since running takes longer
    
    def __init__(self, name, speed, medals, weather):
        super().__init__(name, speed, medals) # Inheritance
        self.weather = weather

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")
        
    def addMedal(self, medal): # encapsulation
        self.medals.append(medal)

class Motorcyclist(Racer): # We'd expect the speed here to be more, also medals could be different
    def __init__(self, name, speed, medals, road_type):
        super().__init__(name, speed, medals)
        self.road_type = road_type
    
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

running = Runner("Ali", 65, [1, 2, 4], 12)
motorcycle = Motorcyclist("Ali", 65, [10, 20, 40], "smooth")
allRacers = [running, motorcycle]

for i in allRacers: # Polymorphism
    i.go()
