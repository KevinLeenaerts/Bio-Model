from random import choice, random
from numpy import short
from Settings import Settings
from simulation.entity.AI import AI

class Entity:
    isMoving = True;
    
    speed = None;
    energy = None;
    
    energyLeft = None;
    eatenFood = [];
    
    x = None;
    y = None;
    
    def __init__(self, x, y, speed):
        self.speed = speed;
        self.energyConsumption = speed
        
        self.energy = Settings.standard_energy;
        
        self.x = x;
        self.y = y;
        
    def move(self, foods):        
        vel = AI.getBestStep(self.x, self.y, self.eatenFood, self.energyLeft, self.energyConsumption, foods)
        
        self.x += vel[0];
        self.y += vel[1]
        
        self.energyLeft -= self.energyConsumption;

    def clone(self, iteration):
        speed = self.speed;
        
        if (random() < Settings.mutationChance and iteration >= Settings.allowed_mutation_iteration):
            if (choice([0, 1]) == 0):
                speed -= 1;
            else:
                speed += 1;
                
            if (speed < 1):
                speed = 1;  
                     
        copy = Entity(None, None, speed)
        
        return copy