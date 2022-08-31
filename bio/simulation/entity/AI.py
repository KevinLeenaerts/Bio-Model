from Settings import Settings

class AI:
    def getBestStep(x, y, eatenFood, energyLeft, energyConsumption, foods):
        if len(eatenFood) == 0 and len(foods) > 0:
            closest_food, vel, turns = AI.getDistanceToClosestFood(x, y, foods)  
            
            return vel
          
        if len(eatenFood) >= 1 and len(foods) > 0:           
            total_turns = 0;
            
            closest_food, vel1, turns = AI.getDistanceToClosestFood(x, y, foods)  
            total_turns += turns * energyConsumption;
            
            shortest_distance, vel = AI.getDistanceToEdge(closest_food.x, closest_food.y);
            total_turns += shortest_distance * energyConsumption
            
            if (total_turns <= energyLeft):
                return vel1
            else:          
                shortest_distance, vel = AI.getDistanceToEdge(x, y);    
                return vel
    
        # if len(eatenFood) >= 2 and len(foods) > 0: 
        #     shortest_distance, vel = AI.getDistanceToEdge(x, y);    
        #     return vel 

    
        shortest_distance, vel = AI.getDistanceToEdge(x, y);    
        return vel

    def getDistanceToClosestFood(x, y, foods):
        closest_food = {
            "food": None,
            "dist": 2 * Settings.grid_size + 1
        }
        
        for food in foods: 
            dist = abs(food.x - x) + abs(food.y - y);
            if dist < closest_food["dist"]:
                closest_food = {
                    "food": food,
                    "dist": dist
                }
        
        dx = closest_food["food"].x - x;
        dy = closest_food["food"].y - y
            
        if not dx == 0:           
            vel_x = dx / abs(dx)
        else:
            vel_x = 0 
               
        if not dy == 0:           
            vel_y = dy / abs(dy)
        else:
            vel_y = 0
            
        if dx > dy:
            dist = dy + (dx - dy)
        
        return closest_food["food"], (vel_x, vel_y), max([abs(dx), abs(dy)])
    
    def getDistanceToEdge(x, y):
            dx_0 = x
            dx_1 = Settings.grid_size + 1 - x
                
            dy_0 = y;
            dy_1 = Settings.grid_size + 1 - y
                
            distances = [dx_0, dx_1, dy_0, dy_1]
                
            shortest_distance = min(distances)
                
            return shortest_distance, Settings.directions[distances.index(shortest_distance)]
        