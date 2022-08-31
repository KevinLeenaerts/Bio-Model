from math import ceil

import numpy as np

from Settings import Settings


class DataProcessor:
    def processEatenFoodAndDeaths(eatenFoodPerIteration, deaths):
        foodPerIteration = [
            [],
            [],
            [],
            []         
        ]
        
        deltaPopulation = []
        
        for i, eatenFoodIteration in enumerate(eatenFoodPerIteration):
            foodPerIteration[0].append(eatenFoodIteration[0])  
            foodPerIteration[1].append(eatenFoodIteration[1])   
            foodPerIteration[2].append(eatenFoodIteration[2])
            foodPerIteration[3].append(eatenFoodIteration[3])
            
            deltaPopulation.append(-deaths[i] + eatenFoodIteration[2] + eatenFoodIteration[3])
            
        return foodPerIteration, deltaPopulation
    
    def processSpeeds(percentageSpeedsPerIteration):
        # Sort speed through iterations
        maxSpeed = len(max(percentageSpeedsPerIteration, key=len)); # Since this array consists of sub-arrays ordered by speed, the longest of these subarrays gives us the maximum achieved speed

        seperatedPercentageSpeedPerIteration = []
        
        for speed in range(maxSpeed): # Loops from speeds from 0 to the maximum speed achieved
            speedPerIteration = []
            
            for percentageSpeeds in percentageSpeedsPerIteration:
                if (speed < len(percentageSpeeds)): # If the current iterated speed is available in this iteration
                    speedPerIteration.append(percentageSpeeds[speed]) # Append the amount of this iteration
                else:
                    speedPerIteration.append(0) # Append 0
            
            seperatedPercentageSpeedPerIteration.append(speedPerIteration)    
            
        return seperatedPercentageSpeedPerIteration
 
    def processCoordsPerSpeed(eatenFoodPerIteration):
        coordsPerSpeed = {}
        colorMeshesPerSpeed = {}
        
        for iteration, eatenFoodIteration in enumerate(eatenFoodPerIteration):
            
            if (iteration < ceil(Settings.iterations) - Settings.checkingIterations):
                continue
            
            for eatenFoodFromEntity in eatenFoodIteration:
                for eatenFood in eatenFoodFromEntity:
                    if not eatenFood["speed"] in coordsPerSpeed.keys():
                        coordsPerSpeed[eatenFood["speed"]] = []
                         
                    coordsPerSpeed[eatenFood["speed"]].append((int(eatenFood["x"]), int(eatenFood["y"])))
        
        for speed in coordsPerSpeed.keys():
            for cord in coordsPerSpeed[speed]:
                if not speed in colorMeshesPerSpeed.keys():
                    colorMeshesPerSpeed[speed] = np.zeros((Settings.grid_size, Settings.grid_size))
                
                colorMeshesPerSpeed[speed][cord[1] - 1][cord[0] - 1] += 1; # cords are (x,y) while array needs to be filtered (y,x)
        
        return colorMeshesPerSpeed
        

        