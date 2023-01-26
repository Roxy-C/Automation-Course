import os
from infrastracture import Infrastracture
from dotenv import load_dotenv

load_dotenv()

class Car:
    logger = Infrastracture()
    fuel_price = int(os.getenv('FUELPRICE'))
    
    def __init__(self):
      # Creates a Car instance, !!! Make sure to drag parms from a file !!!
      
      self.fuel = int(os.getenv('FUEL'))
      self.fuelCap = int(os.getenv('FUELCAP'))
      self.fuelConsumption = float(os.getenv('FUELCONSUMPTION'))
      self.gear = 0 # max 6
      self.velocity = 0
      self.cash = int(os.getenv('CASH')) # for refuling
      self.engineStatus = False
      
        
    def startEngine(self):
        """Ros, 22.01.2023
        Start Engine"""
        
        if (self.engineStatus):
                self.logger.log(os.getenv('START_ENGINE_EX1'))
                raise Exception(os.getenv('START_ENGINE_EX1'))
        
        self.engineStatus = True
        self.logger.log("Car Started")
    
    
    def stopEngine(self):
        """Ros, 22.01.2023
        Stop Engine"""
           
        if not self.engineStatus:
            self.logger.log(os.getenv('STOP_ENGINE_EX1'))
            raise Exception(os.getenv('STOP_ENGINE_EX1'))
        
        if self.velocity > 0:
            self.logger.log(os.getenv('STOP_ENGINE_EX2'))
            raise Exception(os.getenv('STOP_ENGINE_EX2'))
        
        self.engineStatus = False
        self.logger.log(os.getenv('STOP_ENGINE_STATUS'))
   
    
    def drive(self, km, velocity):
        """Ros, 22.01.2023
        Driving method, input num of km to drive and velocity"""
        
        needed_fuel = km * self.fuelConsumption
        
        if self.velocity > 0:
            self.logger.log(os.getenv('DRIVE_EX1'))
            raise Exception(os.getenv('DRIVE_EX1'))
        
        if (needed_fuel > self.fuel):
            self.refuel(needed_fuel)
        
        if (not self.engineStatus):
            self.startEngine()

        self.velocity = velocity
        
        gearIndex = (self.velocity // int(os.getenv('SPEEDPERGEAR'))) + 1
        for _ in range(1, gearIndex):
            self.__shiftUp()
            
        self.fuel -= km * self.fuelConsumption
        self.logger.log('Car has driven {km} in {velocity} km\\h and used {fuelCo} liters'.format(km = km, velocity = velocity, fuelCo = km * self.fuelConsumption))
        
            
    def stop(self):
        """Ros, 22.01.2023
        Stopping method, stops the car, must be driving first"""
        
        if self.velocity == 0:
            self.logger.log(os.getenv('STOP_EX1'))
            raise Exception(os.getenv('STOP_EX1'))
        
        
        self.velocity = 0
        for _ in range(0, self.gear):
            self.__shiftDown()
   
    
    def __shiftUp(self):
        """Ros, 22.01.2023
        Shift gear up method"""
        
        if self.gear < int(os.getenv('MAXGEAR')):
            self.gear += 1
            self.logger.log(os.getenv('SHIFT_UP').format(gear = self.gear))
   
    
    def __shiftDown(self):
        """Ros, 22.01.2023
        Shift gear down method"""
        
        if self.gear > 0:
            self.gear -= 1
            self.logger.log(os.getenv('SHIFT_DOWN').format(gear = self.gear))

    
    def refuel(self, fuel_liters):
            """Ros, 22.01.2023
            Refueling method, can't refuel while engine on, neither can you overfuel or get into debt"""
            
            free_fuel = self.fuelCap - self.fuel
            
            if (self.engineStatus or self.velocity > 0):
                self.logger.log(os.getenv('REFUEL_EX1'))
                raise Exception(os.getenv('REFUEL_EX1'))
            
            if (fuel_liters * self.fuel_price > self.cash):
                self.logger.log(os.getenv('REFUEL_EX2'))
                raise ValueError(os.getenv('REFUEL_EX2'))
            
            if (fuel_liters > self.fuelCap - self.fuel):
                self.logger.log(os.getenv('REFUEL_EX3'.format(free_fuel)))
                raise ValueError(os.getenv('REFUEL_EX3').format(free_fuel))

            self.fuel += fuel_liters
            self.cash -= fuel_liters * self.fuel_price
            self.logger.log(os.getenv('REFUEL_PRINT_STATUS').format(fuel = self.fuel, cash = self.cash))
            