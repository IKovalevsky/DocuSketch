import json
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os


class PlotDrawer:
    def __init__(self):
        self.plot_folder = "plots"
        if not os.path.exists(self.plot_folder):
            os.makedirs(self.plot_folder)

    def draw_plots(self,json_file):
        #Read JSON file into a pandas dataframe
        df = pd.read_json(json_file)
        #Plot comparing different columns
        columns_to_compare = ["gt_corners","rb_corners", "mean", "max", "min"]
        #plot_paths = []
        for column in columns_to_compare:
            plt.figure()
            plt.plot(df[column])
            plt.xlabel("Room")
            plt.ylabel(column)
            plt.title(f"{column} Comparison")
            plt.savefig(os.path.join(self.plot_folder,f"{column}.png"))
            #Return paths to all plots
            plot_paths = [os.path.join(self.plot_folder,f"{column}.png") for column in columns_to_compare]
        return plot_paths
            

json_file = "deviation.json"
plotter = PlotDrawer()
plot_paths = plotter.draw_plots(json_file)
print(plot_paths)