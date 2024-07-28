from Vehicle import *
from Pose import Pose
import numpy as np
from Viz import Visualizer

TIME_HORIZON = 20
DT = 1

def simulate(vehicle: Vehicle) -> list[Pose]:
    current_time = 0
    pose_list = []
    while current_time < TIME_HORIZON:
        new_pose = vehicle.pose.project(vehicle.velocity, vehicle.acceleration, current_time)
        pose_list.append(new_pose)
        current_time += DT
    return pose_list


def find_slope_intercept(vehicle: Vehicle) -> tuple[float, float]:
    m = np.tan(vehicle.pose.heading)
    x = vehicle.pose.x
    y = vehicle.pose.y
    b = y - m * x
    return m, b


def find_intersection(m1: float, b1: float, m2: float, b2: float) -> Pose:

    if m1 == m2:
        return None

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return Pose(x, y, 0)


def find_linear_intersection_vehicles(vehicle_a: Vehicle, vehicle_b: Vehicle) -> Pose:
    m1, b1 = find_slope_intercept(vehicle_a)
    m2, b2 = find_slope_intercept(vehicle_b)
    return find_intersection(m1, b1, m2, b2)


def find_quadratic_intersection_vehicles(vehicle_a: Vehicle, vehicle_b: Vehicle) -> Pose:
    m1, b1 = find_slope_intercept(vehicle_a)
    m2, b2 = find_slope_intercept(vehicle_b)
    return find_intersection(m1, b1, m2, b2)


def distance(p1: Pose, p2: Pose) -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def convert_poses_to_distance_to_intersection(pose_list: list[Pose], intersection: Pose) -> list[float]:
    return [distance(pose, intersection) for pose in pose_list]

vehicle_a = Vehicle(Pose(0, 0, 0), 1, 0)
vehicle_b = Vehicle(Pose(0, -20, np.pi / 4), 0, 2)


intersection = find_linear_intersection_vehicles(vehicle_a, vehicle_b)

pose_list_a = simulate(vehicle_a)
pose_list_b = simulate(vehicle_b)

distance_list_a = convert_poses_to_distance_to_intersection(pose_list_a, intersection)

distance_list_b = convert_poses_to_distance_to_intersection(pose_list_b, intersection)

time_list = list(np.linspace(0, TIME_HORIZON, int(TIME_HORIZON / DT)))

viz = Visualizer(None)

viz.add_plot(time_list, distance_list_a)
viz.add_plot(time_list, distance_list_b)
viz.display()