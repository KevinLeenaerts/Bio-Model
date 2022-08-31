from random import choice, random
from numpy import short
from Settings import Settings
from simulation.entity.AI import AI

class Entity:
    isMoving = True;
    
    allels = None;
    
    energy = None;
    
    energyLeft = None;
    eatenFood = [];
    
    x = None;
    y = None;
    
    def __init__(self, allels):
        self.allels = allels;
        
        self.speed = Entity.getSpeed(allels);
        
        self.energyConsumption = self.speed
        
        self.energy = Settings.standard_energy;
        
    def move(self, foods):        
        vel = AI.getBestStep(self.x, self.y, self.eatenFood, self.energyLeft, self.energyConsumption, foods)
        
        self.x += vel[0];
        self.y += vel[1]
        
        self.energyLeft -= self.energyConsumption;
        
    def getSpeed(allels):
        return allels[0] + allels[1] + 1;