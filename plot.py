import matplotlib.pyplot as plt 
import csv 

from enum import IntEnum

class Param(IntEnum):
    RANDOM_SEED = 0
    ARRIVAL_RATES = 1
    UTILIZATION = 2
    FRACTION_SERVED = 3
    MEAN_NUMBER_IN_SYSTEM = 4
    MEAN_DELAY = 5
    FRACTION_REJECTED = 6


#Columns: random_values[seed], arrival_rates[rate], utilization, fractionServed, meanNumberInSystem, meanDelay, fractionRejected
def plot(title, file, xcolumn, ycolumn, xlabel, ylabel, ylimUpper=0, ylimLower=0,):
    num_samples = 50
    averages = {}
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y;
            else:
                averages[x] = y;

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color = 'g', linestyle = 'solid', marker = 'o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if ylimLower != 0 or ylimUpper != 0:
        plt.ylim(ylimUpper, ylimLower)
    plt.grid()
    plt.show()

def plotTwo(title, file1, file2, xcolumn, ycolumn, xlabel, ylabel, label1, label2, ylimUpper=0, ylimLower=0):
    num_samples = 50
    averages = {}
    with open(file1, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y;
            else:
                averages[x] = y;

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color = 'g', linestyle = 'solid', marker = 'o', label = label1)
    averages = {}
    with open(file2, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y;
            else:
                averages[x] = y;

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color = 'b', linestyle = 'solid', marker = 'o', label = label2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if ylimLower != 0 or ylimUpper != 0:
        plt.ylim(ylimUpper, ylimLower)
    plt.grid()
    plt.legend()
    plt.title(title)
    plt.show()

def main():
    plt.figure(1)
    # plot mean delay versus arrival rate 
    plot("Queue Size: 10", "experiment7_queue10.txt", Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")
    plot("Queue Size: 100", "experiment7_queue100.txt", Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")
    plot("Queue Size: 1000", "experiment7_queue1000.txt", Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")
    plot("Queue Size: Infinity", "experiment7_queueinf.txt", Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")
    plot("Queue Size: 10", "experiment7_queue10.txt", Param.ARRIVAL_RATES, Param.FRACTION_REJECTED, "Arrival Rates", "Fraction Rejected")
    plot("Queue Size: 100", "experiment7_queue100.txt", Param.ARRIVAL_RATES, Param.FRACTION_REJECTED, "Arrival Rates", "Fraction Rejected")
    plot("Queue Size: 1000", "experiment7_queue1000.txt", Param.ARRIVAL_RATES, Param.FRACTION_REJECTED, "Arrival Rates", "Fraction Rejected")
    plot("Queue Size: Infinity", "experiment7_queueinf.txt", Param.ARRIVAL_RATES, Param.FRACTION_REJECTED, "Arrival Rates", "Fraction Rejected")
if __name__ == '__main__':
    main()

