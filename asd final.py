# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 22:16:08 2023

@author: losir
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    """
    Reads a DataFrame from the "global-energy-substitution.csv" file.

    Returns:
        pandas.DataFrame:A DataFrame containing global energy 
        substitution data.

    """
    data = pd.read_csv("global-energy-substitution.csv")
    return data

def plot_line(data_path):

    #line plot
    """
    Create and display a line plot.

    Parameters:
             data_file (Series): The data to be plotted in the line chart.
    """
# Set the figure Size
    plt.figure(figsize=(10, 6))
#Load the Data
    plt.plot(data_path["Year"], data_path["Other_renewables"], \
             label="Other_renewables")
    plt.plot(data_path["Year"], data_path["Biofuels"], label="Biofuels")
    plt.plot(data_path["Year"], data_path["Solar"], label="Solar")
    plt.plot(data_path["Year"], data_path["Wind"], label="Wind")
#Graph the label sand Title
    plt.xlabel("Year")
    plt.ylabel(" Consmption")
    plt.title("Global Energy Substitution")
    plt.legend()


def plot_pie(data_file):
    # Pie Chart
    """

    Create a pie chart for the given data.

    Args:
        data_file (Series): The data to be plotted in the pie chart.
       
     """
    cols = ["Other_renewables", "Hydropower",
        "Nuclear", "Gas", "Coal", "Traditional_biomass"]
    print(data_file.loc[data_file["Year"] == 2022, cols])
# Set the figure
    plt.figure(figsize=(10, 6))
#Graph Pie Chart For 2012 & 2022
    plt.subplot(1, 2, 1)
    plt.pie(data_file.loc[data_file["Year"] == 2012, cols].values.flatten(),
       labels=cols, autopct='%1.0f%%')
    plt.title('2012')
    plt.subplot(1, 2, 2)
    plt.pie(data_file.loc[data_file["Year"] == 2022, cols].values.flatten(),
        labels=cols, autopct='%1.0f%%')
    plt.title('2022')
#Graph the title
    plt.suptitle('Global Energy Resources')


def plot_bar(data_source):
 # Bar Chart
    """
       Create a bar plot for the given data.

       Args:
           data_source (Series): The data to be plotted in the bar chart. 
       """

    cols = ["Other_renewables", "Hydropower",
        "Nuclear", "Gas", "Coal", "Traditional_biomass"]
#Set the Data Figure
    plt.figure(figsize=(10, 6))
    plt.bar(cols, \
            data_source.loc[data_source["Year"]==2022, cols].values.flatten(),\
            label="2022")
#Graph the Label
    plt.xlabel("Global Energy Resources")
    plt.ylabel(" Consumption")
#Graph the title
    plt.title("Energy Resource consumed over the year 2022")
    plt.legend()
#load Data
pd_data = get_data()
plot_line(pd_data)
plot_pie(pd_data)
plot_bar(pd_data)
