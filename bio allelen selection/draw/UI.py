import pygame

from Settings import Settings

screen_size = 800;

class UI:
    screen = None;
    font = None;
    
    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode([screen_size, screen_size])
        pygame.font.init()
        self.font = pygame.font.SysFont('Calibri bold', 25)
        
    def draw(self, simulation):
        self.screen.fill((255, 255, 255))
        cellSize = screen_size / (Settings.grid_size + 2);
    
        # Draw grid
        offset = (screen_size - (cellSize * Settings.grid_size)) / 2;
        for x in range(Settings.grid_size):
            for y in range(Settings.grid_size):
                pygame.draw.rect(self.screen, (100, 100, 100), pygame.Rect(x *  cellSize + offset, y * cellSize + offset, cellSize, cellSize), 2)
        
        # Draw entities
        for entity in simulation.entities:
            eatenColorSpace = 100;
            
            eatenColor = len(entity.eatenFood) / 2 * eatenColorSpace;
            
            if (eatenColor > eatenColorSpace):
                eatenColor = eatenColorSpace
                       
            pygame.draw.circle(self.screen, (255 - eatenColorSpace + eatenColor, 0, 0), (entity.x * cellSize + 0.5 * cellSize, entity.y * cellSize + 0.5 * cellSize), cellSize / 2.5)
            self.printStats(entity, cellSize)
            
        for food in simulation.foods:
            pygame.draw.circle(self.screen, (0, 100, 100), (food.x * cellSize + 0.5 * cellSize, food.y * cellSize + 0.5 * cellSize), cellSize / 4)
               
        pygame.display.flip();
        
    def printStats(self, entity, cellSize):
        stats = {
            "Speed": entity.speed,
            "Food": len(entity.eatenFood),
            "Energyleft": entity.energyLeft
        }
        
        for i, key in enumerate(stats.keys()):
            text = self.font.render(str(key) + ": " + str(stats[key]), False, (0, 0, 0));
            pos = (entity.x + Settings.textOffset) * cellSize, (entity.y - Settings.textOffset) * cellSize + i * 20
            self.screen.blit(text, pos)