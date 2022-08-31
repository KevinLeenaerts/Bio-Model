from time import sleep
from simulation.Simulation import Simulation
from draw.UI import UI

class Model:
    simulation = None
    ui = None
    
    def __init__(self):
        # self.ui = UI();
        # self.ui.init()
        
        self.simulation = Simulation();
    
    def runSimulation(self):
        self.simulation.reset();
        
        running = True;
        
        # self.ui.draw(self.simulation)
        # sleep(2)       
         
        while running:
            running = self.simulation.iterate()
            
            # self.ui.draw(self.simulation)
            # sleep(0.7)

    def end(self, iteration):
        self.simulation.eliminateEntities(iteration);
        
    def getInfo(self):
        N = len(self.simulation.entities)
        
        if N == 0:
            print("Extincion!")
            return; 
        
        entityCountPerAmountOfFood = [0, 0, 0, 0] # [0, 1, 2, >=3]
        for entity in self.simulation.entities:
            eaten = len(entity.eatenFood);
            
            if (eaten == 0):
                entityCountPerAmountOfFood[0] += 1;
            
            if (eaten == 1):
                entityCountPerAmountOfFood[1] += 1;
            
            if (eaten == 2):
                entityCountPerAmountOfFood[2] += 1;
                
            elif (eaten >= 2):
                entityCountPerAmountOfFood[3] += 1;
        
        died = 0;
        for entity in self.simulation.entities:
            if Simulation.isOutOfBounds(entity.x, entity.y) == False or len(entity.eatenFood) < 1:
                died += 1;
            
        all_speeds = [] # gather array
        for entity in self.simulation.entities:
            all_speeds.append(entity.speed);
        
        percentageSpeeds = [] # sorted array [0, 1, 2, ...]
        for i in range(max(all_speeds) + 1): # stops at i = max(speeds)
            percentageSpeeds.insert(i, all_speeds.count(i) / len(all_speeds))
            
        eatenFoodInfo = []    
        for entity in self.simulation.entities:
            if Simulation.isOutOfBounds(entity.x, entity.y) == False or len(entity.eatenFood) < 1:
                continue
            eatenFoodInfo.append(entity.eatenFood)
            
        return N, entityCountPerAmountOfFood, died, percentageSpeeds, eatenFoodInfo
        
        