from math import  floor
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.widgets import Slider, Button

from Settings import Settings

class Graphs:
    def __init__(self):
        self.fig, self.axs = plt.subplots(2, 4);
        
    def show(self, iterations, populationPerIteration, deltaPopulation, seperatedPercentageSpeedPerIteration, colorMeshesPerSpeed):  
        self.axs[0, 0].step(iterations, populationPerIteration, label="population")
        self.axs[0, 0].set_title("N of entities")
        self.axs[0, 0].set_ylim([0, max(populationPerIteration) * 1.1])
        self.axs[0, 0].set_xlim([0, len(iterations) - 1])
        
        self.axs[0, 0].axvline(x=Settings.allowed_mutation_iteration, label="Mutations Allowed", c="black", linestyle="--")
        self.axs[0, 0].legend(loc="lower right")


        self.axs[0, 1].step(iterations, deltaPopulation, label="delta population")
        self.axs[0, 1].set_title("dN of entities")
        extreme = abs(max(deltaPopulation,key=abs)) * 1.1
        self.axs[0, 1].set_ylim([-extreme, extreme])
        self.axs[0, 1].set_xlim([0, len(iterations) - 1])
        
        self.axs[0, 1].axvline(x=Settings.allowed_mutation_iteration, label="Mutations Allowed", c="black", linestyle="--")
        self.axs[0, 1].legend(loc="lower right")


        labels = [*range(len(seperatedPercentageSpeedPerIteration) + 1)]
        labels[0] = None;
        
        self.axs[0, 2].stackplot(iterations, *seperatedPercentageSpeedPerIteration, labels=labels)
        self.axs[0, 2].set_title("speed")
        self.axs[0, 2].set_ylim([0, 1])
        self.axs[0, 2].set_xlim([0, len(iterations) - 1 ])
        
        self.axs[0, 2].axvline(x=Settings.allowed_mutation_iteration, c="black", linestyle="--") # label="Mutations Allowed", 
        self.axs[0, 2].legend(loc="lower left")

        # histogram_speed = []
        # for speed, countedspeeds in enumerate(seperatedPercentageSpeedPerIteration[len(counted_speeds_hist) - 1]):
        #     for i in range(counted_speeds):
        #         histogram_speed.append(speed)
        # self.axs[1,1].hist(histogram_speed)
        
        # coords = {
        #     "x": [],
        #     "y": [],
        # }
        
        for i in range(3):
            mesh = None
            if i < len(colorMeshesPerSpeed):
                mesh = colorMeshesPerSpeed[i + 1]
            else:
                mesh = np.zeros((Settings.grid_size, Settings.grid_size))
            
            self.axs[1, i].pcolormesh(mesh)
            
            # ax = sns.heatmap(mesh, ax=self.axs[1, i], cbar=False)
            # ticks = range(Settings.grid_size)
            # ax.set_xticks(ticks)
            # ax.set_xticklabels(ticks)
            # ax.set_yticks(ticks)
            # ax.set_yticklabels(ticks)
                        
            self.axs[1, i].set_xlim(0, Settings.grid_size)
            self.axs[1, i].set_ylim(Settings.grid_size, 0)
            self.axs[1, i].set_title("Food eaten speed=" + str(i + 1))
            self.axs[1, i].set_aspect('equal')
            
        # Slider ax
        self.axs[1, 3].pcolormesh(colorMeshesPerSpeed[1])
        
        # ax = sns.heatmap(colorMeshesPerSpeed[1], ax=self.axs[1, 3], cbar=False)
        # ticks = range(Settings.grid_size)
        # ax.set_xticks(ticks)
        # ax.set_xticklabels(ticks)
        # ax.set_yticks(ticks)
        # ax.set_yticklabels(ticks)
            
        self.axs[1, 3].set_xlim(0, Settings.grid_size)
        self.axs[1, 3].set_ylim(Settings.grid_size, 0)
        self.axs[1, 3].set_title("Food eaten speed=" + str(1))
        self.axs[1, 3].set_aspect('equal')
            
        slider_ax_bbox = self.axs[1, 3].get_position()
        slider_ax_points = slider_ax_bbox.get_points();
        slider_ax_points[0][1] -= 0.1;
        slider_ax_points[1][1] = slider_ax_points[0][1] + 0.01
        slider_ax_bbox.set_points(slider_ax_points)
        slider_ax = plt.axes(slider_ax_bbox)
 
        # Making slider
        max_speed = len(colorMeshesPerSpeed)
        speedSlider = Slider(
            ax=slider_ax,
            label="Speed",
            valmin=1,
            valmax=max_speed,
            valinit=1,
            valstep=1
        )
        
        speedSlider.on_changed(lambda val: self.update(colorMeshesPerSpeed, val))

        plt.show();
    
    def update(self, colorMeshesPerSpeed, val):
        val = floor(val - 1)
        
        self.axs[1, 3].pcolormesh(colorMeshesPerSpeed[val + 1])
        
        # ax = sns.heatmap(colorMeshesPerSpeed[val + 1], ax=self.axs[1, 3], cbar=False)
        
        self.axs[1, 3].set_title("Food eaten speed=" + str(val + 1))
        self.fig.canvas.draw_idle()
