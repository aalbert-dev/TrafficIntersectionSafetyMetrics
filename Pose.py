import numpy as np

class Pose:
    def __init__(self, x: float, y: float, heading: float):
        self.x = x
        self.y = y
        self.heading = heading


    def project(self, velocity: float, acceleration: float, time: float):
        dx = np.cos(self.heading)
        dy = np.sin(self.heading)
        new_x = self.x + (velocity * time + 0.5 * acceleration * time * time) * dx
        new_y = self.y + (velocity * time + 0.5 * acceleration * time * time) * dy
        return Pose(new_x, new_y, self.heading)
    
    def __str__(self) -> str:
        return f'X: {self.x}, Y: {self.y}, Yaw: {self.heading}'
