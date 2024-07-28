import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, vehicles):
        self.vehicles = vehicles


    def add_plot(self, time_list, distance_list):
        plt.plot(time_list, distance_list, 'r--')

    def display(self):
        plt.axhline(0,color='black')
        plt.axis((-20, 20, -20, 20))
        plt.show()
