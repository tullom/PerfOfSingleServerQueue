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
    TOTAL_CUSTOMERS = 6
    FRACTION_REJECTED = 7


# Columns: RANDOM_SEED, arrival_rates, utilization, fractionServed, meanNumberInSystem, meanDelay, totalCustomers
def plot(file, xcolumn, ycolumn, xlabel, ylabel, ylimUpper=0, ylimLower=0):
    num_samples = 50
    averages = {}
    with open(file, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y
            else:
                averages[x] = y

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color='g', linestyle='solid', marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if ylimLower != 0 or ylimUpper != 0:
        plt.ylim(ylimUpper, ylimLower)
    plt.grid()
    plt.show()


def plotTwo(file1, file2, xcolumn, ycolumn, xlabel, ylabel, label1, label2, ylimUpper=0, ylimLower=0):
    num_samples = 50
    averages = {}
    with open(file1, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y
            else:
                averages[x] = y

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color='g',
             linestyle='solid', marker='o', label=label1)
    averages = {}
    with open(file2, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x = float(row[xcolumn])
            y = float(row[ycolumn])
            if x in averages:
                averages[x] += y
            else:
                averages[x] = y

    x_output = []
    y_output = []

    for key in averages:
        x_output.append(key)
        y_output.append(averages[key]/num_samples)

    plt.plot(x_output, y_output, color='b',
             linestyle='solid', marker='o', label=label2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if ylimLower != 0 or ylimUpper != 0:
        plt.ylim(ylimUpper, ylimLower)
    plt.grid()
    plt.legend()
    plt.show()


def main():
    # # plot mean delay versus arrival rate
    # plot("data50.txt", Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")
    # plot for question 3
    # plot("experiment8_part3.txt", Param.TOTAL_CUSTOMERS,
    #      Param.MEAN_DELAY, "Number of Customers", "Mean Delay")
    # plot("experiment8_part3_exponential.txt", Param.TOTAL_CUSTOMERS,
    #      Param.MEAN_DELAY, "Number of Customers", "Mean Delay")
    # plot("dataForQ3.txt", Param.TOTAL_CUSTOMERS, Param.FRACTION_SERVED, "Number of Customers", "Fraction Served", 0.0, 1.0)
    # plot("dataForQ3.txt", Param.TOTAL_CUSTOMERS, Param.UTILIZATION, "Number of Customers", "Utilization")
    # #plot for questions 4
    # plotTwo("data50.txt", "data50_service_time30.txt",Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay", "Service = 10", "Service = 30")
    # #plot for question 6
    # plotTwo("data50.txt", "experiment6.txt",Param.ARRIVAL_RATES, Param.MEAN_DELAY, "Arrival Rates", "Mean Delay", "Service = M/D/1", "Service = M/M/1")
    # plot for question 7
    # plot for question 8
    plot("experiment8.txt", Param.ARRIVAL_RATES,
         Param.MEAN_DELAY, "Arrival Rates", "Mean Delay")


if __name__ == '__main__':
    main()
