#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:09:51 2018

@author: jorge.gomez
"""

# libraries and data
import matplotlib.pyplot as plt
import pandas as pd


#Defines data file and brings in csv file
data_file = pd.read_csv('MEA_Data_Cortex.csv')
num_trace = int(input("How many traces between 1-4? "))  # how many traces does user want to print out.

# sets up the plot style
plt.style.use('seaborn-darkgrid')
my_dpi = 96
plt.figure(figsize=(480 / my_dpi, 480 / my_dpi), dpi=my_dpi)
plt.figure(1)
# Add title and axis names
plt.title(input("What is the title of the graph? "))
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')

number = 0
for number in range(num_trace):
    if num_trace == 1:  # if you want 1 trace, this code runs.
        trace1 = input('input trace number: ')  # selects the trace to be used between 5-500
        x1 = data_file[f"fastLine{trace1} Time [ms]"]  # defines x
        y1 = data_file[f'fastLine{trace1} Voltage [µV]']  # and y variable.
        plt.plot(x1, y1, label="Trace " + trace1, color='red', linewidth=1.5)  # sets up x and y to be plotted.
        plt.legend()  # sets up figure legend.
        plt.savefig(f'trace_{trace1}.pdf')  # prints out pdf file with the trace numbers
        break
    elif num_trace == 2:
        trace1 = input('input trace number: ')
        trace2 = input('input trace number: ')
        x1 = data_file[f"fastLine{trace1} Time [ms]"]
        y1 = data_file[f'fastLine{trace1} Voltage [µV]']
        x2 = data_file[f"fastLine{trace2} Time [ms]"]
        y2 = data_file[f'fastLine{trace2} Voltage [µV]']
        plt.plot(x1, y1, label="Trace " + trace1, color='red', linewidth=1.5)
        plt.plot(x2, y2, label="Trace " + trace2, color='blue', linewidth=1.5)
        plt.legend()
        plt.savefig(f'trace_{trace1}_{trace2}.pdf')
        break
    elif num_trace == 3:
        trace1 = input('input trace number: ')
        trace2 = input('input trace number: ')
        trace3 = input('input trace number: ')
        x1 = data_file[f"fastLine{trace1} Time [ms]"]
        y1 = data_file[f'fastLine{trace1} Voltage [µV]']
        x2 = data_file[f"fastLine{trace2} Time [ms]"]
        y2 = data_file[f'fastLine{trace2} Voltage [µV]']
        x3 = data_file[f"fastLine{trace3} Time [ms]"]
        y3 = data_file[f'fastLine{trace3} Voltage [µV]']
        plt.plot(x1, y1, label="Trace " + trace1, color='red', linewidth=1.5)
        plt.plot(x2, y2, label="Trace " + trace2, color='blue', linewidth=1.5)
        plt.plot(x3, y3, label="Trace " + trace3, color='green', linewidth=1.5)
        plt.legend()
        plt.savefig(f'trace_{trace1}_{trace2}_{trace3}.pdf')
        break
    else:
        trace1 = input('input trace number: ')
        trace2 = input('input trace number: ')
        trace3 = input('input trace number: ')
        trace4 = input('input trace number: ')
        x1 = data_file[f"fastLine{trace1} Time [ms]"]
        y1 = data_file[f'fastLine{trace1} Voltage [µV]']
        x2 = data_file[f"fastLine{trace2} Time [ms]"]
        y2 = data_file[f'fastLine{trace2} Voltage [µV]']
        x3 = data_file[f"fastLine{trace3} Time [ms]"]
        y3 = data_file[f'fastLine{trace3} Voltage [µV]']
        x4 = data_file[f"fastLine{trace4} Time [ms]"]
        y4 = data_file[f'fastLine{trace4} Voltage [µV]']
        plt.plot(x1, y1, label="Trace " + trace1, color='red', linewidth=1.5)
        plt.plot(x2, y2, label="Trace " + trace2, color='blue', linewidth=1.5)
        plt.plot(x3, y3, label="Trace " + trace3, color='green', linewidth=1.5)
        plt.plot(x4, y4, label="Trace " + trace4, color='black', linewidth=1.5)
        plt.legend()
        plt.savefig(f'trace_{trace1}_{trace2}_{trace3}_{trace4}.pdf')
        break