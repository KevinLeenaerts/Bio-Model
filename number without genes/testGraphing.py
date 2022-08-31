from graphing.DataProcessor import DataProcessor
from graphing.Graphs import Graphs
from model.Model import Model

graphs = Graphs();

graphs.show(
    [0, 1, 2, 3],
    [10, 10, 20, 30],
    [0, 10, 10, 20],
    [
        [0.5, 0.25, 0.25, 0.125],
        [0, 0.25, 0.5, 0.3],
        [0.5, 0.25, 0.25, 0.4],
        [0, 0.25, 0, 175]
    ]
)