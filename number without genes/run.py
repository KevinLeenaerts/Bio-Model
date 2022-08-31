from datetime import datetime
from Settings import Settings
from graphing.DataProcessor import DataProcessor
from graphing.Graphs import Graphs
from model.Model import Model

model = Model();
graphs = Graphs()

iterations = []
populationPerIteration = []
eatenFoodPerIteration = []
deathsPerIteration = []
percentageSpeedsPerIteration = []
eatenFoodInfoPerIteration = []

pastDt = []

pastIteration = datetime.now();

for i in range(Settings.iterations):
    # Calcualte time needed
    now = datetime.now();
    dt = now - pastIteration;
    pastDt.append(dt.total_seconds())
    if (len(pastDt) > 20):
        pastDt.pop(0)
    pastIteration = now;
    avarageDt = 0;
    for dt in pastDt:
        avarageDt += dt;
    avarageDt /= (len(pastDt) + 1);
    
    # Run simulation
    model.runSimulation()
    N, entityCountPerAmountOfFood, died, percentageSpeeds, eatenFoodInfo = model.getInfo();
    model.end(i);
    
    # Keep data
    iterations.append(i) 
    populationPerIteration.append(N)
    eatenFoodPerIteration.append(entityCountPerAmountOfFood)
    deathsPerIteration.append(died)
    percentageSpeedsPerIteration.append(percentageSpeeds)
    eatenFoodInfoPerIteration.append(eatenFoodInfo)

    # Feedback to user
    print("Progress: ", round(i / Settings.iterations * 100), "%, time until completion: ", round(avarageDt * (Settings.iterations - i)), " seconds", end='\r')

foodPerIteration, deltaPopulation = DataProcessor.processEatenFoodAndDeaths(eatenFoodPerIteration, deathsPerIteration);
seperatedPercentageSpeedPerIteration = DataProcessor.processSpeeds(percentageSpeedsPerIteration)
colorMeshesPerSpeed = DataProcessor.processCoordsPerSpeed(eatenFoodInfoPerIteration)

graphs.show(iterations, populationPerIteration, deltaPopulation, seperatedPercentageSpeedPerIteration, colorMeshesPerSpeed)