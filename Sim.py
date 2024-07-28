from Vehicle import *
from Pose import Pose
import numpy as np

TIME_HORIZON = 10
DT = 1

def simulate(vehicle: Vehicle):
    current_time = 0
    pose_list = []
    while current_time < TIME_HORIZON:
        new_pose = vehicle.pose.project(vehicle.velocity, vehicle.acceleration, current_time)
        pose_list.append(new_pose)
        current_time += DT
    return pose_list


def find_slope_intercept(vehicle: Vehicle):
   m = np.tan(vehicle.pose.heading)
   x = vehicle.pose.x
   y = vehicle.pose.y
   b = y - m * x
   return m, b


def find_intersection(m1: float, b1: float, m2: float, b2: float):

  if m1 == m2:
    return None

  x = (b2 - b1) / (m1 - m2)
  y = m1 * x + b1
  return x, y


def find_intersection_vehicles(vehicle_a: Vehicle, vehicle_b: Vehicle):
   m1, b1 = find_slope_intercept(vehicle_a)
   m2, b2 = find_slope_intercept(vehicle_b)
   return find_intersection(m1, b1, m2, b2)


vehicle_a = Vehicle(Pose(0, 0, 0), 1, 0)
vehicle_b = Vehicle(Pose(0, -2, np.pi / 4), 1, 0)


result = find_intersection_vehicles(vehicle_a, vehicle_b)

print(result)