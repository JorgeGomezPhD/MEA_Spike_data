import matplotlib.pyplot as plt
import pandas as pd

# Defines data file and brings in csv file
data_file = pd.read_csv('MEA_Data_Cortex.csv')
num_trace = int(input("How many traces between 1-4? "))  # how many traces does user want to print out.


def plot_leg():
    plt.legend()  # sets up figure legend.
    plt.show()


def one_trace():
    trace1 = input('input trace number: ')  # selects the trace to be used between 5-500
    x1 = data_file[f"fastLine{trace1} Time [ms]"]  # defines x
    y1 = data_file[f'fastLine{trace1} Voltage [µV]']  # and y variable.
    plt.plot(x1, y1, label="Trace " + trace1, color='red', linewidth=1.5)  # sets up x and y to be plotted.


def two_trace():
    one_trace()
    trace2 = input('input trace number: ')  # selects the trace to be used between 5-500
    x2 = data_file[f"fastLine{trace2} Time [ms]"]
    y2 = data_file[f'fastLine{trace2} Voltage [µV]']
    plt.plot(x2, y2, label="Trace " + trace2, color='blue', linewidth=1.5)


def three_trace():
    two_trace()
    trace3 = input('input trace number: ')
    x3 = data_file[f"fastLine{trace3} Time [ms]"]
    y3 = data_file[f'fastLine{trace3} Voltage [µV]']
    plt.plot(x3, y3, label="Trace " + trace3, color='green', linewidth=1.5)


def four_trace():
    three_trace()
    trace4 = input('input trace number: ')
    x4 = data_file[f"fastLine{trace4} Time [ms]"]
    y4 = data_file[f'fastLine{trace4} Voltage [µV]']
    plt.plot(x4, y4, label="Trace " + trace4, color='black', linewidth=1.5)


number = 0
for number in range(num_trace):
    if num_trace == 1:  # if you want 1 trace, this code runs.
        one_trace()
        break
    elif num_trace == 2:
        two_trace()
        break
    elif num_trace == 3:
        three_trace()
        break
    else:
        four_trace()
        break

# Add title and axis names
plt.title(input("What is the title of the graph? "))
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (µV)')
plt.savefig(f'{input("Name your PDF: ")}.pdf')  # naming pdf
plot_leg()  # shows graph and plots legend
