from random import choice, randint

from simulation.Food import Food
from Settings import Settings
from simulation.entity.Entity import Entity

class Simulation:
    entities = []
    foods = []
    
    def __init__(self):
        for i in range(Settings.starting_entity_amount):
            self.entities.append(Entity(None, None, Settings.standard_speed))
           
    def spreadEntitiesEdge(self):
        for entity in self.entities:
            if choice([0, 1]) == 0:
                x = randint(0, Settings.grid_size + 1)
                y = choice([0, Settings.grid_size + 1])
            else:
                y = randint(0, Settings.grid_size + 1)
                x = choice([0, Settings.grid_size + 1])
                
            entity.x = x;
            entity.y = y;
    
    def spreadEntitiesField(self):
        for entity in self.entities:
            overlapsFood = True;
            while overlapsFood:
                entity.x = randint(1, Settings.grid_size)
                entity.y = randint(1, Settings.grid_size)
                
                overlapsFood = False;
                for food in self.foods:
                    if food.x == entity.x and food.y == entity.y:
                        overlapsFood = True;
                        break;
                
            
            
    def reset(self):
        for entity in self.entities:
            entity.isMoving = True;
            entity.energyLeft = entity.energy   
            entity.eatenFood = [];
        
        self.foods = [];       
        for i in range(Settings.food_spawns):
            self.foods.append(Food(randint(1, Settings.grid_size), randint(1, Settings.grid_size)))
            
        self.spreadEntitiesField();  
        
        
            
    def iterate(self):
        anytingStillMoving = False;
        
        for entity in self.entities:
            if entity.isMoving == False:
                continue
            
            for i in range(int(entity.speed)):
                if not entity.isMoving:
                    continue;
                
                entity.move(self.foods);
                
                entity.isMoving = not (Simulation.isOutOfBounds(entity.x, entity.y) or entity.energyLeft <= 0);
                
                for food in self.foods:
                    if entity.x == food.x and entity.y == food.y:
                        entity.eatenFood.append(
                            {
                                "x": entity.x,
                                "y": entity.y,
                                "speed": entity.speed
                            }
                        )
                        self.foods.remove(food)
                        

            
            if entity.isMoving:
                anytingStillMoving = True;
                continue
                
        return anytingStillMoving
            
    def eliminateEntities(self, iteration):
        for entity in reversed(self.entities):
            if Simulation.isOutOfBounds(entity.x, entity.y) == False or len(entity.eatenFood) < 1:
                self.entities.remove(entity)
                continue
            
            if len(entity.eatenFood) >= 2:
                self.entities.append(entity.clone(iteration))
                continue
    
    def isOutOfBounds(x, y):
        return (x <= 0 or x >= Settings.grid_size + 1 or y <= 0 or y >= Settings.grid_size + 1)

            
            
