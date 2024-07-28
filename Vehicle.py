from Pose import Pose

class Vehicle:
    def __init__(self, pose: Pose, velocity: float, acceleration: float):
        self.pose = pose
        self.velocity = velocity
        self.acceleration = acceleration 