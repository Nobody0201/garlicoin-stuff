"""
Module to create graphs from garlicoin balances
"""
from time import strftime
import matplotlib.pyplot as plt
import numpy as np
from checker import VALUE_DICTIONARY, total_value, get_bool

NAMES = [key.capitalize() for key,value in VALUE_DICTIONARY.items() if round(value) > 0]
BALANCES = [value for key,value in VALUE_DICTIONARY.items() if round(value) > 0]
EXPLODE = [0.7 if i<10 else 0 for i in BALANCES]

def save(chart_type):
    if chart_type == "pie":
        plt.savefig("charts/" + input("What file do you want to save to? ")
                    + strftime(" %d.%m.%Y %H %M") +" Pie Chart.png")
    else:
        plt.savefig("charts/" + input("What file do you want to save to? ")
                    + strftime(" %d.%m.%Y %H %M") +"Bar Chart.png")        
        

def pie_chart():
    """Creates a pie chart and saves it to a file"""
    save_as_file = get_bool("Do you want to save as a file? (Y/N) ")

    plt.title("Our total supply is: " + str(round(total_value, 3)))
    plt.pie(BALANCES, explode=EXPLODE, labels=NAMES, autopct=make_autopct(BALANCES))
    plt.axis("equal")
    if save_as_file is True:
        save("pie")
    plt.show()


def bar_chart():
    """Creates a bar chart
    WIP"""
    save_as_file = get_bool("Do you want to save as a file? (Y/N) ")
    range_of_values = np.arange(len(BALANCES))

    plt.title("Our total supply is: " + str(round(total_value, 3)))
    plt.bar(range_of_values, BALANCES)
    plt.xticks(range_of_values, NAMES)
    if save_as_file is True:
        save("bar")
    plt.show()


def make_autopct(sizes):
    """Automatic percentages"""
    def my_autopct(pct):
        """I'm not sure, stackoverflow said to do this"""
        total = sum(sizes)
        val = int(round(pct * total / 100))
        return "{p:.2f}% ({v:d})".format(p=pct, v=val)
    return my_autopct

def main():
    """Runs all the functions"""
    while True:
        chart_type = input("Do you want a bar chart or a pie chart? ").lower()
        if chart_type == "pie":
            pie_chart()
            return
        elif chart_type == 'bar':
            bar_chart()
            return
        else:
            print("Please enter a valid value")
