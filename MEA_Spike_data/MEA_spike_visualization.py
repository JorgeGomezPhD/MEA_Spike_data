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

#Here you define the trace number with a number between 5 and 500. 
trace1=str(input('input trace number: '))
trace2=str(input('input trace number: '))
trace3=str(input('input trace number: '))
trace4=str(input('input trace number: '))

x1 = data_file['fastLine' + trace1 +" " + 'Time [ms]']
y1 = data_file['fastLine' + trace1 + " "+ 'Voltage [µV]']

x2 = data_file['fastLine' + trace2 +" " + 'Time [ms]']
y2 = data_file['fastLine' + trace2 + " "+ 'Voltage [µV]']

x3 = data_file['fastLine' + trace3 +" " + 'Time [ms]']
y3 = data_file['fastLine' + trace3 + " "+ 'Voltage [µV]']

x4 = data_file['fastLine' + trace4 +" " + 'Time [ms]']
y4 = data_file['fastLine' + trace4 + " "+ 'Voltage [µV]']


#plt.style.use('fivethirtyeight')
plt.style.use('seaborn-darkgrid')
my_dpi=96
plt.figure(figsize=(480/my_dpi, 480/my_dpi), dpi=my_dpi)
plt.figure(1)

#Different traces
plt.plot(x1,y1, label= "Trace " + trace1, color = 'red', linewidth=1.5)
plt.plot(x2,y2, label= "Trace " + trace2, color = 'blue', linewidth=1.5)
plt.plot(x3,y3, label= "Trace " + trace3, color = 'green', linewidth=1.5)
plt.plot(x4,y4, label= "Trace " + trace4, color = 'black', linewidth=1.5)
plt.legend()


# Add title and axis names
plt.title('Single spike from cortical neurons')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')


#prints out pdf file with the trace numbers
plt.savefig("trace" + " " + trace1 +"_" +trace2+"_"+trace3 + "_" +trace4+ '.pdf')